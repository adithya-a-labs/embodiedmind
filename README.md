# EmbodiedMind

EmbodiedMind studies how agents use memory and revise beliefs while navigating symbolic, partially observable MiniGrid and BabyAI worlds. Experiments pair agents on the same seeded missions and track mission success, actions, and inference cost. Policies receive agent-visible observations. Full board state is recorded separately for evaluation and replay.

## Results

The original frozen B0–B3 study completed **240 static and 270 dynamic held-out episodes**. Compared with bounded text history, revising memory solved 8/30 versus 4/30 DoorKey layouts and tied at 5/30 on GoToObj Maze. The reactive baseline solved 17/30 DoorKey layouts. The relocation comparison recorded three explicitly cited stale actions for B3 and zero for B2. [Frozen protocol](experiments/manifests/frozen-protocol.md) · [Held-out results](reports/technical_report.md) · [Original run status](STATUS.md)

The B11 follow-up completed **3,090 valid fresh-seed episodes** across five rosters. The broad comparison covers 15 policies, 11 stock games, and three GoToShift conditions. The separate mechanism rosters compare memory representation, belief revision, verification, and model contribution under a shared executor.

| Comparison | Result |
| --- | --- |
| Broad benchmark at 48 actions | B10 and B11 each solved **115/140** episodes. B11 used **2.4% fewer total tokens**. |
| MultiRoom at 48 and 80 actions | B10 and B11 both improved from **6/10 to 10/10** on the same layouts. |
| Belief revision under GoToShift relocation | Fixed-verification success rose from **8/30 to 23/30**, and stale route commitments fell from **543 to zero**. Text history solved **30/30** on the same relocation roster. |
| Fixed versus adaptive verification | Revising arms executed identical action sequences in **150/150** pairs. Passive arms matched in **90/90** GoToShift pairs. |
| Model-enabled B11 versus controller-only B11C | All **150/150** paired action sequences matched. Each solved **125/150** and B11C made zero model calls. |

The broad results compare complete policies on ten seeds per condition. The mechanism results use 30 matched seeds per condition and apply to the registered executor and tasks. The B11 archive preserves the single retried infrastructure attempt alongside all finalized episodes and includes a verified SHA-256 index.

[B11 protocol](experiments/manifests/b11-protocol.md) · [Combined report](outputs/b11-combined-20261116-181345/report/report.md) · [Paired comparisons](outputs/b11-combined-20261116-181345/report/comparisons.csv) · [Coverage](outputs/b11-combined-20261116-181345/report/coverage.json)

## Quick start

Use Ubuntu or Ubuntu on WSL and the locked Python 3.12 environment. These commands install dependencies, run the tests, and check a seeded environment without Ollama.

```sh
uv sync --locked --inexact
.venv/bin/python -m pytest -q
.venv/bin/embodiedmind smoke --env BabyAI-GoToObjS6-v1 --seed 42
```

For model-backed runs, start local Ollama with the model and digest in [configs/models.yaml](configs/models.yaml). Keep `BABYAI_DONE_ACTIONS` unset and use one inference worker for the registered comparisons. This smoke run exercises inference and writes a new archive.

```sh
run="outputs/smoke-$(date +%Y%m%d-%H%M%S)"
.venv/bin/embodiedmind run --config configs/smoke.yaml --output "$run" --monitor --parallel 1
.venv/bin/embodiedmind status "$run"
```

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
