# EmbodiedMind

A frozen local LLM navigates symbolic, partially observable MiniGrid/BabyAI worlds. The study compares B0 reactive, B1 bounded text history, B2 structured evidence without revision, and B3 structured memory with revision under shared observations, controls, inference budgets and paired missions.

H1 tests held-out success for B3 versus B1. H2 tests stale actions for B3 versus B2 after contradiction. H3 asks whether the memory effect increases under lost/delayed evidence. H4 measures costs and failure modes of additional structure. The study concerns discrete symbolic simulation.

See the [frozen registration](experiments/manifests/frozen-protocol.md), [research proposal](RESEARCH_PROPOSAL.md), [execution guide](AGENT_GUIDE.md), and [current status](STATUS.md).

## Bootstrap and reproduce

Run from a clean Ubuntu checkout at the registered source SHA. Keep `BABYAI_DONE_ACTIONS` unset. Use the locked Python environment and configured loopback Ollama model with the verified digest, 4096 context and one active request.

```sh
uv sync --locked --inexact
.venv/bin/python -m pytest -q
.venv/bin/embodiedmind smoke --env BabyAI-GoToObjS6-v1 --seed 42
```

Resume the study's held-out rosters and regenerate its report:

```sh
run=results/runs/embodiedmind-20261114-0428-ist
bash scripts/run_benchmarks.sh "$run"
.venv/bin/embodiedmind status "$run/static"
.venv/bin/embodiedmind status "$run/dynamic"
```

A graceful checkpoint uses `.venv/bin/embodiedmind stop "$run/static"` or the applicable dynamic directory. The coordinator drains active work and then stops before starting the next gate. Rerun the same benchmark command from the registered SHA to reuse checksummed episodes. For a fresh experiment, create the paired pilot under its own study directory before launching the benchmark script with that directory.

The report, manifest, checksummed raw logs, screenshots and replays live under the private study directory. Rebuild from existing outputs with:

```sh
.venv/bin/embodiedmind report "$run/pilot" "$run/static" "$run/dynamic" --output "$run/final-report"
```
