# Alignment with the approved topic

Approved title: Development of an Intelligent System for a Physical Desktop Assistant with a Mobile Application and External Service Integration.

| Topic element | Software deliverable | Report coverage |
| --- | --- | --- |
| Physical desktop assistant | Device software boundary, ownership, versioned protocol, capabilities, display state, rotary actions and recovery | 1, 6 (FR-09, FR-10, FR-15, FR-16), 7, 8, 9 |
| Mobile application | Android onboarding, connection status, external authorization, settings and assistant controls | FR-08, 8.5 and onboarding wireframes |
| External service integration | Independent authorized Calendar/Notion adapters, provenance, freshness and errors | FR-02-FR-04, FR-13; 5, 7, 9 |
| Intelligent system | Source-grounded briefings with a replaceable model, bounded output and deterministic fallback | FR-11; 3, 5.4, 7.3, 9 |
| Software engineering contribution | Explicit contracts, modular architecture, consistent state, authorization, failure recovery and measured verification | 1.4, 5.5, 6, 7, 9 |

The web client is a user-requested additional interface. It does not replace the Android or physical-client deliverable. Circuit design and enclosure manufacture remain outside the main software scope. Voice, camera and training a model are not required.

The earlier related-system table compared data sources rather than physical-assistant software. It has been replaced by Home Assistant/Assist, OpenVoiceOS and Stack-chan against eight criteria, with official documentation and explicit uncertainty. A build-versus-extend decision is now included. Calendar, Notion, Notion Calendar and Trello appear as source/workflow context only.

Research now includes tangible and ambient interaction. Requirements, architecture, onboarding and evaluation explicitly cover the physical-device boundary. The evaluation compares real-device transport behavior and the same assistant flows across physical and screen clients, not only manual calendar checking.

Remaining evidence limits: the three existing interviews mainly establish service use; they do not validate demand for a physical assistant. Supervisor feedback on the deliverables remains pending. No implementation or completed evaluation is claimed.
