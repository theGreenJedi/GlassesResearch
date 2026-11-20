# Mentra Bluetooth SDK 3.3.0 promotion and touchpad-control boundary — November 1, 2026

<!-- news_promotion_schema: 1 -->

**Discovery/review date:** 2026-11-01  
**Source event:** 2026-10-31 production SDK 3.3.0 example-package promotion; underlying touchpad-control code merged 2026-10-16  
**Scope:** Mentra Live; MentraOS-compatible glasses only where model/firmware capabilities are explicitly supported  
**Disposition:** `review` for an attributed developer-release item through the **existing Across the Wire editorial intake**; preserve durable SDK evidence. Not a GlassesResearch physical test or a claim that every model implements the controls.

## Primary evidence, dated

- [Mentra Bluetooth SDK Starter Kit](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit), [main synchronization merge #589 / commit 3b87b61](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/commit/3b87b61a244274013822a0878f19d269c7049fc7) (2026-10-31): source-repository evidence that the example release train was synchronized to 3.3.0.
- [Production promotion commit c5507c4](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/commit/c5507c4f874f0bb149ac2e5db3455bccde5a4c8d) (2026-10-31): maintainer says example pins switched from `3.3.0-beta.1188` to production `3.3.0` published on npm, Maven Central and SwiftPM. This is a maintainer release assertion, not an independently installed package or tested binary.
- [SDK README](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/blob/main/README.md), [getting started](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/blob/main/docs/getting-started.md), [hardware notes](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/blob/main/docs/hardware-integration.md) and [production checklist](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/blob/main/docs/production-checklist.md): documented Android, iOS, React Native, native macOS and React Native macOS integrations; capability gating and privacy requirements.
- [MentraOS SDK PR #4802](https://github.com/Mentra-Community/MentraOS/pull/4802), merged October 16 into `dev`: source and test record for `setTouchGestureDefaultBehaviorEnabled(gesture, enabled)`, including eight independently configurable gestures, acknowledgement correlation and reconnect reset semantics. It links firmware BES 26.10.16.0 and [firmware PR #95](https://github.com/Mentra-Community/mentra-live-bes/pull/95), whose private/unavailable source was **not** independently inspected.
- [Starter Kit README, Touchpad default actions section](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/blob/main/README.md#touchpad-default-actions-os-2123): example UI and explicit physical test plan; **physical hardware verification is marked pending**.

## Specific engineering finding

The SDK's per-gesture API is designed to suppress **stock** Mentra Live media/touchpad actions while still delivering touch events to the owner app. It is an owner-control improvement because an app cannot suppress a firmware-originated media action merely by ignoring its event. It requires compatible firmware with `cs_tpdef`, waits for a correlated settings acknowledgement, rejects unsupported models and invalid gesture names, and resets overrides on BLE disconnect or reboot. The repo documents eight switches in the example apps. Code and automated test claims are available, but no GlassesResearch hardware test was run; the maintainer's physical validation remains pending.

Do **not** inherit this control into Even G2, Vuzix Z100 or other supported SDK models: the [model differences](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/blob/main/docs/hardware-integration.md) expressly distinguish camera-equipped, speaker-equipped Mentra Live from display-only G2 and require capability gating. The [release list](https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit/releases) also includes a `3.4.0` example-build **pre-release**; do not describe 3.3.0 as the numerically newest artifact or treat pre-release and production promotion as interchangeable.

## Existing GlassesResearch context and publication boundary

This is a dated addendum to existing [EV-0060 Mentra SDK/OTA owner-control evidence](../../evidence/EV-0060-Mentra-Bluetooth-SDK-OTA-owner-control.md), not a new device identity, report-card score or duplicate resource listing. EV-0060 already documents direct host-to-glasses control, version-linked OTA manifests and default PostHog telemetry/opt-out; the new SDK version does not nullify those privacy qualifications.

The [actual public Across the Wire JSON feed](https://glassesresearch.org/data/wire-feed.json) was retrieved for this review. No `Mentra` or `SDK` string appeared in the inspected feed snapshot. Feed retrieval may be cached; this **does not establish a publication failure**, nor does it justify hand-editing generated feed data or inventing an item. Route the dated release as an attributed developer candidate through the established intake. Check the deployed public feed and target URL after any merge/deployment before claiming publication.

**Evidence classification:** verified *existence of source commits and public documentation*; manufacturer/maintainer-attributed functional and package-availability claims; **unverified on GlassesResearch hardware**. No APK, firmware, private repository contents or third-party binaries mirrored.
