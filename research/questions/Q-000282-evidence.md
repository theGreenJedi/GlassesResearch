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

Answer: `docs/faq/09-development-openness.md#does-mentra-live-keep-speaker-audio-playing-while-its-camera-streams-over-whip`; directory: `docs/faq/README.md`. The two original Q IDs resolve to one canonical FAQ anchor and must not be counted as two distinct published URLs. Upstream concurrent audio remains **unconfirmed**, with no GlassesResearch iOS/WHIP bench test. **Status: published after exact public production-content verification.**

## Publication verification — 2026-10-29

[Publication PR #714](https://github.com/theGreenJedi/GlassesResearch/pull/714) merged as `0b33532fcb46fd2a68107252d7830c58f40f5c26` after editorial, strict internal link/fragment and CI checks passed. [Main Pages deploy #40950125377](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40950125377) succeeded. [Exact production-content proof #40950500791](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40950500791) succeeded on 2026-10-29 at 20:37:39 UTC: the changed FAQ topic (digest `f2a451c6a102`), Practical Answers directory (digest `2c40c339be34`), and this evidence packet (digest `8abda89f1dbb`) were retrieved from the public site and matched the deployed build. [Canonical answer](https://glassesresearch.org/docs/faq/09-development-openness/#does-mentra-live-keep-speaker-audio-playing-while-its-camera-streams-over-whip). This verifies **publication**, not a device bench test; the upstream Mentra simultaneous-playback uncertainty remains explicit.
