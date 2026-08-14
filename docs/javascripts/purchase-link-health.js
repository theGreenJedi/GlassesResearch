(() => {
  const escAttr = (value) => String(value ?? '').replaceAll('"', '&quot;');
  const healthUrl = '../../data/purchase-link-health.json';

  const normalize = (url) => {
    try {
      const u = new URL(url, location.href);
      u.hash = '';
      return u.href.replace(/\/$/, '');
    } catch {
      return String(url || '').replace(/\/$/, '');
    }
  };

  const ageLabel = (iso) => {
    if (!iso) return '';
    const checked = new Date(iso);
    if (Number.isNaN(checked.getTime())) return '';
    const days = Math.max(0, Math.floor((Date.now() - checked.getTime()) / 86400000));
    if (days === 0) return 'checked today';
    if (days === 1) return 'checked 1 day ago';
    return `checked ${days} days ago`;
  };

  const statusLabel = (record) => {
    const age = ageLabel(record.checked_at);
    const base = {
      reachable: 'verified reachable',
      redirected: 'redirected — review exact model',
      blocked_or_rate_limited: 'retailer blocks automated checks',
      temporary_failure: 'temporary check failure',
      unreachable: 'currently unreachable',
      unknown: 'status unknown',
      dead: 'dead link',
    }[record.status] || record.status || 'status unknown';
    return age ? `${base}; ${age}` : base;
  };

  const decorate = (health) => {
    const byUrl = new Map((health.records || []).map((r) => [normalize(r.url), r]));
    const deadStates = new Set(['dead']);
    document.querySelectorAll('a.purchase-link[href]').forEach((link) => {
      const record = byUrl.get(normalize(link.href));
      if (!record) {
        link.dataset.health = 'unverified';
        link.title = link.title || 'Purchase route has not yet been checked by the automated health monitor.';
        return;
      }
      link.dataset.health = record.status;
      link.dataset.checkedAt = record.checked_at || '';
      link.title = statusLabel(record);
      link.setAttribute('aria-label', `${link.textContent.trim()} — ${statusLabel(record)}`);
      if (deadStates.has(record.status)) {
        link.hidden = true;
        link.dataset.suppressed = 'dead';
      }
    });

    document.querySelectorAll('.purchase-sources').forEach((group) => {
      const visible = [...group.querySelectorAll('a.purchase-link')].filter((a) => !a.hidden);
      const suppressed = [...group.querySelectorAll('a.purchase-link[data-suppressed="dead"]')];
      let note = group.querySelector('.purchase-health-note');
      if (!note) {
        note = document.createElement('small');
        note.className = 'purchase-health-note';
        group.appendChild(note);
      }
      if (suppressed.length && !visible.length) {
        note.textContent = ' Listed purchase routes are currently dead; replacement search is queued.';
      } else if (suppressed.length) {
        note.textContent = ` ${suppressed.length} dead route${suppressed.length === 1 ? '' : 's'} suppressed; replacement queued.`;
      } else {
        note.textContent = '';
      }
    });
  };

  const run = () => fetch(healthUrl, { cache: 'no-store' })
    .then((r) => r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`)))
    .then(decorate)
    .catch(() => {});

  run();

  const host = document.getElementById('comparison-engine-app');
  if (host && 'MutationObserver' in window) {
    let timer;
    const observer = new MutationObserver(() => {
      clearTimeout(timer);
      timer = setTimeout(run, 60);
    });
    observer.observe(host, { childList: true, subtree: true });
  }
})();
