"""Route from observed cells, avoiding repeatedly visited exploration poses."""

from heapq import heappop, heappush

from embodiedmind.memory.spatial import DIRECTION_VECTORS
from embodiedmind.reasoning.prompts import MEMORY_MISSION


def adjacent(point):
    return [(point[0] + dx, point[1] + dy) for dx, dy in DIRECTION_VECTORS]


def navigation_facts(agent):
    if hasattr(agent, "navigation_facts"):
        return agent.navigation_facts()
    return agent.index.recall(agent.odometry.segment)


def route(agent, targets=(), *, stand=False, doors=False, centerline=False):
    odom = agent.odometry
    origin, heading = odom.position, odom.direction
    cells = {f.position: f.appearance for f in navigation_facts(agent)}
    queue = [(0, (), origin, heading)]
    seen = set()
    while queue:
        cost, path, point, facing = heappop(queue)
        if (point, facing) in seen:
            continue
        seen.add((point, facing))
        ahead = adjacent(point)[facing]
        destination = point if stand else ahead
        if targets and destination in targets:
            return path
        if not targets and ahead not in cells and ahead != origin and (
            not centerline or ahead[1] == 0
        ):
            return (*path, 2)
        neighbors = [(point, (facing - 1) % 4, (0,)), (point, (facing + 1) % 4, (1,))]
        cell = cells.get(ahead)
        if not centerline or ahead[1] == 0:
            if ahead == origin or cell and (cell[0] in {"empty", "floor", "goal"}
                                           or cell[0] == "door" and cell[2] == "open"):
                neighbors.append((ahead, facing, (2,)))
            elif doors and cell and cell[0] == "door" and cell[2] == "closed":
                neighbors.append((ahead, facing, (5, 2)))
        for pos, direction, actions in neighbors:
            if (pos, direction) not in seen:
                visits = 0 if targets else agent.visits[odom.segment, pos, direction]
                heappush(queue, (cost + len(actions) + visits, (*path, *actions), pos, direction))
    if not targets and len(seen) > 1:
        # No reachable frontier. Inspect a less-used orientation at this pose.
        return min(((0,), (1,)), key=lambda actions: agent.visits[
            odom.segment, origin, (heading + (1 if actions == (1,) else -1)) % 4
        ])
    return None


def task_action(agent, obs):
    """Resolve a verified task phase using current observations and mapped evidence."""
    if obs.mission == MEMORY_MISSION:
        if agent.branch:
            path = route(agent, [tuple(agent.branch["position"])])
            if path:
                return path[0], "approach_matching_branch", path
        if agent.cue is None:
            # Stay on the centerline while seeking the real start-room landmark.
            # Face west so the cue can enter the public view from a fork-side spawn.
            heading = agent.odometry.direction
            if heading != 2:
                return (1 if heading == 1 else 0), "inspect_toward_start_room", ()
            front = obs.cell(1, 0)
            if front is None or front.object == "empty":
                return 2, "return_toward_start_room", ()
        path = route(agent, centerline=True)
        if path:
            return path[0], "search_hallway", path
        return None

    if agent.target:
        if (agent.phase == "Pick up target ball" and obs.carrying
                and obs.carrying.object == "key"):
            cells = {f.position: f.appearance[0] for f in navigation_facts(agent)}
            target = tuple(agent.target["position"])
            holding_cells = [p for p, kind in cells.items() if kind == "empty"
                             and p not in adjacent(target)]
            path = route(agent, holding_cells, doors=True) if holding_cells else None
            if path:
                return path[0], "find_key_drop_tile", path
            if path == () and (front := obs.cell(1, 0)) and front.object == "empty":
                return 4, "release_key_after_unlock", ()
        path = route(agent, [tuple(agent.target["position"])], doors=True)
        if path:
            return path[0], "route_to_subgoal", path
        if path == ():
            front = obs.cell(1, 0)
            if front and (front.object, front.color) == (agent.target["object"], agent.target["color"]):
                action = 5 if agent.phase == "Unlock matching door" else 3
                return action, "attempt_subgoal_interaction", ()

    if agent.phase == "Place beside reference" and agent.reference:
        ref = tuple(agent.reference["position"])
        cells = {f.position: f.appearance[0] for f in navigation_facts(agent)}
        free = [p for p in adjacent(ref) if cells.get(p) in {"empty", "floor"}
                or p == agent.odometry.position]
        if free:
            path = route(agent, free, doors=True)
            if path:
                return path[0], "route_to_placement", path
            if path == () and (front := obs.cell(1, 0)) and front.object in {"empty", "floor"}:
                return 4, "attempt_verified_placement", ()

    path = route(agent, doors=True)
    return (path[0], "explore_for_subgoal", path) if path else None
