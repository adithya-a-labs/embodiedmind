from dataclasses import asdict

from minigrid.core.constants import COLOR_TO_IDX, OBJECT_TO_IDX, STATE_TO_IDX
from minigrid.core.world_object import Ball
import numpy as np
import pytest

from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.factory import make_environment
from embodiedmind.environments.observation_adapter import adapt_observation
from embodiedmind.reasoning.action_validator import FALLBACK_ACTION, parse_action


def fixture_observation():
    public = np.zeros((7, 7, 3), dtype=np.uint8)
    public[1, 4] = (OBJECT_TO_IDX["empty"], 0, 0)
    public[5, 2] = (OBJECT_TO_IDX["door"], COLOR_TO_IDX["blue"], STATE_TO_IDX["locked"])
    public[3, 6] = (OBJECT_TO_IDX["key"], COLOR_TO_IDX["red"], 0)
    return {"image": public, "direction": 3, "mission": "find the blue door"}


def test_symbolic_observation_exact_coordinates_and_no_extra_fields():
    raw = fixture_observation()
    adapted = adapt_observation(raw)
    injected = adapt_observation({
        **raw, "full_state": "SECRET_CELL", "agent_pos": (99, 99),
        "reward": 123, "hidden_target": "SECRET_TARGET",
    })
    assert adapted == injected
    assert adapted.cell(2, -2).object == "empty"
    assert adapted.cell(4, 2).description == "blue door locked"
    assert adapted.cell(2, 2) is None
    assert adapted.cell(0, 0) is None
    assert adapted.carrying.description == "red key"
    assert adapted.direction == 3
    assert "Facing north" in adapted.render()
    assert "SECRET" not in repr(asdict(injected)) + injected.render()
    assert all(len(line.split(": ", 1)[1]) == 7 for line in adapted.render().splitlines()[3:10])


def test_hidden_world_changes_do_not_cross_policy_boundary():
    env = make_environment("MiniGrid-DoorKey-8x8-v0")
    controller = PrimitiveController(env)
    try:
        clean = controller.reset(42)
        _, visibility = env.unwrapped.gen_obs_grid()
        def is_hidden(x, y):
            relative = env.unwrapped.relative_coords(x, y)
            return relative is None or not visibility[relative]

        hidden = [
            (x, y)
            for x in range(1, env.unwrapped.width - 1)
            for y in range(1, env.unwrapped.height - 1)
            if (x, y) != tuple(env.unwrapped.agent_pos)
            and env.unwrapped.grid.get(x, y) is None
            and is_hidden(x, y)
        ]
        assert hidden
        env.unwrapped.grid.set(*hidden[0], Ball("purple"))
        modified = adapt_observation(env.unwrapped.gen_obs())
        assert clean == modified
        assert "purple ball" not in modified.render()
        result = controller.step(0)
        assert set(asdict(result.agent)) == {"observation", "moved"}
    finally:
        env.close()


@pytest.mark.parametrize("response", [
    '{"action": true, "evidence": ""}',
    '{"action": 7, "evidence": ""}',
    '{"action": "forward", "evidence": ""}',
    '{"action": 2, "action": 1, "evidence": ""}',
    '{"action": 2, "evidence": "", "secret": 1}',
    '{"action": 2}',
    'not JSON',
])
def test_invalid_actions_share_deterministic_fallback(response):
    result = parse_action(response)
    assert not result.valid and result.action == FALLBACK_ACTION and result.error


def test_valid_action_keeps_short_evidence():
    result = parse_action('{"action": 2, "evidence": "open door ahead"}')
    assert result.valid and result.action == 2 and result.evidence == "open door ahead"
