# Comparison Engine

Compare researched smart-glasses records side by side using the same evidence-backed field definitions.

<div id="comparison-engine-app">
Loading comparison data…
</div>

## How to use it

Choose two researched device records above. The comparison updates immediately, highlights differing values, exposes supporting source links, and keeps unsupported fields visible as **Unknown**.

The URL records the selected pair, so a comparison can be shared directly. The print control produces a cleaner printable view.

## What the engine does

- uses one canonical comparison schema across devices;
- preserves field-level source links;
- shows missing research as **Unknown** rather than treating omission as “No”;
- provides shareable pair URLs;
- supports print-friendly output;
- highlights differences without declaring a winner;
- leaves rankings and purchase recommendations outside the engine itself.

## Current researched coverage

The initial research set deliberately spans different device categories so the same schema is exercised across camera/audio glasses, discreet display glasses, tethered XR displays, enterprise HUDs, and open developer hardware:

| GLS ID | Device | Research emphasis |
|---|---|---|
| `GLS-0003` | Ray-Ban Meta (Gen 2) | camera/audio, companion-app dependence, battery and connectivity |
| `GLS-0039` | W610 | hands-on project observations; unsupported specifications remain Unknown |
| `GLS-0048` | Even G2 | discreet display, prescription support, BLE, battery, cloud-dependent features |
| `GLS-0051` | Brilliant Labs Frame | open hardware/software, BLE protocol, firmware and developer access |
| `GLS-0056` | Vuzix Z100 | enterprise monocular display, SDK access, BLE and runtime |
| `GLS-0074` | XREAL One | tethered XR display, optics, audio, compute and wired power/data path |

This is a research seed set, not a claim that these devices are the market's best or most important products. Additional models belong here as evidence is acquired.

## Evidence discipline

Every populated field carries an evidence state and at least one source in the underlying research record. Missing fields normalize to **Unknown**.

A manufacturer omission is not proof that a feature is absent. Negative values such as `camera_count = 0` are recorded only when the supporting evidence establishes them.

Conflicting credible sources should remain visible rather than being silently reconciled. See [Research Standards](RESEARCH_STANDARDS.md).

## Technical sources

- Canonical schema: [`comparisons/schema.json`](../comparisons/schema.json)
- Validator and normalizer: `scripts/build_comparison_engine.py`
- Model research records: `comparisons/data/GLS-####.json`
- Generated site bundle: `/data/comparisons.json`

The comparison framework is complete; future work should primarily increase the amount and quality of verified device data rather than expand the comparison machinery.
