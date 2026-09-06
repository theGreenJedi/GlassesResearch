<div class="gr-home">

<section class="gr-hero" aria-labelledby="gr-home-title">
  <div class="gr-hero-copy">
    <p class="gr-kicker">Independent wearable-intelligence research</p>
    <h1 id="gr-home-title">Understand the glasses.<br>Own the choices.</h1>
    <p class="gr-hero-lede">GlassesResearch investigates smart glasses and wearable AI as products, platforms, interfaces, and long-lived systems — with evidence linked back to the claims.</p>
    <div class="gr-hero-actions">
      <a class="gr-button gr-button-primary" href="docs/COMPARISON_ENGINE/">Find glasses</a>
      <a class="gr-button gr-button-secondary" href="models/catalog/">Research a model</a>
      <a class="gr-button gr-button-secondary" href="docs/ECOSYSTEM_MAP/">Explore ecosystem</a>
    </div>
    <p class="gr-hero-note">No sponsored rankings. Unknown stays unknown. Owner control matters.</p>
  </div>

  <div class="gr-hero-panel" aria-label="GlassesResearch research system">
    <div class="gr-orbit" aria-hidden="true"><span></span><span></span><span></span></div>
    <p class="gr-panel-label">The research system</p>
    <p class="gr-panel-title">Research.<br>Preserve.<br>Compare.</p>
    <div class="home-status" id="homepage-status" aria-label="Research status">
      <div><strong data-site-stat="models">Living catalog</strong><span>canonical models</span></div>
      <div><strong data-site-stat="report-cards">Scored research</strong><span>scored Report Cards</span></div>
      <div><strong data-site-stat="freshness">Continuously built</strong><span>catalog updated</span></div>
    </div>
  </div>
</section>

<div class="gr-trust-strip" aria-label="Research principles">
  <span><strong>Independent</strong> research</span>
  <span><strong>Evidence-linked</strong> claims</span>
  <span><strong>Owner-control</strong> lens</span>
  <span><strong>Historical</strong> preservation</span>
</div>

<section class="gr-section" aria-labelledby="gr-now-title">
  <div class="gr-section-heading gr-heading-compact">
    <div>
      <p class="gr-kicker">Curated now</p>
      <h2 id="gr-now-title">What matters in wearable AI.</h2>
    </div>
    <a class="gr-text-link" href="docs/RESEARCH_NEWS/">All Research &amp; News <span aria-hidden="true">→</span></a>
  </div>

  <div class="gr-editorial-grid">
    <a class="gr-feature-story" href="docs/RESEARCH_NEWS/#august-11-2026-courts-in-england-and-wales-prohibit-meta-smart-glasses">
      <span class="gr-story-art" aria-hidden="true"></span>
      <span class="gr-story-tag">Policy &amp; use</span>
      <strong>Courts in England and Wales prohibit Meta smart glasses</strong>
      <span>Device-specific institutional rules are beginning to define where camera-equipped eyewear can actually be worn.</span>
      <em>Read the research →</em>
    </a>

    <div class="gr-story-stack">
      <a href="hacking/LOCAL_AI_AGENTS/">
        <span class="gr-story-tag">Owner control</span>
        <strong>Local AI agents can move the intelligence out of the glasses</strong>
        <span>Use eyewear as sensors and interfaces while owner-controlled devices handle perception, reasoning, memory, and tools.</span>
      </a>
      <a href="lineages/">
        <span class="gr-story-tag">Ecosystem research</span>
        <strong>Different brands can share the same underlying technology lineage</strong>
        <span>Trace OEM hardware, companion apps, firmware families, protocols, and development paths.</span>
      </a>
    </div>
  </div>
</section>

<section class="gr-section" aria-labelledby="gr-home-wire-title" data-home-wire>
  <div class="gr-section-heading gr-heading-compact">
    <div>
      <p class="gr-kicker">Across the wire</p>
      <h2 id="gr-home-wire-title">Developing now.</h2>
    </div>
    <a class="gr-text-link" href="docs/RESEARCH_NEWS/">Research &amp; News <span aria-hidden="true">→</span></a>
  </div>
  <p>Current source reports surfaced by web/news search. These are discovery signals, not verified GlassesResearch claims.</p>
  <p class="gr-wire-feed-links"><strong>Follow Across the Wire:</strong> <a href="/data/wire-feed.xml">RSS</a> · <a href="https://feedly.com/i/discover/sources/search/feed/https%3A%2F%2Fglassesresearch.org%2Fdata%2Fwire-feed.xml" target="_blank" rel="noopener noreferrer">Feedly</a> · <a href="https://www.inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Fdata%2Fwire-feed.xml" target="_blank" rel="noopener noreferrer">Inoreader</a> · <a href="/data/wire-feed.json">JSON Feed</a></p>
  <div id="gr-home-wire-list" class="gr-story-stack" aria-live="polite">
    <p data-home-wire-status>Loading the current wire…</p>
  </div>
