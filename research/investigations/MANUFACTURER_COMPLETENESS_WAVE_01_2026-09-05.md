# Manufacturer Completeness Audit — Wave 01

**Date:** 2026-09-05  
**Scope:** RayNeo / TCL / Thunderbird, Epson Moverio, VITURE, INMO, Innovative Eyewear / Lucyd  
**Trigger:** Rokid's whole-manufacturer audit exposed three canonical eyewear omissions despite substantial prior Rokid coverage.

## Question

How many apparently well-covered manufacturers contain models, generations, aliases, regional identities, or adjacent wearables that are invisible when GlassesResearch works model-by-model instead of reconstructing the manufacturer as a whole?

## Method

For each manufacturer this pass collision-checked:

1. the current canonical `models/THE_LIST.md` population;
2. existing report cards, news, discovery records, lineage packets and model pages;
3. current first-party store/catalog pages;
4. historical first-party company, product, support, press and developer material;
5. real-world model numbers and regional/brand aliases where available;
6. acquisition evidence versus announcement/prototype evidence;
7. bundles, collector editions and controller packs versus distinct eyewear hardware;
8. adjacent head-worn devices that should not inflate the smart-glasses count.

No score inheritance is authorized by this audit.

## Result

Wave 01 identifies **ten canonical smart-glasses admissions** and **two adjacent industrial wearables**, while deliberately withholding IDs from several unresolved or bundle/configuration identities.

### Admit to canonical purchaser-history ledger

| ID | Manufacturer | Model | Why it crosses the threshold |
|---|---|---|---|
| `GLS-0185` | RayNeo | RayNeo iO | Previously verified as a named Sep. 4 launch; first-party store now shows active in-stock checkout and prescription ordering. |
| `GLS-0186` | RayNeo | RayNeo GT | Current first-party store with active checkout; materially named 46°/68 g GT hardware identity. |
| `GLS-0187` | RayNeo | RayNeo GT Max | Current first-party store with active checkout; materially distinct 59°/76 g product with three IPD size classes. |
| `GLS-0188` | VITURE | VITURE Pro 2 | First-party 5th Anniversary generation, actively sold at $299 with new UltraClarity 3.0 optical/mechanical package. |
| `GLS-0189` | Epson | Moverio BT-350 | Distinct first-party multi-user commercial smart-glasses product, model `V11H837020`. |
| `GLS-0190` | Epson | Moverio BT-30E | Epson support records a Nov. 2018 launch; separate compact monitor-model identity supported in manuals/SDK/firmware. |
| `GLS-0191` | Lucyd | Lucyd Loud 1.0 | Manufacturer says approximately 800 units were made and sold, mostly in 2018. |
| `GLS-0192` | Lucyd | Lucyd Loud — second edition | Manufacturer says it was designed in-house, built Q1 2019 and still available from Lucyd in July 2020. |
| `GLS-0193` | Lucyd | Lucyd Loud 2020 | Manufacturer says Bluetooth 5.0 generation launched January 2020 in seven styles. |
| `GLS-0194` | INMO | INMO X AI+Camera Glasses | Manufacturer's history lists it as a Nov. 2024 product and says the first blind-order batch, alongside Air3/GO2, exceeded 10,000 units. |

Canonical count consequence: **183 → 193**.

## RayNeo / TCL / Thunderbird

### Existing research that masked the gap

The site already had strong X2/X3 Pro research, an Air-family population, NXTWEAR entries, V3 admission and even a verified August 21 news story naming **iO, GT and GT Max**. The news story correctly withheld canonical admission because the first-party pages then pointed to September 4 as the availability milestone.

### What changed

On September 5 RayNeo's own store shows:

- **RayNeo iO** with active purchase controls, in-stock package variants, prescription purchase path and shipping guidance;
- **RayNeo GT** at an active $299 sale price;
- **RayNeo GT Max** at an active $399 sale price.

RayNeo's GT comparison also establishes separate product characteristics rather than a mere size/color option: GT is listed at 46° FOV / 68 g while GT Max is 59° / 76 g and adds three precision IPD size classes.

Disposition: admit all three. Continue historical TCL/Thunderbird regional-name audit.

Primary evidence:
- https://www.rayneo.com/pages/rayneo-io-ai-glasses
- https://www.rayneo.com/products/rayneo-io-ai-glasses
- https://www.rayneo.com/pages/rayneo-gt-series-ar-glasses
- https://www.rayneo.com/pages/buying-guide

## Epson Moverio

### BT-350

Epson's surviving US product page identifies **Moverio BT-350 Smart Glasses**, model `V11H837020`, as a multi-user commercial AR product with Moverio OS, onboard Intel Atom compute, camera, sensors, wireless connectivity and developer support. It is materially distinct from BT-300 despite architectural kinship.

Disposition: `GLS-0189`.

Primary evidence:
- https://epson.com/For-Work/Wearables/Smart-Glasses/Moverio-BT-350-Smart-Glasses/p/V11H837020

### BT-30E

Epson Japan's support record gives **BT-30E** a November 2018 release date and dedicated firmware history. Epson's technical FAQ groups BT-30E/BT-35E as monitor models but distinguishes their interface/design family from later BT-40/45C and from earlier Android-integrated BT-300/350. Epson's licensing and support material names BT-30E as a separate hardware product.

Disposition: `GLS-0190`.

Primary evidence:
- https://www.epson.jp/support/portal/hoshu/bt-30e.htm
- https://tech.moverio.epson.com/en/technical_faq/
- https://www2.epson.jp/support/manual/413701300.PDF

