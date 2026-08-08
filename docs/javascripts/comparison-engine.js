(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

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

  Promise.all([
    fetch('../../data/comparisons.json').then((response) => {
      if (!response.ok) throw new Error(`Comparison data HTTP ${response.status}`);
      return response.json();
    }),
    fetch('../../data/devices.json').then((response) => {
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

      const sourceUrls = (device) => (device.links || [])
        .map((link) => link.url)
        .filter((url) => typeof url === 'string' && url.length);

      const sourced = (value, sources) => ({
        value,
        evidence: 'primary',
        sources,
      });

      const records = devices.map((device) => {
        const existing = researched.get(device.id);
        const fields = existing ? { ...existing.fields } : {};
        const sources = sourceUrls(device);

        if (!fields.manufacturer) fields.manufacturer = sourced(device.maker, sources);
        if (!fields.release_year) fields.release_year = sourced(device.era, sources);
        if (!fields.status) fields.status = sourced(device.state, sources);
        if (!fields.category) fields.category = sourced(device.type, sources);

        return {
          id: device.id,
          maker: device.maker,
          model: device.model,
          fields,
        };
      });

      const params = new URLSearchParams(window.location.search);
      const ids = records.map((record) => record.id);
      const initialLeft = ids.includes(params.get('left')) ? params.get('left') : ids[0];
      const initialRight = ids.includes(params.get('right')) ? params.get('right') : ids[1];

      host.innerHTML = `
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
        .map((record) => `<option value="${record.id}">${record.maker} ${record.model} — ${record.id}</option>`)
        .join('');
      leftSelect.innerHTML = optionHtml;
      rightSelect.innerHTML = optionHtml;
      leftSelect.value = initialLeft;
      rightSelect.value = initialRight;

      const fieldMap = new Map();
      (bundle.groups || []).forEach((group) => {
        (group.fields || []).forEach((field) => fieldMap.set(field.id, { ...field, groupLabel: group.label }));
      });

      const isKnown = (entry) => entry && entry.evidence !== 'unknown' && entry.value !== 'Unknown';

      const render = () => {
        const left = records.find((record) => record.id === leftSelect.value);
        const right = records.find((record) => record.id === rightSelect.value);
        const url = new URL(window.location.href);
        url.searchParams.set('left', left.id);
        url.searchParams.set('right', right.id);
        window.history.replaceState({}, '', url);

        const grouped = new Map();
        for (const [fieldId, meta] of fieldMap.entries()) {
          const a = left.fields[fieldId];
          const b = right.fields[fieldId];
          if (!isKnown(a) && !isKnown(b)) continue;
          if (!grouped.has(meta.groupLabel)) grouped.set(meta.groupLabel, []);
          grouped.get(meta.groupLabel).push([fieldId, meta]);
        }

        let html = '';
        for (const [groupLabel, fields] of grouped.entries()) {
          html += `<h3>${groupLabel}</h3><div class="comparison-table-wrap"><table><thead><tr><th>Field</th><th>${left.maker} ${left.model}</th><th>${right.maker} ${right.model}</th></tr></thead><tbody>`;
          for (const [fieldId, meta] of fields) {
            const a = left.fields[fieldId];
            const b = right.fields[fieldId];
            const aKnown = isKnown(a);
            const bKnown = isKnown(b);
            const aValue = aKnown ? formatValue(a.value) : '—';
            const bValue = bKnown ? formatValue(b.value) : '—';
            const diffClass = aValue !== bValue ? ' comparison-different' : '';
            const sourceLink = (entry) => entry && entry.sources && entry.sources.length
              ? `<div class="comparison-sources">${entry.sources.map((src) => `<a href="${src}">source</a>`).join(' · ')}</div>`
              : '';
            const state = (entry) => {
              const label = entry ? evidenceLabel(entry.evidence) : '';
              return label ? `<div class="comparison-state">${label}</div>` : '';
            };
            html += `<tr class="${diffClass}"><th>${meta.label}</th><td>${aValue}${state(a)}${sourceLink(a)}</td><td>${bValue}${state(b)}${sourceLink(b)}</td></tr>`;
          }
          html += '</tbody></table></div>';
        }
        results.innerHTML = html || '<p>No sourced comparison fields are available for this pair yet.</p>';
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
      host.innerHTML = `<p>The comparison data could not be loaded: ${error.message}</p>`;
    });
})();
