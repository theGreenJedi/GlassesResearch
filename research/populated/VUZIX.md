# Vuzix — populated research record

Primary evidence includes Z100 documentation (`EV-0016`), Ultralite SDK (`EV-0017`), optical-service evidence (`EV-0038`), Vuzix developer/support resources, `docs/report-cards/BATCH_01.md`, `HIGH_THROUGHPUT_BATCH_05.md`, and [EV-0051](../../evidence/EV-0051-replaceable-power-and-modular-parts-wave-one.md).

## Architecture branches
Vuzix spans a phone-assisted Z100/Ultralite display branch and multiple standalone Android wearable-computer branches. Corporate lineage does not imply shared hardware architecture.

## Z100 / Ultralite
Phone-assisted BLE display peripheral with 640×480 monochrome green microLED waveguide, 30° FoV, ~38 g weight, 2+ day runtime, prescription support, touch input and Android/iOS SDKs. Processing lives primarily on the paired host.

Anchor: H7.5 W9.0 VAI N/A S8.0 O7.5 OC8.0 CI9.5 Hack7.5 HUD8.0 V7.0; $499 general-availability price basis.

### Z100 optical serviceability
Vuzix sells a prescription-insert kit made to the owner's prescription and explicitly describes it as a do-it-yourself lens-change kit. The insert ships separately from the glasses and Vuzix publishes installation guidance.

Serviceability state: **owner-installable prescription insert**. This is stronger than vendor-return-only service, although it is not the same as an ordinary optician cutting directly into the electronics-bearing frame.

## Blade 2 — GLS-0055
Enterprise-oriented standalone Android smart glasses with right-eye 480×480 full-color waveguide display (~20° FOV), autofocus HD camera, stereo speakers, noise-cancelling microphones, Wi-Fi/Bluetooth, touch/voice interaction and Android/Vuzix developer tooling.

Report-card anchor: H8.0 W7.0 VAI7.0 S8.5 O8.0 OC8.0 CI8.5 Hack8.0 HUD7.0; Value not yet graded.

Blade 2 is more glasses-like than the head-mounted M-series while retaining meaningful Android application control. Firmware-level openness remains below Brilliant-class benchmarks.

### Blade 2 optical serviceability
Vuzix lists Blade 2 prescription lenses and publishes an owner installation guide. The prescription assembly is installed by removing the nose-bridge screw and fitting the replacement prescription frame assembly.

Serviceability state: **owner-installable specialist insert/frame assembly**.

## Standalone Android M/LX1/Shield generations
- **M100 — GLS-0095:** H4.5 W3.5 VAI3.5 S4.5 O5.0 OC6.0 CI8.0 Hack5.5 HUD4.0; Value not yet graded.
- **M300 — GLS-0096:** H6.0 W4.5 VAI5.5 S6.0 O6.5 OC7.0 CI8.5 Hack6.5 HUD5.0; Value not yet graded.
- **M300XL — GLS-0097:** H6.5 W4.5 VAI6.0 S6.0 O6.5 OC7.0 CI8.5 Hack6.5 HUD5.0; Value not yet graded. Developer treatment is substantially shared with M300; XL changes battery connection and camera behavior.
- **M400 — GLS-0098:** H8.0 W5.5 VAI7.5 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD6.0; Value not yet graded.
- **M4000 — GLS-0099:** H8.0 W5.5 VAI7.5 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD7.0; Value not yet graded.
- **LX1 — GLS-0100:** H8.0 W4.5 VAI6.5 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD6.5; Value not yet graded.
- **Shield — GLS-0121:** H8.5 W6.5 VAI8.0 S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD8.5; Value not yet graded.

The M400/M4000 values above retain the later standardized high-throughput calibration rather than silently replacing it with earlier Batch 02 scores that used a more generous application-openness interpretation.

M400/M4000 use Qualcomm XR1, 6 GB RAM, 64 GB storage, 12.8 MP/4K camera, orientation sensors, triple microphones, touch/buttons/voice and standard Android application deployment. M400 uses occluded 640×360 OLED; M4000 uses 854×480 see-through waveguide. Vuzix View supports APK installation with USB debugging.

### M400 / M4000 / LX1 battery and parts serviceability

M400 and M4000 use an external runtime battery and support true hot swapping through a small internal bridge cell. Vuzix currently sells compatible rail-mounted 3200 mAh and 4800 mAh packs, and its support documentation says a suitable 1.5 A supply can power the devices. This establishes **owner-replaceable runtime power** but not serviceability of the internal bridge cell.

LX1 uses a current 7000 mAh long-shift clip-in battery with a separately available multi-battery charger. Combined with its easy-release mount and current accessory sales, LX1 has **owner-removable runtime power and mounting modules**. Neither finding proves board, display, camera or internal-cell repairability.

LX1 is a 2026 warehouse-focused Android 15 system with 7000 mAh long-shift battery, rugged/freezer-oriented design and NFC pairing. Shield uses Snapdragon XR1, binocular full-color microLED waveguides, stereo HD cameras and prescription-ready safety-glasses framing.

## Ownership interpretation
Vuzix is unusually owner-controllable for commercial enterprise eyewear because standard Android app development, APK installation, sensor APIs and Vuzix SDKs are real. Owner-installable prescription systems on Z100 and Blade 2 add a separate, practical ownership advantage. This remains proprietary hardware: application programmability must not be inflated into open firmware/schematics or unrestricted bootloader access.

## Cloud independence
Z100 is host-dependent rather than inherently cloud-dependent; standalone Android products can run local applications. Vendor cloud/licensing features remain model-specific, but core functionality has strong local architecture.

## Research priorities
Current prices, bootloader/firmware access, exact sensor exposure, internal bridge-cell service, board/display repair, support horizon and service/account dependencies by model.