#!/usr/bin/env bash
# The study must be at the clean freeze commit. Existing validated jobs are reused.
set -euo pipefail
cd "$(dirname "$0")/.."
run="${1:?provide the existing study run root}"
if [[ -v BABYAI_DONE_ACTIONS ]]; then
  printf '%s\n' 'The frozen success semantics require BABYAI_DONE_ACTIONS to be unset.' >&2
  exit 1
fi
mkdir -p "$run"
exec 9>"$run/benchmark-coordinator.lock"
flock -n 9
bin=.venv/bin/embodiedmind
profile=configs/runtime.json

finish_queue() {
  local stage=$1
  local count=$2
  local output="$run/$stage"
  "$bin" resume --config "configs/$stage.yaml" --output "$output" --profile "$profile" --parallel 1
  "$bin" evaluate "$output" >"$run/$stage-coverage.tmp.json"
  .venv/bin/python scripts/verify_coverage.py "$run/$stage-coverage.tmp.json" "$count"
  mv "$run/$stage-coverage.tmp.json" "$run/$stage-coverage.json"
}

finish_queue static 240
finish_queue dynamic 270
.venv/bin/python scripts/render_evidence.py --output "$run/final-report/reproduced-evidence" \
  "$run/pilot" "$run/static" "$run/dynamic"
"$bin" report "$run/pilot" "$run/static" "$run/dynamic" --output "$run/final-report"
