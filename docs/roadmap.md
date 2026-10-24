# Development plan

The system is organized around the physical-client protocol, Android companion and backend. First validate the build-versus-extend decision using one real-device state/action path and recovery behavior. The first implementation has two sources and three main flows: a session-start overview, contextual reminders and focus sessions. Additional connectors and character features follow after the core works reliably.

| Stage | Work | Exit condition |
| --- | --- | --- |
| First submission | Analysis, design, evaluation plan and supervisor review | Accessible PDFs and repository version matching prob-period-1 |
| Integration foundation | Account isolation, schema, Calendar and Notion adapters | Authorized records imported with correct identity/date semantics and no duplicates |
| Assistant backend | Session detection, overview, reminders and focus state | Correct actions with retries and disconnected clients |
| Android and web | Setup, integrations, overview, reminder and timer screens | Independently usable clients reflecting shared state |
| Physical client | Pairing, display, rotary actions, reconnect and revocation | Real hardware receives information and controls reminders/timer |
| Briefings | Model adapter, selected records, source references and fallback | Checked factual output; provider failure preserves core behavior |
| Evaluation | Integration verification, timing measurements and participant walkthroughs | Actual measurements, conditions, failures and baseline comparison |

The first-submission deadline is 24 October 2026 at 18:00. Later dates in YouTrack are planning targets for agreement with the supervisor.

The concrete work items and target dates are listed in [tasks.md](tasks.md). The YouTrack issue is the current record for status, acceptance criteria and links to changes.

Connector feasibility precedes live briefings. Shared state and the protocol precede client synchronization checks. User evaluation follows a working core. Electronics and enclosure development are separate from the software deliverables.
