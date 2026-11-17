# Reproduce the experiments

The [quick start](../README.md#quick-start) covers the NVIDIA driver, locked Python environment and local Ollama setup. Use Bash on native Linux or Ubuntu under WSL2 for the runner scripts. The archived development environment used Python 3.12.16 and Ollama 0.40.16 on a GeForce RTX 5070 Ti Laptop GPU. Ollama serves the pinned [Qwen 2.5 3B Instruct configuration](../configs/models.yaml) at `127.0.0.1:11434` with Q4_K_M quantization and a 4096-token context.

## GPU troubleshooting

| Symptom | Check |
| --- | --- |
| GPU missing in WSL | From Windows, check that the distribution runs under WSL2 with `wsl -l -v` and that the NVIDIA driver supports the installed card. Update WSL if needed. In Ubuntu, try `/usr/lib/wsl/lib/nvidia-smi` if the command is missing from the shell path. The Windows host supplies the CUDA driver interface for WSL2. |
| GPU visible, Ollama reports CPU or split placement | Check that the CLI and experiment use the same Ollama server, inspect its logs, and check free VRAM in `nvidia-smi`. Close competing GPU workloads and verify the pinned model, one inference slot and 4096-token context. A clean loaded `ollama ps` row should report `100% GPU` for the registered profile. |
| Ollama runs out of memory | Model weights and the context cache share VRAM with other workloads. Larger models, longer contexts and parallel requests can exceed the development laptop’s 12 GB. Preserve the registered settings for reproduction. |
| The runner reports an unexpected digest or quantization | The tag can resolve to a different model revision. Compare the local model ID shown by `ollama list` with the prefix in `configs/models.yaml`. The runner checks the full digest and quantization using `/api/tags`. Restore the pinned artifact before running the registered comparison. |

The Python dependencies are defined by [pyproject.toml](../pyproject.toml) and [uv.lock](../uv.lock). GPU execution is supplied by the NVIDIA driver and Ollama. [NVIDIA WSL guide](https://docs.nvidia.com/cuda/wsl-user-guide/) · [Ollama hardware support](https://docs.ollama.com/gpu) · [Ollama GPU placement](https://docs.ollama.com/faq#how-can-i-tell-if-my-model-was-loaded-onto-the-gpu)

## Reproduce from saved artifacts

Use `viewer` for offline replay and `report` to regenerate analysis in a separate directory. The B11 campaign has five checked-in source archives.

```bash
stamp=20261116-181345
report_dir=$(mktemp -d)
.venv/bin/embodiedmind report \
  "outputs/b11-rq-shift-$stamp" "outputs/b11-rq-static-$stamp" \
  "outputs/b11-stock-$stamp" "outputs/b11-shift-$stamp" \
  "outputs/b11-multiroom-80-$stamp" --output "$report_dir"
```

The [combined report](../outputs/b11-combined-20261116-181345/report/report.md) links coverage, paired estimates and its artifact index. The [finalization log](../outputs/b11-combined-20261116-181345/finalize.log) records the coverage and checksum checks. The original B0–B3 raw archive remains under the local, Git-ignored `results/runs/` directory. With that bundle available, regenerate the report with:

```bash
run=results/runs/embodiedmind-20261114-0428-ist
report_dir=$(mktemp -d)
.venv/bin/embodiedmind report "$run/pilot" "$run/static" "$run/dynamic" --output "$report_dir"
```

For a run you own, `embodiedmind package RUN_DIR` also rebuilds its per-episode screenshots, replays and report after the runner has stopped. It writes into the archive. Use `report` with a separate output to review existing evidence without altering that archive.

## Repeat model-backed execution

### Original frozen B0–B3 study

Use the [frozen registration](../experiments/manifests/frozen-protocol.md), a clean checkout at `a44c34e0431322078a368453881366214993b900`, the locked environment, and the calibrated [runtime profile](../configs/runtime.json). The held-out command resumes the supplied study directory and requires the stock pilot evidence there. The runner checks the source, configuration and roster on resume, and verifies the runner, effective context and full GPU residency for the scored rosters.

```bash
unset BABYAI_DONE_ACTIONS
run=results/runs/embodiedmind-20261114-0428-ist
bash scripts/run_benchmarks.sh "$run"
.venv/bin/embodiedmind status "$run/static"
.venv/bin/embodiedmind status "$run/dynamic"
```

### B11 follow-up

The [B11 protocol](../experiments/manifests/b11-protocol.md) defines the five rosters, matched seeds and intervention schedules. Use the saved manifests to recover the exact source, config and lock hashes for each roster. The GoToShift mechanism archive records `7070c1df`. The remaining rosters record `9888e488`, which adds a plotting fallback and recovery behavior for packaging. The original `dirty` flags are part of the saved provenance. Use the [finalization log](../outputs/b11-combined-20261116-181345/finalize.log) to trace the recovery.

A fresh campaign at a chosen clean revision uses [run-b11.sh](../scripts/run-b11.sh), the configured loopback model and one inference slot. Choose a new timestamp for a fresh campaign. Reuse its timestamp and source revision to resume it.

```bash
unset BABYAI_DONE_ACTIONS
bash scripts/run-b11.sh "$(date +%Y%m%d-%H%M%S)"
```

## Archive layout and checkpoints

New experiments use an explicit path under `outputs/`. `status RUN_DIR` reads the heartbeat. `stop RUN_DIR` requests a graceful checkpoint. Resume with the same config, runtime settings and `resume --output RUN_DIR`.

Finalized episodes are stored under `episodes/<episode-id>/`. Attempt logs under `attempts/<episode-id>/<attempt-id>/` retain retry and failure evidence. The archive keeps agent-visible observations, model requests and responses, memory decisions, executed actions and telemetry. Evaluator state and native-resolution frames are stored separately. The manifest, coverage table and SHA-256 index support audits of completeness and artifact integrity.

[Study status and evidence](../STATUS.md) · [Experiment viewer](viewer.md)
