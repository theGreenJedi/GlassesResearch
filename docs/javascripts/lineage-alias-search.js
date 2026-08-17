(() => {
  const normalize = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();

  fetch('../../data/lineage-aliases.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`Lineage aliases HTTP ${response.status}`);
      return response.json();
    })
    .then((payload) => {
      const identities = (payload.aliases || []).filter((entry) => entry.alias && (entry.canonical_id || entry.lineage_path));
      if (!identities.length) return;

      const attach = () => {
        const host = document.getElementById('comparison-engine-app');
        const input = host?.querySelector('#discovery-query');
        if (!host || !input || input.dataset.lineageAliasSearch === 'attached') return false;
        input.dataset.lineageAliasSearch = 'attached';

        let identityNotice = host.querySelector('#lineage-identity-notice');
        if (!identityNotice) {
          identityNotice = document.createElement('div');
          identityNotice.id = 'lineage-identity-notice';
          identityNotice.className = 'lineage-identity-notice';
          identityNotice.hidden = true;
          const status = host.querySelector('#discovery-status');
          status?.insertAdjacentElement('afterend', identityNotice);
        }

        input.addEventListener('input', () => {
          const original = input.value;
          const query = normalize(original);
          if (!query) {
            if (identityNotice) identityNotice.hidden = true;
            return;
          }

          const match = identities.find((entry) => {
            const alias = normalize(entry.alias);
            return alias && (query === alias || query.includes(alias));
          });
          if (!match) {
            if (identityNotice) identityNotice.hidden = true;
            return;
          }

          if (match.canonical_id) {
            input.value = `${match.canonical_id} ${match.canonical_name || ''}`.trim();
            queueMicrotask(() => { input.value = original; });
          }

          const canonical = match.canonical_id
            ? `<strong>${match.canonical_name || match.canonical_id}</strong> (${match.canonical_id})`
            : `<strong>${match.canonical_name || match.lineage}</strong>`;
          const lineageLink = match.lineage_path
            ? ` <a href="${match.lineage_path}">Open lineage research →</a>`
            : '';
          if (identityNotice) {
            identityNotice.innerHTML = `<strong>Recognized market identity:</strong> “${match.alias}” maps to ${canonical} in the ${match.lineage || 'documented'} lineage. ${match.message || ''}${lineageLink}`;
            identityNotice.hidden = false;
          }

          const status = host.querySelector('#discovery-status');
          if (status && match.canonical_id) {
            status.textContent = `“${match.alias}” maps to ${match.canonical_name || match.canonical_id} (${match.canonical_id}). Showing that canonical model while preserving the name you searched.`;
          } else if (status) {
            status.textContent = `“${match.alias}” is a recognized market identity in the ${match.lineage}. Open the lineage research for the underlying platform.`;
          }
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
