"""Extract transferable DoorKey routines from successful development traces."""

import hashlib
import json


def learn_doorkey(run, output):
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    if manifest["split"] not in {"pilot", "dev", "development", "smoke", "integration"}:
        raise ValueError("Workflow learning requires a development archive.")
    sources = []
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
            sources.append({"job": job["id"], "seed": job["seed"],
                            "trajectory_sha256": hashlib.sha256(raw).hexdigest()})
    if not sources:
        raise ValueError("No successful development episode demonstrated key pickup, unlock, and goal.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump([{
            "task": "doorkey", "source": run.name,
            "source_commit": manifest["commit"], "episodes": sources,
            "steps": {
                "Find key": "Approach a matching key; pick it up and confirm it is carried.",
                "Find and cross door": "With the key, face the locked door and toggle. Confirm open before crossing.",
                "Reach goal": "Use the observed opening and approach the green goal. Replan if blocked.",
            },
        }], stream, indent=2)
        stream.write("\n")
