# Site Preservation

## `waybackglasses`

`waybackglasses` is the deliberate preservation routine for GlassesResearch.org.

When invoked, the goal is to **stamp the current public iteration of the site into the Internet Archive Wayback Machine** as a future historical touch point.

### Operational meaning

1. Discover the current public page set from `https://glassesresearch.org/sitemap.xml` when available.
2. Supplement/fallback with a same-origin crawl beginning at the homepage so the preservation set is not dependent on the sitemap alone.
3. Submit every discovered public HTML page individually to Internet Archive Save Page Now.
4. Do not follow or archive unrelated external sites.
5. Record failures visibly; partial success must not be reported as a complete stamp.

Internet Archive Save Page Now archives one supplied page at a time rather than recursively crawling an entire site, so `waybackglasses` performs the page enumeration itself.

### Trigger

The GitHub Action `.github/workflows/waybackglasses.yml` runs when `preservation/waybackglasses.trigger` changes on `main`. The workflow can also be dispatched manually from GitHub Actions.

In our working convention, when the owner says **`waybackglasses`**, update the trigger marker so that the current public iteration is submitted again.

### Why we preserve snapshots

GlassesResearch documents an evolving hardware/software ecosystem. A dated archived copy gives future researchers—and us—a stable reference for what the site reported, sourced, and concluded at that moment rather than relying only on the current mutable version.
