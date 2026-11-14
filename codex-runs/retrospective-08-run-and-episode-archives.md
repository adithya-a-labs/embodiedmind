# Require complete evidence and automate packaging

Retrospective record. Reconstructed from this chat, Git history, and cited evidence. Related follow-up turns are grouped by task.

## Changes

Added the archive policy to `AGENTS.md`, the local guide, and both Notion pages. Updated CLI, runner, packaging, analysis, viewer discovery, ignore rules and tests. Committed policy as `362fbfa`, implementation as `919de25`, and sample evidence as `1a0372b`.

## Rationale

Used one Git-visible outputs folder per run and separated attempts so retries preserve failures. Streamed inputs before model calls and evaluator-only state independently. Generated reports and visuals from saved evidence so packaging can be rerun without inference.

## Verification and evidence

68 tests passed, including a simulated retry. A real smoke archive was packaged, and 35 artifact hashes were verified. [Smoke archive](../outputs/smoke-20261114T054937Z-e8e9ddfe/report/report.md)
