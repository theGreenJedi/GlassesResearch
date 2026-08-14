(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const dataUrl = '../../data/purchase-fallbacks.json';
  let fallbacks = new Map();

  const idFrom = (node) => (node?.textContent.match(/GLS-\d{4}/) || [])[0] || '';

  const addFallback = (container, id) => {
    const fallback = fallbacks.get(id);
    if (!fallback?.url || !container) return;
    if ([...container.querySelectorAll('a[href]')].some((a) => /ebay\./i.test(a.href))) return;

    if (container.classList.contains('purchase-unknown')) {
      container.classList.remove('purchase-unknown');
      container.innerHTML = '<strong>Buy / find one:</strong> ';
    }
    const link = document.createElement('a');
    link.className = 'purchase-link purchase-link-generated';
    link.href = fallback.url;
    link.target = '_blank';
    link.rel = 'noopener';
    link.textContent = 'eBay exact-model search · used';
    link.title = 'Generated secondary-market search fallback; verify the exact model before purchase.';
    container.appendChild(link);
  };

  const decorate = () => {
    if (!fallbacks.size) return;
    host.querySelectorAll('.discovery-card').forEach((card) => {
      const id = idFrom(card.querySelector('.discovery-meta'));
      addFallback(card.querySelector('.purchase-sources'), id);
    });
    host.querySelectorAll('.comparison-selected-device').forEach((card) => {
      const id = idFrom(card.querySelector('strong'));
      let container = card.querySelector('.purchase-sources');
      if (!container && fallbacks.get(id)?.url) {
        container = document.createElement('div');
        container.className = 'purchase-sources';
        container.innerHTML = '<strong>Buy / find:</strong> ';
        card.appendChild(container);
      }
      addFallback(container, id);
    });
  };

  fetch(dataUrl, { cache: 'no-store' })
    .then((r) => r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`)))
    .then((data) => {
      fallbacks = new Map((data.records || []).filter((r) => r.fallback).map((r) => [r.id, r.fallback]));
      decorate();
      let timer;
      const observer = new MutationObserver(() => {
        clearTimeout(timer);
        timer = setTimeout(decorate, 45);
      });
      observer.observe(host, { childList: true, subtree: true });
    })
    .catch(() => {});
})();
