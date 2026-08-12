# Vuzix Z100 — GLS-0056

Lightweight monocular display glasses built on Vuzix's Ultralite platform.

## Architecture

The Z100 belongs to a different technical branch from Vuzix's standalone Android glasses. Vuzix documents Z100 as a **peripheral device**: a paired mobile device handles application processing and sends instructions to the glasses over Bluetooth. That separation makes Z100 especially relevant to owner-controlled architectures where the intelligence layer can live on a phone or other nearby compute.

See the broader [Vuzix lineage map](../../lineages/VUZIX.md).

## Hardware

Vuzix's primary product and release documentation establishes:

- approximately 38 g weight;
- right-eye 640 × 480 monochrome green display;
- MicroLED waveguide optics;
- approximately 30° field of view;
- Bluetooth Low Energy connectivity;
- prescription insert support;
- manufacturer-claimed runtime up to 48 hours / more than two days depending on use.

## Developer access

The Vuzix Ultralite SDK is available for Android and iOS-family platforms. Vuzix documentation describes APIs for:

- connection state;
- sending/displaying content;
- display/power control;
- tap events;
- battery and charger state.

Vuzix Connect is the official companion application used for pairing and device management.

## GlassesResearch evaluation notes

The documented phone-driven architecture and SDK access are meaningful signals for **Openness**, **Owner Control**, **Cloud Independence**, and **Hackability**. They are not, by themselves, enough to assign final report-card grades. We still need to distinguish what the SDK permits from what requires Vuzix services, determine how much of the pairing/transport stack can be replaced, and verify real-world behavior.

A comparison record already exists for `GLS-0056`; future updates should keep its architecture and lineage fields synchronized with this chapter.

## Primary sources

- [Vuzix Z100 product page](https://www.vuzix.com/products/z100-smart-glasses)
- [Z100 documentation](https://support.vuzix.com/docs/z100-documentation)
- [Ultralite SDK overview](https://support.vuzix.com/docs/overview-28)
- [Android SDK](https://support.vuzix.com/docs/sdk-for-android)
- [Z100 connection guide](https://support.vuzix.com/docs/how-to-connect-to-the-z100)
- [Vuzix Developer Resources](https://support.vuzix.com/docs/developer-resources)

## Related GlassesResearch resources

- [Vuzix lineage](../../lineages/VUZIX.md)
- [Comparison engine](../../docs/COMPARISON_ENGINE.md)
- [Developer resources](../../hacking/README.md)
- [Artifact ledger](../../resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md)
