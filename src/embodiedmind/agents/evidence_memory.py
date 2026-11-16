"""Controlled semantic memory and verification policies using public observations."""

from embodiedmind.agents.mission_memory import MissionMemory
from embodiedmind.agents.text_memory import TextMemory
from embodiedmind.memory.belief import BeliefLedger
from embodiedmind.memory.spatial import DIRECTION_VECTORS, PassiveMap
from embodiedmind.reasoning.progress import route


B11_ARMS = {
    "B11": ("revising", "adaptive", True),
    "B11R": ("revising", "fixed", True),
    "B11PA": ("passive", "adaptive", True),
    "B11P": ("passive", "fixed", True),
    "B11T": ("text", "fixed", True),
    "B11C": ("revising", "adaptive", False),
}


class SemanticMemory:
    def __init__(self, mode):
        self.mode = mode
        self.active = {}
        self.visible = ()
        self.backend = {"revising": BeliefLedger(age_after=None), "passive": PassiveMap()}.get(mode)

    def add(self, facts, event):
        self.active.update(((f.segment, f.position), f) for f in facts)
        self.visible = facts
        return self.backend.add(facts, event) if self.backend else []

    def recall(self, segment):
        return self.backend.recall(segment) if self.backend else self.visible


class EvidenceMemory(MissionMemory):
    def __init__(self, arm):
        super().__init__()
        self.memory_mode, self.verification, self.use_model = B11_ARMS[arm]
        self.index = SemanticMemory(self.memory_mode)
        self.visibility = set()
        self.verify_actions = 0

    def _observe(self, event):
        super()._observe(event)
        self.visibility = {fact.position for fact in self.index.visible}
        if self.memory_mode != "revising":
            # The common geometry and live view are available for execution.
            # Absence notices, which retire a semantic claim, belong to revision.
            self._audit["ruled_out"] = []
        self._audit.update(memory_mode=self.memory_mode, verification_policy=self.verification)

    def _memory_lines(self, obs):
        if self.memory_mode == "text":
            yield from TextMemory._memory_lines(self, obs)
        else:
            yield from super()._memory_lines(obs)

    def navigation_facts(self):
        return [fact for (segment, _), fact in self.index.active.items()
                if segment == self.odometry.segment]

    def verify_action(self):
        target = self.target
        if not target or self.verify_actions >= 4 or self.operation not in {"face", "pickup", "toggle"}:
            return None
        point = tuple(target["position"])
        if point in self.visibility:
            return None
        age = self.step - target["last_verified_step"]
        path = route(self, [point])
        if self.verification == "adaptive" and age >= 2:
            # A side glance can observe the claim without walking up to it.
            east, south = (value - origin for value, origin in zip(point, self.odometry.position))
            for action, turn in ((0, -1), (1, 1)):
                dx, dy = DIRECTION_VECTORS[(self.odometry.direction + turn) % 4]
                if 1 <= east * dx + south * dy <= 3 and abs(-east * dy + south * dx) <= 2:
                    path = (action,)
                    break
        eligible = path and (len(path) <= 1 if self.verification == "fixed" else age >= 2 and len(path) <= 4)
        if not eligible:
            return None
        self.verify_actions += 1
        self._audit["verification"] = {
            "target": target, "path_length": len(path), "age": age, "used": self.verify_actions,
        }
        return path[0], "verify_remembered_target", path
