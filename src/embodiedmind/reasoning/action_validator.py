"""Validate the shared model action schema and apply one fixed fallback."""

import json
from dataclasses import dataclass


ACTION_NAMES = ("left", "right", "forward", "pickup", "drop", "toggle", "done")
FALLBACK_ACTION = 1  # rotate right to acquire a new public view
ACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "action": {"type": "integer", "minimum": 0, "maximum": 6},
        "evidence": {"type": "string", "maxLength": 120},
    },
    "required": ["action", "evidence"],
    "additionalProperties": False,
}


@dataclass(frozen=True, slots=True)
class ActionDecision:
    action: int
    evidence: str
    valid: bool
    error: str | None = None


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result = dict(pairs)
    if len(result) != len(pairs):
        raise ValueError("duplicate JSON keys")
    return result


def parse_action(response: str) -> ActionDecision:
    try:
        value = json.loads(response, object_pairs_hook=_unique_object)
    except (TypeError, ValueError, RecursionError):
        return ActionDecision(FALLBACK_ACTION, "", False, "invalid_json")
    if not isinstance(value, dict) or set(value) != {"action", "evidence"}:
        return ActionDecision(FALLBACK_ACTION, "", False, "invalid_fields")
    action, evidence = value["action"], value["evidence"]
    if type(action) is not int or action not in range(len(ACTION_NAMES)):
        return ActionDecision(FALLBACK_ACTION, "", False, "invalid_action")
    if not isinstance(evidence, str) or len(evidence) > 120 or (evidence and not evidence.isprintable()):
        return ActionDecision(FALLBACK_ACTION, "", False, "invalid_evidence")
    return ActionDecision(action, evidence, True)
