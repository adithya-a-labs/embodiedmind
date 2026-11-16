"""Serve recorded evaluator context and isolated sandbox simulations."""

import json
import os
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path

import yaml
from PIL import Image

from embodiedmind.agents import VARIANTS, make_agent
from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.dynamic_world import DYNAMIC_ENV_ID, INTERVENTIONS
from embodiedmind.environments.factory import OFFICIAL_ENVIRONMENTS
from embodiedmind.environments.visual_state import board_snapshot, viewer_environment
from embodiedmind.reasoning.action_validator import ACTION_NAMES
from embodiedmind.reasoning.grounding import CONTROLLER_DECISION, action_request, resolve_response
from embodiedmind.reasoning.llm_client import Ollama
from embodiedmind.viewer.sandbox_archive import save_sandbox
MAX_ACTIONS = 256


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def event_from_trace(row):
    prompt = (row.get("request") or {}).get("prompt", "")
    return {
        "action": row["executed_action"], "moved": row["moved"], "reward": row["reward"],
        "decision": row["decision"], "prompt": prompt,
        "hint": next((line for line in prompt.splitlines()
                      if line.startswith(("Route to visible objective", "No visible route"))), ""),
        "scripted": row["scripted_prefix"], "facts": row["memory"].get("selected_facts", []),
        "revisions": row["memory"].get("revisions", []),
        "inference_seconds": row["inference_seconds"],
        "planning": row.get("planning"), "subgoal": row["memory"].get("subgoal"),
    }


def public_json(observation):
    return json.loads(json.dumps(asdict(observation)))


def live_status(heartbeat):
    status = heartbeat.get("status")
    if status == "running":
        try:
            updated = datetime.fromisoformat(heartbeat["at"])
            if datetime.now(timezone.utc) - updated > timedelta(seconds=45):
                return "stalled"
        except (KeyError, ValueError, TypeError):
            return "stalled"
    return status


