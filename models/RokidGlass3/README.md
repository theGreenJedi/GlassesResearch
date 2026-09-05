# Rokid Glass 3 — GLS-0184

Rokid Glass 3 is Rokid's current enterprise smart-glasses generation, with its own hardware model numbers, enterprise operating environment, developer documentation, and procurement path.

**Technology lineage:** [Rokid](../../lineages/ROKID.md)  
**Catalog state:** canonical — `GLS-0184`  
**Evidence state:** current first-party developer/manual/security documentation + current enterprise commercial availability; hands-on verification pending

## Identifiers / also known as

- Official product name: **Rokid Glass 3** / **Rokid Glass3**
- Manufacturer model numbers: **RG301**, **RG303**
- Operating environment documented by Rokid: **YodaOS-Sprite Enterprise**

## Why Glass 3 is a distinct generation

Rokid's current developer documentation explicitly requires a **Rokid Glass 3 device** and publishes separate glasses-side and phone-side demo projects. The current enterprise manual names Glass 3 and documents generation-specific features. Rokid's security center separately lists Glass 3 with model numbers RG301/RG303 and a 2026 release/support period.

That establishes a current enterprise generation distinct from Rokid Glass 2, current consumer Rokid Glasses, and the display-free RV203 family.

## Manufacturer-documented signals

Current first-party material documents, among other items:

- MicroLED + diffractive-waveguide display architecture;
- 480 × 640 display specification in the enterprise manual;
- approximately 30° field of view;
- approximately 1500-nit brightness claim in the enterprise manual;
- approximately 50 g class weight;
- YodaOS-Sprite Enterprise;
- glasses-side application execution;
- Bluetooth and Wi-Fi/P2P communication with a phone-side companion;
- camera, microphone, media capture, notification sync and OTA capabilities exposed through Rokid's current developer workflow;
- enterprise workflows including offline face/vehicle recognition, work assistance, remote collaboration and device-management functions in the enterprise manual.

Some regional sales pages publish conflicting display terminology/resolution. Those reseller conflicts should remain secondary until reconciled against the first-party manual and physical hardware.

## Developer / owner-control significance

Rokid's current demo guide is unusually useful evidence because it tells developers to connect Glass 3 to Android Studio with a dedicated data/debug cable and run the glasses-side demo directly on the device. It also documents Bluetooth messaging, file transfer, Wi-Fi P2P, media capture/preview and OTA-related capabilities.

This is a materially different research surface from consumer Rokid Glasses and should receive its own openness, owner-control, cloud-independence and hackability testing.

## Investigation queue

1. Preserve and hash the Glass 3 enterprise manual and SDK/demo repository.
2. Verify Android/YodaOS build, ADB behavior, package installation, signing restrictions and bootloader state.
3. Map RG301 versus RG303 regional/enterprise differences.
4. Separate local/offline enterprise recognition features from server/platform-dependent functions.
5. Characterize camera, audio, display, sensors, storage and battery hands-on.
6. Determine ordinary use after Rokid enterprise services are unavailable.
7. Produce a generation-specific report card; do not inherit Glass 2 or Rokid Glasses scores.

## Primary sources

- [Rokid Glass 3 demo/developer guide](https://x-docs.rokid.com/docs/en/downloads/demo-guide.html)
- [Rokid Glass 3 enterprise manual](https://x-docs.rokid.com/lingmou_manual.pdf)
- [Rokid security center](https://global.rokid.com/pages/security-center)

## Related GlassesResearch resources

- [Rokid lineage](../../lineages/ROKID.md)
- [Rokid historical audit](../../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
- [Rokid populated research record](../../research/populated/ROKID.md)
