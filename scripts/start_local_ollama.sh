#!/usr/bin/env bash
# Start an isolated Ollama instance for this run. Track its PID and verify the endpoint before use.
set -euo pipefail
parallel="${1:?use 1 or 2 slots}"
directory="${2:?provide run directory}"
port="${3:-11435}"
mkdir -p "$directory"
if [[ -f "$directory/ollama.pid" ]] && kill -0 "$(cat "$directory/ollama.pid")" 2>/dev/null; then
  printf '%s\n' 'A run-owned Ollama process is already recorded.' >&2
  exit 1
fi
if curl -fsS --max-time 1 "http://127.0.0.1:$port/api/version" >/dev/null 2>&1; then
  printf '%s\n' 'Loopback port already in use.' >&2
  exit 1
fi
OLLAMA_HOST="127.0.0.1:$port" \
OLLAMA_NUM_PARALLEL="$parallel" \
OLLAMA_MAX_LOADED_MODELS=1 \
OLLAMA_MAX_QUEUE=4 \
OLLAMA_NO_CLOUD=1 \
OLLAMA_MODELS="${OLLAMA_MODELS:-/usr/share/ollama/.ollama/models}" \
nohup ollama serve >"$directory/ollama.log" 2>&1 </dev/null &
pid=$!
printf '%s\n' "$pid" >"$directory/ollama.pid"
for attempt in $(seq 1 40); do
  curl -fsS --max-time 1 "http://127.0.0.1:$port/api/version" && exit 0
  kill -0 "$pid" || exit 1
  sleep 0.25
done
kill "$pid" || true
exit 1
