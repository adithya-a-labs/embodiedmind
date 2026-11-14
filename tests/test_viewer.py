import json

import pytest

from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.visual_state import viewer_environment
from embodiedmind.viewer.data import ViewerData, public_json
from embodiedmind.viewer.server import viewer_origins


def test_private_tunnel_allows_only_the_configured_https_origin():
    url = "https://viewer-8765.usw2.devtunnels.ms"
    origins = viewer_origins(8765, url + "/")
    assert origins["http://localhost:8765"] == {"localhost:8765"}
    assert origins[url] == {"localhost:8765", "127.0.0.1:8765", "viewer-8765.usw2.devtunnels.ms"}
    assert "https://other.devtunnels.ms" not in origins
    with pytest.raises(ValueError):
        viewer_origins(8765, url + ".example.org")


def test_replay_reconstructs_view_and_sandbox_forks_without_changing_trace(tmp_path):
    runs = tmp_path / "runs"
    run = runs / "static"
    job = {"id": "sample", "environment": "MiniGrid-DoorKey-8x8-v0", "seed": 1015,
           "variant": "B2", "intervention": "none", "replicate": 0}
    path = run / "episodes" / job["id"]
    path.mkdir(parents=True)
    limits = {"memory_bytes": 768}
    (run / "manifest.json").write_text(json.dumps({
        "split": "static", "jobs": [job], "settings": {"limits": limits},
    }))
    env = viewer_environment(job, limits)
    controller = PrimitiveController(env)
    initial = controller.reset(job["seed"])
    result = controller.step(0)
    try:
        row = {
            "step": 0, "executed_action": 0, "observation": public_json(initial),
            "next_observation": public_json(result.observation), "moved": result.moved,
            "reward": result.reward, "terminated": result.terminated, "truncated": result.truncated,
            "scripted_prefix": False, "decision": {"evidence": "visible"}, "memory": {},
            "request": {"prompt": "Route to visible objective, next suggested action: 0."},
            "inference_seconds": 0.1,
        }
    finally:
        env.close()
    trace = path / "trajectory.jsonl"
    trace.write_text(json.dumps(row))
    (path / "summary.json").write_text(json.dumps({"steps": 1, **job}))
    (path / "evaluator.json").write_text('{"events":[]}')
    data = ViewerData(runs, tmp_path / "sandbox", tmp_path / "models.yaml")

    replay = data.replay("static", job["id"])
    assert replay["frames"][0]["event"]["action"] == 0
    assert replay["frames"][0]["observation"] == row["observation"]
    assert replay["frames"][1]["event"] is None
    state = data.sandbox({"branch": {"run": "static", "job": job["id"], "step": 0},
                          "actions": [1], "save": True})
    assert state["observation"]["direction"] == (initial.direction + 1) % 4
    assert trace.read_text() == json.dumps(row)
    archive = tmp_path / "sandbox" / state["saved"]
    saved = json.loads((archive / "manifest.json").read_text())
    assert saved["split"] == "sandbox"
    assert (archive / "report" / "artifact-index.json").is_file()


def test_live_snapshot_uses_active_job(tmp_path):
    run = tmp_path / "example"
    live = run / "live"
    live.mkdir(parents=True)
    (run / "manifest.json").write_text("{}")
    (run / "heartbeat.json").write_text('{"active":["active"],"completed":1}')
    (live / "active.json").write_text('{"phase":"thinking","step":7}')
    (live / "finished.json").write_text('{"phase":"finished","step":20}')
    data = ViewerData(tmp_path, tmp_path / "sandbox", tmp_path / "models.yaml")
    assert data.live("example")["snapshots"] == [{"phase": "thinking", "step": 7}]
