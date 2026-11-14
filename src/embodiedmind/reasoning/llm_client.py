"""Local, frozen Ollama inference and request provenance."""

import json
import time
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from embodiedmind.reasoning.action_validator import ACTION_SCHEMA


class InferenceUnavailable(RuntimeError):
    """Infrastructure failed to return an inference response."""


@dataclass(frozen=True)
class Ollama:
    endpoint: str
    model: str
    digest: str
    quantization: str
    context: int
    output_tokens: int
    timeout: float

    def __post_init__(self):
        url = urlsplit(self.endpoint)
        if url.scheme != "http" or url.hostname not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("the experiment uses loopback Ollama")

    def call(self, path, payload=None):
        body = json.dumps(payload).encode() if payload is not None else None
        request = Request(self.endpoint.rstrip("/") + path, body, {"Content-Type": "application/json"})
        try:
            with urlopen(request, timeout=self.timeout) as response:
                result = json.load(response)
        except (HTTPError, URLError, OSError, ValueError) as exc:
            raise InferenceUnavailable(f"Ollama {path}: {exc}") from exc
        if not isinstance(result, dict) or result.get("error"):
            raise InferenceUnavailable(f"Ollama {path} returned error: {result}")
        return result

    def verify(self):
        version = self.call("/api/version")["version"]
        models = self.call("/api/tags")["models"]
        actual = next((model for model in models if model["name"] == self.model), None)
        if not actual or actual["digest"] != self.digest:
            raise InferenceUnavailable(f"required model digest missing for {self.model}")
        if actual["details"]["quantization_level"] != self.quantization:
            raise InferenceUnavailable(f"unexpected quantization: {actual['details']}")
        return {"version": version, "model": actual}

    def request(self, system, prompt, seed):
        return {
            "model": self.model, "system": system, "prompt": prompt, "stream": False,
            "format": ACTION_SCHEMA, "keep_alive": "15m",
            "options": {
                "seed": seed, "temperature": 0, "num_ctx": self.context,
                "num_predict": self.output_tokens,
            },
        }

    def generate(self, request):
        started = time.monotonic()
        response = self.call("/api/generate", request)
        if not isinstance(response.get("response"), str) or response.get("done") is not True:
            raise InferenceUnavailable("incomplete Ollama response")
        return response, time.monotonic() - started
