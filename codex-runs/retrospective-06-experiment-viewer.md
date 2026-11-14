# Build replay, live monitor, and sandbox

Retrospective record. Reconstructed from this chat, Git history, and cited evidence. Related follow-up turns are grouped by task.

## Changes

Added viewer code and browser assets under `src/embodiedmind/viewer/`, a visual-state helper, runner monitoring hooks, CLI commands, docs and tests. Committed as `3f0a76f` and later pushed to the experiment branch.

## Rationale

Reused MiniGrid and the saved trace to reconstruct boards without inference. Defaulted to DoorKey seed 1015, B0 vs. B2 at action 8. Sandbox forks into a separate simulation so exploratory actions cannot alter benchmark evidence.

## Verification and evidence

66 tests passed. Verified the replay, relocation, live smoke, manual sandbox control, local agent step and sandbox save. [README](../README.md)
