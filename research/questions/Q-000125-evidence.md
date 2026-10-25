# Q-000125 — Detect Google Glass programmatically

**Original observed question:** [Stack Overflow, September 10, 2013](https://stackoverflow.com/questions/18723689/detect-google-glass-programmatically). The developer asks how a native Android application can distinguish Google Glass from a phone. Preserved in `research/questions/registry.json` as Q-000125.

**Primary platform evidence:** [Android Developers, `android.os.Build`](https://developer.android.com/reference/android/os/Build) documents `MANUFACTURER`, `MODEL`, and other build properties; these are software-exposed device descriptors, not hardware attestation.

**Primary legacy product evidence:** [Google Glass Development Kit](https://developers.google.com/glass/develop/gdk) confirms the original Glass GDK was an Android SDK add-on.

**Attributed historical observation:** The Stack Overflow thread documents `Google` as manufacturer and `Glass 1` as model, with a `Build.MANUFACTURER` + `Build.MODEL.startsWith("Glass")` check. This is a historic community observation, not an all-generation compatibility matrix.

**Claim boundary:** Do not imply this heuristic identifies every Glass Enterprise device, cannot be spoofed, or validates specific features. Avoid treating API level 19 alone as a Glass identifier. No GlassesResearch device reproduction.

**Published answer:** `docs/faq/09-development-openness.md#detect-google-glass-programmatically`. **State:** published and exact production FAQ content verified 2026-10-25; reviewed 2026-10-24. No device reproduction.

## Publication proof — 2026-10-25

[PR #691](https://github.com/theGreenJedi/GlassesResearch/pull/691) merged at revision `3221f106e1853fe0ffd1885cbb14d945319c3465`. [Production content proof run #40161886546](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40161886546) succeeded, fetching the public `/docs/faq/09-development-openness/` page and confirming the exact built content digest `ae61abc38c7f` on 2026-10-25. The FAQ source contains this question's heading and cited answer; the production proof verifies the complete deployed page. This does not verify physical-device behavior.
