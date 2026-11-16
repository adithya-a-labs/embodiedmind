#!/usr/bin/env bash
set -euo pipefail

stamp=${1:?Pass a unique archive timestamp}
[[ $stamp =~ ^[0-9]{8}-[0-9]{6}$ ]]
cd "$(git rev-parse --show-toplevel)"
git diff --quiet HEAD -- . ':(top,exclude)outputs'
cli=.venv/bin/embodiedmind

for roster in rq-shift rq-static stock shift multiroom-80; do
    root="outputs/b11-$roster-$stamp"
    mkdir -p "$root"
    if [[ -f "$root/heartbeat.json" ]] && .venv/bin/python -c '
import json
import sys
from pathlib import Path
beat = json.loads(Path(sys.argv[1]).read_text())
raise SystemExit(beat["status"] != "complete" or beat["completed"] != beat["planned"] or bool(beat["errors"]))
' "$root/heartbeat.json"; then
        "$cli" package "$root"
        continue
    fi
    verb=run
    if [[ -f "$root/manifest.json" ]]; then
        verb=resume
    fi
    cmd=("$cli" "$verb" --config "configs/b11-$roster.yaml" --output "$root" --monitor --parallel 1)
    printf '[%s] %s\n' "$(date --iso-8601=seconds)" "${cmd[*]}" >>"$root/command.log"
    status=0
    "${cmd[@]}" >>"$root/stdout.log" 2>>"$root/stderr.log" || status=$?
    printf '[%s] runner exit %d\n' "$(date --iso-8601=seconds)" "$status" >>"$root/command.log"
    if (( status != 0 )); then
        exit "$status"
    fi
    .venv/bin/python -c '
import json
import sys
from pathlib import Path
beat = json.loads(Path(sys.argv[1]).read_text())
if beat["status"] != "complete":
    raise SystemExit("Archive has unfinished work")
' "$root/heartbeat.json"
done
