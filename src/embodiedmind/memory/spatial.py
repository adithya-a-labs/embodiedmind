"""Construct an episode-relative map without simulator state."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from embodiedmind.memory.episodic import Event

HEADINGS = ("east", "south", "west", "north")
DIRECTION_VECTORS = ((1, 0), (0, 1), (-1, 0), (0, -1))
Geometry = tuple[int, int]
Appearance = tuple[str, str, str]


@dataclass(slots=True)
class Odometry:
    position: Geometry = (0, 0)
    direction: int = 0
    segment: int = 0

    def update(self, event: Event) -> None:
        if event.previous_action == 2:
            if event.moved is True:
                east, south = self.position
                delta_east, delta_south = DIRECTION_VECTORS[self.direction]
                self.position = east + delta_east, south + delta_south
            elif event.moved is None:
                self.segment += 1
                self.position = (0, 0)
        self.direction = event.observation.direction

    def locate(self, forward: int, right: int) -> Geometry:
        east, south = self.position
        heading_east, heading_south = DIRECTION_VECTORS[self.direction]
        right_east, right_south = DIRECTION_VECTORS[(self.direction + 1) % 4]
        return (
            east + forward * heading_east + right * right_east,
            south + forward * heading_south + right * right_south,
        )

    def relative_to_view(self, position: Geometry) -> Geometry:
        east, south = (value - origin for value, origin in zip(position, self.position))
        heading_east, heading_south = DIRECTION_VECTORS[self.direction]
        right_east, right_south = DIRECTION_VECTORS[(self.direction + 1) % 4]
        return (
            east * heading_east + south * heading_south,
            east * right_east + south * right_south,
        )


@dataclass(frozen=True, slots=True)
class Fact:
    id: str
    segment: int
    position: Geometry
    appearance: Appearance
    observed_at_step: int
    last_verified_step: int
    source_event_ids: tuple[str, ...]
    status: str = "OBSERVED"
    contradicts_fact_id: str | None = None

    def verify(self, event: Event) -> Fact:
        return replace(
            self,
            last_verified_step=event.step,
            source_event_ids=(*self.source_event_ids, event.id),
            status="OBSERVED",
        )

    def audit(self) -> dict:
        kind, color, state = self.appearance
        return {
            "id": self.id,
            "segment": self.segment,
            "position": list(self.position),
            "object": kind,
            "color": color,
            "state": state,
            "observed_at_step": self.observed_at_step,
            "last_verified_step": self.last_verified_step,
            "source_event_ids": list(self.source_event_ids),
            "status": self.status,
            "contradicts_fact_id": self.contradicts_fact_id,
        }


def perceived_facts(event: Event, odometry: Odometry) -> tuple[Fact, ...]:
    return tuple(
        Fact(
            id=f"f{event.step}.{index}",
            segment=odometry.segment,
            position=odometry.locate(cell.forward, cell.right),
            appearance=(cell.object, cell.color, cell.state),
            observed_at_step=event.step,
            last_verified_step=event.step,
            source_event_ids=(event.id,),
        )
        for index, cell in enumerate(event.observation.cells)
    )


class PassiveMap:
    """B2 indexes all observed distinct facts and does not retract contradictions."""

    def __init__(self) -> None:
        self.facts: dict[tuple[int, Geometry, Appearance], Fact] = {}

    def add(self, facts: tuple[Fact, ...], event: Event) -> list[dict]:
        for fact in facts:
            key = fact.segment, fact.position, fact.appearance
            previous = self.facts.get(key)
            self.facts[key] = previous.verify(event) if previous else fact
        return []

    def recall(self, segment: int) -> list[Fact]:
        return [fact for fact in self.facts.values() if fact.segment == segment]
