# Commit and publish Codex run records

## Objective

Commit the repository rule and Markdown run history, then publish the local commits to the GitHub experiment branch while retaining `origin/master` as the local upstream.

## Changes and rationale

- Stage `AGENTS.md` separately as `docs(agents): require Codex run records` so the recording rule has its own reviewable change.
- Stage the Markdown records under `codex-runs/`, including this record, as `docs(history): add Codex run records and backfill`.
- Use an explicit Git push refspec for `embodiedmind-experiment` to publish the experiment commits without changing the configured upstream.

## Verification

`git diff --check` passed on the initial working tree. The branch was `embodiedmind-experiment`, tracking `origin/master`, with `1a0372b` as the starting commit. The publish command checks staged whitespace before each commit and verifies the GitHub branch tip against the local commit after pushing. Documentation-only change.
