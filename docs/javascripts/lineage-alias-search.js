(() => {
  const normalize = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();

  fetch('../../data/lineage-aliases.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`Lineage aliases HTTP ${response.status}`);
      return response.json();
    })
    .then((payload) => {
      const aliases = (payload.aliases || []).filter((entry) => entry.alias && entry.canonical_id);
      if (!aliases.length) return;

      const attach = () => {
        const host = document.getElementById('comparison-engine-app');
        const input = host?.querySelector('#discovery-query');
        if (!host || !input || input.dataset.lineageAliasSearch === 'attached') return false;
        input.dataset.lineageAliasSearch = 'attached';

        input.addEventListener('input', () => {
          const original = input.value;
          const query = normalize(original);
          if (!query) return;

          const match = aliases.find((entry) => {
            const alias = normalize(entry.alias);
            return alias && (query === alias || query.includes(alias));
          });
          if (!match) return;

          input.value = `${match.canonical_id} ${match.canonical_name || ''}`.trim();
          queueMicrotask(() => {
            input.value = original;
            const status = host.querySelector('#discovery-status');
            if (status) {
              status.textContent = `“${match.alias}” maps to ${match.canonical_name || match.canonical_id} (${match.canonical_id}) in the ${match.lineage || 'canonical'} lineage. Showing that canonical research.`;
            }
          });
        }, true);

        return true;
      };

      if (attach()) return;
      const observer = new MutationObserver(() => {
        if (attach()) observer.disconnect();
      });
      observer.observe(document.documentElement, { childList: true, subtree: true });
    })
    .catch((error) => console.warn('Lineage alias routing unavailable:', error));
})();
