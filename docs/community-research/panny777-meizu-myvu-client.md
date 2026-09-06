# Panny777 / Meizu-Myvu-Client

**Community Research project**  
**Primary hardware:** Meizu MYVU / Star Air (`XGA010C`)  
**Project:** [Panny777/Meizu-Myvu-Client](https://github.com/Panny777/Meizu-Myvu-Client)  
**Evidence lane:** Community-primary technical research; not yet independently reproduced by GlassesResearch

## What the project does

Panny777 publishes an unofficial, community-built client for the Meizu MYVU / Star Air XGA010C. The repository documents a reverse-engineered Bluetooth path that can pair with the glasses and drive supported on-lens functions without the official companion application.

The project reports working support for notifications, teleprompter output, navigation, trackpad control, system settings, clock synchronization, selected status queries, and a voice-assistant path using the glasses microphone. It includes both an Android client and an earlier Python reference implementation.

## Why it matters

This is a concrete example of protocol reverse engineering becoming owner-usable interoperability. Rather than merely documenting packet formats, the project turns recovered behavior into a replacement client that can exercise real device functions.

Its published protocol work also has downstream value. CyanBridge explicitly credits this repository and states that Panny777's hardware-verified MYVU BLE, ECDH, RFCOMM relay, heartbeat, and display-transport work is used by CyanBridge's native MYVU integration.

## Evidence boundary

The repository describes the project as hardware-verified against one pair of glasses. GlassesResearch has not yet independently reproduced these behaviors on its own XGA010C specimen. Until that happens, the findings remain attributed community evidence and do not become GlassesResearch laboratory findings or automatic Report Card scores.

## Related GlassesResearch material

- [MYVU / StarV lineage research](/models/PROFILES_2026_09_03_MYVU_STARV/)
- [GLS-0167 — MYVU Air / StarV Air](/models/catalog/gls-0167/)
- [Community investigation note](https://github.com/theGreenJedi/GlassesResearch/blob/main/research/investigations/COMMUNITY_MYVU_XGA010C_PANNY777_2026-09-06.md)
- [Related editorial: When owners take their glasses back](../news/articles/2026-09-06-when-owners-take-their-glasses-back.md)
