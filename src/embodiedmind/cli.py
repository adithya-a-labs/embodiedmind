"""Entry points for the headless EmbodiedMind experiment."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="EmbodiedMind reproducible research runner")
    commands = parser.add_subparsers(dest="command", required=True)
    smoke = commands.add_parser("smoke", help="verify seeded stock environment")
    smoke.add_argument("--env", default="BabyAI-GoToObjS6-v1")
    smoke.add_argument("--seed", default=42, type=int)
    smoke.add_argument("--max-steps", default=60, type=int)
    smoke.add_argument("--screenshot", type=Path)
    for name in ("run", "resume"):
        queue = commands.add_parser(name, help=f"{name} an immutable job roster")
        queue.add_argument("--config", type=Path, required=True)
        queue.add_argument("--output", type=Path, required=name == "resume",
                           help="run archive path (run defaults to outputs/<run-id>)")
        queue.add_argument("--models", type=Path, default=Path("configs/models.yaml"))
        queue.add_argument("--profile", type=Path)
        queue.add_argument("--parallel", type=int, default=1)
        queue.add_argument("--limit-jobs", type=int)
        queue.add_argument("--monitor", action="store_true", help="publish evaluator snapshots for the local viewer")
    viewer = commands.add_parser("viewer", help="open the local experiment viewer")
    viewer.add_argument("--runs", type=Path, help="archive to browse instead of outputs and results/runs")
    viewer.add_argument("--sandbox-output", type=Path, default=Path("results/sandbox"))
    viewer.add_argument("--models", type=Path, default=Path("configs/models.yaml"))
    viewer.add_argument("--port", type=int, default=8765)
    viewer.add_argument("--workflows", type=Path, default=Path("configs/workflows.json"))
    learn = commands.add_parser("learn-workflows", help="extract verified routines from a development archive")
    learn.add_argument("run_dir", type=Path)
    learn.add_argument("--output", type=Path, required=True)
    viewer.add_argument("--tunnel-origin", help="exact HTTPS origin of a private Microsoft Dev Tunnel")
    for name in ("status", "evaluate", "stop"):
        sub = commands.add_parser(name)
        sub.add_argument("run_dir", type=Path)
    report = commands.add_parser("report")
    report.add_argument("run_dirs", type=Path, nargs="+")
    report.add_argument("--output", type=Path, required=True)
    package = commands.add_parser("package", help="rebuild a saved run's evidence package")
    package.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    if args.command == "smoke":
        _smoke(args)
    elif args.command in {"run", "resume"}:
        from datetime import datetime, timezone
        from uuid import uuid4

        from embodiedmind.experiments.schedule import git, run

        if args.output is None:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            args.output = Path(git("rev-parse", "--show-toplevel")) / "outputs" / (
                f"{args.config.stem}-{stamp}-{uuid4().hex[:8]}"
            )
        print(f"Run archive: {args.output}", flush=True)
        result = run(args.config, args.output, args.models, args.parallel, args.profile, args.limit_jobs, args.monitor)
        print(json.dumps(result, sort_keys=True))
        if result["status"] == "blocked":
            raise SystemExit(1)
    elif args.command == "status":
        print((args.run_dir / "heartbeat.json").read_text(encoding="utf-8"))
    elif args.command == "stop":
        _stop(args.run_dir)
    elif args.command == "evaluate":
        from embodiedmind.analysis.report import evaluate

        print(json.dumps(evaluate(args.run_dir), indent=2))
    elif args.command == "report":
        from embodiedmind.analysis.report import generate_combined_report

        print(generate_combined_report(args.run_dirs, args.output))
    elif args.command == "package":
        import fcntl

        from embodiedmind.experiments.archive import package_run

        with (args.run_dir / "supervisor.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            print(package_run(args.run_dir))
    elif args.command == "learn-workflows":
        from embodiedmind.memory.workflows import learn_doorkey

        learn_doorkey(args.run_dir, args.output)
    elif args.command == "viewer":
        from embodiedmind.viewer.server import serve

        serve(args.runs, args.sandbox_output, args.models, args.port, args.tunnel_origin, args.workflows)


def _smoke(args):
    from embodiedmind.environments.factory import smoke_environment

    summary, frame = smoke_environment(
        args.env, args.seed, args.max_steps, render=args.screenshot is not None,
    )
    if args.screenshot:
        from PIL import Image

        args.screenshot.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(frame).save(args.screenshot)
    print(json.dumps(summary, sort_keys=True))


def _stop(run_dir):
    import fcntl
    import os
    import signal

    with (run_dir / "supervisor.lock").open("r") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            data = json.loads((run_dir / "heartbeat.json").read_text(encoding="utf-8"))
            pid = int(data["pid"])
            expected = (run_dir / "supervisor.lock").resolve()
            descriptors = Path(f"/proc/{pid}/fd")
            if not any(fd.resolve() == expected for fd in descriptors.iterdir()):
                raise SystemExit("live process identity does not match this run")
            os.kill(pid, signal.SIGTERM)
            return
        raise SystemExit("no active supervisor owns this run")


if __name__ == "__main__":
    main()
