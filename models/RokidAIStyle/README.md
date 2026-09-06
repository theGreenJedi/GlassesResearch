# Rokid AI Glasses / Style / Neo — GLS-0063

Rokid's display-free camera/audio AI-glasses branch is preserved under stable GlassesResearch ID **GLS-0063**. Current first-party naming varies by region and storefront: **Rokid Ai Glasses**, **Rokid AI Glasses Style**, and **Rokid AI Glasses Neo / Neo (Style)** refer to the same display-free product family unless model-specific evidence proves otherwise.

**Technology lineage:** [Rokid](../../lineages/ROKID.md)  
**Catalog state:** canonical — `GLS-0063`  
**Manufacturer model:** `RV203`  
**Evidence state:** current first-party manufacturer/security documentation + current retail availability; hands-on verification pending

## Identity correction

The older GlassesResearch row described `GLS-0063` too loosely as a 2024 region-limited “Rokid AI Glasses” product. Current primary evidence resolves the identity more precisely:

- Rokid's security center lists **Rokid Ai Glasses — RV203** separately from display-equipped Rokid Glasses `RV101/RV102`.
- Rokid's current global store markets the display-free device as **Rokid AI Glasses Style**.
- Regional Rokid stores/pages also use **Rokid AI Glasses Neo** and **Neo (Style)** wording while describing the same display-free architecture.

The stable GLS ID is retained and the real-world nomenclature is expanded rather than minting a duplicate ID.

## Manufacturer-documented hardware

Current Rokid documentation describes:

- approximately **38.5 g** frame weight without prescription lenses;
- TR90 frame with titanium-alloy hinges;
- Qualcomm Snapdragon AR1 Gen 1 + RT600-class companion processing;
- 2 GB RAM and 32 GB storage;
- **12 MP Sony IMX681** wearer-view camera;
- 3024 × 4032 still capture and video up to 3K at 30 fps;
- 109° camera field of view and f/2.25 aperture;
- four-microphone directional array with noise reduction;
- dual directional open-ear AAC speakers;
- Wi-Fi 6 and Bluetooth 5.3;
- 210 mAh battery;
- IPX4 splash resistance;
- voice, touch, and head-gesture interaction;
- **no in-lens display**.

Rokid states that prescription lenses fit directly into the frame and currently advertises prescription, progressive, photochromic, tinted and other lens options. Exact service availability remains region-dependent.

## Software and service boundary

Rokid states that the Hi Rokid companion app is required for pairing, settings, media management, and updates. AI responses, navigation, and translation are delivered through open-ear audio and the app rather than an in-lens display.

Shared chipset family and companion software with Rokid Glasses do not prove identical service-survival behavior or SDK exposure. `GLS-0063` therefore retains its own cloud-independence and owner-control investigation.

## Community Research

The independent [aimindseye / rokid-ai-glasses Community Research profile](/docs/community-research/aimindseye-rokid-ai-glasses/) tracks a public research wiki focused specifically on this display-free family. Its findings remain community-attributed unless separately reproduced by GlassesResearch; the project's own qualification boundaries should be preserved when citing it.

## Style Pack identity

**Rokid AI Glasses Style Pack is not a second glasses model.** Rokid's current collection describes the Pack as the same underlying eyewear with additional power/accessory capacity. It remains a retail configuration of `GLS-0063`.

## Bolon relationship

Rokid's security center separately lists **Bolon Ai Glasses** model numbers `RV201` / `RV202`. Current evidence shows a very close shared display-free platform relationship, but GlassesResearch does not yet count the Bolon co-brand as a separate canonical model because an unchanged co-brand/frame treatment is insufficient by itself. It remains a lineage/registry target until materially distinct hardware is established.

## Investigation queue

1. Confirm RV203 model labeling and regional SKU behavior hands-on.
2. Determine which functions survive initial setup with network access removed.
3. Test capture behavior, recording indicator behavior, file export, metadata, and local storage access.
4. Map companion-app permissions, account requirements, endpoints, update behavior, and data retention.
5. Determine whether Rokid's current terminal/glasses SDK explicitly supports RV203 and which APIs are exposed.
6. Check ADB, USB, Bluetooth services, Wi-Fi services, firmware packages, update manifests, and recoverability paths.
7. Verify prescription-lens serviceability with ordinary optical shops and regional constraints.
8. Resolve RV203 versus Bolon RV201/RV202 electrical/mechanical differences before any additional canonical admission.

## Primary sources

- [Rokid AI Glasses Style product page](https://global.rokid.com/products/rokid-ai-glasses-style)
- [Rokid AI Glasses Style overview](https://global.rokid.com/pages/rokid-ai-glasses-style)
- [Rokid security center](https://global.rokid.com/pages/security-center)
- [Rokid AI Glasses Series comparison](https://global.rokid.com/collections/rokid-ai-glasses-series)

## Related GlassesResearch resources

- [Rokid lineage](../../lineages/ROKID.md)
- [Rokid historical audit](../../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
- [Rokid populated research record](../../research/populated/ROKID.md)
- [Rokid Glasses](../RokidGlasses/README.md)
- [Model Registry](../CATALOG.md)
