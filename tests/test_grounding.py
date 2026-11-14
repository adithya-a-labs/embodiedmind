import pytest

from embodiedmind.agents import make_agent
from embodiedmind.control.controller import PrimitiveController
from embodiedmind.environments.factory import make_environment
from embodiedmind.environments.observation_adapter import Cell, Observation
from embodiedmind.reasoning.grounding import action_request, resolve_response
from embodiedmind.reasoning.prompts import DYNAMIC_OBSTACLES_MISSION


def view(cells, direction=0, mission="go to the purple ball", carrying=None):
    return Observation(mission, direction, tuple(cells), carrying)


def test_feasibility_guard_does_not_treat_unknown_as_a_wall():
    raw = '{"action":2,"evidence":"visible"}'
    blocked = view([Cell(1, 0, "wall", "grey", "")])
    agent = make_agent("B0G")
    assert resolve_response(raw, blocked, agent, "B0").action == 2
    guarded = resolve_response(raw, blocked, agent, "B0G")
    assert guarded.proposed.action == 2 and guarded.action != 2
    assert resolve_response(raw, view([]), agent, "B0G").action == 2


def test_agent_routes_to_verify_remembered_target_and_retains_negative_evidence():
    agent = make_agent("B5")
    first = view([Cell(1, 0, "ball", "purple", "")])
    agent.observe(first, 0)
    facing_north = view([], 3)
    agent.observe(facing_north, 1, 0)
    agent.context(facing_north, 768)
    decision = resolve_response('{"goal":"verify","action":0,"evidence":"f0.0"}', facing_north, agent, "B5")
    assert decision.goal == "verify" and decision.action == 1 and decision.route == (1,)
    assert agent.audit()["candidates"][0]["status"] == "last_seen"

    empty = view([Cell(1, 0, "empty", "", ""), Cell(1, 1, "ball", "purple", "")])
    agent.observe(empty, 2, 1)
    assert agent.audit()["ruled_out"] == [[1, 0]]
    assert agent.audit()["candidates"][0]["position"] == [1, 1]
    assert agent.audit()["revisions"][0]["reason"] == "direct_observation"


def test_doorkey_recall_switches_from_key_to_door():
    mission = "use the key to open the door and then get to the goal"
    key, door = Cell(1, 0, "key", "yellow", ""), Cell(1, 1, "door", "yellow", "locked")
    agent = make_agent("B4")
    agent.observe(view([key, door], mission=mission), 0)
    holding = view([door], mission=mission, carrying=key)
    agent.observe(holding, 1, 3)
    context = agent.context(holding, 768)
    assert "Find and cross door" in context and "yellow door" in context
    assert "yellow key" not in context


def test_goal_requests_constrain_the_schema_to_retrieved_evidence():
    class Model:
        def request(self, system, prompt, seed):
            return {"system": system, "prompt": prompt, "seed": seed}

    request = action_request(Model(), view([]), "f0.0", 7, "B5", [{"id": "f0.0"}])
    assert request["format"]["properties"]["evidence"]["enum"] == ["visible", "explore", "f0.0"]


@pytest.mark.parametrize("variant", ["B0", "B8"])
def test_dynamic_obstacles_limits_model_and_executed_actions(variant):
    class Model:
        def request(self, system, prompt, seed):
            return {"system": system, "format": {"properties": {"action": {"maximum": 6}}}}

    observation = view([], mission=DYNAMIC_OBSTACLES_MISSION)
    request = action_request(Model(), observation, "", 7, variant)
    assert "6 done" not in request["system"]
    assert request["format"]["properties"]["action"]["maximum"] == 2
    raw = '{"goal":"primitive","action":6,"evidence":"visible"}' if variant == "B8" else (
        '{"action":6,"evidence":"visible"}'
    )
    result = resolve_response(raw, observation, make_agent(variant), variant)
    assert result.action in (0, 1)
    assert result.reason == "action_unavailable"


@pytest.mark.parametrize("game, seed, required_reasons", [
    ("BabyAI-KeyCorridorS3R3-v0", 3003, {"release_key_after_unlock", "attempt_subgoal_interaction"}),
    ("BabyAI-PutNextS5N2-v0", 3001, {"attempt_subgoal_interaction", "attempt_verified_placement"}),
    ("MiniGrid-MemoryS17Random-v0", 3001, {"approach_matching_branch"}),
])
def test_b9_completes_public_observation_subgoals(game, seed, required_reasons):
    raw = '{"goal":"explore","action":0,"evidence":"explore"}'
    env = make_environment(game)
    control = PrimitiveController(env)
    agent = make_agent("B9")
    reasons = set()
    previous_action = moved = None
    try:
        obs = control.reset(seed)
        for step in range(48):
            agent.observe(obs, step, previous_action, moved)
            agent.context(obs, 768)
            decision = resolve_response(raw, obs, agent, "B9")
            reasons.add(decision.reason)
            result = control.step(decision.action)
            if result.terminated or result.truncated:
                assert result.terminated and result.reward > 0
                break
            obs, previous_action, moved = result.observation, decision.action, result.moved
        else:
            pytest.fail("B9 did not finish within 48 actions")
        if game == "MiniGrid-MemoryS17Random-v0":
            assert agent.cue["position"][1] == -1
            assert abs(agent.branch["position"][1]) == 2
    finally:
        env.close()
    assert required_reasons <= reasons


@pytest.mark.parametrize("seed", [11, 14, 21, 36])
def test_b8_reaches_the_matching_branch_even_with_repeated_explore(seed):
    raw = '{"goal":"explore","action":0,"evidence":"explore"}'
    env = make_environment("MiniGrid-MemoryS13-v0")
    controller = PrimitiveController(env)
    agent = make_agent("B8")
    reasons = set()
    previous_action = moved = None
    try:
        observation = controller.reset(seed)
        for step in range(48):
            agent.observe(observation, step, previous_action, moved)
            context = agent.context(observation, 768)
            decision = resolve_response(raw, observation, agent, "B8")
            reasons.add(decision.reason)
            result = controller.step(decision.action)
            if result.terminated or result.truncated:
                assert result.terminated and result.reward > 0
                assert "Start-room cue" in context and "Matching branch" in context
                assert agent.audit()["hallway_cue"]["object"] == agent.audit()["hallway_branch"]["object"]
                break
            observation, previous_action, moved = result.observation, decision.action, result.moved
        else:
            pytest.fail("B8 did not reach the matching branch within 48 actions")
    finally:
        env.close()
    assert {"scan_start_cue", "forward_burst", "approach_matching_branch"} <= reasons
