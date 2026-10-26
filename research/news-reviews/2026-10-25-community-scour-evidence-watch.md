# Community evidence survey — October 25, 2026

**Review scope:** Public Reddit owner reports, CyanBridge issue tracker, MentraOS pull requests, independent technical reporting, and the live public Across the Wire feed. Public Discord/Facebook posts and YouTube material were searched where indexed; no unverified private-group content was treated as evidence.  
**Source class:** Public primary owner/developer records plus attributed secondary reporting.  
**Review boundary:** A community report is not GlassesResearch hardware verification; an upstream PR or CI result is not proof of production rollout.

## Disposition: attributed publication — Ray-Ban Meta unexpected voice-activity entries

- **Event:** October 13–25, 2026.
- **Primary:** [r/RaybanMeta original owner thread](https://www.reddit.com/r/RaybanMeta/comments/1x4n96n/warning_my_rayban_meta_glasses_are_recording/).
- **Independent press / vendor response:** [Ars Technica, October 16](https://arstechnica.com/gadgets/2026/10/ray-ban-meta-smart-glasses-found-recording-audio-without-wearers-consent/).
- **Observed claim:** One owner reports unintended saved audio/transcripts on three pairs; additional commenters describe light activation, some also saved logs. Meta told press the issue was resolved, without publishing a cause or fixed build. The original owner later disputed resolution.
- **Evidence limits:** No independent GlassesResearch reproduction, fleet prevalence, trigger diagnosis, video capture, or network-exfiltration evidence. The company statement and subsequent owner claim are in tension.
- **Scope:** `core_glasses`. **Disposition:** `publish` as attributed/disputed news, not Verified. **Destination:** `docs/news/articles/2026-10-25-meta-rayban-unprompted-audio-owner-reports.md`, linked from `docs/RESEARCH_NEWS.md`.
- **Follow-up:** Firmware/app version fingerprint, consent-aware reproduction, voice-activity log and data-path controls.

## Disposition: community profile update / follow-up — CyanBridge local-model workflow

- **Event:** October 25, 2026.
- **Primary:** [CyanBridge issue #33](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/issues/33).
- **Observed claim:** An owner of M02S-C670 on LineageOS/8 GB RAM says local Gemma 4 e2b IT loads but glasses-button voice/image questions do not work. They also ask about local STT, firmware rollback, an Aliyun OSS hostname request, and other owner-control topics.
- **Evidence limits:** No reproducible logs or upstream maintainer response as reviewed. The hostname observation does not establish what data was sent. Requests to disable capture indicators are not endorsed.
- **Scope:** `core_glasses`. **Disposition:** `watch`; preserve attributed report in `docs/community-research/cyanbridge.md`, no device rating or compatibility claim.
- **Follow-up:** Device/firmware tuple, audio-to-STT and camera-to-vision data path, logs and network-request purpose.

## Disposition: watch — Ray-Ban Meta Gen 1 post-battery-repair intermittent functions

- **Event:** October 22, 2026.
- **Primary:** [r/RaybanMeta owner log report](https://www.reddit.com/r/RaybanMeta/comments/1xcgknj/after_a_battery_replacement_right_speaker_right/).
- **Observed claim:** Owner reports that the right speaker and touchpad stop responding after unfolding or wear detection following a battery replacement; reboot restores both. They supply a firmware identifier and selected internal log lines. They also report a weak microphone and missing wake-word response.
- **Evidence limits:** Single self-reported repair and log interpretation. Flex-cable disturbance, reinitialization and microphone blockage are **hypotheses**, not proven causes. No independent disassembly or repair test.
- **Scope:** `core_glasses`. **Disposition:** `watch` for repairability and hinge/wear-sensor research; not eligible for a verified working repair guide.
- **Follow-up:** Corroborating independent repair cases, exact part/connector identification, reversible diagnostic tests with safety and recovery boundaries.

## Disposition: watch — Mentra miniapp audio state

- **Event:** PR opened October 22, updated October 25, 2026.
- **Primary:** [MentraOS PR #4918](https://github.com/Mentra-Community/MentraOS/pull/4918).
- **Observed claim:** Upstream proposes to keep miniapp streamed-speaker state and cancellation ownership synchronized when playback, speech and stream-open requests overlap. Author reports local tests.
- **Evidence limits:** PR remained **open** at review, with red CI gate and no physical-device confirmation. This is not a shipped fix or a reproduced GlassesResearch defect.
- **Scope:** `core_glasses`. **Disposition:** `watch`; revisit after merge, green CI, identified release, and device tests.

## Review closeout

- Duplicated secondary coverage of the Meta reports was consolidated to the original owner account and independent reporting of Meta's response.
- No canonical hardware capability or Report Card score was changed.
- Across the Wire was checked live; publication of the new site content must be confirmed on the live page after deployment, not inferred from commits.
- No private social group material or unverifiable claims were promoted.
