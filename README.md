# EmbodiedMind

A frozen local LLM navigates symbolic, partially observable MiniGrid/BabyAI worlds. The study compares B0 reactive, B1 bounded text history, B2 structured evidence without revision, and B3 structured memory with revision under shared observations, controls, inference budgets and paired missions.

H1 tests held-out success for B3 versus B1. H2 tests stale actions for B3 versus B2 after contradiction. H3 asks whether the memory effect increases under lost/delayed evidence. H4 measures costs and failure modes of additional structure. An engineering smoke run establishes feasibility. The study concerns discrete symbolic simulation.

The full study includes a development pilot, 240 planned static held-out episodes and matched custom dynamic conditions, followed by reproducible analysis. See [research proposal](RESEARCH_PROPOSAL.md), [execution guide](AGENT_GUIDE.md) and [status](STATUS.md).

## Bootstrap

From Ubuntu in the project checkout:

```sh
uv sync --locked --inexact
uv run --locked --no-sync embodiedmind --help
uv run --locked --no-sync python -m pytest
```

Use one pinned local Ollama model on WSL loopback. Runner, resume, stop, and reporting commands will be added as their gates pass.
