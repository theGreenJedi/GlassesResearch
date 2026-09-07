# Captify accessibility smart-glasses lineage

Captify is an accessibility-focused smart-glasses company whose current product family centers on real-time captioning for deaf and hard-of-hearing users. The lineage is software- and service-defined as much as hardware-defined: Captify Myvu builds on DreamSmart/MYVU hardware, while Captify Pro is a distinct Captify-branded hardware generation with its own regulatory identity.

## Current products

### Captify Myvu — DreamSmart / MYVU platform edition

Captify states that its standard/Myvu edition is built in collaboration with **DreamSmart MYVU**. Its published hardware profile aligns closely with the existing **MYVU Air / StarV Air** platform already tracked as `GLS-0167`: 43 g mass, binocular diffractive waveguide display, 640×480 resolution, 30° field of view, 1,500-nit brightness claim, 180 mAh battery, Bluetooth 5.3, dual microphones, and stereo directional speakers.

GlassesResearch therefore treats Captify Myvu as a **Captify accessibility/software/service edition associated with GLS-0167**, not as evidence for a wholly separate underlying hardware generation.

Captify differentiates the edition through its Captify Glass app, caption/translation workflow, prescription program, support, and commercial relationship.

### Captify Pro / CAP001 — `GLS-0218`

Captify Pro is a materially distinct generation. Captify publishes a 37 g frame, 145 mm frame width, 128 mm temples, 49×41 mm lens dimensions, binocular 640×480 / 30° diffractive-waveguide display, Bluetooth 5.3, dual beamforming microphones, stereo directional speakers, 180 mAh battery, and magnetic charging.

A July 2025 RF exposure report identifies the product as **model CAP001, FCC ID 2BQMS-CAP001**, with Captify Inc. as applicant/manufacturer. This stable regulatory identity plus active direct retail availability supports canonical catalog admission as `GLS-0218`.

## Software architecture

Captify says both current glasses require an iOS or Android phone for captioning, with speech-to-text processing performed on the phone. For Captify Pro, the free/standard tier includes offline captioning, offline translation, environmental-sound detection, and note-taking. Premium service adds features including higher-accuracy processing, speaker differentiation, summaries, cloud sync, custom vocabulary, and Ask AI over conversation history.

This is an unusually useful architecture for GlassesResearch because it separates:

- **face hardware:** display, microphones, speakers, controls;
- **phone compute:** speech recognition and core interaction;
- **optional cloud layer:** premium accuracy, synchronization, summaries, and conversational retrieval.

That separation should make service-survival and cloud-dependence testing unusually concrete.

## Accessibility specialization

Captify is not primarily marketed as a general AI assistant or spatial-computing platform. Its central use case is conversational access. Public documentation emphasizes caption readability, directional microphone behavior, translation, prescription compatibility, and private in-lens presentation.

The lineage therefore belongs both in the discreet-display family and in the site's accessibility research layer.

## Evidence boundaries

- Hardware specifications are currently **manufacturer-stated**, not GlassesResearch bench measurements.
- Captify Myvu's DreamSmart relationship is **first-party stated**.
- Captify Pro's CAP001 identity is **regulatory evidence**.
- Offline-operation claims are **manufacturer-stated software behavior** until reproduced.
- No public SDK, open protocol, source repository, bootloader path, or third-party app interface has yet been established.
- Privacy policy language is currently too broad to establish transcript/audio retention, cloud-upload, export, or deletion behavior for conversation data.

## Open investigation

See [Captify lineage investigation — 2026-09-06](../research/investigations/CAPTIFY_LINEAGE_2026-09-06.md).

Primary surfaces:
- https://captify.glass/products/captify-pro
- https://captify.glass/products/captify-myvu
- https://captify.glass/pages/faqs
- https://captify.glass/pages/subscription
- https://help.captify.glass/hc/en-us/categories/43034252521235-Captify-Pro