</section>

<script>
(() => {
  const list = document.getElementById('gr-home-wire-list');
  if (!list) return;

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const displayDate = (value) => {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return '';
    return new Intl.DateTimeFormat(undefined, { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }).format(date);
  };

  const loadWire = async () => {
    let emptyState = null;
    for (const endpoint of ['/wire', '/data/wire-state.json']) {
      try {
        const response = await fetch(endpoint, { credentials: 'same-origin', cache: 'no-store' });
        if (!response.ok) continue;
        const state = await response.json();
        if (state?.schema_version !== 1 || !Array.isArray(state.items)) continue;
        if (state.items.length) return state;
        emptyState ??= state;
      } catch (_) {}
    }
    return emptyState;
  };

  loadWire().then((state) => {
    const items = (state?.items || [])
      .filter((item) => item && ['reported', 'under_review'].includes(item.status) && item.title && item.url)
      .slice(0, 8);

    if (!items.length) {
      list.innerHTML = '<p>The live wire is temporarily unavailable.</p>';
      return;
    }

    list.innerHTML = items.map((item) => {
      const status = item.status === 'under_review' ? 'Under review' : 'Reported';
      const when = displayDate(item.published_at || item.discovered_at);
      const meta = [status, item.publisher, when].filter(Boolean).map(escapeHtml).join(' · ');
      return `<a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer"><span class="gr-story-tag">${meta}</span><strong>${escapeHtml(item.title)}</strong></a>`;
    }).join('');
  }).catch(() => {
    list.innerHTML = '<p>The live wire is temporarily unavailable.</p>';
  });
})();
</script>

<section class="gr-section gr-finder-section" aria-labelledby="gr-finder-title">
  <div class="gr-section-heading">
    <div>
      <p class="gr-kicker">Discovery</p>
      <h2 id="gr-finder-title">Start with what matters to you.</h2>
    </div>
    <p>Choose your priorities. The Finder searches the living catalog for documented matches, then leads into model research, comparisons, and Report Cards.</p>
  </div>

  <div id="homepage-finder-app">Loading the compact Glasses Finder…</div>
  <a class="gr-text-link" href="docs/COMPARISON_ENGINE/">Open the complete Glasses Finder &amp; Compare <span aria-hidden="true">→</span></a>
</section>

<section class="gr-section" aria-labelledby="gr-explore-title">
  <div class="gr-section-heading">
    <div>
      <p class="gr-kicker">Explore the research</p>
      <h2 id="gr-explore-title">Find the part of the ecosystem you want to understand.</h2>
    </div>
    <p>Start with a model, a score, a development path, or the history behind the technology.</p>
  </div>

  <div class="gr-explore-grid">
    <a href="models/">
      <span class="gr-card-number">01</span>
      <strong>Models</strong>
      <span>Browse the living catalog and historical archive without reducing every device to a shopping listing.</span>
    </a>
    <a href="docs/REPORT_CARD/">
      <span class="gr-card-number">02</span>
      <strong>Report Cards</strong>
      <span>See hardware, software, openness, owner control, cloud independence, hackability, and value scored explicitly.</span>
    </a>
    <a href="hacking/">
      <span class="gr-card-number">03</span>
      <strong>Development</strong>
      <span>Follow SDKs, APIs, BLE, firmware, local AI, companion apps, and routes around unnecessary lock-in.</span>
    </a>
    <a href="docs/INDUSTRY_TIMELINE/">
      <span class="gr-card-number">04</span>
      <strong>History &amp; lineages</strong>
      <span>Preserve what disappeared and connect products that share hardware, software, and platform ancestry.</span>
    </a>
  </div>
</section>

<section class="gr-mission-band" aria-label="GlassesResearch mission">
  <div>
    <p class="gr-kicker">Why GlassesResearch exists</p>
    <h2>Document today.<br>Understand tomorrow.</h2>
  </div>
  <div>
    <p>Wearable computing changes quickly. Products vanish, cloud services close, apps disappear, and marketing claims outlive evidence. GlassesResearch exists to preserve, organize, verify, and explain that evolving ecosystem.</p>
    <div class="gr-mission-links">
      <a href="docs/ABOUT/">About the project →</a>
      <a href="docs/TOOLS/">Explore all research tools →</a>
    </div>
  </div>
</section>

</div>