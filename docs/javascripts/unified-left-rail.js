(() => {
  const buildUnifiedRail = () => {
    const primary = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
    const secondary = document.querySelector('.md-sidebar--secondary');
    if (!primary) return;

    primary.querySelectorAll('[data-gr-left-rail-search]').forEach((node) => node.remove());
    primary.querySelectorAll('[data-gr-left-rail-about]').forEach((node) => node.remove());

    /* Make the visible GlassesResearch title in the primary rail a reliable
       home link without disturbing Material's drawer/title structure. */
    const navTitle = primary.querySelector('.md-nav--primary > .md-nav__title, .md-nav__title');
    if (navTitle && !navTitle.querySelector('[data-gr-home-link]')) {
      const textNodes = Array.from(navTitle.childNodes).filter(
        (node) => node.nodeType === Node.TEXT_NODE && node.textContent.trim() === 'GlassesResearch'
      );
      if (textNodes.length) {
        const homeLink = document.createElement('a');
        homeLink.href = '/';
        homeLink.className = 'gr-left-rail-home-link';
        homeLink.dataset.grHomeLink = 'true';
        homeLink.textContent = 'GlassesResearch';
        textNodes[0].replaceWith(homeLink);
      } else if (navTitle.textContent.trim() === 'GlassesResearch') {
        navTitle.textContent = '';
        const homeLink = document.createElement('a');
        homeLink.href = '/';
        homeLink.className = 'gr-left-rail-home-link';
        homeLink.dataset.grHomeLink = 'true';
        homeLink.textContent = 'GlassesResearch';
        navTitle.appendChild(homeLink);
      }
    }

    /* Keep the search entrance at the top of the visible left rail so it can
       never be pushed below long navigation or page-local section lists. */
    const searchLauncher = document.createElement('button');
    searchLauncher.type = 'button';
    searchLauncher.className = 'gr-left-rail-search-launcher';
    searchLauncher.dataset.grLeftRailSearch = 'true';
    searchLauncher.setAttribute('aria-label', 'Search GlassesResearch');
    searchLauncher.innerHTML = '<span class="gr-left-rail-search-icon" aria-hidden="true">⌕</span><span class="gr-left-rail-search-text">Search GlassesResearch…</span>';
    searchLauncher.addEventListener('click', () => {
      const searchToggle = document.querySelector('label[for="__search"]');
      const searchInput = document.querySelector('.md-search__input');
      searchToggle?.click();
      window.setTimeout(() => searchInput?.focus(), 0);
    });
    primary.prepend(searchLauncher);

    /* Preserve useful page-local navigation before removing the secondary rail. */
    const tocNav = secondary?.querySelector('nav.md-nav--secondary');
    const tocList = tocNav?.querySelector(':scope > .md-nav__list');
    if (tocList && tocList.children.length) {
      const about = document.createElement('section');
      about.className = 'gr-left-rail-about';
      about.dataset.grLeftRailAbout = 'true';
      about.setAttribute('aria-label', 'About this page');

      const heading = document.createElement('div');
      heading.className = 'gr-left-rail-about__title';
      heading.textContent = 'ABOUT';
      about.appendChild(heading);

      const clonedList = tocList.cloneNode(true);
      clonedList.classList.add('gr-left-rail-about__list');
      about.appendChild(clonedList);
      primary.appendChild(about);
    }

    /* Remove the old right rail after its useful links have been preserved. */
    secondary?.remove();
    document.documentElement.classList.add('gr-one-rail-ready');
  };

  document.addEventListener('DOMContentLoaded', buildUnifiedRail);
  if (window.document$?.subscribe) window.document$.subscribe(buildUnifiedRail);
})();
