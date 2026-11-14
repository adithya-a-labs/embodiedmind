import pytest

from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.factory import (
    DYNAMIC_OBSTACLES,
    OFFICIAL_ENVIRONMENTS,
    make_environment,
    smoke_environment,
)


@pytest.mark.parametrize("env_id", OFFICIAL_ENVIRONMENTS)
def test_seeded_official_environments_complete_smoke(env_id):
    first, _ = smoke_environment(env_id, 42, 60)
    second, _ = smoke_environment(env_id, 42, 60)
    assert first == second
    assert first["observation_shape"] == [7, 7, 3]
    assert first["mission"]
    assert first["terminated"] or first["truncated"] or first["runner_cap_reached"]


def test_unrecognized_environment_is_not_substituted():
    with pytest.raises(ValueError, match="Registered tasks"):
        make_environment("Unregistered-v0")


@pytest.mark.parametrize("env_id", OFFICIAL_ENVIRONMENTS)
def test_public_forward_rule_matches_evaluator_motion(env_id):
    env = make_environment(env_id)
    controller = PrimitiveController(env)
    try:
        observation = controller.reset(seed=42)
        blocked = 0
        moved = 0
        for action in (2, 2, 0, 2, 3, 5, 2, 1) * 12:
            if not env.action_space.contains(action):
                continue
            previous = tuple(env.unwrapped.agent_pos)
            result = controller.step(action)
            actual_motion = previous != tuple(env.unwrapped.agent_pos)
            if result.moved is not None:
                assert result.moved == actual_motion
                if result.moved:
                    moved += 1
                else:
                    blocked += 1
            if env_id == DYNAMIC_OBSTACLES:
                assert result.moved is None
            if action == 0:
                assert result.observation.direction == (observation.direction - 1) % 4
            if action == 1:
                assert result.observation.direction == (observation.direction + 1) % 4
            observation = result.observation
            if result.terminated or result.truncated:
                break
        assert env_id == DYNAMIC_OBSTACLES or moved + blocked > 0
    finally:
        env.close()
