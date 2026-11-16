import json

from embodiedmind.agents import make_agent
from embodiedmind.environments.observation_adapter import Cell, Observation
from embodiedmind.experiments.runner import episode, purpose_is_stale
from embodiedmind.reasoning.grounding import CONTROLLER_DECISION, resolve_response


MISSION = "go to the red ball"


def test_semantic_memory_is_separate_from_shared_route_map():
    arms = [make_agent(name) for name in ("B11T", "B11P", "B11R")]
    sighting = Observation(MISSION, 0, (Cell(1, 0, "ball", "red", ""),))
    hidden = Observation(MISSION, 1, ())
    contradicted = Observation(MISSION, 0, (Cell(1, 0, "empty", "", ""),))
    for agent in arms:
        agent.observe(sighting, 0)
        agent.observe(hidden, 1, 1)
    assert arms[0].target is None
    assert arms[1].target and arms[2].target
    assert "red ball" in arms[0].context(hidden, 768)
    for agent in arms:
        agent.observe(contradicted, 2, 0)
    assert [agent.target is not None for agent in arms] == [False, True, False]
    assert all(agent.navigation_facts()[0].appearance[0] == "empty" for agent in arms)
    assert arms[2].audit()["revisions"][0]["previous"]["status"] == "CONTRADICTED"


def test_adaptive_policy_can_verify_with_a_side_glance():
    initial = Observation(MISSION, 0, (Cell(1, 2, "ball", "red", ""),))
    for name in ("B11", "B11R"):
        agent = make_agent(name)
        agent.observe(initial, 0)
        hidden = Observation(MISSION, 0, ())
        agent.observe(hidden, 1, 0)
        agent.observe(hidden, 2, 1)
        result = resolve_response(CONTROLLER_DECISION, hidden, agent, name)
        assert (result.reason == "verify_remembered_target") == (name == "B11")
        if name == "B11":
            assert result.action == 1
            planning = {"purpose": "verify", "target": agent.audit()["verification"]["target"]}
            assert not purpose_is_stale(planning, {(0, (1, 2))})
            planning["purpose"] = "act_on_target"
            assert purpose_is_stale(planning, {(0, (1, 2))})


def test_controller_only_step_never_calls_the_model(tmp_path):
    job = {"id": "fixture", "variant": "B11C", "environment": "MiniGrid-DoorKey-8x8-v0",
           "seed": 4002, "intervention": "none", "replicate": 0}
    summary = episode(job, {"max_steps": 1, "max_calls": 1, "memory_bytes": 768}, None, tmp_path,
                      keep_visuals=False)
    row = json.loads((tmp_path / "trajectory.jsonl").read_text())
    assert summary["calls"] == 0
    assert row["request"] is None and not row["planning"]["model_call"]
