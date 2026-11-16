"""Extract transferable DoorKey routines from successful development traces."""

import hashlib
import json
from collections import Counter

HANDWRITTEN = {
    "task": "doorkey", "source": "handwritten",
    "steps": {
        "Find key": "Find the key and pick it up.",
        "Find and cross door": "Find the locked door, toggle it and cross.",
        "Reach goal": "Navigate to the green goal.",
    },
}


def learn_doorkey(run, output):
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    if manifest["split"] not in {"pilot", "dev", "development", "smoke", "integration"}:
        raise ValueError("Workflow learning requires a development archive.")
    sources = []
    outcomes = Counter()
    for job in manifest["jobs"]:
        if job["environment"] != "MiniGrid-DoorKey-8x8-v0":
            continue
        episode = run / "episodes" / job["id"]
        if not (episode / "summary.json").is_file():
            continue
        result = json.loads((episode / "summary.json").read_text(encoding="utf-8"))
        if not result["success"]:
            continue
        raw = (episode / "trajectory.jsonl").read_bytes()
        rows = [json.loads(line) for line in raw.splitlines()]
        pickups = [row["step"] for row in rows if row["executed_action"] == 3
                   and (row["next_observation"].get("carrying") or {}).get("object") == "key"]
        opens = [row["step"] for row in rows if row["executed_action"] == 5
                 and any(cell["object"] == "door" and cell["state"] == "open"
                         for cell in row["next_observation"]["cells"])
                 and any(cell["object"] == "door" and cell["state"] == "locked"
                         for cell in row["observation"]["cells"])]
        if pickups and opens and pickups[0] < opens[0] and rows[-1]["reward"] > 0:
            following = rows[opens[0] + 1:]
            outcomes["advance_after_unlock"] += bool(following and following[0]["executed_action"] == 2
                                                      and following[0]["moved"] is True)
            outcomes["goal_visible_after_unlock"] += any(
                cell["object"] == "goal" for cell in rows[opens[0]]["next_observation"]["cells"]
            )
            sources.append({"job": job["id"], "seed": job["seed"],
                            "pickup_step": pickups[0], "unlock_step": opens[0],
                            "trajectory_sha256": hashlib.sha256(raw).hexdigest()})
    if not sources:
        raise ValueError("No successful development episode demonstrated key pickup, unlock, and goal.")
    output.parent.mkdir(parents=True, exist_ok=True)
    cross = "Step through the open doorway if the tile ahead is traversable." if (
        outcomes["advance_after_unlock"] * 2 >= len(sources)
    ) else "Recheck orientation and route toward the opening after unlocking."
    goal = "Route toward the visible green goal." if (
        outcomes["goal_visible_after_unlock"] * 2 >= len(sources)
    ) else "Look for the green goal beyond the doorway, then approach it."
    with output.open("x", encoding="utf-8") as stream:
        json.dump([{
            "task": "doorkey", "source": run.name,
            "source_commit": manifest["commit"], "episodes": sources,
            "observed_outcomes": dict(outcomes),
            "steps": {
                "Find key": "Approach a matching key; pick it up and confirm it is carried.",
                "Find and cross door": f"With the key, face the locked door and toggle. {cross}",
                "Reach goal": goal,
            },
        }], stream, indent=2)
        stream.write("\n")
