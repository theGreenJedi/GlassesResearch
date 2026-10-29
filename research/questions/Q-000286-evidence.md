---
description: Evidence and verification limits for Q-000286, troubleshooting even g2 microphone speech recognition.
---

# Q-000286 — Troubleshooting Even G2 microphone speech recognition

**Original observed question:** Even G2 Mic Issues - AI Can't Understand - Suggestions?

**Original observation:** https://www.reddit.com/r/SmartGlasses/comments/1xghpj8/even_g2_mic_issues_ai_cant_understand_suggestions/ (observed 2026-10-28; reviewed October 29, 2026). Preserve the original source and question rather than treating a proposed feature or community report as a measured result.

## Claim-level provenance

- **Even's official guide prescribes glasses/phone input comparison, five-tap dual-touchpad restart, app restart and logs; Even AI input cannot be switched.** Source: https://support.evenrealities.com/hc/en-us/articles/17206473148815-Voice-Features-Do-Not-Work-with-the-G2-Microphone
- **The maker recommends checking spoken language and quiet surroundings when recognition is inaccurate.** Source: https://support.evenrealities.com/hc/en-us/articles/17203734229775-Even-AI-Voice-Recognition-Is-Inaccurate
- **Premature Even AI error may require checking network; it does not alone establish microphone damage.** Source: https://support.evenrealities.com/hc/en-us/articles/17203580053519-Even-AI-Reports-an-Error-Before-You-Finish-Speaking

## Verification and publication gate

Answer: `docs/faq/06-ai-cameras-audio.md#how-do-i-troubleshoot-even-g2-microphone-speech-recognition-failures`; directory: `docs/faq/README.md`. Manufacturer documentation is identified as such; no independent device bench verification is claimed. **Status: published after exact public production-content verification.**

## Publication verification — 2026-10-29

[Publication PR #714](https://github.com/theGreenJedi/GlassesResearch/pull/714) merged as `0b33532fcb46fd2a68107252d7830c58f40f5c26` after editorial, strict internal link/fragment and CI checks passed. [Main Pages deploy #40950125377](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40950125377) succeeded. [Exact production-content proof #40950500791](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40950500791) succeeded on 2026-10-29 at 20:37:39 UTC: the changed FAQ topic (digest `f422e3982064`), Practical Answers directory (digest `2c40c339be34`), and this evidence packet (digest `249610d47f13`) were retrieved from the public site and matched the deployed build. [Canonical answer](https://glassesresearch.org/docs/faq/06-ai-cameras-audio/#how-do-i-troubleshoot-even-g2-microphone-speech-recognition-failures). This verifies **publication**, not a device bench test; the upstream Mentra simultaneous-playback uncertainty remains explicit.
