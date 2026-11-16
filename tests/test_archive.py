import json
from pathlib import Path

from embodiedmind.experiments import schedule
from embodiedmind.experiments.archive import package_run
from embodiedmind.reasoning.llm_client import InferenceUnavailable


def test_retry_preserves_failed_request_and_packages_every_attempt(tmp_path, monkeypatch):
    class Model:
        requests = 0

        def request(self, system, prompt, seed):
            return {"system": system, "prompt": prompt, "seed": seed}

        def generate(self, request):
            self.requests += 1
            if self.requests == 1:
                raise InferenceUnavailable("test connection loss")
            return {"response": '{"action":1,"evidence":"explore"}'}, 0.1

    root = tmp_path / "run"
    (root / "episodes").mkdir(parents=True)
    job = {"id": "episode", "environment": "MiniGrid-DoorKey-8x8-v0",
           "seed": 1015, "variant": "B0", "intervention": "none", "replicate": 0}
    limits = {"max_steps": 1, "max_calls": 1, "memory_bytes": 768, "infrastructure_retries": 1}
    manifest = {"split": "smoke", "lock_sha256": "test", "jobs": [job]}
    (root / "manifest.json").write_text(json.dumps(manifest))
    monkeypatch.setattr(schedule.time, "sleep", lambda _: None)

    result = schedule.execute(root, job, limits, Model(), True)
    assert result["success"] is False
    assert schedule.complete(root / "episodes", job["id"])
    failed, = (root / "attempts" / job["id"]).iterdir()
    episode = root / "episodes" / job["id"]
    assert "test connection loss" in (failed / "error.json").read_text()
    assert "before_action" in (failed / "step-events.jsonl").read_text()
    assert (failed / "trajectory.jsonl").read_text() == ""
    assert (episode / "evaluator-steps.jsonl").read_text().count("\n") == 2

    report = package_run(root)
    assert report.is_file()
    for folder in (failed, episode):
        assert (folder / "start.png").is_file()
        assert (folder / "replay.gif").is_file()
        assert (folder / "artifact-status.json").is_file()
    coverage = json.loads((report.parent / "coverage.json").read_text())
    assert coverage["valid"] == 1 and coverage["attempt_records"] == 2
    index = json.loads((report.parent / "artifact-index.json").read_text())
    assert any(Path(item["path"]).name == "error.json" for item in index["files"])
    assert schedule.complete(root / "episodes", job["id"])
