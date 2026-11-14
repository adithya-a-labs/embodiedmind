"""B8 retains a hallway cue and tracks repeated exploration."""

from embodiedmind.agents.grounded import GroundedMemory
from embodiedmind.reasoning.prompts import MEMORY_MISSION


class CueMemory(GroundedMemory):
    def __init__(self):
        super().__init__()
        self.start_heading = None
        self.cue = None
        self.scanning = True
        self.branch = None
        self.explore_streak = 0
        self.forward_remaining = 0

    def _observe(self, event):
        super()._observe(event)
        obs = event.observation
        if obs.mission != MEMORY_MISSION:
            return

        if self.start_heading is None:
            self.start_heading = obs.direction
        visible_objects = [
            fact for fact in self._audit["visible_facts"] if fact["object"] in {"key", "ball"}
        ]
        if self.scanning:
            if self.cue is None and len(visible_objects) == 1:
                self.cue = visible_objects[0]
            if obs.direction == self.start_heading and event.step > 0:
                self.scanning = False
        if not self.scanning and self.cue and self.branch is None:
            choices = [
                fact for fact in visible_objects
                if (fact["segment"], fact["position"]) != (self.cue["segment"], self.cue["position"])
            ]
            if len(choices) == 2 and {fact["object"] for fact in choices} == {"key", "ball"}:
                self.branch = next(fact for fact in choices if fact["object"] == self.cue["object"])
        self._audit.update(hallway_cue=self.cue, hallway_branch=self.branch, hallway_scanning=self.scanning)

    def _memory_lines(self, obs):
        if obs.mission == MEMORY_MISSION:
            if self.cue:
                yield (
                    f"Start-room cue {self.cue['id']}: {self.cue['object']}. "
                    "At the fork, choose the branch with the same object type.",
                    self.cue,
                )
            if self.branch:
                offset = self.odometry.relative_to_view(tuple(self.branch["position"]))
                yield f"Matching branch {self.branch['id']}: {self.branch['object']} at {offset}.", self.branch
        yield from super()._memory_lines(obs)
