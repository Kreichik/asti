# Physical client software

The software boundary covers pairing, display state, rotary-step/click actions, acknowledgments, reconnection and revocation. Microphone and camera are not required.

Messages will include action IDs and state revisions. Reconnect retrieves a current snapshot; the display distinguishes cached information from fresh synchronization. Transport choice needs a real-hardware check. Circuit and enclosure work are outside the main software scope. Firmware code will follow the protocol definition.
