"""Immutable job manifests and a bounded, resumable local execution queue."""

import fcntl
import hashlib
import json
import os
import platform
import signal
import subprocess
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime, timezone
from importlib.metadata import version
from itertools import product
from pathlib import Path
from threading import Event

import yaml

from embodiedmind.experiments.runner import episode, write_event
from embodiedmind.reasoning.llm_client import InferenceUnavailable, Ollama


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path, data):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def build_manifest(config, model_config, model, info, slots, profile):
    cfg = yaml.safe_load(config.read_text(encoding="utf-8"))
    limits = cfg["limits"]
    if any(type(limits[k]) is not int or limits[k] < 1 for k in ("max_steps", "max_calls", "memory_bytes")):
        raise ValueError("each episode limit must be a positive integer")
    seeds = cfg["seeds"] if "seeds" in cfg else range(cfg["seed_start"], cfg["seed_start"] + cfg["seed_count"])
    jobs = [
        {
            "id": f"e{e:02}-s{seed:05}-{intervention}-{variant}-r{replicate}",
            "environment": environment, "seed": seed, "variant": variant,
            "intervention": intervention, "replicate": replicate,
        }
        for (e, environment), seed, intervention, variant, replicate in product(
            enumerate(cfg["environments"]), seeds, cfg["interventions"], cfg["variants"],
            range(cfg.get("replicates", 1)),
        )
    ]
    if not jobs or len({job["id"] for job in jobs}) != len(jobs):
        raise ValueError("the experiment roster must be nonempty and unique")
    guarded = cfg["split"] in {"static", "dynamic"}
    commit = git("rev-parse", "HEAD")
    dirty = git("status", "--porcelain")
    if guarded and dirty:
        raise ValueError("scored runs require the frozen clean commit")
    if guarded:
        _verify_roster(cfg, jobs)
        if "BABYAI_DONE_ACTIONS" in os.environ:
            raise ValueError("frozen BabyAI success semantics require BABYAI_DONE_ACTIONS to be unset")
    if guarded and (not profile or not profile.is_file()):
        raise ValueError("scored runs require a calibrated runtime profile")
    approved = load_json(profile) if profile else {}
    if profile and (approved["parallel"] != slots or approved["version"] != info["version"]):
        raise ValueError("live model/version or slot limit differs from the approved runtime profile")
    if guarded:
        model.generate(model.request(
            "Return one JSON action.", "Choose action 1 with evidence 'explore'.", 42,
        ))
        active = next((record for record in model.call("/api/ps")["models"]
                       if record["digest"] == model.digest), None)
        if not active or active["runner"] != approved["runner"] or active["context_length"] != approved["context"]:
            raise ValueError("loaded runner does not match the frozen runtime profile")
        if approved["require_full_gpu"] and active["size_vram"] != active["size"]:
            raise ValueError("Ollama model is not fully resident on the GPU")
    return {
        "split": cfg["split"], "commit": commit, "dirty": bool(dirty), "settings": cfg,
        "config": str(config), "config_sha256": digest(config),
        "model_config": str(model_config), "model_config_sha256": digest(model_config),
        "lock_sha256": digest(Path("uv.lock")), "model": info, "endpoint": model.endpoint,
        "profile": approved, "parallel": slots, "os": platform.platform(),
        "python": platform.python_version(),
        "packages": {name: version(name) for name in ("minigrid", "gymnasium", "numpy", "matplotlib")},
        "jobs": jobs,
    }


def _verify_roster(cfg, jobs):
    if cfg["split"] == "static":
        expected = (
            {"MiniGrid-DoorKey-8x8-v0", "BabyAI-GoToObjMazeS7-v0"},
            set(range(1000, 1030)), {"none"}, {"B0", "B1", "B2", "B3"}, {0},
        )
    else:
        expected = (
            {"EmbodiedMind-GoToShift-v0"}, set(range(2000, 2030)),
            {"no_change", "dropout", "relocation"}, {"B1", "B2", "B3"}, {0},
        )
    keys = ("environment", "seed", "intervention", "variant", "replicate")
    observed = {tuple(job[key] for key in keys) for job in jobs}
    if observed != set(product(*expected)):
        raise ValueError("scored roster differs from the preregistered design")


def complete(episodes, job_id):
    path = episodes / job_id
    if not path.is_dir():
        return False
    data = load_json(path / "integrity.json")
    expected = {"summary.json", "trajectory.jsonl", "evaluator.json"}
    if not expected <= set(data) or any(digest(path / name) != value for name, value in data.items()):
        raise RuntimeError(f"integrity check failed for {job_id}")
    summary = load_json(path / "summary.json")
    if summary["id"] != job_id or summary["status"] != "completed":
        raise RuntimeError(f"invalid completion for {job_id}")
    return True


