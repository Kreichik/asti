# ASTI

A software platform for a physical desktop assistant, with a backend API, Android application, web application and external-service integrations.

ASTI is my bachelor diploma project in Software Engineering at Astana IT University. The work covers application architecture, account management, integration adapters, shared assistant state and a connection API for compatible devices. Hardware and device firmware are outside the development scope.

## Main features

- Automatic overview when a new work session starts.
- Contextual reminders with snooze and acknowledgment.
- Shared focus and break timer.
- Google Calendar and a selected Notion task database as the first data sources.

Android and web provide an overview, reminders, focus controls, an integration catalogue, device connections and account settings. Physical devices are external clients that communicate through the documented interface.

## Why this project

Students and people working at a desk use several task and calendar services. ASTI provides applications for managing these integrations and assistant functions, and an API through which compatible devices can access the same state. Discussions with two students and one office employee informed the initial source selection.

## Current stage

**First probationary period, 24 October 2026:** analysis and design. This repository contains the proposal, literature review, comparisons, requirements, diagrams, wireframes and evaluation plan. Supervisor review is pending.

The application and live connectors are not implemented yet. Installation and runtime test instructions will accompany the first executable version.

## Documents

| Material | Link |
| --- | --- |
| Consolidated report | [PDF](output/pdf/SE-2413_Kudashov_ProbPeriod1.pdf) · [Editable Word report](output/docx/SE-2413_Kudashov_ProbPeriod1.docx) |
| Requirements | [Requirements and acceptance criteria](docs/requirements.md) |
| Architecture | [Diagram sources and exports](docs/diagrams/) |
| Interaction design | [Android screens](docs/prototype/mobile.png) · [Web workspace](docs/prototype/web.png) |
| Interviews | [Interview notes](docs/interviews.md) |
| Planning | [YouTrack board](https://asti-diploma.youtrack.cloud/agiles/204-1/current) · [Work items](docs/tasks.md) · [Development plan](docs/roadmap.md) |
| Task evidence | [Screenshots PDF](output/pdf/ASTI_YouTrack_Evidence.pdf) |
| Submission | [First-submission checklist](docs/submission-checklist.md) |

The related-system comparison covers Home Assistant/Assist, OpenVoiceOS and Stack-chan. Calendar and Notion are data sources rather than the primary system analogues.

## Technical direction

Initial choices: **Python with FastAPI**, **PostgreSQL**, and **Flutter for Android and web**. Secure WebSocket is the preferred device channel, for compatible external clients. HTTPS polling and MQTT are alternatives in the [technology comparison](docs/report.md#5-technology-comparison).

A replaceable model adapter will generate short briefings from selected source records. Event times and reminder scheduling remain deterministic. If generation fails, the user sees the same records as an ordered list.

## Repository layout

```text
apps/           Android and web client scope
backend/        API, integration and scheduling scope
device/         External device connection API scope
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

The first-submission snapshot is [prob-period-1](https://github.com/Kreichik/asti/tree/prob-period-1). Its report and task evidence are listed in the [submission manifest](docs/submission-version.md). Supervisor feedback is still pending and is stated as such in the report.
