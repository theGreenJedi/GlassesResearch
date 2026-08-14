# Solos AirGo — populated research record

This record combines the existing Solos developer-evidence framework with generation-specific findings from `docs/report-cards/HIGH_THROUGHPUT_BATCH_01.md`. Primary developer evidence includes the official Solos SDK (`EV-0026`).

## AirGo 2 — GLS-0026
Audio-first predecessor. Existing research documents Bluetooth 5.0/BLE, Android/iOS support, roughly 11 hours music, eight hours calls, quick charging and prescription-compatible frame options. The current Solos SDK does not list AirGo 2 among supported targets.

Report-card anchor: H6.0 W7.5 VAI N/A S5.5 O4.0 OC5.5 CI8.5 Hack4.5 HUD N/A; Value not yet graded.

## AirGo 3 — GLS-0027
Solos documents ~39 g examples, Bluetooth 5.2/BLE, IP67, ~10 hours music/seven hours calls and an official SDK exposing audio I/O, motion, compass and touch APIs.

Report-card anchor: H7.5 W8.5 VAI N/A S8.0 O7.5 OC8.0 CI8.5 Hack7.5 HUD N/A; Value not yet graded.

Developer access materially improves application-level owner control, while firmware/bootloader access remains unestablished.

## AirGo Vision / AirGo V — GLS-0028
Camera-enabled generation on the shared mobile development platform. Official SDK access includes audio, sensors, touch, photo-taking and photo-streaming functions. Visual AI is applicable because owners/developers can route imagery into downstream processing rather than being limited to a single vendor assistant.

Report-card anchor: H7.5 W8.0 VAI8.0 S8.5 O8.0 OC8.5 CI8.5 Hack8.0 HUD N/A; Value not yet graded.

## AirGo V2 — GLS-0029
Expanded camera generation with video recording/streaming, Wi-Fi data transport, BLE control, voice-command, firmware-update, webhook and RTMP pathways while retaining V1 APIs.

Report-card anchor: H8.5 W8.0 VAI8.5 S9.0 O8.5 OC9.0 CI9.0 Hack8.5 HUD N/A; Value not yet graded.

The documented protocol/API expansion makes V2 one of the catalog's strongest officially supported screen-free development platforms below fully open hardware.

## Lineage interpretation
Solos spans audio-only and camera-enabled glasses within one modular ecosystem. Audio-only models have Visual AI and HUD marked N/A. Camera models can support owner-selected downstream processing because official APIs expose capture functions. SDK availability does not prove open firmware, bootloader access or unrestricted exposure of every sensor.

## Cloud independence
Core Bluetooth audio and custom host applications can operate without Solos cloud AI on supported models. AirGo V2 goes further by supporting owner-directed media/events, webhooks, RTMP and private/local endpoints. Individual vendor AI features and transcription services must still be scored separately.

## Remaining evidence targets
Firmware replacement/boot chain, full sensor exposure, exact offline behavior, subscription/account dependence, repairability, battery aging, prescription serviceability by model, regional differences and long-term service survival remain open.