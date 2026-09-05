# Rokid smart-glasses lineage

Rokid is tracked as a **corporate lineage with multiple technical branches**, not as one homogeneous hardware platform. Its history spans standalone enterprise AR, tethered display glasses, spatial-computing systems, integrated display-AI eyewear, display-free camera/audio AI glasses, and industrial head-worn AR. Claims, scores, software dependencies, and owner-control properties must remain branch- and model-specific.

**Relationship type:** corporate lineage with model-specific software, protocol, hardware, and system sub-relationships  
**Confidence:** Confirmed

## Canonical lineage map

| Product | GlassesResearch status | Technical role | Identity treatment |
|---|---|---|---|
| Rokid Glass / Glass 1 | `GLS-0061` | Early standalone enterprise AR | Distinct eyewear generation |
| Rokid Glass 2 | `GLS-0062` | Split-type monocular enterprise AR | Distinct eyewear generation |
| [Rokid Glass 3](../models/RokidGlass3/README.md) | `GLS-0184` | Current enterprise smart glasses / YodaOS-Sprite Enterprise | Distinct eyewear generation |
| Rokid Air | `GLS-0092` | Host-driven XR display | Distinct eyewear model |
| [Rokid Air Pro](../models/RokidAirPro/README.md) | `GLS-0182` | Camera-equipped host-driven AR glasses | Distinct eyewear model |
| Rokid Max | `GLS-0093` | Host-driven XR display | Distinct eyewear model |
| [Rokid Max Pro](../models/RokidMaxPro/README.md) | `GLS-0183` | 6DoF spatial eyewear used by AR Studio | Distinct eyewear model |
| [Rokid Max 2](../models/RokidMax2/README.md) | `GLS-0094` | Host-driven binocular personal display | Distinct eyewear model |
| [Rokid AI Glasses / Style / Neo](../models/RokidAIStyle/README.md) | `GLS-0063` | Display-free camera/audio AI eyewear (`RV203`) | One canonical family with regional/current naming aliases |
| [Rokid Glasses](../models/RokidGlasses/README.md) | `GLS-0064` | Integrated camera + binocular MicroLED display + AI/audio eyewear | Distinct eyewear model |
| Rokid X-Craft | `ADJ-0010` | Industrial explosion-proof AR headband / helmet-mounted system | Adjacent wearable; excluded from smart-glasses count |

## System and bundle identities

| System / retail configuration | Composition | Counting treatment |
|---|---|---|
| Rokid AR Studio | Max Pro + Station Pro | System identity; Max Pro is the eyewear model |
| Rokid AR Lite / current AR Spatial | Max 2 + Station 2 | System identity; Max 2 is the eyewear model |
| Rokid AR Joy / AR Joy 2 | Max/Max 2 + Station-family host depending generation | System/bundle identity; do not duplicate unchanged eyewear |
| Rokid AI Glasses Style Pack | GLS-0063 eyewear + power/accessory package | Retail configuration; no additional model |

## Branch 1 — enterprise standalone AR: Glass 1 → Glass 2 → Glass 3

### Rokid Glass / Glass 1 — GLS-0061

The original 2018 Rokid Glass established Rokid's early all-in-one enterprise/developer AR direction. It remains a canonical historical model because it crossed a documented enterprise/developer procurement threshold.

### Rokid Glass 2 — GLS-0062

Rokid's corporate chronology places Glass 2 in **2020**, not 2021. The generation shifted to a split-type monocular optical-waveguide architecture and reached enterprise/developer procurement. Generation-specific internals must remain separate from Glass 1 and Glass 3.

### Rokid Glass 3 — GLS-0184

Glass 3 is a current enterprise generation with first-party developer documentation, enterprise manual, and model numbers `RG301` / `RG303`. Rokid documents YodaOS-Sprite Enterprise, direct glasses-side application execution, Android Studio/debug workflows, Bluetooth and Wi-Fi/P2P communication, media capture, OTA capabilities, and enterprise recognition/work-assistance functions.

This is not an enterprise alias for consumer Rokid Glasses. It receives its own canonical identity and research surface.

## Branch 2 — host-driven display and spatial eyewear

### Rokid Air — GLS-0092

Air is an early consumer host-driven XR display. Its durable value is largely peripheral/display behavior rather than onboard cloud AI.

### Rokid Air Pro — GLS-0182

Air Pro is a distinct 2021 sibling, not an Air bundle. Rokid's own developer material states that **Air Pro has cameras while Air does not**, while Air provides myopia adjustment that Air Pro lacks. The UXR SDK addresses the two as separate targets. Those differences materially affect sensing, privacy, optics, and AR capability.

### Rokid Max — GLS-0093

Max continues the host-driven personal-display branch.

### Rokid Max Pro — GLS-0183

Max Pro is the glasses component of AR Studio and is separately identifiable from Station Pro. Rokid's AR Studio developer material documents Max Pro-specific display hardware and 6DoF/spatial behavior, while the current security center lists hardware model `RA202`. AR Studio is therefore a system identity built around a distinct eyewear model, not merely ordinary Max bundled with a compute puck.

