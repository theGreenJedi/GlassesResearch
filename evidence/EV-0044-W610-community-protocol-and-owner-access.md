# EV-0044 — W610 community protocol and owner-access surface

**Status:** Community-source evidence; physical W610 validation pending  
**Verified against:** CyanBridge / Alternative HeyCyan App and SDK release `v2.1.1`  
**Reviewed:** 2026-08-14  
**Affected scope:** W610 and compatible HeyCyan variants; exact hardware and firmware coverage must be tested per unit

## Question

Does the W610/HeyCyan family expose enough of its transport path for an owner-controlled companion to retrieve media and eventually replace parts of the vendor workflow?

## Finding

The CyanBridge community project documents and implements a concrete independent Android path for compatible HeyCyan glasses:

1. BLE connects to the glasses.
2. A vendor control call with payload `02 01 04` requests transfer mode.
3. A BLE notification whose command byte is `08` carries the glasses' IPv4 address in bytes 7–10.
4. Wi-Fi Direct carries the bulk transfer.
5. The phone reads a plaintext filename manifest from `http://<glasses-ip>/files/media.config`.
6. Individual media objects are downloaded from `http://<glasses-ip>/files/<filename>`.

The same notes describe `02 01 0F` as a Wi-Fi P2P reset command and `09` notifications as P2P/Wi-Fi error reports. They warn that Android's Wi-Fi Direct group-owner address commonly identifies the phone, not the glasses, so the BLE-reported address should be used.

This is materially stronger than merely observing a BLE device name: it identifies a reproducible control-and-transfer architecture and demonstrates that media retrieval need not be confined to the official HeyCyan user interface.

## What this does and does not establish

### Established from the community source

- A community Android application and reusable modules exist.
- BLE is used for connection, state and transfer-mode control.
- Wi-Fi Direct plus local HTTP is used for photos, video and supported recordings.
- The local manifest and media paths are documented.
- The project includes configurable local-model runtimes and an optional OpenAI-compatible remote endpoint.
- Vendor-library calls remain part of the present HeyCyan integration.
- The repository contains vendor artifacts, decompiled reference material and protocol notes whose individual licensing and redistribution status are not uniformly open.

### Not yet established by GlassesResearch hands-on testing

- That Pete's owned W610 revision accepts every documented command.
- The complete GATT service and characteristic inventory.
- Whether the flow works from a clean phone with the official HeyCyan app force-stopped or absent.
- Authentication, authorization or encryption properties of the local HTTP server.
- Firmware image format, signature enforcement, rollback or recovery behavior.
- A vendor-independent reimplementation of all required control calls.
- Coverage across W610 rebrands or other W6xx revisions.

## OTA boundary

CyanBridge's research identifies an app-mediated OTA path using the vendor service at `qlifesnap.com`. Its notes report metadata endpoints, hardware/ROM identifiers and signed or access-controlled `.swu` delivery. The project had not obtained a legitimate firmware payload for the tested revision because the service returned “No upgraded version,” and direct object-store guesses were access denied.

This means the update mechanism is partially mapped but firmware ownership is not established. Do not send speculative OTA payloads to the owned unit until a recovery path exists.

## Safe physical validation gate

1. Preserve the unpaired advertisement and complete GATT inventory.
2. Record hardware, firmware and app versions without publishing private identifiers.
3. Force-stop or remove the official app so it cannot perform the transfer in the background.
4. Capture the BLE request and notification sequence.
5. Confirm the device-reported IP rather than assuming the Wi-Fi group-owner address.
6. Retrieve only `media.config` first; record HTTP headers and whether access is authenticated.
7. Download a known disposable test capture and compare its hash.
8. Test disconnect and P2P reset behavior.
9. Do not attempt OTA until a valid package, integrity checks and recovery procedure are documented.

## Report-card effect

This evidence moves W610 from “BLE observed, developer path unknown” to “community-demonstrated companion and media-transfer path, pending validation on the owned unit.” It supports greater **Hackability** and potential **Owner Control** than the previous record, but it does not justify a score yet because the path still depends on vendor binaries and has not been reproduced by GlassesResearch.

## Sources

- [CyanBridge v2.1.1 repository overview](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/blob/v2.1.1/README.md)
- [HeyCyan Android transfer and OTA notes](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/blob/v2.1.1/android/AGENTS.md)
- [CyanBridge Android companion](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/tree/v2.1.1/android/CyanBridge)
- [HeyCyan core modules](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/tree/v2.1.1/heycyan-core)

## Preservation note

The source tag and exact paths are recorded so the research remains reproducible if the default branch changes. GlassesResearch links to the upstream materials and does not redistribute the repository's vendor AAR, decompiled application, firmware material or other vendor-owned artifacts.
