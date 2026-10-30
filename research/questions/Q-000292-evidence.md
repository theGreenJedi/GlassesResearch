---
description: Claim-level evidence and publication limits for observed Q-000292.
---

# Q-000292 — Can overseas Rokid Glasses developers obtain a data cable or use wireless ADB?

**Original observed question:** Is there an official data/debug cable for Rokid Glasses that overseas developers can buy, or a way to enable ADB over Wi-Fi?

**Original observation:** [Source](https://github.com/yodaos-project/AIUI/issues/89) (observed 2026-10-29; reviewed October 30, 2026). The original observation remains in the canonical registry; the question is not independent device verification.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Official Rokid product lists developer cable for ADB | [Source](https://global.rokid.com/products/rokid-glasses-prototype) | Store option; shipping and exact device compatibility unverified |
| Stock cable did not enumerate and ADB TCP refused in owner report | [Source](https://github.com/yodaos-project/AIUI/issues/89) | Device-specific evidence only |
| Community project describes data-cable ADB steps | [Source](https://github.com/sses79/rokid-glasses) | Not official universal wireless-debugging support |

## Uncertainty and publication gate

Proposed answer: docs/faq/09-development-openness.md#can-overseas-rokid-glasses-developers-obtain-a-data-cable-or-use-wireless-adb. Single directory: docs/faq/README.md. Sources are attributed manufacturer, project or community reports, with their limits stated. No GlassesResearch hardware bench test, permanent retailer inventory survey or universal compatibility guarantee is claimed. **Status: published after exact production proof.** Keep the original registry Q ID observed until the publication PR passes checks, merges, the existing main Pages deployment succeeds and production-content-proof fetches exact public FAQ, directory and evidence pages. Then reconcile the original registry row with canonical answer_url, publication_verified_at and proof in a separate PR.

## Publication verification — 2026-10-30

[Publication PR #722](https://github.com/theGreenJedi/GlassesResearch/pull/722) merged as 477cdd2e4860a8bd275214a710adf06715a2d3c3 after editorial, strict built-page links/fragments and all CI checks passed. [Main Pages deploy #41123139911](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41123139911) succeeded. [Exact production-content-proof #41123622208](https://github.com/theGreenJedi/GlassesResearch/actions/runs/41123622208) succeeded at 2026-10-30T20:30:30Z, fetching the live FAQ (digest 7ac892f5def2), single Practical Answers directory (digest 51baf576859e), and this evidence page (digest 34e6b0a8f94a), all matching the deployed build. The [canonical published answer](https://glassesresearch.org/docs/faq/09-development-openness/#can-overseas-rokid-glasses-developers-obtain-a-data-cable-or-use-wireless-adb) has a verified directory fragment. Publication proof does **not** establish independent device or retail testing. Original registry observations remain intact; Q-000292 is credited only after this proof.
