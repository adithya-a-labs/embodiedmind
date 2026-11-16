# Backfill earlier EmbodiedMind runs

## Objective

Record work that happened before the repository adopted per-run Markdown records.

## Changes and rationale

Added eight `retrospective-*.md` files to `codex-runs/`. They cover the Notion protocol, full experiment, results and world explanations, branch setup, DoorKey trace review, viewer, Dev Tunnel, and evidence archiving. Each record identifies the changes, documented rationale, and verification. Related follow-ups are grouped by task because the earlier work predates the per-run rule.

## Verification

Cross-checked commit IDs against `git log` and matched experiment and smoke archive paths to the recorded run IDs. The entries are in the working tree on `embodiedmind-experiment`, based on `1a0372b`. Documentation-only change.