class ViewerData:
    def __init__(self, runs, sandbox_output, models, workflows=None):
        self.runs = {"": runs.resolve()} if runs is not None else {
            "": Path("results/runs").resolve(), "outputs/": Path("outputs").resolve(),
        }
        self.sandbox_output = sandbox_output.resolve()
        self.models = models
        self.workflows = workflows

    def catalog(self, *, include_coverage=False):
        runs = []
        for prefix, root in self.runs.items():
            for path in sorted(root.glob("**/manifest.json")):
                heartbeat = self.heartbeat(path.parent)
                manifest = read_json(path)
                run = {
                    "id": prefix + path.parent.relative_to(root).as_posix(), "split": manifest["split"],
                    "status": live_status(heartbeat),
                }
                if include_coverage:
                    coverage = {}
                    for job in self.completed_jobs(path.parent, manifest):
                        coverage.setdefault(job["environment"], set()).add(job["variant"])
                    run["coverage"] = {env: sorted(variants) for env, variants in coverage.items()}
                runs.append(run)
        return runs

    @staticmethod
    def heartbeat(root):
        try:
            return read_json(root / "heartbeat.json")
        except FileNotFoundError:
            return {}

    def run_path(self, run):
        prefix = "outputs/" if "outputs/" in self.runs and run.startswith("outputs/") else ""
        base = self.runs[prefix]
        root = (base / run.removeprefix(prefix)).resolve()
        if not root.is_relative_to(base) or not (root / "manifest.json").is_file():
            raise FileNotFoundError("Run manifest unavailable.")
        return root

    def jobs(self, run):
        root = self.run_path(run)
        return self.completed_jobs(root, read_json(root / "manifest.json"))

    @staticmethod
    def completed_jobs(root, manifest):
        return [job for job in manifest.get("jobs", [])
                if (root / "episodes" / job["id"] / "summary.json").is_file()]

    def source(self, run, job_id):
        root = self.run_path(run)
        manifest = read_json(root / "manifest.json")
        job = next((row for row in manifest["jobs"] if row["id"] == job_id), None)
        if job is None or Path(job_id).name != job_id:
            raise FileNotFoundError("Unknown episode.")
        path = root / "episodes" / job_id
        summary = read_json(path / "summary.json")
        rows = [json.loads(line) for line in (path / "trajectory.jsonl").read_text(encoding="utf-8").splitlines()]
        if not rows or len(rows) != summary["steps"]:
            raise ValueError("Saved trajectory is incomplete.")
        return job, manifest["settings"]["limits"], summary, rows, read_json(path / "evaluator.json")

    @lru_cache(maxsize=16)
    def replay(self, run, job_id):
        job, limits, summary, rows, evaluator = self.source(run, job_id)
        env = viewer_environment(job, limits)
        try:
            controller = PrimitiveController(env)
            observation = controller.reset(job["seed"])
            frames = []
            for index, row in enumerate(rows):
                if row["step"] != index or public_json(observation) != row["observation"]:
                    raise ValueError(f"Reconstructed observation diverges at action {index + 1}.")
                frames.append({"board": board_snapshot(env), "observation": row["observation"],
                               "event": event_from_trace(row)})
                result = controller.step(row["executed_action"])
                if (result.reward, result.terminated, result.truncated, result.moved) != (
                    row["reward"], row["terminated"], row["truncated"], row["moved"],
                ):
                    raise ValueError(f"Reconstructed outcome diverges at action {index + 1}.")
                observation = result.observation
            if "next_observation" in rows[-1] and public_json(observation) != rows[-1]["next_observation"]:
                raise ValueError("Reconstructed final observation diverges.")
            events = json.loads(json.dumps(getattr(env, "intervention_log", [])))
            if events != evaluator["events"]:
                raise ValueError("Reconstructed interventions diverge.")
            frames.append({"board": board_snapshot(env), "observation": asdict(observation), "event": None})
            return {"summary": summary, "frames": frames, "interventions": events}
        finally:
            env.close()

    def live(self, run):
        root = self.run_path(run)
        heartbeat = self.heartbeat(root)
        snapshots = sorted((root / "live").glob("*.json"), key=lambda file: file.stat().st_mtime_ns, reverse=True)
        selected = [file for file in snapshots if file.stem in heartbeat.get("active", [])] or snapshots[:1]
        return {"heartbeat": heartbeat, "status": live_status(heartbeat),
                "snapshots": [read_json(file) for file in selected]}

    def sandbox(self, body):
        if not isinstance(body, dict):
            raise ValueError("Expected a sandbox request object.")
        variant, actions = body.get("variant", "B0"), body.get("actions", [])
        if variant not in VARIANTS or not isinstance(actions, list) or len(actions) > MAX_ACTIONS:
            raise ValueError("Invalid sandbox variant or action history.")
        if any(type(action) is not int or action not in range(len(ACTION_NAMES)) for action in actions):
            raise ValueError("Invalid sandbox action.")
        branch = body.get("branch")
        if branch is not None:
            if not isinstance(branch, dict):
                raise ValueError("Expected a replay branch.")
            run, job_id, step = branch["run"], branch["job"], branch["step"]
            job, limits, _, rows, _ = self.source(run, job_id)
            if type(step) is not int or not 0 <= step < len(rows):
                raise ValueError("Choose a replay action before the episode ends.")
            self.replay(run, job_id)
            prefix = [row["executed_action"] for row in rows[:step]]
        else:
            seed = body["seed"]
            environment, intervention = body["environment"], body.get("intervention", "no_change")
            if type(seed) is not int or not 0 <= seed <= 2**31 - 1:
                raise ValueError("Enter a seed from 0 to 2,147,483,647.")
            if environment not in (*OFFICIAL_ENVIRONMENTS, DYNAMIC_ENV_ID) or intervention not in INTERVENTIONS:
                raise ValueError("Choose an available environment and intervention.")
            job = {"environment": environment, "seed": seed,
                   "intervention": intervention if environment == DYNAMIC_ENV_ID else "none"}
            limits = {"memory_bytes": 768, "dynamics": {"step": 2, "dropout_until": 9, "dropout_probability": 0.25}}
            prefix = [0, 0] if environment == DYNAMIC_ENV_ID else []
        env = viewer_environment(job, limits, render_mode="rgb_array" if body.get("save") is True else None)
        try:
            return self._play(env, job, limits, prefix, actions, variant, branch, body)
        finally:
            env.close()

    def _play(self, env, job, limits, prefix, actions, variant, branch, body):
        if body.get("save") is True and (body.get("agent_step") is True or not prefix and not actions):
            raise ValueError("Apply at least one action before saving the sandbox.")
        workflows = limits.get("workflows")
        if variant == "B6" and not workflows:
            if self.workflows is None or not self.workflows.is_file():
                raise ValueError("B6 needs a verified workflow library. Set --workflows when starting the viewer.")
            workflows = read_json(self.workflows)
        controller, agent = PrimitiveController(env), make_agent(variant, workflows or ())
        observation = controller.reset(job["seed"])
        previous = moved = result = decision = None
        records, states, frames = [], [], []
        saving = body.get("save") is True
        model_record = None
        supplied = body.get("model_steps", [])
        if not isinstance(supplied, list) or len(supplied) > len(actions):
            raise ValueError("Invalid sandbox model history.")
        model_steps = {}
        for item in supplied:
            offset = item["offset"]
            if type(offset) is not int or not 0 <= offset < len(actions) or item["executed_action"] != actions[offset]:
                raise ValueError("Sandbox model history does not match the executed actions.")
            model_steps[offset] = item

        def capture(step):
            if saving:
                states.append({"step": step, "board": board_snapshot(env),
                               "interventions": list(getattr(env, "intervention_log", ()))})
                frames.append(Image.fromarray(env.render()))

        capture(0)
        for index, action in enumerate(prefix + actions):
            if result and (result.terminated or result.truncated):
                raise ValueError("The sandbox episode has already ended.")
            agent.observe(observation, index, previous, moved)
            before = observation
            result = controller.step(action)
            previous, moved, observation = action, result.moved, result.observation
            if saving:
                record = {
                    "step": index, "observation": asdict(before), "next_observation": asdict(observation),
                    "executed_action": action, "moved": moved, "reward": result.reward,
                    "terminated": result.terminated, "truncated": result.truncated,
                    "scripted_prefix": index < len(prefix), "inference_seconds": 0,
                    "decision": {"action": action, "evidence": "", "source": "reconstructed"},
                    "memory": agent.audit(), "request": None, "response": {},
                }
                if evidence := model_steps.get(index - len(prefix)):
                    for name in ("request", "response", "memory", "decision", "planning", "inference_seconds"):
                        record[name] = evidence[name]
                records.append(record)
            capture(index + 1)
        done = bool(result and (result.terminated or result.truncated))
        if body.get("agent_step") is True:
            if done or len(actions) >= MAX_ACTIONS:
                raise ValueError("Start a new sandbox episode before asking the agent to move.")
            index = len(prefix) + len(actions)
            agent.observe(observation, index, previous, moved)
            if getattr(agent, "use_model", True):
                model_values = yaml.safe_load(self.models.read_text(encoding="utf-8"))
                model_values.pop("temperature")
                model_values["endpoint"] = os.environ.get("OLLAMA_HOST", model_values["endpoint"])
                model = Ollama(**model_values)
                model_info = model.verify()
                context = agent.context(observation, limits["memory_bytes"])
                request = action_request(model, observation, context, (job["seed"] * 1000 + index) % (2**31),
                                         variant, agent.audit()["selected_facts"])
                raw, elapsed = model.generate(request)
                response = raw["response"]
            else:
                request, raw, elapsed, model_info = None, {}, 0.0, {"mode": "controller_only"}
                response = CONTROLLER_DECISION
            resolved = resolve_response(response, observation, agent, variant)
            selected = resolved.proposed
            result = controller.step(resolved.action)
            observation = result.observation
            actions = actions + [resolved.action]
            decision = {**asdict(selected), "action": resolved.action, "proposed_action": selected.action,
                        "inference_seconds": elapsed, "subgoal": agent.audit().get("subgoal"),
                        "planning": {"goal": resolved.goal, "reason": resolved.reason, "route": resolved.route}}
            model_record = {"offset": len(actions) - 1, "executed_action": resolved.action,
                            "request": request, "response": raw, "memory": agent.audit(),
                            "decision": asdict(selected), "planning": decision["planning"],
                            "inference_seconds": elapsed, "model": model_info, "variant": variant}
            done = result.terminated or result.truncated
        state = {"board": board_snapshot(env), "observation": asdict(observation),
                 "step": len(prefix) + len(actions), "actions": actions, "done": done,
                 "reward": result.reward if result else 0, "moved": result.moved if result else None,
                 "decision": decision, "model_record": model_record}
        if saving:
            state["saved"] = save_sandbox(self.sandbox_output, job, limits, variant, branch,
                                          records, states, frames, done,
                                          [item["model"] for item in model_steps.values()])
        return state
