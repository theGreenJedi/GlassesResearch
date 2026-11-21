# Community scour — Rokid Lumen and Neural Band interoperability (2026-10-29)

<!-- news_promotion_schema: 1 -->

**Survey date:** 2026-10-29  
**Discovery lane:** Public GitHub repository, release history, maintainer technical/security documents, independent community project directory, indexed web/Reddit. Public Discord/Facebook posts and YouTube material were searched only where accessible/indexed; no private-channel access or hardware test.  
**Scope:** Smart-glasses community development and owner control; existing developer resources, not a new public content category.

## Finding — unofficial Meta Neural Band input for Rokid RG

- **Disposition:** `archive / resource backfill` into existing community directory and open development ledger; **not** a fresh October 29 product launch or independently verified interoperability.
- **Primary project:** https://github.com/beyondlevi/rokid-lumen
- **Release evidence:** https://github.com/beyondlevi/rokid-lumen/releases — versioned beta artifacts, including 0.2.0-beta.28 dated October 13, 2026 on the public release page.
- **Protocol and test evidence:** https://github.com/beyondlevi/rokid-lumen/blob/main/NEURALBAND.md — maintainer's unofficial Bluetooth/L2CAP bridge and documented gesture/handwriting tests; distinguish author-run tests from GlassesResearch reproduction. The Meta Wearables Device Access Toolkit is for glasses interfaces, **not** a documented third-party Android Neural Band gesture API.
- **Device boundary:** https://github.com/beyondlevi/rokid-lumen/blob/main/docs/getting-started.md — documented target is Rokid RG glasses on YodaOS-Sprite, with Android phone companion and a Meta Neural Band. Do not extrapolate to Rokid Max, other Rokid generations, or all Meta glasses.
- **Security evidence:** https://github.com/beyondlevi/rokid-lumen/blob/main/docs/security.md — maintainer acknowledges persistent TCP ADB listener on port 5555 across joined networks after self-arm, still requiring trusted ADB keys; file-mediated external-storage IPC and key import; phone hotspot proxy without per-session authentication; unencrypted web-app secrets in private preferences. These are **maintainer-disclosed design risks**, not an independently verified compromise or GlassesResearch security audit.
- **Independent discovery pointer:** https://github.com/Anezium/awesome-rokid — community-maintained index listing Lumen and related Rokid projects. This is discovery corroboration, **not** independent replication of the protocol or security properties.
- **Secondary context:** https://www.metaversewatcher.io/rokid-lumen-meta-neural-band-rokid-glasses-adb-port-5555/ — October 7 coverage, used for discovery only; technical claims were checked against maintainer-authored sources.

## Research disposition and publication boundary

The resource is materially useful for cross-vendor input, owner-controlled companion systems and the tradeoff between expanded device authority and exposed debugging surfaces. It is **not** a zero-day disclosure: the project documents these security issues itself. Do not imply Meta or Rokid support this integration, or that GlassesResearch reproduced the hardware results.

**Across the Wire:** the live public [JSON Wire feed](https://glassesresearch.org/data/wire-feed.json), [Research & News](https://glassesresearch.org/docs/RESEARCH_NEWS/) and homepage were checked before disposition. The public feed contains dated October 29 discovery items for XREAL Aura, Rokid Glasses 2 and Android XR developer tooling; they are already in the existing discovery conveyor and must not be duplicated as independent events. This October 7–13 development is an archival technical backfill, **not a new October 29 wire event**. Do not hand-edit generated feed JSON, create a new feed, or invent a wire candidate ID. If a genuinely new upstream release or independently demonstrated exploit emerges, send it through the existing attributed source-intake and editorial-review process with its real date and provenance.

**Canonical destinations:** `resources/COMMUNITY_AND_DEVELOPMENT.md` and `hacking/OPEN_HACKING_RESOURCE_LEDGER.md`. No model spec, score, compatibility-matrix assertion, or Verified article changed.

## Verification and remaining work

- [x] Primary GitHub project, release page, Neural Band notes, getting-started and security documentation inspected.
- [x] Compared against existing GlassesResearch developer directory/ledger; no Lumen entry existed at review time.
- [x] Maintainer claims and limits preserved without promoting to GlassesResearch verification.
- [x] Existing public Wire/newsroom surface inspected; no publication inferred from repository edits.
- [ ] Re-read branch files and run repository CI before merge.
- [ ] Verify deployed pages independently after a qualified merge before claiming live publication.
- [ ] Hardware testing, security assessment and compatibility beyond the named Rokid RG target remain open.

**Preservation:** Link to project-owned source and release artifacts; do not mirror third-party firmware, credentials, private keys or binaries.
