# Scaffold, execute, and report the full experiment

Retrospective record. Reconstructed from this chat, Git history, and cited evidence. Related follow-up turns are grouped by task.

## Changes

Built the scaffold, seeded environments, observation checks, B0–B3 memory, runner, dynamic world, and offline analysis. Froze the protocol at `a44c34e` and committed the audited handoff at `3b3ec26`. Commits from `9265972` through `3b3ec26` record the implementation.

## Rationale

Kept the four variants on a shared controller and frozen model. Chose one inference slot after development calibration. Fixed relocation log serialization, then used two shared scripted turns after the original dynamic pilot produced no relocations. Froze these decisions before held-out scoring.

## Verification and evidence

40 stock pilot, 240 static and 270 dynamic episodes validated in the main report. 64 tests passed, 2,906 artifact hashes were audited, and the regenerated tables and figures matched. [Tracked summary](../reports/technical_report.md) · [Local final report](../results/runs/embodiedmind-20261114-0428-ist/final-report/report.md)
