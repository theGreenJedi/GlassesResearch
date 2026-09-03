(() => {
  const buildUnifiedRail = () => {
    const primary = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
    const secondary = document.querySelector('.md-sidebar--secondary .md-sidebar__inner');
    if (!primary || !secondary) return;

    primary.querySelectorAll('[data-gr-left-rail-extra]').forEach((node) => node.remove());

    const extra = document.createElement('div');
    extra.className = 'gr-left-rail-extra';
    extra.dataset.grLeftRailExtra = 'true';

    const searchButton = document.createElement('button');
    searchButton.type = 'button';
    searchButton.className = 'gr-left-rail-search';
    searchButton.setAttribute('aria-label', 'Search GlassesResearch');
    searchButton.innerHTML = '<span aria-hidden="true">⌕</span><span>Search</span>';
    searchButton.addEventListener('click', () => {
      const searchToggle = document.querySelector('label[for="__search"]');
      const searchInput = document.querySelector('.md-search__input');
      if (searchToggle) searchToggle.click();
      window.setTimeout(() => searchInput?.focus(), 0);
    });
    extra.appendChild(searchButton);

    const tocNav = secondary.querySelector('nav.md-nav--secondary');
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
  };

  document.addEventListener('DOMContentLoaded', buildUnifiedRail);
  if (window.document$?.subscribe) window.document$.subscribe(buildUnifiedRail);
})();