def execute(root, job, limits, model, visuals, monitor=False):
    attempts = root / "attempts" / job["id"]
    attempts.mkdir(parents=True, exist_ok=True)
    for retry in range(limits.get("infrastructure_retries", 2) + 1):
        attempt = attempts / f"{time.time_ns()}-{retry}"
        attempt.mkdir()
        atomic_json(attempt / "job.json", {**job, "started": now()})

        def publish(event):
            atomic_json(root / "live" / f"{job['id']}.json", {
                **event, "job": job, "at": now(), "attempt": attempt.name,
            })

        try:
            summary = episode(job, limits, model, attempt, visuals, publish if monitor else None)
            summary.update({"attempt": attempt.name, "completed": now()})
            atomic_json(attempt / "summary.json", summary)
            atomic_json(attempt / "integrity.json", {
                path.name: digest(path) for path in sorted(attempt.iterdir()) if path.is_file()
            })
            attempt.rename(root / "episodes" / job["id"])
            return {"id": job["id"], "attempt": attempt.name, "success": summary["success"]}
        except InferenceUnavailable as exc:
            atomic_json(attempt / "error.json", {"kind": "infrastructure", "at": now(), "error": str(exc)})
            if monitor:
                publish({"phase": "retrying" if retry < limits.get("infrastructure_retries", 2)
                         else "failed", "error": str(exc)})
            if retry == limits.get("infrastructure_retries", 2):
                return {"id": job["id"], "error": str(exc)}
            time.sleep(2 ** retry)
        except Exception as exc:
            atomic_json(attempt / "error.json", {"kind": "execution", "at": now(), "error": str(exc)})
            if monitor:
                publish({"phase": "failed", "error": str(exc)})
            raise
    raise AssertionError("retry loop did not return")


def run(config, root, model_config, slots, profile, limit_jobs, monitor=False):
    if limit_jobs is not None and limit_jobs < 1:
        raise ValueError("a job limit must be positive")
    if slots not in (1, 2):
        raise ValueError("supported calibrated slot count is one or two")
    model_values = yaml.safe_load(model_config.read_text(encoding="utf-8"))
    model_values.pop("temperature")
    model_values["endpoint"] = os.environ.get("OLLAMA_HOST", model_values["endpoint"])
    model = Ollama(**model_values)
    root.mkdir(parents=True, exist_ok=True)
    with (root / "supervisor.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        (root / "episodes").mkdir(exist_ok=True)
        if monitor:
            (root / "live").mkdir(exist_ok=True)
        manifest = build_manifest(config, model_config, model, model.verify(), slots, profile)
        path = root / "manifest.json"
        if path.exists():
            registered = load_json(path)
            if any(registered[k] != v for k, v in manifest.items() if k not in {"commit", "dirty"}):
                raise ValueError("resume settings differ from the immutable manifest")
            if registered["commit"] != manifest["commit"]:
                raise ValueError("resume at the registered source commit")
        else:
            atomic_json(path, {**manifest, "created": now()})

        stop = Event()
        previous = {sig: signal.signal(sig, lambda *_: stop.set()) for sig in (signal.SIGINT, signal.SIGTERM)}
        try:
            return supervise(root, manifest, model, stop, limit_jobs, monitor)
        finally:
            for sig, handler in previous.items():
                signal.signal(sig, handler)


def supervise(root, manifest, model, stop, limit_jobs, monitor=False):
    all_jobs = manifest["jobs"]
    planned = len(all_jobs)
    pending = [job for job in all_jobs if not complete(root / "episodes", job["id"])]
    checked = planned - len(pending)
    jobs = iter(pending[:limit_jobs] if limit_jobs else pending)
    errors = 0
    # Preserve the same profile and submission order across a resumed comparison.
    slots = manifest["parallel"]
    settings = manifest["settings"]
    output = root / "heartbeat.json"
    run_state = {"pid": os.getpid(), "planned": planned, "completed": checked, "errors": 0}
    with (root / "journal.jsonl").open("a", encoding="utf-8") as journal:
        with ThreadPoolExecutor(max_workers=slots) as pool:
            active = {}

            def top_up():
                while len(active) < slots and not stop.is_set():
                    job = next(jobs, None)
                    if job is None:
                        return
                    visuals = job["seed"] == all_jobs[0]["seed"] or manifest["split"] == "smoke"
                    future = pool.submit(execute, root, job, settings["limits"], model, visuals, monitor)
                    active[future] = job["id"]

            top_up()
            while active:
                atomic_json(output, {**run_state, "status": "running", "at": now(), "active": list(active.values())})
                finished, _ = wait(active, timeout=10, return_when=FIRST_COMPLETED)
                for future in finished:
                    job_id = active.pop(future)
                    try:
                        result = future.result()
                    except Exception as exc:
                        stop.set()
                        error = {"id": job_id, "error": str(exc)}
                        write_event(journal, {"at": now(), **error})
                        atomic_json(output, {**run_state, "status": "blocked", "at": now(),
                                             "active": list(active.values()), **error})
                        raise
                    errors += "error" in result
                    checked += "error" not in result
                    run_state.update(completed=checked, errors=errors)
                    write_event(journal, {"at": now(), **result})
                    if errors >= 2:
                        stop.set()
                top_up()
    status = "complete" if checked == planned else ("blocked" if errors else "checkpoint")
    atomic_json(output, {**run_state, "status": status, "at": now(), "active": []})
    return {**run_state, "status": status}
