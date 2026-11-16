"""Execute a single seeded episode and write a private replayable trace."""

import json
from contextlib import ExitStack
from dataclasses import asdict
from pathlib import Path
from time import monotonic, time_ns

from PIL import Image

from embodiedmind.agents import make_agent
from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.factory import make_environment
from embodiedmind.environments.observation_adapter import front_move_outcome
from embodiedmind.environments.visual_state import board_snapshot
from embodiedmind.memory.episodic import Event
from embodiedmind.memory.spatial import Odometry
from embodiedmind.reasoning.action_validator import ActionDecision
from embodiedmind.reasoning.grounding import CONTROLLER_DECISION, Resolution, action_request, resolve_response


def write_event(stream, value):
    stream.write(json.dumps(value, ensure_ascii=True, separators=(",", ":")) + "\n")
    stream.flush()


def episode(job, limits, model, path: Path, keep_visuals=True, monitor=None):
    if job["intervention"] != "none" or job["environment"].startswith("EmbodiedMind-"):
        from embodiedmind.environments.dynamic_world import InterventionConfig, make_dynamic_environment

        dynamics = InterventionConfig(**limits.get("dynamics", {}))
        env = make_dynamic_environment(
            job["intervention"], render_mode="rgb_array" if keep_visuals else None, config=dynamics,
        )
    else:
        env = make_environment(job["environment"], render_mode="rgb_array" if keep_visuals else None)
    try:
        agent = make_agent(job["variant"], limits.get("workflows", ()))
        return _run_episode(env, agent, job, limits, model, path, keep_visuals, monitor)
    finally:
        env.close()


