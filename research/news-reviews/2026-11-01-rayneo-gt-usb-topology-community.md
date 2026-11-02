# RayNeo GT 20260922 USB topology: community regression and corrected compatibility report — November 1, 2026

<!-- news_promotion_schema: 1 -->

**Review date:** 2026-11-01  
**Original report:** 2026-10-06; important correction 2026-10-07  
**Affected devices as reported:** RayNeo GT and GT Max, firmware `20260922`; third-party IMU/3DoF software  
**Disposition:** `archive/review` as a firmware/owner-interoperability case study, **not** a new breaking-news Wire item or a verified device defect.

## Firsthand community claims, with provenance

- [Original r/RayNeo technical post](https://www.reddit.com/r/RayNeo/comments/1wzcua4/warning_new_gt_series_fw_update_22_sept_2026/) by `u/ivan_p046` (October 6): reports a changed Windows USB enumeration for GT-series firmware `20260922`. The author's before/after listings show the prior composite USB `VID_3941&PID_AF50&MI_XX` interface paths disappearing, with a bare HID path `VID_3941&PID_AF50`. They propose a new HID discovery method and unchanged IMU packet decoding. This is **user-supplied diagnostic text**, not an independent USB capture by GlassesResearch.
- [October 7 replies in the same original discussion](https://www.reddit.com/r/RayNeo/comments/1wzcua4/warning_new_gt_series_fw_update_22_sept_2026/): one user says **VertoXR 0.2.9 failed** on firmware `20260922` despite working on `20260907`; the same commenter then **corrects** the blanket warning, reporting that **VertoXR 0.2.10 works** with `20260922`, though OpenTrack yaw drift remained under the Fusion tracking mode and improved when switched to Plain. The developer replied acknowledging the behavior and intended fix. Preserve the correction alongside the initial alarm; never repeat the headline's blanket 'all third-party 3DoF software is broken' claim as fact.
- [VertoXR official supported-glasses page](https://vertoxr.com/) lists RayNeo GT and GT Max and current downloadable builds (Windows `0.2.11` in the inspected page). This confirms advertised support, **not** successful testing on every firmware/OS combination.
- [VertoXR maintainer repository](https://github.com/rohitsangwan01/Verto_XR) and [RayNeo GT Max compatibility issue #18](https://github.com/rohitsangwan01/Verto_XR/issues/18): additional maintainer/community technical context, including GT Max USB `VID 0x3941`/`PID 0xAF50` reported on macOS in August 2026. The August issue predates the September firmware and does not corroborate the claimed September enumeration change.
- [Separate GT Max display-reset anecdote](https://www.reddit.com/r/RayNeo/comments/1wxsz0z/issue_with_rayneo_gt_max_right_lens_going/) (October 4): a user reports white/gray right lens and display restarts after `20260922` update. Distinct symptom; **do not conflate** with USB 3DoF enumeration or infer shared root cause.

## Practical significance and boundaries

The report is a concrete example of why firmware version, **USB interface descriptors**, host OS, app version and tracking mode must all be preserved in a smart-glasses compatibility claim. A vendor firmware update can change third-party device discovery without proving the underlying IMU stopped transmitting. The original post's proposed 65-byte HID report handling is a community hypothesis and implementation guide, **not** a GlassesResearch-verified protocol specification.

No GlassesResearch unit was connected, no descriptor dump was reproduced, and no manufacturer change log or independently captured USB enumeration was obtained. The community correction means a blanket 'avoid all updates' advisory would be misleading. AirPin, Decky XR, RayNeo's Android app and all other named applications have **not** been independently rechecked here. Do not provide firmware downgrade instructions or endorse unofficial firmware files.

## Publication state

The [actual public Across the Wire JSON feed](https://glassesresearch.org/data/wire-feed.json) was inspected in this scour. The original report and its correction are October events; preserve this as a dated, attributed research backfill in the existing review workflow, **not** a fabricated fresh Wire headline. The inspected feed snapshot is not evidence of a broken publisher. No generated feed file was edited and no live publication is claimed.

**Evidence classification:** community-reported USB change and specific compatibility observations; maintainer site supports product/app identity; **no independently reproduced firmware defect or universal incompatibility**.
