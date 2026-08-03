# Bluetooth Low Energy

## Purpose

Record repeatable BLE discovery, pairing, service enumeration, characteristic testing, and protocol analysis for W610/W6xx-family devices.

## Known baseline

- Observed pairing name: **HeyCyan Glasses**
- Initial pairing attempts were inconsistent.
- More than one Bluetooth-visible device or interface may appear during testing.
- Vendor-app-free investigation is preferred where practical.

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

## GATT inventory

| Service UUID | Characteristic UUID | Properties | Observed behavior | Confidence |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | Unverified |

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
- Which characteristics control capture, playback, buttons, status, or configuration?
- Is traffic encrypted after pairing?
- Can the glasses be controlled without the vendor application?
- Are protocol details shared with other HeyCyan or W6xx products?
