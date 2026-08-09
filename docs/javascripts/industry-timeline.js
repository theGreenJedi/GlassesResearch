(() => {
  const root = document.getElementById('industry-timeline-app');
  if (!root) return;

  const categoryLabels = {
    product: 'Products', company: 'Companies', technology: 'Technology',
    'open-source': 'Open source', regulatory: 'Regulatory', industry: 'Industry',
    research: 'Research', glassesresearch: 'GlassesResearch'
  };
  const categoryOrder = Object.keys(categoryLabels);

  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const parse = value => new Date(`${value}T00:00:00Z`);
  const now = new Date();
  let canonical = [];
  let provisional = [];
  let selectedCategories = new Set(categoryOrder);
  let minSignificance = 4;
  let showSignals = true;

  root.innerHTML = `
    <div class="timeline-controls" aria-label="Timeline filters">
      <div class="timeline-category-filters"></div>
      <label>Importance
        <select id="timeline-significance">
          <option value="5">Major industry milestones</option>
          <option value="4" selected>Major and notable events</option>
          <option value="3">Include additional events</option>
          <option value="2">Include minor events</option>
          <option value="1">Show all events</option>
        </select>
      </label>
      <label class="timeline-signal-toggle"><input type="checkbox" id="timeline-signals" checked> Include recent announcements</label>
    </div>
    <div class="timeline-status" aria-live="polite">Loading timeline data…</div>
    <div class="timeline-chart-wrap"><svg class="timeline-chart" role="img" aria-label="Smart-glasses industry timeline"></svg></div>
    <div class="timeline-detail" aria-live="polite"></div>
    <div class="timeline-list"></div>`;

  const controls = root.querySelector('.timeline-category-filters');
  categoryOrder.forEach(category => {
    const label = document.createElement('label');
    label.className = 'timeline-chip';
    label.innerHTML = `<input type="checkbox" value="${category}" checked> ${categoryLabels[category]}`;
    label.querySelector('input').addEventListener('change', event => {
      if (event.target.checked) selectedCategories.add(category); else selectedCategories.delete(category);
      render();
    });
    controls.appendChild(label);
  });

  root.querySelector('#timeline-significance').addEventListener('change', event => {
    minSignificance = Number(event.target.value); render();
  });
  root.querySelector('#timeline-signals').addEventListener('change', event => {
    showSignals = event.target.checked; render();
  });

  function allEvents() {
    const pool = canonical.concat(showSignals ? provisional : []);
    return pool.filter(event => selectedCategories.has(event.category) && event.significance >= minSignificance)
      .sort((a,b) => a.date.localeCompare(b.date));
  }

  function eventClass(event) {
    return `timeline-event state-${event.state} significance-${event.significance}`;
  }

  function publicSummary(event) {
    const summary = String(event.summary || '');
    if (event.state === 'provisional' && /^Automatically discovered primary-source signal\./i.test(summary)) return '';
    return summary;
  }

  function showDetail(event) {
    const detail = root.querySelector('.timeline-detail');
    const sources = (event.sources || []).map((url, i) => `<a href="${esc(url)}" rel="noopener">Source${event.sources.length > 1 ? ` ${i+1}` : ''}</a>`).join(' · ');
    const summary = publicSummary(event);
    detail.innerHTML = `<article id="${esc(event.id)}" class="timeline-detail-card">
      <div class="timeline-detail-meta"><span>${esc(event.date)}</span><span>${esc(categoryLabels[event.category] || event.category)}</span></div>
      <h3>${esc(event.title)}</h3>${summary ? `<p>${esc(summary)}</p>` : ''}${sources ? `<p>${sources}</p>` : ''}
    </article>`;
    history.replaceState(null, '', `#${event.id}`);
  }

  function renderChart(events) {
    const svg = root.querySelector('.timeline-chart');
    svg.innerHTML = '';
    if (!events.length) return;
    const width = 1200, left = 130, right = 30, top = 40, lane = 54;
    const categories = categoryOrder.filter(cat => events.some(e => e.category === cat));
    const height = top + categories.length * lane + 58;
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);

    const dates = events.map(e => parse(e.date).getTime());
    const minDate = Math.min(...dates);
    const maxDate = Math.max(...dates, now.getTime());
    const pad = Math.max((maxDate - minDate) * 0.04, 86400000 * 120);
    const domainMin = minDate - pad, domainMax = maxDate + pad;
    const x = time => left + ((time - domainMin) / (domainMax - domainMin)) * (width-left-right);

    const ns = 'http://www.w3.org/2000/svg';
    const make = (tag, attrs, text) => {
      const node = document.createElementNS(ns, tag);
      Object.entries(attrs || {}).forEach(([k,v]) => node.setAttribute(k, v));
      if (text) node.textContent = text;
      svg.appendChild(node); return node;
    };

    categories.forEach((category, idx) => {
      const y = top + idx * lane + lane/2;
      make('line', {x1:left, x2:width-right, y1:y, y2:y, class:'timeline-lane'});
      make('text', {x:8, y:y+5, class:'timeline-lane-label'}, categoryLabels[category]);
    });

    const todayX = x(now.getTime());
    make('line', {x1:todayX, x2:todayX, y1:18, y2:height-24, class:'timeline-today'});
    make('text', {x:todayX+6, y:24, class:'timeline-today-label'}, 'TODAY');

    const years = new Set(events.map(e => Number(e.date.slice(0,4))));
    years.add(now.getUTCFullYear());
    [...years].sort().forEach(year => {
      const tx = x(Date.UTC(year,0,1));
      make('text', {x:tx, y:height-7, class:'timeline-year'}, String(year));
    });

    events.forEach(event => {
      const y = top + categories.indexOf(event.category) * lane + lane/2;
      const cx = x(parse(event.date).getTime());
      const radius = 4 + event.significance * 2.2;
      const circle = make('circle', {cx, cy:y, r:radius, class:eventClass(event), 'data-id':event.id});
      circle.setAttribute('tabindex', '0');
      circle.setAttribute('role', 'button');
      circle.setAttribute('aria-label', `${event.date}: ${event.title}`);
      const activate = () => showDetail(event);
      circle.addEventListener('click', activate);
      circle.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); } });
      const title = document.createElementNS(ns, 'title'); title.textContent = `${event.date} — ${event.title}`; circle.appendChild(title);
    });
  }

  function renderList(events) {
    const list = root.querySelector('.timeline-list');
    list.innerHTML = events.slice().reverse().map(event => {
      const summary = publicSummary(event);
      return `<article class="timeline-list-item ${eventClass(event)}" id="list-${esc(event.id)}">
        <div class="timeline-list-date">${esc(event.date)}</div>
        <div><h3><a href="#${esc(event.id)}" data-event-id="${esc(event.id)}">${esc(event.title)}</a></h3>
        ${summary ? `<p>${esc(summary)}</p>` : ''}<div class="timeline-list-meta">${esc(categoryLabels[event.category])}</div></div>
      </article>`;
    }).join('');
    list.querySelectorAll('[data-event-id]').forEach(link => link.addEventListener('click', e => {
      const event = canonical.concat(provisional).find(item => item.id === e.currentTarget.dataset.eventId);
      if (event) { e.preventDefault(); showDetail(event); }
    }));
  }

  function render() {
    const events = allEvents();
    root.querySelector('.timeline-status').textContent = `${events.length} events shown`;
    renderChart(events); renderList(events);
    const requested = location.hash.slice(1);
    if (requested) {
      const event = canonical.concat(provisional).find(item => item.id === requested);
      if (event) showDetail(event);
    }
  }

  Promise.all([
    fetch('/timeline/events.json').then(r => { if (!r.ok) throw new Error('timeline unavailable'); return r.json(); }),
    fetch('/timeline/auto-events.json').then(r => r.ok ? r.json() : {events:[]}).catch(() => ({events:[]}))
  ]).then(([canon, auto]) => {
    canonical = canon.events || []; provisional = auto.events || []; render();
  }).catch(error => {
    root.querySelector('.timeline-status').textContent = `Timeline data could not be loaded: ${error.message}`;
  });
})();
