# External device connection interface

This component defines the server-side API used by compatible physical clients. It covers account association, connection authorization, state delivery, supported assistant commands, action identifiers, reconnection and revocation.

Devices are external to the platform. Their hardware, firmware, controls and screen layouts are implemented separately. Clients must follow the documented API contract; support is not tied to a particular board or enclosure.
