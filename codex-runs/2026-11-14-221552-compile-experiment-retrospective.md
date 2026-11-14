# Compile the EmbodiedMind experiment retrospective

## Objective

Compile the experiment from Phase 0 through B10, including implementation and infrastructure, the learning from every archived run, and the Codex work records. Save the result as a new Notion page.

## Changes

- Created [EmbodiedMind experiment retrospective](https://app.notion.com/p/418f975653bf81e6a729e31e76558154?pvs=204) as a private Notion draft. It contains the original study and controls, architecture and viewer history, findings and regressions, all 30 run entries, 49 prior Codex records, three full development scorecards, and a source map. The roadmap, proposal, and architecture guide are linked sources.
- Added `codex-runs/2026-11-14-221552-compile-experiment-retrospective.md` as the record of this work. No code, archived evidence, or prior Notion page changed. No new simulator or inference run took place.
- Inspected `embodiedmind-experiment` at `72c28725` with upstream `origin/master`. The initial working tree was clean. The run record is an uncommitted working-tree change.

## Evidence and decisions

- Read the project proposal, status, phase checkpoints, frozen protocol, final report, architecture changes, Git history, and all 49 preexisting Markdown records. Examined legacy `results/runs/` and modern `outputs/`, including manifests, coverage, summaries, raw traces, representative episode evidence, and report bundles.
- Counted 2,281 manifest cells across 30 archives, with 2,263 finalized episode records and 1,720 per-episode GIFs. The first dynamic pilot finalized 6 of 18 planned jobs before a serialization error. The live follow check stopped by design at 4 of 10. Preserved both denominators and their distinct purposes.
- Kept the 510 frozen held-out episodes apart from pilots and development comparisons. The 80-action MultiRoom rerun uses the same layouts under a different cap. The B10 development layouts informed its design. These choices preserve the scope of the measured claims.
- Used one Notion page with an evidence register and a Markdown record index. Raw traces and visuals remain in their original repository archives. Existing summary bundles reuse underlying episodes, so they were not counted as new runs.

## Verification and limits

- Used native WSL `git status --short --branch`, Git log, and file searches with `rg`, then parsed manifests, finalized summaries, reports, and JSONL traces in Python. Recomputed all 88,964 indexed SHA-256 references across 24 saved artifact indexes. All reads and hashes passed. Indexes overlap.
- Normalized legacy metrics from raw traces when the CSV schema lacked `blocked_actions`. Parsed the calibration JSON after its simulator warning prefix and confirmed the saved serial and two-slot profiles. A first PowerShell path search needed explicit paths in place of Bash brace expansion.
- Windows Git rejected the WSL mount ownership and the sandboxed native WSL call returned access denied. Ran the read-only status check with approved native WSL access without changing Git configuration.
- Fetched the created Notion page and verified its 23 headings, all 30 archive paths, all 49 record names, and all 42 scorecard table lines including headers. Confirmed the existing Notion references and opened the page panel.
- Current remote status, unarchived development probes, and unseen-layout B10 performance were outside the available retrospective evidence.
