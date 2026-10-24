# Initial requirements and acceptance criteria

Status: proposed requirements for supervisor review, 24 October 2026. These criteria describe future acceptance checks; they are not test results.

| ID | Priority | Requirement | Acceptance criterion |
| --- | --- | --- | --- |
| FR-01 | Must | Authenticate users and isolate their data | Two separately authorized users cannot retrieve each other's records, integration credentials or device controls |
| FR-02 | Must | Connect and disconnect Google Calendar | Authorized calendar events are imported with source ID, start/end, time zone and source URL; revoked access is reported without exposing credentials |
| FR-03 | Must | Connect a user-selected Notion task data source | A documented mapping imports title, status and available due date; records without a due date are shown without an invented deadline |
| FR-04 | Must | Normalize tasks and events with provenance | Each item retains service, external ID, source URL when available, last synchronization time and the original date semantics |
| FR-05 | Must | Show an automatic session-start overview | First interaction after a configurable inactivity interval presents the overview once; subsequent menu navigation does not repeatedly restart it |
| FR-06 | Must | Deliver configurable contextual reminders | A reminder is scheduled using exact source dates and user settings; snooze changes the reminder, not the external event deadline; acknowledgment is recorded |
| FR-07 | Must | Support focus and break intervals | User can start, pause, resume and stop a timer; reconnecting clients recover its state from server timestamps; reminder behavior follows an explicit focus policy |
| FR-08 | Must | Provide Android and web clients | Both clients allow overview viewing, integration management, reminder settings and focus control, without requiring a physical device |
| FR-09 | Must | Pair and revoke a physical client | A user can authorize an identified device and revoke it; the revoked device cannot receive subsequent protected data |
| FR-10 | Must | Map rotary interaction to software actions | Clockwise/counterclockwise steps move menu selection, click confirms; reminder snooze and focus start are accessible without typed input |
| FR-11 | Must | Generate grounded overview text with fallback | Every event/task statement references imported items; a failed generation falls back to an ordered deterministic overview and does not prevent reminders |
| FR-12 | Should | Show optional character and sound | User can disable character animation and sound independently; disabling them preserves reminders and timer functionality |
| FR-13 | Must | Report connection freshness and errors | Clients display last successful synchronization and explain disconnected/expired integrations; stale data is not presented as live |
| FR-14 | Should | Allow manual refresh | Refresh reports success or a recoverable error and does not duplicate existing source items |
| NFR-01 | Must | Protect credentials | Client responses and logs contain no service access/refresh tokens; server secrets are excluded from Git and encrypted at rest with the key stored separately |
| NFR-02 | Must | Make synchronization idempotent | Replaying the same source response creates no duplicate item or duplicate reminder for the same occurrence |
| NFR-03 | Must | Handle local times explicitly | Acceptance cases cover UTC conversion, all-day dates, events crossing midnight and recurrence exceptions; date-only tasks are not silently treated as precise instants |
| NFR-04 | Must | Recover from network interruptions | Disconnect/reconnect produces an explicit state and recovers current reminders/timer; missed and expired notifications follow a documented replay policy |
| NFR-05 | Should | Keep interaction responsive | Proposed target: p95 ordinary API response below 500 ms on the documented VPS test environment, excluding external-service and model waits |
| NFR-06 | Should | Deliver reminders promptly | Proposed target: server dispatch within 5 seconds of scheduled time under a stated healthy-connection workload; external import delay measured separately |
| NFR-07 | Must | Bound model latency | A configurable timeout leads to a deterministic fallback; provider name, model version, input size, latency and estimated usage cost are recorded without sensitive payloads |
| NFR-08 | Must | Keep connector boundaries extensible | A new connector can implement the documented adapter contract without changing timer or client domain logic |
| NFR-09 | Must | Support inspection and testing | Import, reminder and device-action records use correlation IDs; automated checks cover authorization, idempotency, timing and failures |

## Open decisions

Exact inactivity threshold, default reminder lead times, snooze duration, source write-back, device network provisioning and model provider remain subject to design review. Current plan prioritizes read-only external data; marking an ASTI reminder acknowledged does not mark a Notion task complete.
