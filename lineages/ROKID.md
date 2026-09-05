# Rokid smart-glasses lineage

Rokid is tracked as a **corporate lineage with multiple technical branches**, not as one homogeneous hardware platform. The company currently spans integrated camera/AI eyewear and host-driven personal-display/spatial-computing glasses. Claims, scores, software dependencies, and owner-control properties must stay branch- and model-specific.

**Relationship type:** corporate lineage with model-specific software, protocol, and hardware sub-relationships  
**Confidence:** Confirmed

## Current lineage map

| Product | GlassesResearch status | Technical role | Identity treatment |
|---|---|---|---|
| [Rokid Glasses](../models/RokidGlasses/README.md) | `GLS-0064` | Integrated camera + binocular MicroLED display + AI/audio eyewear | Distinct eyewear model |
| [Rokid AI Glasses Style](../models/RokidAIStyle/README.md) | Active investigation | Integrated camera/audio AI eyewear without an in-lens display | Distinct eyewear model; do not collapse into Rokid Glasses |
| Rokid AI Glasses Style Pack | Configuration of Style | Style glasses plus additional power/accessory package | Bundle/configuration; does not add another eyewear identity |
| [Rokid Max 2](../models/RokidMax2/README.md) | `GLS-0094` | Host-driven binocular personal display | Distinct eyewear model |
| [Rokid AR Spatial](../models/RokidARSpatial/README.md) | Active system investigation | Max 2 + Station 2 spatial-computing system | Product/system bundle; Max 2 remains the eyewear identity |
| [Rokid AR Joy 2](../models/RokidARJoy2/README.md) | Active system investigation | Max 2 + original Rokid Station entertainment system | Product/system bundle; Max 2 remains the eyewear identity |

Historical canonical members already preserved by GlassesResearch include **Rokid Glass (`GLS-0061`)**, **Rokid Air (`GLS-0092`)**, and **Rokid Max (`GLS-0093`)**.

## Branch 1 — integrated AI eyewear

### Rokid Glasses — GLS-0064

Rokid Glasses combine a wearer-view camera, microphones, speakers, onboard compute, wireless connectivity, and a binocular monochrome MicroLED waveguide display. The Hi Rokid/Rokid AI companion layer handles activation, settings, media management, updates, and connected AI services. Some functions can retain useful offline or phone-peripheral behavior after provisioning, but defining AI services remain materially service-dependent.

### Rokid AI Glasses Style

Style is a materially different product, not merely a display-disabled SKU of Rokid Glasses. Rokid currently documents a lighter approximately 38.5 g frame, no in-lens display, direct prescription-lens fitting, a 12 MP Sony IMX681 POV camera, open-ear audio, four microphones, Wi-Fi 6, Bluetooth 5.3, 32 GB storage, voice/touch/head-gesture interaction, and companion-app dependence for pairing, settings, media management, and updates.

The architecture merits its own investigation because removing the display changes wearability, power use, interaction, accessibility, privacy expectations, and the value of the device if Rokid's service layer disappears.

## Branch 2 — host-driven display and spatial systems

### Rokid Air / Max / Max 2

Air, Max, and Max 2 are fundamentally display peripherals. Their useful behavior depends on a compatible video/compute source rather than an onboard general-purpose AI stack. This produces a very different owner-control and cloud-independence profile from Rokid's integrated AI glasses.

Max 2 (`GLS-0094`) is the current principal eyewear hardware in Rokid's AR line. Rokid documents direct DisplayPort-over-USB-C operation with compatible source devices and built-in myopia adjustment from 0.00D to -6.00D. Spatial-computing behavior is added when Max 2 is paired with Station 2.

### Rokid AR Spatial

Rokid's current lineup defines **AR Spatial as Max 2 + Station 2**, with Station 2 providing the compute/software layer for 3DoF spatial computing and multiple virtual app windows. GlassesResearch therefore treats AR Spatial as a commercially meaningful system configuration, but not as a separate eyewear model from Max 2.

### Rokid AR Joy 2

Rokid's current comparison page defines **AR Joy 2 as Max 2 + the original Rokid Station**, aimed at single-screen entertainment. The original Station and Station 2 have materially different compute/software roles and must not be conflated.

## Source-contradiction watch

Rokid's current global storefront contains copy and specification conflicts that must remain visible in the evidence layer:

- the AR-series comparison page identifies AR Spatial as **Max 2 + Station 2** and AR Joy 2 as **Max 2 + original Rokid Station**;
- individual AR product pages currently contain sections advertising **8 GB RAM / 128 GB storage, Wi-Fi 6, Bluetooth 5.2, a 5000 mAh battery, and YodaOS-Master** even where that wording appears to describe Station 2 rather than the selected glasses/bundle;
- the Max 2 standalone product page likewise contains Station 2-style compute copy despite the AR-series comparison page describing standalone Max 2 as a display device that uses the connected phone, computer, or console;
- current pricing and product naming vary across collection and landing pages.

These are manufacturer-source contradictions, not facts to normalize away. Model records should preserve which page asserted each claim and prefer architecture-specific documentation over generic storefront modules.

## Investigation priorities

1. Capture and hash current first-party product/specification pages for Style, Max 2, AR Spatial, AR Joy 2, Station, and Station 2.
2. Resolve Max 2 display specifications independently from Station 2 compute specifications.
3. Map Hi Rokid / Rokid AI App versus Rokid AR App responsibilities and account/network requirements.
4. Verify whether Style exposes the same terminal SDK surface as Rokid Glasses or only a subset.
5. Test offline/service-loss behavior separately for Rokid Glasses, Style, bare Max 2, Max 2 + original Station, and Max 2 + Station 2.
6. Preserve regional SKU, firmware, prescription-support, and accessory compatibility boundaries.
7. Track repairability, battery replacement, bootloader/firmware access, and long-term service survivability.

## Primary sources

- [Rokid global site](https://global.rokid.com/)
- [Rokid AI Glasses Series](https://global.rokid.com/collections/rokid-ai-glasses-series)
- [Rokid AI Glasses Style](https://global.rokid.com/products/rokid-ai-glasses-style)
- [Rokid AR Glasses Series](https://global.rokid.com/collections/rokid-ar-glasses-series)
- [Rokid Max 2](https://global.rokid.com/products/rokid-max-2-ar-glasses)
- [Rokid AR Spatial](https://global.rokid.com/products/rokid-ar-spatial)
- [Rokid AR Joy 2](https://global.rokid.com/products/rokid-ar-joy-2)
- [Rokid terminal SDK](https://x-docs.rokid.com/docs/en/terminal-sdk/)

## Related GlassesResearch layers

- [Populated Rokid research record](../research/populated/ROKID.md)
- [Model Registry](../models/CATALOG.md)
- [Report Cards](../docs/REPORT_CARD.md)
- [Comparison engine](../docs/COMPARISON_ENGINE.md)
- [Open Development Resource Ledger](../hacking/OPEN_HACKING_RESOURCE_LEDGER.md)
