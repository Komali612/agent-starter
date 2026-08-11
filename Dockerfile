# FROZEN — identical in every agent repo.
# Multi-stage: install into a builder, copy into a slim runtime.
FROM python:3.11-slim AS build
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
# NOTE: agent-core must be resolvable (private index / extra-index-url).
RUN pip install --no-cache-dir .

FROM python:3.11-slim AS runtime
WORKDIR /app
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
ENTRYPOINT ["agent"]
