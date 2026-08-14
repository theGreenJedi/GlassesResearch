# Solos AirGo — populated research record

This record combines the existing Solos developer-evidence framework with generation-specific findings from `docs/report-cards/HIGH_THROUGHPUT_BATCH_01.md`. Primary developer evidence includes the official Solos SDK (`EV-0026`); optical-service evidence is captured in `EV-0037`; modular-repair evidence is in `EV-0041` and [EV-0051](../../evidence/EV-0051-replaceable-power-and-modular-parts-wave-one.md).

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

## Prescription / optical serviceability
Solos accepts externally issued prescriptions and supports custom lens production, including alternate lens indices and finishes. The modular architecture separates front frames from smart temples on supported collections, making optical replacement structurally more practical than on sealed integrated-display eyewear.

Current vendor-primary evidence now confirms **ordinary independent optical service** for supported frames: Solos explicitly says owners may take the glasses to any optical eyewear shop because the lenses are swappable. Vendor-produced prescription lenses remain an optional route. Exact frame compatibility and parts availability are still generation-specific; see [EV-0049](../../evidence/EV-0049-optical-serviceability-wave-six.md).

## Modular electronics / repairability
Solos explicitly documents detachable frame fronts and temples. AirGo V troubleshooting guidance instructs owners to detach the left temple to stop the camera module drawing standby power, confirming that temple removal is an owner-supported physical operation rather than teardown-only access.

Solos currently sells an **AirGo A5 Temple Kit** that attaches to compatible AirGo 3 frame fronts, allowing the smart-electronics temples to be upgraded/replaced without replacing the optical front. Historical manuals also preserve an **AirGo Battery Temple Kit** for AirGo 1.

This supports a genuine **owner-removable modular electronics** classification for specific Solos generations. Do not infer that every AirGo generation has a retail replacement temple/battery module; current policy and product availability remain generation-specific.

## Lineage interpretation
Solos spans audio-only and camera-enabled glasses within one modular ecosystem. Audio-only models have Visual AI and HUD marked N/A. Camera models can support owner-selected downstream processing because official APIs expose capture functions. SDK availability does not prove open firmware, bootloader access or unrestricted exposure of every sensor.

## Cloud independence
Core Bluetooth audio and custom host applications can operate without Solos cloud AI on supported models. AirGo V2 goes further by supporting owner-directed media/events, webhooks, RTMP and private/local endpoints. Individual vendor AI features and transcription services must still be scored separately.

## Remaining evidence targets
Firmware replacement/boot chain, full sensor exposure, exact offline behavior, subscription/account dependence, ordinary-independent optical service by model, temple-kit stock/firmware pairing, battery-cell service by generation, battery aging, regional differences and long-term service survival remain open.