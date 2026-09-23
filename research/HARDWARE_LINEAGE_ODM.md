# Hardware Lineage / ODM Research

**Mission:** identify when apparently different smart-glasses products share hardware ancestry, ODM/OEM platforms, regulatory identities, firmware families, companion applications, or component architectures.

## Why this exists

Visual convergence makes lineage harder to infer from appearance and more important to establish from evidence. A familiar frame shape is not lineage evidence. A shared chipset is not, by itself, proof of a shared ODM. A common app can be stronger evidence, but can also span multiple hardware families.

GlassesResearch therefore treats lineage as an evidence graph rather than a resemblance judgment.

## Evidence ladder

Strong signals include regulatory filings and model identifiers; manufacturer/OEM documentation; matching firmware/update artifacts; board markings and teardown evidence; protocol-level identity; exact companion-app device identifiers; and reproducible cross-device behavior.

Supporting but non-dispositive signals include enclosure geometry, control placement, packaging, retailer claims, Bluetooth names, shared component selections, and marketplace photographs.

Weak signals such as visual resemblance or copied marketing language are leads only.

## Required lineage record

For each proposed relationship preserve:

- GlassesResearch IDs and public model names;
- manufacturer/brand and suspected OEM/ODM;
- exact model/regulatory identifiers;
- source URLs and artifact hashes where available;
- hardware/firmware/app/protocol observations;
- evidence state and confidence;
- contradictions and alternative explanations;
- what test would falsify the proposed relationship.

## Relationship vocabulary

Use explicit relationships instead of a generic "same hardware" label:

- **same model / alias**
- **rebrand**
- **variant**
- **generation**
- **shared platform**
- **shared OEM/ODM lead**
- **shared software/protocol only**
- **component overlap only**
- **unresolved resemblance**

## Current priority families

1. MYVU / StarV / XGA010C.
2. HeyCyan / CY-series and related marketplace identities.
3. W100C / Ear Dance / Goodway ecosystem.
4. Region-specific and marketplace models whose brand identity may obscure a shared platform.
5. Open platforms where public firmware can expose architecture relationships that marketing pages do not.

## Evidence threshold

Do not collapse models or assert an OEM/ODM relationship until evidence supports the specific relationship. Preserve uncertainty publicly when lineage affects purchasing, interoperability, firmware, owner control, or sourcing.
