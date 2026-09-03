(() => {
  const buildUnifiedRail = () => {
    const primary = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
    const secondary = document.querySelector('.md-sidebar--secondary');
    if (!primary) return;

    primary.querySelectorAll('[data-gr-left-rail-extra]').forEach((node) => node.remove());

    const extra = document.createElement('div');
    extra.className = 'gr-left-rail-extra';
    extra.dataset.grLeftRailExtra = 'true';

    /* Keep Material's real search machinery in its native header position,
       but give it a permanent, visible launcher in the left rail. Moving the
       component itself breaks Material's positioning assumptions. */
    const searchLauncher = document.createElement('button');
    searchLauncher.type = 'button';
    searchLauncher.className = 'gr-left-rail-search-launcher';
    searchLauncher.setAttribute('aria-label', 'Search GlassesResearch');
    searchLauncher.innerHTML = '<span class="gr-left-rail-search-icon" aria-hidden="true">⌕</span><span class="gr-left-rail-search-text">Search GlassesResearch…</span>';
    searchLauncher.addEventListener('click', () => {
      const searchToggle = document.querySelector('label[for="__search"]');
      const searchInput = document.querySelector('.md-search__input');
      searchToggle?.click();
      window.setTimeout(() => searchInput?.focus(), 0);
    });
    extra.appendChild(searchLauncher);

    /* Preserve useful page-local navigation before removing the secondary rail. */
    const tocNav = secondary?.querySelector('nav.md-nav--secondary');
    const tocList = tocNav?.querySelector(':scope > .md-nav__list');
    if (tocList && tocList.children.length) {
      const about = document.createElement('section');
      about.className = 'gr-left-rail-about';
      about.setAttribute('aria-label', 'About this page');

      const heading = document.createElement('div');
      heading.className = 'gr-left-rail-about__title';
      heading.textContent = 'ABOUT';
      about.appendChild(heading);

      const clonedList = tocList.cloneNode(true);
      clonedList.classList.add('gr-left-rail-about__list');
      about.appendChild(clonedList);
      extra.appendChild(about);
    }

    primary.appendChild(extra);

    /* Remove the old right rail after its useful links have been preserved. */
    secondary?.remove();
    document.documentElement.classList.add('gr-one-rail-ready');
  };

  document.addEventListener('DOMContentLoaded', buildUnifiedRail);
  if (window.document$?.subscribe) window.document$.subscribe(buildUnifiedRail);
})();
