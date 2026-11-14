"""Package durable episode evidence into reports and visuals without inference."""

import csv
import json
from pathlib import Path

from PIL import Image

from embodiedmind.analysis.report import generate_report


def package_episode(directory):
    status = {"missing": {}}
    trace = directory / "trajectory.jsonl"
    count = 0
    if trace.is_file():
        with trace.open(encoding="utf-8") as source, (directory / "steps.csv").open(
            "w", encoding="utf-8", newline="",
        ) as output:
            fields = ("step", "action", "evidence", "moved", "reward", "terminated", "truncated",
                      "prompt_tokens", "completion_tokens", "inference_seconds")
            writer = csv.DictWriter(output, fieldnames=fields)
            writer.writeheader()
            for line in source:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    status["missing"]["steps"] = "Unreadable trajectory line. Raw bytes preserved."
                    break
                response = row["response"] or {}
                writer.writerow({
                    **{name: row.get(name) for name in fields if name in row},
                    "action": row["executed_action"], "evidence": row["decision"]["evidence"],
                    "prompt_tokens": response.get("prompt_eval_count"),
                    "completion_tokens": response.get("eval_count"),
                })
                count += 1
    if count == 0:
        status["missing"].setdefault("steps", "No completed action was recorded.")
    status["recorded_steps"] = count
    error = directory / "error.json"
    summary = directory / "summary.json"
    status["status"] = ("finalized" if summary.is_file() else
                        "failed" if error.is_file() else "interrupted")

    frames = sorted((directory / "frames").glob("*.png"))
    if frames:
        with Image.open(frames[0]) as first, Image.open(frames[-1]) as last:
            first.save(directory / "start.png")
            last.save(directory / "finish.png")
            first.save(directory / "replay.gif", save_all=True, duration=210, loop=0,
                       append_images=(load_frame(path) for path in frames[1:]))
        status["recorded_frames"] = len(frames)
        if len(frames) < count + 1:
            status["missing"]["frames"] = "Replay covers only the frames captured before interruption."
    elif not (directory / "replay.gif").is_file():
        status["missing"]["visuals"] = "No rendered frames were captured by this attempt."
    if not (directory / "summary.json").is_file():
        status["missing"]["summary"] = "Attempt did not finalize an episode result."
    for name in ("step-events.jsonl", "evaluator-steps.jsonl"):
        if not (directory / name).is_file():
            status["missing"][name] = "This attempt did not capture this stream."
    for name in ("stdout.log", "stderr.log"):
        if not (directory / name).is_file():
            status["missing"][name] = "The runner does not redirect process-wide streams into per-attempt files."
    (directory / "artifact-status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")


def load_frame(path):
    with Image.open(path) as image:
        return image.copy()


def package_run(root: Path):
    if not (root / "manifest.json").is_file():
        raise FileNotFoundError(f"Run manifest unavailable in {root}")
    episode_dirs = sorted((root / "episodes").glob("*"))
    attempts = sorted((root / "attempts").glob("*/*"))
    for directory in episode_dirs + attempts:
        if directory.is_dir():
            package_episode(directory)
    return generate_report(root)
