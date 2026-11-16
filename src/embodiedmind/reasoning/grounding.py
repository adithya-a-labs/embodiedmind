"""Resolve model choices using only observations and the agent's own map."""

import json
from collections import deque
from dataclasses import dataclass

from embodiedmind.memory.spatial import DIRECTION_VECTORS
from embodiedmind.agents.evidence_memory import B11_ARMS
from embodiedmind.reasoning.action_validator import ActionDecision, _unique_object, parse_action
from embodiedmind.reasoning.mission_control import mission_action
from embodiedmind.reasoning.progress import navigation_facts, route as progress_route, task_action
from embodiedmind.reasoning.prompts import (
    DYNAMIC_OBSTACLES_MISSION,
    GOTO_INSTRUCTIONS,
    MEMORY_INSTRUCTIONS,
    MEMORY_MISSION,
    SYSTEM,
    _route_hint,
    prompt_for,
)

GUARDED = {"B0G", "B3G", "B4", "B5", "B6", "B7", "B8", "B9N", "B9", "B10"}
AGENTIC = {"B5", "B6", "B7", "B8", "B9N", "B9", "B10"}
GUARDED.update(B11_ARMS)
AGENTIC.update(B11_ARMS)
CONTROLLER_DECISION = '{"goal":"explore","action":0,"evidence":"explore"}'
GOALS = ("primitive", "approach", "verify", "explore")
GOAL_SCHEMA = {
    "type": "object",
    "properties": {
        "goal": {"type": "string", "enum": GOALS},
        "action": {"type": "integer", "minimum": 0, "maximum": 6},
        "evidence": {"type": "string", "maxLength": 120},
    },
    "required": ["goal", "action", "evidence"],
    "additionalProperties": False,
}


@dataclass(frozen=True)
class Resolution:
    proposed: ActionDecision
    action: int
    goal: str = "primitive"
    reason: str | None = None
    route: tuple[int, ...] = ()


def action_request(model, observation, context, seed, variant, facts=()):
    system = SYSTEM
    dynamic_obstacles = observation.mission == DYNAMIC_OBSTACLES_MISSION
    if observation.mission == MEMORY_MISSION:
        system = system.replace(GOTO_INSTRUCTIONS, MEMORY_INSTRUCTIONS)
    elif dynamic_obstacles:
        system = system.replace(
            "3 pick up the object directly ahead, 4 drop ahead, 5 toggle the door directly ahead, 6 done. "
            + GOTO_INSTRUCTIONS
            + " For DoorKey, collect the key, toggle the locked door, then walk onto the green goal.",
            "and no interaction actions. Reach the green goal square without colliding with moving obstacles.",
        )
    if variant in AGENTIC:
        system = (
            system.split("Return JSON", 1)[0] + " Return JSON with goal, action, and evidence. "
            "Choose primitive to execute action directly; "
            "approach to route to the supplied fact ID in evidence; verify to look at a last-seen "
            "fact again; or explore to navigate toward unknown space. Use action 0 as a placeholder "
            "for non-primitive goals. Cite visible or explore if you do not cite a fact. "
            "An unknown cell can be observed before entering it."
        )
    if variant in B11_ARMS:
        system = system.replace(
            "verify to look at a last-seen fact again; or explore",
            "or explore",
        )
    prompt = prompt_for(observation, context)
    if variant in AGENTIC:
        prompt = prompt.replace("Return one JSON action with a source citation.",
                                "Return one JSON goal, action, and evidence.")
    request = model.request(system, prompt, seed)
    if variant in AGENTIC:
        allowed = ["visible", "explore", *(fact["id"] for fact in facts)]
        request["format"] = {**GOAL_SCHEMA, "properties": {
            **GOAL_SCHEMA["properties"], "evidence": {"type": "string", "enum": allowed},
        }}
        if variant in B11_ARMS:
            request["format"]["properties"]["goal"] = {
                "type": "string", "enum": ["primitive", "approach", "explore"],
            }
    if dynamic_obstacles:
        schema = request["format"]
        properties = schema["properties"]
        request["format"] = {**schema, "properties": {
            **properties, "action": {**properties["action"], "maximum": 2},
        }}
    return request


def passable(cell):
    return cell is not None and (cell.object in {"empty", "floor", "goal"}
                                 or cell.object == "door" and cell.state == "open")


def local_alternative(observation):
    return 0 if passable(observation.cell(0, -1)) else 1


def _visible_objective_action(observation):
    hint = _route_hint(observation)
    return int(hint[-2]) if hint.startswith("Route to visible objective") else None


def _route(agent, target=None):
    odometry = agent.odometry
    facts = navigation_facts(agent)
    cells = {fact.position: fact for fact in facts}
    position, heading = odometry.position, odometry.direction
    queue = deque([(position, heading, ())])
    seen = {(position, heading)}
    while queue:
        point, heading, path = queue.popleft()
        dx, dy = DIRECTION_VECTORS[heading]
        ahead = point[0] + dx, point[1] + dy
        if target is not None and ahead == target:
            return path
        if target is None and path and ahead not in cells and ahead != position:
            return path
        neighbors = [(point, (heading - 1) % 4, 0), (point, (heading + 1) % 4, 1)]
        cell = cells.get(ahead)
        if ahead == position or cell and (cell.appearance[0] in {"empty", "floor", "goal"}
                                         or cell.appearance[0] == "door" and cell.appearance[2] == "open"):
            neighbors.append((ahead, heading, 2))
        for next_cell, next_heading, action in neighbors:
            if (next_cell, next_heading) not in seen:
                seen.add((next_cell, next_heading))
                queue.append((next_cell, next_heading, (*path, action)))
    return None


