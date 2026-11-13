"""Custom seeded BabyAI GoTo benchmark with evaluator-only interventions."""

from collections import deque
from dataclasses import asdict, dataclass
from math import isfinite

from minigrid.core.constants import DIR_TO_VEC, OBJECT_TO_IDX
from minigrid.core.world_object import Ball, Box, Key
from minigrid.envs.babyai.core.roomgrid_level import RoomGridLevel
from minigrid.envs.babyai.core.verifier import GoToInstr, ObjDesc
import numpy as np


DYNAMIC_ENV_ID = "EmbodiedMind-GoToShift-v0"
INTERVENTIONS = ("no_change", "dropout", "relocation")
TARGET_COLORS = ("blue", "green", "purple", "red", "yellow")
TARGET_TYPES = (Ball, Key)
NEIGHBORS = tuple(tuple(int(axis) for axis in direction) for direction in DIR_TO_VEC)


@dataclass(frozen=True, slots=True)
class InterventionConfig:
    step: int = 5
    dropout_until: int = 12
    dropout_probability: float = 0.25

    def __post_init__(self):
        if self.step < 1 or self.dropout_until < self.step:
            raise ValueError("expected a positive step with a nonempty dropout window")
        if not isfinite(self.dropout_probability) or not 0 <= self.dropout_probability <= 1:
            raise ValueError("dropout probability must be between zero and one")


