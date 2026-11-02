---
description: Claim-level evidence and publication limits for original observed Q-000333.
---

# Q-000333 — Which smart glasses allow third party apps today?

**Original observed question:** which smart glasses are actually open for third party apps right now?

**Original observation:** [Original observed discussion](https://www.reddit.com/r/SmartGlasses/comments/1xlrmsx/which_smart_glasses_are_actually_open_for_third/) Reddit community question observed 2026-11-02; a request for currently usable third-party development, not a claim about a specific device. The registry's original observations and metrics must remain unchanged.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Even G2 has live plugin development with simulator, QR sideload and submission workflow | [Primary source](https://hub.evenrealities.com/docs/reference/app-submission) | Other promised Even app surfaces not treated as shipping |
| MentraOS lists supported devices and a miniapp developer SDK | [Primary source](https://mentraglass.com/os) | Support applies only to named devices and current app versions |
| Vuzix Z100 Android SDK sends text, notifications and images from a phone | [Primary source](https://support.vuzix.com/docs/sdk-for-android) | Phone companion path, not arbitrary native Z100 apps |
| Meta Wearables Toolkit and Display Web Apps are available for development; discovery has gates | [Primary source](https://developers.meta.com/wearables/faq/) | Device, region, permissions and public submission restrictions apply |
| Brilliant SDK provides open-source host libraries for Halo and Frame | [Primary source](https://github.com/brilliantlabsAR/brilliant_sdk) | SDK availability does not prove unrestricted firmware or cloud control |

## Uncertainty and publication gate

Canonical proposed FAQ: `docs/faq/09-development-openness.md#which-smart-glasses-allow-third-party-apps-today`. Existing single directory: `docs/faq/README.md`. Reviewed **2026-11-02**. Manufacturer, software-project and professional guidance is attributed, not treated as independent GlassesResearch hardware testing. No invented owner experience, universal compatibility, safety certification, product ranking or shipping forecast. The observed question is evidence of reader interest, not proof of its premise.

**State: publication verified.** Do not credit the original registry ID until editorial, built-page links/fragments and all CI checks pass; the publication PR merges; the existing main Pages deployment succeeds; and production-content-proof fetches the exact changed FAQ, directory and evidence pages. Then reconcile the original registry row with the canonical answer URL, `publication_verified_at` and claim-specific proof in a separate checked PR. Count unique URLs, not rows.

## Publication verification — November 2, 2026

[Publication PR #736](https://github.com/theGreenJedi/GlassesResearch/pull/736) merged as `90bc15d8d67d3a3cdfc52c16491db250a0d8d652` after editorial, strict built-site links/fragments and all PR CI checks passed. [Main Pages deployment #41532204654](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41532204654) succeeded. [Exact production-content-proof #41532749214](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41532749214) succeeded 2026-11-02T21:56:53Z, fetching the live FAQ (digest `b1514d92c57b`), the single Practical Answers directory (digest `bacf8cba1f5b`) and this evidence page (digest `42a3256e7f2e`) with exact deployed-build matches. [Canonical answer](https://glassesresearch.org/docs/faq/09-development-openness/#which-smart-glasses-allow-third-party-apps-today) has a validated directory fragment. This is one new distinct canonical answer URL. The original observed registry ID is now answered; publication proof does **not** independently establish hardware performance, user outcomes, or safety.
