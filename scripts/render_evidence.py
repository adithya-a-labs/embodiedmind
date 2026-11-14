"""Reproduce representative saved trajectories without running inference."""

import argparse
import json
from pathlib import Path

from PIL import Image

from embodiedmind.environments.dynamic_world import DYNAMIC_ENV_ID, InterventionConfig, make_dynamic_environment
from embodiedmind.environments.factory import make_environment
from embodiedmind.experiments.schedule import atomic_json, digest, load_json


def render_episode(job_dir, summary, settings, out):
    job = summary
    if job["environment"] == DYNAMIC_ENV_ID:
        config = InterventionConfig(**settings["limits"]["dynamics"])
        env = make_dynamic_environment(job["intervention"], render_mode="rgb_array", config=config)
    else:
        env = make_environment(job["environment"], render_mode="rgb_array")
    steps = [json.loads(row) for row in (job_dir / "trajectory.jsonl").read_text().splitlines()]
    frames = []

    def frame():
        image = Image.fromarray(env.render())
        image.thumbnail((420, 420))
        frames.append(image)

    try:
        reset, _ = env.reset(seed=job["seed"])
        if reset["mission"] != job["mission"]:
            raise ValueError("replay mission does not match the run")
        frame()
        for row in steps:
            _, reward, terminated, truncated, _ = env.step(row["executed_action"])
            if (reward, terminated, truncated) != (row["reward"], row["terminated"], row["truncated"]):
                raise ValueError("replay terminal behavior differs from the stored trajectory")
            frame()
        if list(getattr(env, "intervention_log", ())) and json.loads(json.dumps(env.intervention_log)) != load_json(
            job_dir / "evaluator.json"
        )["events"]:
            raise ValueError("replay intervention log differs")
    finally:
        env.close()
    out.mkdir(parents=True, exist_ok=True)
    frames[0].save(out / "step-000-start.png")
    frames[-1].save(out / f"step-{len(steps):03}-finish.png")
    for event in load_json(job_dir / "evaluator.json")["events"]:
        index = event["step"]
        if event["applied"] and index < len(frames):
            for i, suffix in ((index - 1, "before"), (index, "after")):
                frames[i].save(out / f"step-{i:03}-{suffix}-{event['intervention']}.png")
            break
    frames[0].save(out / "replay.gif", save_all=True, append_images=frames[1:], duration=210, loop=0)
    atomic_json(out / "source.json", {"run_id": job_dir.parent.parent.name, "episode": job["id"],
                                     "trajectory_sha256": digest(job_dir / "trajectory.jsonl")})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("run_dirs", nargs="+", type=Path)
    args = parser.parse_args()
    for run in args.run_dirs:
        manifest = load_json(run / "manifest.json")
        selected = {}
        for job in manifest["jobs"]:
            root = run / "episodes" / job["id"]
            if not (root / "summary.json").is_file():
                continue
            result = load_json(root / "summary.json")
            key = (job["environment"], job["intervention"], result["success"],
                   result.get("intervention_applied", False))
            selected.setdefault(key, (root, result))
        for root, result in selected.values():
            render_episode(root, result, manifest["settings"], args.output / run.name / result["id"])


if __name__ == "__main__":
    main()
