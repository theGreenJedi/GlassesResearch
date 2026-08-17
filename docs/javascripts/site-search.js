document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".md-search__input");
  if (!input) return;
  input.setAttribute("placeholder", "Search GlassesResearch…");
  input.setAttribute("aria-label", "Search GlassesResearch");

  const normalize = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const safeTypes = new Set(['rebrand', 'retail-brand', 'market-name']);
  let aliases = [];

  fetch('/data/lineage-aliases.json', { cache: 'no-store' })
    .then((response) => response.ok ? response.json() : Promise.reject(new Error(`Alias index HTTP ${response.status}`)))
    .then((payload) => {
      aliases = (payload.aliases || []).filter((entry) => entry.alias && entry.canonical_id && safeTypes.has(entry.alias_type));
      const list = document.createElement('datalist');
      list.id = 'glassesresearch-market-identities';
      list.innerHTML = aliases.map((entry) => `<option value="${entry.alias.replaceAll('"', '&quot;')}">${entry.canonical_name || entry.canonical_id}</option>`).join('');
      document.body.appendChild(list);
      input.setAttribute('list', list.id);
    })
    .catch((error) => console.warn('Market identity search unavailable:', error));

  input.addEventListener('keydown', (event) => {
    if (event.key !== 'Enter') return;
    const query = normalize(input.value);
    const match = aliases.find((entry) => normalize(entry.alias) === query);
    if (!match) return;
    event.preventDefault();
    event.stopPropagation();
    location.assign(`/models/catalog/${match.canonical_id.toLowerCase()}/`);
  }, true);
});
