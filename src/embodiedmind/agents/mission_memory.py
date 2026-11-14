"""B10 task roles and navigation state from public evidence."""

import re

from embodiedmind.agents.task_memory import TaskMemory
from embodiedmind.reasoning.progress import adjacent
from embodiedmind.reasoning.prompts import DYNAMIC_OBSTACLES_MISSION, MEMORY_MISSION


_COLORS = "red|green|blue|purple|yellow|grey"
_OBJECT = rf"(?:the |a |an )?(?:({_COLORS}) )?(key|ball|box|door)"
_SIMPLE = re.compile(rf"(go to|open|pick up) {_OBJECT}")
_PLACEMENT = re.compile(rf"put {_OBJECT} next to {_OBJECT}")


class MissionMemory(TaskMemory):
    def __init__(self):
        super().__init__()
        self.operation = None
        self.frontier = None
        self.exhausted = set()
        self.failed_interactions = {}
        self.last_interaction = None

    def _observe(self, event):
        old_phase = self.phase
        super()._observe(event)
        obs = event.observation
        mission = obs.mission
        self.operation = None
        if mission.startswith("use the key to open the door"):
            self._unlock(obs, "goal")
        elif mission == "pick up the box":
            self._unlock(obs, "box")
        elif mission == "traverse the rooms to get to the goal":
            self._set_goal("Reach goal through the rooms", "stand", self._first("goal"))
        elif mission not in {MEMORY_MISSION, DYNAMIC_OBSTACLES_MISSION, "pick up the ball"}:
            placement = _PLACEMENT.fullmatch(mission)
            simple = _SIMPLE.fullmatch(mission)
            if placement:
                self._placement(obs, placement.groups())
                self.operation = "place" if self.phase == "Place beside reference" else "pickup"
            elif simple:
                verb, color, kind = simple.groups()
                operation = {"go to": "face", "open": "toggle", "pick up": "pickup"}[verb]
                target = next((fact for fact in self._matching(kind, color)
                               if operation != "toggle" or fact.appearance[2] != "open"), None)
                self._set_goal(mission, operation, target)
        if old_phase != self.phase:
            self.frontier = None
            self.exhausted.clear()
        if self.last_interaction is not None:
            operation, point, before = self.last_interaction
            current = (obs.carrying, obs.cell(1, 0))
            if current == before:
                self.failed_interactions[operation, point] = current
            else:
                self._audit["verified_interaction"] = operation
            self.last_interaction = None
        self._audit.update(subgoal=self.phase or self._audit["subgoal"], task_phase=self.phase,
                           operation=self.operation, task_target=self.target, task_reference=self.reference)

    def _first(self, kind, color=None):
        return next(iter(self._matching(kind, color)), None)

    def _set_goal(self, phase, operation, fact=None):
        self.phase, self.operation = phase, operation
        self.target = fact.audit() if fact else None

    def _unlock(self, obs, objective):
        locked = next((door for door in self._matching("door") if door.appearance[2] == "locked"), None)
        carried = obs.carrying
        if objective == "box" and locked:
            blocker = next((ball for ball in self._matching("ball")
                            if ball.position in adjacent(locked.position)), None)
            if carried and carried.object == "ball":
                self._set_goal("Relocate the doorway blocker", "drop_blocker", locked)
                return
            if blocker and carried:
                self._set_goal("Free carrying slot for the blocker", "drop_key", locked)
                return
            if blocker and not carried:
                self._set_goal("Pick up doorway blocker", "pickup", blocker)
                return
        if locked and carried and (carried.object, carried.color) == ("key", locked.appearance[1]):
            self._set_goal("Unlock matching door", "toggle", locked)
        elif locked and not carried:
            self._set_goal("Find matching key", "pickup", self._first("key", locked.appearance[1]))
        elif objective == "goal" and (carried or self.crossed_door):
            goal = self._first("goal")
            opened = next((door for door in self._matching("door") if door.appearance[2] == "open"), None)
            self._set_goal("Reach goal beyond the door", "stand",
                           goal or (opened if not self.crossed_door else None))
        elif objective == "box" and (box := self._first("box")):
            self._set_goal("Free carrying slot" if carried else "Pick up target box",
                           "drop_key" if carried else "pickup", box)
        elif not carried and not any(door.appearance[2] == "open" for door in self._matching("door")):
            self._set_goal("Find and pick up key", "pickup", self._first("key"))
        else:
            self._set_goal("Find the destination", "search")
