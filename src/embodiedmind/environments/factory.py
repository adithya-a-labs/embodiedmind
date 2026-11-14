"""Construction and seeded smoke checks for unmodified official tasks."""

import hashlib

import gymnasium as gym
import minigrid

from embodiedmind.environments.observation_adapter import adapt_observation


DYNAMIC_OBSTACLES = "MiniGrid-Dynamic-Obstacles-8x8-v0"
OFFICIAL_ENVIRONMENTS = (
    "BabyAI-GoToObjS6-v1",
    "MiniGrid-DoorKey-8x8-v0",
    "BabyAI-GoToObjMazeS7-v0",
    "MiniGrid-MemoryS13-v0",
    "MiniGrid-MemoryS17Random-v0",
    "MiniGrid-MultiRoom-N6-v0",
    "BabyAI-KeyCorridorS3R3-v0",
    "BabyAI-BlockedUnlockPickup-v0",
    "BabyAI-PutNextS5N2-v0",
    DYNAMIC_OBSTACLES,
    "BabyAI-SynthS5R2-v0",
)


def make_environment(env_id: str, *, render_mode: str | None = None) -> gym.Env:
    if env_id not in OFFICIAL_ENVIRONMENTS or env_id not in gym.registry:
        candidates = sorted(
            name for name in gym.registry if name.startswith(("BabyAI-", "MiniGrid-"))
        )
        raise ValueError(
            f"Unsupported MiniGrid task {env_id!r} in MiniGrid {minigrid.__version__}. "
            f"Registered tasks: {', '.join(candidates)}"
        )
    return gym.make(env_id, render_mode=render_mode)


def smoke_environment(
    env_id: str, seed: int, max_steps: int = 60, *, render: bool = False
) -> tuple[dict, object | None]:
    """Verify reset, action identities and bounds, step transitions and headless output."""
    if max_steps <= 0:
        raise ValueError("smoke step cap must be positive")
    env = make_environment(env_id, render_mode="rgb_array" if render else None)
    try:
        raw, _ = env.reset(seed=seed)
        observation = adapt_observation(raw)
        reset, _ = env.reset(seed=seed)
        if observation != adapt_observation(reset):
            raise ValueError("same seed did not reproduce the public reset")
        expected = {"left": 0, "right": 1, "forward": 2, "pickup": 3, "drop": 4,
                    "toggle": 5, "done": 6}
        env_actions = env.unwrapped.actions
        action_count = 3 if env_id == DYNAMIC_OBSTACLES else len(expected)
        if {action.name: int(action) for action in env_actions} != expected or (
            env.action_space.n != action_count or env.action_space.start != 0
        ):
            raise ValueError(f"unexpected stock action space: {env.action_space}")
        frame = None
        if render:
            # The render is evaluator-only. No policy is created by this smoke check.
            frame = env.render()
            if frame is None or frame.ndim != 3 or frame.shape[2] != 3:
                raise ValueError("expected a headless RGB visualization")
        min_reward = -1 if env_id == DYNAMIC_OBSTACLES else 0
        for step in range(1, max_steps + 1):
            action = (0, 2, 1, 2)[(step - 1) % 4]
            updated, reward, terminated, truncated, _ = env.step(action)
            current = adapt_observation(updated)
            if current.mission != observation.mission or not min_reward <= float(reward) <= 1:
                raise ValueError("invalid mission or reward during smoke rollout")
            if terminated or truncated:
                break
        return {
            "env_id": env_id,
            "seed": seed,
            "mission": observation.mission,
            "observation_shape": list(raw["image"].shape),
            "observation_hash": hashlib.sha256(raw["image"].tobytes()).hexdigest(),
            "deterministic_reset": True,
            "steps": step,
            "reward": float(reward),
            "terminated": bool(terminated),
            "truncated": bool(truncated),
            "runner_cap_reached": step == max_steps and not (terminated or truncated),
        }, frame
    finally:
        env.close()