class DynamicGoToObject(RoomGridLevel):
    """Same GoTo verifier and start across arms, with one prespecified event."""

    def __init__(
        self,
        intervention: str,
        *,
        render_mode: str | None = None,
        config: InterventionConfig | None = None,
    ):
        if intervention not in INTERVENTIONS:
            raise ValueError(f"unsupported intervention {intervention!r}: {INTERVENTIONS}")
        self.intervention = intervention
        self.intervention_config = config or InterventionConfig()
        self.intervention_log: list[dict] = []
        super().__init__(room_size=15, num_rows=1, num_cols=1, render_mode=render_mode)

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        if seed is None:
            raise ValueError("the custom benchmark requires an explicit episode seed")
        self.intervention_log.clear()
        self._mask_seed = seed
        return super().reset(seed=seed, options=options)

    def gen_mission(self):
        self.agent_dir = self._rand_int(0, 4)
        self.agent_pos = (self._rand_int(6, 9), self._rand_int(6, 9))
        dx, dy = NEIGHBORS[self.agent_dir]

        def relative(forward, right):
            x, y = self.agent_pos
            return x + forward * dx - right * dy, y + forward * dy + right * dx

        # Use center axis 7 for long forward placements on the 15 × 15 map.
        if dx:
            self.agent_pos = (7, self.agent_pos[1])
        else:
            self.agent_pos = (self.agent_pos[0], 7)
        self._original_pos = relative(6, self._rand_int(1, 3))
        self._destination = relative(4, self._rand_int(4, 6))
        target_type = TARGET_TYPES[self._rand_int(0, len(TARGET_TYPES))]
        target_color = TARGET_COLORS[self._rand_int(0, len(TARGET_COLORS))]
        self._target = target_type(target_color)
        self.put_obj(self._target, *self._original_pos)
        distractor_colors = tuple(color for color in TARGET_COLORS if color != target_color)
        self.put_obj(Ball(distractor_colors[0]), *relative(3, -2))
        self.put_obj(Box(distractor_colors[1]), *relative(-4, -1))
        self.put_obj(Key(distractor_colors[2]), *relative(-2, 3))
        self.instrs = GoToInstr(ObjDesc(self._target.type, self._target.color))
        if not self._visible(*self._original_pos):
            raise RuntimeError("custom layout must make the original target publicly observable")
        if not self._target_reachable(self._original_pos):
            raise RuntimeError("custom layout created an unreachable mission")

    def _visible(self, x: int, y: int) -> bool:
        relative = self.relative_coords(x, y)
        if relative is None:
            return False
        _, visible = self.gen_obs_grid()
        return bool(visible[relative])

    def _target_reachable(self, target: tuple[int, int]) -> bool:
        """Find public-action reachability to a tile from which facing the target wins."""
        start = tuple(int(axis) for axis in self.agent_pos)
        queue = deque([start])
        visited = {start}
        while queue:
            x, y = queue.popleft()
            for dx, dy in NEIGHBORS:
                neighbor = x + dx, y + dy
                if neighbor == target:
                    return True
                if neighbor in visited or not (
                    0 < neighbor[0] < self.width - 1 and 0 < neighbor[1] < self.height - 1
                ):
                    continue
                cell = self.grid.get(*neighbor)
                if cell is None or cell.can_overlap():
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    def _relocate(self, step: int) -> bool:
        old, new = self._original_pos, self._destination
        event = {
            "intervention": "relocation", "step": step, "applied": False,
            "old_position": old, "planned_position": new,
        }
        if self.grid.get(*old) is not self._target:
            event["reason"] = "target_displaced_before_trigger"
        elif new == tuple(self.agent_pos) or self.grid.get(*new) is not None:
            event["reason"] = "destination_occupied"
        elif self._visible(*old) or self._visible(*new):
            event["reason"] = "old_or_new_position_visible_at_trigger"
        else:
            self.grid.set(*old, None)
            self.grid.set(*new, self._target)
            if not self._target_reachable(new):
                self.grid.set(*new, None)
                self.grid.set(*old, self._target)
                event["reason"] = "destination_unreachable"
            else:
                self._target.cur_pos = new
                self.update_objs_poss()
                if list(self.instrs.desc.obj_poss) != [new]:
                    raise RuntimeError("BabyAI verifier failed to follow the target entity")
                event.update(applied=True, reason="both_positions_unseen_and_reachable", new_position=new)
        self.intervention_log.append(event)
        return event["applied"]

    def _dropout(self, observation: dict, step: int) -> dict:
        image = observation["image"].copy()
        random = np.random.default_rng(np.random.SeedSequence([self._mask_seed, 91, step]))
        keep = image[:, :, 0] != OBJECT_TO_IDX["unseen"]
        masked = (random.random(keep.shape) < self.intervention_config.dropout_probability) & keep
        center_x, center_y = image.shape[0] // 2, image.shape[1] - 1
        # Carrying and the immediate destination support the common public action/odometry contract.
        masked[center_x, center_y - 1:center_y + 1] = False
        image[masked] = (OBJECT_TO_IDX["unseen"], 0, 0)
        count = int(masked.sum())
        self.intervention_log.append({
            "intervention": "dropout", "step": step, "applied": count > 0,
            "masked_cells": count,
            "reason": "seeded_symbolic_mask" if count else "no_visible_cells_selected",
        })
        return {**observation, "image": image}

    def step(self, action):
        observation, reward, terminated, truncated, _ = super().step(action)
        step = self.step_count
        config = self.intervention_config
        if step == config.step:
            if terminated or truncated:
                self.intervention_log.append({
                    "intervention": self.intervention, "step": step, "applied": False,
                    "reason": "terminal_before_intervention",
                })
            elif self.intervention == "relocation" and self._relocate(step):
                observation = self.gen_obs()
            elif self.intervention == "no_change":
                self.intervention_log.append({
                    "intervention": self.intervention, "step": step, "applied": False,
                    "reason": "control_arm",
                })
        if self.intervention == "dropout" and config.step <= step <= config.dropout_until:
            if not (terminated or truncated):
                observation = self._dropout(observation, step)
        return observation, reward, terminated, truncated, {}

    @property
    def intervention_spec(self) -> dict:
        return asdict(self.intervention_config)


def make_dynamic_environment(
    intervention: str, *, render_mode: str | None = None, config: InterventionConfig | None = None
) -> DynamicGoToObject:
    return DynamicGoToObject(intervention, render_mode=render_mode, config=config)
