from embodiedmind.agents import make_agent
from embodiedmind.environments.observation_adapter import Cell, Observation
from embodiedmind.reasoning.grounding import resolve_response


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
