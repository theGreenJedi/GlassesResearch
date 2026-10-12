# MentraOS community engineering: SDK telemetry and hotspot reliability

**Across the Wire · Community-reported · October 12, 2026 · Not independently verified by GlassesResearch**

Recent upstream MentraOS changes warrant owner-control and hardware reliability investigation. Merge status and behavior below are based on upstream reports, not independent GlassesResearch device testing.

## Bluetooth SDK telemetry

[MentraOS PR #4675](https://github.com/Mentra-Community/MentraOS/pull/4675) was reported merged October 12. It adds SDK telemetry around camera use, recordings, microphone sessions, connectivity, and device identifiers. Its developers say media content and location are excluded. GlassesResearch has not independently inspected actual transmitted payloads or verified whether owners can opt out.

**Investigation:** Identify data destinations, collection defaults, retention, disable controls, and actual payload contents. Do not conflate the developer's stated exclusions with independently verified privacy guarantees.

## Hotspot reliability

[MentraOS PR #4687](https://github.com/Mentra-Community/MentraOS/pull/4687) addresses glasses hotspots reportedly remaining active after failed media synchronization. [PR #4689](https://github.com/Mentra-Community/MentraOS/pull/4689) addresses an iOS hotspot connection failure during firmware updates. Both were reported merged October 12. Physical-device behavior, regression coverage, and release availability have not been independently confirmed.

**Investigation:** Reproduce failed media-sync and firmware-update paths on physical glasses and inspect hotspot shutdown/recovery.

## Evidence status

**Across the Wire / community-reported. Not GR Verified.** The cited pull requests are the source of these claims. A merged change does not establish that the fix shipped to consumers or resolves every affected device.
