# MYVU Open Research — Maturity Review

**Review date:** 2026-09-10  
**Scope:** repository integration layer, not laboratory validation of the hardware claims themselves.

## Decision

**PASS — mature for repository merge.**

The integration layer is ready to become the canonical GlassesResearch MYVU technical knowledge area because its claims are bounded by evidence state, upstreams are version-pinned, community observations retain provenance, hardware identity is separated from branding, and future GR verification has a reproducible evidence-output standard.

This decision does **not** mean that all recorded technical claims are independently verified by GlassesResearch. `GR-VERIFIED` remains reserved for successful GR reproduction on identified hardware/firmware.

## Review gates

### 1. Evidence taxonomy — PASS

The repository distinguishes `UPSTREAM-DOCUMENTED`, `COMMUNITY-REPORTED`, `GR-VERIFIED`, `INFERRED`, and `UNKNOWN / CONFLICTING`. Community reports are not promoted to specifications.

### 2. Source provenance — PASS

Primary upstream repositories are pinned to the snapshots examined for this review:

- Panny777 / Meizu-Myvu-Client: `2a7b4ba975b409cab2acc3d8eba4f1af8e981d79`
- Panny777 / Meizu-Myvu-SDK: `81a2d3243e2c6edfbddfd22932706ebdf2a9d02a`
- FerSaiyan / Alternative-HeyCyan-App-and-SDK: `f3a7d1c2825b5dd7fff52985d98d0388074326a2`

Living branches are treated as changing sources; future upstream changes require an explicit snapshot update and reassessment rather than silently rewriting the evidence base.

### 3. Community-report provenance — PASS WITH DOCUMENTED LIMITATION

The key Imiki pairing, short-runtime, battery and optical observations now retain public contributor names where technically relevant, direct thread/comment links where retrievable, retrieval date and evidence status. The regional/iOS record preserves the source thread and dated sequence of reports.

Where Reddit did not expose a canonical exact comment timestamp through the captured research surface, the record says so rather than inventing precision. This is acceptable provenance because the direct public source and retrieval date remain preserved.

### 4. Hardware-lineage discipline — PASS

The repository does not assume that MYVU, Star Air, Air2, Imiki-branded or visually similar hardware are protocol-identical. XGA010C is the strongest identified target in the current upstream protocol evidence; other variants remain separately qualified until exact identity is established.

### 5. Protocol normalization — PASS

The crosswalk correctly treats CyanBridge's MYVU implementation as downstream adoption of Panny777's transport work rather than independent confirmation. The strongest protocol assertions remain attributed to the Panny777 Client/SDK evidence base.

### 6. Reproducibility — PASS

`TEST-PLAN.md` now requires specimen identity, firmware, host, client/SDK commit, timestamps, procedure, result, raw evidence location, claim under test and evidence-state transition. Protocol conclusions require auditable raw observations; physical/optical conclusions require documented setup/environment.

### 7. Safety / reversibility — PASS

Routine testing excludes reset/recovery flashing, destructive firmware modification, protection bypasses and other difficult-to-reverse operations. Such work requires a separately justified investigation and recovery plan.

### 8. Privacy / publication hygiene — PASS

Public evidence records exclude credentials, API keys, personal message contents and unrelated identifiers. Contributor identities are retained only where they are part of the public technical provenance.

## Claims specifically re-checked during maturity review

- The documented XGA010C transport is BLE-first followed by Classic Bluetooth RFCOMM.
- Panny777 documents StarryNet service `0x0BD1`, Air characteristics `0x2020–0x2023`, and V2 `0x2010–0x2012`.
- Panny777 documents a 3-second urgent-characteristic heartbeat and per-session RFCOMM UUID synchronization.
- Panny777 documents P-256 ECDH and the RunAsOne/ability-authentication sequence.
- CyanBridge explicitly credits Panny777's MYVU BLE, ECDH, RFCOMM relay, heartbeat and display transport; this is reused upstream work, not independent protocol discovery.
- Imiki pairing, short shutdown/runtime, battery and rainbow-artifact items remain community reports only.
- Regional Android/iOS/app-account behavior remains fragmented owner evidence and must not be generalized across the MYVU family.

## Remaining research gaps — expected, not merge blockers

- No GlassesResearch specimen has yet converted the protocol claims to `GR-VERIFIED`.
- Exact Imiki hardware/model/firmware identity is unresolved.
- Air/Air2/Imiki lineage relationships require hardware and Bluetooth-service comparison.
- Regional official-app behavior needs a controlled OS × app-region × hardware × firmware matrix.
- Battery and optical observations need controlled bench reproduction.

These are the purpose of the research program, not defects in the integration layer.

## Site disposition

**No site placement selected in this mission.** After merge, this material can remain a repository research asset until GlassesResearch chooses the most useful public entrance on the site. The eventual site surface should link to the canonical research area rather than duplicate a second drifting copy of the technical record.
