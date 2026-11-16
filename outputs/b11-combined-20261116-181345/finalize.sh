#!/usr/bin/env bash
set -euo pipefail
stamp=20261116-181345
root=outputs/b11-combined-$stamp
exec >>"$root/finalize.log" 2>&1
printf '[%s] Waiting for the benchmark service\n' "$(date --iso-8601=seconds)"
while systemctl --user is-active --quiet "embodiedmind-b11-recovery-$stamp"; do
    sleep 30
done
runs=()
for roster in rq-shift rq-static stock shift multiroom-80; do
    runs+=("outputs/b11-$roster-$stamp")
done
.venv/bin/python - "${runs[@]}" <<'PY'
import json
import sys
from pathlib import Path
for value in sys.argv[1:]:
    path = Path(value)
    manifest = json.loads((path / "manifest.json").read_text())
    expected = "7070c1df449dfecf24b45444a91707caffcc4825" if "b11-rq-shift-" in value else "9888e4881b26910a5f61cfea838829098d2b819d"
    if manifest["commit"] != expected:
        raise SystemExit(f"Frozen revision changed: {path}")
    beat = json.loads((path / "heartbeat.json").read_text())
    if beat["status"] != "complete" or beat["completed"] != beat["planned"] or beat["errors"]:
        raise SystemExit(f"Incomplete roster: {path} {beat}")
PY
for archive in "${runs[@]}"; do
    .venv/bin/embodiedmind report "$archive" --output "$archive/report"
done
.venv/bin/embodiedmind report "${runs[@]}" --output "$root/report"
.venv/bin/python - "$root/report" <<'PY'
import hashlib
import json
import sys
from pathlib import Path
report = Path(sys.argv[1])
coverage = json.loads((report / "coverage.json").read_text())
if coverage["planned"] != 3090 or coverage["valid"] != 3090:
    raise SystemExit(f"Unexpected coverage: planned {coverage['planned']}, valid {coverage['valid']}")
index = json.loads((report / "artifact-index.json").read_text())
for entry in index["files"]:
    with (report.parent / entry["path"]).open("rb") as handle:
        expected = hashlib.file_digest(handle, "sha256").hexdigest()
    if expected != entry["sha256"]:
        raise SystemExit(f"Checksum mismatch: {entry['path']}")
print(f"Verified all 3090 episodes and {len(index['files'])} indexed artifacts.")
PY
printf '[%s] Combined benchmark verified\n' "$(date --iso-8601=seconds)"
