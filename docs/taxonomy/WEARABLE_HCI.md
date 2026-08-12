# Wearable HCI taxonomy

GlassesResearch begins with smart glasses, but the research subject is broader: wearable human-computer augmentation. The long-term system may be a constellation of devices rather than one universal form factor. This taxonomy keeps those devices in one research universe without pretending they are physically equivalent.

## Canonical rule

**One research umbrella. Separate catalogs by form factor. Shared evidence standards. Shared ownership/control philosophy.**

A device belongs in a catalog only after model-level evidence establishes a documented route to acquisition. Prototypes, concepts, components, and unshipped announcements remain in the research registry until that threshold is crossed.

The current canonical shelves are:

- [Smart glasses — The List](../../models/THE_LIST.md), with `GLS-####` IDs.
- [Adjacent Wearable-HCI Catalog](../../models/ADJACENT_WEARABLES.md), with `ADJ-####` IDs for qualifying non-eyewear wearables.
- [2026-08-12 catalog reconciliation ledger](../../models/THE_LIST_RECONCILIATION_2026-08-12.md), recording the lineage decisions that expanded the smart-glasses ledger from 121 to 145 rows while routing adjacent devices separately.

## Form-factor catalogs

1. **Smart glasses / eyewear** — devices fundamentally worn as glasses. Includes audio glasses, camera/AI glasses, discreet displays, AR glasses, XR display glasses, accessibility eyewear, and enterprise monocular/binocular eyewear.
2. **Headphones / head-worn audio-display devices** — over-ear or head-mounted devices that are not fundamentally eyewear but provide AI, sensing, display, spatial-computing, or augmented-interface capability. Optinvent ORA-X belongs here.
3. **Earbuds / earables** — in-ear or ear-mounted devices that contribute sensing, AI, audio interaction, translation, contextual assistance, or other human-computer interface functions.
4. **Neural / gesture / wrist interfaces** — bands, cuffs, EMG/EEG interfaces, gesture controllers, and related body-worn input systems.
5. **Pendants / body-worn cameras and assistants** — chest-, neck-, clothing-, or lanyard-worn devices providing sensing, capture, AI assistance, or contextual memory.
6. **Watches / rings / peripheral wearables** — wrist, finger, and other peripheral devices when they materially participate in the augmented-human interface rather than merely existing as generic consumer electronics.
7. **Composite systems** — deliberately integrated multi-device systems whose meaningful capability emerges from the combination: for example glasses + neural band, glasses + earbuds, or wearable sensors + a local compute node.
8. **Eyeglass-mounted modules** — cameras, AI assistants or other modules that attach to ordinary eyeglasses but are not themselves the eyewear. OrCam MyEye belongs here: physically close to glasses, but counted separately rather than inflating the smart-glasses ledger.

## Delineation matters

Catalog membership is based on physical form and interface role, not marketing language. A display-equipped headphone does not become smart glasses because it overlaps with AR. A pair of audio glasses remains eyewear even when its primary function resembles headphones. A wrist controller paired with glasses remains a wrist interface and can also be documented as part of a composite system. A clip-on camera attached to ordinary eyeglasses remains a clip-on module rather than becoming a pair of smart glasses.

Counts remain separate. The smart-glasses count must never silently include headphones, pendants, rings, headsets, helmets, clip-on modules or other adjacent wearables.

## Shared report-card ruler

Where a dimension applies, its score means the same thing across catalogs. Hardware, Software, Openness, Owner Control, Cloud Independence, Hackability, and Value retain the same evidence and scoring philosophy. Form-specific dimensions may be marked `N/A` rather than forced into a misleading score. Display/HUD, for example, is `N/A` for an audio-only earable.

The taxonomy may eventually justify additional cross-form dimensions such as Input/Control or Sensor Richness. Those should be added only after the rubric is explicitly defined and calibrated against existing benchmark devices.

## Lineage protocol

Research remains lineage-first inside each form-factor catalog:

1. identify the complete defensible product lineage;
2. investigate the lineage together;
3. distinguish shared architecture from generation-specific evidence;
4. never inherit a specification or score merely because adjacent generations are related;
5. score each qualifying model on the fixed catalog-wide ruler;
6. generate or audit prose from the completed evidence package;
7. preserve related prototypes and non-qualifying products as lineage context rather than silently counting them;
8. reconcile every completed lineage into one of four outcomes: `GLS-` smart-glasses row, `ADJ-` adjacent wearable row, registry/archive candidate, or documented non-wearable lineage relative.

A lineage, not an arbitrary model quota, defines a research batch.

## Research purpose

The site can therefore remain exceptionally precise about smart glasses while preserving the larger question: how do combinations of body-worn computers augment a person without taking ownership, agency, or control away from that person?
