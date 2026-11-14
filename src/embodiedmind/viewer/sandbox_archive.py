"""Save exploratory episodes in the same durable format as recorded runs."""

import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from importlib.metadata import version
from uuid import uuid4

from embodiedmind.experiments.archive import package_run


def save_sandbox(output, job, limits, variant, branch, steps, states, frames, done, model_info):
    timestamp = datetime.now(timezone.utc)
    name = f"sandbox-{timestamp:%Y%m%dT%H%M%SZ}-{uuid4().hex[:8]}"
    root = output / name
    episode = root / "episodes" / "exploration"
    episode.mkdir(parents=True)
    job = {**job, "variant": variant, "id": "exploration", "replicate": 0}
    config = json.dumps({"job": job, "limits": limits, "branch": branch}, sort_keys=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

    def write(directory, file, content):
        (directory / file).write_text(json.dumps(content, indent=2) + "\n", encoding="utf-8")

    write(root, "manifest.json", {
        "split": "sandbox", "commit": commit, "jobs": [job], "settings": {"limits": limits},
        "created": timestamp.isoformat(), "branch": branch, "command": "POST /api/sandbox",
        "config_sha256": hashlib.sha256(config.encode()).hexdigest(),
        "python": platform.python_version(), "minigrid": version("minigrid"),
        "gymnasium": version("gymnasium"), "model": model_info,
    })
    for filename, rows in (("trajectory.jsonl", steps), ("evaluator-steps.jsonl", states)):
        (episode / filename).write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    write(episode, "evaluator.json", {"events": states[-1]["interventions"]})
    reward = sum(row["reward"] for row in steps)
    write(episode, "summary.json", {
        **job, "steps": len(steps), "status": "completed", "mission": steps[0]["observation"]["mission"],
        "success": reward > 0, "outcome": "success" if reward > 0 else "ended" if done else "sandbox_snapshot",
        "reward": reward, "calls": sum(row["request"] is not None for row in steps),
    })
    write(root, "invocation.json", {"status": "snapshot_saved", "created": timestamp.isoformat(),
                                   "seed": job["seed"], "recorded_actions": len(steps)})
    (episode / "frames").mkdir()
    for step, frame in enumerate(frames):
        frame.save(episode / "frames" / f"{step:06}.png")
    package_run(root)
    return name
