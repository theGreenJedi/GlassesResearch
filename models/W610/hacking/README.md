# W610 Open-Hacking Dossier

This dossier tracks lawful owner-control, interoperability, preservation, and modification research for the W610 and closely related HeyCyan-branded variants.

## Verified Working

The entries below are limited to behavior directly observed on the current hands-on unit. They establish a reproducible control baseline; they do **not** yet establish custom firmware, vendor-app replacement, or protocol control.

### Power-on control

- **Status:** Verified Working
- **Model:** HeyCyan W610 retail variant
- **Hardware revision:** Not yet identified
- **Firmware version:** Not yet identified
- **Date verified:** 2026-08-02
- **Method:** Physical device test
- **Procedure:** Press and hold the rear button on the right temple until the startup response occurs.
- **Expected result:** Startup tone, brief status-LED activity near the hinge, and the device becomes discoverable.
- **Evidence state:** Personally reproduced on the hands-on unit.
- **Risk:** Low
- **Limitations:** Button timing and behavior may vary across revisions.

### Bluetooth advertising identity

- **Status:** Verified Working
- **Model:** HeyCyan W610 retail variant
- **Hardware revision:** Not yet identified
- **Firmware version:** Not yet identified
- **Date verified:** 2026-08-02
- **Method:** Phone Bluetooth discovery
- **Procedure:** Power on the glasses and scan for nearby Bluetooth devices.
- **Expected result:** A device advertising as `HeyCyan Glasses` appears.
- **Evidence state:** Personally reproduced on the hands-on unit.
- **Risk:** Low
- **Limitations:** This confirms advertising identity only. It does not document services, characteristics, commands, audio profiles, or pairing reliability.

### Vendor-app-free initial observation

- **Status:** Verified Working
- **Model:** HeyCyan W610 retail variant
- **Date verified:** 2026-08-02
- **Method:** Controlled baseline setup
- **Result:** The unit can be powered on and detected by a phone without first installing the vendor companion application.
- **Evidence state:** Personally reproduced.
- **Risk:** Low
- **Limitations:** This does not prove that all functions operate without the vendor app.

## Not Verified Yet

The following are preserved as research targets only. They are **not instructions** and must not be represented as working capabilities until qualifying tests are completed.

| Research target | Current status | Verification needed |
|---|---|---|
| Enumerate BLE GATT services and characteristics | Not Verified Yet | Capture from identified hardware and firmware; repeat scan; preserve raw output |
| Identify writable BLE controls | Not Verified Yet | Controlled writes with packet capture, expected-response record, and rollback |
| Replace the vendor assistant | Not Verified Yet | Demonstrate an open client performing a defined function without vendor-cloud dependence |
| Use a third-party or community companion app | Not Verified Yet | Reproduce installation, pairing, function, and recovery on the hands-on unit |
| Obtain and preserve firmware packages | Not Verified Yet | Establish lawful source, hashes, model compatibility, and retrieval date |
| Flash community or modified firmware | Not Verified Yet | Verified image provenance, exact revision match, successful flash, and tested recovery path |
| Replace embedded AI models | Not Verified Yet | Identify where inference runs, model format, deployment path, and reproducible result |
| Capture microphone or camera data through an open interface | Not Verified Yet | Authorized capture with documented protocol and privacy controls |
| Operate core functions entirely offline | Not Verified Yet | Define core functions and reproduce them with network isolation |
| Recover from failed update or flash | Not Verified Yet | Repeatable recovery method tested on matching hardware |
| Identify ODM/rebrand compatibility | Not Verified Yet | Hardware, firmware, protocol, and accessory comparison across physical units |
| Prescription-lens or optics workarounds | Not Verified Yet | Dimensional verification, fit test, optical safety review, and repeatability |

## Verification priorities

1. Record hardware and firmware identifiers without altering the device.
2. Capture complete Bluetooth advertisements and service enumeration.
3. Establish pairing behavior and profiles on a controlled phone.
4. Preserve raw evidence before interpreting packet behavior.
5. Test one reversible command at a time.
6. Document recovery before attempting firmware writes.
7. Promote only successfully reproduced procedures into Verified Working.

## Required evidence paths

Future experiments should preserve material under the W610 chapter:

```text
models/W610/evidence/
models/W610/ble/
models/W610/firmware/
models/W610/software/
models/W610/research-log/
```

Each experiment should include date, device identity, tool versions, raw output, interpretation, result, and contradictory observations.

## Safety boundary

Research must be limited to owned or explicitly authorized devices and services. Do not publish credentials, private user traffic, unlawfully obtained firmware, or procedures intended to compromise another person's device or account.