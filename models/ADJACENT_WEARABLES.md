# Adjacent Wearable-HCI Catalog

**Edition:** 2026-09-05  
**Scope:** purchasable or documented-procurement wearable-HCI devices that belong in GlassesResearch's broader augmented-human research universe but are **not fundamentally smart glasses**.

This catalog implements the form-factor rule in [`WEARABLE_HCI.md`](../docs/taxonomy/WEARABLE_HCI.md): one research umbrella, separate catalogs by physical interface type, shared evidence standards and shared ownership/control philosophy. Entries here must never be silently included in the smart-glasses count in [`THE_LIST.md`](THE_LIST.md).

For era fields, `c.` marks an approximate year and `≤2026` means the current evidence proves the product was obtainable by this edition but has not yet pinned the earliest sale year.

## Headphones / head-worn audio-display devices

| ID | Maker | Model | Era | State | Form | Evidence / research |
|---|---|---|---:|---|---|---|
| ADJ-0001 | Optinvent | ORA-X | c. 2017 | legacy / archival | over-ear AR headphones | [ORA lineage packet](../docs/report-cards/LINEAGE_OPTINVENT_ORA.md) |
| ADJ-0015 | Vuzix | iWear Video Headphones | 2015 | legacy | headphone/visor video and VR display | [Vuzix Wave 02 audit](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md); [Vuzix lineage](../lineages/VUZIX.md) |

## Industrial head-worn AR / mixed-reality systems

| ID | Maker | Model | Era | State | Form | Evidence / research |
|---|---|---|---:|---|---|---|
| ADJ-0002 | DAQRI | Smart Helmet | c. 2016 | legacy | industrial AR helmet | [DAQRI lineage packet](../docs/report-cards/LINEAGE_DAQRI_PROFESSIONAL_AR.md) |
| ADJ-0003 | ThirdEye | MIDAS | ≤2026 | current / enterprise | protective head-worn AR | [ThirdEye lineage packet](../docs/report-cards/LINEAGE_THIRDEYE_X_SERIES.md) |
| ADJ-0004 | Microsoft | HoloLens | 2016 | legacy | mixed-reality headset | [HoloLens lineage packet](../docs/report-cards/LINEAGE_MICROSOFT_HOLOLENS.md) |
| ADJ-0005 | Microsoft | HoloLens 2 | 2019 | legacy / enterprise lifecycle | mixed-reality headset | [HoloLens lineage packet](../docs/report-cards/LINEAGE_MICROSOFT_HOLOLENS.md) |
| ADJ-0006 | Magic Leap | Magic Leap One / Magic Leap 1 | 2018 | legacy | spatial-computing headset + compute puck | [Magic Leap lineage packet](../docs/report-cards/LINEAGE_MAGIC_LEAP.md) |
| ADJ-0007 | Magic Leap | Magic Leap 2 | 2022 | enterprise | spatial-computing headset + compute puck | [Magic Leap lineage packet](../docs/report-cards/LINEAGE_MAGIC_LEAP.md) |
| ADJ-0010 | Rokid | X-Craft | 2020 | current / enterprise / supply-limited | industrial explosion-proof AR headband / helmet-mounted system | [Rokid historical audit](../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md); [current B2B source](https://de.rokid.com/de-de/products/rokid-x-craft-for-b2b) |
| ADJ-0011 | Epson | Moverio Pro BT-2000 | c. 2016 | legacy / enterprise | industrial AR smart headset with headband / forehead support | [Epson lineage](../lineages/EPSON_MOVERIO.md); [first-party product](https://epson.com/For-Work/Wearables/Smart-Glasses/Moverio-Pro-BT-2000-Smart-Headset-/p/V11H725020) |
| ADJ-0012 | Epson | Moverio Pro BT-2200 | 2017 | legacy / enterprise | helmet-compatible industrial AR smart headset | [Epson lineage](../lineages/EPSON_MOVERIO.md); [first-party product](https://epson.com/For-Work/Wearables/Smart-Glasses/Moverio-Pro-BT-2200-Smart-Headset/p/V11H853020) |
| ADJ-0013 | Vuzix | Tac-Eye | ≤2009 | legacy / defense-industrial | rugged monocular display clipped to ballistic eyewear, headsets or safety goggles | [Vuzix Wave 02 audit](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md); [Vuzix lineage](../lineages/VUZIX.md) |
| ADJ-0014 | Vuzix | M2000AR | 2013 | legacy / industrial | waveguide HMD mounted to hardhats or goggles | [Vuzix Wave 02 audit](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md); [Vuzix lineage](../lineages/VUZIX.md) |

## Eyeglass-mounted assistive modules

These devices use ordinary glasses as a mounting surface but are not themselves eyeglass frames. They therefore remain adjacent wearables rather than inflating the smart-glasses count.

| ID | Maker | Model | Era | State | Form | Evidence / research |
|---|---|---|---:|---|---|---|
| ADJ-0008 | OrCam | MyEye 2 Pro | ≤2026 | current | magnetic eyeglass-mounted visual-AI/audio module | [OrCam lineage packet](../docs/report-cards/LINEAGE_ORCAM_MYEYE.md) |
| ADJ-0009 | OrCam | MyEye 3 Pro | ≤2026 | current | magnetic eyeglass-mounted visual-AI/audio module | [OrCam lineage packet](../docs/report-cards/LINEAGE_ORCAM_MYEYE.md) |

## Sport-goggle attachments

These products attach to sport goggles rather than forming an eyeglass frame themselves.

| ID | Maker | Model | Era | State | Form | Evidence / research |
|---|---|---|---:|---|---|---|
| ADJ-0016 | Vuzix | Smart Swim | 2020 | legacy/current support unclear | AR training display attachment for swim goggles | [Vuzix Wave 02 audit](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md); [product sheet](https://files.vuzix.com/Content/pdfs/vuzix-smart-swim-d01.pdf) |

## Non-wearable lineage relatives

Not every related platform is wearable. These remain documented because they help explain a manufacturer's HCI lineage, but they are not assigned `ADJ-` wearable IDs.

- **DAQRI Smart HUD** — related AR/display platform for vehicle/industrial use; not a wearable.

## Admission and counting rules

- A device enters this catalog only after a model-level acquisition or documented procurement route is established.
- A product is classified by **physical form and interface role**, not by marketing terminology.
- A headset, helmet, clip-on module or headphone does not become “smart glasses” merely because it provides AR, AI, sensing or a near-eye display.
- Report-card dimensions use the same fixed ruler as smart glasses where applicable; truly inapplicable dimensions are `N/A`.
- New form-factor shelves—earables, neural/gesture interfaces, pendants, watches/rings and composite systems—should be added here as qualifying products are researched.
