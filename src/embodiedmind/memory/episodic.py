"""Append-only evidence from the policy's public input and executed actions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from embodiedmind.environments.observation_adapter import Observation


@dataclass(frozen=True, slots=True)
class Event:
    step: int
    observation: Observation
    previous_action: int | None
    moved: bool | None

    @property
    def id(self) -> str:
        return f"o{self.step}"

    def audit(self) -> dict:
        return {
            "id": self.id,
            "step": self.step,
            "previous_action": self.previous_action,
            "moved": self.moved,
        }


class EpisodicLog:
    def __init__(self) -> None:
        self.events: list[Event] = []

    def append(self, event: Event) -> None:
        if event.step < 0 or (self.events and event.step <= self.events[-1].step):
            raise ValueError("memory observations must advance in episode step order")
        self.events.append(event)
