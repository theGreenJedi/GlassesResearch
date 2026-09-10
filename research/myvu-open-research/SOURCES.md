# Sources and Attribution

This ledger preserves provenance. Inclusion means the source is relevant; it does **not** mean GlassesResearch independently verified every claim.

**Research snapshot date:** 2026-09-10

## Primary public technical upstreams

### Panny777 — Meizu-Myvu-Client
https://github.com/Panny777/Meizu-Myvu-Client

Pinned research snapshot: `2a7b4ba975b409cab2acc3d8eba4f1af8e981d79` (2026-07-21, "Bump to 0.3 for release")  
Pinned commit: https://github.com/Panny777/Meizu-Myvu-Client/commit/2a7b4ba975b409cab2acc3d8eba4f1af8e981d79

Role: reverse-engineered, hardware-verified MYVU / Star Air XGA010C client; Android and Python implementations; documents practical connection and feature behavior.

License note: upstream states MIT applies to its original code. Meizu proprietary/decompiled source is not distributed there and is not incorporated here.

### Panny777 — Meizu-Myvu-SDK
https://github.com/Panny777/Meizu-Myvu-SDK

Pinned research snapshot: `81a2d3243e2c6edfbddfd22932706ebdf2a9d02a` (2026-07-21)  
Pinned commit: https://github.com/Panny777/Meizu-Myvu-SDK/commit/81a2d3243e2c6edfbddfd22932706ebdf2a9d02a  
Pinned protocol reference: https://github.com/Panny777/Meizu-Myvu-SDK/blob/81a2d3243e2c6edfbddfd22932706ebdf2a9d02a/PROTOCOL.md

Role: structured Android SDK plus detailed wire-protocol reference derived from packet captures and official-app study. Particularly important for BLE/ECDH, ability auth, RFCOMM relay, heartbeat, initialization, weather, microphone/AI, and model-generation distinctions.

### FerSaiyan — Alternative-HeyCyan-App-and-SDK / CyanBridge
https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK

Pinned research snapshot: `f3a7d1c2825b5dd7fff52985d98d0388074326a2` (2026-08-27)  
Pinned commit: https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/commit/f3a7d1c2825b5dd7fff52985d98d0388074326a2

Role: broader glasses integration project. Its README explicitly credits Panny777's MYVU work and states that Panny777's BLE, ECDH, RFCOMM relay, heartbeat and display transport are used by its native MYVU integration. It also contains independent protocol research for adjacent hardware families.

Important interpretation: CyanBridge's reuse of Panny777's MYVU transport is downstream adoption, not independent confirmation of each protocol detail. CyanBridge's own README also distinguishes active hardware paths from experimental/device-dependent ones; GlassesResearch preserves that distinction.

## Primary community threads

### Panny777 reverse-engineering announcement
https://www.reddit.com/r/augmentedreality/comments/1uy1qoe/i_reverseengineered_meizus_myvu_ar_glasses_and/  
Published: 2026-07-16.  
Use: origin/context for the public reverse-engineering work and hardware-tested feature claims.

### Panny777 open-source Android/client follow-up
https://www.reddit.com/r/augmentedreality/comments/1v1zcph/update_i_opensourced_my_meuizu_myvu_ar_glasses/  
Published: 2026-07-20.  
Use: principal community thread for model-compatibility reports and owner observations recorded in `FAILURE-MODES.md`.

### MYVU regional/app compatibility discussion
https://www.reddit.com/r/SmartGlasses/comments/1it0ptk/myvu_smart_glasses/  
Published: 2025-02-19; later comments through at least 2026-09-04.  
Use: community reports about China/global app behavior, phone-number/account requirements, Android/iOS differences and regional pairing friction.

All community sources above were re-checked on 2026-09-10. Reddit observations remain `COMMUNITY-REPORTED` unless separately reproduced by GlassesResearch.

## Attribution rule

Every material technical statement added to this research area should retain enough information to answer:

1. Who observed or documented it?
2. On what identified hardware/firmware?
3. Was it source documentation, community observation, GlassesResearch reproduction, or inference?
4. Where is the original public evidence?
5. What source version/commit was examined?
6. Has a later source contradicted or refined it?

When GlassesResearch reproduces an upstream finding, both facts should remain visible: **who discovered/documented it upstream and that GR independently reproduced it.**

## Community evidence rule

Reddit and owner reports are attributed leads and field observations, not specifications. A formal community record should capture, where available: direct thread/comment permalink, public username only when technically relevant, post/comment date, retrieval date, normalized claim, hardware identity, software/host context, and verification state. If an exact timestamp or identity is unavailable from the captured source, mark it unavailable rather than estimating it.

## Living-source rule

`main` branches move. Technical claims should therefore cite a commit/tag when practical. A later upstream revision does not silently rewrite the evidence base: update the pinned snapshot, record what changed, and reassess affected GR conclusions.

## Future source intake

Add additional repositories, forks, issues, PRs, packet captures, teardowns, firmware analyses and owner tests only when they materially improve hardware identity, protocol understanding, interoperability, sourcing, failure analysis or reproducibility.