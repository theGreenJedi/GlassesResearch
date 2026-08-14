(() => {
  const host = document.getElementById('homepage-finder-app');
  if (!host) return;

  const esc = (value) => String(value ?? '')
    .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#039;');

  const filters = [
    { id: 'prescription', label: 'Prescription lenses', capability: 'prescription_support' },
    { id: 'video_recording', label: 'Records video', capability: 'video_recording' },
    { id: 'display', label: 'HUD / display', capability: 'display' },
    { id: 'sdk', label: 'SDK / API', capability: 'sdk_api' },
    { id: 'open_source', label: 'Open source', capability: 'open_source' },
    { id: 'offline', label: 'Local / offline operation', capability: 'offline_operation' },
    { id: 'custom_ai', label: 'Custom / replaceable AI', capability: 'custom_ai' },
    { id: 'under_500', label: 'Under $500', priceMax: 500 },
  ];

  const json = (path) => fetch(new URL(path, document.baseURI), { cache: 'no-store' }).then((response) => {
    if (!response.ok) throw new Error(`${path} HTTP ${response.status}`);
    return response.json();
  });

  Promise.all([
    json('data/devices.json'),
    json('data/finder-capabilities.json'),
    json('data/price-observations.json'),
  ]).then(([deviceBundle, capabilityBundle, priceBundle]) => {
    const devices = deviceBundle.records || [];
    const capabilities = new Map((capabilityBundle.records || []).map((record) => [record.id, record.capabilities || {}]));
    const prices = new Map();
    (priceBundle.records || []).forEach((observation) => {
      const price = Number(observation.price_usd);
      if (!Number.isFinite(price)) return;
      if (!prices.has(observation.id)) prices.set(observation.id, []);
      prices.get(observation.id).push(price);
    });

    const passes = (device, filter) => {
      if (filter.priceMax) return (prices.get(device.id) || []).some((price) => price <= filter.priceMax);
      return capabilities.get(device.id)?.[filter.capability]?.value === 'yes';
    };

    host.innerHTML = `
      <section class="home-finder" aria-labelledby="home-finder-title">
        <div class="home-finder-heading">
          <h3 id="home-finder-title">What must your glasses do?</h3>
          <p>Check every requirement that matters. Unknown capabilities do not count as matches.</p>
        </div>
        <div class="home-finder-options">
          ${filters.map((filter) => `<label><input type="checkbox" value="${esc(filter.id)}"> <span>${esc(filter.label)}</span><small data-count-for="${esc(filter.id)}"></small></label>`).join('')}
        </div>
        <div class="home-finder-summary">
          <p data-home-finder-status aria-live="polite"></p>
          <button type="button" data-home-finder-clear>Clear</button>
        </div>
        <div class="home-finder-preview" data-home-finder-preview></div>
        <a class="home-finder-open" data-home-finder-open href="docs/COMPARISON_ENGINE/">Open the complete Finder with these requirements →</a>
      </section>`;

    const boxes = [...host.querySelectorAll('input[type=checkbox]')];
    const status = host.querySelector('[data-home-finder-status]');
    const preview = host.querySelector('[data-home-finder-preview]');
    const open = host.querySelector('[data-home-finder-open]');

    const render = () => {
      const selectedIds = boxes.filter((box) => box.checked).map((box) => box.value);
      const selected = filters.filter((filter) => selectedIds.includes(filter.id));
      const matches = selected.length ? devices.filter((device) => selected.every((filter) => passes(device, filter))) : [];
      status.innerHTML = selected.length
        ? `<strong>${matches.length}</strong> of ${devices.length} models match ${selected.length} requirement${selected.length === 1 ? '' : 's'}.`
        : `<strong>${devices.length}</strong> models are ready to filter.`;
      preview.innerHTML = selected.length
        ? (matches.slice(0, 3).map((device) => `<article><strong>${esc(device.maker)} ${esc(device.model)}</strong><span>${esc(device.type || 'Smart glasses')} · ${esc(device.state || 'Status unknown')}</span></article>`).join('') || '<p><strong>0 found.</strong> No candidates fulfill all of your criteria.</p>')
        : '<p>Choose a requirement to reveal matching models.</p>';
      open.href = selectedIds.length
        ? `docs/COMPARISON_ENGINE/?filters=${encodeURIComponent(selectedIds.join(','))}`
        : 'docs/COMPARISON_ENGINE/';
      boxes.forEach((box) => {
        const candidate = filters.find((filter) => filter.id === box.value);
        const other = selected.filter((filter) => filter.id !== box.value);
        const count = devices.filter((device) => [...other, candidate].every((filter) => passes(device, filter))).length;
        host.querySelector(`[data-count-for="${CSS.escape(box.value)}"]`).textContent = count;
      });
    };

    boxes.forEach((box) => box.addEventListener('change', render));
    host.querySelector('[data-home-finder-clear]').addEventListener('click', () => {
      boxes.forEach((box) => { box.checked = false; });
      render();
    });
    render();
  }).catch((error) => {
    host.innerHTML = `<p class="comparison-status">The compact Glasses Finder could not load: ${esc(error.message)}</p>`;
  });
})();
