(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const stateLabel = (evidence) => {
    if (evidence === 'unknown') return 'Unknown';
    return 'Verified';
  };

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

  fetch('../../data/comparisons.json')
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((bundle) => {
      const records = bundle.records || [];
      if (records.length < 2) {
        host.innerHTML = '<p>Not enough researched model records are available for a comparison yet.</p>';
        return;
      }

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
      const optionHtml = records.map((record) => `<option value="${record.id}">${record.id}</option>`).join('');
      leftSelect.innerHTML = optionHtml;
      rightSelect.innerHTML = optionHtml;
      leftSelect.value = initialLeft;
      rightSelect.value = initialRight;

      const fieldMap = new Map();
      (bundle.groups || []).forEach((group) => {
        (group.fields || []).forEach((field) => fieldMap.set(field.id, { ...field, groupLabel: group.label }));
      });

      const render = () => {
        const left = records.find((record) => record.id === leftSelect.value);
        const right = records.find((record) => record.id === rightSelect.value);
        const url = new URL(window.location.href);
        url.searchParams.set('left', left.id);
        url.searchParams.set('right', right.id);
        window.history.replaceState({}, '', url);

        const grouped = new Map();
        for (const [fieldId, meta] of fieldMap.entries()) {
          if (!grouped.has(meta.groupLabel)) grouped.set(meta.groupLabel, []);
          grouped.get(meta.groupLabel).push([fieldId, meta]);
        }

        let html = '';
        for (const [groupLabel, fields] of grouped.entries()) {
          html += `<h3>${groupLabel}</h3><div class="comparison-table-wrap"><table><thead><tr><th>Field</th><th>${left.id}</th><th>${right.id}</th></tr></thead><tbody>`;
          for (const [fieldId, meta] of fields) {
            const a = left.fields[fieldId];
            const b = right.fields[fieldId];
            const aValue = formatValue(a.value);
            const bValue = formatValue(b.value);
            const diffClass = aValue !== bValue ? ' comparison-different' : '';
            const sourceLink = (entry) => entry.sources && entry.sources.length ? `<div class="comparison-sources">${entry.sources.map((src) => `<a href="${src}">source</a>`).join(' · ')}</div>` : '';
            html += `<tr class="${diffClass}"><th>${meta.label}</th><td>${aValue}<div class="comparison-state">${stateLabel(a.evidence)}</div>${sourceLink(a)}</td><td>${bValue}<div class="comparison-state">${stateLabel(b.evidence)}</div>${sourceLink(b)}</td></tr>`;
          }
          html += '</tbody></table></div>';
        }
        results.innerHTML = html;
        status.textContent = `${left.id} vs ${right.id} — Unknown means the current research record does not support a value yet.`;
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
