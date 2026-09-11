(() => {
  const normalizedPath = window.location.pathname.replace(/\/+$/, '');

  const parseIsoDate = (value) => {
    if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}/.test(value)) return null;
    const date = new Date(value.length === 10 ? `${value}T12:00:00` : value);
    return Number.isNaN(date.getTime()) ? null : date;
  };

  const displayDate = (value) => {
    const date = parseIsoDate(value) || new Date(value);
    if (Number.isNaN(date.getTime())) return value || '';
    return new Intl.DateTimeFormat(undefined, { year: 'numeric', month: 'short', day: 'numeric' }).format(date);
  };

  const relativeAge = (value) => {
    const date = parseIsoDate(value) || new Date(value);
    if (Number.isNaN(date.getTime())) return '';
    const hours = Math.max(0, (Date.now() - date.getTime()) / 36e5);
    if (hours < 1) return 'less than 1h ago';
    if (hours < 48) return `${Math.floor(hours)}h ago`;
    const days = Math.floor(hours / 24);
    if (days < 60) return `${days}d ago`;
    return displayDate(value);
  };

  document.querySelectorAll('[data-relative-time]').forEach((node) => {
    const value = node.getAttribute('datetime') || node.dataset.relativeTime;
    const rendered = relativeAge(value);
    if (rendered) node.textContent = rendered;
  });

  const finderFreshness = document.querySelector('[data-finder-freshness]');
  if (finderFreshness) {
    Promise.all([
      fetch('/data/finder-schema.json', { cache: 'no-store' }).then((response) => {
        if (!response.ok) throw new Error('finder schema unavailable');
        return response.json();
      }),
      fetch('/data/price-observations.json', { cache: 'no-store' }).then((response) => {
        if (!response.ok) throw new Error('price observations unavailable');
        return response.json();
      }),
    ]).then(([schema, prices]) => {
      const schemaDate = schema?.updated ? displayDate(schema.updated) : 'date unavailable';
      const priceDate = prices?.updated ? displayDate(prices.updated) : 'date unavailable';
      finderFreshness.innerHTML = `<strong>Evidence freshness</strong> capability schema ${schemaDate} · acquisition-price set ${priceDate} · Unknown never means No`;
    }).catch(() => {
      finderFreshness.innerHTML = '<strong>Evidence freshness</strong> live dates unavailable · Unknown never means No';
    });
  }

  if (!/^\/docs\/news\/articles\/[^/]+$/.test(normalizedPath)) return;

  const root = document.querySelector('.md-content__inner');
  const title = root?.querySelector(':scope > h1:first-child');
  if (!root || !title || root.querySelector('.gr-publication-meta')) return;

  document.body.classList.add('gr-publication-article');

  const deck = title.nextElementSibling?.tagName === 'P' && title.nextElementSibling.querySelector('em')
    ? title.nextElementSibling
    : null;
  if (deck) deck.classList.add('gr-publication-deck');

  const meta = {};
  const labels = new Map([
    ['published', 'Published'],
    ['updated', 'Updated'],
    ['status', 'Status'],
    ['type', 'Type'],
    ['evidence posture', 'Evidence posture'],
  ]);

  [...root.querySelectorAll(':scope > p')].slice(0, 8).forEach((paragraph) => {
    const clone = paragraph.cloneNode(true);
    clone.querySelectorAll('br').forEach((br) => br.replaceWith('\n'));
    const text = clone.textContent || '';
    let found = false;
    text.split(/\n+/).map((line) => line.trim()).filter(Boolean).forEach((line) => {
      const match = line.match(/^(Published|Updated|Status|Type|Evidence posture):\s*(.+)$/i);
      if (!match) return;
      const key = match[1].toLowerCase();
      meta[key] = match[2].trim();
      found = true;
    });
    if (found) paragraph.classList.add('gr-publication-source-meta');
  });

  const articleWords = (root.innerText || '').trim().split(/\s+/).filter(Boolean).length;
  const readingMinutes = Math.max(1, Math.ceil(articleWords / 220));

  const metaStrip = document.createElement('div');
  metaStrip.className = 'gr-publication-meta';
  metaStrip.setAttribute('aria-label', 'Publication details');
  const metaItems = [];
  if (meta.published) metaItems.push(`<span><strong>Published</strong>${meta.published}</span>`);
  if (meta.updated) metaItems.push(`<span><strong>Updated</strong>${meta.updated}</span>`);
  if (meta.status) metaItems.push(`<span><strong>Status</strong>${meta.status}</span>`);
  if (meta.type) metaItems.push(`<span><strong>Desk</strong>${meta.type}</span>`);
  metaItems.push(`<span><strong>Reading time</strong>${readingMinutes} min</span>`);
  metaStrip.innerHTML = metaItems.join('');

  const anchor = deck || title;
  anchor.insertAdjacentElement('afterend', metaStrip);

  const topics = document.createElement('div');
  topics.className = 'gr-publication-topics';
  topics.setAttribute('aria-label', 'Article topics and models');
  const topicEntries = [];
  const seen = new Set();
  const addTopic = (label, href = '') => {
    const clean = String(label || '').trim();
    const key = clean.toLowerCase();
    if (!clean || seen.has(key) || topicEntries.length >= 6) return;
    seen.add(key);
    topicEntries.push({ label: clean, href });
  };
  if (meta.type) meta.type.split(/[\/,]/).forEach((value) => addTopic(value));
  if (meta.status && !/published/i.test(meta.status)) addTopic(meta.status);
  [...root.querySelectorAll('a[href*="/models/catalog/"]')].forEach((link) => addTopic(link.textContent, link.href));
  if (topicEntries.length) {
    topics.innerHTML = topicEntries.map((entry) => entry.href
      ? `<a class="gr-publication-topic" href="${entry.href}">${entry.label}</a>`
      : `<span class="gr-publication-topic">${entry.label}</span>`).join('');
    metaStrip.insertAdjacentElement('afterend', topics);
  }

  const evidenceHeading = [...root.querySelectorAll('h2')].find((heading) => /evidence boundary/i.test(heading.textContent || ''));
  const evidenceBand = document.createElement('section');
  evidenceBand.className = 'gr-publication-evidence-band';
  evidenceBand.setAttribute('aria-label', 'Research evidence state');
  const publicationState = meta.status || meta.type || 'Published research';
  const evidenceState = meta['evidence posture'] || (evidenceHeading ? 'Evidence boundary stated in article' : 'Follow cited sources and evidence notes');
  const revisionState = meta.updated ? `Updated ${meta.updated}` : 'Published version; revision history retained in Git';
  evidenceBand.innerHTML = `
    <div><span>Publication state</span><strong>${publicationState}</strong></div>
    <div><span>Evidence posture</span><strong>${evidenceState}</strong></div>
    <div><span>Revision trail</span><strong>${revisionState}</strong></div>`;
  (topics.childElementCount ? topics : metaStrip).insertAdjacentElement('afterend', evidenceBand);

  const slug = normalizedPath.split('/').pop();
  const historyUrl = `https://github.com/theGreenJedi/GlassesResearch/commits/main/docs/news/articles/${encodeURIComponent(slug)}.md`;
  const footer = document.createElement('section');
  footer.className = 'gr-publication-footer';
  footer.setAttribute('aria-label', 'Continue researching this story');
  footer.innerHTML = `
    <div>
      <h2>Keep following the evidence</h2>
      <p>Articles are publication surfaces, not the end of the research trail. Follow the newsroom, inspect the model evidence, or challenge a claim when better documentation appears.</p>
    </div>
    <div class="gr-publication-footer-links">
      <a href="/docs/RESEARCH_NEWS/">Research &amp; News →</a>
      <a href="/docs/COMPARISON_ENGINE/">Open the Finder →</a>
      <a href="/docs/RESEARCH_CHALLENGES/">Challenge or correct →</a>
      <a href="${historyUrl}" target="_blank" rel="noopener noreferrer">Revision history →</a>
    </div>`;
  root.append(footer);
})();
