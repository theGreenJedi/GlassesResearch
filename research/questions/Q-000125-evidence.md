# Q-000125 — Detect Google Glass programmatically

**Original observed question:** [Stack Overflow, September 10, 2013](https://stackoverflow.com/questions/18723689/detect-google-glass-programmatically). The developer asks how a native Android application can distinguish Google Glass from a phone. Preserved in `research/questions/registry.json` as Q-000125.

**Primary platform evidence:** [Android Developers, `android.os.Build`](https://developer.android.com/reference/android/os/Build) documents `MANUFACTURER`, `MODEL`, and other build properties; these are software-exposed device descriptors, not hardware attestation.

**Primary legacy product evidence:** [Google Glass Development Kit](https://developers.google.com/glass/develop/gdk) confirms the original Glass GDK was an Android SDK add-on.

**Attributed historical observation:** The Stack Overflow thread documents `Google` as manufacturer and `Glass 1` as model, with a `Build.MANUFACTURER` + `Build.MODEL.startsWith("Glass")` check. This is a historic community observation, not an all-generation compatibility matrix.

**Claim boundary:** Do not imply this heuristic identifies every Glass Enterprise device, cannot be spoofed, or validates specific features. Avoid treating API level 19 alone as a Glass identifier. No GlassesResearch device reproduction.

**Proposed answer:** `docs/faq/09-development-openness.md#how-can-an-android-app-detect-whether-it-is-running-on-google-glass`. **State:** researched; pending deployment and exact live-page verification. Reviewed 2026-10-24.
