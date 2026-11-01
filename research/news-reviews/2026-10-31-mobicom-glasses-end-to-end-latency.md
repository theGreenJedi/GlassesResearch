# MobiCom 2026: measured glasses–phone–cloud bottlenecks — October 31, 2026

<!-- news_promotion_schema: 1 -->

**Discovery/review date:** 2026-10-31  
**Event date:** 2026-10-26–30, ACM MobiCom 2026, Austin; paper listed in the October 27 program  
**Scope:** `core_glasses` — Ray-Ban Meta G1, Meta Display, Even G1, Cyan and a custom ESP32-based Dragon prototype  
**Disposition:** `review` for attributed academic research through existing Across the Wire editorial intake; preserve reproducibility source in research. **Not** a GlassesResearch bench result, device score, or Verified claim.

## Primary evidence and independent event corroboration

- [Northeastern SINRG-Lab authors' code, measurement data and README](https://github.com/SINRG-Lab/mobicom-26-xr-ai-glass) — **researcher-primary**. README identifies Majd Khalaf, Mathew Garcia, Mayank Chadha and Mallesham Dasari and gives measured outcomes, platforms, applications, protocols, and notebook/CSV locations. Repository includes an MIT LICENSE, scripts and a Docker/container recipe.
- [ACM MobiCom 2026 official program](https://www.sigmobile.org/mobicom/2026/program.html) and [official accepted papers](https://www.sigmobile.org/mobicom/2026/accepted.html) — **independent conference-primary confirmation** that this specific paper was accepted and programmed; **not** independent reproduction of results.
- [Lead author's publication page](https://mkhalaf0.github.io/) and [SINRG publication listing](https://sinrg.org/publications/publications.html) — researcher/institution attribution. The repository claims all 14 analysis notebooks pass locally and in a container; **GlassesResearch has not executed them**.

## Findings, all attributed to the research team

- Live streaming from first-generation Ray-Ban Meta involves a phone decode–upscale–re-encode path; the authors report **2–3× latency versus phone-native streaming**, with phone transcoding rather than the glasses' short-range uplink as a principal bottleneck.
- The researchers describe asymmetrical video conferencing: incoming video downscaled for a small glasses display, upstream video relayed without equivalent transcoding.
- For Meta Live AI, they report roughly **300 kbps** video uplink as a bandwidth/fidelity tradeoff.
- The README reports **over one second end-to-end AI interaction latency** across its measured platforms/applications, compared against the authors' sub-300-ms interactive target; their measured voice-AI medians vary from roughly **1 second** (Ray-Ban Meta G1) to **over 10 seconds** (Cyan). These are *specific tested configurations*, not a claim about all smart glasses or all firmware versions.
- Researchers supply separate datasets/notebooks for streaming, conferencing, AI voice/image, power, and distance. Their reproduction claim is for figures from supplied data, not independent repeat capture on every device.

## Practical editorial value and uncertainty

The work exposes where latency actually accumulates across **glasses → phone → cloud**, useful for GlassesResearch's Flow Before Form/real-task evaluations. Do not reduce this to a generic 'Bluetooth is slow' claim or infer every device's battery life from the network measurements. Publication date is the conference window; source availability may precede the October 31 scour. Check hardware/firmware, network, test workload and author limitations before promoting precise figures into buyer advice. No GlassesResearch replication or independent remeasurement was performed.

## Wire and publication boundary

The live public [Across the Wire JSON feed](https://glassesresearch.org/data/wire-feed.json) was inspected October 31, 2026. Its existing current discovery entries are marked reported/under-review, not verified. No exact MobiCom study-title entry was identified in the inspected snapshot; this is **not evidence of a broken publisher**. Route the conference paper as an attributed, dated research candidate through the **existing** intake/editorial workflow; do not hand-edit generated feed JSON, invent a candidate ID, or claim public publication without a subsequent live check.

**Follow-up:** Validate the supplied notebook execution and configuration-specific data; compare with actual end-user latency protocols; after any editorial merge, inspect the deployed page/feed before claiming it is public.
