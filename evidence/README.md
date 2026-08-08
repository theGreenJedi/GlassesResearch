# Evidence Corpus

GlassesResearch treats concrete evidence as the substrate of the site. Model pages, hacking views, timelines, comparisons, archives, and future search features should point back to identifiable resources rather than generic discovery suggestions.

## Institutional workflow

**Discover → Verify → Preserve → Organize → Cross-reference**

A resource enters the corpus only when it has an identifiable title or artifact, a direct URL or preserved local record, a known evidence state, and a reason it matters. Generic instructions such as “search Reddit,” “check YouTube,” or “look for a Discord” belong in internal research notes, not in the public evidence catalog.

## Evidence states

- **regulatory-primary** — government or standards record tied to an identified device/applicant.
- **vendor-primary** — manufacturer, supplier, or platform owner material; authoritative for what the owner claims, not independent verification.
- **community-primary** — the originating public project/repository/release maintained by its author or community.
- **community-report** — a specific discussion, test report, post, or thread; useful evidence but not treated as independently verified fact.
- **GlassesResearch-verified** — reproduced or observed by GlassesResearch with the test context recorded elsewhere.

## Public resource standard

A public resource entry must answer four questions:

1. **What exactly is it?**
2. **Where is the direct resource?**
3. **Why does it matter?**
4. **What level of evidence does it represent?**

If we cannot answer those questions, it does not belong in the public catalog yet.

## Canonical data

[`resources.json`](resources.json) is the first machine-readable evidence corpus. Every record has a stable `EV-####` identifier so future model pages, timelines, company maps, hacking sections, and search interfaces can reference the same underlying evidence rather than duplicating prose.

The first population deliberately focuses on W610 / HeyCyan because that is where generic discovery scaffolding had become most obvious. The corpus is designed to expand across the entire smart-glasses ecosystem.
