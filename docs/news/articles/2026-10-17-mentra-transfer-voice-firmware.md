# MentraOS community research: video transfer, voice activity, and firmware hotspot

**Across the Wire · Community-reported · October 17, 2026 · Not independently verified by GlassesResearch**

## iOS gallery transfer recovery

[MentraOS PR #4822](https://github.com/Mentra-Community/MentraOS/pull/4822) documents a reported failure in which large video transfers stall after an iPhone backgrounds the app and the glasses hotspot times out. The upstream change proposes a shorter timeout and resumable retries, with automated test results reported. Physical-device reproduction and production availability remain unconfirmed.

## Voice recognition onset

[MentraOS PR #4821](https://github.com/Mentra-Community/MentraOS/pull/4821) changes voice-activity-detection defaults following reports that the first words or wake commands were clipped. The scope of affected hardware and actual release behavior need independent testing.

## Firmware update transport

[MentraOS PR #4829](https://github.com/Mentra-Community/MentraOS/pull/4829) changes update transport to prefer the glasses hotspot when supported. Validate fallback and recovery behavior on physical devices.

## Independent MYVU control

The [technosonder/MeizuMYVU_ESP32 project](https://github.com/technosonder/MeizuMYVU_ESP32) documents an ESP32-S3 implementation of BLE pairing, notifications, time synchronization, and reconnection for MYVU glasses. This is an older project (reported last commit August 22), newly identified for GlassesResearch; it is not an October release. Inspect hardware compatibility and owner-independent operation before claiming reproducibility.

## Additional interoperability lead

[hkust-spark/xg-glass-sdk](https://github.com/hkust-spark/xg-glass-sdk) documents a cross-manufacturer SDK and distinguishes hardware-tested integrations from untested adapters. Track the supported-device evidence rather than assuming universal compatibility.

**Evidence boundary:** All statements above are attributed to upstream repositories. No GlassesResearch bench verification is claimed.
