# Vuzix smart-glasses lineages

Vuzix spans several materially different smart-glasses architectures. GlassesResearch therefore tracks Vuzix as a **corporate lineage with multiple technical branches**, not as one homogeneous hardware platform.

## Z100 / Ultralite peripheral-display branch

**Relationship type:** corporate + protocol/software lineage  
**Confidence:** Confirmed

Vuzix documents the Z100 as a peripheral device connected to a mobile device; the phone performs application processing and sends instructions over Bluetooth. Vuzix provides Android and iOS development paths for this branch.

Canonical model: [Vuzix Z100](../models/VuzixZ100/README.md) (`GLS-0056`).

## Android standalone wearable-computer branch

**Relationship type:** corporate + software/developer lineage  
**Confidence:** Confirmed

Vuzix documents the **M400, M4000, Blade 2, LX1, and Shield** as standalone devices that do not require an outside connection. They are largely Android-based wearable computers, with standard Android APIs plus Vuzix SDKs for speech, barcode scanning, connectivity, and HUD-oriented interfaces.

Model chapters:

- [M400 / M4000](../models/VuzixM400/README.md)
- [Blade 2](../models/VuzixBlade2/README.md)
- [Shield](../models/VuzixShield/README.md)
- [LX1](../models/VuzixLX1/README.md)

The Connectivity SDK supports communication between Android phone applications and applications running on M400, M4000, Shield, Blade, and Blade 2 devices. Vuzix also publishes HUD Action Menu resources for these Android-enabled glasses.

## Legacy Android enterprise branch

Earlier Android enterprise products such as M300/M300XL remain historically relevant. Vuzix maintains migration and development documentation for them. GlassesResearch should preserve them as predecessors to the M400 generation rather than treating them as current equivalents.

## Why the branches stay separate

The Z100 architecture pushes application processing to a paired phone, while the M400/M4000/Blade 2/Shield/LX1 branch can run applications on the glasses themselves. That difference directly affects Hardware, Software, Openness, Owner Control, Cloud Independence, and Hackability.

Corporate ownership alone is therefore not enough to collapse the models into one technical lineage.

## Developer ecosystem signals

Primary documentation establishes standard Android development for the standalone branch; Vuzix Speech, Barcode, Connectivity, and HUD resources; Wi-Fi/Bluetooth/BLE communication options; USB debugging and APK installation through Vuzix View for supported Android models; and Android/iOS development paths for Z100.

These are strong research signals, but GlassesResearch does not convert them automatically into report-card grades. Model-specific limits, licensing, cloud dependencies, bootloader/firmware access, and real-world owner control still require evidence.

## Primary sources

- [Vuzix Developer Resources](https://support.vuzix.com/docs/developer-resources)
- [Vuzix support device index](https://support.vuzix.com/)
- [Vuzix Connectivity SDK](https://github.com/Vuzix/connectivity-sdk)
- [Vuzix HUD Action Menu SDK](https://github.com/Vuzix/hud-actionmenu)
- [Vuzix View functionality](https://support.vuzix.com/docs/vuzix-view-functionality)
- [Blade / Blade 2 downloads](https://support.vuzix.com/docs/blade-downloads-2)
- [M300 legacy developer documentation](https://support.vuzix.com/docs/m300)

## Related GlassesResearch layers

- [The List](../models/THE_LIST.md)
- [Model Registry](../models/CATALOG.md)
- [Comparison engine](../docs/COMPARISON_ENGINE.md)
- [Open Development Resource Ledger](../hacking/OPEN_HACKING_RESOURCE_LEDGER.md)
- [Research & News](../docs/RESEARCH_NEWS.md)