def _goal_response(raw):
    try:
        value = json.loads(raw, object_pairs_hook=_unique_object)
        goal = value.pop("goal")
        if goal not in GOALS:
            raise ValueError
        return goal, parse_action(json.dumps(value))
    except (ValueError, TypeError, AttributeError, KeyError):
        return "primitive", ActionDecision(1, "", False, "invalid_goal")


def _cue_memory_action(agent, observation, goal, valid, exploration_route):
    if goal == "explore" and valid:
        agent.explore_streak += 1
    else:
        agent.explore_streak = 0

    if observation.mission == MEMORY_MISSION:
        if agent.scanning:
            return 0, "scan_start_cue", ()
        if agent.branch and agent.branch["segment"] == agent.odometry.segment:
            route = _route(agent, tuple(agent.branch["position"]))
            if route:
                return route[0], "approach_matching_branch", route

    front = observation.cell(1, 0)
    if agent.explore_streak >= 3 or (valid and goal == "explore" and not exploration_route):
        if agent.forward_remaining == 0 and passable(front):
            agent.forward_remaining = 3
            agent.explore_streak = 0
    if agent.forward_remaining:
        if passable(front):
            agent.forward_remaining -= 1
            return 2, "forward_burst", ()
        agent.forward_remaining = 0
    return None


def resolve_response(raw, observation, agent, variant):
    goal, proposed = _goal_response(raw) if variant in AGENTIC else ("primitive", parse_action(raw))
    action, reason, route = proposed.action, None, ()
    if goal != "primitive" and proposed.valid:
        refs = {fact["id"]: tuple(fact["position"]) for fact in agent.audit()["selected_facts"]
                if "position" in fact}
        if goal == "explore":
            route = _route(agent)
            # At the frontier, turn to gather another view. Unknown is not an obstacle.
            action = 2 if observation.cell(1, 0) is None else (
                route[0] if route else local_alternative(observation)
            )
        elif proposed.evidence in refs:
            target = refs[proposed.evidence]
            route = _route(agent, target)
            if route:
                action = route[0]
            elif route == () and goal == "approach":
                cell = observation.cell(1, 0)
                action = _interact(agent, observation, cell)
            else:
                frontier = _route(agent)
                action = frontier[0] if frontier else local_alternative(observation)
                reason = "verify_target_visible" if route == () else "no_known_route"
        else:
            visible_action = _visible_objective_action(observation)
            action = local_alternative(observation) if visible_action is None else visible_action
            reason = "unknown_fact_reference"

    if variant in B11_ARMS:
        if observation.mission == DYNAMIC_OBSTACLES_MISSION:
            override = _cue_memory_action(agent, observation, goal, proposed.valid, route)
        else:
            override = agent.verify_action() or mission_action(agent, observation, explore=False)
            if override is None and (not proposed.valid or goal == "explore"):
                override = mission_action(agent, observation)
        if override is not None:
            action, reason, route = override
    elif variant == "B10":
        override = mission_action(agent, observation)
        if observation.mission == DYNAMIC_OBSTACLES_MISSION:
            override = _cue_memory_action(agent, observation, goal, proposed.valid, route)
        if override is not None:
            action, reason, route = override
    elif variant == "B8":
        override = _cue_memory_action(agent, observation, goal, proposed.valid, route)
        if override is not None:
            action, reason, route = override
    elif variant in {"B9N", "B9"}:
        if variant == "B9" and agent.phase:
            override = task_action(agent, observation)
        else:
            override = _cue_memory_action(agent, observation, goal, proposed.valid, route)
        if override is not None:
            action, reason, route = override
        if (override is None or reason == "forward_burst") and (
            goal == "explore" or agent.visits[
                agent.odometry.segment, agent.odometry.position, agent.odometry.direction
            ] >= 3 and action in (0, 1, 2, 6)
        ):
            path = progress_route(agent)
            if path:
                action, reason, route = path[0], "progress_aware_explore", path

    cell = observation.cell(1, 0)
    if observation.mission == DYNAMIC_OBSTACLES_MISSION and action > 2:
        action, reason = local_alternative(observation), "action_unavailable"
    if variant in GUARDED and action == 2 and cell is not None and not passable(cell):
        action, reason = local_alternative(observation), f"blocked_by_visible_{cell.object}"
    return Resolution(proposed, action, goal, reason, route or ())


def _interact(agent, observation, cell):
    subgoal = agent.audit()["subgoal"]
    if cell and cell.object == "key" and subgoal == "Find key" and not observation.carrying:
        return 3
    if cell and cell.object == "door" and subgoal == "Find and cross door":
        return 2 if cell.state == "open" else 5
    if cell and cell.object == "goal":
        return 2
    return 6 if cell and cell.object in {"key", "ball", "box"} else local_alternative(observation)
