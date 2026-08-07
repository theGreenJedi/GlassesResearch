// Make models/THE_LIST.md a useful interactive research hub on the rendered site.
// The Markdown remains the canonical evidence ledger; this layer adds navigation
// and client-side filtering without changing the underlying research record.

function enhanceTheList() {
  const article = document.querySelector("article.md-content__inner");
  if (!article) return;

  const heading = article.querySelector("h1");
  if (!heading || !heading.textContent.includes("The List")) return;

  const tables = Array.from(article.querySelectorAll("table")).filter((table) => {
    const headers = Array.from(table.querySelectorAll("thead th")).map((cell) =>
      cell.textContent.trim().toLowerCase()
    );
    return headers.includes("model") && headers.includes("maker");
  });
  if (!tables.length) return;

  // Prefer a repository model chapter when one exists; otherwise use the row's
  // canonical external source. This leaves the evidence/source column intact.
  tables.forEach((table) => {
    const headers = Array.from(table.querySelectorAll("thead th")).map((cell) =>
      cell.textContent.trim().toLowerCase()
    );
    const modelIndex = headers.indexOf("model");
    const evidenceIndex = headers.indexOf("evidence / links");
    if (modelIndex < 0 || evidenceIndex < 0) return;

    table.querySelectorAll("tbody tr").forEach((row) => {
      const cells = row.querySelectorAll("td");
      const modelCell = cells[modelIndex];
      const evidenceCell = cells[evidenceIndex];
      if (!modelCell || !evidenceCell || modelCell.querySelector("a")) return;

      const links = Array.from(evidenceCell.querySelectorAll("a[href]"));
      if (!links.length) return;
      const chapterLink = links.find((link) =>
        /\/models\/[A-Za-z0-9._-]+\/(?:README\.md)?(?:$|[#?])/.test(link.getAttribute("href") || "")
      );
      const namedSource = links.find(
        (link) => link.textContent.trim().toLowerCase() === "source"
      );
      const externalLink = links.find((link) => /^https?:\/\//.test(link.href));
      const destination = chapterLink || namedSource || externalLink || links[0];
      if (!destination) return;

      const anchor = document.createElement("a");
      anchor.href = destination.href;
      anchor.textContent = modelCell.textContent.trim();
      anchor.className = "model-index-link";
      anchor.title = chapterLink
        ? "Open the GlassesResearch model chapter"
        : "Open the best available model source";
      if (!chapterLink && /^https?:\/\//.test(destination.href)) {
        anchor.target = "_blank";
        anchor.rel = "noopener noreferrer";
      }
      modelCell.replaceChildren(anchor);
    });
  });

  if (article.querySelector(".model-hub-controls")) return;

  const rows = tables.flatMap((table) => Array.from(table.querySelectorAll("tbody tr")));
  const read = (row, field) => {
    const headers = Array.from(row.closest("table").querySelectorAll("thead th")).map((cell) =>
      cell.textContent.trim().toLowerCase()
    );
    const index = headers.indexOf(field);
    const cells = row.querySelectorAll("td");
    return index >= 0 && cells[index] ? cells[index].textContent.trim() : "";
  };

  const unique = (field) => Array.from(new Set(rows.map((row) => read(row, field)).filter(Boolean))).sort();
  const makers = unique("maker");
  const states = unique("state");
  const types = unique("type");
  const evidence = unique("evidence / links");

  const controls = document.createElement("section");
  controls.className = "model-hub-controls";
  controls.innerHTML = `
    <h2>Explore the smart-glasses ecosystem</h2>
    <p><strong>The List is the central index for GlassesResearch.</strong> Search the catalog, narrow it by maker, status, or device type, then follow each model into its chapter or strongest available source.</p>
    <div class="model-hub-links">
      <a href="../buyers/BUYER_AND_OPENNESS_GUIDE.md">Buyer & openness guide</a> ·
      <a href="../hacking/README.md">Hacking & open development</a> ·
      <a href="../docs/news/README.md">Research & news</a> ·
      <a href="../docs/faq/COMMUNITY_QUESTIONS.md">Community questions</a> ·
      <a href="../glossary/README.md">Glossary</a>
    </div>
    <div class="model-filter-grid">
      <label>Search <input type="search" data-model-filter="search" placeholder="Model, maker, ID, feature…" /></label>
      <label>Maker <select data-model-filter="maker"><option value="">All makers</option>${makers.map((v) => `<option>${v}</option>`).join("")}</select></label>
      <label>Status <select data-model-filter="state"><option value="">All states</option>${states.map((v) => `<option>${v}</option>`).join("")}</select></label>
      <label>Type <select data-model-filter="type"><option value="">All types</option>${types.map((v) => `<option>${v}</option>`).join("")}</select></label>
      <button type="button" data-model-filter="reset">Reset</button>
    </div>
    <p class="model-result-count" aria-live="polite"></p>
    <details>
      <summary><strong>Verification & evidence legend</strong></summary>
      <p><strong>Hands-on</strong> = directly exercised by GlassesResearch. <strong>Primary</strong> = manufacturer, official support, manual, release, or maintained product history. <strong>Commercial</strong> = documented retail route. <strong>Secondary</strong> = reputable reporting used when stronger historical sources are unavailable. Community and inferred claims remain explicitly labeled elsewhere in the repository.</p>
    </details>
    <p><strong>Missing a model?</strong> <a href="../docs/faq/ASK_YOUR_OWN_QUESTION.md">Ask us to investigate it</a> or <a href="../docs/CONTRIBUTE.md">contribute what you know</a>.</p>
  `;

  const firstTable = tables[0];
  firstTable.parentNode.insertBefore(controls, firstTable);

  const search = controls.querySelector('[data-model-filter="search"]');
  const maker = controls.querySelector('[data-model-filter="maker"]');
  const state = controls.querySelector('[data-model-filter="state"]');
  const type = controls.querySelector('[data-model-filter="type"]');
  const count = controls.querySelector(".model-result-count");

  const apply = () => {
    const q = search.value.trim().toLowerCase();
    let visible = 0;
    rows.forEach((row) => {
      const haystack = row.textContent.toLowerCase();
      const matches = (!q || haystack.includes(q)) &&
        (!maker.value || read(row, "maker") === maker.value) &&
        (!state.value || read(row, "state") === state.value) &&
        (!type.value || read(row, "type") === type.value);
      row.hidden = !matches;
      if (matches) visible += 1;
    });
    count.textContent = `${visible} of ${rows.length} models shown`;
    tables.forEach((table) => {
      const anyVisible = Array.from(table.querySelectorAll("tbody tr")).some((row) => !row.hidden);
      table.style.display = anyVisible ? "" : "none";
      let sibling = table.previousElementSibling;
      if (sibling && /^H[2-4]$/.test(sibling.tagName)) sibling.style.display = anyVisible ? "" : "none";
    });
  };

  [search, maker, state, type].forEach((control) => control.addEventListener("input", apply));
  controls.querySelector('[data-model-filter="reset"]').addEventListener("click", () => {
    search.value = "";
    maker.value = "";
    state.value = "";
    type.value = "";
    apply();
  });
  apply();
}

if (typeof document$ !== "undefined") {
  document$.subscribe(enhanceTheList);
} else {
  document.addEventListener("DOMContentLoaded", enhanceTheList);
}
