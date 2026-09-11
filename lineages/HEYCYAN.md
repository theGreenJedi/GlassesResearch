---
description: "HeyCyan and CyanBridge smart-glasses lineage research covering W610, Anko, BLE, alternative companion software, owner control, and compatibility boundaries."
---

# HeyCyan / CyanBridge smart-glasses lineage

The HeyCyan lineage groups smart glasses that are documented to participate in the same **HeyCyan software ecosystem**. This is a software/ecosystem lineage first. It does not imply that every member shares the same PCB, enclosure, ODM, firmware image, or manufacturer.

## CyanBridge and the alternative HeyCyan software path

**CyanBridge** is an independent community companion application and SDK for HeyCyan-compatible smart glasses. It matters because it demonstrates that at least part of the HeyCyan ecosystem can be used outside the stock vendor experience, including Bluetooth/BLE interaction, media handling, diagnostics, and owner-selected downstream AI endpoints.

Current GlassesResearch evidence for CyanBridge includes:

- the public [CyanBridge / Alternative HeyCyan App and SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK) project;
- its [release history](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases);
- documented W610/HeyCyan media-transfer and owner-access research;
- CyanBridge v2.1.1 support for remote OpenAI-compatible endpoints, including owner-controlled servers reachable over private networking.

That is strong evidence for **companion-level openness and owner control**. It is not evidence that every HeyCyan-branded or marketplace rebrand is protocol-compatible, and it does not establish open firmware, an unlocked boot chain, or unrestricted low-level sensor access.

See the [W610 research page](../models/W610/README.md) and [W610 community resources](../models/W610/COMMUNITY_MAP.md) for the deeper protocol and owner-control trail.

## Current confirmed members

| Model | GlassesResearch ID | Relationship | Confidence |
|---|---|---|---|
| [W610](../models/W610/README.md) | GLS-0039 | Device identifies as `HeyCyan Glasses`; community SDK and companion-stack research target HeyCyan-compatible hardware | Confirmed software/ecosystem relationship |
| [Anko Camera Glasses](../models/AnkoCameraGlasses/README.md) | GLS-0120 | Contemporary retail reporting identifies HeyCyan as the software platform | Confirmed software/ecosystem relationship |

Other W6xx and marketplace products may belong to this lineage, but each device is added only when evidence establishes the relationship.

## Owner-reported lineage candidates

These are useful compatibility fingerprints, not confirmed lineage assignments.

| Candidate | Public evidence | Status |
|---|---|---|
| `CY01` | A September 2026 CyanBridge issue participant reported a repeatable Wi-Fi Direct test on a CY01 specimen and a capability response with `supportLiveReview = false`. | COMMUNITY-REPORTED / owner-tested. Keep separate from Eyevue and W610 until stronger identity evidence exists. |
| Bluetooth `X01_C4E4`; `AX01_V1.0`; firmware `1.00.34_260721`; `WIFIAX01_V1.0`; Wi-Fi firmware `3.00.07_2602021600A01`; HeyCyan app `1.0.142_20260807` | Exact owner-provided hardware/software tuple in CyanBridge issue #16. | COMMUNITY-REPORTED identity fingerprint. Do not equate it with another HeyCyan device without corroboration. |

Primary public records: [CyanBridge issue #5](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/issues/5) and [issue #16](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/issues/16).

## What is shared

The strongest common denominator currently documented is the HeyCyan companion/software environment. Public community work also demonstrates an alternative development ecosystem around HeyCyan-compatible glasses, including BLE interaction and independent companion applications.

- [HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK)
- [CyanBridge / Alternative HeyCyan App and SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK)
- [CyanBridge releases](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases)

## Current-model view

The lineage currently spans at least two very different retail routes: marketplace/OEM-style W610 products and a mass-market Anko/Kmart retail product. That makes the lineage useful for studying how one software platform can surface under unrelated consumer brands.

## Strengths

- Low-cost hardware appears across multiple retail channels.
- A public community development ecosystem exists outside the vendor application.
- Shared software creates a practical basis for cross-model protocol and compatibility research.
- White-label/rebrand behavior makes the lineage especially valuable for identifying hidden relationships across the market.

## Weaknesses

- Brand names often reveal little about the underlying hardware origin.
- Software compatibility alone cannot establish hardware identity or common manufacture.
- Public technical documentation is uneven, making regulatory, firmware, BLE, teardown, and hands-on evidence important.

## Best-fit use cases

- Budget camera/audio smart glasses.
- Open-development and reverse-engineering research.
- OEM/rebrand lineage analysis.
- Testing whether community companion software can reduce dependence on vendor applications.

## Compatibility questions tracked across the lineage

GlassesResearch will distinguish each of these rather than collapsing them into a single claim of compatibility:

- companion-app compatibility
- BLE protocol compatibility
- media-transfer compatibility
- SDK/API compatibility
- firmware/update compatibility
- charging and accessory compatibility
- lens/frame compatibility
- PCB/component commonality
- confirmed ODM/OEM relationships

## Research direction

The main unanswered question is not whether W610 and Anko both touch HeyCyan—that relationship is documented—but **how deep the shared lineage goes**. Future evidence should determine whether specific members share protocols, firmware branches, chipsets, boards, charging systems, mechanical designs, or ODM sources.

The new CY01 and AX01/WIFIAX01 reports should be used as comparison targets for exact model labels, firmware/build identification, Bluetooth service inventories, capability responses, and controlled cross-device compatibility work.

## Community

See the ecosystem-wide [Community & Development](../resources/COMMUNITY_AND_DEVELOPMENT.md) directory and the model-specific [W610 community resources](../models/W610/COMMUNITY_MAP.md).
