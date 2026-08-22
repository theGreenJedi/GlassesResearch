---
title: "Smart Glasses Bluetooth & BLE Research"
description: "Evidence-tracked Bluetooth Low Energy research for smart glasses: official interfaces, independent protocol work, W610 hands-on investigation, GATT analysis, pairing, control, and media-transfer paths."
---

# Smart Glasses Bluetooth & BLE Research

Last reviewed: **2026-08-21**

## Purpose

Track what Bluetooth and Bluetooth Low Energy actually expose across smart-glasses platforms, while keeping **official interfaces, independent reverse engineering, and GlassesResearch hands-on observations separate**. The W610 remains the detailed hands-on lab on this page; other models provide cross-device reference points where concrete public evidence exists.

Bluetooth support by itself does **not** establish owner control, a public SDK, an open protocol, or offline operation. A device can use BLE while keeping application behavior undocumented and vendor-controlled.

## Cross-device BLE research map

| Device / platform | Evidence lane | What the public evidence establishes | Boundary |
|---|---|---|---|
| **W610 / HeyCyan** | GlassesResearch hands-on + community | Pairing identity observed on owned hardware; CyanBridge documents BLE control/state traffic and a BLE-triggered Wi-Fi Direct media-transfer path | Services, characteristics and transfer commands have not yet been reproduced by GlassesResearch |
| **Even Realities G1** | Community | [`even_glasses`](https://github.com/emingenc/even_glasses) publishes a GPL-3.0 Python package for scanning, connecting and owner-side BLE control experiments | Community implementation, not an Even Realities API contract |
| **Even Realities G2** | Community | [`even-g2-protocol`](https://github.com/i-soxi/even-g2-protocol) documents G2 BLE services, authentication, packet structure and working text-display experiments | Reverse engineering remains incomplete; notifications are partial and navigation/AI remain research areas in the project |
| **Brilliant Labs Frame** | Project-primary | Brilliant Labs publishes direct Bluetooth development and firmware/tooling documentation as part of Frame's developer stack | Published access is unusually open, but individual firmware behavior still belongs to the documented hardware/software revision |
| **Vuzix Z100** | Project-primary | Vuzix documents Bluetooth pairing plus its Ultralite/Android SDK path for application control and device state | Official developer surface; do not transfer Z100 behavior to unrelated Vuzix Android glasses |
| **MentraOS integrations** | Project-primary / community | Cross-device runtime code provides inspectable implementations for multiple supported glasses | Integration code can reuse upstream protocol findings; it is not automatically independent confirmation |

The broader [Open Development Resource Ledger](../hacking/OPEN_HACKING_RESOURCE_LEDGER.md) links the concrete SDKs, protocol projects, firmware repositories and official developer documentation behind these examples.

## Evidence boundary for the W610 lab

Two evidence classes are kept separate:

- **GlassesResearch hands-on:** observations from the owned W610 unit.
- **Community-source:** implementation and protocol claims in CyanBridge v2.1.1, which still require reproduction on the owned hardware.

See [EV-0044](../evidence/EV-0044-W610-community-protocol-and-owner-access.md) for the complete community-source assessment and validation gate.

## Known W610 hands-on baseline

- Observed pairing name: **HeyCyan Glasses**
- Initial pairing attempts were inconsistent.
- More than one Bluetooth-visible device or interface may appear during testing.
- Vendor-app-free investigation is preferred where practical.
- Services, characteristics and command behavior have not yet been enumerated by GlassesResearch.

## Community-mapped W610 transfer path

CyanBridge v2.1.1 documents a working media-transfer architecture for compatible HeyCyan glasses:

| Stage | Community-documented behavior | GlassesResearch status |
|---|---|---|
| Control connection | BLE connects and carries device-control/state traffic | BLE identity observed; control path not reproduced |
| Enter transfer mode | Vendor control payload `02 01 04` | Not reproduced |
| Address notification | Notification command `08`; IPv4 in bytes 7–10 | Not reproduced |
| Bulk network | Wi-Fi Direct | Not reproduced |
| Manifest | `http://<glasses-ip>/files/media.config` | Not reproduced |
| Media | `http://<glasses-ip>/files/<filename>` | Not reproduced |
| P2P reset | Vendor control payload `02 01 0F` | Not reproduced |
| Error notification | Command `09`; `FF` may be noisy/nonfatal | Not reproduced |

The Android Wi-Fi Direct group-owner address may identify the phone rather than the glasses. Testing must prefer the device-reported address and must force-stop the official app to prevent it from silently completing the transfer.

## W610 test environment

| Field | Value |
|---|---|
| Glasses hardware revision | To be documented |
| Phone or host | To be documented |
| Operating system | To be documented |
| BLE inspection tool | To be selected |
| Firmware version | Unknown |

## W610 discovery procedure

1. Fully charge the glasses.
2. Power-cycle the device.
3. Record all advertisements before pairing.
4. Record names, addresses, RSSI, service UUIDs, manufacturer data, and advertising intervals.
5. Pair only after preserving the unpaired baseline.
6. Repeat after button presses, audio activity, charging, and vendor-app interaction.
7. Force-stop the official application before independent-transfer validation.
8. Preserve packet captures with personal device identifiers redacted.

## W610 GATT inventory

| Service UUID | Characteristic UUID | Properties | Observed behavior | Confidence |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | Unverified |

## W610 independent-transfer experiment

1. Capture the BLE request that corresponds to transfer-mode payload `02 01 04`.
2. Confirm whether a notification carrying command `08` returns an IPv4 address.
3. Join the Wi-Fi Direct network without allowing the official app to run.
4. Request only `media.config`; preserve status, headers and response hash.
5. Download one disposable test capture and compare its hash.
6. Record whether the local HTTP surface is authenticated or accessible to any joined peer.
7. Disconnect cleanly; test reset payload `02 01 0F` only after ordinary disconnect behavior is known.

## Experiment log template

### Experiment ID

- Date:
- Tester:
- Device state:
- Host state:
- Action:
- Observed packets or changes:
- Reproduction result:
- Interpretation:
- Confidence:

## Open questions

### W610

- Does the device expose separate classic Bluetooth and BLE roles?
- What are the complete services, characteristics and permissions?
- Which characteristics carry the community-documented control and notify frames?
- Is traffic encrypted after pairing?
- Can the transfer flow be reimplemented without the vendor AAR?
- Is the local HTTP server authenticated or isolated only by Wi-Fi Direct membership?
- Are protocol details shared with other HeyCyan or W6xx products?
- Which behavior varies by hardware and firmware revision?

### Cross-device

- Which products expose an intentionally documented BLE application interface versus only a private companion-app protocol?
- Which owner-side implementations continue working after vendor firmware changes?
- Where does BLE carry the application payload itself, and where does it only bootstrap Wi-Fi, USB, or another bulk-data path?
- Which independent projects have genuinely reproduced the same behavior rather than simply forking the same upstream code?

## Sources

- [EV-0044 — W610 community protocol and owner-access surface](../evidence/EV-0044-W610-community-protocol-and-owner-access.md)
- [CyanBridge v2.1.1 transfer notes](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/blob/v2.1.1/android/AGENTS.md)
- [Even Realities G1 `even_glasses`](https://github.com/emingenc/even_glasses)
- [Even Realities G2 protocol research](https://github.com/i-soxi/even-g2-protocol)
- [Open Development Resource Ledger](../hacking/OPEN_HACKING_RESOURCE_LEDGER.md)
