(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const formatValue = (value) => {
    if (Array.isArray(value)) return value.join(', ');
    if (typeof value === 'boolean') return value ? 'Yes' : 'No';
    return String(value);
  };

  const permalink = (left, right) => {
    const url = new URL(window.location.href);
    url.searchParams.set('left', left);
    url.searchParams.set('right', right);
    return url.toString();
  };

  const evidenceLabel = (evidence) => {
    if (evidence === 'hands-on') return 'Hands-on';
    if (evidence === 'community') return 'Community source';
    if (evidence === 'primary') return 'Primary source';
    return '';
  };

  const externalSources = (device) => (device.links || [])
    .filter((link) => link && link.kind === 'external' && typeof link.url === 'string')
    .map((link) => link.url);

  const sourceLinks = (urls) => {
    if (!urls || !urls.length) return '';
    return `<div class="comparison-sources">${urls
      .map((src, index) => `<a href="${escapeHtml(src)}" target="_blank" rel="noopener">source${urls.length > 1 ? ` ${index + 1}` : ''}</a>`)
      .join(' · ')}</div>`;
  };

  Promise.all([
    fetch('../../data/comparisons.json', { cache: 'no-store' }).then((response) => {
      if (!response.ok) throw new Error(`Comparison data HTTP ${response.status}`);
      return response.json();
    }),
    fetch('../../data/devices.json', { cache: 'no-store' }).then((response) => {
      if (!response.ok) throw new Error(`Device data HTTP ${response.status}`);
      return response.json();
    }),
  ])
    .then(([bundle, deviceBundle]) => {
      const researched = new Map((bundle.records || []).map((record) => [record.id, record]));
      const devices = deviceBundle.records || [];
      if (devices.length < 2) {
        host.innerHTML = '<p>Not enough device records are available for a comparison.</p>';
        return;
      }

      const records = devices.map((device) => ({
        ...device,
        researchedFields: researched.get(device.id)?.fields || {},
      }));

      const params = new URLSearchParams(window.location.search);
      const ids = records.map((record) => record.id);
      const initialLeft = ids.includes(params.get('left')) ? params.get('left') : ids[0];
      const initialRight = ids.includes(params.get('right')) ? params.get('right') : ids[1];

      host.innerHTML = `
        <p class="comparison-coverage"><strong>${records.length} models available for comparison.</strong> Every device in The List is selectable. Additional technical rows appear only when sourced research exists; empty placeholder rows are not shown.</p>
        <div class="comparison-controls">
          <label>Device A <select id="comparison-left"></select></label>
          <label>Device B <select id="comparison-right"></select></label>
          <button type="button" id="comparison-copy-link">Copy shareable link</button>
          <button type="button" id="comparison-print">Print</button>
        </div>
        <p id="comparison-status" class="comparison-status"></p>
        <div id="comparison-results"></div>
      `;

      const leftSelect = host.querySelector('#comparison-left');
      const rightSelect = host.querySelector('#comparison-right');
      const results = host.querySelector('#comparison-results');
      const status = host.querySelector('#comparison-status');
      const optionHtml = records
        .map((record) => `<option value="${escapeHtml(record.id)}">${escapeHtml(record.maker)} ${escapeHtml(record.model)} — ${escapeHtml(record.id)}</option>`)
        .join('');
      leftSelect.innerHTML = optionHtml;
      rightSelect.innerHTML = optionHtml;
      leftSelect.value = initialLeft;
      rightSelect.value = initialRight;

      const fieldMap = new Map();
      (bundle.groups || []).forEach((group) => {
        (group.fields || []).forEach((field) => fieldMap.set(field.id, { ...field, groupLabel: group.label }));
      });

      const identityFieldIds = new Set(['manufacturer', 'release_year', 'status', 'category']);
      const isKnown = (entry) => entry && entry.evidence !== 'unknown' && entry.value !== 'Unknown' && entry.value !== null && entry.value !== '';

      const canonicalRow = (label, leftValue, rightValue, leftSources = [], rightSources = []) => {
        const a = leftValue || '—';
        const b = rightValue || '—';
        const diffClass = String(a) !== String(b) ? ' comparison-different' : '';
        return `<tr class="${diffClass}"><th>${escapeHtml(label)}</th><td>${escapeHtml(a)}${sourceLinks(leftSources)}</td><td>${escapeHtml(b)}${sourceLinks(rightSources)}</td></tr>`;
      };

      const render = () => {
        const left = records.find((record) => record.id === leftSelect.value);
        const right = records.find((record) => record.id === rightSelect.value);
        const url = new URL(window.location.href);
        url.searchParams.set('left', left.id);
        url.searchParams.set('right', right.id);
        window.history.replaceState({}, '', url);

        const leftSources = externalSources(left);
        const rightSources = externalSources(right);

        let html = '<h3>Canonical record</h3><div class="comparison-table-wrap"><table><thead><tr><th>Field</th>';
        html += `<th>${escapeHtml(left.maker)} ${escapeHtml(left.model)}</th><th>${escapeHtml(right.maker)} ${escapeHtml(right.model)}</th></tr></thead><tbody>`;
        html += canonicalRow('Stable ID', left.id, right.id);
        html += canonicalRow('Manufacturer', left.maker, right.maker, leftSources, rightSources);
        html += canonicalRow('Model', left.model, right.model, leftSources, rightSources);
        html += canonicalRow('First documented sale / order', left.era, right.era, leftSources, rightSources);
        html += canonicalRow('Lifecycle state', left.state, right.state, leftSources, rightSources);
        html += canonicalRow('Device type', left.type, right.type, leftSources, rightSources);
        html += canonicalRow('Access route', left.access, right.access, leftSources, rightSources);
        html += canonicalRow('Evidence classification', left.evidence, right.evidence, leftSources, rightSources);
        html += '</tbody></table></div>';

        const grouped = new Map();
        for (const [fieldId, meta] of fieldMap.entries()) {
          if (identityFieldIds.has(fieldId)) continue;
          const a = left.researchedFields[fieldId];
          const b = right.researchedFields[fieldId];
          if (!isKnown(a) && !isKnown(b)) continue;
          if (!grouped.has(meta.groupLabel)) grouped.set(meta.groupLabel, []);
          grouped.get(meta.groupLabel).push([fieldId, meta]);
        }

        for (const [groupLabel, fields] of grouped.entries()) {
          html += `<h3>${escapeHtml(groupLabel)}</h3><div class="comparison-table-wrap"><table><thead><tr><th>Field</th><th>${escapeHtml(left.maker)} ${escapeHtml(left.model)}</th><th>${escapeHtml(right.maker)} ${escapeHtml(right.model)}</th></tr></thead><tbody>`;
          for (const [fieldId, meta] of fields) {
            const a = left.researchedFields[fieldId];
            const b = right.researchedFields[fieldId];
            const aKnown = isKnown(a);
            const bKnown = isKnown(b);
            const aValue = aKnown ? formatValue(a.value) : '—';
            const bValue = bKnown ? formatValue(b.value) : '—';
            const diffClass = aValue !== bValue ? ' comparison-different' : '';
            const state = (entry) => {
              const label = entry ? evidenceLabel(entry.evidence) : '';
              return label ? `<div class="comparison-state">${escapeHtml(label)}</div>` : '';
            };
            html += `<tr class="${diffClass}"><th>${escapeHtml(meta.label)}</th><td>${escapeHtml(aValue)}${state(a)}${aKnown ? sourceLinks(a.sources) : ''}</td><td>${escapeHtml(bValue)}${state(b)}${bKnown ? sourceLinks(b.sources) : ''}</td></tr>`;
          }
          html += '</tbody></table></div>';
        }

        results.innerHTML = html;
        status.textContent = `${left.maker} ${left.model} vs ${right.maker} ${right.model}`;
      };

      leftSelect.addEventListener('change', render);
      rightSelect.addEventListener('change', render);
      host.querySelector('#comparison-print').addEventListener('click', () => window.print());
      host.querySelector('#comparison-copy-link').addEventListener('click', async () => {
        const link = permalink(leftSelect.value, rightSelect.value);
        try {
          await navigator.clipboard.writeText(link);
          status.textContent = 'Shareable comparison link copied.';
        } catch (error) {
          status.textContent = link;
        }
      });
      render();
    })
    .catch((error) => {
      host.innerHTML = `<p>The comparison data could not be loaded: ${escapeHtml(error.message)}</p>`;
    });
})();
