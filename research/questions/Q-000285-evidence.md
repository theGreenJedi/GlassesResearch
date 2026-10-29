---
description: Evidence and verification limits for Q-000285, which smart glasses support offline live translation?.
---

# Q-000285 — Which smart glasses support offline live translation?

**Original observed question:** What smart glasses have offline live translation?

**Original observation:** https://www.reddit.com/r/SmartGlasses/comments/1xgxt02/what_smart_glasses_have_offline_live_translation/ (observed 2026-10-28; reviewed October 29, 2026). Preserve the original source and question rather than treating a proposed feature or community report as a measured result.

## Claim-level provenance

- **Meta announced downloadable packs for back-and-forth translation among six languages including airplane-mode use, not proof of all later language pairs.** Source: https://about.fb.com/news/2025/09/ray-ban-meta-gen-2-better-battery-life-video-capture/
- **Even G2 Conversate explicitly requires a paired phone with internet before use, so its real-time translation cannot be labeled offline based on these docs.** Source: https://support.evenrealities.com/hc/en-us/articles/14273795154319-Conversate
- **A paired phone's offline capability is not evidence the computation runs on the glasses.** Source: https://www.reddit.com/r/SmartGlasses/comments/1xgxt02/what_smart_glasses_have_offline_live_translation/

## Verification and publication gate

Answer: `docs/faq/06-ai-cameras-audio.md#which-smart-glasses-can-translate-speech-offline`; directory: `docs/faq/README.md`. Manufacturer documentation is identified as such; no independent device bench verification is claimed. **Status: published after exact public production-content verification.**

## Publication verification — 2026-10-29

[Publication PR #714](https://github.com/theGreenJedi/GlassesResearch/pull/714) merged as `0b33532fcb46fd2a68107252d7830c58f40f5c26` after editorial, strict internal link/fragment and CI checks passed. [Main Pages deploy #40950125377](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40950125377) succeeded. [Exact production-content proof #40950500791](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40950500791) succeeded on 2026-10-29 at 20:37:39 UTC: the changed FAQ topic (digest `f422e3982064`), Practical Answers directory (digest `2c40c339be34`), and this evidence packet (digest `e19050fc26c7`) were retrieved from the public site and matched the deployed build. [Canonical answer](https://glassesresearch.org/docs/faq/06-ai-cameras-audio/#which-smart-glasses-can-translate-speech-offline). This verifies **publication**, not a device bench test; the offline language-pair and phone-versus-glasses processing limitations remain explicit.
