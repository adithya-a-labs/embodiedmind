"""Shared planner instructions and hints derived solely from the current view."""

from collections import deque
import re

from embodiedmind.environments.observation_adapter import PASSABLE


MEMORY_MISSION = "go to the matching object at the end of the hallway"
GOTO_INSTRUCTIONS = "A GoTo succeeds when you face the matching object in an adjacent cell. Do not pick up that target."
MEMORY_INSTRUCTIONS = (
    "Inspect the object in the starting room. At the fork, walk onto the floor tile "
    "next to the object of the same type. Entering the other branch ends the episode. "
    "Do not pick up either object or use done."
)

SYSTEM = """You control a MiniGrid agent. Complete the mission using the current view and any memory. Choose one primitive: 0 turn left, 1 turn right, 2 move forward, 3 pick up the object directly ahead, 4 drop ahead, 5 toggle the door directly ahead, 6 done. A GoTo succeeds when you face the matching object in an adjacent cell. Do not pick up that target. For DoorKey, collect the key, toggle the locked door, then walk onto the green goal. Follow the visible route hint when it applies. To explore, move forward on known safe tiles when possible. If blocked, turn toward a free side or turn around. Avoid repeatedly rotating in open space. Memory offsets are relative to your current view when stated. Return JSON with integer action and one short evidence citation. Use 'visible', one exact supplied memory ID, or 'explore'. Do not invent IDs."""


def _route_hint(observation):
    cells = {(cell.forward, cell.right): cell for cell in observation.cells}
    mission = observation.mission.lower()
    carrying_key = observation.carrying is not None and observation.carrying.object == "key"
    door_task = "the door" in mission and "the key" in mission and "the goal" in mission
    target = {}
    if door_task:
        objectives = [("goal", 2)] if carrying_key else [("key", 3), ("goal", 2)]
        if carrying_key:
            objectives += [("door", 5)]
        for kind, final in objectives:
            matching = {
                pos: final for pos, node in cells.items()
                if node.object == kind and (kind != "door" or node.state != "open")
            }
            if matching:
                target = matching
                break
    elif mission.startswith("go to "):
        description = set(re.findall(r"[a-z]+", mission))
        target = {
            pos: None for pos, node in cells.items()
            if node.object in description and node.color in description and node.object in {"key", "ball", "box", "door"}
        }

    if target:
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        queue = deque([((0, 0), 0, ())])
        visited = {((0, 0), 0)}
        while queue:
            pos, turn, path = queue.popleft()
            df, dr = dirs[turn]
            ahead = pos[0] + df, pos[1] + dr
            if ahead in target:
                actions = path + (() if target[ahead] is None else (target[ahead],))
                if actions:
                    return f"Route to visible objective, next suggested action: {actions[0]}."
            neighbors = [(pos, (turn - 1) % 4, 0), (pos, (turn + 1) % 4, 1)]
            cell = cells.get(ahead)
            if ahead == (0, 0) or cell and (cell.object in PASSABLE - {"lava"} or
                                            cell.object == "door" and cell.state == "open"):
                neighbors.append((ahead, turn, 2))
            for loc, heading, action in neighbors:
                if (loc, heading) not in visited:
                    visited.add((loc, heading))
                    queue.append((loc, heading, path + (action,)))
    front = cells.get((1, 0))
    if front and (front.object in PASSABLE - {"lava"} or front.object == "door" and front.state == "open"):
        return "No visible route to objective. Explore by moving forward (2) if memory has no better clue."
    for action, offset in ((0, -1), (1, 1)):
        side = cells.get((0, offset))
        if side and side.object in PASSABLE - {"lava"}:
            return f"No visible route to objective. Explore by turning toward free space ({action})."
    return "No visible route to objective. Turn right (1) to inspect another direction."


def prompt_for(observation, memory):
    return (
        f"Mission: {observation.mission}\n\n"
        f"{observation.render()}\n{_route_hint(observation)}\n\n"
        f"Memory from previous observations:\n{memory or '(empty)'}\n\n"
        "Return one JSON action with a source citation."
    )
