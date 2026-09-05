# Rokid — populated research record

**Technology lineage:** [Rokid](../../lineages/ROKID.md)

Primary evidence includes the official terminal SDK (`EV-0024`), Rokid Glasses specifications (`EV-0025`), optical-service evidence (`EV-0038`), `docs/report-cards/BATCH_02.md`, display-lineage research from `HIGH_THROUGHPUT_BATCH_04.md`, [EV-0047](../../evidence/EV-0047-Rokid-Glasses-service-survival.md), [EV-0052](../../evidence/EV-0052-current-value-wave-one.md), and the [2026-09-05 historical audit](../investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md).

## Family boundary

Rokid spans several materially different branches: standalone enterprise AR (Glass 1/2/3), host-driven displays and spatial systems (Air/Max families), integrated display-AI eyewear (Rokid Glasses), display-free camera/audio AI eyewear (`RV203` / Style / Neo), and industrial head-worn AR (X-Craft). Do not transfer camera, onboard processing, AI, cloud-dependence, SDK, optics, or service-survival claims across those branches.

## Historical audit — 2026-09-05

The whole-lineage pass found three canonical smart-glasses omissions and one adjacent-wearable omission:

- **[Rokid Air Pro](../../models/RokidAirPro/README.md) — GLS-0182:** distinct 2021 camera-equipped Air sibling. Rokid's own developer material distinguishes Air Pro from Air by camera and optical-adjustment behavior.
- **[Rokid Max Pro](../../models/RokidMaxPro/README.md) — GLS-0183:** distinct 6DoF eyewear component of AR Studio; hardware model `RA202` in Rokid's security/support documentation.
- **[Rokid Glass 3](../../models/RokidGlass3/README.md) — GLS-0184:** current enterprise generation, model numbers `RG301` / `RG303`, with dedicated first-party manual and developer workflow.
- **Rokid X-Craft — ADJ-0010:** industrial explosion-proof AR headband/helmet-mounted system; preserved in the adjacent wearable catalog rather than inflating the smart-glasses count.

The audit also corrects two existing identities:

- **Rokid Glass 2 — GLS-0062:** Rokid's own chronology places the generation in **2020**, not 2021.
- **[Rokid AI Glasses / Style / Neo](../../models/RokidAIStyle/README.md) — GLS-0063:** current evidence resolves the display-free `RV203` family under one stable ID. Style and Neo are naming/market variants, not new canonical rows.

Current active canonical count after the Rokid admissions: **183**.

## Canonical Rokid eyewear map

### Enterprise standalone AR

- **Rokid Glass / Glass 1 — GLS-0061:** 2018 all-in-one enterprise/developer AR generation.
- **Rokid Glass 2 — GLS-0062:** 2020 split-type monocular enterprise AR generation.
- **Rokid Glass 3 — GLS-0184:** current enterprise/YodaOS-Sprite generation with direct developer/debug surface.

### Host-driven display / spatial branch

- **Rokid Air — GLS-0092:** early host-driven XR display.
- **Rokid Air Pro — GLS-0182:** camera-equipped Air sibling; separate hardware identity.
- **Rokid Max — GLS-0093:** host-driven XR display.
- **Rokid Max Pro — GLS-0183:** 6DoF/spatial eyewear used by AR Studio.
- **Rokid Max 2 — GLS-0094:** current host-driven display glasses.

### Integrated AI eyewear

- **Rokid AI Glasses / Style / Neo — GLS-0063:** display-free `RV203` camera/audio AI family.
- **Rokid Glasses — GLS-0064:** display-equipped integrated camera/AI eyewear.

## System/bundle identities

- **Rokid AR Studio:** Max Pro + Station Pro. Preserve the system, but count Max Pro once as eyewear.
- **Rokid AR Lite / AR Spatial:** Max 2 + Station 2. Preserve system identity without duplicating Max 2.
- **Rokid AR Joy / AR Joy 2:** Station-family entertainment bundles around Max/Max 2 generations; do not count unchanged glasses twice.
- **Rokid AI Glasses Style Pack:** `GLS-0063` eyewear plus accessory/power package; configuration, not another model.

## Rokid Glasses — GLS-0064

