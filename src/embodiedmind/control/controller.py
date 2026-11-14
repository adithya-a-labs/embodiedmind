"""Shared primitive controller, with an explicit policy-visible step projection."""

from dataclasses import dataclass

import gymnasium as gym

from embodiedmind.environments.observation_adapter import (
    Observation,
    adapt_observation,
    front_move_outcome,
)


@dataclass(frozen=True, slots=True)
class AgentStep:
    observation: Observation
    moved: bool | None


@dataclass(frozen=True, slots=True)
class StepResult:
    agent: AgentStep
    reward: float
    terminated: bool
    truncated: bool

    @property
    def observation(self) -> Observation:
        return self.agent.observation

    @property
    def moved(self) -> bool | None:
        return self.agent.moved


class PrimitiveController:
    def __init__(self, environment: gym.Env):
        self._environment = environment
        self._observation = None
        self._finished = True

    def reset(self, seed: int) -> Observation:
        raw, _ = self._environment.reset(seed=seed)
        self._observation = adapt_observation(raw)
        self._finished = False
        return self._observation

    def step(self, action: int) -> StepResult:
        if self._observation is None or self._finished:
            raise RuntimeError("reset before stepping a new episode")
        if type(action) is not int or not self._environment.action_space.contains(action):
            raise ValueError(f"illegal primitive action: {action!r}")
        moved = front_move_outcome(self._observation) if action == 2 else None
        raw, reward, terminated, truncated, _ = self._environment.step(action)
        self._observation = adapt_observation(raw)
        self._finished = bool(terminated or truncated)
        return StepResult(
            AgentStep(self._observation, moved), float(reward), bool(terminated), bool(truncated)
        )
