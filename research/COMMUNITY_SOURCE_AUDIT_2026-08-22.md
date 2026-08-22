# Community / developer source intake audit — 2026-08-22

This note records the disposition of a user-supplied batch of GitHub, Discord, Reddit, AMA, hands-on, retail-field-report, and industry links collected on 2026-08-22.

Inclusion in the supplied batch is a **discovery lead, not verification**. This audit separates project-primary material, regulatory evidence, team/self-report, independent hands-on observations, ordinary community discussion, and duplicate coverage. Community claims do not overwrite manufacturer, regulatory, code-visible, or reproduced evidence.

## Executive disposition

The batch produced four high-value outcomes:

1. **Nimbo X1** — a genuinely new product/research lead. Nimbo now exposes a direct preorder route and its team reports a funded Kickstarter. The product therefore appears to cross the repository's purchaser-history threshold. Canonical admission is warranted, but this intake PR does not hand-edit `THE_LIST.md` while the catalog-synchronization machinery is under concurrent work; the admission decision is preserved here and in `research/populated/NIMBO_X1.md` for deterministic follow-through.
2. **NIMO Holo-Optical Glasses** — distinct from Nimbo X1. NIMO currently sells a refundable $20 deposit reservation and explicitly says it is a reservation, not a product purchase. Keep as pre-release/discovery until the Kickstarter/product purchase route actually opens. MentraOS compatibility is useful development evidence, not purchaser-history evidence.
3. **AG05** — much stronger than a social-media pitch alone. FCC ID `2BWND-AG05` identifies Shenzhen NAMIOT Technology Co., Ltd. as the original-equipment applicant. The filed manual names the OneGlance app and documents the removable-battery architecture. Keep as an in-scope pre-release/OEM lead until a real acquisition route is verified.
4. **Wearable Intelligence System (WIS)** — historically important open smart-glasses software, not a model. Its README explicitly says WIS was reorganized/upgraded into SmartGlassesManager. Preserve WIS as an archived software lineage and treat SmartGlassesManager as the successor to investigate, rather than counting both as separate confirmations.

The Shenzhen retail-report links are also unusually valuable as **field intelligence**: they identify physical-retail presence, white-label frames, and possible OEM/rebrand leads in Huaqiangbei. They are discovery evidence, not manufacturing proof.

---

## 1. Open-development and software lineage

### Wearable Intelligence System — preserve as archived predecessor

Source:
- https://github.com/emexlabs/WearableIntelligenceSystem

The repository describes an open-source Android smart-glasses + smartphone framework with HUD apps, voice commands, live captions, translation, visual search, memory tools and developer support. Its README now begins with an explicit archival notice stating that WIS was reorganized and upgraded into SmartGlassesManager:

- https://github.com/TeamOpenSmartGlasses/SmartGlassesManager/

Disposition:
- classify WIS as **Historical / archived project-primary**;
- preserve its Vuzix Blade-era Android architecture and application ideas;
- treat SmartGlassesManager as the successor lineage, not as independent corroboration of WIS behavior;
- add this lineage to the open-project research surface.

### Discord invite

The supplied Discord invite is a community access point, not durable technical evidence.

Disposition:
- useful for discovery/community contact;
- do not cite Discord membership or ephemeral messages as technical proof without preserving a stable attributable artifact;
- do not promote the invite itself into model facts.

---

## 2. New model / platform leads

### Nimbo X1 — canonical admission warranted

Primary/project sources:
- https://nimbopearl.com/
- https://nimbopearl.com/campaign/
- https://www.kickstarter.com/projects/nimbopearl/nimbo-x1-worlds-lightest-sic-color-display-ar-glasses

Team AMA / technical source:
- https://www.reddit.com/r/augmentedreality/comments/1vtu6j9/ama_aug_20_5_pm_pdtnimbo_x1_49g_fullcolor_ar/

Independent hands-on lead:
- https://www.reddit.com/r/SmartGlasses/comments/1vobxkt/unboxing_nimbo_x1_07mm_sic_waveguide_30_fov_and_a/

Current Nimbo material presents X1 as a 49 g full-color SiC-waveguide AR product with an active preorder surface. The Nimbo team reports that the Kickstarter is funded and that production preparation is complete. Team/project claims include a 30° field of view, 32 MP camera, AOSP-based software, open SDK, low-level hardware access, raw sensor access, system-level signing access, an independent app center, and access to camera/IMU data for custom applications.

Evidence boundary:
- `49 g`, `SiC waveguide`, preorder state and public project existence are project-primary facts/claims tied to live surfaces;
- SDK openness, unrestricted APIs, raw-sensor access, system-level signing, background-app behavior, 32 MP camera construction, battery figures and optical performance remain **project/team claims until code, documentation, shipped hardware or independent testing reproduces them**;
- the Reddit AMA is unusually useful because the team answers specific developer and hardware questions, but it is still self-report;
- the independent unboxing is useful hands-on corroboration for physical existence/weight/optical impressions, not a substitute for reproducible measurements.

