# Captify Pro — Research Hub

**Canonical ID:** `GLS-0218`  
**Regulatory model:** CAP001  
**FCC ID:** 2BQMS-CAP001  
**Lineage:** [Captify accessibility smart-glasses lineage](../../lineages/CAPTIFY.md)

Captify Pro is a 2025–2026 accessibility-focused binocular display smart-glasses platform sold directly by Captify for real-time captions and translation. Captify's current retail and support surfaces establish active purchaser access, while regulatory evidence independently identifies model CAP001 under FCC ID 2BQMS-CAP001.

## Current manufacturer-stated hardware

- binocular diffractive-waveguide display;
- 640×480 resolution;
- 30° field of view;
- 1,500-nit brightness claim;
- 37 g frame mass;
- 145 mm frame width;
- 128 mm temple length;
- 49×41 mm lens dimensions;
- 180 mAh battery;
- 20 h standby / 4 h continuous-use claims;
- Bluetooth 5.3, 10 m claimed range;
- dual beamforming microphones;
- stereo directional speakers;
- IPX4 claim;
- magnetic charging.

These values are manufacturer statements pending GlassesResearch bench measurement.

## Phone / cloud architecture

Captify says a paired iOS 16+ or Android 12+ phone is required and that speech-to-text processing occurs on the phone. Standard Captify Pro service includes offline captions and translations, environmental-sound detection, and automated note-taking. The optional Premium tier adds higher-accuracy services, speaker differentiation, AI summaries, custom vocabulary, cloud backup/sync, and Ask AI over saved conversations.

That makes Captify Pro a strong candidate for service-survival testing: core captioning is claimed to work without internet access, while higher-level capabilities deliberately depend on cloud service.

## Owner-control questions

Do not infer answers from marketing. Verify:

1. whether Standard-mode audio or transcripts ever leave the phone;
2. what data are stored locally and in what format;
3. whether transcripts/notes can be exported and fully deleted;
4. whether the glasses expose a generic Bluetooth display/audio protocol;
5. firmware-update behavior and downgrade/recovery options;
6. factory-reset semantics;
7. functionality with Captify servers unreachable;
8. whether third-party software can drive the display or microphones.

## Prescription discrepancy

Captify's public pages conflict. The dedicated specification page states SPH -10.00 to +6.00 and CYL -6.00 to +6.00; the current product page/FAQ advertises sphere support down to -20.00. GlassesResearch preserves that conflict rather than selecting a preferred value. Bench/order verification or a corrected first-party specification is required.

## Related hardware

**Captify Myvu** is not treated as a separate underlying hardware generation. Captify explicitly states that it is built in collaboration with DreamSmart MYVU, and its published specifications align with the existing MYVU Air / StarV Air platform tracked as `GLS-0167`. Its Captify software, support, prescription, and accessibility-service layer remain separately material.

## Evidence

- https://captify.glass/products/captify-pro
- https://captify.glass/pages/pro-specifications
- https://captify.glass/pages/faqs
- https://captify.glass/pages/subscription
- https://captify.glass/pages/privacy-policy
- https://help.captify.glass/hc/en-us/categories/43034252521235-Captify-Pro
- https://help.captify.glass/hc/en-us/articles/43602292076947-Setting-Up-Your-Captify-Pro-for-the-First-Time
- Regulatory report: Captify Pro CAP001 / FCC ID 2BQMS-CAP001
- [Lineage investigation](../../research/investigations/CAPTIFY_LINEAGE_2026-09-06.md)
