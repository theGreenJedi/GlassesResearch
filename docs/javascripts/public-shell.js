(() => {
  const activate = (event) => {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    const control = event.target.closest('.gr-search-button, .gr-menu-button');
    if (!control) return;
    event.preventDefault();
    control.click();
  };
  document.addEventListener('keydown', activate);
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
      path.includes("/report_card")
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
