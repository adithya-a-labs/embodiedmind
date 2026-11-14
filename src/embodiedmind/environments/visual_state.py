"""Evaluator-only board snapshots for the experiment viewer."""

from embodiedmind.environments.dynamic_world import (
    DYNAMIC_ENV_ID,
    InterventionConfig,
    make_dynamic_environment,
)
from embodiedmind.environments.factory import make_environment


def viewer_environment(job, limits, *, render_mode=None):
    if job["environment"] == DYNAMIC_ENV_ID:
        return make_dynamic_environment(
            job["intervention"], config=InterventionConfig(**limits.get("dynamics", {})), render_mode=render_mode,
        )
    return make_environment(job["environment"], render_mode=render_mode)


def board_snapshot(env):
    world = env.unwrapped
    objects = []
    for index, tile in enumerate(world.grid.grid):
        if tile is not None:
            objects.append({
                "x": index % world.width, "y": index // world.width,
                "object": tile.type, "color": tile.color,
                "state": ("open" if tile.is_open else "locked" if tile.is_locked else "closed")
                if tile.type == "door" else "",
            })
    return {
        "width": world.width, "height": world.height, "objects": objects,
        "agent": {"x": int(world.agent_pos[0]), "y": int(world.agent_pos[1]),
                  "direction": int(world.agent_dir)},
    }
