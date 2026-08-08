# Device Comparison Engine

GlassesResearch compares devices from evidence, not from prose written to favor a winner. This directory defines the comparison schema and rendering rules. It intentionally does **not** publish model-vs-model conclusions yet.

## What PR #40 establishes

The comparison engine has four responsibilities:

1. define one canonical field schema for every device;
2. accept any two or more device records without requiring special-case code;
3. render unknown or unresearched fields explicitly instead of guessing;
4. carry field-level evidence status and source references alongside every value.

The engine is infrastructure. Populating comparison values is separate research work.

## Comparison schema

The canonical schema is stored in [`schema.json`](schema.json). Fields are grouped by research domain:

- identity and lifecycle;
- physical hardware;
- display and capture hardware;
- audio;
- compute and sensors;
- connectivity;
- software and companion applications;
- developer access and openness;
- repairability and hardware research;
- regulatory/documentation resources;
- evidence and review state.

Every field has a stable machine name, human label, group, value type, and unknown-value policy.

## Evidence states

The renderer supports four field-level evidence states:

| State | Meaning |
|---|---|
| `hands-on` | directly verified by GlassesResearch |
| `community` | attributed community verification |
| `primary` | manufacturer, project, regulatory, or other primary-source claim |
| `unknown` | no reliable comparison value has been recorded |

A value and its evidence state are separate. For example, `camera_count = 2` with `primary` evidence is not equivalent to a hands-on count of two cameras.

## No silent inference

The engine must never infer that a missing field means `false`, `0`, unsupported, or unavailable. Missing research renders as **Unknown**.

This rule is especially important for openness fields such as SDK access, bootloader state, firmware availability, repairability, and offline operation. Absence of documentation is not proof of absence.

## Input format

Model comparison data will live in `comparisons/data/<GLS-ID>.json` as it is researched. A record contains only fields that have actual evidence; missing fields remain absent.

Example shape:

```json
{
  "id": "GLS-0039",
  "fields": {
    "bluetooth": {
      "value": true,
      "evidence": "hands-on",
      "sources": ["models/W610/ble/README.md"]
    }
  }
}
```

The example above documents the format only. PR #40 does not create model comparison records.

## Renderer

`scripts/build_comparison_engine.py` validates the schema and any future comparison records, then produces a normalized JSON bundle for the website. The bundle contains:

- ordered comparison groups and fields;
- normalized model records;
- explicit `unknown` placeholders for missing values;
- field-level evidence state and sources.

This permits a website table, filtered browser, or side-by-side view to use one stable data contract later without changing the research format.

## Scope boundary

This PR deliberately does **not**:

- declare any device better than another;
- populate battery, camera, display, chipset, firmware, SDK, or other comparison claims;
- generate editorial "X vs Y" articles;
- rank devices;
- recommend purchases.

Those require evidence collection and belong in later content-focused PRs.
