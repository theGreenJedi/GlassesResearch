# Mentra / open smart-glasses ecosystem — populated research record

Primary evidence includes MentraOS (`EV-0013`), MentraOS releases (`EV-0014`), Open Source Smart Glasses (`EV-0015`), Mentra Live product material, `docs/report-cards/BATCH_06.md`, and `EV-0040`.

## Ecosystem architecture
Mentra is an open software/hardware ecosystem rather than one uniform hardware lineage. Device compatibility and sensors remain implementation-specific. Public source, SDK/application work and open hardware provide some of the strongest owner-inspectability evidence in GlassesResearch.

## Mentra Live — GLS-0038
Current retail/developer camera/audio glasses. Mentra documents a 43 g frame, 119° camera, 3264×2448 stills, 1080p video, stereo speakers, three microphones, touch/buttons, Wi-Fi, Bluetooth, 260 mAh glasses battery, 2200 mAh charging case and 12+ hours mixed use.

Mentra states developers can build Android/iOS apps that directly control camera, speakers, microphone, touchpad and buttons. MentraOS is MIT-licensed and publicly developed.

Report-card anchor: H8.0 W9.0 VAI8.5 S9.0 O9.5 OC9.5 CI9.5 Hack9.0 HUD N/A; Value not yet graded.

This is a near-benchmark example of open camera/audio eyewear. It remains below Monocle/Frame's 10/10 hardware-level benchmark because the commercial hardware itself is not documented at the same schematic/firmware/debug depth.

## Optical serviceability
Mentra's current FAQ explicitly says owners can swap in their own lenses through **any optician**. Mentra plans checkout prescription options separately, so ordinary optical service does not require a Mentra-only prescription channel. Exact prescription ranges, progressive/high-index limits and electronics-safe lens-fitting procedures still need characterization.

Optical-service class: **ordinary local optician**.

## Open Source Smart Glasses branch
EV-0015 provides mechanical, electrical, firmware and software design material for independently buildable glasses. This branch may exceed commercial Mentra-compatible hardware in repairability/inspectability; do not transfer those attributes automatically to every compatible product.

## Owner control and cloud independence
Mentra Live documents offline calls, music and phone audio. App behavior is more nuanced: the official MentraOS architecture uses cloud services for orchestration, but the cloud code is open source and the official local-development guide documents running the cloud locally with Docker/local services and configuring the mobile app's **Cloud URL** to the developer-operated instance.

That is unusually strong service-survival evidence. The vendor-hosted cloud is not the only technically documented control plane. It does not mean every first-party feature automatically survives a shutdown without owner configuration, credentials or replacement external services.

## Repairability decomposition
Commercial Mentra Live should not inherit full open-hardware repairability merely because MentraOS and the separate Open Source Smart Glasses branch are open. Track battery replacement, hinge/temple repair, camera/audio modules and replacement parts independently.

## Connectivity/sensor rule
Mentra compatibility is not evidence that every device has the same radio, camera, display or sensors. Populate capability per hardware target.

## Research priorities
Mentra Live hardware-level firmware/debug access, battery/charging-case aging and replacement, exact BLE/Wi-Fi protocol surfaces, physical parts availability, prescription range/progressives, and end-to-end self-hosted operation without Mentra production services.