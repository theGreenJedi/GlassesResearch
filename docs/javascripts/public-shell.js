(() => {
  const searchControl = () => document.querySelector('.gr-search-button');
  const menuControl = () => document.querySelector('.gr-menu-button');
  const searchToggle = () => document.getElementById('__search');
  const drawerToggle = () => document.getElementById('__drawer');

  const setChecked = (toggle, checked) => {
    if (!toggle || toggle.checked === checked) return;
    toggle.checked = checked;
    toggle.dispatchEvent(new Event('change', { bubbles: true }));
  };

  const syncSearch = () => {
    const open = Boolean(searchToggle()?.checked);
    document.documentElement.classList.toggle('gr-search-open', open);
    searchControl()?.setAttribute('aria-expanded', String(open));
    if (open) {
      window.requestAnimationFrame(() => {
        document.querySelector('.md-search__input')?.focus();
      });
    }
  };

  const syncMenu = () => {
    const open = Boolean(drawerToggle()?.checked);
    document.documentElement.classList.toggle('gr-menu-open', open);
    menuControl()?.setAttribute('aria-expanded', String(open));
  };

  const bindControls = () => {
    const search = searchControl();
    const menu = menuControl();
    const searchState = searchToggle();
    const drawerState = drawerToggle();

    if (search && !search.dataset.grBound) {
      search.dataset.grBound = 'true';
      search.addEventListener('click', () => setChecked(searchState, true));
    }
    if (menu && !menu.dataset.grBound) {
      menu.dataset.grBound = 'true';
      menu.addEventListener('click', () => setChecked(drawerState, !drawerState?.checked));
    }
    if (searchState && !searchState.dataset.grBound) {
      searchState.dataset.grBound = 'true';
      searchState.addEventListener('change', syncSearch);
    }
    if (drawerState && !drawerState.dataset.grBound) {
      drawerState.dataset.grBound = 'true';
      drawerState.addEventListener('change', syncMenu);
    }

    syncSearch();
    syncMenu();
  };

  document.addEventListener('DOMContentLoaded', bindControls);
  if (window.document$?.subscribe) window.document$.subscribe(bindControls);

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    if (searchToggle()?.checked) setChecked(searchToggle(), false);
  });
})();

/* Visual department routing only. Public URLs remain authoritative; this assigns presentation tokens. */
(() => {
  const applyDepartment = () => {
    if (!document.body) return;
    const path = window.location.pathname.toLowerCase().replace(/\/+$/, "") || "/";

    let department = "home";
    if (
      path.includes("/comparison_engine") ||
      path.startsWith("/guides") ||
      path.startsWith("/buyers")
    ) {
      department = "finder";
    } else if (
      path.startsWith("/models") ||
      path.startsWith("/docs/report-cards") ||
      path.includes("/report_card") ||
      path.includes("/report-card")
    ) {
      department = "models";
    } else if (
      path.startsWith("/docs/research_news") ||
      path.startsWith("/docs/news") ||
      path.startsWith("/changes") ||
      path.startsWith("/community-research") ||
      path.startsWith("/docs/feeds") ||
      path.startsWith("/docs/events")
    ) {
      department = "research";
    } else if (
      path.startsWith("/hacking") ||
      path.startsWith("/resources") ||
      path.startsWith("/dataset") ||
      path.startsWith("/docs/tools")
    ) {
      department = "develop";
    } else if (
      path.startsWith("/docs/about") ||
      path.startsWith("/docs/privacy") ||
      path.startsWith("/docs/research_standards") ||
      path.startsWith("/docs/evidence_standard") ||
      path.startsWith("/docs/report_card_method") ||
      path.startsWith("/docs/repository_laws") ||
      path.startsWith("/docs/investigation_workflow") ||
      path.startsWith("/preservation") ||
      path.startsWith("/timeline") ||
      path.startsWith("/glossary") ||
      path === "/why" ||
      path === "/founding_charter"
    ) {
      department = "about";
    } else if (path !== "/") {
      department = "about";
    }

    document.body.dataset.grDepartment = department;
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyDepartment, { once: true });
  } else {
    applyDepartment();
  }
})();
