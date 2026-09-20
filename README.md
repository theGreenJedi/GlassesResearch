<div class="gr-home">

<section class="gr-hero" aria-labelledby="gr-home-title">
  <div class="gr-hero-copy">
    <p class="gr-kicker">Independent wearable-intelligence research</p>
    <h1 id="gr-home-title">Understand the glasses.<br>Own the choices.</h1>
    <p class="gr-hero-lede">Find the glasses. See what they actually do. Follow the evidence when you want to go deeper.</p>
  </div>

  <div class="gr-hero-panel gr-hero-object" aria-label="Browse smart-glasses models">
    <p class="gr-panel-label">The glasses come first</p>
    <p class="gr-panel-title">See them.<br>Compare them.<br>Understand them.</p>
    <a class="gr-button gr-button-secondary" href="models/catalog/">Browse all models</a>
  </div>

  <div class="gr-hero-followup">
    <div class="gr-hero-actions">
      <a class="gr-button gr-button-primary" href="docs/COMPARISON_ENGINE/">Find glasses</a>
      <a class="gr-button gr-button-secondary" href="models/catalog/">Research a model</a>
      <a class="gr-button gr-button-secondary" href="docs/RESEARCH_NEWS/">Follow what’s changing</a>
    </div>
    <div class="gr-home-principles" aria-label="Research principles">
      <p>No sponsored rankings. Unknown stays unknown. Owner control matters.</p>
      <p><strong>Independent</strong> research. <strong>Evidence-linked</strong> claims. <strong>Owner-control</strong> lens. <strong>Historical</strong> preservation.</p>
    </div>
  </div>
</section>

<section class="gr-section" aria-labelledby="gr-now-title">
  <div class="gr-section-heading gr-heading-compact">
    <div>
      <p class="gr-kicker">Curated now</p>
      <h2 id="gr-now-title">What matters in wearable AI.</h2>
    </div>
    <a class="gr-text-link" href="docs/RESEARCH_NEWS/">All Research &amp; News <span aria-hidden="true">→</span></a>
  </div>

  <div class="gr-editorial-grid">
    <a class="gr-feature-story" href="docs/news/articles/2026-09-19-right-to-repair-smart-glasses/">
      <span class="gr-story-tag">Verified · Editorial · Right to repair</span>
      <strong>You bought the glasses. Can you repair them?</strong>
      <span>The lawsuit is new. The question is older: what does ownership mean when eyewear becomes computing hardware?</span>
      <em>Read the editorial →</em>
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

  const displayFreshness = (value) => {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return '';
    const hours = Math.max(0, (Date.now() - date.getTime()) / 36e5);
    if (hours < 1) return '<1h ago';
    if (hours < 48) return `${Math.floor(hours)}h ago`;
    const days = Math.floor(hours / 24);
    if (days < 60) return `${days}d ago`;
    return new Intl.DateTimeFormat(undefined, { month: 'short', day: 'numeric' }).format(date);
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
      const when = displayFreshness(item.published_at || item.discovered_at);
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

<section class="gr-section" aria-labelledby="gr-upcoming-title" data-home-events hidden>
  <div class="gr-section-heading gr-heading-compact">
    <div>
      <p class="gr-kicker">Upcoming</p>
      <h2 id="gr-upcoming-title">Dates worth watching.</h2>
    </div>
    <a class="gr-text-link" href="docs/EVENTS/">Open calendar <span aria-hidden="true">→</span></a>
  </div>
  <p>Verified public dates for launches, conferences, research, and developer events relevant to smart glasses and wearable AI.</p>
  <div id="gr-home-events-list" class="gr-story-stack" aria-live="polite"></div>
</section>

<script>
(() => {
  const list = document.getElementById('gr-home-events-list');
  const section = document.querySelector('[data-home-events]');
  if (!list || !section) return;

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const parseDate = (value) => {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(String(value || ''))) return null;
    const [year, month, day] = value.split('-').map(Number);
    return new Date(year, month - 1, day, 12, 0, 0);
  };

  const displayDateRange = (event) => {
    const start = parseDate(event.start_date);
    const end = parseDate(event.end_date || event.start_date);
    if (!start) return '';
    const short = new Intl.DateTimeFormat(undefined, { month: 'short', day: 'numeric' });
    if (!end || event.end_date === event.start_date) return short.format(start);
    return `${short.format(start)}–${short.format(end)}`;
  };

  fetch('/data/events.json', { credentials: 'same-origin', cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error('events unavailable');
      return response.json();
    })
    .then((state) => {
      if (![1, 2].includes(state?.schema_version) || !Array.isArray(state.events)) throw new Error('invalid events');
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const items = state.events
        .filter((event) => event && event.title && event.start_date && event.source_url && event.verified_on && event.status !== 'cancelled')
        .filter((event) => {
          const end = parseDate(event.end_date || event.start_date);
          return end && end >= today;
        })
        .sort((a, b) => parseDate(a.start_date) - parseDate(b.start_date))
        .slice(0, 3);

      if (!items.length) return;

      list.innerHTML = items.map((event) => {
        const meta = [displayDateRange(event), event.location].filter(Boolean).map(escapeHtml).join(' · ');
        const why = event.why_it_matters ? `<span>${escapeHtml(event.why_it_matters)}</span>` : '';
        return `<a href="${escapeHtml(event.source_url)}" target="_blank" rel="noopener noreferrer"><span class="gr-story-tag">${meta}</span><strong>${escapeHtml(event.title)}</strong>${why}</a>`;
      }).join('');
      section.hidden = false;
    })
    .catch(() => {
      section.hidden = true;
      list.replaceChildren();
    });
})();
</script>

<section class="gr-section" aria-labelledby="gr-explore-title">
  <div class="gr-section-heading">
    <div>
      <p class="gr-kicker">Choose a door</p>
      <h2 id="gr-explore-title">What do you want to do?</h2>
    </div>
    <p>Five entrances lead into the complete research system. The machinery stays behind them until you need it.</p>
  </div>

  <div class="gr-explore-grid">
    <a href="docs/COMPARISON_ENGINE/"><span class="gr-card-number">01</span><strong>Find &amp; Compare</strong><span>Start with what you need and narrow the catalog.</span></a>
    <a href="models/catalog/"><span class="gr-card-number">02</span><strong>Models</strong><span>Browse the glasses visually, then open the evidence.</span></a>
    <a href="docs/RESEARCH_NEWS/"><span class="gr-card-number">03</span><strong>Research &amp; News</strong><span>Follow verified work and developing signals.</span></a>
    <a href="hacking/"><span class="gr-card-number">04</span><strong>Develop</strong><span>SDKs, APIs, firmware, local AI and owner-controlled paths.</span></a>
    <a href="docs/ABOUT/"><span class="gr-card-number">05</span><strong>About</strong><span>Methods, standards, privacy, preservation and the complete contents.</span></a>
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