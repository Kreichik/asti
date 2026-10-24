# ASTI

A desktop assistant that brings upcoming events and task deadlines together, with a focus timer and a small physical display. The same assistant is available through an Android app and a web interface.

ASTI is my bachelor diploma project in Software Engineering at Astana IT University. The work focuses on service integrations, backend architecture, client synchronization and communication with the desktop device.

## Main features

- Automatic overview when a new work session starts.
- Contextual reminders with snooze and acknowledgment.
- Shared focus and break timer.
- Google Calendar and a selected Notion task database as the first data sources.

The physical client uses a round display and a rotary ring with click. Android and web have their own overview and controls, plus account, integration and device settings. Character animation and sound are optional. Voice input, camera features and additional connectors are outside the first implementation.

## Why this project

Students and people working at a desk often keep commitments in several tools. ASTI explores whether a short overview and well-timed reminders make those commitments easier to follow without repeatedly checking each source. Discussions with two students and one office employee informed the source selection; the proposed flows still need user evaluation.

## Current stage

**First probationary period, 24 October 2026:** analysis and design. This repository contains the proposal, literature review, comparisons, requirements, diagrams, wireframes and evaluation plan. Supervisor review is pending.

The application and live connectors are not implemented yet. Earlier display and Wi-Fi experiments are separate from this repository. Installation and runtime test instructions will accompany the first executable version.

## Documents

| Material | Link |
| --- | --- |
| Consolidated report | [Review PDF](output/pdf/ASTI_Supervisor_Review.pdf) · [Editable text](docs/report.md) |
| Requirements | [Requirements and acceptance criteria](docs/requirements.md) |
| Architecture | [Diagram sources and exports](docs/diagrams/) |
| Interaction design | [Overview, reminder and focus wireframes](docs/prototype/flows.png) |
| Interviews | [Notes and follow-up questions](docs/interviews.md) |
| Planning | [YouTrack board](https://asti-diploma.youtrack.cloud/agiles/204-1/current) · [Work items](docs/tasks.md) · [Development plan](docs/roadmap.md) |
| Task evidence | [Screenshots PDF](output/pdf/ASTI_YouTrack_Evidence.pdf) |
| Submission | [First-submission checklist](docs/submission-checklist.md) |

## Technical direction

Initial choices: **Python with FastAPI**, **PostgreSQL**, and **Flutter for Android and web**. Secure WebSocket is the preferred device channel, subject to real-hardware validation. HTTPS polling and MQTT are alternatives in the [technology comparison](docs/report.md#5-technology-comparison).

A replaceable model adapter will generate short briefings from selected source records. Event times and reminder scheduling remain deterministic. If generation fails, the user sees the same records as an ordered list.

## Repository layout

```text
apps/           Android and web client scope
backend/        API, integration and scheduling scope
device/         Device protocol and client software scope
docs/           Report, requirements, diagrams and planning
config/         Configuration conventions
tests/          Verification scope and acceptance coverage
tools/          Documentation PDF build scripts
output/pdf/     Current report and task evidence
```

Application directories currently describe component responsibilities. Implementation code will be added as the work progresses. The PDF tools can be run separately; see [tools](tools/README.md).

## Author and supervision

**Author:** Yan Kudashov (Кудашов Ян Сергеевич), SE-2413 — [Kreichik](https://github.com/Kreichik). I am responsible for analysis, architecture, implementation, testing and documentation.

**Supervisor:** Сарсенова Жибек Нуржановна.

**Approved topic:** Development of an Intelligent System for a Physical Desktop Assistant with a Mobile Application and External Service Integration.

## Workflow

Work items are tracked in YouTrack. Branches and commits reference the corresponding ASTI task, and the task links back to its deliverable or pull request. Significant changes are reviewed with the supervisor at agreed checkpoints.

The first submission will be fixed with the tag `prob-period-1` after review and final checks. It has not been tagged yet.
