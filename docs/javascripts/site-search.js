document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".md-search__input");
  if (input) {
    input.setAttribute("placeholder", "Search GlassesResearch…");
    input.setAttribute("aria-label", "Search GlassesResearch");
  }

  const normalize = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const compact = (value) => normalize(value).replaceAll(' ', '');
  const safeTypes = new Set(['rebrand', 'retail-brand', 'market-name']);
  let aliases = [];
  let aliasByCanonicalId = new Map();
  let lineageTermMap = new Map();
  let lineageSuggestions = [];

  const withinOneEdit = (left, right) => {
    if (left === right) return true;
    if (Math.abs(left.length - right.length) > 1) return false;
    let a = left;
    let b = right;
    if (a.length > b.length) [a, b] = [b, a];
    let i = 0;
    let j = 0;
    let edits = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) {
        i += 1;
        j += 1;
        continue;
      }
      edits += 1;
      if (edits > 1) return false;
      if (a.length === b.length) i += 1;
      j += 1;
    }
    if (i < a.length || j < b.length) edits += 1;
    return edits <= 1;
  };

  const resolveAlias = (value) => {
    const query = normalize(value);
    if (!query) return null;
    const exact = aliases.find((entry) => normalize(entry.alias) === query);
    if (exact) return { entry: exact, fuzzy: false };

    const queryCompact = compact(value);
    if (queryCompact.length < 5) return null;
    const candidates = aliases.filter((entry) => withinOneEdit(queryCompact, compact(entry.alias)));
    if (!candidates.length) return null;
    const canonicalIds = new Set(candidates.map((entry) => entry.canonical_id));
    if (canonicalIds.size !== 1) return null;
    return { entry: candidates[0], fuzzy: true };
  };

  const resolveLineageTerm = (value) => lineageTermMap.get(normalize(value)) || null;
  const aliasesFor = (canonicalId) => aliasByCanonicalId.get(String(canonicalId || '').toUpperCase()) || [];
  const aliasText = (entries) => entries.map((entry) => entry.alias).join(' · ');

  const decorateCanonicalPage = () => {
    const match = location.pathname.match(/\/models\/catalog\/(gls-\d{4})(?:\/|\.html|$)/i);
    if (!match) return;
    const canonicalId = match[1].toUpperCase();
    const entries = aliasesFor(canonicalId);
    if (!entries.length || document.querySelector(`[data-market-identities-for="${canonicalId}"]`)) return;
    const heading = document.querySelector('.md-content__inner h1, main h1');
    if (!heading) return;
    const note = document.createElement('p');
    note.className = 'model-market-identities';
    note.dataset.marketIdentitiesFor = canonicalId;
    const strong = document.createElement('strong');
    strong.textContent = 'Also sold as / known as: ';
    note.append(strong, document.createTextNode(aliasText(entries)));
    heading.insertAdjacentElement('afterend', note);
  };

  const decorateFinderCards = () => {
    const finderLabel = document.querySelector('.discovery-search');
    if (finderLabel && !finderLabel.dataset.aliasAware) {
      const firstText = [...finderLabel.childNodes].find((node) => node.nodeType === Node.TEXT_NODE);
      if (firstText) firstText.textContent = 'Search by model, brand, alias, or family ';
      finderLabel.dataset.aliasAware = 'true';
    }

    document.querySelectorAll('#discovery-results .discovery-card').forEach((card) => {
      if (card.querySelector('.discovery-aliases')) return;
      const meta = card.querySelector('.discovery-meta');
      const canonicalId = meta?.textContent?.match(/GLS-\d{4}/i)?.[0]?.toUpperCase();
      if (!canonicalId) return;
      const entries = aliasesFor(canonicalId);
      if (!entries.length) return;
      const aliasLine = document.createElement('div');
      aliasLine.className = 'discovery-aliases';
      const strong = document.createElement('strong');
      strong.textContent = 'Aliases / rebrands: ';
      aliasLine.append(strong, document.createTextNode(aliasText(entries)));
      meta.insertAdjacentElement('afterend', aliasLine);
    });
  };

  document.addEventListener('input', (event) => {
    const target = event.target;
    if (!(target instanceof HTMLInputElement) || target.id !== 'discovery-query') return;
    const original = target.value;
    const match = resolveAlias(original);
    if (!match) return;

    // Finder's own listener searches canonical record fields. During this one
    // event, present the stable GLS id to it, then restore what the visitor typed.
    target.value = match.entry.canonical_id.toLowerCase();
    queueMicrotask(() => {
      target.value = original;
      decorateFinderCards();
    });
  }, true);

  let finderDecorationScheduled = false;
  const scheduleFinderDecoration = () => {
    if (finderDecorationScheduled) return;
    finderDecorationScheduled = true;
    queueMicrotask(() => {
      finderDecorationScheduled = false;
      decorateFinderCards();
    });
  };
  const observer = new MutationObserver(scheduleFinderDecoration);
  observer.observe(document.body, { childList: true, subtree: true });

  Promise.all([
    fetch('/data/lineage-aliases.json', { cache: 'no-store' }).then((response) =>
      response.ok ? response.json() : Promise.reject(new Error(`Alias index HTTP ${response.status}`))),
    fetch('/data/lineage-index.json', { cache: 'no-store' }).then((response) =>
      response.ok ? response.json() : Promise.reject(new Error(`Lineage index HTTP ${response.status}`))),
  ]).then(([aliasPayload, lineagePayload]) => {
    aliases = (aliasPayload.aliases || []).filter((entry) => entry.alias && entry.canonical_id && safeTypes.has(entry.alias_type));
    aliasByCanonicalId = new Map();
    aliases.forEach((entry) => {
      const canonicalId = String(entry.canonical_id).toUpperCase();
      if (!aliasByCanonicalId.has(canonicalId)) aliasByCanonicalId.set(canonicalId, []);
      aliasByCanonicalId.get(canonicalId).push(entry);
    });

    lineageTermMap = new Map();
    const suggestionSet = new Set();
    Object.entries(lineagePayload.models || {}).forEach(([canonicalId, context]) => {
      const terms = new Set([
        context.family_label,
        context.model_label,
        ...(context.branch_path || []).map((item) => item.label),
        ...(context.aliases || []).map((item) => item.label),
        ...(context.search_terms || []),
      ].filter(Boolean));
      terms.forEach((term) => {
        const key = normalize(term);
        if (!key) return;
        if (!lineageTermMap.has(key)) lineageTermMap.set(key, new Set());
        lineageTermMap.get(key).add(canonicalId);
      });
      if (context.family_label) suggestionSet.add(context.family_label);
      (context.branch_path || []).forEach((item) => { if (item.label) suggestionSet.add(item.label); });
      (context.aliases || []).forEach((item) => { if (item.label) suggestionSet.add(item.label); });
    });
    lineageSuggestions = [...suggestionSet].sort((a, b) => a.localeCompare(b));

    if (input) {
      const list = document.createElement('datalist');
      list.id = 'glassesresearch-market-identities';
      const aliasOptions = aliases.map((entry) => `<option value="${entry.alias.replaceAll('"', '&quot;')}">${entry.canonical_name || entry.canonical_id}</option>`);
      const lineageOptions = lineageSuggestions.map((term) => `<option value="${String(term).replaceAll('"', '&quot;')}">lineage</option>`);
      list.innerHTML = [...aliasOptions, ...lineageOptions].join('');
      document.body.appendChild(list);
      input.setAttribute('list', list.id);
    }

    decorateCanonicalPage();
    decorateFinderCards();
  }).catch((error) => console.warn('Identity / lineage search unavailable:', error));

  if (input) {
    input.addEventListener('keydown', (event) => {
      if (event.key !== 'Enter') return;
      const match = resolveAlias(input.value);
      if (match) {
        event.preventDefault();
        event.stopPropagation();
        location.assign(`/models/catalog/${match.entry.canonical_id.toLowerCase()}/`);
        return;
      }
      const lineageIds = resolveLineageTerm(input.value);
      if (!lineageIds?.size) return;
      event.preventDefault();
      event.stopPropagation();
      if (lineageIds.size === 1) {
        const canonicalId = [...lineageIds][0];
        location.assign(`/models/catalog/${canonicalId.toLowerCase()}/`);
      } else {
        location.assign(`/docs/COMPARISON_ENGINE/?q=${encodeURIComponent(input.value)}`);
      }
    }, true);
  }
});
