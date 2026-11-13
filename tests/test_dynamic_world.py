from collections import deque

from minigrid.core.constants import OBJECT_TO_IDX
import numpy as np
import pytest

from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.dynamic_world import (
    INTERVENTIONS,
    NEIGHBORS,
    InterventionConfig,
    make_dynamic_environment,
)


@pytest.mark.parametrize("seed", [0, 1, 2, 3, 4, 8, 12, 19])
def test_matched_worlds_begin_identically_and_reachable(seed):
    envs = [make_dynamic_environment(arm) for arm in INTERVENTIONS]
    try:
        snapshots = [PrimitiveController(env).reset(seed) for env in envs]
        assert all(observation == snapshots[0] for observation in snapshots)
        first = envs[0]
        dx, dy = NEIGHBORS[first.agent_dir]
        assert all(tuple(env.agent_pos) == tuple(first.agent_pos) for env in envs)
        assert all(env._original_pos == first._original_pos for env in envs)
        assert all(env._destination == first._destination for env in envs)
        assert first._visible(*first._original_pos)
        assert first._target_reachable(first._original_pos)
        assert first._target_reachable(first._destination)
        assert first.grid.get(*first._destination) is None
        assert tuple(first.agent_pos) != first._destination
        assert (first.agent_pos[0] + dx, first.agent_pos[1] + dy) != first._original_pos
    finally:
        for env in envs:
            env.close()


def _shortest_action_plan(env, target):
    """Evaluator fixture to test the verifier, with no projection to policy."""
    start = (*env.agent_pos, env.agent_dir)
    seen = {start}
    queue = deque([(start, ())])
    while queue:
        (x, y, direction), plan = queue.popleft()
        dx, dy = NEIGHBORS[direction]
        front = x + dx, y + dy
        if front == target:
            return plan
        choices = [(0, (x, y, (direction - 1) % 4)), (1, (x, y, (direction + 1) % 4))]
        if env.grid.get(*front) is None:
            choices.append((2, (*front, direction)))
        for action, state in choices:
            if state not in seen:
                seen.add(state)
                queue.append((state, (*plan, action)))
    raise AssertionError("fixture target was unreachable")


@pytest.mark.parametrize("seed", [0, 1, 4, 19])
def test_hidden_relocation_preserves_public_view_and_follows_target(seed):
    moved_env = make_dynamic_environment("relocation")
    control_env = make_dynamic_environment("no_change")
    moved = PrimitiveController(moved_env)
    control = PrimitiveController(control_env)
    try:
        assert moved.reset(seed) == control.reset(seed)
        target = moved_env._target
        old, new = moved_env._original_pos, moved_env._destination
        for _ in range(moved_env.intervention_config.step):
            mstep = moved.step(0)
            cstep = control.step(0)
            assert mstep.agent == cstep.agent
            assert not mstep.terminated
        assert moved_env.intervention_log[-1]["applied"]
        assert moved_env.grid.get(*old) is None
        assert moved_env.grid.get(*new) is target
        assert moved_env.instrs.desc.obj_poss == [new]
        assert control_env.grid.get(*old) is control_env._target
        assert set(mstep.agent.__slots__) == {"observation", "moved"}

        for action in _shortest_action_plan(moved_env, old):
            outcome = moved.step(action)
            assert not outcome.terminated and outcome.reward == 0
        for action in _shortest_action_plan(moved_env, new):
            outcome = moved.step(action)
        assert outcome.terminated and outcome.reward > 0
    finally:
        moved_env.close()
        control_env.close()


def test_visible_old_target_yields_a_retained_noop():
    env = make_dynamic_environment("relocation")
    controller = PrimitiveController(env)
    try:
        controller.reset(0)
        for action in (0, 0, 0, 0, 2):
            controller.step(action)
        assert env.intervention_log[-1]["reason"] == "old_or_new_position_visible_at_trigger"
        assert not env.intervention_log[-1]["applied"]
        assert env.grid.get(*env._original_pos) is env._target
    finally:
        env.close()


def test_dropout_is_seeded_and_protects_carry_and_forward_cell():
    config = InterventionConfig(step=1, dropout_until=2, dropout_probability=1)
    a = make_dynamic_environment("dropout", config=config)
    b = make_dynamic_environment("dropout", config=config)
    control = make_dynamic_environment("no_change", config=config)
    try:
        for env in (a, b, control):
            env.reset(seed=4)
        a_step, b_step, c_step = (env.step(0)[0] for env in (a, b, control))
        assert np.array_equal(a_step["image"], b_step["image"])
        assert np.array_equal(a_step["image"][3, 5:], c_step["image"][3, 5:])
        assert np.all(a_step["image"][:, :5, 0] == OBJECT_TO_IDX["unseen"])
        assert a.intervention_log == b.intervention_log
        assert a.intervention_log[-1]["masked_cells"] > 0
    finally:
        for env in (a, b, control):
            env.close()
