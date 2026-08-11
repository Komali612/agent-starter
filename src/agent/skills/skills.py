"""FILL — this agent's skills. Fixed filename (Option B).

Define each capability as a Skill subclass and list them all in SKILLS.
"""
from agent_core import Skill


class ExampleSkill(Skill):
    name = "example"

    def run(self, **kwargs):
        # replace with a real skill
        return {"ok": True}


SKILLS = [ExampleSkill()]
