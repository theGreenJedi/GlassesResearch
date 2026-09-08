# Fieldwork implementation roadmap

## Phase 1 — contracts and public entry

- [x] Progressive v1 question bank.
- [x] 50–100% completion semantics.
- [x] Anonymous-by-default attribution policy.
- [x] Raw-serial non-retention invariant.
- [x] Persisted submission schema forbidding raw serial fields.
- [x] Public Fieldwork contribution page.
- [x] Dedicated CI contract check.

## Phase 2 — installable client

- [ ] Mobile-first installable client.
- [ ] Progressive section renderer driven by the canonical questionnaire JSON.
- [ ] Local draft persistence that does not store raw serials.
- [ ] Local/ephemeral serial fingerprint flow with explicit tests.
- [ ] Canonical GLS model lookup and alias resolution.
- [ ] 50–100% completion calculation and resume-later behavior.
- [ ] Anonymous, pseudonymous, and public-name submission modes.

## Phase 3 — research intake

- [ ] Privacy-preserving submission transport that does not require GitHub.
- [ ] Stable `GR-FW-*` submission IDs.
- [ ] Duplicate-unit detection without exposing device fingerprints.
- [ ] Moderator reconciliation view.
- [ ] Evidence-state transitions separate from completion.
- [ ] Revision lineage so the same owner/unit can add later BLE or firmware findings without being counted as a new independent device.

## Phase 4 — community intelligence

- [ ] Per-model owner-report counts.
- [ ] Independent physical-unit counts where fingerprints are available.
- [ ] Corroborated observation clusters.
- [ ] Firmware/app/version-aware failure-mode tracking.
- [ ] GREP bench-candidate generation from recurring community patterns.
- [ ] Bench-confirmed / not-reproduced / resolved-by-update lifecycle.
- [ ] Unexpected-use and problem-solved synthesis.

## Phase 5 — distribution

- [ ] Signed/reproducible release artifacts where platform permits.
- [ ] Canonical install/download page.
- [ ] QR code pointing to the real install/download route.
- [ ] Checksums/version/release notes.
- [ ] Public source/build documentation.
