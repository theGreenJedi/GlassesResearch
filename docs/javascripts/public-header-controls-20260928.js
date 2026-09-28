(() => {
  const searchButton = () => document.querySelector('.gr-search-button');
  const menuButton = () => document.querySelector('.gr-menu-button');
  const searchPanel = () => document.getElementById('gr-site-search-panel');
  const menuPanel = () => document.getElementById('gr-site-menu-panel');
  const searchInput = () => document.getElementById('gr-site-search-input');
  const searchResults = () => document.getElementById('gr-site-search-results');
  const searchStatus = () => document.getElementById('gr-site-search-status');

  let searchDocs = null;
  let searchLoad = null;

  const normalize = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();

  const setPanelState = (panel, button, open) => {
    if (!panel || !button) return;
    panel.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    document.documentElement.classList.toggle('gr-header-panel-open', open);
  };

  const closeAll = () => {
    setPanelState(searchPanel(), searchButton(), false);
    setPanelState(menuPanel(), menuButton(), false);
    document.documentElement.classList.remove('gr-header-panel-open');
  };

  const openSearch = () => {
    setPanelState(menuPanel(), menuButton(), false);
    setPanelState(searchPanel(), searchButton(), true);
    window.requestAnimationFrame(() => searchInput()?.focus());
  };

  const openMenu = () => {
    setPanelState(searchPanel(), searchButton(), false);
    setPanelState(menuPanel(), menuButton(), true);
  };

  const loadSearch = () => {
    if (searchDocs) return Promise.resolve(searchDocs);
    if (searchLoad) return searchLoad;
    searchLoad = fetch('/search/search_index.json', { cache: 'no-store' })
      .then((response) => {
        if (!response.ok) throw new Error('Search index unavailable');
        return response.json();
      })
      .then((payload) => {
        searchDocs = Array.isArray(payload.docs) ? payload.docs : [];
        return searchDocs;
      });
    return searchLoad;
  };

  const snippet = (text, query) => {
    const raw = String(text || '').replace(/\s+/g, ' ').trim();
    if (!raw) return '';
    const lower = raw.toLowerCase();
    const needle = query.toLowerCase();
    const index = lower.indexOf(needle);
    const start = index > 80 ? index - 80 : 0;
    const chunk = raw.slice(start, start + 220);
    return (start ? '…' : '') + chunk + (start + 220 < raw.length ? '…' : '');
  };

  const score = (doc, query) => {
    const q = normalize(query);
    if (!q) return 0;
    const title = normalize(doc.title);
    const text = normalize(doc.text);
    const tokens = q.split(' ').filter(Boolean);
    let value = 0;
    if (title === q) value += 120;
    if (title.startsWith(q)) value += 80;
    if (title.includes(q)) value += 55;
    if (text.includes(q)) value += 20;
    for (const token of tokens) {
      if (title.includes(token)) value += 12;
      if (text.includes(token)) value += 3;
    }
    return value;
  };

  const renderResults = async (query) => {
    const resultsNode = searchResults();
    const statusNode = searchStatus();
    if (!resultsNode || !statusNode) return;
    resultsNode.replaceChildren();
    const q = normalize(query);
    if (q.length < 2) {
      statusNode.textContent = 'Type at least two characters to search the site.';
      return;
    }
    statusNode.textContent = 'Searching…';
    try {
      const docs = await loadSearch();
      const matches = docs
        .map((doc) => ({ doc, score: score(doc, q) }))
        .filter((item) => item.score > 0)
        .sort((a, b) => b.score - a.score)
        .slice(0, 16);
      statusNode.textContent = matches.length ? `${matches.length} best matches` : 'No matches found.';
      for (const { doc } of matches) {
        const link = document.createElement('a');
        link.className = 'gr-header-search-result';
        link.href = '/' + String(doc.location || '').replace(/^\/+/, '');
        const title = document.createElement('strong');
        title.textContent = doc.title || doc.location || 'Untitled';
        const detail = document.createElement('span');
        detail.textContent = snippet(doc.text, q);
        link.append(title, detail);
        resultsNode.append(link);
      }
    } catch (error) {
      statusNode.textContent = 'Search is temporarily unavailable.';
      console.warn('Public site search failed:', error);
    }
  };

  const bind = () => {
    const search = searchButton();
    const menu = menuButton();
    const input = searchInput();
    if (search && !search.dataset.grNativePanelBound) {
      search.dataset.grNativePanelBound = 'true';
      search.addEventListener('click', () => {
        if (searchPanel()?.hidden === false) closeAll();
        else openSearch();
      });
    }
    if (menu && !menu.dataset.grNativePanelBound) {
      menu.dataset.grNativePanelBound = 'true';
      menu.addEventListener('click', () => {
        if (menuPanel()?.hidden === false) closeAll();
        else openMenu();
      });
    }
    document.querySelectorAll('[data-gr-close-panel]').forEach((control) => {
      if (control.dataset.grNativePanelBound) return;
      control.dataset.grNativePanelBound = 'true';
      control.addEventListener('click', closeAll);
    });
    if (input && !input.dataset.grNativePanelBound) {
      input.dataset.grNativePanelBound = 'true';
      let timer = null;
      input.addEventListener('input', () => {
        window.clearTimeout(timer);
        timer = window.setTimeout(() => renderResults(input.value), 80);
      });
      input.addEventListener('keydown', (event) => {
        if (event.key !== 'Enter') return;
        const first = searchResults()?.querySelector('a');
        if (first) {
          event.preventDefault();
          first.click();
        }
      });
    }
  };

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeAll();
  });
  document.addEventListener('DOMContentLoaded', bind);
  if (window.document$?.subscribe) window.document$.subscribe(bind);
})();
