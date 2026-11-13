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
    args = parser.parse_args()
    if args.command == "smoke":
        from embodiedmind.environments.factory import smoke_environment

        summary, frame = smoke_environment(
            args.env, args.seed, args.max_steps, render=args.screenshot is not None,
        )
        if args.screenshot:
            from PIL import Image

            args.screenshot.parent.mkdir(parents=True, exist_ok=True)
            Image.fromarray(frame).save(args.screenshot)
        print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
