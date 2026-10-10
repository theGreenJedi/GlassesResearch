---
description: "Across the Wire: community technical findings on Mentra Live Bluetooth photo transfer, dark-scene camera timing, and Even Realities G1 character support."
---

# Community engineering: Mentra photo transfer, low-light timing, and G1 text support

**Across the Wire · Community-reported · October 10, 2026**

These are public project-maintainer and contributor findings, **not independently verified by GlassesResearch**. Reported tests are attributed to the upstream project; a merged PR is not proof of broad device rollout or independent performance.

## Mentra Live: Bluetooth photo transfer disrupted by audio startup

[MentraOS PR #4574](https://github.com/Mentra-Community/MentraOS/pull/4574) documents a photo-transfer failure when A2DP audio begins during a BLE file transfer. The project's diagnosis points to MTK-to-BES UART receive-buffer synchronization, not simply a phone-app failure. Its proposed/released BES firmware 26.10.8.0 uses hardware UART write-position tracking; the application change adds a 35 KB/s pacing fallback for older firmware.

The contributor reports 6 of 8 transfers failing without pacing versus 8 of 8 succeeding at 35 KB/s, and 7 of 7 succeeding with the 26.10.8.0 firmware in a specific hardware trial. These are small, project-reported samples, not general reliability rates. iPhone A2DP-start validation remained an explicit follow-up in the PR description.

**GR investigation:** Distinguish firmware, interprocessor UART, BLE transport and application-level errors when testing camera transfer; record exact firmware and audio-start timing.

## Mentra Live: dark-scene camera latency depends on warm versus cold start

[MentraOS PR #4599](https://github.com/Mentra-Community/MentraOS/pull/4599) proposes treating Android's `FLASH_REQUIRED` auto-exposure state as settled in a constrained **already-running-camera** path. Project tests report shutter-to-file time falling from 3.19 s to 1.39 s without measured noise deterioration in that test. Earlier capture after a **cold** camera start produced substantially noisier photos; the proposal preserves the cold-start wait.

**GR investigation:** Measure low-light capture latency and image quality separately for warm-camera reuse and cold starts. **Do not treat a proposed PR as released behavior.**

## Even Realities G1: firmware contains accented Latin glyphs

[MentraOS PR #4578](https://github.com/Mentra-Community/MentraOS/pull/4578) describes extraction of a character table from stock G1 firmware 1.5.6: 445 embedded records, 413 unique code points, including 124 extended Latin glyphs. The change preserves supported accented characters instead of stripping them in host formatting. Its contributor reports passing host and platform tests, but **physical G1 projection verification was still pending** in the PR evidence.

**GR investigation:** Test accented and decomposed Latin text on physical G1 hardware, across Android and iOS, before making display-support claims.

## Evidence boundary and provenance

All three items are attributed to their original GitHub pull requests. Project-reported hardware trials and software tests are evidence of work performed by contributors, **not GlassesResearch bench verification**. PR merge state, firmware availability, and device rollout must be checked separately; no Report Card score or Verified designation changes on this evidence alone.

## Primary sources

- [MentraOS #4574 — BES firmware and BLE file pacing](https://github.com/Mentra-Community/MentraOS/pull/4574)
- [MentraOS #4599 — dark-photo auto-exposure timing](https://github.com/Mentra-Community/MentraOS/pull/4599)
- [MentraOS #4578 — G1 Latin-character preservation](https://github.com/Mentra-Community/MentraOS/pull/4578)
