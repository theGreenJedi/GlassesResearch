(() => {
  const buildUnifiedRail = () => {
    const primary = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
    const secondary = document.querySelector('.md-sidebar--secondary');
    if (!primary) return;

    primary.querySelectorAll('[data-gr-left-rail-extra]').forEach((node) => node.remove());

    const extra = document.createElement('div');
    extra.className = 'gr-left-rail-extra';
    extra.dataset.grLeftRailExtra = 'true';

    /* Put the real Material search control in the left rail rather than
       leaving a second search surface floating at the far right of the header. */
    const search = document.querySelector('.md-header .md-search');
    if (search) {
      search.classList.add('gr-left-rail-search');
      extra.appendChild(search);
    }

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

    /* Do not merely hide the old rail: remove it from the page layout so
       Material cannot continue reserving a phantom right-hand column. */
    secondary?.remove();
    document.documentElement.classList.add('gr-one-rail-ready');
  };

  document.addEventListener('DOMContentLoaded', buildUnifiedRail);
  if (window.document$?.subscribe) window.document$.subscribe(buildUnifiedRail);
})();
