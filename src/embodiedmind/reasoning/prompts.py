"""Shared planner instructions for all four memory conditions."""

SYSTEM = """You control a MiniGrid agent. Complete the mission using the current symbolic view and any memory provided. The view is egocentric. Choose one primitive action: 0 turn left, 1 turn right, 2 move forward, 3 pick up the object in front, 4 drop in front, 5 toggle the door in front, 6 done. For a 'go to' mission, stand adjacent and face the target. For DoorKey, collect a matching key, toggle the locked door, then walk onto the goal. You can walk on free cells, goals, or open doors. Prefer a visible legal move toward the goal. Explore if needed. Only use supported facts. Return JSON with integer action and evidence, a short source citation only. Evidence can be 'visible', a single supplied memory ID like 'f3.7' or 'o3', or 'explore' if searching. Do not fabricate an ID."""


def prompt_for(observation, memory):
    return (
        f"Mission: {observation.mission}\n\n"
        f"{observation.render()}\n\n"
        f"Memory from previous observations:\n{memory or '(empty)'}\n\n"
        "Return one JSON action with a source citation."
    )
