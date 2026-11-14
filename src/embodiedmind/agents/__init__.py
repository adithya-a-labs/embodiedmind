"""Construct a fresh, isolated memory condition for each episode."""

from embodiedmind.agents.base import Agent
from embodiedmind.agents.hybrid import Hybrid
from embodiedmind.agents.reactive import Reactive
from embodiedmind.agents.structured import Structured
from embodiedmind.agents.text_memory import TextMemory

VARIANTS = {"B0": Reactive, "B1": TextMemory, "B2": Structured, "B3": Hybrid}


def make_agent(variant: str) -> Agent:
    try:
        cls = VARIANTS[variant]
    except KeyError:
        raise ValueError(f"unknown memory variant {variant!r}") from None
    return cls()
