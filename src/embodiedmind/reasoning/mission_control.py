"""B10 routes to useful viewpoints, then verifies observable interactions."""

from collections import deque

from embodiedmind.reasoning.progress import adjacent, navigation_facts, route, task_action
from embodiedmind.reasoning.prompts import DYNAMIC_OBSTACLES_MISSION


def _walkable(appearance):
    return appearance[0] in {"empty", "floor", "goal"} or appearance[::2] == ("door", "open")


def _explore(agent, obs):
    odom = agent.odometry
    origin, direction = odom.position, odom.direction
    cells = {fact.position: fact.appearance for fact in navigation_facts(agent)}
    cells[origin] = ("empty", "", "")
    start = origin, direction
    queue = deque([(start, ())])
    seen = {start}
    options = {}
    while queue:
        (point, heading), path = queue.popleft()
        ahead = adjacent(point)[heading]
        view = cells.get(ahead)
        signature = odom.segment, point, heading
        visits = agent.visits[signature]
        candidates = [
            ((point, (heading - 1) % 4), 0),
            ((point, (heading + 1) % 4), 1),
        ]
        if view and _walkable(view):
            candidates.append(((ahead, heading), 2))
        # Try closed, unlocked exits and uninspected viewpoints even when all
        # immediately adjacent floor cells already appear in the map.
        if view and view[::2] == ("door", "closed") and (
            ("toggle", ahead) not in agent.failed_interactions
        ):
            options[(signature, "door")] = (len(path) - 9, (*path, 5))
        if view and view[::2] == ("door", "open") and not any(
            agent.visits[odom.segment, ahead, facing] for facing in range(4)
        ):
            options[(signature, "cross")] = (len(path) - 9, (*path, 2))
        if view is None:
            options[(signature, "forward")] = (len(path) + 2 * visits - 3, (*path, 2))
        if path and not visits:
            options[(signature, "view")] = (len(path) - (2 if point != origin else 0), path)
        for state, action in candidates:
            if state not in seen:
                seen.add(state)
                queue.append((state, (*path, action)))
    if agent.frontier:
        if agent.frontier in options:
            path = options[agent.frontier][1]
            if path[0] == 5:
                return _interact(agent, obs, "toggle", adjacent(origin)[direction])
            return path[0], "continue_frontier_route", path
        agent.exhausted.add(agent.frontier)
    available = [key for key in options if key not in agent.exhausted]
    if available:
        agent.frontier = min(available, key=lambda key: (*options[key], key))
        path = options[agent.frontier][1]
        if path[0] == 5:
            return _interact(agent, obs, "toggle", adjacent(origin)[direction])
        return path[0], "choose_frontier_route", path
    agent.frontier = None
    front = obs.cell(1, 0)
    if front is not None and _walkable((front.object, front.color, front.state)):
        return 2, "advance_after_exhausted_scan", ()
    return None


def _interact(agent, obs, operation, point, expected=None):
    front = obs.cell(1, 0)
    carried = obs.carrying
    if not front or agent.failed_interactions.get((operation, point)) == (carried, front):
        return None
    if expected and (front.object, front.color) != (expected["object"], expected["color"]):
        return None
    if operation == "toggle" and front.object == "door" and (
        front.state == "closed" or front.state == "locked" and carried
        and (carried.object, carried.color) == ("key", front.color)
    ):
        action = 5
    elif operation == "pickup" and not carried and front.object in {"key", "ball", "box"}:
        action = 3
    elif operation == "drop" and carried and front.object == "empty":
        action = 4
    else:
        return None
    agent.last_interaction = operation, point, (carried, front)
    return action, f"verified_{operation}_precondition", ()


def _drop(agent, obs, point, *, near):
    odom = agent.odometry
    neighborhood = set(adjacent(point))
    candidates = [
        f.position for f in navigation_facts(agent)
        if f.appearance[0] == "empty" and (f.position in neighborhood) == near
    ]
    if not candidates:
        return None
    path = route(agent, candidates, doors=True)
    if path:
        return path[0], "route_to_drop_position", path
    if path == ():
        return _interact(agent, obs, "drop", adjacent(odom.position)[odom.direction])
    return None


def mission_action(agent, obs, *, explore=True):
    if obs.mission == DYNAMIC_OBSTACLES_MISSION:
        # The caller retains B8's reactive fallback when a moving obstacle
        # makes forward odometry uncertain.
        return None
    operation = agent.operation
    if operation is None and agent.phase:
        return task_action(agent, obs)
    if agent.target:
        target = tuple(agent.target["position"])
        if operation in {"drop_blocker", "drop_key"}:
            choice = _drop(agent, obs, target, near=False)
            if choice:
                return choice
        else:
            path = route(agent, [target], stand=operation == "stand", doors=True)
            if path:
                if path[0] == 5:
                    choice = _interact(agent, obs, "toggle",
                                       adjacent(agent.odometry.position)[agent.odometry.direction])
                    if choice:
                        return choice
                else:
                    return path[0], "route_to_mission_target", path
            if path == () and operation in {"toggle", "pickup"}:
                choice = _interact(agent, obs, operation, target, agent.target)
                if choice:
                    return choice
    if operation == "place" and agent.reference:
        choice = _drop(agent, obs, tuple(agent.reference["position"]), near=True)
        if choice:
            return choice
    return _explore(agent, obs) if explore else None
