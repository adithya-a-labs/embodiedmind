from embodiedmind.environments.observation_adapter import Cell, Observation
from embodiedmind.reasoning.prompts import _route_hint, prompt_for


def obs(mission, cells, carrying=None):
    return Observation(mission, 0, tuple(cells), carrying)


def test_route_uses_legal_visible_geometry():
    view = obs("go to the yellow ball", [
        Cell(1, 0, "wall", "grey", ""),
        Cell(0, 1, "empty", "", ""),
        Cell(1, 1, "empty", "", ""),
        Cell(2, 1, "ball", "yellow", ""),
    ])
    assert "action: 1." in _route_hint(view)
    assert "secret" not in prompt_for(view, "")


def test_operates_door_when_visible():
    view = obs("use the key to open the door and then get to the goal", [
        Cell(1, 0, "door", "yellow", "locked"),
    ], Cell(0, 0, "key", "yellow", ""))
    assert "action: 5." in _route_hint(view)
