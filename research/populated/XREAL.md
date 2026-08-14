# Nreal / XREAL — populated research record

Primary evidence includes XREAL SDK documentation (`EV-0021`), One specifications (`EV-0022`), manufacturer history/product pages `docs/report-cards/HIGH_THROUGHPUT_BATCH_03.md`, and [EV-0053](../../evidence/EV-0053-current-value-wave-two.md).

## Lineage pattern
Nreal Light → XREAL Air → Air 2 / Air 2 Pro / Air 2 Ultra → One / One Pro. Most of the lineage is host-driven display eyewear: the owner chooses the phone/PC/console and the glasses provide local display/spatial functions. Air 2 Ultra is the major sensing-oriented exception.

## Nreal Light — GLS-0069
Early 52°-FOV 6DoF consumer AR device with a mobile host and developer path.

Anchor: H7.5 W6.5 VAI4.0 S7.0 O6.0 OC6.5 CI8.5 Hack6.0 HUD8.0; Value not yet graded.

## XREAL Air — GLS-0070
2021 mass-market host-powered Micro-OLED display generation.

Anchor: H7.5 W7.5 VAI N/A S7.0 O5.5 OC7.5 CI9.0 Hack5.5 HUD8.0; Value not yet graded.

## Air 2 — GLS-0071
72 g, 46° FOV, Sony 0.55-inch Micro-OLED, 1920×1080 per eye, up to 120 Hz, 500 nits, stereo speakers and prescription insert support.

Anchor: H8.0 W8.0 VAI N/A S7.5 O5.5 OC8.0 CI9.5 Hack5.5 HUD8.5 V8.5. Official US price basis in the completed packet: ~$199.

## Air 2 Pro — GLS-0072
Air 2 optical platform plus three-level electrochromic dimming, ~75 g.

Anchor: H8.5 W8.0 VAI N/A S7.5 O5.5 OC8.0 CI9.5 Hack5.5 HUD8.8 V8.5. Price basis: ~$249.

## Air 2 Ultra — GLS-0073
83 g titanium frame, 52° FOV, 1080p-per-eye Micro-OLED, 120 Hz 2D/90 Hz 3D, dual environment sensors, hand/head tracking, 6DoF, depth mesh, spatial anchors and plane/image tracking.

Anchor: H9.0 W7.0 VAI7.0 S8.5 O7.0 OC8.0 CI9.0 Hack7.0 HUD9.0; Value not yet graded.

This model should not inherit ordinary camera-glasses assumptions: environment sensing supports spatial understanding, but it is not primarily a photo/video capture device.

## XREAL One — GLS-0074
On-glasses X1 spatial-computing chip, binocular Micro-OLED display, spatial stabilization and host-driven content architecture.

Anchor: H9.0 W7.5 VAI N/A S8.5 O5.5 OC8.5 CI9.5 Hack5.5 HUD9.2; **V8.0 at $399 sale / V7.5 at $499 regular (US, checked 2026-08-14).**

## XREAL One Pro — GLS-0075
X Prism optical engine, 57° FOV, up to 171-inch virtual screen, two IPD size ranges, 120 Hz and dedicated spatial compute.

Anchor: H9.3 W7.5 VAI N/A S8.5 O5.5 OC8.5 CI9.5 Hack5.5 HUD9.5 V7.5. Completed-packet price basis: ~$599.

## Ownership interpretation
The lineage scores unusually well in practical Owner Control and Cloud Independence because host selection controls content and compute, while the display itself does not need an AI cloud. That is different from system-level openness: firmware/hardware remain proprietary, so host freedom should not be confused with open internals.

## Developer access
Official SDK support is meaningful application-layer openness. Air 2 Ultra's spatial APIs materially deepen the development surface. No claim is made here for open firmware, unlocked bootloaders or unrestricted low-level control.

## Research priorities
Populate exact USB/display transport by model, accessory/Beam dependence, prescription insert/service details, repairability, firmware/update behavior, sensor exposure, regional differences and historical/current acquisition value where still ungraded.