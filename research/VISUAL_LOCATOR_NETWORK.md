# Visual Locator Network

Third-party smart-glasses catalogs and editorial sites may be used as **locator/reference sources** to reduce blind image hunting. They are not publication provenance unless the site is independently the rights holder for a specific asset and that basis is documented separately.

## Source classes

### locator-primary
Dedicated smart-glasses catalogs whose core value is model identification/comparison.
- Smart Glasses Geek — `smartglassesgeek.com`

### locator-router
Industry indexes/aggregators that primarily route to original publishers or maker channels.
- smartglasses.today — `smartglasses.today`

### locator-secondary
Editorial/review outlets with model-specific reporting and useful product imagery.
- Wareable — `wareable.com`
- UploadVR — `uploadvr.com`

## Allowed use
- identify the exact glasses/model visually
- distinguish generations, variants, and similarly named products
- confirm that a candidate image appears to depict the intended model
- discover or confirm the likely manufacturer/rightsholder page
- recover leads for legacy products whose official pages are difficult to find
- record locator URLs in the internal acquisition ledger

## Not allowed
- hotlink locator image files
- publish image bytes merely because they appear on a locator site
- treat a locator as the rights holder unless that is independently documented for the specific asset
- replace manufacturer/rightsholder provenance with a competitor/editorial citation
- allow a locator-domain URL into `source_url`, `source_asset_url`, or other publication-provenance fields

## Search order
1. Check locator-primary sources for exact model identity and presentation.
2. Check locator-router sources for paths to maker/original-publisher material.
3. Check locator-secondary sources for model-specific visual confirmation, especially for legacy or poorly maintained manufacturer pages.
4. Trace the selected image to the manufacturer/rightsholder or another independently documented lawful source.
5. Preserve the selected original locally.
6. Record source, asset URL, credit, rights basis, retrieval date, and model-specific alt text.
7. Pass normal visual QA and publication validation.

The locator network is a discovery shortcut. It does not lower the publication gate.
