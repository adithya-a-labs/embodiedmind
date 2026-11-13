"""Deterministic retrieval under a shared, conservative byte budget."""

from __future__ import annotations

import re
from collections.abc import Iterable

from embodiedmind.memory.episodic import Event
from embodiedmind.memory.spatial import Fact


def mission_terms(mission: str) -> set[str]:
    return set(re.findall(r"[a-z]+", mission.lower()))


def ascii_line(text: str) -> str:
    return " ".join(text.encode("ascii", errors="backslashreplace").decode("ascii").split())


def fit_lines(
    lines: Iterable[tuple[str, dict | None]], byte_budget: int
) -> tuple[str, list[dict]]:
    if byte_budget < 0:
        raise ValueError("memory budget must be nonnegative")
    used = 0
    selected = []
    rendered = []
    for line, evidence in lines:
        packed = ascii_line(line)
        if not packed:
            continue
        cost = len(packed) + bool(rendered)
        if cost > byte_budget - used:
            continue
        rendered.append(packed)
        used += cost
        if evidence is not None:
            selected.append(evidence)
    return "\n".join(rendered), selected


def fact_priority(fact: Fact, terms: set[str], position: tuple[int, int]) -> tuple:
    kind, color, _ = fact.appearance
    distance = sum(abs(value - origin) for value, origin in zip(fact.position, position))
    return (
        kind not in terms,
        color not in terms,
        kind in {"wall", "floor", "empty"},
        fact.status == "STALE",
        distance,
        -fact.last_verified_step,
        fact.id,
    )


def text_history_line(event: Event, terms: set[str]) -> tuple[str, dict]:
    visible = [cell for cell in event.observation.cells if cell.object not in {"empty", "wall", "floor"}]
    visible.sort(key=lambda cell: (cell.object not in terms, cell.color not in terms, cell.forward, abs(cell.right)))
    cells = []
    descriptions = []
    for cell in visible[:4]:
        appearance = " ".join(value for value in (cell.color, cell.object, cell.state) if value)
        descriptions.append(f"{appearance}@{cell.forward},{cell.right}")
        cells.append({
            "forward": cell.forward,
            "right": cell.right,
            "object": cell.object,
            "color": cell.color,
            "state": cell.state,
        })
    prior = f" prev={event.previous_action}" if event.previous_action is not None else ""
    seen = "; ".join(descriptions) if descriptions else "no named objects"
    line = f"{event.id} step {event.step}{prior} facing={event.observation.direction}: {seen}"
    return line, {**event.audit(), "direction": event.observation.direction, "cells": cells}
