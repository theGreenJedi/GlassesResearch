(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const esc = (value) => String(value ?? '')
    .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#039;');

  const formatValue = (value) => {
    if (Array.isArray(value)) return value.join(', ');
    if (typeof value === 'boolean') return value ? 'Yes' : 'No';
    return String(value);
  };

  const isKnown = (entry) => entry && entry.evidence !== 'unknown' && entry.value !== 'Unknown' && entry.value !== null && entry.value !== '';
  const valueOf = (record, field) => isKnown(record.fields[field]) ? record.fields[field].value : null;
  const textOf = (record, field) => String(valueOf(record, field) ?? '').toLowerCase();
  const truthy = (record, field) => valueOf(record, field) === true;

  const sourceLinks = (entry) => {
    if (!entry?.sources?.length) return '';
    return `<div class="comparison-sources">${entry.sources.map((src, i) =>
      `<a href="${esc(src)}" target="_blank" rel="noopener">source${entry.sources.length > 1 ? ` ${i + 1}` : ''}</a>`).join(' · ')}</div>`;
  };

  const researchLinks = (record) => {
    const paths = record.public || {};
    const links = [];
    if (paths.profile) links.push(`<a href="${esc(paths.profile)}">Read profile</a>`);
    if (paths.report_card) links.push(`<a href="${esc(paths.report_card)}">Report card</a>`);
    if (paths.lineage) links.push(`<a href="${esc(paths.lineage)}">Lineage research</a>`);
    return links.length ? `<div class="comparison-research-links">${links.join(' · ')}</div>` : '';
  };

  Promise.all([
    fetch('../../data/comparisons.json', { cache: 'no-store' }).then((r) => {
      if (!r.ok) throw new Error(`Comparison data HTTP ${r.status}`);
      return r.json();
    }),
    fetch('../../data/devices.json', { cache: 'no-store' }).then((r) => {
      if (!r.ok) throw new Error(`Device data HTTP ${r.status}`);
      return r.json();
    }),
  ]).then(([bundle, deviceBundle]) => {
    const researched = new Map((bundle.records || []).map((record) => [record.id, record]));
    const devices = deviceBundle.records || [];
    if (devices.length < 2) throw new Error('Not enough device records are available.');

    const sourceUrls = (device) => (device.links || []).map((l) => l.url).filter(Boolean);
    const sourced = (value, sources) => ({ value, evidence: 'primary', sources });
    const records = devices.map((device) => {
      const existing = researched.get(device.id);
      const fields = existing ? { ...existing.fields } : {};
      const sources = sourceUrls(device);
      if (!fields.manufacturer) fields.manufacturer = sourced(device.maker, sources);
      if (!fields.release_year) fields.release_year = sourced(device.era, sources);
      if (!fields.status) fields.status = sourced(device.state, sources);
      if (!fields.category) fields.category = sourced(device.type, sources);
      return { ...device, fields };
    });

    const fieldMap = new Map();
    (bundle.groups || []).forEach((group) => (group.fields || []).forEach((field) =>
      fieldMap.set(field.id, { ...field, groupLabel: group.label })));

    const constraints = [
      { id: 'current', label: 'Currently available', test: (r) => /current|shipping|available|preorder/i.test(`${r.state} ${textOf(r, 'status')}`) && !/legacy|discontinued/i.test(`${r.state} ${textOf(r, 'status')}`) },
      { id: 'camera', label: 'Camera', test: (r) => Number(valueOf(r, 'camera_count')) > 0 || /camera/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()) },
      { id: 'display', label: 'Display', test: (r) => isKnown(r.fields.display) || isKnown(r.fields.display_type) || /display|ar|xr|hud/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()) },
      { id: 'prescription', label: 'Prescription support', test: (r) => truthy(r, 'prescription_support') },
      { id: 'bluetooth', label: 'Bluetooth', test: (r) => truthy(r, 'bluetooth') },
      { id: 'ble', label: 'BLE', test: (r) => truthy(r, 'ble') },
      { id: 'wifi', label: 'Wi-Fi', test: (r) => truthy(r, 'wifi') },
      { id: 'audio', label: 'Speakers / audio', test: (r) => isKnown(r.fields.speakers) || /audio/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()) },
      { id: 'translation', label: 'Translation', test: (r) => isKnown(r.fields.translation) },
      { id: 'developer', label: 'SDK / API access', test: (r) => isKnown(r.fields.sdk) || isKnown(r.fields.api) || /developer|open/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()) },
      { id: 'offline', label: 'Offline/local operation documented', test: (r) => {
        const v = textOf(r, 'offline_operation');
        return v && !/unknown|no|none/.test(v);
      }},
    ];

    const params = new URLSearchParams(location.search);
    const initialCompare = ['left', 'right', 'third', 'fourth'].map((key) => params.get(key)).filter((id) => records.some((r) => r.id === id));
    while (initialCompare.length < 2) {
      const candidate = records.find((r) => !initialCompare.includes(r.id));
      if (!candidate) break;
      initialCompare.push(candidate.id);
    }

    host.innerHTML = `
      <section class="discovery-panel">
        <div class="discovery-heading"><h2>Find glasses that fit your constraints</h2><p>Choose what matters. Exact matches rise to the top; near-matches show which requirements they miss. Every canonical model links back into its editorial research.</p></div>
        <label class="discovery-search">Search models, brands, categories or hardware <input id="discovery-query" type="search" placeholder="e.g. AR1, Solos, display, camera"></label>
        <div class="discovery-constraints">${constraints.map((c) => `<label><input type="checkbox" value="${c.id}"> ${esc(c.label)}</label>`).join('')}</div>
        <div class="discovery-actions"><label><input id="exact-only" type="checkbox"> Exact matches only</label><button type="button" id="clear-filters">Clear filters</button></div>
        <p id="discovery-status" class="comparison-status"></p>
        <div id="discovery-results" class="discovery-results"></div>
      </section>

      <section class="compare-panel">
        <div class="compare-heading"><h2>Compare side by side</h2><p>Compare two to four models. Turn on “differences only” when the table gets noisy. Profile, report-card, and lineage links stay attached to the selected devices.</p></div>
        <div class="comparison-controls">
          <label>Device A <select data-slot="0"></select></label>
          <label>Device B <select data-slot="1"></select></label>
          <label>Device C <select data-slot="2"><option value="">— none —</option></select></label>
          <label>Device D <select data-slot="3"><option value="">— none —</option></select></label>
          <label class="comparison-toggle"><input type="checkbox" id="differences-only"> Differences only</label>
          <button type="button" id="comparison-copy-link">Copy link</button>
          <button type="button" id="comparison-print">Print</button>
        </div>
        <p id="comparison-status" class="comparison-status"></p>
        <div id="comparison-selected-research"></div>
        <div id="comparison-results"></div>
      </section>`;

    const discoveryResults = host.querySelector('#discovery-results');
    const discoveryStatus = host.querySelector('#discovery-status');
    const queryInput = host.querySelector('#discovery-query');
    const exactOnly = host.querySelector('#exact-only');
    const constraintBoxes = [...host.querySelectorAll('.discovery-constraints input')];
    const compareSelects = [...host.querySelectorAll('.comparison-controls select[data-slot]')];
    const comparisonResults = host.querySelector('#comparison-results');
    const comparisonStatus = host.querySelector('#comparison-status');
    const comparisonSelectedResearch = host.querySelector('#comparison-selected-research');
    const differencesOnly = host.querySelector('#differences-only');

    const optionHtml = records.map((r) => `<option value="${esc(r.id)}">${esc(r.maker)} ${esc(r.model)}</option>`).join('');
    compareSelects.forEach((select, i) => {
      if (i < 2) select.innerHTML = optionHtml;
      else select.innerHTML = `<option value="">— none —</option>${optionHtml}`;
      select.value = initialCompare[i] || '';
    });

    const searchable = (r) => [r.id, r.maker, r.model, r.type, r.state, ...Object.values(r.fields).map((e) => isKnown(e) ? formatValue(e.value) : '')].join(' ').toLowerCase();

    const selectedConstraintIds = () => constraintBoxes.filter((b) => b.checked).map((b) => b.value);
    const constraintById = new Map(constraints.map((c) => [c.id, c]));

    const addToCompare = (id) => {
      const empty = compareSelects.find((s, i) => i >= 2 && !s.value);
      if (empty) empty.value = id;
      else compareSelects[1].value = id;
      renderComparison();
      host.querySelector('.compare-panel').scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    const renderDiscovery = () => {
      const query = queryInput.value.trim().toLowerCase();
      const chosen = selectedConstraintIds();
      const scored = records.map((record) => {
        if (query && !searchable(record).includes(query)) return null;
        const checks = chosen.map((id) => ({ id, ok: constraintById.get(id).test(record) }));
        const matched = checks.filter((x) => x.ok).length;
        return { record, checks, matched, total: chosen.length };
      }).filter(Boolean)
        .filter((x) => !exactOnly.checked || x.matched === x.total)
        .sort((a, b) => b.matched - a.matched || a.record.maker.localeCompare(b.record.maker) || a.record.model.localeCompare(b.record.model));

      const visible = scored.slice(0, 60);
      discoveryStatus.textContent = chosen.length
        ? `${scored.length} models shown · ranked by how many of your ${chosen.length} constraints they meet`
        : `${scored.length} models shown · add constraints to narrow the field`;

      discoveryResults.innerHTML = visible.map(({ record, checks, matched, total }) => {
        const misses = checks.filter((x) => !x.ok).map((x) => constraintById.get(x.id).label);
        const hits = checks.filter((x) => x.ok).map((x) => constraintById.get(x.id).label);
        const score = total ? `<strong>${matched}/${total} constraints matched</strong>` : `<strong>${esc(record.type || 'Smart glasses')}</strong>`;
        return `<article class="discovery-card ${total && matched === total ? 'exact-match' : ''}">
          <div class="discovery-card-head"><div><h3>${esc(record.maker)} ${esc(record.model)}</h3><div class="discovery-meta">${esc(record.id)} · ${esc(record.era || '')} · ${esc(record.state || '')} · ${esc(record.type || '')}</div></div><div class="match-score">${score}</div></div>
          ${hits.length ? `<div class="match-hits">✓ ${esc(hits.join(' · '))}</div>` : ''}
          ${misses.length ? `<div class="match-misses">Missing / not documented: ${esc(misses.join(' · '))}</div>` : ''}
          <div class="discovery-card-actions"><button type="button" data-compare-id="${esc(record.id)}">Add to comparison</button>${researchLinks(record)}</div>
        </article>`;
      }).join('') || '<p>No models match the current search and filters.</p>';

      discoveryResults.querySelectorAll('[data-compare-id]').forEach((button) =>
        button.addEventListener('click', () => addToCompare(button.dataset.compareId)));
    };

    const renderComparison = () => {
      const selectedIds = compareSelects.map((s) => s.value).filter(Boolean);
      const uniqueIds = [...new Set(selectedIds)];
      const selected = uniqueIds.map((id) => records.find((r) => r.id === id)).filter(Boolean);
      if (selected.length < 2) {
        comparisonResults.innerHTML = '<p>Select at least two different devices.</p>';
        comparisonStatus.textContent = '';
        comparisonSelectedResearch.innerHTML = '';
        return;
      }

      const url = new URL(location.href);
      ['left', 'right', 'third', 'fourth'].forEach((key, i) => {
        if (selected[i]) url.searchParams.set(key, selected[i].id); else url.searchParams.delete(key);
      });
      history.replaceState({}, '', url);

      comparisonSelectedResearch.innerHTML = selected.map((record) =>
        `<div class="comparison-selected-device"><strong>${esc(record.id)} · ${esc(record.maker)} ${esc(record.model)}</strong>${researchLinks(record)}</div>`
      ).join('');

      const grouped = new Map();
      for (const [fieldId, meta] of fieldMap.entries()) {
        const entries = selected.map((r) => r.fields[fieldId]);
        if (!entries.some(isKnown)) continue;
        const values = entries.map((e) => isKnown(e) ? formatValue(e.value) : '—');
        if (differencesOnly.checked && new Set(values).size <= 1) continue;
        if (!grouped.has(meta.groupLabel)) grouped.set(meta.groupLabel, []);
        grouped.get(meta.groupLabel).push([fieldId, meta]);
      }

      let html = '';
      for (const [groupLabel, fields] of grouped.entries()) {
        html += `<h3>${esc(groupLabel)}</h3><div class="comparison-table-wrap"><table><thead><tr><th>Field</th>${selected.map((r) => `<th>${esc(r.maker)} ${esc(r.model)}</th>`).join('')}</tr></thead><tbody>`;
        for (const [fieldId, meta] of fields) {
          const entries = selected.map((r) => r.fields[fieldId]);
          const values = entries.map((e) => isKnown(e) ? formatValue(e.value) : '—');
          const diffClass = new Set(values).size > 1 ? 'comparison-different' : '';
          html += `<tr class="${diffClass}"><th>${esc(meta.label)}</th>${entries.map((entry, i) => `<td>${esc(values[i])}${isKnown(entry) ? sourceLinks(entry) : ''}</td>`).join('')}</tr>`;
        }
        html += '</tbody></table></div>';
      }
      comparisonResults.innerHTML = html || '<p>No differing documented fields are available for this selection.</p>';
      comparisonStatus.textContent = `${selected.map((r) => `${r.maker} ${r.model}`).join(' vs ')} · ${records.length} models in the discovery pool`;
    };

    queryInput.addEventListener('input', renderDiscovery);
    constraintBoxes.forEach((b) => b.addEventListener('change', renderDiscovery));
    exactOnly.addEventListener('change', renderDiscovery);
    host.querySelector('#clear-filters').addEventListener('click', () => {
      queryInput.value = '';
      constraintBoxes.forEach((b) => { b.checked = false; });
      exactOnly.checked = false;
      renderDiscovery();
    });
    compareSelects.forEach((s) => s.addEventListener('change', renderComparison));
    differencesOnly.addEventListener('change', renderComparison);
    host.querySelector('#comparison-print').addEventListener('click', () => window.print());
    host.querySelector('#comparison-copy-link').addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(location.href);
        comparisonStatus.textContent = 'Shareable comparison link copied.';
      } catch (_) {
        comparisonStatus.textContent = location.href;
      }
    });

    renderDiscovery();
    renderComparison();
  }).catch((error) => {
    host.innerHTML = `<p>The discovery/comparison data could not be loaded: ${esc(error.message)}</p>`;
  });
})();
