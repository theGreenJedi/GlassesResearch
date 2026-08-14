# Vuzix — populated research record

Primary evidence includes Z100 documentation (`EV-0016`), Ultralite SDK (`EV-0017`), Vuzix developer/support resources and `docs/report-cards/HIGH_THROUGHPUT_BATCH_05.md`.

## Architecture branches
Vuzix spans a phone-assisted Z100/Ultralite display branch and standalone Android wearable-computer branches. Corporate lineage does not imply shared hardware architecture.

## Z100 / Ultralite
Phone-assisted BLE display peripheral with 640×480 monochrome green microLED waveguide, 30° FoV, ~38 g weight, 2+ day runtime, prescription support, touch input and Android/iOS SDKs. Processing lives primarily on the paired host.

Anchor from completed research: H7.5 W9.0 VAI N/A S8.0 O7.5 OC8.0 CI9.5 Hack7.5 HUD8.0 V7.0; $499 general-availability price basis.

## Standalone Android generations
- **M100 — GLS-0095:** H4.5 W3.5 VAI3.5 S4.5 O5.0 OC6.0 CI8.0 Hack5.5 HUD4.0; Value not yet graded.
- **M300 — GLS-0096:** H6.0 W4.5 VAI5.5 S6.0 O6.5 OC7.0 CI8.5 Hack6.5 HUD5.0; Value not yet graded.
- **M300XL — GLS-0097:** H6.5 W4.5 VAI6.0 S6.0 O6.5 OC7.0 CI8.5 Hack6.5 HUD5.0; Value not yet graded. Developer treatment is substantially shared with M300; XL changes battery connection and camera behavior.
- **M400 — GLS-0098:** H8.0 W5.5 VAI7.5 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD6.0; Value not yet graded.
- **M4000 — GLS-0099:** H8.0 W5.5 VAI7.5 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD7.0; Value not yet graded.
- **LX1 — GLS-0100:** H8.0 W4.5 VAI6.5 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD6.5; Value not yet graded.
- **Shield — GLS-0121:** H8.5 W6.5 VAI8.0 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD8.5; Value not yet graded.

M400/M4000 are a major platform step: Qualcomm XR1, 6 GB RAM, 64 GB storage, 12.8 MP/4K camera, orientation sensors, triple microphones, touch/buttons/voice and standard Android application deployment. M400 uses an occluded 640×360 OLED; M4000 uses an 854×480 see-through waveguide. Vuzix View supports APK installation with USB debugging.

LX1 is a 2026 warehouse-focused Android 15 system with 7000 mAh long-shift battery, rugged/freezer-oriented design and NFC pairing. Shield uses Snapdragon XR1, binocular full-color microLED waveguides, stereo HD cameras and prescription-ready safety-glasses framing.

## Ownership interpretation
Vuzix is unusually owner-controllable for commercial enterprise eyewear because standard Android app development, APK installation, sensor APIs and Vuzix SDKs are real. This is still proprietary hardware: application programmability must not be inflated into open firmware/schematics or unrestricted bootloader access.

## Cloud independence
Z100 is host-dependent rather than inherently cloud-dependent; standalone Android products can run local applications. Vendor cloud/licensing features remain model-specific, but core functionality has strong local architecture.

## Research priorities
Current prices, bootloader/firmware access, exact sensor exposure, prescription service paths, battery/parts repairability, support horizon and service/account dependencies by model.