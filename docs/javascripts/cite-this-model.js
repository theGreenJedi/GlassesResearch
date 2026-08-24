(() => {
  "use strict";

  function citationPanel() {
    const bib = document.querySelector('a[href*="/data/citations/gls-"][href$=".bib"]');
    if (!bib) return;

    const container = bib.parentElement;
    if (!container || container.dataset.glassesresearchCitationUi === "1") return;

    const match = bib.getAttribute("href")?.match(/(gls-\d{4})\.bib$/i);
    if (!match) return;

    const modelId = match[1].toUpperCase();
    const heading = document.querySelector("main h1, article h1, .md-content h1");
    const title = (heading?.textContent || modelId).trim();
    const canonicalUrl = `${window.location.origin}/models/catalog/${modelId.toLowerCase()}/`;
    const citation = `GlassesResearch. ${title}. ${canonicalUrl}`;

    const csl = container.querySelector('a[href*="/data/citations/gls-"][href$=".json"]');
    const embed = Array.from(container.querySelectorAll("a")).find((link) =>
      /embeddable model card/i.test(link.textContent || "")
    );

    const panel = document.createElement("details");
    panel.className = "gr-cite-model";
    panel.open = false;

    const summary = document.createElement("summary");
    summary.textContent = "Cite this model";

    const text = document.createElement("p");
    text.className = "gr-cite-model__text";
    const code = document.createElement("code");
    code.dataset.grCitation = "";
    code.textContent = citation;
    text.appendChild(code);

    const actions = document.createElement("p");
    actions.className = "gr-cite-model__actions";

    const copy = document.createElement("button");
    copy.type = "button";
    copy.className = "md-button md-button--primary";
    copy.dataset.grCopyCitation = "";
    copy.textContent = "Copy citation";
    actions.appendChild(copy);

    [bib, csl, embed].filter(Boolean).forEach((link) => {
      actions.appendChild(document.createTextNode(" · "));
      const clone = link.cloneNode(true);
      clone.classList.add("md-button");
      actions.appendChild(clone);
    });

    panel.append(summary, text, actions);
    container.dataset.glassesresearchCitationUi = "1";
    container.replaceWith(panel);
  }

  async function copyCitation(button) {
    const panel = button.closest(".gr-cite-model");
    const citation = panel?.querySelector("[data-gr-citation]")?.textContent?.trim();
    if (!citation) return;

    const original = button.textContent;
    try {
      await navigator.clipboard.writeText(citation);
    } catch (_) {
      const helper = document.createElement("textarea");
      helper.value = citation;
      helper.setAttribute("readonly", "");
      helper.style.position = "fixed";
      helper.style.opacity = "0";
      document.body.appendChild(helper);
      helper.select();
      document.execCommand("copy");
      helper.remove();
    }

    button.textContent = "Copied";
    window.setTimeout(() => {
      button.textContent = original;
    }, 1600);
  }

  document.addEventListener("click", (event) => {
    const button = event.target.closest?.("[data-gr-copy-citation]");
    if (button) copyCitation(button);
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", citationPanel, { once: true });
  } else {
    citationPanel();
  }
})();
