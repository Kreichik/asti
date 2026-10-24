# ASTI project context

Updated: 24 October 2026. This file records decisions and evidence supplied by the author; it is not evidence of implementation.

## Identity

- Product name: ASTI.
- Author: Кудашов Ян Сергеевич / Yan Kudashov. Group: SE-2413. English spelling of the supervisor's name must be confirmed before final submission; Russian name: Сарсенова Жибек Нуржановна.
- Approved English topic: Development of an Intelligent System for a Physical Desktop Assistant with a Mobile Application and External Service Integration.
- Repository: https://github.com/Kreichik/asti
- Task management: https://asti-diploma.youtrack.cloud/
- Report language: English.
- Submission: 24 October 2026 at 18:00; required tag: prob-period-1. Do not create or move this tag until the submitted materials are finalized.

## Product decisions

- Software engineering is the focus: backend architecture, integration adapters, data processing, client synchronization and software interaction with a physical device.
- Physical client: small round display, rotating ring with click and observable step count; optional sound. Hardware components may change. Electronics and enclosure design are outside the main software scope.
- Android and web are first-class interfaces to the same assistant, not simulators or mock devices. Do not build or describe a device simulator.
- Mobile app supports onboarding, device setup and integration/settings management. Wi-Fi versus Bluetooth provisioning is undecided.
- Mandatory external services: Google Calendar and Notion. Trello, Microsoft Teams, Moodle, email and messaging are possible extensions, not promised deliverables.
- Core scenarios: automatic overview on first interaction after an inactivity interval; contextual upcoming-event/deadline reminders with snooze; focus timer with optional character.
- Do not require a typed phone request merely to obtain an answer on the physical device.
- Voice input is optional and may be excluded; microphone and camera are not required. Character/gamification is optional. Do not claim demonstrated motivational benefits.
- Candidate stack: Python backend and Flutter Android/web. Framework, storage and transport choices need documented comparison.
- AI: pretrained model integration is acceptable as a design option; proposed use is source-grounded briefings, with deterministic scheduling and fallback. Provider is undecided.
- Author has a .kz domain and VPS; exact domain and server specifications have not been supplied.
- Author reported initial display and Wi-Fi experiments. Their code and behavior have not been inspected.

## Interview evidence

Three in-person exploratory discussions: two students and one office employee. Summary was supplied retrospectively by the author on 24 October 2026. No dates, recordings, quotations, individual student attribution or raw transcripts have been supplied.

- Student group: Notion, Google Calendar, Notion Calendar; occasional Microsoft Teams for study events/calls, with most current study interaction in person.
- Office employee: Trello for work tasks and Microsoft Teams for calls.
- Do not invent complaints, missed deadlines, notification overload, preferences for ASTI, or positive reactions to a prototype.
- Follow-up interviews must test the proposed fragmentation problem, preferred reminder timing and tolerance of interruptions.

## Supervisor evidence

Author reports that the supervisor discussed and accepted the topic and is ready to receive the current report. No substantive feedback on today's requirements, architecture or report has yet been supplied. Keep this pending until real feedback is available.

## Submission requirements

Consolidated PDF: 11 sections in the prescribed order and a table of contents; filename SE-2413_Kudashov_ProbPeriod1.pdf; limit 100 MB. Separate task-board and task screenshots PDF: limit 10 MB. Both must match prob-period-1. Full accessible repository, tag, prototype, diagram-source and task links are required. Public repository authorized by the author. Do not upload the topic application containing personal contact details into the public repository.
