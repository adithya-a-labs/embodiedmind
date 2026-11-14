"""B3 adds explicit belief revision and compact working memory."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from embodiedmind.agents.structured import Structured
from embodiedmind.memory.belief import BeliefLedger
from embodiedmind.memory.retrieval import ascii_line

if TYPE_CHECKING:
    from embodiedmind.environments.observation_adapter import Observation


class Hybrid(Structured):
    def __init__(self) -> None:
        super().__init__(BeliefLedger())
        self.intent: str | None = None

    def record_decision(self, action: int, intent: str | None = None) -> None:
        del action
        self.intent = ascii_line(intent)[:100] if intent else None

    def _memory_lines(self, obs: Observation) -> Iterable[tuple[str, dict | None]]:
        event = self.log.events[-1]
        if event.previous_action is not None:
            action = ("left", "right", "forward", "pickup", "drop", "toggle", "done")[event.previous_action]
            outcome = " moved" if event.moved is True else " blocked" if event.moved is False else ""
            yield f"Previous action: {action}{outcome}.", None
        if self.intent:
            yield f"Prior model intent (unverified): {self.intent}", None
        for revision in self._audit["revisions"]:
            old = revision["previous"]
            if revision["reason"] == "direct_observation" and old["object"] in {"ball", "box", "door", "key"}:
                relative = self.odometry.relative_to_view(tuple(old["position"]))
                description = " ".join(value for value in (old["color"], old["object"], old["state"]) if value)
                yield f"{old['id']} contradicted: {description} at {relative}. Reobserve before use.", old
        yield from super()._memory_lines(obs)
