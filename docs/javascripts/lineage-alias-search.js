(() => {
  const normalize = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const esc = (value) => String(value ?? '')
    .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#039;');
  const SAFE_ALIAS_TYPES = new Set(['rebrand', 'retail-brand', 'market-name']);

  fetch('../../data/lineage-aliases.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`Lineage aliases HTTP ${response.status}`);
      return response.json();
    })
    .then((payload) => {
      const identities = (payload.aliases || []).filter((entry) =>
        entry.alias && entry.canonical_id && SAFE_ALIAS_TYPES.has(entry.alias_type));
      if (!identities.length) return;

      const byCanonical = new Map();
      identities.forEach((entry) => {
        if (!byCanonical.has(entry.canonical_id)) byCanonical.set(entry.canonical_id, []);
        byCanonical.get(entry.canonical_id).push(entry);
      });

      const canonicalIdFromPage = () => {
        const pathMatch = location.pathname.match(/\/models\/catalog\/(gls-\d{4})\/?$/i);
        if (pathMatch) return pathMatch[1].toUpperCase();
        const heading = document.querySelector('main h1, article h1, .md-content h1');
        const headingMatch = heading?.textContent?.match(/\b(GLS-\d{4})\b/i);
        return headingMatch ? headingMatch[1].toUpperCase() : null;
      };

      const renderAliasesOnCanonicalPage = () => {
        const canonicalId = canonicalIdFromPage();
        const aliases = canonicalId ? byCanonical.get(canonicalId) : null;
        if (!aliases?.length || document.getElementById('canonical-market-identities')) return;

        const reportHeading = [...document.querySelectorAll('h2')]
          .find((node) => /GlassesResearch Report Card/i.test(node.textContent || ''));
        const anchor = reportHeading || [...document.querySelectorAll('h2')]
          .find((node) => /Verified capabilities/i.test(node.textContent || ''));
        if (!anchor) return;

        const section = document.createElement('section');
        section.id = 'canonical-market-identities';
        section.className = 'canonical-market-identities';
        const canonicalName = aliases[0].canonical_name || canonicalId;
        const items = aliases
          .sort((a, b) => a.alias.localeCompare(b.alias))
          .map((entry) => `<li><strong>${esc(entry.alias)}</strong> <small>${esc(entry.alias_type.replaceAll('-', ' '))} · ${esc(entry.confidence || 'documented')}</small></li>`)
          .join('');
        section.innerHTML = `<h2>Known as / sold as</h2><p>These verified market identities resolve to this same canonical ${esc(canonicalName)} research record and Report Card. They do not create additional model counts.</p><ul>${items}</ul>`;
        anchor.insertAdjacentElement('beforebegin', section);
      };

      const attachFinder = () => {
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

        let routing = false;
        input.addEventListener('input', () => {
          if (routing) return;
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

          // Re-run the Finder's own search using the stable canonical ID, then
          // restore the market name in the box without firing another search.
          routing = true;
          input.value = `${match.canonical_id} ${match.canonical_name || ''}`.trim();
          input.dispatchEvent(new Event('input', { bubbles: true }));
          input.value = original;
          routing = false;

          const canonical = `<strong>${esc(match.canonical_name || match.canonical_id)}</strong> (${esc(match.canonical_id)})`;
          const lineageLink = match.lineage_path
            ? ` <a href="${esc(match.lineage_path)}">Open lineage research →</a>`
            : '';
          if (identityNotice) {
            identityNotice.innerHTML = `<strong>Recognized market identity:</strong> “${esc(match.alias)}” maps to ${canonical} in the ${esc(match.lineage || 'documented')} lineage. ${esc(match.message || '')}${lineageLink}`;
            identityNotice.hidden = false;
          }

          const status = host.querySelector('#discovery-status');
          if (status) {
            status.textContent = `“${match.alias}” maps to ${match.canonical_name || match.canonical_id} (${match.canonical_id}). Showing that canonical model and Report Card while preserving the name you searched.`;
          }
        }, true);

        return true;
      };

      renderAliasesOnCanonicalPage();
      if (!attachFinder()) {
        const observer = new MutationObserver(() => {
          renderAliasesOnCanonicalPage();
          if (attachFinder()) observer.disconnect();
        });
        observer.observe(document.documentElement, { childList: true, subtree: true });
      }
    })
    .catch((error) => console.warn('Lineage alias routing unavailable:', error));
})();
