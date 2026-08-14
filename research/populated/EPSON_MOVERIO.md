# Epson Moverio — populated research record

Source basis: `docs/report-cards/HIGH_THROUGHPUT_BATCH_06.md`, Epson product/support releases and the Moverio technical/SDK portal cited there.

## Lineage
BT-100 → BT-200 → BT-300 → BT-30C / BT-35E → BT-40/40S → BT-45C/45CS. The lineage evolves from self-contained Android/controller AR toward modern USB-C host-driven and enterprise sensing architectures.

## Report-card anchors
- **BT-100 — GLS-0106:** H5.0 W4.0 VAI N/A S5.0 O4.0 OC6.0 CI7.5 Hack4.5 HUD5.5 V4.5.
- **BT-200 — GLS-0107:** H6.0 W5.5 VAI4.0 S6.0 O6.0 OC7.0 CI8.0 Hack6.5 HUD6.0 V5.5.
- **BT-300 — GLS-0108:** H7.0 W7.0 VAI5.5 S7.0 O6.5 OC7.0 CI8.0 Hack6.5 HUD7.0 V6.5.
- **BT-30C — GLS-0109:** H6.5 W7.5 VAI N/A S6.5 O6.5 OC8.0 CI9.5 Hack6.5 HUD7.0 V7.0.
- **BT-35E — GLS-0110:** H7.0 W6.5 VAI5.5 S7.0 O7.0 OC8.0 CI9.0 Hack7.0 HUD7.0 V6.5.
- **BT-40 / BT-40S — GLS-0111:** H7.5 W7.0 VAI N/A S7.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD8.0 V7.0.
- **BT-45C / BT-45CS — GLS-0112:** H8.5 W6.5 VAI7.0 S8.0 O7.5 OC8.5 CI9.0 Hack7.5 HUD8.5 V7.5.

## Generational interpretation
BT-100 established self-contained Android binocular see-through AR with separate controller, Wi-Fi/removable storage and ~6-hour battery. BT-200 added 960×540 binocular display, 23° FOV, camera, microphone, GPS/motion sensors, Bluetooth/Wi-Fi and a stronger developer posture. BT-300 moved to much lighter Si-OLED AR.

BT-30C changes ownership architecture by acting mainly as a USB-C DisplayPort wearable display: host choice becomes central and cloud independence becomes especially strong. BT-35E adds camera/sensor access. BT-40/40S continue the modern tethered architecture with Epson's Basic Function SDK.

BT-45C/45CS is the strongest entry in the packet: binocular Full-HD Si-OLED, 34° FOV, centered 8 MP autofocus camera, motion/environment sensors, integrated audio on BT-45C, USB-C host support, IP52, industrial mounts and Android/Windows SDK access to display, sensors, camera and audio.

## Ownership interpretation
Moverio offers substantial supported application/developer access, especially in later enterprise models. That does not imply open firmware/schematics. Host-driven generations score particularly well for practical owner control and service-independent core display use.

## Research priorities
Current support horizon, firmware/bootloader access, exact host compatibility, repairability, optical/prescription support, battery/parts aging and historical acquisition-value verification.