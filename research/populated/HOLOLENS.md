# Microsoft HoloLens — populated research record

Source basis: `docs/report-cards/LINEAGE_MICROSOFT_HOLOLENS.md` (2026-08-12), Microsoft primary documentation and `EV-0036` service-survival evidence.

## Taxonomy
HoloLens is adjacent head-worn mixed reality rather than ordinary smart glasses. Hardware generations are HoloLens 1 and HoloLens 2; Development/Industrial editions are procurement/support configurations unless hardware differences are proven.

## HoloLens 1
Fully untethered spatial computer with see-through waveguides, environment-understanding cameras, depth sensing, photo/video camera, IMU, microphones, spatial audio, Intel 32-bit compute, custom HPU, 2 GB RAM, 64 GB flash, Wi-Fi/Bluetooth and 2–3 hours active battery life. Weight: 579 g. Windows 10 Holographic.

Microsoft states December 2024 was the final monthly servicing update and explicitly says devices continue to function after 2024-12-10, while security updates, technical support and out-of-warranty exchange inventory end.

**Service status:** **Discontinued-functional.** This is an important counterexample to destructive cloud shutdown: support/security aging is real, but local device function survives according to the vendor.

Report-card anchor: H8.0 W2.0 VAI6.5 S8.5 O6.5 OC8.0 CI9.0 Hack7.0 HUD9.0; Value not yet graded.

## HoloLens 2
Second-generation standalone MR platform with Snapdragon 850, second-gen HPU, 4 GB RAM, 64 GB UFS, 2k 3:2 light engines, tracking and eye-tracking cameras, ToF depth sensing, 8 MP camera, articulated hand tracking, eye tracking, iris auth, spatial mapping, Wi-Fi 5, Bluetooth 5 and USB-C. Weight: 566 g. Microsoft states it is no longer manufactured and is out of stock globally.

Microsoft documents November 2024 as the final feature release while monthly security servicing continues through December 2027 for supported Windows 11 configurations. Older Windows 10 branches reached final servicing in December 2024.

**Service status:** **Maintenance / winding down**, with support horizon dependent on OS version rather than a single all-or-nothing end date.

Report-card anchor: H9.0 W2.5 VAI7.5 S9.0 O7.0 OC8.0 CI8.0 Hack7.5 HUD9.5; Value not yet graded.

## Service-survival matrix

EV-0066 establishes that HoloLens 1 continues functioning with local Device Portal/Visual Studio deployment after support. For HoloLens 2, ordinary first run requires network plus Microsoft/Entra identity, but Microsoft also documents local-account secure-offline provisioning, signed Appx installation by USB/File Explorer, Device Portal deployment and offline FFU recovery when the image was downloaded in advance.

## Ownership interpretation
Both generations support local spatial-computing applications and meaningful developer control. HoloLens 1's continued function after support ends is direct positive service-survival evidence. HoloLens 2's first-run account/network requirements and OS-version-specific servicing show that Cloud Independence and support lifetime are related but distinct dimensions.

## Evidence gaps
Source boundary completed in EV-0066. Remaining: post-2027 hands-on Store, sign-out, certificate trust, reset, endpoint blocking and recovery tests; plus acquisition price, repairability, parts and battery aging.