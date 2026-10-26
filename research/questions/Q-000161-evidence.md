---
description: Evidence review of eight-hour AI-glasses battery claims, required workload disclosures, charging case distinctions, and measurement limitations.
---

# Q-000161 — What an eight-hour AI-glasses battery claim must disclose

**Original observed question:** [What should an "8-hour battery life" claim on AI glasses include?](https://www.reddit.com/r/SmartGlasses/comments/1x1be39/what_should_an_8hour_battery_life_claim_on_ai/), retained as Q-000161. **Reviewed:** 2026-10-26. Reddit thread content was inaccessible in this pass; original question text comes from the pre-existing registry.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Meta advertised up to eight hours for Ray-Ban Meta Gen 2 with "typical use" | [Meta Gen 2 launch announcement](https://about.fb.com/news/2025/09/ray-ban-meta-gen-2-better-battery-life-video-capture/) | Manufacturer marketing, not independently measured endurance |
| Charging case provides additional 48 hours as a separate capacity claim | [Same Meta announcement](https://about.fb.com/news/2025/09/ray-ban-meta-gen-2-better-battery-life-video-capture/) | Case replenishment is not uninterrupted on-face runtime |
| GlassesResearch already distinguishes standby, audio, video, mixed use and external power | [Existing battery FAQ](../../docs/faq/04-battery.md) | Editorial measurement framework, not manufacturer laboratory protocol |
| Repeatable battery reports should disclose workload, starting/ending charge, brightness, radios, AI/camera activity, firmware, phone, temperature and interruptions | [Existing GlassesResearch battery-method FAQ](../../docs/faq/04-battery.md) | Proposed transparent test/reporting method; not an externally standardized requirement |

## Verification and publication gate

No independent 8-hour test was performed; no single standardized test regime is claimed to be legally required. The answer is a reproducibility checklist and distinguishes manufacturer "up to" claims from real-world measured endurance. **State: published after exact live FAQ and directory proof.** Proposed anchor: `docs/faq/04-battery.md#what-should-an-eight-hour-ai-glasses-battery-claim-disclose`.

## Publication proof — 2026-10-26

[PR #698](https://github.com/theGreenJedi/GlassesResearch/pull/698) merged as revision `2262054aaa16529f36e768925535be576f9a17b6` after documentation, editorial, link/fragment, deploy and Lighthouse checks passed. [Production content proof #40396645760](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40396645760) succeeded: fetched the complete public FAQ `/docs/faq/04-battery/` (digest `562b4d5f066e`), Practical Answers directory `/docs/faq/` (digest `3f42fb3fe4bc`), and this evidence page (digest `5b629fc84fea`) matching the deployed build. The directory links to the exact built-page anchor [published answer](https://glassesresearch.org/docs/faq/04-battery/#what-should-an-eight-hour-ai-glasses-battery-claim-disclose), validated by strict internal fragment checks. This proves content publication, **not** a device or SDK bench test. Registry Q-000161 was credited only after this proof; original observations and uncertainty remain intact.
