"""Construct a fresh, isolated memory condition for each episode."""

from embodiedmind.agents.base import Agent
from embodiedmind.agents.hybrid import Hybrid
from embodiedmind.agents.grounded import GroundedMemory
from embodiedmind.agents.reactive import Reactive
from embodiedmind.agents.structured import Structured
from embodiedmind.agents.text_memory import TextMemory

VARIANTS = {"B0": Reactive, "B1": TextMemory, "B2": Structured, "B3": Hybrid,
            "B0G": Reactive, "B3G": Hybrid, "B4": GroundedMemory,
            "B5": GroundedMemory, "B6": GroundedMemory}


def make_agent(variant: str, workflows=()) -> Agent:
    try:
        cls = VARIANTS[variant]
    except KeyError:
        raise ValueError(f"unknown memory variant {variant!r}") from None
    return cls(workflows=workflows) if variant == "B6" else cls()
