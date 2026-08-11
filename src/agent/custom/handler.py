"""FILL — this agent's logic. Fixed filename (Option B)."""
from agent_core import Handler as BaseHandler


class Handler(BaseHandler):
    def handle(self, ctx):
        # your agent's logic goes here
        return ctx.done("hello from a freshly stamped agent")
