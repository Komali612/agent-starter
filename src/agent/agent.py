"""FROZEN — identical in every agent repo. Do not edit.

Wires the parts that vary (name, prompt, skills, handler) into an Agent. Edit
prompts/system.md, skills/skills.py, and custom/handler.py instead.
"""
from agent_core import Agent

from .config import settings
from .custom.handler import Handler
from .prompts import SYSTEM_PROMPT
from .skills import SKILLS


def build_agent() -> Agent:
    return Agent(
        name=settings.name,
        prompt=SYSTEM_PROMPT,
        skills=SKILLS,
        handler=Handler(),
        model=settings.model,
    )