Disposition:
- **canonical admission warranted** under the paid preorder/crowdfunding acquisition rule;
- create/populate a Nimbo X1 research record now;
- queue report-card and comparison work after canonical ID synchronization;
- assign no openness score solely from marketing language; verify actual SDK/code/license and privilege boundaries first.

### NIMO Holo-Optical Glasses — pre-release, do not conflate with Nimbo

Primary reservation source:
- https://shop.nimoar.com/products/nimo

Mentra compatibility / community-development leads:
- https://www.reddit.com/r/augmentedreality/comments/1st5b0p/nimo_display_smart_glasses_support_open_dev/
- https://www.reddit.com/r/augmentedreality/comments/1vlml5f/mentraos_running_on_nimo_smart_glasses_making/

The NIMO shop currently offers a **$20 deposit reservation** and explicitly says the transaction is a reservation, not a product purchase; the page advertises future Kickstarter VIP pricing beginning at $399 and says the deposit can be cancelled for a full refund.

Disposition:
- keep **pre-release / registry-only** until Kickstarter backing or another real product purchase route opens;
- preserve the claimed 29 g / binocular-display / MentraOS compatibility leads for later verification;
- do not infer owner control from MentraOS compatibility alone;
- **NIMO and Nimbo are separate projects/brands and must never be merged by spelling similarity**.

### AG05 — NAMIOT regulatory identity established; public sale not yet established

Regulatory / durable sources:
- https://fccid.io/2BWND-AG05
- https://fccid.io/2BWND-AG05/User-Manual/Users-Manual-9485222
- https://fccid.io/2BWNDAG05/Internal-Photos/Internal-Photos-9485210

Team/community source:
- https://www.reddit.com/r/SmartGlasses/comments/1vv2ppn/we_got_tired_of_smart_glasses_dying_midday_so_our/

FCC records identify:
- equipment: `SMART AI GLASSES`;
- product code: `AG05`;
- applicant: **Shenzhen NAMIOT Technology Co., Ltd.**;
- application purpose: **Original Equipment**;
- application date: 2026-07-21.

The filed user manual documents a removable battery, camera, left/right speakers, microphones, touch/button controls, local photo/video/audio capture, Wi-Fi transfer, the `AG05` Bluetooth/device name, and the `OneGlance` companion app.

The Reddit poster says the team developed a swappable dual-battery design and describes in-house R&D/product design/electronic integration with specialized contract manufacturers for manufacturing/assembly. The poster also says the product is not yet officially on public ecommerce platforms.

Disposition:
- **in-scope pre-release/OEM lead; not canonical yet** because a real acquisition route has not been established;
- treat NAMIOT/FCC identity as high-confidence regulatory evidence;
- treat the poster's architecture/manufacturing statements as attributed team self-report until independently tied to NAMIOT or other corporate documentation;
- use FCC internal/external photos as future hardware-provenance/teardown evidence;
- investigate AG03 and other NAMIOT filings as a possible product/OEM lineage rather than assuming AG05 is a one-off.

### Opvek — project lead only

Supplied/community sources:
- https://www.reddit.com/r/SmartGlasses/comments/1vukrx3/opvek_more_than_just_glasses/
- https://opvek.vision

Related discoverable project posts describe Opvek as being built around open/transparent firmware/data-flow goals, privacy and eyewear design.

Disposition:
- retain as **early project/discovery lead**;
- no canonical model identity or acquisition route established in this audit;
- do not score openness from stated philosophy; require published code, firmware, API documentation or inspectable hardware/software artifacts.

---

## 3. Existing-model enrichment, not new catalog rows

### RayNeo iO / GT / GT Max

Supplied links include announcement, AMA, unboxing and 3DoF discussion. The repository already contains current RayNeo iO/GT-series news and RayNeo lineage research.

Disposition:
- deduplicate against `docs/news/articles/2026-08-21-rayneo-io-gt-series.md` and the RayNeo research record;
- use hands-on/AMA material only to add attributed observations or developer details that are not already supported by RayNeo primary sources;
- iO remains a launch/pre-release state until the announced September 4, 2026 sale route actually opens; do not create a duplicate product merely because multiple Reddit posts cover it.

### Xiaomi / Mijia smart glasses

The repository already contains Xiaomi/Mijia research, generation-comparison evidence, and an identity-boundary record for Mijia Glasses Camera.

Disposition:
- treat the supplied Xiaomi post as a recheck/enrichment lead;
- confirm whether it represents a new hardware generation, a regional relaunch, or an already-cataloged model before changing identity;
- do not add a new row from a title alone.

### Meta Ray-Ban Display retail-demo post

Meta Ray-Ban Display is already canonical and publicly sold through controlled demo/retail channels.

