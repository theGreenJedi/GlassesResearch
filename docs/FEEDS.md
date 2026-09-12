# Follow GlassesResearch

GlassesResearch publishes two deliberately separate feed families. Choose the one that matches what you want to receive.

## Verified Research {#verified-research}

Use this feed when you want material that GlassesResearch has verified and published. Watching items and unverified discovery signals are excluded.

<div class="follow-research__actions">
  <button class="md-button md-button--primary" type="button" data-feed-copy data-feed-url="https://glassesresearch.org/feed.xml">Copy RSS URL</button>
  <a class="md-button" href="https://feedly.com/" target="_blank" rel="noopener noreferrer">Open Feedly</a>
  <a class="md-button" href="https://www.inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Ffeed.xml" target="_blank" rel="noopener noreferrer">Open in Inoreader</a>
  <a class="md-button" href="https://glassesresearch.org/feed.xml">Raw RSS</a>
  <a class="md-button" href="https://glassesresearch.org/feed.json">JSON Feed</a>
</div>
<p class="follow-research__status" data-feed-copy-status role="status" aria-live="polite"></p>

**Feed URL:** `https://glassesresearch.org/feed.xml`

For **Feedly**, copy the RSS URL above, open Feedly, choose **Follow Sources**, paste the URL, and follow the returned source. GlassesResearch does not claim a one-click Feedly subscription handoff because Feedly's private UI routes can change independently of this site.

For **Inoreader**, the button passes the selected feed URL into Inoreader. If Inoreader asks you to sign in first, complete sign-in and continue with the preserved feed request. Copy/paste remains the reader-independent fallback.

## Across the Wire {#across-the-wire}

Use this feed when you want the fast-moving smart-glasses news wire. Items are source reports marked **Reported** or **Under review** and are **not verified GlassesResearch claims**.

The discovery collector is scheduled every **15 minutes** and keeps a rolling 120-item public window. GitHub Actions scheduling can drift, so 15 minutes is the scan cadence rather than a guaranteed publication latency. Benchmark sentinels may tell the collector that an original publisher has something we missed, but the sentinel itself is not treated as evidence or verification.

The underlying wire state also retains discovery provenance. `discovered_via` records every search wheel or sentinel known to have surfaced an item, while `first_discovered_via` preserves the route or routes present when GlassesResearch first saw it. That distinction lets us count a true sentinel rescue even if Google or Bing finds the same story later.

<div class="follow-research__actions">
  <button class="md-button md-button--primary" type="button" data-feed-copy data-feed-url="https://glassesresearch.org/data/wire-feed.xml">Copy RSS URL</button>
  <a class="md-button" href="https://feedly.com/" target="_blank" rel="noopener noreferrer">Open Feedly</a>
  <a class="md-button" href="https://www.inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Fdata%2Fwire-feed.xml" target="_blank" rel="noopener noreferrer">Open in Inoreader</a>
  <a class="md-button" href="https://glassesresearch.org/data/wire-feed.xml">Raw RSS</a>
  <a class="md-button" href="https://glassesresearch.org/data/wire-feed.json">JSON Feed</a>
</div>
<p class="follow-research__status" data-feed-copy-status role="status" aria-live="polite"></p>

**Feed URL:** `https://glassesresearch.org/data/wire-feed.xml`

For **Feedly**, copy this RSS URL, open Feedly, choose **Follow Sources**, paste the URL, and follow the returned source. For other readers, copy/paste is the canonical path.

## Reader contract

The public RSS and JSON URLs above are canonical and are the surfaces GlassesResearch can test end to end. Reader-specific controls are convenience links only. GlassesResearch does not automate tests against third-party reader interfaces; those interfaces are manually checked when integrations change or a reader problem is reported.

!!! note "Seeing XML in a browser is normal"
    A raw RSS link is meant for feed readers. Many browsers display it as an XML document instead of a human-readable page.
