"""Common policy-visible interface for the experimental memory conditions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from embodiedmind.memory.episodic import Event
from embodiedmind.memory.retrieval import fit_lines

if TYPE_CHECKING:
    from collections.abc import Iterable

    from embodiedmind.environments.observation_adapter import Observation


class Agent:
    def __init__(self) -> None:
        self.step: int | None = None
        self._audit: dict = {"event": None, "selected_facts": [], "revisions": [], "context_bytes": 0}

    def observe(
        self,
        obs: Observation,
        step: int,
        prev_action: int | None = None,
        moved: bool | None = None,
    ) -> None:
        if step < 0 or (self.step is not None and step <= self.step):
            raise ValueError("agent observations must advance in episode step order")
        event = Event(step, obs, prev_action, moved)
        self.step = step
        self._audit = {
            "event": {"id": event.id, "step": event.step},
            "selected_facts": [],
            "revisions": [],
            "context_bytes": 0,
        }
        self._observe(event)

    def _observe(self, event: Event) -> None:
        pass

    def _memory_lines(self, obs: Observation) -> Iterable[tuple[str, dict | None]]:
        return ()

    def context(self, obs: Observation, byte_budget: int) -> str:
        if self.step is None:
            raise ValueError("observe the current step before building policy context")
        text, selected = fit_lines(self._memory_lines(obs), byte_budget)
        self._audit["selected_facts"] = selected
        self._audit["context_bytes"] = len(text)
        return text

    def record_decision(self, action: int, intent: str | None = None) -> None:
        """Allow memory variants to retain the previous policy-selected subgoal."""

    def audit(self) -> dict:
        return dict(self._audit)
