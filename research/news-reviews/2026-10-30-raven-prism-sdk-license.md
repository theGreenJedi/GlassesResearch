# Raven Prism: public preorder, source-available SDK, and community app evidence — October 30, 2026

<!-- news_promotion_schema: 1 -->

**Survey date:** 2026-10-30  
**Event window:** 2026-09-09 to 2026-10-30  
**Discovery routes:** Manufacturer and component-supplier press releases; manufacturer GitHub README, LICENSE and commit history; independent developer GitHub and public Reddit discussion; actual public GlassesResearch Across the Wire JSON feed.  
**Reviewer:** GlassesResearch community scour

## Decision and routing

- **Scope:** `core_glasses`, Raven Prism / RavenOS.
- **Disposition:** `publish` to the existing Open Development Resource Ledger and Community & Development directory; `review` for the October 29 attributed preorder news already represented by a third-party Raven Prism item in the live Across the Wire feed.
- **Wire:** On October 30, the live `https://glassesresearch.org/data/wire-feed.json` was directly inspected. It contained a Notebookcheck report titled **“Linux PC in a pair of glasses: New AR glasses work without a smartphone”** (Raven Resonance). That establishes existing attributed Raven discovery coverage, **not** GlassesResearch verification of the claims. Do **not** add a duplicate manually to generated wire JSON or claim that the manufacturer's release was published as a separate feed item.
- **Model/catalog:** No new model or Verified classification added. Earlier GlassesResearch competitor research already identified Raven as a watch; commercial preorder alone does not establish delivered hardware or hands-on verification.
- **Public state:** Repository changes are not considered published until the deployed public resource pages and the live feed are checked after merge/deploy.

## Primary source: October 29 manufacturer preorder

- Manufacturer release: https://www.prnewswire.com/news-releases/raven-resonance-announces-raven-prism-the-worlds-first-ambient-computer-is-officially-available-for-pre-orders-302923690.html
- Event date: **2026-10-29**; manufacturer says a **$49 fully refundable reservation deposit** and **expected January 2027 first shipments**. These are preorder/forecast claims, not fulfilled orders or shipping evidence.
- Manufacturer describes a standalone Linux-based 64-bit quad-core ARM computer, full-color LCoS waveguide, gaze and voice control, SSH access, a physical camera cover, activity lights and hot-swappable Raven Wings. Manufacturer privacy, uninterrupted operation and all-day wear assertions are **not** independently validated by GlassesResearch.
- Component partner: https://avegant.com/raven-prism-launch/ (dated 2026-10-29). Avegant confirms its participation and a 30-degree full-color display light engine. A partner's component confirmation does not verify every Raven system claim.

## Official developer source and a consequential license boundary

- Framework: https://github.com/RavenResonance/raven-framework
- License: https://github.com/RavenResonance/raven-framework/blob/main/LICENSE
- Exact October 30 license clarification: https://github.com/RavenResonance/raven-framework/commit/b0efac742ed0ec6c9e76e1c52868ebd39afd531f
- Starter: https://github.com/RavenResonance/raven-starter-project
- The manufacturer's current framework README identifies **alpha v1.0.7** and Python/PySide6 gaze-based UI/API, simulator, and deployment entry points. The manufacturer permits app authors to own their apps.
- **Crucial distinction:** the framework LICENSE expressly says **“source available, not open source.”** Unmodified installation and use to develop apps are permitted; modification, redistribution, sublicensing and derivative works of the framework require permission. RavenOS being Linux-based and supporting SSH/native ARM64 applications does not establish that RavenOS, the hardware, or the framework are freely modifiable or redistributable.
- Framework version 1.0.7's October 30 release/commit clarifies that licensing boundary and adjusts simulator fade-in rendering. Existence and terms of published source are directly verifiable; actual device API coverage and deployment behavior remain manufacturer-authored until reproduced.

## Community implementation: DOOMed Prism

- Code: https://github.com/RBraga01/DOOMed-Prism
- Public discussion: https://www.reddit.com/r/augmentedreality/comments/1wgyxow/doom_running_on_actual_raven_prism_smart_glasses/
- Developer documents Windows simulator tests, CI on ARM64, gaze/IPC controls and shared-memory compositor. The author attributes physical-hardware execution to Raven engineers, **not** to the author's own access to a Prism unit. The repo explicitly marks its own controlled on-device validation as outstanding, along with full on-glasses interaction and headless compositor behavior.
- Treat manufacturer demonstrations and a developer's simulator/CI tests as **distinct evidence lanes**, not two independent physical-device confirmations. Reddit discussion is useful provenance, not a hardware acceptance test.

## Editorial boundaries / next checks

- [x] Public manufacturer and component-partner sources preserved with dates and attribution.
- [x] Official framework, starter, exact license and commit linked; source-available vs open-source distinction explicit.
- [x] Independent project and public discussion linked with untested on-device behavior clearly marked.
- [x] Live Across the Wire JSON feed inspected; existing Raven discovery item found, so no duplicate manual wire entry.
- [x] Existing canonical development resource paths used; no new publishing category or plumbing.
- [ ] Await production hardware, third-party tests of display, battery continuity, privacy and SSH controls, and independently reproduced application deployment.
- [ ] After PR merge and deployment, check public canonical resource pages before asserting publication.
