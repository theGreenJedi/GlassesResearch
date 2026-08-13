# Evidence Provenance Framework

GlassesResearch treats specifications as claims that should be traceable to evidence. Important fields should identify the source, confidence, verification date, and exact device or version scope.

## Source classes

Use the existing research-library classes: GlassesResearch verified, regulatory primary, vendor primary, community primary, community report, retailer, and unknown.

## Confidence

- Confirmed: direct evidence supports the exact claim and device/version.
- Strong: highly specific evidence supports the claim with only a small unresolved qualification.
- Provisional: plausible evidence exists but identity, version, wording, or reproducibility remains incomplete.
- Conflicting: credible sources disagree; preserve the disagreement.
- Unknown: insufficient evidence.

## Field record

A researched field should preserve its value, confidence, one or more stable EV source IDs, verification date, device/region/firmware scope when relevant, and an optional qualification note.

## Rules

1. Unknown remains unknown. Absence of evidence is not a negative finding.
2. Hardware presence and owner accessibility are separate claims.
3. Do not automatically transfer evidence among rebrands, regional variants, or suspected OEM siblings.
4. Cloud behavior, subscriptions, applications, firmware, and support status require dated evidence.
5. Marketing language establishes a vendor claim, not necessarily measured behavior.
6. Retail listings can establish observed asking price and availability but should not automatically establish engineering specifications.
7. Community reports retain attribution and sample scope.
8. Conflicting evidence remains visible until resolved.
9. Report-card scores should be derived from evidenced facts rather than replace them.
10. Hands-on results should preserve enough test conditions to permit repetition.

## Migration

Existing records need not be rewritten at once. Apply the framework to new research first, then migrate high-value fields lineage by lineage. Prioritize Owner Control, Cloud Independence, Openness, connectivity, sensors, AI capability, subscription dependence, prescription support, and lifecycle status.
