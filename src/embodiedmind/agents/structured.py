"""B2 recalls public clues from an episodic log and an unrevised spatial map."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from embodiedmind.agents.base import Agent
from embodiedmind.memory.episodic import EpisodicLog, Event
from embodiedmind.memory.retrieval import fact_priority, mission_terms
from embodiedmind.memory.spatial import HEADINGS, Odometry, PassiveMap, perceived_facts

if TYPE_CHECKING:
    from embodiedmind.environments.observation_adapter import Observation
    from embodiedmind.memory.belief import BeliefLedger


class Structured(Agent):
    def __init__(self, index: PassiveMap | BeliefLedger | None = None) -> None:
        super().__init__()
        self.log = EpisodicLog()
        self.odometry = Odometry()
        self.index = index if index is not None else PassiveMap()

    def _observe(self, event: Event) -> None:
        self.log.append(event)
        self.odometry.update(event)
        facts = perceived_facts(event, self.odometry)
        self._audit["event"] = {
            **event.audit(),
            "position": list(self.odometry.position),
            "segment": self.odometry.segment,
            "direction": self.odometry.direction,
        }
        self._audit["visible_facts"] = [fact.audit() for fact in facts]
        self._audit["revisions"] = self.index.add(facts, event)

    def _memory_lines(self, obs: Observation) -> Iterable[tuple[str, dict | None]]:
        origin = self.odometry.position
        facts = self.index.recall(self.odometry.segment)
        terms = mission_terms(obs.mission)
        viewed = {self.odometry.locate(cell.forward, cell.right) for cell in obs.cells}
        viewed.add(origin)

        yield "Remembered cells use (forward,right) offsets from your current position.", None
        for fact in sorted(facts, key=lambda fact: fact_priority(fact, terms, origin)):
            if fact.position in viewed:
                continue
            kind, color, state = fact.appearance
            appearance = " ".join(value for value in (color, kind, state) if value)
            relative = self.odometry.relative_to_view(fact.position)
            qualifier = "STALE; reobserve" if fact.status == "STALE" else "observed"
            yield (
                f"{fact.id} {appearance} {relative} {qualifier} at step {fact.last_verified_step}",
                {**fact.audit(), "relative": list(relative)},
            )
