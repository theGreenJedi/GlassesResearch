# Brilliant Labs — populated research record

Primary evidence: Frame hardware/SDK/Bluetooth/codebase (`EV-0009` through `EV-0012`), Brilliant primary product/docs, `docs/report-cards/BATCH_01.md`, `BATCH_06.md`, and `HIGH_THROUGHPUT_BATCH_02.md`.

## Lineage
Monocle → Frame → Halo. Shared corporate/open-development philosophy does not justify copying hardware, sensors or firmware details between generations.

## Monocle — GLS-0050
Clip-on open developer display module. Brilliant documents 640×400 color OLED (~20° FOV), 5 MP camera, microphone, Bluetooth 5.2, 70 mAh battery, touch, nRF52832 MCU, FPGA acceleration, MicroPython, custom firmware, OTA updates, custom FPGA images, published schematics/mechanical files and SWD/JTAG programming.

Report-card anchor: H8.0 W6.0 VAI8.0 S9.0 O10.0 OC10.0 CI9.5 Hack10.0 HUD7.5; Value not yet graded.

Monocle remains a catalog benchmark for openness/hackability because owner access extends below the application layer into firmware, FPGA and hardware documentation.

## Frame — GLS-0051
Prescription-capable glasses with 640×400 color OLED, 20° FOV, 720p camera, microphone, FPGA, Bluetooth 5.3, 210 mAh battery and motion sensors. Brilliant documents Lua on-device execution, BLE development, Python/Flutter SDKs, Lua REPL, OTA firmware, open-source firmware, FPGA source, schematics, mechanical files and SWD access.

Report-card anchor: H8.5 W7.5 VAI8.5 S9.5 O10.0 OC10.0 CI9.5 Hack10.0 HUD7.5; Value not yet graded.

## Halo — GLS-0052
Shipping/current open-source platform (shipping began Q1 2026 in the completed source packet). Brilliant documents color OLED, dual bone-conduction speakers, dual microphones, optical sensor, 6-axis IMU, Bluetooth 5.3, Alif B1 Cortex-M55/NPU, ZephyrOS + Lua, all-day battery and open hardware/software/design files.

Report-card anchor: H8.5 W9.0 VAI8.0 S8.5 O10.0 OC9.5 CI9.0 Hack10.0 HUD7.5 V8.5. Price basis: $349.

## Common-ruler interpretation
Brilliant Labs establishes the high end of the catalog's Openness/Hackability ruler. Open source alone is not enough for every other dimension: wearability, optics, battery, visual AI and value stay generation-specific. Cloud features such as bundled assistants are optional layers rather than the sole route to hardware use.

## Preservation / repair
Published schematics, mechanical files, firmware and source materially improve long-term preservation potential. Actual replacement-part availability and practical repair procedures should still be evidenced separately.

## Research priorities
Normalized battery measurements, exact prescription/optical serviceability, parts sourcing, long-term firmware support, current Halo/Frame local-AI capability and hands-on repairability.