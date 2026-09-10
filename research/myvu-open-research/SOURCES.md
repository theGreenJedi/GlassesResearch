# Sources and Attribution

This ledger preserves provenance. Inclusion means the source is relevant; it does **not** mean GlassesResearch independently verified every claim.

## Primary public technical upstreams

### Panny777 — Meizu-Myvu-Client
https://github.com/Panny777/Meizu-Myvu-Client

Role: reverse-engineered, hardware-verified MYVU / Star Air XGA010C client; Android and Python implementations; documents practical connection and feature behavior.

License note: upstream states MIT applies to its original code. Meizu proprietary/decompiled source is not distributed there and is not incorporated here.

### Panny777 — Meizu-Myvu-SDK
https://github.com/Panny777/Meizu-Myvu-SDK

Protocol reference:
https://github.com/Panny777/Meizu-Myvu-SDK/blob/main/PROTOCOL.md

Role: structured Android SDK plus detailed wire-protocol reference derived from packet captures and official-app study. Particularly important for BLE/ECDH, ability auth, RFCOMM relay, heartbeat, initialization, weather, microphone/AI, and model-generation distinctions.

### FerSaiyan — Alternative-HeyCyan-App-and-SDK / CyanBridge
https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK

Role: broader glasses integration project. Its README explicitly credits Panny777's MYVU work and states that Panny777's BLE, ECDH, RFCOMM relay, heartbeat and display transport are used by its native MYVU integration. It also contains independent protocol research for adjacent hardware families.

## Attribution rule

Every material technical statement added to this research area should retain enough information to answer:

1. Who observed or documented it?
2. On what identified hardware/firmware?
3. Was it source documentation, community observation, GlassesResearch reproduction, or inference?
4. Where is the original public evidence?
5. Has a later source contradicted or refined it?

When GlassesResearch reproduces an upstream finding, both facts should remain visible: **who discovered/documented it upstream and that GR independently reproduced it.**

## Community evidence

Reddit and owner reports are maintained as attributed leads and field observations. They must not be silently converted into specifications. Direct thread URLs, usernames where technically relevant, dates, quoted/normalized claim, hardware identity, and verification status should be captured when an observation is promoted into a formal investigation record.

## Future source intake

Add additional repositories, forks, issues, PRs, packet captures, teardowns, firmware analyses and owner tests only when they materially improve hardware identity, protocol understanding, interoperability, sourcing, failure analysis or reproducibility.