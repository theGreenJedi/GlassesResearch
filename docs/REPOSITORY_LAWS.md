# GlassesResearch Repository Laws

These rules convert the project's values into daily engineering behavior.

## 1. No orphan knowledge

If a company, person, repository, channel, firmware version, Bluetooth identifier, component, photograph, standard, application, or other recurring entity matters enough to mention repeatedly, it receives one canonical home in the glossary or another designated catalog.

Other pages link to that canonical entry instead of redefining it.

## 2. No empty merges

A new directory must provide immediate value when merged. Do not merge empty directories or placeholder-only pages.

A new section should contain at least one useful entry, known fact, sourced lead, procedure, or explicit statement of what has been tested and what remains unknown.

## 3. Everything linkable should be linked

External organizations, product pages, databases, communities, videos, repositories, standards, filings, manuals, and search tools should be hyperlinked whenever a stable public link is available.

Internal references should link directly to the canonical local page.

## 4. Explain before sending readers elsewhere

A resource entry must tell readers why the link matters, what they can expect to find, its limitations, and whether it is worth investigating before they click.

A bare URL is not a curated resource.

## 5. Claims follow evidence

Clearly distinguish:

- direct observation;
- repeated experiment;
- primary-source statement;
- commercial claim;
- community report;
- inference;
- hypothesis;
- disproven or superseded claim.

Do not convert repetition across copied listings into independent confirmation.

## 6. Investigations drive architecture

Create or change structure when an actual investigation needs it. Do not delay practical research to perfect a hypothetical taxonomy.

If repeated work exposes a missing field, entity type, or workflow, improve the architecture in the same or a small follow-up pull request.

## 7. Every merge should answer a real question

Pull-request titles should describe what was learned or established, not merely that files were changed.

Prefer:

- `INV-0002: Map W610 BLE services`
- `INV-0003: Identify the main camera processor`

Avoid:

- `Update docs`
- `Add files`
- `Miscellaneous fixes`

## 8. No important decisions trapped only in chat

When a design discussion produces an actionable rule, workflow, or research conclusion, preserve the smallest useful version in Git as soon as practical.

The repository is the durable project memory.

## 9. Preserve corrections

Do not silently erase a disproven theory or obsolete conclusion when its history is useful. Mark it as disproven or superseded, explain why, and link to the correcting evidence.

## 10. Leave every page useful

A reader opening any newly merged page should immediately learn something, find something, verify something, or understand the next research step.

## 11. The W610 is a laboratory, not a boundary

Hands-on testing may concentrate on hardware the maintainers own, currently the W610. Repository architecture and research scope must continue to support the broader smart-glasses ecosystem and potentially hundreds of models.

Do not imply hands-on verification for externally sourced models. Preserve and label manufacturer, regulatory, archival, repository, commercial, and community evidence on its own terms.

## 12. Archive first, organize second

When a lawful, fragile resource may disappear, preserve it before perfecting its taxonomy. Priority material includes firmware, APKs, SDKs, packet captures, protocol notes, model files, manuals, flashing and recovery procedures, tools, repositories, and community posts.

Record source URL, retrieval date, hashes, license or redistribution status, and any authenticity caveat. A link is useful; a well-provenanced preservation copy is more durable.

## 13. Every merge strengthens ecosystem coverage

Every future merge must preserve the model-agnostic architecture. Whenever practical, it should improve cross-model discovery, add substantive model coverage, connect shared components or software, or preserve ecosystem resources beyond the current hands-on device.

Never satisfy this rule by creating empty model folders.
