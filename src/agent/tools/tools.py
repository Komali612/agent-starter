"""Tools — the code capabilities the LLM can call. Add yours here.

Each Tool has a ``name``, a ``description`` (the model reads it to decide when to
call it), a JSON-schema for its inputs, and a ``run()``. List them in ``TOOLS``.
"""
from agent_core import Tool


class Echo(Tool):
    name = "echo"
    description = "Echo a message back to the caller."
    parameters = {
        "type": "object",
        "properties": {"text": {"type": "string", "description": "text to echo"}},
        "required": ["text"],
    }

    def run(self, text: str):
        return {"echo": text}


# The tools this agent exposes to the brain. Replace with your own.
TOOLS = [Echo()]
