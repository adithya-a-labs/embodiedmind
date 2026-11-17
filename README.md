<div align="center">

# EmbodiedMind

**Memory, belief revision, and grounded decision-making in partially observable worlds.**

A research testbed for studying what agents remember, when they should revise their beliefs, and whether memory actually changes their actions.

<p>
  <img alt="Python 3.12" src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white">
  <img alt="MiniGrid and BabyAI" src="https://img.shields.io/badge/Environments-MiniGrid%20%2B%20BabyAI-398A6C">
  <img alt="Local inference" src="https://img.shields.io/badge/Inference-local%20Ollama-444444">
  <img alt="Research status" src="https://img.shields.io/badge/Status-active%20research-9B6B35">
</p>

[**Explore the results**](#results) · [**Get started**](#quick-start) · [**Replay experiments**](#experiment-viewer) · [**Research protocol**](experiments/manifests/b11-protocol.md)

</div>

---

## Overview

EmbodiedMind investigates **memory and belief revision in embodied agents** using symbolic, partially observable MiniGrid and BabyAI environments. Agents are evaluated on matched, seeded missions; their decisions are traced against agent-visible observations while evaluator-only state remains separate.

The focus is deliberately experimental: compare memory representations, test how agents react when previously observed information becomes wrong, and measure the effect of verification, planning, and inference cost.

| Research dimension | What is evaluated |
| --- | --- |
| **Memory** | Text history, structured observations, episodic/spatial memory, and retrieval |
| **Belief revision** | What happens when an agent re-observes evidence that contradicts a stored fact |
| **Information acquisition** | Fixed vs adaptive verification under partial observability |
| **Agent contribution** | Language-model proposals compared with deterministic controller behavior |
| **Reliability** | Success, actions, stale commitments, inference costs, paired uncertainty estimates, and auditable traces |

> **Research scope:** These are controlled studies in symbolic simulation, not demonstrations of general real-world robot intelligence. Some comparisons show null or negative effects; those results are retained.

## Results

**At a glance**

| Study | Evaluated episodes | Design |
| --- | ---: | --- |
| Original B0–B3 held-out study | **510** | 240 static + 270 dynamic episodes |
| B11 fresh-seed follow-up | **3,090** | Five rosters; broad benchmark and focused mechanism comparisons |

**Selected findings from the completed B11 follow-up**

| Comparison | Observation |
| --- | --- |
| Broad benchmark, 48-action budget | B10 and B11 each completed **115/140** episodes; B11 used **2.4% fewer total tokens** |
| MultiRoom, 48 vs 80 actions | B10 and B11 each improved from **6/10** to **10/10** on the same layouts |
| Belief revision under target relocation | Fixed-verification success increased from **8/30** to **23/30**; stale route commitments fell from **543 to zero** |
| Fixed vs adaptive verification | Revising arms had identical action sequences in **150/150** matched pairs |
| Language model vs controller-only B11C | Both completed **125/150**; all **150/150** paired action sequences matched |

The model-vs-controller result is particularly important: **these tasks did not demonstrate an independent action-selection benefit from the model**. Results are specific to the registered task suites, budgets, and executor.

The original frozen B0–B3 study found DoorKey success of **8/30 for revising memory (B3)** versus **4/30 for text history (B1)**, while the reactive baseline (B0) reached **17/30**. The original relocation study did **not** show a reduction in explicitly cited stale actions for B3 versus B2.

![Paired comparison figure from the B11 report](outputs/b11-combined-20261116-181345/report/figures/paired-comparisons.png)

**Read the evidence:** [B11 report](outputs/b11-combined-20261116-181345/report/report.md) · [Paired comparisons (CSV)](outputs/b11-combined-20261116-181345/report/comparisons.csv) · [Coverage audit](outputs/b11-combined-20261116-181345/report/coverage.json) · [Frozen B0–B3 report](reports/technical_report.md) · [B11 protocol](experiments/manifests/b11-protocol.md)

## Quick start

**Requirements:** Ubuntu or WSL, \`uv\`, and Python 3.12. The deterministic smoke test and test suite do not require Ollama.

\`\`\`bash
uv sync --locked --inexact
.venv/bin/python -m pytest -q
.venv/bin/embodiedmind smoke --env BabyAI-GoToObjS6-v1 --seed 42
\`\`\`

For model-backed experiments, use the local Ollama model and exact digest in [configs/models.yaml](configs/models.yaml). Keep \`BABYAI_DONE_ACTIONS\` unset and run the registered comparisons with one inference worker.

\`\`\`bash
run="outputs/smoke-$(date +%Y%m%d-%H%M%S)"
.venv/bin/embodiedmind run --config configs/smoke.yaml --output "$run" --monitor --parallel 1
.venv/bin/embodiedmind status "$run"
\`\`\`

**Where to look next:** [Agent variants](#agent-variants) · [Experiment viewer](#experiment-viewer) · [Reproduce the reports](#reproduce-the-reports) · [Research proposal](RESEARCH_PROPOSAL.md)

## Experiment viewer

From the Ubuntu checkout, start the viewer and open <http://127.0.0.1:8765>.

```sh
.venv/bin/embodiedmind viewer
```

In **Replay**, choose a game, run, and seed, then select agents to compare. One
example from the checked-in evidence is GoToShift relocation seed `11101` in
`b11-rq-shift-20261116-181345`, comparing **B11P** with **B11R**. At step 6 both
agents saw the moved target. B11R completed the mission in 13 actions, while
B11P timed out at 48.

The boards show the evaluator state and the logged agent observation separately.
The action inspector shows the hint, chosen action, and outcome. Open
**Model input and memory** and select a spatial fact to locate it on the
evaluator board. Replay uses saved actions, checks reconstructed observations
and outcomes against the trace, and runs without Ollama. Use
`viewer --runs PATH` to browse a specific archive or archive directory.

To see a live run, keep the viewer open and run the monitored smoke example in another terminal.

Open **Live monitor** or add `#live` to the viewer URL. It automatically
discovers and follows an active run. Select a run manually to pin it and use
**Follow active run** to resume automatic selection. Open completed runs in
**Replay**. The runner publishes evaluator snapshots alongside the run and continues if you close
the browser. Use `--monitor` with `resume` to monitor a resumed run.

In **Sandbox**, start a seeded environment or use **Take over before action**
from either side of a replay. Use the buttons or arrow keys to move and turn.
**Agent move** and **Auto-play** use the configured local Ollama model. Saved
exploratory sessions go under `outputs/sandbox-…/` by default and can be
opened from Replay. The archive reconstructs manual and branch-prefix actions
and preserves model requests made in that browser session.

For access from another device, forward only port 8765 through a **private**
Microsoft Dev Tunnel. Restart the viewer with the exact HTTPS address printed
for the forwarded port:

```sh
.venv/bin/embodiedmind viewer --tunnel-origin https://your-forwarded-host.devtunnels.ms
```

Open that address on your phone and sign in with the tunnel owner's account.
Keep the laptop awake, the viewer running, and the tunnel connected. Keep
Ollama on loopback and leave port 11434 out of the tunnel.

## Run archives

The `run` command creates a new directory under `outputs/` by default and
prints the archive path. To checkpoint an active run, use
`.venv/bin/embodiedmind stop "$run"` with that path and wait for active work to
finish. Resume with the same config and the original archive path. This
command resumes the smoke example above.

```sh
.venv/bin/embodiedmind resume --config configs/smoke.yaml --output "$run" --parallel 1
```

Each finalized episode has a directory under `episodes/`. Failed and
interrupted attempts remain under `attempts/<episode-id>/<attempt-id>/`.
The runner records request and response events separately from completed steps
so a failed model call still has its inputs. Evaluator snapshots and native-size
frames are saved separately from the policy's observations.

After completion, a checkpoint, or an execution error, the runner builds
per-step CSVs, episode screenshots and GIFs, and a report with episode metrics,
coverage, comparisons, figures, and a SHA-256 index. Partial attempts get visuals
for the frames they captured. Use `package` to rebuild the report and visuals
from saved evidence without Ollama once the active runner has stopped.
Run `.venv/bin/embodiedmind package "$run"` to package the smoke archive. A hard kill leaves the already-written raw
files available for packaging or resume.

`outputs/` is eligible for Git, including archives and logs. Review the files
before staging them. The viewer discovers both `outputs/` and `results/runs/`.

## Agent variants

| Variants | Behavior |
| --- | --- |
| B0, B1, B2, B3 | Original reactive, bounded text-history, passive structured-memory, and belief-revision conditions. |
| B0G, B3G | Apply the same visible-obstacle guard to B0 and B3. |
| B4, B5 | Retrieve evidence for the current subgoal. B5 also resolves `approach`, `verify`, and `explore` proposals to primitive actions using the observed map. |
| B6, B7 | Compare a DoorKey routine extracted from successful development traces with a handwritten routine. |
| B8 | Remembers the observed hallway cue and uses guarded forward exploration. |
| B9N, B9 | Add progress-aware navigation. B9 also tracks verified task subgoals and interactions. |
| B10 | Grounds mission roles from observations, commits to exploration destinations, and verifies interactions such as opening a door or picking up an object. |
| B11, B11T, B11P, B11R, B11PA, B11C | Compare text history, passive or revising structured memory, fixed or adaptive verification, and a controller-only mode. |

B6 uses [configs/workflows.json](configs/workflows.json) by default. To build a
library from another development archive, use
`.venv/bin/embodiedmind learn-workflows RUN_DIR --output NEW_LIBRARY.json`.
Keep source seeds disjoint from evaluation seeds. The library retains routine
provenance and omits source-world coordinates from agent prompts.

[Development comparisons](reports/memory-48-development-20261114/README.md) · [B9 failure audit](reports/b9-failure-analysis-20261114/README.md) · [Matched B9–B10 report](outputs/memory-b10-stock-20261114-202808/report/b10-comparison.md)

## Reproduce the reports

### B11 fresh-seed campaign

The five source archives are checked in under `outputs/`. Rebuild the combined
analysis from the existing episode records without running inference. Run the
following from the repo root in Bash.

```bash
stamp=20261116-181345
report_dir=$(mktemp -d)
.venv/bin/embodiedmind report \
  "outputs/b11-rq-shift-$stamp" "outputs/b11-rq-static-$stamp" \
  "outputs/b11-stock-$stamp" "outputs/b11-shift-$stamp" \
  "outputs/b11-multiroom-80-$stamp" --output "$report_dir"
```

The saved [finalization log](outputs/b11-combined-20261116-181345/finalize.log)
records the coverage and checksum verification. Consult the five run manifests
for the exact source revisions, model configuration, and rosters used for the
published campaign. To start a new campaign with the current code, run
`bash scripts/run-b11.sh "$(date +%Y%m%d-%H%M%S)"` from a clean checkout with
the pinned Ollama model available. The script runs all five rosters. Reuse the
same timestamp and source revision to resume that new campaign.

### Original frozen B0–B3 study

The repository includes the [held-out results summary](reports/technical_report.md).
Resuming the original rosters requires their local `results/runs/` archive and
a clean checkout at the frozen source revision
`a44c34e0431322078a368453881366214993b900`. The study uses the locked environment,
the configured loopback Ollama model with its verified digest and 4096-token
context, one inference worker, and `BABYAI_DONE_ACTIONS` unset.

```sh
run=results/runs/embodiedmind-20261114-0428-ist
bash scripts/run_benchmarks.sh "$run"
.venv/bin/embodiedmind status "$run/static"
.venv/bin/embodiedmind status "$run/dynamic"
```

Use `.venv/bin/embodiedmind stop "$run/static"` or the corresponding dynamic
directory for a graceful checkpoint. Rerun the benchmark command at the
registered revision to reuse checksummed episodes. For a fresh experiment under
the original protocol, create the paired pilot under its own study directory
before launching the benchmark script.

See the [research proposal](RESEARCH_PROPOSAL.md) and [execution guide](AGENT_GUIDE.md)
for study design and run procedures.
