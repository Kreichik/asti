# Backend

Planned Python API and workers for accounts, device authorization, Calendar/Notion adapters, normalized source records, overview, reminders and focus state. A replaceable model adapter produces briefings with deterministic fallback.

The initial design uses FastAPI and PostgreSQL. Workers can run as separate processes sharing the domain model. See the [architecture](../docs/diagrams/components.png) and [requirements](../docs/requirements.md). Startup commands will be added with the first executable implementation.
