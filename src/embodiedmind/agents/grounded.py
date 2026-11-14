"""Subgoal and location memory built exclusively from public observations."""

from embodiedmind.agents.structured import Structured
from embodiedmind.memory.belief import BeliefLedger
from embodiedmind.memory.retrieval import mission_terms


class GroundedMemory(Structured):
    def __init__(self, *, workflows=()):
        super().__init__(BeliefLedger(age_after=None))
        self.crossed_door = False
        self.workflows = workflows
        self.targets = set()

    def _observe(self, event):
        super()._observe(event)
        obs = event.observation
        terms = mission_terms(obs.mission)
        door_task = {"key", "door", "goal"} <= terms
        carried = obs.carrying is not None and obs.carrying.object == "key"
        segment, position = self.odometry.segment, self.odometry.position
        previous = self.log.events[-2] if len(self.log.events) > 1 else None
        previous_front = previous.observation.cell(1, 0) if previous else None
        if door_task and event.moved is True and previous_front and previous_front.object == "door":
            self.crossed_door = True
        if door_task:
            label, kind = (("Reach goal", "goal") if self.crossed_door else
                           ("Find and cross door", "door") if carried else ("Find key", "key"))
        else:
            label, kind = "Find mission target", next(iter(sorted(terms & {"ball", "key", "box", "door"})), "")
        relevant = [fact for fact in self.index.recall(segment) if fact.appearance[0] == kind
                    and (door_task or not terms & {"blue", "green", "grey", "purple", "red", "yellow"}
                         or fact.appearance[1] in terms)]
        visible = {self.odometry.locate(cell.forward, cell.right) for cell in obs.cells}
        candidates = []
        for fact in relevant:
            self.targets.add((kind, segment, fact.position))
            candidates.append({"id": fact.id, "position": list(fact.position),
                               "status": "visible" if fact.position in visible else "last_seen"})
        known = {fact.position for fact in relevant}
        ruled_out = [list(cell) for target_kind, seg, cell in sorted(self.targets)
                     if target_kind == kind and seg == segment and cell not in known
                     and (segment, cell) in self.index.active]
        self._audit.update(subgoal=label, candidates=candidates, ruled_out=ruled_out)
        self.relevant = sorted(relevant, key=lambda f: (
            f.position not in visible, -f.last_verified_step,
            sum(abs(a - b) for a, b in zip(position, f.position)), f.id,
        ))

    def _memory_lines(self, obs):
        yield f"Subgoal: {self._audit['subgoal']}. Offsets are (forward,right).", None
        for workflow in self.workflows:
            if workflow["task"] == "doorkey" and {"key", "door", "goal"} <= mission_terms(obs.mission):
                cue = workflow["steps"].get(self._audit["subgoal"])
                if cue:
                    yield f"DoorKey routine: {cue}", None
                    self._audit["workflow"] = workflow["source"]
        if self._audit["ruled_out"]:
            recent = self._audit["ruled_out"][-1]
            yield f"Previously sighted target now absent at {self.odometry.relative_to_view(recent)}.", None
        for fact in self.relevant[:3]:
            relative = self.odometry.relative_to_view(fact.position)
            kind, color, state = fact.appearance
            appearance = " ".join(filter(None, (color, kind, state)))
            status = next(row["status"] for row in self._audit["candidates"] if row["id"] == fact.id)
            yield (f"{fact.id} {appearance} {relative} {status}; verified at {fact.last_verified_step}",
                   {**fact.audit(), "relative": list(relative)})