### Moverio Pro BT-2000 / BT-2200

Epson sells/preserves both as industrial **smart headsets**. BT-2000 uses a headband and forehead pad specifically to remove pressure from the nose; BT-2200 is engineered for mounting with safety helmets. BT-2200 preserves much of BT-2000's internal platform but adds a helmet-oriented hinge.

Disposition:
- `ADJ-0011` — Moverio Pro BT-2000
- `ADJ-0012` — Moverio Pro BT-2200

Primary evidence:
- https://epson.com/For-Work/Wearables/Smart-Glasses/Moverio-Pro-BT-2000-Smart-Headset-/p/V11H725020
- https://epson.com/For-Work/Wearables/Smart-Glasses/Moverio-Pro-BT-2200-Smart-Headset/p/V11H853020

## VITURE

### VITURE Pro 2

VITURE's current first-party 5th Anniversary material sells **VITURE Pro 2** for $299 and describes a new UltraClarity 3.0 package with 50° FOV, 1600-nit claimed brightness, 0 to -5D built-in diopter range and a 63 g frame. Current bundles also expose Pro 2 as a selectable eyewear identity beside Beast and Luma models.

Disposition: `GLS-0188`.

Primary evidence:
- https://www.viture.com/pro2
- https://www.viture.com/product/viture-pro-2-ultimate-collection

### Phantom Beast

The VITURE × Phantom Blade Zero **Phantom Beast** is currently marketed as a collector/themed Beast edition. The audit found presentation/theme/accessory differentiation but not enough evidence of a distinct optics/electronics generation from canonical VITURE Beast.

Disposition: configuration/collector edition of Beast; **no new GLS ID** unless hardware evidence changes.

## INMO

INMO's company-history page explicitly divides its eyewear into Air, GO and X branches. It states that:

- the INMO X series first debuted as a 5G all-in-one AR concept/family in May 2021;
- in November 2024, **INMO X series AI photo glasses** were released alongside Air3 and GO2;
- the first batch of blind orders exceeded 10,000;
- the product list names **INMO X AI+Camera Glasses — 2024 Nov.**

This is sufficient to establish a named marketed product and preorder/acquisition event, while not sufficient to assume that the May 2021 X device is the same hardware.

Disposition: admit the 2024 identity as `GLS-0194`; keep the 2021 X-series relationship unresolved until model-specific archival evidence is recovered.

Primary evidence:
- https://www.inmoxr.com/pages/about-us

## Innovative Eyewear / Lucyd

The current canonical Lucyd history began with Lyte in 2021, but Lucyd's own July 2020 corporate retrospective proves a commercial pre-Lyte lineage.

### Loud 1.0

Lucyd calls Loud 1.0 its first Bluetooth audio glass and states approximately **800 units were made and sold, mostly in 2018**.

Disposition: `GLS-0191`.

### Loud second edition

Lucyd describes a **second edition** designed in-house and built in Q1 2019, with multiple colors/patterns and a Slim style later renamed Youth. The company says this edition remained available on Lucyd.co in July 2020.

Disposition: `GLS-0192`. Preserve “second edition” as manufacturer wording; do not invent the unsupported name “Loud 2.0.”

### Loud 2020

Lucyd says a Bluetooth 5.0 chipset enabled a new **Loud 2020**, developed in seven styles and launched in January 2020.

Disposition: `GLS-0193`.

Primary evidence:
- https://lucyd.co/blogs/news/july-2020-corporate-update

### Unresolved later collection boundary

Current first-party corporate/press material refers to a **Lucyd Lyte 2025 collection** launched in December 2024 and compares newer 2026 hardware against it. That is a substantial generation lead but not yet enough to decide whether “Lyte 2025” is a distinct electronics generation, a collection refresh, or several named frame models on an existing platform.

Disposition: retain as active lineage candidate; no new GLS ID in this wave.

Licensed Nautica, Eddie Bauer and Reebok collections receive the same treatment: brand/frame proliferation does not automatically equal hardware-generation proliferation.

## Coverage debt remaining after Wave 01

The point of this program is not to declare a manufacturer complete after finding one omission. After these admissions:

- **RayNeo/TCL/Thunderbird** remains audit-in-progress because China-market Thunderbird and NXTWEAR/RayNeo naming need a full historical collision map.
- **Epson Moverio** has the clearest known historical branches mapped, but regional/industrial archival checks remain.
- **VITURE** remains audit-in-progress because fast release cadence and collector/co-brand editions require continuing identity checks.
- **INMO** remains audit-in-progress because the 2021-versus-2024 X relationship is unresolved.
- **Lucyd** remains audit-in-progress because Lyte 2025 and licensed-collection electronics generations remain unresolved.

This is intentional. A dedicated lineage page is not a certificate of completeness.

## Site/process changes produced by this investigation

- `data/manufacturer-coverage.json` makes manufacturer completeness explicit and machine-readable.
- `scripts/check_manufacturer_coverage.py` fails CI when an exact Maker population reaches three canonical rows without a ledger assignment.
- Existing large but unaudited families emit visible coverage-debt warnings.
- `docs/MANUFACTURER_COMPLETENESS.md` publishes the methodology and priority queue.
- dedicated corporate lineage chapters are added for RayNeo/TCL, Epson, VITURE, INMO and Lucyd.

The next audit waves should continue down the risk queue rather than returning to opportunistic model discovery alone.
