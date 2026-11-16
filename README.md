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

## Results

### Automatic run archives

```sh
.venv/bin/embodiedmind run --config configs/smoke.yaml
.venv/bin/embodiedmind package outputs/<run-id>
```

`run` prints its new archive path under `outputs/`. Use `--output` to select
another path. Resume with the same config and the original path passed to
`resume --output`.

Each finalized episode has a directory under `episodes/`. Failed and
interrupted attempts remain under `attempts/<episode-id>/<attempt-id>/`.
The runner records request and response events separately from completed steps
so a failed model call still has its inputs. Evaluator snapshots and native-size
frames are saved separately from the policy's observations.

After completion, a checkpoint, or an execution error, the runner builds
per-step CSVs, episode screenshots and GIFs, and a report with episode metrics,
coverage, comparisons, figures, and a SHA-256 index. Partial attempts get visuals
for the frames they captured. Use `package` to rebuild the report and visuals
from saved evidence without Ollama. A hard kill leaves the already-written raw
files available for packaging or resume.

`outputs/` is eligible for Git, including archives and logs. Review the files
before staging them. The viewer discovers both `outputs/` and `results/runs/`.

### Experiment viewer

From the Ubuntu checkout, start the viewer and open <http://127.0.0.1:8765>.

```sh
.venv/bin/embodiedmind viewer
```

With the original study files under `results/runs/`, Replay opens DoorKey seed 1015
with B0 and B2 side by side, immediately before action 8. The boards show the
evaluator state and the logged agent observation separately. The action inspector
shows the hint, chosen action and outcome. Open **Model input and memory** and
select a spatial fact to locate it on the evaluator board. Replaying uses the
saved actions and checks the reconstructed observations and outcomes against
the trace. It does not call Ollama. Use `viewer --runs PATH` for another archive.

To see a live run, keep the viewer open and start a monitored run in another
terminal. Use a fresh directory for this development example:

```sh
.venv/bin/embodiedmind run --config configs/smoke.yaml \
  --output outputs/viewer-smoke --monitor
```

Open **Live monitor** or add `#live` to the viewer URL. It automatically
discovers and follows an active run. Select a run manually to pin it and use
**Follow active run** to resume automatic selection. Open completed runs in
**Replay**. The runner
publishes evaluator snapshots alongside the run and continues if you close
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

See the [held-out results summary](reports/technical_report.md) and [final run status](STATUS.md).

### Memory development modes

The original B0–B3 conditions still use the frozen action interface. B0G and
B3G add the same visible-obstacle guard to B0 and B3. B4 retrieves evidence
for the current subgoal. B5 adds `approach`, `verify`, and `explore` decisions
that resolve to a single primitive action using the observed map. B6 adds an
episode-independent DoorKey routine extracted from successful development traces.
B7 supplies a hand-written routine for comparison with B6.

```sh
.venv/bin/embodiedmind run --config configs/memory-doorkey-dev.yaml --monitor
.venv/bin/embodiedmind run --config configs/memory-relocation-dev.yaml --monitor
```

The viewer lists the new archives under **Replay** and **Live monitor**. The same
variants are available in **Sandbox**. B6 uses `configs/workflows.json` by
default. To build a library from another development archive, use
`embodiedmind learn-workflows RUN_DIR --output NEW_LIBRARY.json`. Keep the
source seeds disjoint from the evaluation seeds. The library contains routines
and provenance, with no source-world coordinates in the agent's prompt.
