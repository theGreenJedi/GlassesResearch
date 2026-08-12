# Report-Card-First Research Pipeline

A catalog row is an index entry, not completed research. GlassesResearch considers a model research-ready for editorial synthesis only after its Report Card is supported by traceable evidence.

## Required order

For each canonical model in `models/THE_LIST.md`:

1. **Investigate** — collect the strongest available evidence, preferring manufacturer/developer documentation, manuals, regulatory material, SDK/API documentation, archived first-party material for discontinued devices, credible independent testing, and GlassesResearch hands-on observations where available.
2. **Correct the listing** — reconcile model name, generation, date, category, capabilities, availability, lineage, and other canonical facts when the evidence contradicts or improves the existing record.
3. **Build the evidence package** — preserve source links and note which claims each source supports. Separate hands-on observations from externally sourced claims.
4. **Complete the Report Card** — evaluate Hardware, Wearability, Visual AI, Software, Display/HUD, Openness, Owner Control, Cloud Independence, Hackability, and Value.
5. **Write or audit the editorial summary** — only after the evidence and Report Card exist, synthesize what the device is, what it does well, its compromises, its ownership/developer posture, and why it matters.

## Scoring rules

- A numerical score requires enough evidence to defend the judgment.
- **N/A** means the dimension genuinely does not apply to the device.
- **Not yet graded** means the dimension applies but evidence is not yet sufficient for a defensible score.
- Unknown facts are research debt, not permission to infer specifications.
- A family-wide score must not hide materially different hardware generations; split the evaluation when necessary.
- Value should be time-aware. If current price/availability cannot be established reliably, leave Value as Not yet graded rather than inventing a durable score.

## Completion gates

A model progresses through these states:

`Listed → Investigated → Canonical data checked/corrected → Evidence recorded → Report Card completed → Editorial summary written/audited`

A model is **research complete** only when every applicable Report Card dimension is either scored with evidence or explicitly left Not yet graded with the missing evidence identified. It is **editorially complete** only after its human-readable summary has been written or re-audited from that research package.

## Existing summaries

Existing profile paragraphs are retained. When their model reaches the Report Card pass, the paragraph must be audited against the completed evidence package and corrected where necessary. The paragraph is an output of the research, not a substitute for it.

## Project target

The canonical target is every model in `models/THE_LIST.md`: one investigated evidence package, one defensible Report Card, and one evidence-derived human-readable summary per listing.
