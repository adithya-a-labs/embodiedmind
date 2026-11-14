import hashlib
import json

import pytest

from embodiedmind.analysis.report import evaluate, generate_combined_report, load_run
from embodiedmind.analysis.statistics import compare


def _job(seed, variant, replicate=0):
    return {
        "id": f"{seed}-{variant}-{replicate}",
        "environment": "MiniGrid-Fixture-v0",
        "seed": seed,
        "variant": variant,
        "intervention": "none",
        "replicate": replicate,
    }


def _manifest(run, jobs, split="static"):
    run.mkdir()
    (run / "manifest.json").write_text(json.dumps({"run_id": run.name, "split": split, "jobs": jobs}))


def _episode(run, job, summary, trace='{"event":"step"}' + "\n"):
    episode = run / "episodes" / job["id"]
    episode.mkdir(parents=True)
    (episode / "summary.json").write_text(json.dumps(summary))
    if trace is not None:
        (episode / "trajectory.jsonl").write_text(trace)
    return episode


def test_coverage_preserves_task_failures_and_infrastructure_omissions(tmp_path):
    jobs = [_job(i, "B1") for i in range(5)]
    run = tmp_path / "static"
    _manifest(run, jobs)
    _episode(run, jobs[0], {"mission": "target", "success": False, "outcome": "budget", "steps": 2})
    _episode(run, jobs[1], {"status": "excluded", "reason": "frozen world invariant"})
    _episode(run, jobs[2], {"status": "infra_failed", "reason": "oom", "attempts": 2})
    _episode(run, jobs[3], {"mission": "target", "success": True, "outcome": "success"}, trace="{")
    summary = evaluate(run)
    assert (summary["valid"], summary["excluded"], summary["failed"], summary["pending"], summary["invalid"]) == (1, 1, 1, 1, 1)
    assert summary["attempted"] == 4
    assert summary["attempt_records"] == 5
    assert summary["strata"][0]["matched_seeds"] == 1


def test_pairing_uses_mission_and_replicates_without_inflating_seed_count(tmp_path):
    run = tmp_path / "static"
    jobs = [_job(i, variant) for i in range(7) for variant in ("B1", "B3")]
    jobs += [_job(0, variant, replicate=1) for variant in ("B1", "B3")]
    _manifest(run, jobs)
    for job in jobs:
        if job["seed"] == 6 and job["variant"] == "B1":
            continue
        success = (job["variant"] == "B3") != bool(job["replicate"])
        mission = "other" if job["seed"] == 5 and job["variant"] == "B1" else "target"
        _episode(run, job, {"success": success, "mission": mission, "outcome": "ended"})
    _, rows = load_run(run)
    result = next(result for result in compare(rows) if result.metric == "success")
    assert (result.treatment_n, result.control_n, result.paired_n) == (7, 6, 5)
    assert result.difference == pytest.approx(0.8)
    assert result.lower_95 <= result.difference <= result.upper_95


def test_report_generates_figures_and_verifiable_evidence(tmp_path):
    run = tmp_path / "static"
    jobs = [_job(0, variant) for variant in ("B1", "B3")]
    _manifest(run, jobs)
    for job in jobs:
        directory = _episode(run, job, {
            "success": job["variant"] == "B3", "mission": "target", "outcome": "ended",
            "steps": 3, "stale_actions": 1, "prompt_tokens": 10, "completion_tokens": 2,
        })
        (directory / "evaluator.jsonl").write_text('{"ground_truth":"private"}' + "\n")
    path = generate_combined_report([run], tmp_path / "report")
    assert "B3 − B1" in path.read_text(encoding="utf-8")
    assert (path.parent / "figures" / "success.png").read_bytes().startswith(b"\x89PNG")
    index = json.loads((path.parent / "artifact-index.json").read_text(encoding="utf-8"))
    assert sum(item["kind"] == "private-evaluator" for item in index["files"]) == 2
    for item in index["files"]:
        assert item["sha256"] == hashlib.sha256((tmp_path / item["path"]).read_bytes()).hexdigest()


def test_reports_verify_supervisor_integrity_and_count_attempts(tmp_path):
    run = tmp_path / "static"
    first, second = _job(1, "B3"), _job(2, "B3")
    _manifest(run, [first, second])
    manifest_path = run / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["lock_sha256"] = "lock is present in supervisor manifests"
    manifest_path.write_text(json.dumps(manifest))
    directory = _episode(run, first, {"success": True, "mission": "target", "outcome": "success"})
    (directory / "evaluator.json").write_text("{}")
    integrity = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in directory.iterdir()}
    (directory / "integrity.json").write_text(json.dumps(integrity))
    for job in (first, second):
        attempt = run / "attempts" / job["id"] / "first"
        attempt.mkdir(parents=True)
        (attempt / "error.json").write_text('{"error":"engine interrupted"}')
    status = evaluate(run)
    assert (status["valid"], status["failed"], status["attempt_records"]) == (1, 1, 3)
    (directory / "trajectory.jsonl").write_text('{"event":"changed"}\n')
    status = evaluate(run)
    assert status["invalid"] == 1
    assert "checksum failed" in status["nonvalid_cells"][0]["reason"]
