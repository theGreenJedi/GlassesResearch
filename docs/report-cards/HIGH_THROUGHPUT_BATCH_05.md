# High-Throughput Report Card Batch 05 — Enterprise Monocular Systems

**Research date:** 2026-08-12

This packet continues the report-card-first pipeline with the next 12 enterprise models in the canonical ledger: Vuzix M100, M300, M300XL, M400, M4000, LX1, Shield; and RealWear HMT-1, HMT-1Z1, Navigator 500, Navigator 520, and Navigator Z1.

The shared catalog-wide benchmark ruler in `research/REPORT_CARD_BENCHMARKS.md` is used without enterprise-category inflation. Industrial ruggedness can raise Hardware while headbands, boom displays and PPE-oriented bulk can constrain Wearability. Android application deployment, sensor APIs and documented SDKs materially improve Openness, Owner Control and Hackability, but do not approach the Monocle/Frame 10/10 benchmark without comparable firmware, schematic and low-level access.

## Report Cards

| ID | Model | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GLS-0095 | Vuzix M100 | 4.5 | 3.5 | 3.5 | 4.5 | 5.0 | 6.0 | 8.0 | 5.5 | 4.0 | Not yet graded |
| GLS-0096 | Vuzix M300 | 6.0 | 4.5 | 5.5 | 6.0 | 6.5 | 7.0 | 8.5 | 6.5 | 5.0 | Not yet graded |
| GLS-0097 | Vuzix M300XL | 6.5 | 4.5 | 6.0 | 6.0 | 6.5 | 7.0 | 8.5 | 6.5 | 5.0 | Not yet graded |
| GLS-0098 | Vuzix M400 | 8.0 | 5.5 | 7.5 | 7.5 | 7.0 | 8.0 | 9.0 | 7.0 | 6.0 | Not yet graded |
| GLS-0099 | Vuzix M4000 | 8.0 | 5.5 | 7.5 | 7.5 | 7.0 | 8.0 | 9.0 | 7.0 | 7.0 | Not yet graded |
| GLS-0100 | Vuzix LX1 | 8.0 | 4.5 | 6.5 | 7.5 | 7.0 | 8.0 | 9.0 | 7.0 | 6.5 | Not yet graded |
| GLS-0121 | Vuzix Shield | 8.5 | 6.5 | 8.0 | 7.5 | 7.0 | 8.0 | 9.0 | 7.0 | 8.5 | Not yet graded |
| GLS-0101 | RealWear HMT-1 | 6.5 | 4.0 | 5.5 | 6.5 | 6.0 | 7.0 | 8.0 | 6.0 | 5.0 | Not yet graded |
| GLS-0102 | RealWear HMT-1Z1 | 7.0 | 3.5 | 5.5 | 6.5 | 6.0 | 7.0 | 8.0 | 6.0 | 5.0 | Not yet graded |
| GLS-0103 | RealWear Navigator 500 | 8.0 | 4.5 | 7.0 | 7.5 | 6.5 | 7.5 | 8.5 | 6.5 | 5.5 | Not yet graded |
| GLS-0104 | RealWear Navigator 520 | 8.5 | 4.5 | 7.0 | 8.0 | 6.5 | 7.5 | 8.5 | 6.5 | 7.0 | Not yet graded |
| GLS-0105 | RealWear Navigator Z1 | 8.5 | 4.0 | 7.0 | 8.0 | 6.5 | 7.5 | 8.5 | 6.5 | 7.0 | Not yet graded |

## Evidence-derived judgments

### Vuzix lineage

The M-series is unusually owner-controllable for commercial enterprise eyewear because it is fundamentally an Android wearable-computer lineage rather than a locked companion peripheral. Vuzix documents standard Android camera, sensor, Bluetooth/BLE and database APIs plus device-specific speech/barcode SDK surfaces. M300/M300XL use Android 6.0.1 and can be treated identically by developers; the XL changes the battery connection and improves camera behavior. This supports materially stronger Openness, Owner Control and Hackability scores than ordinary proprietary consumer glasses, but source firmware, schematics and benchmark-level low-level hardware access are not documented.

