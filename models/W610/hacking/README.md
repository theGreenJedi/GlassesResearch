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

## Safety boundary

Research must be limited to owned or explicitly authorized devices and services. Do not publish credentials, private user traffic, unlawfully obtained firmware, or procedures intended to compromise another person's device or account.
