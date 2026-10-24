# ASTI

ASTI is a bachelor diploma project on an intelligent software system for a physical desktop assistant, with Android and web interfaces and external service integration.

## Project purpose

The system is designed to combine tasks and scheduled events from explicitly connected services into a source-linked overview, deliver contextual reminders, and support focus sessions. The initial problem hypothesis is that users who organize work across separate services must repeatedly check those sources to understand their upcoming obligations. Three exploratory discussions establish use of several relevant tools; they do not yet establish demand for ASTI or measurable productivity benefits.

## Author and supervisor

- Sole author: Yan Kudashov (Кудашов Ян Сергеевич), SE-2413, [Kreichik](https://github.com/Kreichik).
- Supervisor: Сарсенова Жибек Нуржановна.
- Author responsibilities: analysis, literature review, requirements, architecture, backend, Android/web clients, device communication software, integration, testing and documentation.
- Approved topic: **Development of an Intelligent System for a Physical Desktop Assistant with a Mobile Application and External Service Integration**.

## Scope

The planned first implementation connects Google Calendar and a selected Notion task database, normalizes records, produces an automatic session-start overview, schedules contextual reminders and synchronizes a focus timer across authorized clients. The physical client supports a round display and a rotary ring with click. Android, web and the physical device are independent interfaces to the same system; no device simulator is planned.

Hardware engineering, model training, camera input and mandatory voice input are outside the initial scope. Optional character interaction and future connectors require separate prioritization.

## Status on 24 October 2026

Analysis and design are in preparation. The author has reported preliminary hardware/display and Wi-Fi experiments, but their source code has not been imported or verified here. This repository currently documents the planned system, not a production application. There are no measured evaluation results or verified live service integrations yet.

## Candidate technologies

Python backend, Flutter Android/web clients, relational storage, authenticated device communication and a replaceable language-model adapter. Specific choices will be supported by the technology comparison rather than treated as implemented facts.

## Materials and task management

- [Consolidated report source](docs/report.md)
- [Report PDF for supervisor review](output/pdf/ASTI_Supervisor_Review.pdf)
- [YouTrack board and task evidence PDF](output/pdf/ASTI_YouTrack_Evidence.pdf)
- [Requirements](docs/requirements.md)
- [Interview evidence](docs/interviews.md)
- [Editable architecture diagrams](docs/diagrams/)
- [YouTrack Kanban board](https://asti-diploma.youtrack.cloud/agiles/204-1/current)
- [Interaction wireframes](docs/prototype/flows.png)
- [Project decisions and evidence boundaries](PROJECT_CONTEXT.md)

## Repository organization

Documentation and diagrams live under `docs/`; submission PDFs will be under `output/pdf/`. Source code, tests and deployment configuration will be added when implementation begins. Runtime secrets and personal contact information must not be committed.

## Setup and verification

There is no runnable application in this analysis-stage version. Setup, execution and automated-test instructions will be added with the first executable implementation. The documentation can be reviewed directly in GitHub.

## Development workflow

Each meaningful work item is tracked in YouTrack with an assignee, priority, due date, expected outcome and acceptance criteria. Task IDs belong in branch names and commit or pull-request descriptions, with reciprocal links from the issue. Significant changes are developed on branches and submitted through pull requests; supervisor reviews are recorded at agreed checkpoints. Work history is recorded at the actual time it occurs.

The submission tag `prob-period-1` will identify the finalized first submission. It has not been created while these materials are still being prepared.
