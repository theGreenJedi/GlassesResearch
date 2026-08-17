---
title: "Smart Glasses Bluetooth & BLE Research"
description: "Hands-on and community-sourced Bluetooth Low Energy research for smart glasses, including W610/W6xx discovery, pairing, GATT analysis, protocol testing, and media-transfer investigation."
---

# Smart Glasses Bluetooth & BLE Research

## Purpose

Record repeatable BLE discovery, pairing, service enumeration, characteristic testing, and protocol analysis for W610/W6xx-family devices.

## Evidence boundary

Two evidence classes are kept separate:

- **GlassesResearch hands-on:** observations from the owned W610 unit.
- **Community-source:** implementation and protocol claims in CyanBridge v2.1.1, which still require reproduction on the owned hardware.

See [EV-0044](../evidence/EV-0044-W610-community-protocol-and-owner-access.md) for the complete community-source assessment and validation gate.

## Known hands-on baseline

- Observed pairing name: **HeyCyan Glasses**
- Initial pairing attempts were inconsistent.
- More than one Bluetooth-visible device or interface may appear during testing.
- Vendor-app-free investigation is preferred where practical.
- Services, characteristics and command behavior have not yet been enumerated by GlassesResearch.

## Community-mapped transfer path

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

## Test environment

| Field | Value |
|---|---|
| Glasses hardware revision | To be documented |
| Phone or host | To be documented |
| Operating system | To be documented |
| BLE inspection tool | To be selected |
| Firmware version | Unknown |

## Discovery procedure

1. Fully charge the glasses.
2. Power-cycle the device.
3. Record all advertisements before pairing.
4. Record names, addresses, RSSI, service UUIDs, manufacturer data, and advertising intervals.
5. Pair only after preserving the unpaired baseline.
6. Repeat after button presses, audio activity, charging, and vendor-app interaction.
7. Force-stop the official application before independent-transfer validation.
8. Preserve packet captures with personal device identifiers redacted.

## GATT inventory

| Service UUID | Characteristic UUID | Properties | Observed behavior | Confidence |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | Unverified |

## Independent-transfer experiment

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

- Does the device expose separate classic Bluetooth and BLE roles?
- What are the complete services, characteristics and permissions?
- Which characteristics carry the community-documented control and notify frames?
- Is traffic encrypted after pairing?
- Can the transfer flow be reimplemented without the vendor AAR?
- Is the local HTTP server authenticated or isolated only by Wi-Fi Direct membership?
- Are protocol details shared with other HeyCyan or W6xx products?
- Which behavior varies by hardware and firmware revision?

## Sources

- [EV-0044 — W610 community protocol and owner-access surface](../evidence/EV-0044-W610-community-protocol-and-owner-access.md)
- [CyanBridge v2.1.1 transfer notes](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/blob/v2.1.1/android/AGENTS.md)
