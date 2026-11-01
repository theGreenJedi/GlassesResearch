# Subvocal and Subvox: silent-speech glasses versus an AirPods experiment — October 31, 2026

<!-- news_promotion_schema: 1 -->

**Discovery date:** 2026-10-31  
**Event window:** October 30–31, 2026 public launch discussion and community open-source response  
**Scope:** `core_glasses` for Subvocal preorder; adjacent wearable-input developer research for Joe Blau's Subvox  
**Disposition:** `review` for existing Across the Wire attributed launch coverage; preserve developer resource and claim boundary. **No shipping, measured accuracy or equivalent-hardware claim.**

## Source provenance

- [The Subvocal Company's own preorder page](https://subvocal.company/preorder) — **manufacturer-primary**, checked October 31: **$199 refundable deposit**, **$499 total early-bird price** ($300 due later), US-only paid reservations, estimated **Q1 2027** shipment, subject to development, FCC approval and no guaranteed date. Optional prescription lenses, tax and shipping cost extra. The manufacturer says it does not need a camera and final specifications are still in development.
- [Y Combinator's Subvocal company job description](https://www.ycombinator.com/companies/the-subvocal-company/jobs/XEN2HGf-head-of-hardware) and [head-of-sensing description](https://www.ycombinator.com/companies/the-subvocal-company/jobs/yBCprPW-head-of-sensing) — **company-authored claims hosted by YC**. They claim prototypes decode continuous subvocal speech at **200+ words/min**, while explicitly stating that the exact current sensor architecture is **not publicly disclosed** and wearable generalization is unfinished. RF, EMG, EEG and mmWave are described as a *design space*, **not confirmed contents of the shipping product**.
- [Joe Blau's Subvox repository README](https://github.com/joeblau/subvox) and [MIT LICENSE](https://github.com/joeblau/subvox/blob/main/LICENSE) — **independent developer-primary code**, not independently validated by GlassesResearch. macOS 14+ application uses `CMHeadphoneMotionManager` to test AirPods head-motion features, dynamic-time-warping matching and a 500-permutation statistical evaluation for a *small trained vocabulary*. It has no language model.
- [October 31 secondary comparison](https://startupfortune.com/a-startup-raised-13-million-for-silent-speech-glasses-and-a-developer-built-the-free-version-in-nine-minutes/) — attributes a reported nine-minute implementation and social-media response to the developer. **Nine minutes is a developer anecdote, not an independently timed build or performance validation**.

## Essential non-equivalence

Subvocal claims continuous open-ended text from custom physiological sensing at speaking speed; it has not publicly demonstrated independently reproducible accuracy or a shipping device. Subvox tests whether ~25 Hz processed AirPods head motion, mostly jaw/head motion rather than exposed vocal vibration, distinguishes **a few user/session-specific trained words**. The repo warns about headset reseating and capture limitations. Its presence proves a public MIT-licensed experimental implementation, **not** a replication or disproof of Subvocal's claimed hardware capabilities. A comparison that says a free AirPods app 'recreated the same product' is misleading.

## Wire / verification boundary

The actual public [Across the Wire feed](https://glassesresearch.org/data/wire-feed.json) was inspected October 31. It already includes a **Subvocal-related India Today discovery item**, labelled *Under Review* and *unverified*, with publication timestamp 2026-10-31T12:32:11Z. This is already attributed discovery coverage, **not** a GlassesResearch confirmation of company claims. Do not add a duplicate manually, and do not assert Subvox appears in the feed merely because Subvocal does.

**Follow-up:** Track actual preorder fulfillment, full sensor disclosure, real-world word error rate, calibration burden, power, privacy, and availability; independently run Subvox with documented users and conditions before drawing performance comparisons. Do not change catalog Verified status.