Integrated AI/AR eyewear. Rokid documents a 49 g frame, Snapdragon AR1 Gen 1 + NXP RT600, 2 GB RAM, 32 GB storage, dual-eye monochrome MicroLED waveguides at 480×640, 30° FOV, up to 1500 nits, 12 MP Sony IMX681 camera, four microphones, dual open-ear speakers, Wi-Fi 6, Bluetooth 5.3, 210 mAh battery, prescription support, translation, navigation, transcription and multimodal AI.

Report-card anchor: H8.5 W8.5 VAI8.5 S8.0 O7.0 OC6.5 CI5.5 Hack6.5 HUD8.5; **V7.5 at $699 sale / V7.0 at $799 regular (US, checked 2026-08-14).**

## Service-survival boundary

Rokid's first-party FAQ establishes a meaningful split for consumer Rokid Glasses. Operation and first activation require a phone, wireless internet, Rokid account and Hi Rokid app; account reassignment clears device information, and settings/firmware/media management remain app-mediated. Six-language offline translation can run after pairing, activation and model download, while Bluetooth phone audio and onboard capture leave plausible residual value.

The correct label is **recoverable with pre-provisioned local translation and phone-peripheral residue; defining AI remains service-dependent**. EV-0047 preserves the complete function table and the sign-out/endpoint-blocked test queue. “Offline” must not be rewritten as account-free or phone-free first use.

## Prescription / optical serviceability

Rokid Glasses use an official magnetic prescription frame. Rokid explicitly states that owners may take that frame to a local optical store and have lenses made by a professional optician. Current FAQ material documents prescription customization from approximately +6.00D to -16.00D and support for myopia and astigmatism, with a lens-curvature constraint for proper fit.

Serviceability state: **ordinary optical shop supported with official carrier/frame**. Rokid also offers a partner lens service, but that path is optional rather than the only supported route.

## Established report-card anchors for display branch

- **Rokid Air — GLS-0092:** H7.0 W7.0 VAI N/A S6.0 O4.0 OC8.0 CI9.0 Hack4.5 HUD7.5 V7.0.
- **Rokid Max — GLS-0093:** H8.0 W7.5 VAI N/A S6.5 O4.0 OC8.5 CI9.5 Hack4.5 HUD8.5 V8.0.
- **Rokid Max 2 — GLS-0094:** H8.5 W8.0 VAI N/A S6.5 O4.0 OC8.5 CI9.5 Hack4.5 HUD9.0 V8.0.

**Do not inherit these scores** into newly admitted Air Pro or Max Pro. Cameras, 6DoF behavior, optics, host requirements, and software boundaries differ materially.

## Source-contradiction watch

Rokid's current storefront and regional materials require provenance discipline:

- current AR-series comparison identifies AR Spatial as Max 2 + Station 2, while some individual storefront pages repeat Station 2 compute copy on glasses/bundle pages;
- Glass 3 reseller pages can conflict with the first-party enterprise manual on display terminology/resolution;
- the display-free `RV203` family is marketed under Rokid AI Glasses, Style, and Neo names;
- security-center “release dates” can reflect support lifecycle entries rather than the earliest public order/sale year.

Preserve the source and date for each claim instead of smoothing those differences into one spec sheet.

## Ownership interpretation

Display-only Rokid products can retain high service independence as host peripherals. Integrated consumer AI glasses provide richer AI/capture capability but are more tied to Rokid software and connected services. Enterprise Glass 3 exposes a materially different developer/debug surface, while Max Pro's spatial behavior depends on the AR Studio host architecture. The lineage therefore requires model-specific Owner Control and Cloud Independence rather than brand-wide scoring.

## Research priorities

1. Recover first-party Air Pro manuals, regulatory IDs, and archived pages.
2. Preserve Max Pro/Station Pro technical artifacts and separate glasses versus host claims.
3. Characterize Glass 3 `RG301` / `RG303`, ADB/package installation, firmware, local enterprise functions, and service-loss residue.
4. Resolve `RV203` versus Bolon `RV201/RV202` hardware differences before any additional canonical admission.
5. Map Hi Rokid / Rokid AI, Rokid AR, YodaOS-Master, and YodaOS-Sprite Enterprise responsibilities by generation.
6. Capture current first-party pages as dated evidence because storefront copy and naming presently vary across Rokid's lineup.
