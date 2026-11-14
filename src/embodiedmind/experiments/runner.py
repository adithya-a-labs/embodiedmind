"""Execute a single seeded episode and write a private replayable trace."""

import json
from contextlib import ExitStack
from dataclasses import asdict
from pathlib import Path
from time import time_ns

from PIL import Image

from embodiedmind.agents import make_agent
from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.factory import make_environment
from embodiedmind.environments.visual_state import board_snapshot
from embodiedmind.memory.episodic import Event
from embodiedmind.memory.spatial import Odometry
from embodiedmind.reasoning.action_validator import ActionDecision, parse_action
from embodiedmind.reasoning.prompts import SYSTEM, prompt_for


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
        return _run_episode(env, make_agent(job["variant"]), job, limits, model, path, keep_visuals, monitor)
    finally:
        env.close()


def _run_episode(env, agent, job, limits, model, path, keep_visuals, monitor=None):
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
            request = None if scripted else model.request(
                SYSTEM, prompt_for(observation, context), job["seed"] * 1000 + index,
            )
            write_event(events, {
                "phase": "before_action", "step": index, "at_ns": time_ns(),
                "observation": asdict(observation), "memory": audit, "request": request,
            })
            if scripted:
                request, raw, elapsed = None, {}, 0.0
                decision = ActionDecision(prefix[index], "", True)
            else:
                publish("thinking", index, observation, last_action)
                raw, elapsed = model.generate(request)
                write_event(events, {"phase": "model_response", "step": index, "at_ns": time_ns(),
                                     "response": raw, "inference_seconds": elapsed})
                decision = parse_action(raw["response"])
                calls += 1
            if raw.get("done_reason") == "length" and not decision.valid:
                audit = {**audit, "generation_hit_output_limit": True}
            refs = {item["id"]: item for item in audit.get("selected_facts", [])}
            scoring_odometry.update(Event(index, observation, previous_action, moved))
            visible = {
                (scoring_odometry.segment, scoring_odometry.locate(cell.forward, cell.right)):
                    (cell.object, cell.color, cell.state)
                for cell in observation.cells
            }
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
                                 "decision": asdict(decision)})
            result = controller.step(decision.action)
            last_action = {
                **asdict(decision), "moved": result.moved, "reward": result.reward,
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
                "executed_action": decision.action, "moved": result.moved,
                "unsupported_reference": unsupported_reference, "stale_reference": stale_reference,
                "reward": result.reward, "terminated": result.terminated, "truncated": result.truncated,
            })
            capture(evaluator, index + 1)
            publish("acted", index + 1, result.observation, last_action)
            if hasattr(agent, "record_decision"):
                agent.record_decision(decision.action)
            prompt_tokens += int(raw.get("prompt_eval_count") or 0)
            completion_tokens += int(raw.get("eval_count") or 0)
            invalid += not decision.valid
            unsupported += unsupported_reference
            stale += stale_reference
            inference_seconds += elapsed
            observation, moved = result.observation, result.moved
            previous_action = decision.action
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
        "post_contradiction_recovered": None if contradicted_at is None else recovered_at is not None,
        "steps_to_recovery": recovered_at, "reward": reward,
        "intervention_applied": any(event.get("applied") is True for event in interventions),
    }
