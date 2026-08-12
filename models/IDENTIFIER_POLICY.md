# Model Identifier Policy

GlassesResearch uses two complementary kinds of identifiers:

1. **`GLS-####`** — the permanent GlassesResearch reference for a cataloged model.
2. **Real-world nomenclature** — the names and numbers manufacturers, regulators, OEMs, retailers, firmware, and communities actually use for that device.

The GLS ID is the database key. It must never replace the world's nomenclature.

## Identifiers to preserve

For every model, preserve these fields when supported by evidence:

| Identifier | Examples of evidence |
|---|---|
| Official product name | manufacturer product/support pages, manuals |
| Manufacturer model number | labels, manuals, support pages, certification records |
| SKU / part number | manufacturer or retailer ordering records |
| FCC / regulatory designation | FCC or equivalent regulatory filings |
| OEM / internal identifier | firmware, board, Bluetooth, OEM documentation |
| Also known as | former names, aliases, regional names, spelling variants, community shorthand |
| Rebrands | independently marketed products demonstrated to share the underlying device/platform |

## Search and discovery rule

Searchable model resources should contain supported real-world identifiers in text or structured data. This allows searches for obscure model numbers, regulatory identifiers, aliases, and rebrand names to resolve to the correct GlassesResearch material rather than requiring a visitor to already know the GLS ID.

## Evidence rule

Do not invent or infer identifiers merely to increase search visibility. Each identifier should be traceable to a source, a preserved artifact, a hands-on observation, or clearly labeled community usage. Conflicting identifiers remain documented as conflicts until resolved.

## Model-page presentation

Where a model has a dedicated research chapter, use a compact **Identifiers / Also known as** section near the beginning of the page. Omit unknown fields rather than filling the page with empty placeholders. As research discovers additional nomenclature, add it to the same canonical model record.
