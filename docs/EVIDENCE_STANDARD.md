# Evidence and Confidence Standard

Every important technical claim should show how it is known.

## Claim status

- **Verified** — reproduced directly or supported by authoritative primary evidence.
- **Community confirmed** — independently reported by multiple credible, unrelated sources, but not automatically eligible for publication as a working procedure.
- **Independent hands-on review** — an accepted, provenance-bearing community report from a contributor who attests that they personally used or handled the identified device. Acceptance verifies that the report meets the intake and evidence-record requirements; it does **not** make every claim in the review Verified.
- **Not Verified Yet** — plausible, sourced, or community-reported material awaiting qualifying reproduction. It belongs in a research queue and must not be written as a working guide.
- **Personally observed** — a claim-level label for something directly observed on a documented device but not yet independently reproduced. It may appear inside a GlassesResearch experiment or an independent hands-on review when the observer and device context are explicit.
- **Hypothesis** — plausible interpretation awaiting testing.
- **Disproven** — tested and found false or contradicted by stronger evidence.
- **Historical** — preserved because it once existed or may illuminate prior device behavior; not represented as currently functional.
- **Unknown** — open question with insufficient evidence.

## Independent review rule

Community submissions remain a separate evidence layer from GlassesResearch's own physical inspection and experiments. One accepted owner report is labeled **Independent hands-on review**. Compatible findings from multiple unrelated reviewers can support **Community confirmed** status when the evidence record justifies it. Neither label silently replaces a canonical GlassesResearch Report Card score.

A contributor's history is provenance, not authority. Prior accepted work may help readers understand experience and context, but every new claim must still stand on its own evidence, device context, reproducibility, and corroboration.

## Working-guide publication rule

Only a procedure that has been reproduced successfully with an identified model, hardware revision when available, firmware and tool versions, date, evidence, expected result, and recovery information may be published as **Verified Working**.

Community confirmation is valuable evidence, but it does not by itself promote a procedure into the working-guide library. Community-reported procedures remain clearly labeled outside that library until qualifying verification is complete.

## Required claim record

```text
Claim:
Status:
Model / revision:
Firmware / software versions:
Source or experiment:
Date checked:
Contributor:
Confidence:
Reproduction steps:
Expected result:
Actual result:
Evidence path or archive:
Recovery / rollback:
Contradictory evidence:
Notes:
```

## Confidence

Use plain-language confidence: **high**, **moderate**, or **low**. Confidence should reflect evidence quality, reproducibility, device-revision coverage, and whether alternative explanations remain.

## Sources

Prefer primary sources: direct measurements, captures, photographs, manuals, firmware, regulatory filings, manufacturer documents, and reproducible experiments. Secondary sources remain valuable when clearly labeled and attributed.

## Promotion path

A claim or procedure can move through the repository only when the evidence record justifies the change:

```text
Independent hands-on review -> Community confirmed -> Verified
Not Verified Yet -> Community confirmed -> Verified
Not Verified Yet -> Disproven
Hypothesis -> Not Verified Yet, Verified, or Disproven
Verified -> Historical or Disproven when later evidence requires correction
```

Popularity is not verification. Reproducibility is verification.

## Corrections

Do not silently erase disproven work. Preserve the former claim, mark it disproven, explain why, and link the stronger evidence. This protects the reasoning trail and prevents repeated mistakes.
