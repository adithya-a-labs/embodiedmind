"""B3 records observed facts, ages movable facts, and preserves revisions."""

from __future__ import annotations

from dataclasses import replace
from typing import TYPE_CHECKING

from embodiedmind.memory.spatial import Fact, Geometry

if TYPE_CHECKING:
    from embodiedmind.memory.episodic import Event

STALE_AFTER_STEPS = 12
CHANGEABLE = frozenset({"ball", "box", "door", "key"})


class BeliefLedger:
    def __init__(self) -> None:
        self.active: dict[tuple[int, Geometry], Fact] = {}
        self.history: list[Fact] = []

    def add(self, facts: tuple[Fact, ...], event: Event) -> list[dict]:
        revisions = []
        for fact in facts:
            key = fact.segment, fact.position
            previous = self.active.get(key)
            if previous is None:
                self.active[key] = fact
            elif previous.appearance == fact.appearance:
                self.active[key] = previous.verify(event)
            else:
                contradicted = replace(previous, status="CONTRADICTED")
                replacement = replace(fact, contradicts_fact_id=previous.id)
                self.history.append(contradicted)
                self.active[key] = replacement
                revisions.append({
                    "reason": "direct_observation",
                    "previous": contradicted.audit(),
                    "replacement": replacement.audit(),
                })

        for key, fact in self.active.items():
            if (
                fact.status == "OBSERVED"
                and fact.appearance[0] in CHANGEABLE
                and event.step - fact.last_verified_step >= STALE_AFTER_STEPS
            ):
                stale = replace(fact, status="STALE")
                self.active[key] = stale
                revisions.append({"reason": "age", "previous": fact.audit(), "replacement": stale.audit()})

        return revisions

    def recall(self, segment: int) -> list[Fact]:
        return [fact for fact in self.active.values() if fact.segment == segment]
