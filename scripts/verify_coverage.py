"""Require the full validated matched roster before advancing the experiment."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("coverage", type=Path)
    parser.add_argument("expected", type=int)
    args = parser.parse_args()
    data = json.loads(args.coverage.read_text())
    if data["valid"] != args.expected or data["planned"] != args.expected:
        raise SystemExit(f"coverage incomplete: {data['valid']} valid of {args.expected} required")
    if any(row["matched_cells"] != row["planned_matched_cells"] for row in data["strata"]):
        raise SystemExit("one or more comparison cells do not match on mission, seed and replicate")
    print(f"Verified {args.expected} episodes with every required pair intact.")


if __name__ == "__main__":
    main()
