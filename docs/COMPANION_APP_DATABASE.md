# Companion App Database

Smart glasses are often defined as much by their companion software as by the frames themselves. This database tracks the application layer that controls pairing, permissions, firmware, AI access, media handling, account dependence, and long-term survivability.

The goal is not to list app-store links. It is to answer a harder question: **what software must exist for the hardware to remain useful, and who controls that software?**

## Evidence rules

A row should distinguish between:

- **Officially documented** — stated by the manufacturer or project owner.
- **Hands-on verified** — observed on physical hardware by GlassesResearch.
- **Community observed** — reported by independent users or developers and not yet reproduced here.
- **Inferred relationship** — shared app, package, firmware, protocol, or UI suggests a lineage, but identity is not claimed without stronger evidence.

App names alone are weak evidence. Package identifiers, signing certificates, Bluetooth names, service UUIDs, firmware endpoints, supported-device lists, and preserved installers are stronger.

## Current seed database

| Device / family | Companion software | Required for normal use? | Account / cloud dependence | Developer significance | Research notes |
|---|---|---:|---|---|---|
| Vuzix Z100 | Vuzix Connect on Android; official iOS/Android SDK path | Yes for supported phone-driven operation | Core HUD transport is phone-driven; cloud dependence varies by application | Strong: official SDKs and samples | Important reference case for a documented BLE display peripheral architecture. |
| Solos AirGo family | Solos companion applications; generation-dependent | Yes for supported consumer features | AI and service features vary by generation | Stronger than average: Solos publishes developer SDK material | Do not assume AirGo 3/A5 and AirGo V generations expose identical transports or capabilities. |
| Brilliant Labs Frame | Brilliant Labs software / developer tooling | Needed for supported setup and workflows, but project exposes substantial developer surface | Cloud AI is separable from the underlying open-development posture | Very strong: published hardware/software development material | Useful benchmark for owner-controlled experimentation. |
| Brilliant Labs Halo | Brilliant ecosystem / SDK tooling | Product-generation dependent | Verify delivered local/cloud split per release | Strong: vendor describes an open-source development posture | Shipment state and source completeness should be re-verified at purchase time. |
| Ray-Ban Meta / Meta AI glasses | Meta View / Meta AI ecosystem | Yes for mainstream setup and assistant features | High account and service dependence | Limited compared with open hardware platforms | Consumer scale is high; independent survival is correspondingly more constrained. |
| Even Realities G1/G2 | Even Realities companion ecosystem | Yes for supported consumer features | Product and integration dependent | Public integrations exist; general-purpose hardware access should not be assumed | Prescription-first product design makes app continuity especially important to long-term utility. |
| XREAL One family | XREAL host software and accessories, depending on platform | Not always for basic display use; feature-dependent | Lower cloud dependence for basic display use than AI-assistant glasses | Developer/accessory ecosystem exists | Separate standard video/display survival from proprietary spatial features. |
| MentraOS-compatible devices | MentraOS ecosystem | Depends on device | Designed to reduce application lock-in across supported glasses | Very strong for cross-device experimentation | Compatibility must be tracked by exact device and MentraOS release. |
| HTC VIVE Eagle | VIVE Connect (Android/iOS) | Yes for setup, import/management and advanced AI; button capture works without app open | Advanced VIVE AI requires app connection plus phone internet; camera capture and onboard storage work offline | No broad public hardware SDK documented | [EV-0041](../evidence/EV-0041-HTC-VIVE-Eagle-service-survival.md) separates capture, import, offline commands and cloud AI. Preserve app installers and export media to the ordinary phone library. |
| W610 / HeyCyan retail variants | HeyCyan companion app observed in hands-on work | Vendor-supported workflow appears app-oriented | Exact cloud and account dependencies remain under investigation | No independently verified public SDK yet | Shared app and Bluetooth evidence may help identify OEM/rebrand relationships. Do not infer firmware interchangeability from appearance alone. |

## Fields to capture for each app

Each app record should eventually include the app name, publisher, Android package identifier, iOS bundle identifier when available, signing identity where legally and technically observable, first/last known release, supported glasses, required permissions, account requirement, region restrictions, firmware-update role, media-transfer role, AI-service role, Bluetooth/Wi-Fi transport role, documented API/SDK relationship, preserved installer status, and shutdown/discontinuation status.

## Why this matters

A pair of glasses can remain physically perfect while becoming useless because an app disappears, an account server closes, a certificate expires, or a firmware endpoint is removed. Conversely, hardware that speaks a documented standard or exposes a public SDK may outlive the original product strategy.

For that reason, companion-app continuity should be treated as part of **Owner Control**, **Cloud Independence**, **Hackability**, and **Value** in the GlassesResearch Report Card.
