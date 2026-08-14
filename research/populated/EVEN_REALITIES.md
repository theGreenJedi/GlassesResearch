# Even Realities G2 — populated research record

Status: evidence-backed population pass
Last reviewed: 2026-08-13
Primary evidence: EV-0029, EV-0030

## Identity and scope

This record covers Even Realities G2. Claims are limited to the G2 unless a source explicitly establishes continuity with another Even Realities model. Similar product appearance or brand lineage is not enough to transfer hardware or service claims.

## Hardware and display

- Display: present and central to the product experience. Exact display specifications should follow EV-0029 rather than secondary summaries.
- Camera: no camera claim is established by EV-0029/EV-0030; preserve as not evidenced here rather than inferring from the broader AI-glasses category.
- Microphones: documented by EV-0029.
- Audio output: EV-0030 is the controlling source for whether the glasses themselves provide audio; do not infer speaker capability from microphone or AI features.
- Battery: documented by EV-0029. Manufacturer endurance figures remain vendor claims until normalized independent testing is available.

## Connectivity

- Bluetooth/BLE: documented by EV-0029.
- Companion-device relationship: documented operationally by EV-0030.
- Wi-Fi/cellular/USB data: no owner-access claim is made in this population pass without specific primary evidence.

Connectivity presence and developer accessibility remain separate questions.

## Sensing

Confirmed from the current evidence set:

- microphones are present;
- display hardware is present.

Camera, IMU, ambient-light, proximity, touch, and other sensing capabilities should remain unknown unless the primary specification explicitly documents them. Internal use of a component would not by itself establish owner or SDK access.

## AI and software behavior

EV-0030 documents the G2 companion-app and AI/service behavior at a product-support level. Record individual features separately rather than treating “AI” as one capability. Where a feature requires the phone, internet, Even Realities service, or another remote service, that dependence should be retained in the field-level record.

No claim is made here that the owner can replace the default model, redirect AI endpoints, or run the product's AI stack locally. Those remain unknown until evidenced.

## Offline and service dependence

EV-0030 is primary evidence for offline and connectivity behavior. The correct survival question is function-by-function: what remains available without internet, without the companion application, while signed out, or after a future service shutdown. Do not collapse partial offline usefulness into either “cloud independent” or “cloud dependent.”

Current evidence supports documenting a companion/service relationship; a full shutdown-survival test has not been independently performed by GlassesResearch.

## Openness and owner control

- Public low-level protocol: unknown in this evidence set.
- Public SDK exposing hardware: unknown in this evidence set.
- Replaceable AI/model endpoint: unknown.
- Local owner-controlled processing: unknown.
- Independent companion implementation: not established by EV-0029/EV-0030.

These unknowns should materially constrain Openness, Owner Control, Cloud Independence, and Hackability scoring rather than being converted into unsupported negative claims.

## Prescription, fit, and serviceability

Prescription compatibility, independent optical serviceability, fit, repairability, replacement parts, and battery replacement require dedicated evidence. Do not infer optical serviceability from ordinary-eyewear appearance.

## Lifecycle and aging

G2 is treated as a current product in the source set reviewed for this pass. No reliability rate, battery-aging curve, or long-term failure pattern is established here. Future service changes should be dated rather than silently overwriting this record.

## Report-card implications

- Hardware: display, microphones, battery and documented connectivity can be evidenced from EV-0029; unsupported sensors remain unknown.
- Wearability: requires geometry and wear evidence beyond appearance.
- Visual AI: do not award camera-based visual-AI credit without evidence of visual input.
- Software: companion and AI behavior are evidenced at a support-documentation level by EV-0030.
- Openness: insufficient evidence for broad developer or protocol access.
- Owner Control: model/endpoint replacement and independent control remain unknown.
- Cloud Independence: evaluate feature by feature using EV-0030 and future hands-on tests.
- Hackability: insufficient evidence for low-level access in this pass.
- Value: requires dated purchase/subscription and ownership-cost evidence.

## Next verification targets

1. Exact display and battery specification extraction from EV-0029.
2. Function-by-function offline test.
3. Companion-app account and first-run requirements.
4. Public protocol/SDK search and BLE service characterization.
5. Prescription and independent optical-service evidence.
6. Repairability, battery replacement, and parts availability.
7. Independent wear and endurance testing.