### Rokid Max 2 — GLS-0094

Max 2 is the current principal host-driven display glasses model in Rokid's consumer AR line. Rokid documents direct DisplayPort-over-USB-C operation with compatible source devices and built-in myopia adjustment from 0.00D to -6.00D. Spatial-computing behavior is added when Max 2 is paired with Station 2.

## Branch 3 — integrated AI eyewear

### Rokid AI Glasses / Style / Neo — GLS-0063

The display-free camera/audio branch is now resolved under one stable identity. Rokid's security center identifies **Rokid Ai Glasses model `RV203`**; current global retail uses **Rokid AI Glasses Style**, while regional pages also use **Neo** / **Neo (Style)**. GlassesResearch preserves those real-world names as aliases rather than creating duplicate GLS rows.

The approximately 38.5 g architecture uses AR1/RT600-class processing, 12 MP camera, open-ear audio, four microphones, Wi-Fi 6, Bluetooth 5.3 and local storage, but no in-lens display. Its service-survival and SDK behavior must be tested independently from display-equipped Rokid Glasses.

Rokid also lists **Bolon AI Glasses `RV201` / `RV202`**. Available evidence shows a close shared-platform relationship, but a co-brand/frame treatment alone does not earn another canonical model. Bolon remains a lineage/registry target until materially distinct hardware is established.

### Rokid Glasses — GLS-0064

Rokid Glasses combine a wearer-view camera, microphones, speakers, onboard compute, wireless connectivity, and a binocular monochrome MicroLED waveguide display. The Hi Rokid/Rokid AI companion layer handles activation, settings, media management, updates, and connected AI services. Some useful offline or phone-peripheral behavior remains after provisioning, but defining AI services remain materially service-dependent.

## Adjacent industrial branch — X-Craft

Rokid X-Craft is historically important but is **not counted as smart glasses**. Rokid describes it as an industrial 5G/explosion-proof AR headband/helmet-mounted product, and current B2B channels preserve separately orderable variants. It is therefore `ADJ-0010` in the Adjacent Wearable-HCI Catalog.

## Source-contradiction watch

Rokid's current global storefront contains copy and specification conflicts that must remain visible in the evidence layer:

- the AR-series comparison page identifies AR Spatial as **Max 2 + Station 2** and AR Joy 2 as a Station-based Max 2 bundle;
- individual AR product pages currently contain **Station 2-like compute specifications** even where the selected product is bare Max 2 or a different Station generation;
- some regional Glass 3 seller pages conflict with Rokid's first-party enterprise manual on display terminology/resolution;
- product naming for the `RV203` display-free family varies among Rokid AI Glasses, Style, and Neo;
- support/security dates do not always equal first public sale/order dates.

These are source-boundary findings, not inconsistencies to normalize away.

## Investigation priorities

1. Recover and preserve first-party Air Pro manuals, regulatory identifiers, and archived product pages.
2. Separate Max Pro glasses specifications from Station Pro compute specifications and capture AR Studio developer artifacts.
3. Preserve Glass 3 manuals/SDK demos and map `RG301` versus `RG303` differences, ADB/package-install behavior, and service-loss residue.
4. Resolve `RV203` versus Bolon `RV201/RV202` mechanical/electrical differences before considering any extra Bolon canonical row.
5. Map Hi Rokid / Rokid AI App, Rokid AR App, YodaOS-Master, and YodaOS-Sprite Enterprise responsibilities by generation.
6. Test offline/service-loss behavior separately for integrated AI eyewear, bare display glasses, Station-based systems, and enterprise standalone devices.
7. Preserve regional SKU, firmware, prescription-support, repairability, battery-replacement, bootloader, and accessory-compatibility boundaries.

## Primary sources

- [Rokid corporate milestones](https://www.rokid.com/en-US/about)
- [Rokid global site](https://global.rokid.com/)
- [Rokid security center](https://global.rokid.com/pages/security-center)
- [Rokid AI Glasses Style](https://global.rokid.com/products/rokid-ai-glasses-style)
- [Rokid AR Glasses Series](https://global.rokid.com/collections/rokid-ar-glasses-series)
- [Rokid AR Studio](https://arstudio.rokid.com/)
- [Rokid Air / Air Pro developer discussion](https://forum.rokid.com/post/detail/365)
- [Rokid Glass 3 developer guide](https://x-docs.rokid.com/docs/en/downloads/demo-guide.html)
- [Rokid terminal SDK](https://x-docs.rokid.com/docs/en/terminal-sdk/)

## Related GlassesResearch layers

- [Rokid historical audit](../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
- [Populated Rokid research record](../research/populated/ROKID.md)
- [Adjacent Wearable-HCI Catalog](../models/ADJACENT_WEARABLES.md)
- [Model Registry](../models/CATALOG.md)
- [Report Cards](../docs/REPORT_CARD.md)
- [Comparison engine](../docs/COMPARISON_ENGINE.md)
- [Open Development Resource Ledger](../hacking/OPEN_HACKING_RESOURCE_LEDGER.md)
