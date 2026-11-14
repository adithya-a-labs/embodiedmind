# Record every Codex run

Date: 14 November 2026, 11:25 IST

## Objective

Create a repository folder for Markdown records of Codex runs, including the changes made and the rationale behind them.

## Changes and rationale

- `AGENTS.md` now requires one record per Codex run before the final reply. The root agent instructions are the existing entry point for repository-wide rules.
- `codex-runs/` holds the records. This keeps the rationale and verification near the code while `outputs/` holds raw experiment evidence. Timestamped filenames let multiple runs on the same topic keep their own history.
- This file records the first run. The new rule also covers read-only, blocked, and interrupted runs so the history includes their outcomes and open items.

## Verification

- `git diff --check` passed. `git status --short --branch --untracked-files=all` showed the instruction update and new Markdown record on `embodiedmind-experiment`, based on `1a0372b`. Both changes are in the working tree.
- Documentation-only change. No tests run.
