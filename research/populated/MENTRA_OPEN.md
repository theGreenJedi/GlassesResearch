# Mentra / open smart-glasses ecosystem — populated research record

Primary evidence includes MentraOS (`EV-0013`), MentraOS releases (`EV-0014`), Open Source Smart Glasses (`EV-0015`), Mentra Live product material and `docs/report-cards/BATCH_06.md`.

## Ecosystem architecture
Mentra is an open software/hardware ecosystem rather than one uniform hardware lineage. Device compatibility and sensors remain implementation-specific. Public source, SDK/application work and open hardware provide some of the strongest owner-inspectability evidence in GlassesResearch.

## Mentra Live — GLS-0038
Current retail/developer camera/audio glasses. Mentra documents a 43 g frame, 119° camera, 3264×2448 stills, 1080p video, stereo speakers, three microphones, touch/buttons, Wi-Fi, Bluetooth, 260 mAh glasses battery, 2200 mAh charging case and 12+ hours mixed use.

Mentra states developers can build Android/iOS apps that directly control camera, speakers, microphone, touchpad and buttons, including offline operation without Mentra-hosted cloud infrastructure. MentraOS is MIT-licensed and publicly developed.

Report-card anchor: H8.0 W9.0 VAI8.5 S9.0 O9.5 OC9.5 CI9.5 Hack9.0 HUD N/A; Value not yet graded.

This is a near-benchmark example of open camera/audio eyewear. It remains below Monocle/Frame's 10/10 hardware-level benchmark because the commercial hardware itself is not documented at the same schematic/firmware/debug depth.

## Open Source Smart Glasses branch
EV-0015 provides mechanical, electrical, firmware and software design material for independently buildable glasses. This branch may exceed commercial Mentra-compatible hardware in repairability/inspectability; do not transfer those attributes automatically to every compatible product.

## Owner control and cloud independence
The ecosystem structurally supports owner-selected companion applications and services. Mentra Live provides concrete evidence that core custom applications can run without Mentra cloud. Cloud AI remains an optional downstream choice rather than a required sole path for owner-written workflows.

## Connectivity/sensor rule
Mentra compatibility is not evidence that every device has the same radio, camera, display or sensors. Populate capability per hardware target.

## Research priorities
Mentra Live current value, hardware-level firmware/debug access, battery/charging-case aging, optical serviceability, repair parts, exact BLE/Wi-Fi protocol surfaces and long-term compatibility across MentraOS releases.