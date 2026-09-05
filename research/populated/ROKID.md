# Rokid — populated research record

**Technology lineage:** [Rokid](../../lineages/ROKID.md)

Primary evidence includes the official terminal SDK (`EV-0024`), Rokid Glasses specifications (`EV-0025`), optical-service evidence (`EV-0038`), `docs/report-cards/BATCH_02.md`, display-lineage research from `HIGH_THROUGHPUT_BATCH_04.md`, [EV-0047](../../evidence/EV-0047-Rokid-Glasses-service-survival.md), and [EV-0052](../../evidence/EV-0052-current-value-wave-one.md).

## Family boundary
Rokid spans host-driven display glasses (Air/Max) and integrated camera/display/AI glasses (Rokid Glasses). The 2026 lineup also adds display-free [Rokid AI Glasses Style](../../models/RokidAIStyle/README.md). Do not transfer camera, onboard processing, AI, cloud-dependence, SDK, or service-survival claims across classes.

## Current-lineup investigation — checked 2026-09-05

Rokid's current global storefront exposes two product families that should be represented separately while remaining under one corporate lineage.

### Integrated AI eyewear

- **[Rokid Glasses](../../models/RokidGlasses/README.md) — GLS-0064:** distinct display-equipped camera/AI eyewear.
- **[Rokid AI Glasses Style](../../models/RokidAIStyle/README.md):** distinct display-free camera/audio AI eyewear; active investigation, no new stable GLS ID assigned here.
- **Rokid AI Glasses Style Pack:** retail configuration of Style with additional power/accessory capacity; not a second eyewear model.

### Host-driven AR/display systems

- **[Rokid Max 2](../../models/RokidMax2/README.md) — GLS-0094:** current tethered display glasses hardware.
- **[Rokid AR Spatial](../../models/RokidARSpatial/README.md):** Max 2 + Station 2; system/bundle identity, not a separate glasses identity.
- **[Rokid AR Joy 2](../../models/RokidARJoy2/README.md):** Max 2 + original Rokid Station; system/bundle identity, not a separate glasses identity.

Rokid's own AR-series comparison explicitly distinguishes the Station generations and describes bare Max 2 as a connected-device display. Individual storefront pages currently contain Station 2-like compute copy on Max 2 and Joy 2 pages. Preserve that contradiction in provenance rather than treating the repeated storefront module as verified glasses hardware.

## Rokid Glasses — GLS-0064
Integrated AI/AR eyewear. Rokid documents a 49 g frame, Snapdragon AR1 Gen 1 + NXP RT600, 2 GB RAM, 32 GB storage, dual-eye monochrome MicroLED waveguides at 480×640, 30° FOV, up to 1500 nits, 12 MP Sony IMX681 camera, four microphones, dual open-ear speakers, Wi-Fi 6, Bluetooth 5.3, 210 mAh battery, prescription support, translation, navigation, transcription and multimodal AI.

Report-card anchor: H8.5 W8.5 VAI8.5 S8.0 O7.0 OC6.5 CI5.5 Hack6.5 HUD8.5; **V7.5 at $699 sale / V7.0 at $799 regular (US, checked 2026-08-14).**

This is a strong everyday-form-factor HUD/AI product, but many headline AI services remain network/companion dependent. SDK/developer ecosystem is meaningful without approaching open-firmware/hardware benchmarks.

## Service-survival boundary

Rokid's first-party FAQ establishes a meaningful split. Operation and first activation require a phone, wireless internet, Rokid account and Hi Rokid app; account reassignment clears device information, and settings/firmware/media management remain app-mediated. However, six-language offline translation can run after pairing, activation and model download, while Bluetooth phone audio and onboard capture leave plausible residual value.

The correct label is **recoverable with pre-provisioned local translation and phone-peripheral residue; defining AI remains service-dependent**. EV-0047 preserves the complete function table and the sign-out/endpoint-blocked test queue. “Offline” must not be rewritten as account-free or phone-free first use.

## Prescription / optical serviceability
Rokid Glasses use an official magnetic prescription frame. Rokid explicitly states that owners may take that frame to a local optical store and have lenses made by a professional optician. Current FAQ material documents prescription customization from approximately +6.00D to -16.00D and support for myopia and astigmatism, with a lens-curvature constraint for proper fit.

Serviceability state: **ordinary optical shop supported with official carrier/frame**. Rokid also offers a partner lens service, but that partner path is optional rather than the only supported route.

This is materially stronger owner serviceability than vendor-only or certified-partner-only lens replacement.

## Rokid Air / Max display lineage
Host-driven wearable displays. Visual AI is N/A where no wearer-view camera system exists; owner-selected host compute gives strong Cloud Independence and practical Owner Control.

- **Rokid Air — GLS-0092:** H7.0 W7.0 VAI N/A S6.0 O4.0 OC8.0 CI9.0 Hack4.5 HUD7.5 V7.0.
- **Rokid Max — GLS-0093:** H8.0 W7.5 VAI N/A S6.5 O4.0 OC8.5 CI9.5 Hack4.5 HUD8.5 V8.0.
- **Rokid Max 2 — GLS-0094:** H8.5 W8.0 VAI N/A S6.5 O4.0 OC8.5 CI9.5 Hack4.5 HUD9.0 V8.0.

Max 2 additionally supports built-in myopia adjustment from 0.00D to -6.00D plus prescription lens solutions outside that range or for farsightedness/astigmatism. Do not equate diopter adjustment with full prescription service.

## Ownership interpretation
Display-only Rokid products are highly service-independent as host peripherals. Integrated Rokid Glasses provide richer developer/AI capability but are more tied to Rokid software and connected models. The lineage therefore requires architecture-specific rather than brand-wide Cloud Independence scoring.

Style adds a third useful ownership comparison: integrated camera/audio AI eyewear without a display. Its offline residue, SDK exposure, app/account requirements, and service-loss behavior must be tested independently rather than inherited from Rokid Glasses.

## Research priorities

1. Exact offline AI modes, companion/account requirements, and terminal-SDK exposure for Rokid Glasses and Style.
2. Air/Max/Max 2 optical, host, firmware, and generic DisplayPort behavior.
3. Station versus Station 2 hardware/software boundaries, including YodaOS-Master, update paths, sideloading, recovery, and account/network requirements.
4. Current pricing, regional SKUs, prescription-service differences, repairability, battery aging, bootloader/firmware access, and regional restrictions.
5. Capture current first-party pages as dated evidence because storefront copy presently contradicts itself across the AR lineup.
