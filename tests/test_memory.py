"""Verify matched memory inputs, explicit revision and the evidence boundary."""

import pytest

from embodiedmind.agents import make_agent
from embodiedmind.environments.observation_adapter import Cell, Observation
from embodiedmind.memory.belief import BeliefLedger, STALE_AFTER_STEPS


def view(*cells: Cell, heading: int = 0) -> Observation:
    return Observation("go to the blue key", heading, cells)


BLUE_KEY = Cell(2, 0, "key", "blue", "")
EMPTY_AT_KEY = Cell(2, 0, "empty", "", "")


def test_reactive_has_no_memory_and_text_history_keeps_public_clue():
    reactive = make_agent("B0")
    text = make_agent("B1")
    for agent in (reactive, text):
        agent.observe(view(BLUE_KEY), 0)
        agent.observe(view(), 1)

    assert reactive.context(view(), 500) == ""
    assert reactive.audit()["selected_facts"] == []
    assert "blue key@2,0" in text.context(view(), 500)
    assert text.audit()["selected_facts"][0]["id"] == "o0"
    assert text.audit()["selected_facts"][0]["cells"][0]["object"] == "key"


@pytest.mark.parametrize("variant", ("B0", "B1", "B2", "B3"))
@pytest.mark.parametrize("budget", (0, 21, 75, 190, 500))
def test_memory_context_has_hard_common_ascii_budget(variant, budget):
    agent = make_agent(variant)
    agent.observe(view(BLUE_KEY, Cell(3, 0, "ball", "grün", "")), 0)
    agent.record_decision(0, "look for the key 🗝")
    obs = view()
    agent.observe(obs, 1, prev_action=0)
    context = agent.context(obs, budget)

    assert len(context.encode("ascii")) <= budget
    assert agent.audit()["context_bytes"] == len(context)
    assert all(fact["id"] in context for fact in agent.audit()["selected_facts"])


@pytest.mark.parametrize("variant", ("B2", "B3"))
def test_spatial_rotation_translation_blocking_and_unknown(variant):
    agent = make_agent(variant)
    agent.observe(view(BLUE_KEY), 0)
    obs = view(heading=1)
    agent.observe(obs, 1, prev_action=1)
    assert "blue key (0, -2)" in agent.context(obs, 400)

    agent.observe(obs, 2, prev_action=2, moved=True)
    assert "blue key (-1, -2)" in agent.context(obs, 400)
    agent.observe(obs, 3, prev_action=2, moved=False)
    assert "blue key (-1, -2)" in agent.context(obs, 400)
    assert agent.audit()["event"]["position"] == [0, 1]
    assert agent.audit()["selected_facts"][0]["source_event_ids"] == ["o0"]

    agent.observe(obs, 4, prev_action=2, moved=None)
    assert agent.audit()["event"]["segment"] == 1
    assert "blue key" not in agent.context(obs, 400)


def test_repeated_observations_preserve_provenance_and_facts_and_reset():
    agent = make_agent("B3")
    agent.observe(view(BLUE_KEY), 0)
    agent.observe(view(BLUE_KEY), 1)
    obs = view()
    agent.observe(obs, 2)
    agent.context(obs, 500)
    fact = agent.audit()["selected_facts"][0]
    assert fact["id"] == "f0.0"
    assert fact["source_event_ids"] == ["o0", "o1"]
    assert fact["observed_at_step"] == 0
    assert fact["last_verified_step"] == 1
    assert len(agent.log.events) == 3

    with pytest.raises(ValueError, match="step order"):
        agent.observe(obs, 2)

    next_agent = make_agent("B3")
    next_agent.observe(obs, 0)
    assert "blue key" not in next_agent.context(obs, 500)


def test_observed_empty_contradicts_key_but_unknown_does_not():
    structured = make_agent("B2")
    hybrid = make_agent("B3")
    for agent in (structured, hybrid):
        agent.observe(view(BLUE_KEY), 0)
        agent.observe(view(), 1)
        assert "blue key" in agent.context(view(), 500)
        assert agent.audit()["revisions"] == []
        agent.observe(view(EMPTY_AT_KEY), 2)

    [revision] = hybrid.audit()["revisions"]
    assert revision["previous"]["status"] == "CONTRADICTED"
    assert revision["previous"]["id"] == "f0.0"
    assert revision["replacement"]["contradicts_fact_id"] == "f0.0"
    assert revision["replacement"]["object"] == "empty"
    assert structured.audit()["revisions"] == []

    for agent in (structured, hybrid):
        agent.observe(view(), 3)
    assert "blue key" in structured.context(view(), 500)
    assert "blue key" not in hybrid.context(view(), 500)
    assert isinstance(hybrid.index, BeliefLedger)
    assert len(hybrid.index.history) == 1
    assert hybrid.log.events[0].observation == view(BLUE_KEY)


def test_dynamic_age_and_reobservation_keep_history():
    agent = make_agent("B3")
    agent.observe(view(BLUE_KEY, Cell(2, 1, "wall", "grey", "")), 0)
    for step in range(1, STALE_AFTER_STEPS + 1):
        agent.observe(view(), step)
    assert "STALE; reobserve" in agent.context(view(), 500)
    facts = {fact["object"]: fact for fact in agent.audit()["selected_facts"]}
    assert facts["key"]["status"] == "STALE"
    assert facts["wall"]["status"] == "OBSERVED"
    assert agent.audit()["revisions"][0]["reason"] == "age"

    agent.observe(view(BLUE_KEY), STALE_AFTER_STEPS + 1)
    agent.observe(view(), STALE_AFTER_STEPS + 2)
    agent.context(view(), 500)
    key = next(fact for fact in agent.audit()["selected_facts"] if fact["object"] == "key")
    assert key["status"] == "OBSERVED"
    assert key["id"] == "f0.0"
    assert key["source_event_ids"] == ["o0", f"o{STALE_AFTER_STEPS + 1}"]


def test_cardinal_transform_does_not_read_simulator_state():
    agent = make_agent("B2")
    agent.observe(view(Cell(3, 1, "door", "blue", "locked"), heading=2), 0)
    obs = view(heading=3)
    agent.observe(obs, 1, prev_action=1)
    assert "blue door locked (1, -3)" in agent.context(obs, 500)
    assert agent.audit()["selected_facts"][0]["position"] == [-3, -1]
