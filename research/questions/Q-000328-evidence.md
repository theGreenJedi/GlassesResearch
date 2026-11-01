---
description: Claim-level evidence and publication limits for original observed Q-000328.
---

# Q-000328 — Can smart glasses translate WhatsApp voice calls live?

**Original observed question:** Has anyone managed to get live translation working during WhatsApp calls?

**Original observation:** [Source](https://www.reddit.com/r/SmartGlasses/comments/1xkobye/has_anyone_managed_to_get_live_translation/) (preserved unchanged in canonical registry; reviewed November 1, 2026). The observation itself is not device verification.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| WhatsApp official translation announcement covers text messages in chats and Channels | [Primary/source](https://about.fb.com/news/2025/09/introducing-message-translations-whatsapp/) | Does not establish live voice-call translation |
| Android playback capture is constrained by audio usage and app policy | [Primary/source](https://developer.android.com/media/platform/av-capture) | General platform documentation, not a WhatsApp-specific audio route test |
| MemoMind release notes advertise call captions | [Primary/source](https://www.memo-mind.com/blogs/news/memomind-one-september-update) | Call captions do not establish WhatsApp translation |

## Uncertainty and publication gate

Canonical proposed FAQ: `docs/faq/06-ai-cameras-audio.md#can-smart-glasses-translate-whatsapp-voice-calls-live`. Existing single directory: `docs/faq/README.md`. The answer distinguishes manufacturer/platform statements from community reports, inference and unknowns. **No independent GlassesResearch device, application or compatibility test is claimed.** Links are preserved to primary/support resources rather than reproducing copyrighted documents or inventing an archive.

**State: awaiting publication proof.** Do not credit this original registry ID until this publication PR passes editorial, strict built-page links/fragments and all CI checks, merges, the existing main Pages deployment succeeds, and the production-content-proof workflow fetches the exact changed FAQ, directory and evidence pages. Reconcile the original registry row in a follow-up PR with canonical answer_url, publication_verified_at and claim-specific proof. Related Q IDs must not inflate distinct URL counts.

## Publication verification — 2026-11-01

[Publication PR #733](https://github.com/theGreenJedi/GlassesResearch/pull/733) merged as `7bca76c7aed93f84eb69100a22cd8b3f0c4cdb00` after editorial, strict links/fragments and all PR checks passed. [Main Pages deploy #41351137343](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41351137343) succeeded. [Exact production-content-proof #41351341361](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41351341361) succeeded 2026-11-01T21:19:48Z, fetching the live FAQ (digest `5e8cd2d6edc1`), single Practical Answers directory (digest `691ceffcb7b8`) and this evidence page (digest `f5bfcf2da93d`) with exact deployed-build matches. [Canonical answer](https://glassesresearch.org/docs/faq/06-ai-cameras-audio/#can-smart-glasses-translate-whatsapp-voice-calls-live) has a validated directory fragment. This adds one distinct canonical answer URL. Publication proof does **not** independently verify device hardware, application compatibility, or performance. The original observed registry ID is now answered.
