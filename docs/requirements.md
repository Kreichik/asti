# Requirements and acceptance criteria

### 6.1 Functional requirements

Must identifies the required first-version functions. Should identifies optional extensions.

| ID | Priority | Requirement and acceptance criterion |
| --- | --- | --- |
| FR-01 | Must | Authenticate users and isolate their data: one user cannot read another user's items, connection secrets or device controls |
| FR-02 | Must | Import Google Calendar events preserving external identity, start/end, time zone and source reference; report revoked authorization |
| FR-03 | Must | Import selected Notion task data using documented property mapping; absent due dates remain absent |
| FR-04 | Must | Preserve provider, external ID, connection ownership, source URL where available and last successful synchronization |
| FR-05 | Must | Present an overview automatically on first interaction after a configurable inactivity interval, without restarting it on every menu action |
| FR-06 | Must | Schedule contextual reminders; snooze affects the reminder, not the external deadline; acknowledgment is synchronized |
| FR-07 | Must | Start, pause, resume and stop focus/break intervals; recover timer state from authoritative timestamps after reconnection |
| FR-08 | Must | Support overview, integration/settings management and focus controls in Android and web without requiring a physical device |
| FR-09 | Must | Associate a compatible external device with an account through the applications; revocation blocks subsequent protected access |
| FR-10 | Must | Expose authorized API commands for reminder acknowledgment, snooze and focus control; return the resulting state to connected clients |
| FR-11 | Must | Generate source-grounded briefing text with a bounded timeout and deterministic fallback; failed generation does not stop reminder delivery |
| FR-12 | Should | Allow optional notification sound and character preferences to be configured through the applications |
| FR-13 | Must | Display synchronization freshness and actionable connection errors; stale records are not described as live |
| FR-14 | Should | Permit manual synchronization without duplicate source items |
| FR-15 | Must | Publish a versioned external-client contract and validate supported message types; unsupported versions return a compatibility error |
| FR-16 | Must | Validate device actions by owner, action ID and state revision; retries have one accepted effect and reconnect restores current state |

### 6.2 Nonfunctional requirements

| ID | Priority | Requirement and proposed acceptance condition |
| --- | --- | --- |
| NFR-01 | Must | No connector tokens in Git, logs or client responses; encrypt stored tokens with separately managed key material |
| NFR-02 | Must | Repeated imports and repeated action IDs do not create duplicate records or effects |
| NFR-03 | Must | Explicit time semantics cover UTC/local conversion, all-day events, date-only tasks, recurrence exceptions and midnight boundaries |
| NFR-04 | Must | Network recovery restores current state and follows a documented policy for missed/expired reminders |
| NFR-05 | Should | Proposed p95 ordinary backend response below 500 ms under a documented test workload, excluding external/provider waits |
| NFR-06 | Should | Proposed healthy-connection server reminder dispatch within 5 seconds of its schedule; import freshness is measured separately |
| NFR-07 | Must | Model calls have a configured timeout, fallback and non-sensitive latency/usage diagnostics |
| NFR-08 | Must | Connector additions do not require changing focus-timer or client domain logic |
| NFR-09 | Must | Trace imports, reminders and actions using correlation identifiers; verify key failure paths |

Performance targets apply to a documented workload on the deployment server. The initial integrations read source information; acknowledging an ASTI reminder does not change the corresponding Notion task.
