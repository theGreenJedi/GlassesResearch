document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".md-search__input");
  if (input) {
    input.setAttribute("placeholder", "Search GlassesResearch…");
    input.setAttribute("aria-label", "Search GlassesResearch");
  }
});
