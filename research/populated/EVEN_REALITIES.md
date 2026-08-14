# Even Realities G2 — populated research record

Last reviewed: 2026-08-13
Primary evidence: EV-0029, EV-0030, Even Hub developer documentation, and `docs/report-cards/HIGH_THROUGHPUT_BATCH_02.md`.

## Identity and architecture
This record covers Even Realities G2 only. Similar styling or brand continuity is not enough to transfer claims to G1 or future models.

Even documents binocular green MicroLED waveguides, 640×350 display resolution, 27.5° FoV, up to 1200 nits, four microphones, BLE, IP65 and roughly two-day battery life. The glasses intentionally omit both camera and speaker; Visual AI based on wearer-view imaging is therefore N/A, not merely unknown.

## Display and wearability
The binocular 27.5° waveguide HUD is the core hardware feature rather than an immersive wide-field AR system. Magnesium/titanium construction, prescription-ready positioning and two-day endurance support unusually strong everyday-wearability evidence for a display product.

Report-card anchors: Hardware8.0, Wearability9.5, Display/HUD8.5.

## Developer surface
Even Hub developer documentation exposes display, microphone and touch inputs to phone-hosted plugins. This materially changes the earlier provisional openness assessment: there is a supported application-development surface rather than only first-party companion behavior.

Report-card anchors: Software8.0, Openness7.0, Owner Control7.0, Hackability6.5.

This is application/plugin openness, not proof of open firmware, bootloader access, schematics or unrestricted low-level BLE control.

## AI and service dependence
There is no glasses-mounted camera, so camera-driven Visual AI is N/A. Microphone/display workflows can still support transcription, assistant and information-delivery features through the phone/service layer.

Custom phone-hosted plugins can drive display/input without requiring every workflow to depend on an Even cloud. Some headline AI/transcription features remain service-backed.

Report-card anchor: Cloud Independence8.0.

## Audio and sensing boundaries
Four microphones are documented; speaker output is not part of the G2 glasses architecture. Do not infer audio playback capability from microphone-based assistant features. Touch/input exposed to plugins is documented by the developer platform. Other sensors remain model-field claims requiring primary evidence.

## Ownership / prescription / serviceability
Prescription-ready positioning is a positive wearability signal, but independent optical serviceability, exact correction range, repair path, battery replacement, parts availability and long-term support still need dedicated field evidence.

## Report card
- Hardware: 8.0
- Wearability: 9.5
- Visual AI: N/A
- Software: 8.0
- Display/HUD: 8.5
- Openness: 7.0
- Owner Control: 7.0
- Cloud Independence: 8.0
- Hackability: 6.5
- Value: Not yet graded

## Next verification targets
1. Exact prescription limits and independent optical-service path.
2. Function-by-function offline test for first-party and custom plugins.
3. BLE/protocol characterization below the supported plugin layer.
4. Companion-app account and first-run requirements.
5. Repairability, battery replacement and parts availability.
6. Independent wear, brightness and endurance measurements.
7. Current price and ownership-cost analysis.