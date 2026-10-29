---
description: Evidence and verification limits for Q-000282, does ios bluetooth speech remain audible while mentra live streams over whip?.
---

# Q-000282 — Does iOS Bluetooth speech remain audible while Mentra Live streams over WHIP?

**Original observed question:** the Bluetooth SDK on iOS, the camera streaming to the phone over WHIP, and speech played through the phone's normal audio APIs to Mentra Live as the Bluetooth media output: does the speech stay audible during the stream?

**Original observation:** https://github.com/Mentra-Community/MentraOS/issues/4967 (observed 2026-10-28; reviewed October 29, 2026). Preserve the original source and question rather than treating a proposed feature or community report as a measured result.

## Claim-level provenance

- **The issue describes a proposed iOS WHIP-plus-speech workflow; it contains no maintainer confirmation or bench measurements as of review.** Source: https://github.com/Mentra-Community/MentraOS/issues/4967
- **The documented iOS audio route is phone-originated playback over Bluetooth media, not a dedicated BLE playback command.** Source: https://github.com/Mentra-Community/MentraOS/blob/dev/mintlify-docs/bluetooth-sdk/audio.mdx
- **WHIP stream controls are documented separately; the simultaneous audio route is an open verification question.** Source: https://github.com/Mentra-Community/MentraOS/blob/dev/mintlify-docs/bluetooth-sdk/camera-streaming.mdx

## Verification and publication gate

Answer: `docs/faq/09-development-openness.md#does-mentra-live-keep-speaker-audio-playing-while-its-camera-streams-over-whip`; directory: `docs/faq/README.md`. The two original Q IDs resolve to one canonical FAQ anchor and must not be counted as two distinct published URLs. Upstream concurrent audio remains **unconfirmed**, with no GlassesResearch iOS/WHIP bench test. **Status: researched; registry credit withheld pending merged FAQ, directory, evidence, successful CI, and exact public production-content proof.**
