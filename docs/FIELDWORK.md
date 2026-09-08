# Fieldwork

**Fieldwork is the GlassesResearch community field-research app.**

Own or have hands-on access to smart glasses? Fieldwork lets you contribute in minutes—or go as deep as you want.

<div class="fieldwork-privacy-promise">
<strong>Anonymous is welcome.</strong><br>
<strong>Attribution is optional.</strong><br>
<strong>Raw serial numbers are never retained.</strong>
</div>

If you provide a serial number, Fieldwork uses it only to create a one-way device fingerprint for duplicate detection. The raw serial must not be stored, published, exported, placed in logs, or used for visitor profiling. Anonymous and attributed submissions receive the same evidentiary treatment.

[Read the short privacy explanation](PRIVACY.md#fieldwork)

## Five minutes helps. An hour helps. You decide.

Fieldwork begins with easy questions:

- What model is it?
- Why did you buy it?
- What problem were you trying to solve?
- What has it actually solved?
- Was the marketing truthful?
- Would you buy it again?

Then, if you want to keep going, it progressively opens deeper field-research questions about firmware, software, battery behavior, owner control, BLE, USB, network behavior, developer access, and reproducible technical evidence.

The current v1 instrument contains **68 questions across eight sections**. It is intentionally progressive: nobody is expected to answer all 68.

## Your Fieldwork Completion score

Every valid contribution starts at **50% Fieldwork Completion**.

The remaining 50 percentage points reflect how much of the optional instrument you completed. Answer everything and you reach **100%**.

**Completion is not credibility.** A 100% submission is not automatically more truthful than a 55% submission. Evidence confidence is determined separately through provenance, corroboration, reproducibility, technical specificity, and—where applicable—GlassesResearch bench testing.

Choosing **I don't know / not tested** is a valid research answer. Fieldwork must never pressure a contributor to guess for points.

## One physical unit, one device fingerprint

We would ideally like the exact model number and serial number because they help distinguish independent devices from repeat submissions involving the same physical unit.

Fieldwork therefore separates three concepts:

- **Contributor identity** — anonymous, pseudonymous, or publicly attributed.
- **Device identity** — a one-way duplicate-check fingerprint derived from model + serial when voluntarily supplied.
- **Research evidence** — what the contributor actually observed.

A contributor can remain completely anonymous while still allowing GlassesResearch to recognize that two submissions came from the same physical device.

The fingerprint prevents accidental double-counting; it is **not** a contributor-tracking identifier and must not be exposed publicly.

## What Fieldwork asks

### 1. The glasses in your hands

Exact model, retail alias, model number, optional serial for duplicate detection, hardware revision, region, acquisition date, and how the contributor got access.

### 2. Why you chose them

Purchase motivation, intended problem, alternatives considered, price, current use, problems actually solved, and unexpected uses.

### 3. Wearing them

Comfort, fit, balance, heat, controls, prescription experience, and social acceptability.

### 4. What actually works

Observed battery life, calls, audio, camera, display, translation, visual AI, reliability failures, and missing expected capabilities.

### 5. Marketing versus reality

Was the marketing truthful? Which claim proved true? Which claim was misleading? What exceeded expectations? Would the owner buy them again?

### 6. Software and owner control

Firmware, app and host versions, account/cloud requirements, permissions, offline behavior, data export, updates, and owner-controlled functionality.

### 7. Go deeper — optional technical fieldwork

BLE advertised identity, services, characteristics and state changes; Wi-Fi behavior; USB identity; SDK/API/debug paths; network observations; reproducible technical evidence.

### 8. Your assessment

Best thing, worst thing, one change you would make, disclosure, attribution choice, and a large free-form space to tell future owners and GlassesResearch whatever matters.

The canonical v1 question set is maintained in [`data/fieldwork-questionnaire.v1.json`](../data/fieldwork-questionnaire.v1.json).

## What happens to a submission

Fieldwork submissions remain **community evidence** unless and until stronger evidence supports a different label.

A single valid owner report can become an independent hands-on observation. Compatible reports from unrelated physical units can become corroborated community evidence. Recurring patterns can become failure-mode or compatibility leads. Strong patterns can generate a targeted GREP bench test. Bench reproduction can then confirm, fail to reproduce, or refine the original community hypothesis.

**Community repetition never silently becomes GlassesResearch Verified.** The evidence standard still applies.

## Attribution

You choose:

- **Anonymous** — no public contributor identity.
- **Pseudonym / handle** — credit a persistent public handle.
- **Public name** — use the name you provide.

Anonymous submissions are not second-class submissions. Attribution changes public credit, not the evidence rules.

## Download / install

The installable Fieldwork client is being built as a lightweight, privacy-first companion to GlassesResearch. The permanent public entry point will live here under **Contribute**, with a QR code for quick phone installation once the signed/distributable client is published.

Until that client is ready, the existing [independent hands-on review intake](COMMUNITY_REVIEWS.md) remains available and feeds the same evidence philosophy.

## Design contract

Fieldwork must remain:

- progressive rather than a wall of questions;
- useful after only a few minutes;
- capable of deep technical fieldwork;
- anonymous by default;
- explicit that raw serials are never retained;
- free of advertising and behavioral profiling;
- careful not to confuse completion with credibility;
- evidence-preserving rather than popularity-driven;
- compatible with future targeted questions for models where GlassesResearch has known research gaps.

**Own glasses? Help characterize them. Five minutes is useful. Go as deep as you want.**
