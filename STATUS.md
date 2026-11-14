# EmbodiedMind status

**Complete.** Both frozen held-out rosters finished on 14 November 2026 IST. The final report, independent regeneration and checksums were verified.

- Run: `embodiedmind-20261114-0428-ist`. Branch: `codex/embodiedmind-overnight`. Frozen experiment source: `a44c34e0431322078a368453881366214993b900`.
- Development: 40/40 paired stock episodes and 18/18 revised custom development episodes. The final report's pooled coverage includes the 40 stock pilot and both held-out rosters. Custom development has its own pilot report.
- Static: 240/240 valid episodes, 30 matched seeds per environment, 50 mission successes.
- Dynamic: 270/270 valid episodes, 30 matched seeds per intervention, 15 mission successes. Dropout and relocation occurred in each of their 90 assigned episodes.
- Zero held-out infrastructure failures, retries or exclusions. Valid task failures were included.
- Final validation: 64 local tests, 550 report rows, and 2,906 artifact checksums. Independent regeneration matched tables and figures byte for byte. No hosted CI workflow is configured.
- Local Ollama provided 13,572 held-out requests, 7,765,116 prompt tokens and 270,584 completion tokens. Sum of per-request latencies: 3,637 seconds. No cloud inference was used. The temporary two-slot server was stopped after calibration; the original serial service remains active.

## Evidence

Study directory: `results/runs/embodiedmind-20261114-0428-ist/`.

- `final-report/report.md`, `comparisons.csv`, `metrics.csv`, `figures/`, `application-summary.md`, `coverage.json`, `artifact-index.json`, and `reproduced-evidence/` are in the final report bundle.
- `pilot-report/report.md` contains the stock and custom development results.
- `final-audit.log`, `final-tests.log`, `report-regeneration.log`, and `checkpoint-journal.jsonl` document verification. `FAILURES.md` records recovered development issues.
- There are no remaining scored jobs. To reproduce execution, use the frozen source commit in a checkout with the locked environment and the saved study directory. See the commands in [README](README.md) and [the frozen protocol](experiments/manifests/frozen-protocol.md).
