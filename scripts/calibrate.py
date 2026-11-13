"""Measure local development inference with one and two concurrent clients."""

import argparse
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

import yaml

from embodiedmind.environments.factory import make_environment
from embodiedmind.environments.observation_adapter import adapt_observation
from embodiedmind.reasoning.action_validator import parse_action
from embodiedmind.reasoning.llm_client import Ollama
from embodiedmind.reasoning.prompts import SYSTEM, prompt_for


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--parallel", type=int, required=True, choices=(1, 2))
    args = parser.parse_args()
    cfg = yaml.safe_load(open("configs/models.yaml", encoding="utf-8"))
    cfg.pop("temperature")
    cfg["endpoint"] = args.endpoint
    model = Ollama(**cfg)
    versions = model.verify()
    requests = []
    env = make_environment("BabyAI-GoToObjMazeS7-v0")
    try:
        for seed in range(12):
            obs = adapt_observation(env.reset(seed=seed)[0])
            padding = "f9.8 last observed green key at local (-1,2). " * 18
            requests.append(model.request(SYSTEM, prompt_for(obs, padding), seed))
    finally:
        env.close()
    model.generate(requests[0])
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=args.parallel) as executor:
        responses = list(executor.map(model.generate, requests))
    elapsed = time.monotonic() - start
    active = model.call("/api/ps")["models"]
    gpu = subprocess.check_output(
        ["nvidia-smi", "--query-gpu=memory.total,memory.free,temperature.gpu", "--format=csv,noheader,nounits"],
        text=True,
    ).strip()
    print(json.dumps({
        "parallel": args.parallel, "seconds": elapsed, "requests_per_minute": len(requests) / elapsed * 60,
        "valid": sum(parse_action(raw["response"]).valid for raw, _ in responses),
        "responses": [raw["response"] for raw, _ in responses],
        "prompt_tokens": [raw["prompt_eval_count"] for raw, _ in responses],
        "seconds_per_request": [seconds for _, seconds in responses],
        "active": active, "gpu_total_free_temperature": gpu,
        "version": versions["version"],
    }, indent=2))


if __name__ == "__main__":
    main()
