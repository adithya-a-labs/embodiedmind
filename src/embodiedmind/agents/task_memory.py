"""Observation-grounded task state for B9 and its navigation control."""

from collections import Counter
import re

from embodiedmind.agents.cue_memory import CueMemory
from embodiedmind.agents.grounded import GroundedMemory
from embodiedmind.reasoning.prompts import MEMORY_MISSION


class ProgressMemory(CueMemory):
    def __init__(self):
        super().__init__()
        self.visits = Counter()

    def _record_pose(self):
        self.visits[self.odometry.segment, self.odometry.position, self.odometry.direction] += 1

    def _observe(self, event):
        super()._observe(event)
        self._record_pose()


class TaskMemory(ProgressMemory):
    def __init__(self):
        super().__init__()
        self.phase = None
        self.target = None
        self.reference = None
        self.unlocked = False

    def _observe(self, event):
        # The hallway uses geometric provenance instead of B8's singleton scan.
        GroundedMemory._observe(self, event)
        self._record_pose()
        obs = event.observation
        if obs.mission == MEMORY_MISSION:
            self._hallway()
        elif obs.mission == "pick up the ball":
            self._corridor(obs)
        else:
            match = re.fullmatch(r"put the (\w+) (key|ball|box) next to the (\w+) (key|ball|box)", obs.mission)
            if match:
                self._placement(obs, match.groups())
        if self.phase:
            self._audit.update(subgoal=self.phase, task_phase=self.phase,
                               task_target=self.target, task_reference=self.reference)

    def _matching(self, kind, color=None):
        here = self.odometry.position
        candidates = [
            f for f in self.index.recall(self.odometry.segment)
            if f.appearance[0] == kind and (color is None or f.appearance[1] == color)
        ]
        return sorted(candidates, key=lambda f: (
            sum(abs(a - b) for a, b in zip(f.position, here)), -f.last_verified_step, f.id,
        ))

    def _corridor(self, obs):
        doors = self._matching("door")
        locked = next((f for f in doors if f.appearance[2] == "locked"), None)
        balls = self._matching("ball")
        carried = obs.carrying
        if carried and carried.object == "key" and self.target and self.phase == "Unlock matching door":
            door = self.index.active.get((self.odometry.segment, tuple(self.target["position"])))
            self.unlocked |= bool(door and door.appearance == ("door", carried.color, "open"))
        if balls and (self.unlocked or not carried):
            self.phase, self.target = "Pick up target ball", balls[0].audit()
        elif carried and carried.object == "key":
            self.phase = "Unlock matching door"
            self.target = locked.audit() if locked and locked.appearance[1] == carried.color else None
            if self.target is None:
                self.phase = "Find locked door or target ball"
        else:
            self.phase = "Find and pick up key"
            keys = self._matching("key", locked.appearance[1] if locked else None)
            self.target = keys[0].audit() if keys else None

    def _placement(self, obs, source):
        color, kind, ref_color, ref_kind = source
        items = self._matching(kind, color)
        references = self._matching(ref_kind, ref_color)
        self.reference = references[0].audit() if references else None
        holding = obs.carrying and (obs.carrying.color, obs.carrying.object) == (color, kind)
        if holding:
            self.phase, self.target = "Place beside reference", None
        else:
            self.phase = "Find and pick up source"
            self.target = items[0].audit() if items else None

    def _hallway(self):
        segment = self.odometry.segment
        facts = self.index.recall(segment)
        objects = [f for f in facts if f.appearance[0] in {"key", "ball"}]
        if segment != 0:
            self.cue = self.branch = None
        else:
            # Stock Memory starts on the hallway centerline. The cue is one
            # tile north of it, while the fork objects are two tiles away.
            cue = next((f for f in objects if f.position[1] == -1), None)
            self.cue = cue.audit() if cue else None
            branch = next((f for f in objects if cue and abs(f.position[1]) == 2
                           and f.appearance[0] == cue.appearance[0]), None)
            self.branch = branch.audit() if branch else None
        self.scanning = False
        self.phase = "Choose matching branch" if self.branch else (
            "Find hallway fork" if self.cue else "Find start-room cue"
        )
        self._audit.update(hallway_cue=self.cue, hallway_branch=self.branch, hallway_scanning=False)

    def _memory_lines(self, obs):
        for label, fact in (("Task target", self.target), ("Reference object", self.reference)):
            if fact:
                yield f"{label} {fact['id']}: {fact['color']} {fact['object']}.", fact
        yield from super()._memory_lines(obs)
