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

Report-card anchor from the completed batch begins with H8.5 W8.0 VAI8.5; the remaining dimensions should be imported only from the complete scored source rather than guessed from V1. The documented protocol/API expansion itself strongly supports continued high developer-access and owner-control research priority.

## Lineage interpretation
Solos spans audio-only and camera-enabled glasses within one modular ecosystem. Audio-only models have Visual AI and HUD marked N/A. Camera models can support owner-selected downstream processing because official APIs expose capture functions. SDK availability does not prove open firmware, bootloader access or unrestricted exposure of every sensor.

## Cloud independence
Core Bluetooth audio and custom host applications can operate without Solos cloud AI on supported models. Individual vendor AI features, transcription, remote endpoints and network workflows must be scored separately. Custom host control is a genuine positive signal but not proof that every first-party feature is locally self-sufficient.

## Remaining evidence targets
Firmware replacement/boot chain, full sensor exposure, exact offline behavior, subscription/account dependence, repairability, battery aging, prescription serviceability by model, regional differences and long-term service survival remain open.