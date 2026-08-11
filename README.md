# my-agent

Starter repo for a new agent. **Clone it, then change a few details** — that's
the whole workflow. No special tooling required.

## Create a new agent

1. Clone/copy this repo under your agent's name.
2. Set the name in `pyproject.toml`, `Makefile`, and `deploy/helm/values.yaml`
   (and `AGENT_NAME` in `.env` / values).
3. Edit the three files that define what it does:
   - `src/agent/prompts/system.md` — the prompt
   - `src/agent/skills/skills.py` — the skills
   - `src/agent/custom/handler.py` — the logic

Everything else — the wiring (`main.py`, `agent.py`, `config.py`), the
Dockerfile, the Helm chart, CI — is inherited from `agent-core` and rarely
touched.

## Run locally

```bash
uv sync
cp .env.example .env
uv run agent            # serves on http://localhost:8080
```

## Ship (Kubernetes)

```bash
make image
make deploy
```
