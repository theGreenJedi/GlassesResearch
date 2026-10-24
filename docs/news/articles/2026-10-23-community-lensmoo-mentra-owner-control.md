# Community engineering: LensMoo/XKOENPRO control and Mentra owner settings

**Across the Wire · Community-reported · October 23, 2026 · Not independently hardware-verified by GlassesResearch**

## CyanBridge: experimental LensMoo / XKOENPRO integration

[CyanBridge PR #32, opened October 23](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/pull/32), proposes a **separate, experimental Android integration** for LensMoo/XKOENPRO glasses using Classic Bluetooth SPP. The contributor describes original JPEG capture, explicit H.264 preview, battery queries and a physical-button assistant that can run with the phone locked. The proposed assistant sequence is deliberately bounded: microphone input, one photo, confirmed camera shutdown, original-image download, AI answer and audio to the glasses.

The contributor reports testing **XKOENPRO-12 firmware 1.0.2** with a **Pixel 11 Pro XL on Android 16**: a 320×240 preview, 1280×720 original JPEG, locked-phone physical-button activation, repeated requests and successful use after more than ten minutes idle. The PR reports 598 unit tests passing and two APK build targets. These are **author-reported tests**, not GlassesResearch reproduction. At the time of review, **PR #32 is open**: no general-release or universal compatibility claim is justified.

Important boundaries from the author: manual owner-ID setup, a separate Russian-language screen, Android 12+ for HFP routing, no OTA or native video download, no wake word, no high-resolution live preview, and no demonstrated all-day battery behavior. The integration explicitly avoids silently changing the user's chosen AI provider. The author also documents a separate debug package for side-by-side testing.

**Research disposition:** Add LensMoo/XKOENPRO to the community device-protocol watch and inspect model identity before any canonical model or compatibility score is changed. Track whether the PR merges, whether a signed release includes it, and whether independent owners reproduce the capture/shutdown and locked-phone voice paths.

## Mentra Live: unworn automatic power-off

[MentraOS PR #4734, merged October 23](https://github.com/Mentra-Community/MentraOS/pull/4734), describes consolidating the unworn automatic power-off setting across app and SDK/firmware paths. The proposed default is **ON**, while a user's explicitly saved **OFF** preference is meant to persist on reconnection. The PR also addresses a false success indication from stale OFF acknowledgements.

The author lists component and session tests but says that **physical-device verification of the saved OFF setting and fresh acknowledgement remains pending**. Merge status establishes code integration, not that every production firmware has received or correctly applied it.

**Research disposition:** Preserve the distinction between a saved app preference, a queued command and an actual glasses acknowledgement. Check physical hardware only when a matching released firmware is available.

## Mentra Live: iPhone 17 microphone repair

[MentraOS PR #4862, merged October 20](https://github.com/Mentra-Community/MentraOS/pull/4862), pins BES firmware **26.10.20.0** on staging to address reportedly silent HFP microphone uplink on iPhone 17-class hardware. Its technical account attributes the fault to a one-byte mSBC/eSCO frame alignment error. The contributor reports manual success with a local build on an iPhone 17 and validates the firmware asset's size and hash, but explicitly says the **published 26.10.20.0 artifact itself was not flashed and tested** in that validation.

**Research disposition:** Treat the fix as a concrete firmware and interoperability lead, not as verified fleet-wide resolution. Preserve the exact version and distinguish staging availability from consumer rollout.

## Mentra repository continuity

[MentraOS PR #4933](https://github.com/Mentra-Community/MentraOS/pull/4933), open on October 23, says the team's development has moved after a monorepo cutover and references `Mentra-Community/Mentra`. That destination was **not publicly accessible through the GitHub API at review time**; the upstream statement is preserved as a tracking lead, not proof that a public replacement repository is available.

**Evidence boundary:** All device behavior, test results and rollout statements above are attributed to the respective upstream contributors. GlassesResearch has not independently tested these devices, firmware images, software builds or release channels.