M400/M4000 are a major hardware step: Qualcomm XR1, 6 GB RAM, 64 GB storage, 12.8 MP stills/4K camera, orientation sensors, triple microphones, touch, buttons and voice control. M400 uses an occluded 640×360 OLED; M4000 moves to an 854×480 see-through waveguide. Standard Android development remains available, and Vuzix View explicitly supports APK installation with USB debugging. The result is strong owner application control and cloud independence without confusing Android programmability with open hardware.

LX1 is a 2026 warehouse-focused Android 15 system with a 7000 mAh long-shift battery, rugged/freezer-oriented design and NFC pairing. Its purpose-built headband form is valuable industrially but scores below ordinary glasses for catalog-wide Wearability.

Shield is the most optically ambitious Vuzix system in this packet: Snapdragon XR1, binocular full-color microLED waveguide optics, stereo HD cameras, voice/touch interaction and prescription-ready safety-glasses framing. Its binocular see-through architecture establishes the strongest Display/HUD score in this batch while retaining the same broadly Android-oriented developer posture as Vuzix's current standalone line.

### RealWear lineage

HMT-1/HMT-1Z1 established RealWear's rugged voice-first monocular model. Their 854×480 0.32-inch displays remain useful but modest on the catalog-wide display ruler. HMT-1Z1's intrinsically safe construction is a hardware advantage for hazardous environments but does not translate into ordinary-eyewear wearability. Both are now end-of-support, with firmware ending at 12.6; HMT-1 nevertheless reached Android 10 and supports local dictation in English, German and Mandarin, showing that core operation was not wholly cloud-bound.

Navigator 500 modernized the platform with a modular camera and swappable battery while retaining an 854×480 display. Navigator 520 and Navigator Z1 move to 1280×720 0.35-inch HD displays; Z1 adds intrinsically safe construction. RealWear states that Navigator 500, 520 and Z1 remain supported through at least December 2030 and plans Android-16-based software for currently supported devices in 2026. Their Android enterprise application model gives owners meaningful deployment control, but the platform remains proprietary and therefore stays well below the Monocle/Frame openness benchmark.

## Primary-source families

- Vuzix developer resources: https://support.vuzix.com/docs/developer-resources
- Vuzix M300/M300XL overview: https://support.vuzix.com/docs/getting-to-know-the-m300xl-overview
- Vuzix M300/M300XL technical details: https://support.vuzix.com/docs/m300xl-technical-details
- Vuzix M400/M4000 overview: https://support.vuzix.com/docs/overview-22
- Vuzix M400/M4000 technical details: https://support.vuzix.com/docs/m400-m4000-technical-details
- Vuzix M400 product specifications: https://www.vuzix.com/products/m400-smart-glasses
- Vuzix current smart-glasses lineup/LX1: https://www.vuzix.com/pages/smart-glasses
- Vuzix Shield launch details: https://ir.vuzix.com/news-events/press-releases/detail/1938/vuzix-showcases-its-new-shield-at-ces-2022-as-the
- RealWear device identification/lineage: https://support.realwear.com/knowledge/which-realwear-device-model-do-i-have
- RealWear display resolutions: https://support.realwear.com/knowledge/device-screen-resolution
- RealWear firmware support policy: https://support.realwear.com/knowledge/realwear-firmware-update-and-support-policy
- RealWear HMT-1 release 12.6: https://support.realwear.com/knowledge/firmware-release-12.6-release-notes
- RealWear HMT speech/dictation behavior: https://support.realwear.com/knowledge/speech-keyboard-hmt-interaction

## Batch result

Twelve additional canonical models now have explicit evidence-backed Report Cards. This batch also clarifies a recurring catalog distinction: a proprietary Android wearable can provide substantial owner application control and practical hackability without qualifying as open hardware. That distinction keeps the common ruler anchored to Monocle/Frame rather than inflating enterprise SDK access into a 10.