# Fieldwork

Fieldwork is the GlassesResearch community field-research app.

It is designed for a spectrum of contributors: someone who bought a pair of smart glasses yesterday and wants to answer a few useful questions, through advanced contributors inspecting BLE, USB, firmware, network behavior, or reproducible failure modes.

## Product contract

Fieldwork must satisfy these invariants:

1. **Progressive depth.** A contributor should be able to produce a useful submission quickly and stop at any time.
2. **50–100% completion.** Every valid submission begins at 50%; optional answered questions advance toward 100%. Completion is never a credibility score.
3. **Anonymous by default.** Attribution is optional and does not change evidentiary treatment.
4. **No retained raw serials.** A serial number may be volunteered for duplicate-device detection but must be transformed into a one-way fingerprint before persistence. Raw serial material must not enter logs, analytics, crash reports, exports, issue bodies, or public records.
5. **Community evidence stays community evidence.** Popularity does not silently promote a report to GlassesResearch Verified.
6. **Version context matters.** Firmware, app, host OS, region, and date should accompany technical claims whenever known.
7. **Unknown is valid.** Contributors must be able to say they did not test or do not know rather than guessing for completion points.
8. **Targeted follow-up.** The client may eventually append model-specific questions derived from known GlassesResearch research gaps.

## Initial application surfaces

### Start

- short explanation of Fieldwork;
- three-line privacy promise;
- start anonymously by default;
- optional attribution choice;
- model lookup.

### Progressive questionnaire

The canonical question bank lives in `data/fieldwork-questionnaire.v1.json`. The client should present one small section at a time rather than a single long form.

### Completion indicator

Show `Fieldwork Completion` prominently as 50–100% after minimum submission fields are satisfied.

Never label this value trust, confidence, reputation, verification, quality, expertise, or accuracy.

### Review before submit

Before persistence, clearly show:

- chosen attribution mode;
- model identity;
- whether a serial-derived device fingerprint will be included;
- completion percentage;
- evidence links/files;
- a reminder that the contribution remains community evidence pending moderation/corroboration.

### Contribution history

Returning contributors may reopen a prior local/session contribution and add observations later. Revisions from the same physical unit must update the same device-level contribution lineage rather than inflate independent-unit counts.

## Device duplicate detection

The research goal is to recognize when multiple submissions likely involve the same physical device while avoiding retention or publication of serial numbers.

Implementation requirements:

- normalize model identity before fingerprinting where possible;
- transform the serial before any durable write;
- persist only the resulting device fingerprint;
- never expose the fingerprint publicly;
- never use the fingerprint as a cross-site/user behavioral identifier;
- do not treat two reports with the same fingerprint as independent corroboration;
- allow reports without a serial/fingerprint;
- make duplicate detection a research-quality aid, not an eligibility requirement.

The final cryptographic construction must receive a separate implementation review before production deployment. The privacy promise is stricter than the initial implementation convenience: if a proposed telemetry/logging stack could capture the raw serial, it cannot be used as-is.

## Evidence lifecycle

Suggested states:

`community_reported` → `independent_hands_on` → `corroborated_community` → `bench_candidate` → (`bench_confirmed` | `not_reproduced`) → optionally `resolved_by_update`

Promotion between states must depend on evidence, not completion score or vote count alone.

## Data artifacts

- Questionnaire: `data/fieldwork-questionnaire.v1.json`
- Persisted submission contract: `data/fieldwork-submission.schema.json`
- Public product page: `docs/FIELDWORK.md`
- Privacy policy: `docs/PRIVACY.md#fieldwork`

## Distribution

The intended public entry point is GlassesResearch → **Contribute → Fieldwork**.

Once an installable client exists, the page should expose:

- direct install/download route appropriate to each supported platform;
- QR code to the canonical Fieldwork install page;
- checksum/signature information for downloadable builds where applicable;
- version and release notes;
- source link.

Do not display a QR code that points to a placeholder or non-download page as though it installs the app.

## MVP sequence

1. Freeze question/data/privacy contracts.
2. Build an installable client with progressive sections and local completion calculation.
3. Implement serial-to-fingerprint handling with tests proving raw serial absence from persistence/logging.
4. Add model lookup against the canonical GlassesResearch catalog.
5. Add authenticated or anonymous submission transport without requiring a public GitHub account.
6. Build moderation/reconciliation intake on the GlassesResearch side.
7. Surface aggregate community intelligence on model pages without exposing device fingerprints or anonymous contributor identity.
8. Publish signed/distributable builds and generate the canonical download QR code.

## Non-goals for the first release

- social network;
- follower counts;
- likes/upvotes as evidence;
- contributor ranking by completion;
- mandatory identity;
- mandatory serial number;
- automatic promotion to Verified;
- advertising or behavioral analytics.
