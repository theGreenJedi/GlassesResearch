# Community development-resource survey — October 28, 2026

<!-- news_promotion_schema: 1 -->

**Survey date:** 2026-10-28  
**Candidate window:** 2026-10-09 to 2026-10-28 (with older high-value resources backfilled)  
**Candidate files reviewed:** Public GitHub repository READMEs, release pages, commit histories, and attributed Reddit discussion; discoveries made outside the generated wire, so no fabricated wire candidate IDs.  
**Reviewer:** GlassesResearch community scour

## Executive summary

- Candidates reviewed: five development-resource families
- Unique developments after deduplication: five
- Publish: one fresh primary-source firmware release into canonical developer resources
- Watch / archival backfill: four previously released community or research resources
- Public Wire: current public feed and repository wire state inspected; **no manual edit to generated wire data** and no claim of live publication from this review

## Publish — Brilliant Labs Halo firmware owner-build route

- **Scope lane:** `core_glasses`
- **Disposition:** `publish` — canonical development-resource documentation, **not** GlassesResearch hands-on verification
- **Institution test:** yes; firmware source, build instructions, BLE protocol and owner flashing route remain useful beyond a news cycle
- **Event date:** 2026-10-27 (official release `0.8.23`)
- **Discovery date:** 2026-10-28
- **Best primary source:** https://github.com/brilliantlabsAR/halo-firmware/releases/tag/0.8.23 and https://github.com/brilliantlabsAR/halo-firmware
- **Independent context:** none required to establish that the official source repository and release exist; device behavior and recovery claims have **not** been independently reproduced
- **What changed:** Brilliant Labs publishes Halo firmware as a Zephyr/Alif Balletto workspace with on-device Lua, BLE APIs, owner-build/OTA instructions, and MCUboot test-boot/auto-revert as documented by the maintainer. The October 27 release provides a concrete dated artifact.
- **Affected models:** Halo (no model-specification or score changes; resource-only)
- **Affected lineages / platforms / resources:** Brilliant Labs Halo; `hacking/OPEN_HACKING_RESOURCE_LEDGER.md`; `resources/COMMUNITY_AND_DEVELOPMENT.md`
- **Canonical destinations:** `hacking/OPEN_HACKING_RESOURCE_LEDGER.md`, `resources/COMMUNITY_AND_DEVELOPMENT.md`
- **Uncertainty / contradictions:** Owner flashing support and rollback are manufacturer-authored documentation, not a GlassesResearch device test. Repository is **mixed-license** (Halo-specific Apache-2.0, Alif SDK license, vendored component terms), not uniformly Apache-2.0.
- **Candidate IDs / intake dates:** none — discovered through direct GitHub review; do not fabricate a wire item or imply it appeared on the live feed

## Watch / archival backfill — existing independent development paths

- **OpenSQZ Glass / OpenGlass** — https://github.com/OpenSQZ/OpenGlass — research prototype; local-first nearby-host inference and published hardware/build files; September 30 Rokid adapter update. **Disposition:** `watch` for reproducible host/device tests, not a newly shipped commercial model.
- **OpenSource-Ai-Glasses / OSAIG** — https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses — v0.7.0 dated May 8; RV1106B Linux software/SDK and hardware-specific firmware caveats. **Disposition:** `archive` as a reusable development path, not a claim of wholly open hardware.
- **Even Realities WebFlasher** — https://github.com/AM-Guru/evenRealities-webflasher and https://www.reddit.com/r/EvenRealities/comments/1vmz7gs/were_open_sourcing_part_of_our_even_realities/ — August release, October 9 code update; official-firmware-only owner recovery/inspection with **no dead-temple recovery** and explicitly unvalidated experimental case write path. **Disposition:** `watch` for independently replicated safety/repair outcomes; not a universal repair procedure.
- **Panny777 MYVU XGA010C SDK/client** — https://github.com/Panny777/Meizu-Myvu-SDK and https://github.com/Panny777/Meizu-Myvu-Client — July research, **already preserved** in `research/investigations/COMMUNITY_MYVU_XGA010C_PANNY777_2026-09-06.md`; now cross-linked in the existing public resource directory. **Disposition:** `archive` this discovery gap, not a second independent source.

## Canonical follow-up and boundaries

- [x] Publicly useful source paths added to existing canonical resource pages.
- [x] Source/claim lanes distinguished; manufacturer documentation and independent developer reports are not GlassesResearch lab results.
- [x] Model, lineage and comparison implications reviewed: no supported model-spec or scoring change.
- [x] Duplicate MYVU work linked to existing research rather than restated as new verification.
- [x] Fresh Halo release recorded with date and direct primary source.
- [x] No new public category, feed, or automation plumbing created.
- [ ] Deployed-page verification remains required before claiming public publication; a GitHub merge alone is insufficient.
- [ ] Future firmware/OTA testing requires appropriate device, version, backup and safety controls.

**Preservation choice:** Direct source links and immutable GitHub commit snapshots where available; third-party firmware and SDK binaries are not redistributed without separate licensing and integrity review.
