(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const selected = new Set();
  const modelIdForCard = (card) => (card.querySelector('.discovery-meta')?.textContent.match(/GLS-\d{4}/) || [])[0] || '';

  const ensureToolbar = () => {
    const panel = host.querySelector('.glasses-finder');
    if (!panel || panel.querySelector('.finder-shortlist-toolbar')) return;
    const anchor = panel.querySelector('.discovery-actions');
    if (!anchor) return;
    const toolbar = document.createElement('div');
    toolbar.className = 'finder-shortlist-toolbar';
    toolbar.innerHTML = '<strong>Shortlist:</strong> <span data-shortlist-count>0 selected</span> <button type="button" data-compare-selected disabled>Compare selected</button> <button type="button" data-clear-shortlist disabled>Clear shortlist</button>';
    anchor.insertAdjacentElement('afterend', toolbar);
    toolbar.querySelector('[data-compare-selected]').addEventListener('click', compareSelected);
    toolbar.querySelector('[data-clear-shortlist]').addEventListener('click', () => {
      selected.clear();
      decorate();
    });
    updateToolbar();
  };

  const updateToolbar = () => {
    const toolbar = host.querySelector('.finder-shortlist-toolbar');
    if (!toolbar) return;
    const count = selected.size;
    toolbar.querySelector('[data-shortlist-count]').textContent = `${count} selected${count >= 4 ? ' · maximum 4' : ''}`;
    toolbar.querySelector('[data-compare-selected]').disabled = count < 2;
    toolbar.querySelector('[data-clear-shortlist]').disabled = count === 0;
  };

  const compareSelected = () => {
    const ids = [...selected].slice(0, 4);
    if (ids.length < 2) return;
    const selects = [...host.querySelectorAll('.comparison-controls select[data-slot]')];
    selects.forEach((select, index) => {
      const next = ids[index] || '';
      if (index < 2 && !next) return;
      select.value = next;
    });
    selects[0]?.dispatchEvent(new Event('change', { bubbles: true }));
    host.querySelector('.compare-panel')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const decorateCard = (card) => {
    const id = modelIdForCard(card);
    if (!id) return;
    const actions = card.querySelector('.discovery-card-actions');
    if (!actions) return;
    let control = actions.querySelector('[data-shortlist-id]');
    if (!control) {
      const label = document.createElement('label');
      label.className = 'finder-shortlist-choice';
      label.innerHTML = `<input type="checkbox" data-shortlist-id="${id}"> Shortlist`;
      actions.prepend(label);
      control = label.querySelector('input');
      control.addEventListener('change', () => {
        if (control.checked) {
          if (selected.size >= 4 && !selected.has(id)) {
            control.checked = false;
            return;
          }
          selected.add(id);
        } else {
          selected.delete(id);
        }
        decorate();
      });
    }
    control.checked = selected.has(id);
    control.disabled = !selected.has(id) && selected.size >= 4;
    card.classList.toggle('shortlisted', selected.has(id));
  };

  const decorate = () => {
    ensureToolbar();
    host.querySelectorAll('.discovery-card').forEach(decorateCard);
    updateToolbar();
  };

  let timer;
  const observer = new MutationObserver(() => {
    clearTimeout(timer);
    timer = setTimeout(decorate, 40);
  });
  observer.observe(host, { childList: true, subtree: true });
  decorate();
})();
