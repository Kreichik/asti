# Verification plan

Automated tests will accompany executable components. This milestone contains acceptance criteria and planned checks, not executed application tests.

| Area | Checks | Requirements |
| --- | --- | --- |
| Device contract | Protocol versions, display/input capabilities, repeated action IDs, stale revisions and real-device reconnect | FR-09, FR-10, FR-15, FR-16 |
| Access | Account isolation, unauthorized actions, revocation | FR-01, FR-09, NFR-01 |
| Sources | Authorized source records, update/delete, pagination, missing dates, repeated imports | FR-02-FR-04, FR-14, NFR-02-NFR-03 |
| Overview | Inactivity threshold, one overview per session, empty/stale/error states | FR-05, FR-13 |
| Reminders | Source time, lead time, snooze, acknowledgment, retry deduplication | FR-06, NFR-02-NFR-04, NFR-06 |
| Focus and clients | Start/pause/resume/stop, shared timestamps, reconnect | FR-07-FR-10, NFR-04 |
| Briefings | Source references, date correctness, timeout, fallback | FR-11, NFR-07 |

Separate import freshness, scheduler delay, delivery and rendering when measuring behavior. Record environment and workload. Participant walkthroughs compare existing tools and ASTI; interview accounts and measured observations remain distinct. See [report section 9](../docs/report.md#9-verification-and-evaluation-plan).
