"""B1 retrieves a bounded natural-language history of legitimate observations."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from embodiedmind.agents.base import Agent
from embodiedmind.memory.episodic import EpisodicLog, Event
from embodiedmind.memory.retrieval import mission_terms, text_history_line

if TYPE_CHECKING:
    from embodiedmind.environments.observation_adapter import Observation


class TextMemory(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.log = EpisodicLog()

    def _observe(self, event: Event) -> None:
        self.log.append(event)
        self._audit["event"] = event.audit()

    def _memory_lines(self, obs: Observation) -> Iterable[tuple[str, dict | None]]:
        terms = mission_terms(obs.mission)
        for event in reversed(self.log.events[:-1]):
            yield text_history_line(event, terms)
