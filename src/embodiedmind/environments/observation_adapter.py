"""Translate MiniGrid's public symbolic observation into an immutable policy input."""

from dataclasses import dataclass
from operator import index
from typing import Mapping

from minigrid.core.constants import IDX_TO_COLOR, IDX_TO_OBJECT, STATE_TO_IDX
import numpy as np


DIRECTIONS = ("east", "south", "west", "north")
DOOR_STATES = {number: name for name, number in STATE_TO_IDX.items()}
VIEW_SIZE = 7
PASSABLE = frozenset({"empty", "floor", "goal", "lava"})


@dataclass(frozen=True, slots=True)
class Cell:
    forward: int
    right: int
    object: str
    color: str
    state: str

    @property
    def description(self) -> str:
        return " ".join(part for part in (self.color, self.object, self.state) if part)


@dataclass(frozen=True, slots=True)
class Observation:
    mission: str
    direction: int
    cells: tuple[Cell, ...]
    carrying: Cell | None = None

    def cell(self, forward: int, right: int) -> Cell | None:
        return next(
            (cell for cell in self.cells if (cell.forward, cell.right) == (forward, right)),
            None,
        )

    def render(self) -> str:
        """Render compact ASCII with explicit empty and unknown view cells."""
        packed = {(cell.forward, cell.right): cell for cell in self.cells}
        objects = {
            "wall": "#", "floor": ".", "empty": ".", "goal": "G", "lava": "!",
            "door": "D", "key": "K", "ball": "O", "box": "B", "agent": "A",
        }
        rows = []
        named = []
        for forward in range(VIEW_SIZE):
            row = []
            for right in range(-(VIEW_SIZE // 2), VIEW_SIZE // 2 + 1):
                cell = packed.get((forward, right))
                if (forward, right) == (0, 0):
                    row.append("^")
                elif cell is None:
                    row.append("?")
                else:
                    row.append(objects[cell.object])
                    if cell.object not in {"empty", "floor", "wall"}:
                        named.append(f"({forward},{right})={cell.description}")
            rows.append(f"{forward}: {''.join(row)}")
        carrying = self.carrying.description if self.carrying else "nothing"
        return "\n".join(
            [
                f"Facing {DIRECTIONS[self.direction]}; carrying {carrying}.",
                "View rows are forward distance 0-6; columns are right offsets -3..3.",
                "^=you, .=free, #=wall, ?=unknown. Objects are listed as (forward,right).",
                *rows,
                "Visible objects: " + (", ".join(named) if named else "none"),
            ]
        )


def adapt_observation(raw: Mapping[str, object]) -> Observation:
    """Allowlist public fields and decode MiniGrid's x-major egocentric image."""
    image = raw["image"]
    mission = raw["mission"]
    direction = index(raw["direction"])
    if (
        not isinstance(image, np.ndarray)
        or image.shape != (VIEW_SIZE, VIEW_SIZE, 3)
        or not np.issubdtype(image.dtype, np.integer)
    ):
        raise ValueError("expected a 7 x 7 x 3 integer symbolic view")
    if not isinstance(mission, str) or not mission or direction not in range(len(DIRECTIONS)):
        raise ValueError("expected a nonempty public mission and a cardinal direction")

    cells = []
    carrying = None
    for x in range(VIEW_SIZE):
        for y in range(VIEW_SIZE):
            object_id, color_id, state_id = (int(item) for item in image[x, y])
            object_name = IDX_TO_OBJECT.get(object_id)
            if object_name == "unseen":
                continue
            if object_name is None:
                raise ValueError(f"unexpected symbolic object index {object_id}")
            forward = VIEW_SIZE - 1 - y
            right = x - VIEW_SIZE // 2
            color = "" if object_name == "empty" else IDX_TO_COLOR.get(color_id)
            state = DOOR_STATES.get(state_id) if object_name == "door" else ""
            if color is None or state is None:
                raise ValueError(f"unexpected color or state for symbolic object {object_name}")
            cell = Cell(forward, right, object_name, color, state)
            if (forward, right) == (0, 0):
                if object_name != "empty":
                    carrying = cell
            else:
                cells.append(cell)
    return Observation(mission, direction, tuple(cells), carrying)


def front_move_outcome(observation: Observation) -> bool | None:
    """Derive forward odometry from the visible destination and stock move rules."""
    front = observation.cell(1, 0)
    if front is None:
        return None
    return front.object in PASSABLE or (front.object == "door" and front.state == "open")
