(() => {
  const POLICY_VERSION = 'diversity-v1';
  const BURST_WINDOW_MS = 24 * 60 * 60 * 1000;

  const itemTime = (item) => {
    const value = item?.published_at || item?.discovered_at || '';
    const stamp = Date.parse(value);
    return Number.isNaN(stamp) ? 0 : stamp;
  };

  const sourceKey = (item) => {
    try {
      const url = new URL(item?.url || '', 'https://glassesresearch.org/');
      if (url.hostname.toLowerCase() === 'github.com') {
        const parts = url.pathname.split('/').filter(Boolean);
        if (parts.length >= 2) return `github:${parts[0].toLowerCase()}/${parts[1].toLowerCase()}`;
      }
    } catch (_) {}
    return `publisher:${String(item?.publisher || 'unknown publisher').trim().toLowerCase()}`;
  };

  const isPrerelease = (item) => {
    const text = `${item?.title || ''} ${item?.url || ''}`;
    return /(?:^|[\s._/-])(dev|alpha|beta|rc|preview|nightly)(?:[\s._/-]?\d+|\b)/i.test(text)
      || /pre[-_ ]?release/i.test(text);
  };

  const isStableVersion = (item) => {
    if (isPrerelease(item)) return false;
    return /\bv?\d+\.\d+(?:\.\d+)?\b/i.test(String(item?.title || ''));
  };

  const collapsePrereleaseBursts = (items) => {
    const indexed = items.map((item, index) => ({ item, index }));
    const prereleaseBySource = new Map();
    for (const entry of indexed) {
      if (!isPrerelease(entry.item)) continue;
      const key = sourceKey(entry.item);
      if (!prereleaseBySource.has(key)) prereleaseBySource.set(key, []);
      prereleaseBySource.get(key).push(entry);
    }

    const replacementByIndex = new Map();
    const suppressed = new Set();

    for (const entries of prereleaseBySource.values()) {
      entries.sort((a, b) => itemTime(b.item) - itemTime(a.item) || a.index - b.index);
      let cursor = 0;
      while (cursor < entries.length) {
        const first = entries[cursor];
        const newest = itemTime(first.item);
        const group = [first];
        cursor += 1;
        while (cursor < entries.length) {
          const candidate = entries[cursor];
          const when = itemTime(candidate.item);
          if (newest && when && newest - when > BURST_WINDOW_MS) break;
          group.push(candidate);
          cursor += 1;
        }
        if (group.length < 2) continue;

        const anchor = group.reduce((best, entry) => entry.index < best.index ? entry : best, group[0]);
        const newestEntry = group[0];
        const publisher = newestEntry.item.publisher || 'Development source';
        const anyReview = group.some((entry) => entry.item.status === 'under_review');
        replacementByIndex.set(anchor.index, {
          ...newestEntry.item,
          status: anyReview ? 'under_review' : 'reported',
          title: `${publisher} development activity — ${group.length} prerelease updates`,
          source_class: 'development_burst',
          bundle_count: group.length,
          bundle_kind: 'prerelease',
          _wire_source_key: sourceKey(newestEntry.item),
        });
        for (const entry of group) {
          if (entry.index !== anchor.index) suppressed.add(entry.index);
        }
      }
    }

    return indexed.flatMap(({ item, index }) => {
      if (suppressed.has(index)) return [];
      return [replacementByIndex.get(index) || item];
    });
  };

  const preferImportantWithinSource = (items) => {
    const positions = new Map();
    items.forEach((item, index) => {
      const key = sourceKey(item);
      if (!positions.has(key)) positions.set(key, []);
      positions.get(key).push(index);
    });

    const promoted = new Set();
    for (const indexes of positions.values()) {
      if (indexes.length < 2) continue;
      const first = indexes[0];
      const stable = indexes.find((index) => isStableVersion(items[index]));
      if (stable === undefined || stable === first) continue;
      const age = Math.abs(itemTime(items[first]) - itemTime(items[stable]));
      if (age <= 48 * 60 * 60 * 1000) promoted.add(stable);
    }

    if (!promoted.size) return items;
    const copy = [...items];
    for (const stableIndex of [...promoted].sort((a, b) => a - b)) {
      const key = sourceKey(copy[stableIndex]);
      const firstIndex = copy.findIndex((item) => sourceKey(item) === key);
      if (firstIndex >= 0 && stableIndex > firstIndex) {
        const [stable] = copy.splice(stableIndex, 1);
        copy.splice(firstIndex, 0, stable);
      }
    }
    return copy;
  };

  const selectDiversified = (rawItems, limit, perSourceLimit) => {
    const eligible = (rawItems || []).filter((item) => item
      && ['reported', 'under_review'].includes(item.status)
      && item.title
      && item.url);
    const collapsed = preferImportantWithinSource(collapsePrereleaseBursts(eligible));
    const counts = new Map();
    const selected = [];
    for (const item of collapsed) {
      const key = sourceKey(item);
      const count = counts.get(key) || 0;
      if (count >= perSourceLimit) continue;
      selected.push(item);
      counts.set(key, count + 1);
      if (selected.length >= limit) break;
    }
    return selected;
  };

  globalThis.GlassesResearchWirePresentation = {
    sourceKey,
    isPrerelease,
    collapsePrereleaseBursts,
    selectDiversified,
  };

  if (typeof document === 'undefined' || typeof fetch === 'undefined') return;

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const displayDate = (value, withTime = false) => {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return '';
    const options = withTime
      ? { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }
      : { month: 'short', day: 'numeric', year: 'numeric' };
    return new Intl.DateTimeFormat(undefined, options).format(date);
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

  const homepageMarkup = (items) => items.map((item) => {
    const status = item.status === 'under_review' ? 'Under review' : 'Reported';
    const when = displayDate(item.published_at || item.discovered_at, true);
    const burst = item.bundle_count ? `${item.bundle_count} updates` : '';
    const meta = [status, item.publisher, burst, when].filter(Boolean).map(escapeHtml).join(' · ');
    return `<a data-wire-presented-by="${POLICY_VERSION}" href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer"><span class="gr-story-tag">${meta}</span><strong>${escapeHtml(item.title)}</strong></a>`;
  }).join('');

  const newsroomMarkup = (items) => items.map((item) => {
    const status = item.status === 'under_review' ? 'Under review' : 'Reported';
    const burst = item.bundle_count ? `<span>${escapeHtml(`${item.bundle_count} updates`)}</span>` : '';
    const sourceClass = item.bundle_count ? 'development burst' : String(item.source_class || 'source').replaceAll('_', ' ');
    return `<article data-wire-presented-by="${POLICY_VERSION}" class="gr-wire-item"><div class="gr-wire-meta"><span class="gr-wire-status is-${escapeHtml(item.status)}">${escapeHtml(status)}</span><span>${escapeHtml(item.publisher)}</span>${burst}<span>${escapeHtml(displayDate(item.published_at || item.discovered_at))}</span></div><a class="gr-wire-title" href="${escapeHtml(item.url)}" rel="noopener">${escapeHtml(item.title)}</a><div class="gr-wire-source-class">${escapeHtml(sourceClass)}</div></article>`;
  }).join('');

  const ownsChildren = (target) => {
    const children = [...target.children];
    return children.length > 0 && children.every((child) => child.dataset?.wirePresentedBy === POLICY_VERSION);
  };

  const installSurface = (target, render, reveal) => {
    if (!target) return;
    render();
    const observer = new MutationObserver(() => {
      if (!ownsChildren(target)) render();
    });
    observer.observe(target, { childList: true });
    if (reveal) reveal();
  };

  loadWire().then((state) => {
    if (!state?.items?.length) return;

    const home = document.getElementById('gr-home-wire-list');
    if (home) {
      const items = selectDiversified(state.items, 8, 1);
      if (items.length) installSurface(home, () => { home.innerHTML = homepageMarkup(items); });
    }

    const newsroom = document.querySelector('[data-newsroom-wire]');
    if (newsroom) {
      const items = selectDiversified(state.items, 12, 2);
      if (items.length) {
        const section = newsroom.closest('.gr-newsroom-wire');
        installSurface(newsroom, () => { newsroom.innerHTML = newsroomMarkup(items); }, () => { if (section) section.hidden = false; });
      }
    }
  }).catch(() => {});
})();
