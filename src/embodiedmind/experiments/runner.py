"""Execute a single seeded episode and write a private replayable trace."""

import json
from dataclasses import asdict
from pathlib import Path

from PIL import Image

from embodiedmind.agents import make_agent
from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.factory import make_environment
from embodiedmind.memory.episodic import Event
from embodiedmind.memory.spatial import Odometry
from embodiedmind.reasoning.action_validator import ActionDecision, parse_action
from embodiedmind.reasoning.prompts import SYSTEM, prompt_for


def write_event(stream, value):
    stream.write(json.dumps(value, ensure_ascii=True, separators=(",", ":")) + "\n")
    stream.flush()


def episode(job, limits, model, path: Path, keep_visuals=False):
    if job["intervention"] != "none" or job["environment"].startswith("EmbodiedMind-"):
        from embodiedmind.environments.dynamic_world import InterventionConfig, make_dynamic_environment

        dynamics = InterventionConfig(**limits.get("dynamics", {}))
        env = make_dynamic_environment(
            job["intervention"], render_mode="rgb_array" if keep_visuals else None, config=dynamics,
        )
    else:
        env = make_environment(job["environment"], render_mode="rgb_array" if keep_visuals else None)
    try:
        return _run_episode(env, make_agent(job["variant"]), job, limits, model, path, keep_visuals)
    finally:
        env.close()


def _run_episode(env, agent, job, limits, model, path, keep_visuals):
    controller = PrimitiveController(env)
    initial = controller.reset(job["seed"])
    observation = initial
    frames = []
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

    def frame():
        if keep_visuals:
            pixels = env.render()
            if pixels is not None:
                image = Image.fromarray(pixels)
                image.thumbnail((360, 360))
                frames.append(image)

    frame()
    with (path / "trajectory.jsonl").open("w", encoding="utf-8") as trace:
        for index in range(min(limits["max_steps"], limits["max_calls"] + len(prefix))):
            agent.observe(observation, index, previous_action, moved)
            context = agent.context(observation, limits["memory_bytes"])
            audit = agent.audit()
            scripted = index < len(prefix)
            if scripted:
                request, raw, elapsed = None, {}, 0.0
                decision = ActionDecision(prefix[index], "", True)
            else:
                request = model.request(SYSTEM, prompt_for(observation, context), job["seed"] * 1000 + index)
                raw, elapsed = model.generate(request)
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
            result = controller.step(decision.action)
            write_event(trace, {
                "step": index, "observation": asdict(observation),
                "next_observation": asdict(result.observation), "memory": audit,
                "request": request, "response": raw, "inference_seconds": elapsed,
                "decision": asdict(decision), "scripted_prefix": scripted,
                "executed_action": decision.action, "moved": result.moved,
                "unsupported_reference": unsupported_reference, "stale_reference": stale_reference,
                "reward": result.reward, "terminated": result.terminated, "truncated": result.truncated,
            })
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
            frame()
            if terminated or truncated:
                if reward > 0 and contradicted_at is not None:
                    recovered_at = index - contradicted_at
                break
    steps = index + 1
    if frames:
        frames[0].save(path / "start.png")
        frames[-1].save(path / "finish.png")
        frames[0].save(path / "replay.gif", save_all=True, append_images=frames[1:], duration=210, loop=0)
    interventions = list(getattr(env, "intervention_log", ()))
    with (path / "evaluator.json").open("w", encoding="utf-8") as private_data:
        json.dump({"events": interventions, "terminated": terminated, "truncated": truncated}, private_data)
    success = reward > 0 and bool(terminated)
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
