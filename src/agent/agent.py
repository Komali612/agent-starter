"""FROZEN — identical in every agent repo. Do not edit.

Assembles the agent from the parts that vary: the prompt, the markdown skills in
``skills/``, and the code tools in ``tools/``. With no model set (settings.model
is None) the brain runs keyless.
"""
from pathlib import Path

from agent_core import Agent, load_skills

from .config import settings
from .prompts import SYSTEM_PROMPT
from .tools import TOOLS

_SKILLS_DIR = Path(__file__).parent / "skills"


def build_agent() -> Agent:
    return Agent(
        name=settings.name,
        prompt=SYSTEM_PROMPT,
        skills=load_skills(_SKILLS_DIR),
        tools=TOOLS,
        model=settings.model,
    )