def _run_episode(env, agent, job, limits, model, path, keep_visuals, monitor=None):
    start_time = monotonic()
    use_model = getattr(agent, "use_model", True)
    controller = PrimitiveController(env)
    initial = controller.reset(job["seed"])
    observation = initial
    previous_action = moved = None
    calls = prompt_tokens = completion_tokens = invalid = unsupported = stale = 0
    prefix = limits.get("scripted_prefix", [])
    inference_seconds = reward = 0.0
    terminated = truncated = False
    contradicted_at = None
    recovered_at = None
    seen_facts = {}
    last_view = {}
    invalidated = {}
    scoring_odometry = Odometry()
    last_action = None
    blocked_proposals = blocked_actions = verification_requests = 0
    checked_old_target = found_new_target = None
    verification_actions = informative_checks = stale_commitments = 0
    target_cells = set()
    target_type = observation.mission.split()[-1]
    target_color = observation.mission.split()[-2]

    def publish(phase, step, observation, decision=None):
        if monitor is not None:
            monitor({
                "phase": phase, "step": step, "observation": asdict(observation),
                "board": board_snapshot(env), "decision": decision,
            })

    def capture(evaluator, step):
        write_event(evaluator, {
            "step": step, "board": board_snapshot(env),
            "interventions": list(getattr(env, "intervention_log", ())),
        })
        if keep_visuals:
            image = env.render()
            if image is not None:
                target = path / "frames" / f"{step:06}.png"
                temporary = target.with_suffix(".tmp")
                Image.fromarray(image).save(temporary, format="PNG")
                temporary.replace(target)

    if keep_visuals:
        (path / "frames").mkdir()
    with ExitStack() as stack:
        def stream(name):
            return stack.enter_context((path / name).open("w", encoding="utf-8"))

        trace = stream("trajectory.jsonl")
        events = stream("step-events.jsonl")
        evaluator = stream("evaluator-steps.jsonl")
        write_event(events, {"phase": "reset", "at_ns": time_ns(), "observation": asdict(initial)})
        capture(evaluator, 0)
        publish("started", 0, initial)
        for index in range(min(limits["max_steps"], limits["max_calls"] + len(prefix))):
            agent.observe(observation, index, previous_action, moved)
            context = agent.context(observation, limits["memory_bytes"])
            audit = agent.audit()
            scripted = index < len(prefix)
            request = None if scripted or not use_model else action_request(
                model, observation, context, job["seed"] * 1000 + index, job["variant"],
                audit.get("selected_facts", ()),
            )
            write_event(events, {
                "phase": "before_action", "step": index, "at_ns": time_ns(),
                "observation": asdict(observation), "memory": audit, "request": request,
            })
            if scripted:
                request, raw, elapsed = None, {}, 0.0
                resolved = Resolution(ActionDecision(prefix[index], "", True), prefix[index])
            elif not use_model:
                raw, elapsed = {}, 0.0
                resolved = resolve_response(CONTROLLER_DECISION, observation, agent, job["variant"])
            else:
                publish("thinking", index, observation, last_action)
                raw, elapsed = model.generate(request)
                write_event(events, {"phase": "model_response", "step": index, "at_ns": time_ns(),
                                     "response": raw, "inference_seconds": elapsed})
                resolved = resolve_response(raw["response"], observation, agent, job["variant"])
                calls += 1
            decision = resolved.proposed
            executed = resolved.action
            planning = {"goal": resolved.goal, "reason": resolved.reason, "route": resolved.route}
            if hasattr(agent, "verification"):
                audit = agent.audit()
                focus = audit.get("verification", {}).get("target") or audit.get("task_target")
                purpose = ("verify" if resolved.reason == "verify_remembered_target" else
                           "act_on_target" if resolved.reason == "route_to_mission_target" else "other")
                planning.update(purpose=purpose, target=focus, model_call=request is not None)
            blocked_proposals += (
                not scripted and decision.valid and resolved.goal == "primitive"
                and decision.action == 2 and front_move_outcome(observation) is False
            )
            verification_requests += resolved.goal == "verify" and decision.valid
            if raw.get("done_reason") == "length" and not decision.valid:
                audit = {**audit, "generation_hit_output_limit": True}
            refs = {item["id"]: item for item in audit.get("selected_facts", [])}
            scoring_odometry.update(Event(index, observation, previous_action, moved))
            visible = {
                (scoring_odometry.segment, scoring_odometry.locate(cell.forward, cell.right)):
                    (cell.object, cell.color, cell.state)
                for cell in observation.cells
            }
            if job["intervention"] == "relocation":
                matching = {cell for cell, appearance in visible.items()
                            if appearance[:2] == (target_type, target_color)}
                applied = next((row for row in getattr(env, "intervention_log", ())
                                if row.get("intervention") == "relocation" and row.get("applied")), None)
                if applied:
                    if checked_old_target is None and any(
                        cell in visible and cell not in matching for cell in target_cells
                    ):
                        checked_old_target = index
                    if found_new_target is None and matching - target_cells:
                        found_new_target = index
                else:
                    target_cells.update(matching)
                if checked_old_target is not None and purpose_is_stale(planning, target_cells):
                    stale_commitments += 1
            if contradicted_at is None and any(
                previous[0] in {"ball", "key", "box", "door"} and visible.get(cell, previous) != previous
                for cell, previous in last_view.items()
            ):
                contradicted_at = index
            last_view.update(visible)
            seen_facts.update((key, value) for key, value in refs.items() if "position" in value)
            for ref, fact in seen_facts.items():
                appearance = (fact["object"], fact["color"], fact["state"])
                cell = (fact["segment"], tuple(fact["position"]))
                if visible.get(cell, appearance) != appearance or fact.get("status") == "CONTRADICTED":
                    invalidated[ref] = index
                elif fact["last_verified_step"] > invalidated.get(ref, index):
                    invalidated.pop(ref)
            unsupported_reference = (
                not scripted and decision.valid and decision.evidence not in {"visible", "explore"}
                and decision.evidence not in refs
            )
            stale_reference = decision.valid and decision.evidence in invalidated
            write_event(events, {"phase": "decision", "step": index, "at_ns": time_ns(),
                                 "decision": asdict(decision), "planning": planning,
                                 "executed_action": executed})
            result = controller.step(executed)
            if planning.get("purpose") == "verify":
                verification_actions += 1
                fact = planning["target"]
                after_pose = Odometry(scoring_odometry.position, scoring_odometry.direction, scoring_odometry.segment)
                after_pose.update(Event(index + 1, result.observation, executed, result.moved))
                if after_pose.segment == fact["segment"] and any(
                    after_pose.locate(cell.forward, cell.right) == tuple(fact["position"])
                    for cell in result.observation.cells
                ):
                    informative_checks += 1
            blocked_actions += result.moved is False
            last_action = {
                **asdict(decision), "action": executed, "proposed_action": decision.action,
                "planning": planning, "subgoal": audit.get("subgoal"),
                "moved": result.moved, "reward": result.reward,
                "terminated": result.terminated, "truncated": result.truncated,
                "inference_seconds": elapsed,
            }
            if monitor is not None and request:
                last_action["hint"] = next((line for line in request["prompt"].splitlines()
                                            if line.startswith(("Route to visible objective", "No visible route"))), "")
            write_event(trace, {
                "step": index, "at_ns": time_ns(), "observation": asdict(observation),
                "next_observation": asdict(result.observation), "memory": audit,
                "request": request, "response": raw, "inference_seconds": elapsed,
                "decision": asdict(decision), "scripted_prefix": scripted,
                "executed_action": executed, "planning": planning, "moved": result.moved,
                "unsupported_reference": unsupported_reference, "stale_reference": stale_reference,
                "reward": result.reward, "terminated": result.terminated, "truncated": result.truncated,
            })
            capture(evaluator, index + 1)
            publish("acted", index + 1, result.observation, last_action)
            if hasattr(agent, "record_decision"):
                agent.record_decision(executed)
            prompt_tokens += int(raw.get("prompt_eval_count") or 0)
            completion_tokens += int(raw.get("eval_count") or 0)
            invalid += not decision.valid
            unsupported += unsupported_reference
            stale += stale_reference
            inference_seconds += elapsed
            observation, moved = result.observation, result.moved
            previous_action = executed
            reward += float(result.reward)
            terminated, truncated = result.terminated, result.truncated
            if terminated or truncated:
                if reward > 0 and contradicted_at is not None:
                    recovered_at = index - contradicted_at
                break
    steps = index + 1
    interventions = list(getattr(env, "intervention_log", ()))
    with (path / "evaluator.json").open("w", encoding="utf-8") as private_data:
        json.dump({"events": interventions, "terminated": terminated, "truncated": truncated}, private_data)
    success = reward > 0 and bool(terminated)
    publish("finished", steps, observation, {**last_action, "success": success})
    return {
        **job, "status": "completed", "mission": initial.mission, "success": success,
        "outcome": "success" if success else ("terminated_failure" if terminated else
                    "environment_timeout" if truncated else "budget_timeout"),
        "steps": steps, "calls": calls, "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens, "inference_seconds": inference_seconds,
        "invalid_actions": invalid, "unsupported_claims": unsupported, "stale_actions": stale,
        "blocked_proposals": blocked_proposals, "blocked_actions": blocked_actions,
        "verification_requests": verification_requests,
        "verification_actions": verification_actions, "informative_checks": informative_checks,
        "stale_commitments": stale_commitments if hasattr(agent, "verification") else None,
        "reacquired": found_new_target is not None if job["intervention"] == "relocation" else None,
        "episode_wall_seconds": monotonic() - start_time,
        "old_target_rechecked_step": checked_old_target, "new_target_seen_step": found_new_target,
        "post_contradiction_recovered": None if contradicted_at is None else recovered_at is not None,
        "steps_to_recovery": recovered_at, "reward": reward,
        "intervention_applied": any(event.get("applied") is True for event in interventions),
    }


def purpose_is_stale(planning, old_cells):
    target = planning.get("target")
    return (planning.get("purpose") == "act_on_target" and target
            and (target["segment"], tuple(target["position"])) in old_cells)
