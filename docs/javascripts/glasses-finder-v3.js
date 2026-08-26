(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const esc = (value) => String(value ?? '')
    .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#039;');

  const known = (entry) => entry && entry.evidence !== 'unknown' && entry.value !== 'Unknown' && entry.value !== null && entry.value !== '';
  const valueOf = (record, field) => known(record.fields?.[field]) ? record.fields[field].value : null;
  const textOf = (record, field) => String(valueOf(record, field) ?? '').toLowerCase();
  const yes = (record, field) => valueOf(record, field) === true || /^yes$/i.test(String(valueOf(record, field) ?? ''));

  const fetchJson = (url, label) => fetch(url, { cache: 'no-store' }).then((r) => {
    if (!r.ok) throw new Error(`${label} HTTP ${r.status}`);
    return r.json();
  });

  Promise.all([
    fetchJson('../../data/comparisons.json', 'Comparison data'),
    fetchJson('../../data/devices.json', 'Device data'),
    fetchJson('../../data/finder-schema.json', 'Finder schema'),
    fetchJson('../../data/purchase-sources.json', 'Purchase sources'),
    fetchJson('../../data/finder-capabilities.json', 'Finder capability matrix'),
    fetchJson('../../data/report-card-scores.json', 'Report Card scores'),
    fetchJson('../../data/price-observations.json', 'Price observations'),
  ]).then(([bundle, deviceBundle, finderSchema, purchaseBundle, capabilityBundle, reportCardBundle, priceBundle]) => {
    const researched = new Map((bundle.records || []).map((r) => [r.id, r]));
    const purchaseById = new Map((purchaseBundle.records || []).map((r) => [r.id, r.sources || []]));
    const capabilityById = new Map((capabilityBundle.records || []).map((r) => [r.id, r.capabilities || {}]));
    const reportCardById = new Map((reportCardBundle.records || []).map((r) => [r.id, r.scores || {}]));
    const priceById = new Map();
    (priceBundle.records || []).forEach((observation) => {
      if (!priceById.has(observation.id)) priceById.set(observation.id, []);
      priceById.get(observation.id).push(observation);
    });
    const devices = deviceBundle.records || [];
    if (!devices.length) throw new Error('No canonical device records are available.');

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
      return {
        ...device,
        fields,
        purchaseSources: purchaseById.get(device.id) || [],
        capabilityFacts: capabilityById.get(device.id) || {},
        reportCardScores: reportCardById.get(device.id) || {},
        priceObservations: priceById.get(device.id) || [],
      };
    });

    const fieldMap = new Map();
    (bundle.groups || []).forEach((group) => (group.fields || []).forEach((field) =>
      fieldMap.set(field.id, { ...field, groupLabel: group.label })));

    const aliases = {
      camera: (r) => Number(valueOf(r, 'camera_count')) > 0 || /camera/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()),
      no_camera: (r) => {
        const count = valueOf(r, 'camera_count');
        if (count !== null) return Number(count) === 0;
        const camera = r.capabilityFacts?.camera?.value;
        return camera === 'no' || camera === 'na';
      },
      photo_capture: (r) => yes(r, 'photo_capture') || yes(r, 'photos') || Number(valueOf(r, 'camera_count')) > 0,
      video_recording: (r) => yes(r, 'video_recording') || /video/.test(`${textOf(r, 'camera')} ${textOf(r, 'recording')} ${textOf(r, 'video')}`),
      live_video: (r) => yes(r, 'live_video') || yes(r, 'streaming') || /stream|rtmp|live video/.test(`${textOf(r, 'api')} ${textOf(r, 'sdk')} ${textOf(r, 'video')}`),
      prescription_support: (r) => yes(r, 'prescription_support'),
      progressive_lenses: (r) => yes(r, 'progressive_lenses') || /progressive/.test(textOf(r, 'prescription_support')),
      ordinary_optician: (r) => yes(r, 'ordinary_optician') || /ordinary|local opti|any opti|optical shop/.test(`${textOf(r, 'prescription_serviceability')} ${textOf(r, 'prescription_support')}`),
      adjustable_diopter: (r) => yes(r, 'adjustable_diopter') || /diopter|myopia adjustment/.test(`${textOf(r, 'display')} ${textOf(r, 'optics')}`),
      speakers: (r) => yes(r, 'speakers') || (known(r.fields?.speakers) && !/^no$/i.test(String(valueOf(r, 'speakers')))) || /audio/.test(`${r.type}`.toLowerCase()),
      microphones: (r) => yes(r, 'microphones') || Number(valueOf(r, 'microphone_count')) > 0 || known(r.fields?.microphones),
      phone_calls: (r) => yes(r, 'phone_calls') || /call/.test(`${textOf(r, 'audio')} ${textOf(r, 'features')}`),
      music: (r) => yes(r, 'music') || /music|audio/.test(`${r.type} ${textOf(r, 'audio')}`.toLowerCase()),
      display: (r) => known(r.fields?.display) || known(r.fields?.display_type) || /display|ar|xr|hud/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()),
      full_color_display: (r) => /color|micro-?oled|oled/.test(`${textOf(r, 'display')} ${textOf(r, 'display_type')}`),
      binocular_display: (r) => /binocular|dual-eye|two-eye/.test(`${textOf(r, 'display')} ${textOf(r, 'display_type')}`),
      ai_assistant: (r) => yes(r, 'ai_assistant') || /ai|assistant|alexa|gemini|meta ai/.test(`${r.type} ${textOf(r, 'features')} ${textOf(r, 'ai')}`.toLowerCase()),
      visual_ai: (r) => yes(r, 'visual_ai') || (aliases.camera(r) && /ai|vision|visual/.test(`${r.type} ${textOf(r, 'ai')}`.toLowerCase())),
      translation: (r) => known(r.fields?.translation) && !/^no$/i.test(String(valueOf(r, 'translation'))),
      transcription: (r) => yes(r, 'transcription') || /transcri|caption|speech.?to.?text/.test(`${textOf(r, 'features')} ${textOf(r, 'ai')}`),
      navigation: (r) => yes(r, 'navigation') || /navigation|directions|maps/.test(`${textOf(r, 'features')} ${textOf(r, 'software')}`),
      bluetooth: (r) => yes(r, 'bluetooth'),
      ble: (r) => yes(r, 'ble'),
      wifi: (r) => yes(r, 'wifi'),
      sdk_api: (r) => known(r.fields?.sdk) || known(r.fields?.api) || /developer|sdk|api|open/.test(`${r.type} ${textOf(r, 'category')}`.toLowerCase()),
      open_source: (r) => yes(r, 'open_source') || /open source|open-source|mit licensed/.test(`${textOf(r, 'openness')} ${textOf(r, 'sdk')}`),
      custom_ai: (r) => yes(r, 'custom_ai') || /custom ai|own endpoint|replaceable|webhook|self-host/.test(`${textOf(r, 'owner_control')} ${textOf(r, 'api')} ${textOf(r, 'sdk')}`),
      offline_operation: (r) => { const v = textOf(r, 'offline_operation'); return Boolean(v && !/unknown|none|^no$/.test(v)); },
      self_hostable: (r) => yes(r, 'self_hostable') || /self-host|self host|local cloud/.test(`${textOf(r, 'cloud_independence')} ${textOf(r, 'owner_control')}`),
    };

    const capabilityState = (r, field) => r.capabilityFacts?.[field]?.value || 'unknown';
    const currentAvailable = (r) => /current|shipping|available|preorder/i.test(`${r.state} ${textOf(r, 'status')}`) && !/legacy|discontinued|end of life|eol/i.test(`${r.state} ${textOf(r, 'status')}`);
    const purchaseMatches = (r, filter) => {
      const sources = r.purchaseSources || [];
      if (filter.type === 'purchase') return filter.field === 'available_new' ? (currentAvailable(r) || sources.some((s) => s.availability === 'available' && ['new','refurbished'].includes(s.condition))) : false;
      if (filter.type === 'purchase_source') return sources.some((s) => s.source_type === filter.value);
      if (filter.type === 'condition') return sources.some((s) => s.condition === filter.value);
      return false;
    };

    const filterState = (r, filter) => {
      if (filter.type === 'capability') {
        const canonical = capabilityState(r, filter.field);
        if (canonical === 'yes') return 'yes';
        if (canonical === 'no') return 'no';
        if (canonical === 'na') return 'na';
        if (filter.field === 'no_display') return 'unknown';
        const fn = aliases[filter.field];
        return (fn ? Boolean(fn(r)) : yes(r, filter.field)) ? 'inferred-yes' : 'unknown';
      }
      if (filter.type === 'report_score') {
        const score = r.reportCardScores?.[filter.field];
        if (typeof score !== 'number') return score === 'na' ? 'na' : 'unknown';
        return score >= filter.min ? 'yes' : 'no';
      }
      if (filter.type === 'price_max') {
        const prices = (r.priceObservations || []).map((p) => Number(p.price_usd)).filter(Number.isFinite);
        if (!prices.length) return 'unknown';
        return Math.min(...prices) <= Number(filter.value) ? 'yes' : 'no';
      }
      return purchaseMatches(r, filter) ? 'yes' : 'no';
    };
    const filterMatches = (r, filter) => ['yes', 'inferred-yes'].includes(filterState(r, filter));

    const params = new URLSearchParams(location.search);
    const initialCompare = ['left','right','third','fourth'].map((k) => params.get(k)).filter((id) => records.some((r) => r.id === id));
    while (initialCompare.length < 2) {
      const candidate = records.find((r) => !initialCompare.includes(r.id));
      if (!candidate) break;
      initialCompare.push(candidate.id);
    }

    const filterMarkup = (finderSchema.groups || []).map((group) => `
      <fieldset class="finder-group" data-group="${esc(group.id)}">
        <legend>${esc(group.label)}</legend>
        <div class="finder-options">${(group.filters || []).map((f) => `<label><input type="checkbox" value="${esc(f.id)}"> <span>${esc(f.label)}</span><small data-count-for="${esc(f.id)}"></small></label>`).join('')}</div>
      </fieldset>`).join('');

    const advancedMarkup = (reportCardBundle.dimensions || []).map((dimension) => `
      <div class="finder-score-filter">
        <label><input type="checkbox" data-score-enable="${esc(dimension.id)}"> ${esc(dimension.label)} ≥ <output data-score-output="${esc(dimension.id)}">7</output></label>
        <input type="range" data-score-range="${esc(dimension.id)}" min="0" max="10" step="0.5" value="7" disabled aria-label="Minimum ${esc(dimension.label)} score">
      </div>`).join('');

    host.innerHTML = `
      <section class="discovery-panel glasses-finder">
        <div class="discovery-heading"><h2>Find glasses that do what you need</h2><p>Pick requirements like prescription lenses, video recording, audio, AI, display, price, or where you are willing to buy. Results narrow immediately. Open the research only after you have a useful shortlist.</p></div>
        <label class="discovery-search">Search by model or brand <input id="discovery-query" type="search" placeholder="e.g. Solos, Meta, Rokid, Vuzix"></label>
        <div class="finder-groups">${filterMarkup}</div>
        <details class="finder-advanced"><summary>Advanced filters · Report Card scores</summary><p>Enable only the dimensions you care about. Models without a documented score do not pass an enabled minimum.</p><div class="finder-score-grid">${advancedMarkup}</div></details>
        <div class="discovery-actions"><label><input id="exact-only" type="checkbox" checked> Exact matches only</label><button type="button" id="clear-filters">Clear filters</button></div>
        <p id="discovery-status" class="comparison-status"></p>
        <div id="discovery-results" class="discovery-results"></div>
      </section>
      <section class="compare-panel">
        <div class="compare-heading"><h2>Compare selected candidates</h2><p>Compare two to four models after narrowing the field. Deep research remains attached to each candidate.</p></div>
        <div class="comparison-controls">
          <label>Device A <select data-slot="0"></select></label><label>Device B <select data-slot="1"></select></label>
          <label>Device C <select data-slot="2"></select></label><label>Device D <select data-slot="3"></select></label>
          <label class="comparison-toggle"><input type="checkbox" id="differences-only"> Differences only</label>
          <button type="button" id="comparison-copy-link">Copy link</button><button type="button" id="comparison-print">Print</button>
        </div>
        <p id="comparison-status" class="comparison-status"></p><div id="comparison-selected-research"></div><div id="comparison-results"></div>
      </section>`;

    const queryInput = host.querySelector('#discovery-query');
    const exactOnly = host.querySelector('#exact-only');
    const boxes = [...host.querySelectorAll('.finder-options input[type=checkbox]')];
    const requestedFilters = new Set((params.get('filters') || '').split(',').map((id) => id.trim()).filter(Boolean));
    boxes.forEach((box) => { box.checked = requestedFilters.has(box.value); });
    const scoreEnables = [...host.querySelectorAll('[data-score-enable]')];
    const scoreRanges = [...host.querySelectorAll('[data-score-range]')];
    const results = host.querySelector('#discovery-results');
    const status = host.querySelector('#discovery-status');
    const compareSelects = [...host.querySelectorAll('.comparison-controls select[data-slot]')];
    const comparisonResults = host.querySelector('#comparison-results');
    const comparisonStatus = host.querySelector('#comparison-status');
    const comparisonSelectedResearch = host.querySelector('#comparison-selected-research');
    const differencesOnly = host.querySelector('#differences-only');

    const filters = new Map();
    (finderSchema.groups || []).forEach((g) => (g.filters || []).forEach((f) => filters.set(f.id, { ...f, group: g.label })));
    const reportLabels = new Map((reportCardBundle.dimensions || []).map((d) => [d.id, d.label]));
    const optionHtml = records.map((r) => `<option value="${esc(r.id)}">${esc(r.maker)} ${esc(r.model)}</option>`).join('');
    compareSelects.forEach((s, i) => { s.innerHTML = `${i >= 2 ? '<option value="">— none —</option>' : ''}${optionHtml}`; s.value = initialCompare[i] || ''; });

    const researchLinks = (r) => {
      const p = r.public || {}; const links = [];
      if (p.profile) links.push(`<a href="${esc(p.profile)}">Canonical model</a>`);
      if (p.report_card) links.push(`<a href="${esc(p.report_card)}">Report Card</a>`);
      if (p.lineage) links.push(`<a href="${esc(p.lineage)}">Evidence / lineage</a>`);
      return links.join(' · ');
    };
    const purchaseLinks = (r) => (r.purchaseSources || []).filter((s) => s.url && s.availability !== 'unavailable').map((s) => {
      const label = s.label || s.retailer || s.source_type.replaceAll('_',' ');
      const condition = s.condition && s.condition !== 'new' ? ` · ${s.condition}` : '';
      return `<a class="purchase-link" href="${esc(s.url)}" target="_blank" rel="noopener">${esc(label)}${esc(condition)}</a>`;
    }).join(' ');
    const lowestPrice = (r) => (r.priceObservations || []).filter((p) => Number.isFinite(Number(p.price_usd))).sort((a,b) => Number(a.price_usd)-Number(b.price_usd))[0] || null;
    const priceLine = (r) => {
      const p = lowestPrice(r);
      if (!p) return '';
      const date = p.observed_at ? ` · checked ${p.observed_at}` : '';
      const condition = p.condition ? ` · ${p.condition}` : '';
      return `<div class="finder-price"><strong>$${Number(p.price_usd).toLocaleString(undefined,{minimumFractionDigits:Number(p.price_usd)%1?2:0,maximumFractionDigits:2})}</strong>${esc(condition)}${esc(date)}</div>`;
    };
    const searchable = (r) => [r.id,r.maker,r.model,r.type,r.state].join(' ').toLowerCase();
    const chosen = () => {
      const basic = boxes.filter((b) => b.checked).map((b) => filters.get(b.value));
      const advanced = scoreEnables.filter((b) => b.checked).map((b) => {
        const id = b.dataset.scoreEnable;
        const range = host.querySelector(`[data-score-range="${CSS.escape(id)}"]`);
        return { id: `score_${id}`, type: 'report_score', field: id, min: Number(range?.value || 0), label: `${reportLabels.get(id) || id} ≥ ${range?.value || 0}`, group: 'Report Card' };
      });
      return [...basic, ...advanced];
    };

    const addToCompare = (id) => {
      const empty = compareSelects.find((s, i) => i >= 2 && !s.value);
      if (empty) empty.value = id; else if (compareSelects[0].value !== id) compareSelects[1].value = id;
      renderComparison();
    };

    const compute = (selected, query) => records.map((record) => {
      if (query && !searchable(record).includes(query)) return null;
      const checks = selected.map((f) => ({ filter: f, state: filterState(record, f), ok: filterMatches(record, f) }));
      const matched = checks.filter((x) => x.ok).length;
      return { record, checks, matched, total: selected.length };
    }).filter(Boolean);

    const updateCounts = (selected, query) => {
      for (const [id, filter] of filters.entries()) {
        const other = selected.filter((f) => f.id !== id);
        const count = compute([...other, filter], query).filter((x) => x.matched === x.total).length;
        const node = host.querySelector(`[data-count-for="${CSS.escape(id)}"]`);
        if (node) node.textContent = ` ${count}`;
      }
    };

    const renderDiscovery = () => {
      const query = queryInput.value.trim().toLowerCase();
      const selected = chosen();
      let scored = compute(selected, query);
      if (exactOnly.checked) scored = scored.filter((x) => x.matched === x.total);
      scored.sort((a,b) => b.matched-a.matched || Number(Boolean(b.record.purchaseSources.length))-Number(Boolean(a.record.purchaseSources.length)) || a.record.maker.localeCompare(b.record.maker) || a.record.model.localeCompare(b.record.model));
      updateCounts(selected, query);
      status.textContent = selected.length ? `${scored.length} candidates match your current view · ${selected.length} requirements selected` : `${scored.length} glasses in the catalog · choose a requirement to narrow the field`;
      results.innerHTML = scored.slice(0,80).map(({record,checks,matched,total}) => {
        const hits = checks.filter((x) => x.ok).map((x) => x.filter.label);
        const knownMisses = checks.filter((x) => !x.ok && ['no','na'].includes(x.state)).map((x) => x.filter.label);
        const unknownMisses = checks.filter((x) => !x.ok && !['no','na'].includes(x.state)).map((x) => x.filter.label);
        const buys = purchaseLinks(record);
        return `<article class="discovery-card ${total && matched===total?'exact-match':''}">
          <div class="discovery-card-head"><div><h3>${esc(record.maker)} ${esc(record.model)}</h3><div class="discovery-meta">${esc(record.id)} · ${esc(record.era||'')} · ${esc(record.state||'')}</div></div><div class="match-score"><strong>${total?`${matched}/${total} matched`:esc(record.type||'Smart glasses')}</strong></div></div>
          ${priceLine(record)}
          ${hits.length?`<div class="match-hits">✓ ${esc(hits.join(' · '))}</div>`:''}
          ${knownMisses.length?`<div class="match-misses">Does not match: ${esc(knownMisses.join(' · '))}</div>`:''}
          ${unknownMisses.length?`<div class="match-misses">Not documented: ${esc(unknownMisses.join(' · '))}</div>`:''}
          ${buys?`<div class="purchase-sources"><strong>Buy / find one:</strong> ${buys}</div>`:'<div class="purchase-sources purchase-unknown">Purchase links not populated yet.</div>'}
          <div class="discovery-card-actions"><button type="button" data-compare-id="${esc(record.id)}">Shortlist / compare</button><span><strong>Research path:</strong> Summary → ${researchLinks(record) || 'canonical research pending'}</span></div>
        </article>`;
      }).join('') || `<div class="finder-zero"><strong>No exact matches.</strong><p>Unknown, No, and N/A are not treated as matches. Remove one criterion or include near matches to continue.</p><button type="button" data-remove-criterion ${selected.length ? '' : 'disabled'}>Remove last criterion</button> <button type="button" data-show-near>Show near matches</button></div>`;
      results.querySelectorAll('[data-compare-id]').forEach((b) => b.addEventListener('click', () => addToCompare(b.dataset.compareId)));
      results.querySelector('[data-remove-criterion]')?.addEventListener('click', () => {
        const checked = boxes.filter((box) => box.checked);
        const last = checked[checked.length - 1];
        if (last) last.checked = false;
        renderDiscovery();
      });
      results.querySelector('[data-show-near]')?.addEventListener('click', () => {
        exactOnly.checked = false;
        renderDiscovery();
      });
    };

    const sourceLinks = (entry) => entry?.sources?.length ? `<div class="comparison-sources">${entry.sources.map((src,i)=>`<a href="${esc(src)}" target="_blank" rel="noopener">source${entry.sources.length>1?` ${i+1}`:''}</a>`).join(' · ')}</div>` : '';
    const formatValue = (v) => Array.isArray(v) ? v.join(', ') : typeof v === 'boolean' ? (v?'Yes':'No') : String(v);
    const renderComparison = () => {
      const selected = [...new Set(compareSelects.map((s)=>s.value).filter(Boolean))].map((id)=>records.find((r)=>r.id===id)).filter(Boolean);
      if (selected.length < 2) { comparisonResults.innerHTML='<p>Select at least two different devices.</p>'; comparisonStatus.textContent=''; comparisonSelectedResearch.innerHTML=''; return; }
      const url = new URL(location.href); ['left','right','third','fourth'].forEach((k,i)=>selected[i]?url.searchParams.set(k,selected[i].id):url.searchParams.delete(k)); history.replaceState({},'',url);
      comparisonSelectedResearch.innerHTML = selected.map((r)=>`<div class="comparison-selected-device"><strong>${esc(r.id)} · ${esc(r.maker)} ${esc(r.model)}</strong>${priceLine(r)}<div>${researchLinks(r)}</div>${purchaseLinks(r)?`<div class="purchase-sources"><strong>Buy / find:</strong> ${purchaseLinks(r)}</div>`:''}</div>`).join('');
      const grouped = new Map();
      for (const [fieldId,meta] of fieldMap.entries()) { const entries=selected.map((r)=>r.fields[fieldId]); if(!entries.some(known)) continue; const vals=entries.map((e)=>known(e)?formatValue(e.value):'—'); if(differencesOnly.checked&&new Set(vals).size<=1) continue; if(!grouped.has(meta.groupLabel)) grouped.set(meta.groupLabel,[]); grouped.get(meta.groupLabel).push([fieldId,meta]); }
      let html=''; for(const [groupLabel,fields] of grouped.entries()){ html+=`<h3>${esc(groupLabel)}</h3><div class="comparison-table-wrap"><table><thead><tr><th>Field</th>${selected.map((r)=>`<th>${esc(r.maker)} ${esc(r.model)}</th>`).join('')}</tr></thead><tbody>`; for(const [fieldId,meta] of fields){const entries=selected.map((r)=>r.fields[fieldId]); const vals=entries.map((e)=>known(e)?formatValue(e.value):'—'); html+=`<tr class="${new Set(vals).size>1?'comparison-different':''}"><th>${esc(meta.label)}</th>${entries.map((e,i)=>`<td>${esc(vals[i])}${known(e)?sourceLinks(e):''}</td>`).join('')}</tr>`;} html+='</tbody></table></div>'; }
      comparisonResults.innerHTML=html||'<p>No documented comparison fields are available for this selection.</p>'; comparisonStatus.textContent=`${selected.map((r)=>`${r.maker} ${r.model}`).join(' vs ')} · ${records.length} models in Finder`;
    };

    queryInput.addEventListener('input', renderDiscovery);
    boxes.forEach((b)=>b.addEventListener('change',renderDiscovery));
    exactOnly.addEventListener('change',renderDiscovery);
    scoreEnables.forEach((b) => b.addEventListener('change', () => {
      const id = b.dataset.scoreEnable;
      const range = host.querySelector(`[data-score-range="${CSS.escape(id)}"]`);
      if (range) range.disabled = !b.checked;
      renderDiscovery();
    }));
    scoreRanges.forEach((range) => range.addEventListener('input', () => {
      const id = range.dataset.scoreRange;
      const output = host.querySelector(`[data-score-output="${CSS.escape(id)}"]`);
      if (output) output.value = range.value;
      renderDiscovery();
    }));
    host.querySelector('#clear-filters').addEventListener('click',()=>{
      queryInput.value=''; boxes.forEach((b)=>{b.checked=false;}); exactOnly.checked=true;
      scoreEnables.forEach((b)=>{b.checked=false;}); scoreRanges.forEach((r)=>{r.value='7';r.disabled=true;});
      host.querySelectorAll('[data-score-output]').forEach((o)=>{o.value='7';}); renderDiscovery();
    });
    compareSelects.forEach((s)=>s.addEventListener('change',renderComparison)); differencesOnly.addEventListener('change',renderComparison);
    host.querySelector('#comparison-copy-link').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(location.href);comparisonStatus.textContent='Comparison link copied.';}catch{comparisonStatus.textContent='Copy failed; copy the browser URL instead.';}});
    host.querySelector('#comparison-print').addEventListener('click',()=>window.print());
    renderDiscovery(); renderComparison();
  }).catch((error) => { host.innerHTML=`<p class="comparison-status">The Glasses Finder could not load: ${esc(error.message)}</p>`; });
})();