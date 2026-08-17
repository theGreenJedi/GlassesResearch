(() => {
  const ready = (fn) => document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn) : fn();

  function modelIcon() {
    if (!/\/models\/catalog\//.test(location.pathname)) return;
    const article = document.querySelector('.md-content__inner');
    const h1 = article?.querySelector('h1');
    if (!article || !h1 || article.querySelector('.gr-model-mark')) return;
    let type = 'smart-glasses';
    article.querySelectorAll('table tr').forEach((row) => {
      const cells = row.querySelectorAll('th,td');
      if (cells.length >= 2 && /Device type/i.test(cells[0].textContent || '')) type = (cells[1].textContent || '').trim().toLowerCase();
    });
    const mark = document.createElement('div');
    mark.className = 'gr-model-mark';
    mark.setAttribute('aria-hidden', 'true');
    mark.dataset.kind = /display|ar|hud|spatial/.test(type) ? 'display' : /audio/.test(type) ? 'audio' : /camera|ai/.test(type) ? 'camera' : 'generic';
    mark.innerHTML = '<span class="gr-lens gr-left"></span><span class="gr-lens gr-right"></span><span class="gr-bridge"></span><span class="gr-temple gr-tl"></span><span class="gr-temple gr-tr"></span><span class="gr-feature"></span>';
    h1.insertAdjacentElement('afterend', mark);
  }

  function lineageChains() {
    if (!/\/lineages\//.test(location.pathname)) return;
    document.querySelectorAll('.md-content__inner h2').forEach((heading) => {
      if (!/Canonical model pages/i.test(heading.textContent || '')) return;
      const block = heading.nextElementSibling;
      if (!block || block.classList.contains('gr-lineage-chain')) return;
      const links = [...block.querySelectorAll('a[href*="/models/catalog/"]')];
      if (links.length < 2) return;
      const chain = document.createElement('div');
      chain.className = 'gr-lineage-chain';
      chain.setAttribute('aria-label', 'Canonical model lineage');
      links.forEach((link, i) => {
        const node = document.createElement('a');
        node.className = 'gr-lineage-node';
        node.href = link.href;
        node.textContent = link.textContent.trim();
        chain.appendChild(node);
        if (i < links.length - 1) {
          const edge = document.createElement('span');
          edge.className = 'gr-lineage-edge';
          edge.setAttribute('aria-hidden', 'true');
          edge.textContent = '→';
          chain.appendChild(edge);
        }
      });
      block.insertAdjacentElement('afterend', chain);
    });
  }

  ready(() => { modelIcon(); lineageChains(); });
  document.addEventListener('navigation:complete', () => { modelIcon(); lineageChains(); });
})();