Disposition:
- the Best Buy demo post is availability/user-experience evidence only;
- no new model identity.

### Even Realities G2 discussion

G2 already has a canonical record and active community protocol research.

Disposition:
- use community discussion for question discovery and owner-experience leads;
- do not let recommendation threads overwrite primary specs or packet-level evidence.

### VITURE Pro 2 / RayNeo Air 2S XR / Google AR-spec discussion

These links are comparative/discovery discussions rather than new identity proof in this intake.

Disposition:
- route to existing model/research records when the comment contains a testable observation;
- speculation about unreleased Google hardware remains speculation until primary Google/Android XR material establishes a named product.

---

## 4. Shenzhen field intelligence and supply-chain leads

### Huaqiangbei / Shenzhen retail reports

Sources:
- https://www.reddit.com/r/SmartGlasses/comments/1vdl9w9/smart_glasses_retail_report_shenzhen_%F0%9D%97%A3%F0%9D%97%AE%F0%9D%97%BF%F0%9D%98%81_%F0%9D%9F%AE/
- https://www.reddit.com/r/SmartGlasses/comments/1vq3tlj/exploring_the_worlds_largest_electronics_market_a/

The author reports direct visits to Shenzhen/Huaqiangbei retail locations and names Qwen, RayNeo, XREAL, INMO, iFlytek, INAIR, Rokid, MLVision, Holoswim, Goolton, LLVISION, Lawaken, Superhexa, DreamSmart/StarV/MYVU/Meizu, BleeqUp and others. The report also identifies inexpensive transparent/white-label frames as products sold under names such as Rocklion (Youhe) and Jishan Jiapin, while explicitly stopping short of naming the actual factory.

Disposition:
- high-value **field-intelligence/discovery** source;
- feed named unknowns into manufacturer/OEM searches;
- physical presence can corroborate that a product exists in a retail channel, but it does not prove who designed/manufactured it;
- white-label visual similarity is a lead for shared-platform analysis, not proof of common ODM;
- use these posts to expand the Shenzhen supply-chain investigation without collapsing brand, reseller, solution house and factory roles.

Priority follow-ups from this source:
1. identify the actual OEM/ODM behind the transparent $59-class white-label frames;
2. investigate Rocklion / Youhe and Jishan Jiapin role boundaries;
3. investigate Lawaken's modular-front-frame and magnetic-camera architecture;
4. verify Superhexa ↔ Xiaomi/Mijia product relationships with primary sources;
5. audit underrepresented Chinese physical-retail brands against the canonical list.

---

## 5. Industry / component ecosystem

### TDK / OQmented

Supplied source:
- https://www.reddit.com/r/augmentedreality/comments/1vrvh56/tdk_acquires_assets_from_oqmented_to_advance_ar/

Disposition:
- important **component/supply-chain** lead, not a glasses-model lead;
- investigate with TDK/OQmented primary corporate material before publishing the acquisition terms or specific IP/assets as verified facts;
- if confirmed, link it into the optical-engine / MEMS scanning / AR-display supply-chain map rather than a consumer model page.

### SIVA Awards 2026

Disposition:
- discovery surface for companies/projects and technical categories;
- award entry or nomination is not product verification and does not establish commercial availability.

### Aggregated AR-news post

Disposition:
- lead generator only;
- split each claim into its underlying primary source before ingestion.

---

## 6. Community and hands-on source policy reinforced by this batch

The supplied Reddit corpus is useful precisely because not every link plays the same role.

### High-value community evidence
- identifiable team AMAs with specific technical answers;
- hands-on posts with physical units and reproducible observations;
- field reports from named locations with photographs;
- teardown/protocol/developer observations that can be compared with code or regulatory artifacts.

### Discovery-only material
- recommendation threads;
- speculative future-product questions;
- generic opinion posts;
- reposts of announcements without additional evidence;
- marketing posts where the poster's relationship to the product is unclear.

### Rule
A community source may tell GlassesResearch **where to investigate, what failed, what to test, or what a team claims**. It does not silently become primary specification truth.

---

## Closeout

This batch is not retained as an undifferentiated bookmark dump. Its durable outcomes are:

- Nimbo X1 promoted into populated research with canonical admission warranted;
- NIMO kept distinct and pre-release because its current $20 transaction is explicitly only a reservation;
- AG05 tied to Shenzhen NAMIOT through FCC original-equipment evidence and queued for OEM/teardown investigation;
- WIS preserved as an archived open-software predecessor to SmartGlassesManager;
- Shenzhen/Huaqiangbei posts promoted as field-intelligence inputs to the supply-chain investigation;
- existing RayNeo, Xiaomi/Mijia, Meta, Even Realities and display-glasses discussion deduplicated into enrichment rather than duplicate models;
- Opvek, TDK/OQmented and other project/component links assigned explicit follow-up lanes rather than being promoted beyond the evidence.
