---
description: Claim-level evidence and publication limits for original observed Q-000342.
---

# Q-000342 — Should smart glasses work with the apps we already use?

**Original observed question:** Should smart glasses work with the apps we already use?

**Original observation:** [Community discussion](https://www.reddit.com/r/SmartGlasses/comments/1xmtrr7/should_smart_glasses_work_with_the_apps_we/) observed 2026-11-03 via reddit_rss. This is a question about expectations, not evidence that every glasses model can use every app. Preserve the original registry observation.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Most existing Android apps run as 2D panels on Android XR headsets and wired XR glasses | [Google Android XR developer documentation](https://developer.android.com/develop/xr) | Not a blanket guarantee for audio/display AI glasses, nor for every APK |
| Vuzix Z100 has a host Android SDK for sending display content | [Vuzix Z100 SDK](https://support.vuzix.com/docs/sdk-for-android) | Phone-driven content is not APK installation on the glasses |
| App compatibility must be evaluated by feature, connection and platform | Inference from distinct documented architecture paths above | Practical evaluation recommendation, not measured product compatibility |

## Uncertainty and publication gate

Proposed canonical answer: `/docs/faq/09-development-openness/#should-smart-glasses-work-with-the-apps-we-already-use`. Existing evergreen directory `docs/faq/README.md` stays unchanged. Reviewed **2026-11-04**. No device test, blanket app compatibility, subscription claim or proprietary API capability is asserted. Publication requires all editorial, link/fragment and CI checks, main Pages deployment, and exact production-content-proof before registry credit and a separate evidence reconciliation PR. Count distinct URLs, not rows.
