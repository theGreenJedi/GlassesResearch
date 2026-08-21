---
description: "Vuzix Z100 smart-glasses and Ultralite SDK research: phone-driven architecture, Android and iOS developer access, BLE controls, display APIs, owner-control implications, and primary documentation."
---

# Vuzix Z100 smart glasses and Ultralite SDK — GLS-0056

The **Vuzix Z100** is a lightweight monocular display peripheral built on Vuzix's Ultralite platform. Unlike Vuzix's standalone Android smart glasses, the Z100 relies on a paired phone or other mobile device for application processing and uses Bluetooth to receive display instructions.

That architecture makes the Z100 especially relevant to owner-controlled systems: the glasses can remain a lightweight display/interface while the application, AI, memory, and network logic live on hardware chosen by the owner.

See the broader [Vuzix lineage map](../../lineages/VUZIX.md).

## Hardware

Vuzix's primary product and support documentation establishes:

- approximately 38 g weight;
- right-eye 640 × 480 monochrome green display;
- MicroLED waveguide optics;
- approximately 30° field of view;
- Bluetooth Low Energy connectivity;
- prescription insert support;
- manufacturer-claimed runtime up to 48 hours / more than two days depending on use.

## Vuzix SDK / Ultralite SDK

For developers searching for a **Vuzix SDK**, the key distinction is that Z100 uses the **Vuzix Ultralite SDK** rather than the application model used by Vuzix's standalone Android glasses.

Vuzix currently documents SDK support for Android and Apple-family platforms. The documented control surface includes:

- monitoring connection and disconnection state;
- sending text, images, notifications, and simple animations to the display;
- controlling or observing display/power state;
- receiving tap events from the glasses;
- reading battery and charger state.

Vuzix explicitly describes the developer as being in control of the content shown on the Z100 display.

### Android development

Vuzix's current Android SDK documentation requires an Android 12-or-later phone, the **Vuzix Connect** companion application, and Z100 glasses. The Android SDK is intended for connecting an application to the glasses and sending notifications, text, and images.

That companion-app dependency matters to GlassesResearch: the SDK is real developer access, but it does not by itself prove a fully vendor-app-independent Android transport path.

### iOS, watchOS, and macOS development

Vuzix also documents an SDK for iOS-family platforms, with support listed for iOS 14+, watchOS 9+, and macOS 11+ using Swift 5.7+. The same basic model applies: the host device runs the application and the Z100 acts as the wearable display/peripheral.

## What the Z100 is not

The Z100 should not be confused with Vuzix products such as M400/M4000, Blade 2, Shield, or LX1 that run their own applications on the glasses. Vuzix's own developer documentation separates those standalone products from the Z100 peripheral architecture.

That distinction is important when comparing openness or hackability: an SDK for a Bluetooth display peripheral creates a different owner-control surface from installing software directly on an Android-based wearable computer.

## GlassesResearch evaluation notes

The documented phone-driven architecture and SDK access are meaningful signals for **Openness**, **Owner Control**, **Cloud Independence**, and **Hackability**. They are not, by themselves, enough to assign final Report Card grades.

Remaining questions include:

- whether Android pairing/transport can be reproduced without Vuzix Connect;
- how much of the protocol is documented versus hidden behind SDK libraries;
- whether all display and interaction functions work without vendor network services;
- firmware/update independence;
- repairability, optical serviceability, and long-term platform support.

A comparison record already exists for `GLS-0056`; future updates should keep its architecture and lineage fields synchronized with this chapter.

## Primary sources

- [Vuzix Z100 product page](https://www.vuzix.com/products/z100-smart-glasses)
- [Z100 documentation](https://support.vuzix.com/docs/z100-documentation)
- [Ultralite SDK overview](https://support.vuzix.com/docs/overview-28)
- [Android SDK](https://support.vuzix.com/docs/sdk-for-android)
- [iOS SDK](https://support.vuzix.com/docs/sdk-for-ios)
- [Z100 connection guide](https://support.vuzix.com/docs/how-to-connect-to-the-z100)
- [Vuzix developer resources](https://support.vuzix.com/docs/developer-resources)

## Related GlassesResearch resources

- [Vuzix lineage](../../lineages/VUZIX.md)
- [Comparison engine](../../docs/COMPARISON_ENGINE.md)
- [Developer resources](../../hacking/README.md)
- [SDK/API matrix](../../docs/SDK_API_MATRIX.md)
- [Artifact ledger](../../resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md)
