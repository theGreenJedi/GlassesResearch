// Make models/THE_LIST.md a useful interactive research hub on the rendered site.
// The Markdown remains the canonical evidence ledger; this layer adds navigation
// and client-side filtering without changing the underlying research record.

async function enhanceTheList() {
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

  let deviceMap = new Map();
  try {
    const response = await fetch("/data/devices.json", { cache: "no-store" });
    if (response.ok) {
      const payload = await response.json();
      deviceMap = new Map((payload.records || []).map((record) => [record.id, record]));
    }
  } catch (_) {
    // The ledger remains usable even if the enhancement data cannot load.
  }

  // Prefer a dedicated repository chapter, then the evidence-derived editorial
  // profile, then the strongest available source. Every canonical row receives
  // a profile path from the device-database validation layer.
  tables.forEach((table) => {
    const headers = Array.from(table.querySelectorAll("thead th")).map((cell) =>
      cell.textContent.trim().toLowerCase()
    );
    const idIndex = headers.indexOf("id");
    const modelIndex = headers.indexOf("model");
    const evidenceIndex = headers.indexOf("evidence / links");
    if (idIndex < 0 || modelIndex < 0 || evidenceIndex < 0) return;

    table.querySelectorAll("tbody tr").forEach((row) => {
      const cells = row.querySelectorAll("td");
      const idCell = cells[idIndex];
      const modelCell = cells[modelIndex];
      const evidenceCell = cells[evidenceIndex];
      if (!idCell || !modelCell || !evidenceCell) return;

      const modelId = idCell.textContent.trim();
      const publicPaths = deviceMap.get(modelId)?.public || {};
      const links = Array.from(evidenceCell.querySelectorAll("a[href]"));
      const chapterLink = links.find((link) =>
        /\/models\/[A-Za-z0-9._-]+\/(?:README\.md)?(?:$|[#?])/.test(link.getAttribute("href") || "")
      );
      const namedSource = links.find(
        (link) => link.textContent.trim().toLowerCase() === "source"
      );
      const externalLink = links.find((link) => /^https?:\/\//.test(link.href));

      if (!modelCell.querySelector("a")) {
        const destination = chapterLink?.href || publicPaths.profile || namedSource?.href || externalLink?.href || links[0]?.href;
        if (destination) {
          const anchor = document.createElement("a");
          anchor.href = destination;
          anchor.textContent = modelCell.textContent.trim();
          anchor.className = "model-index-link";
          anchor.title = chapterLink
            ? "Open the GlassesResearch model chapter"
            : publicPaths.profile
              ? "Open the GlassesResearch editorial profile"
              : "Open the best available model source";
          if (!chapterLink && !publicPaths.profile && /^https?:\/\//.test(destination)) {
            anchor.target = "_blank";
            anchor.rel = "noopener noreferrer";
          }
          modelCell.replaceChildren(anchor);
        }
      }

      if (modelCell.querySelector(".model-research-paths")) return;
      const research = [];
      if (publicPaths.profile) research.push(`<a href="${publicPaths.profile}">Profile</a>`);
      if (publicPaths.report_card) research.push(`<a href="${publicPaths.report_card}">Report card</a>`);
      if (publicPaths.lineage) research.push(`<a href="${publicPaths.lineage}">Lineage</a>`);
      if (research.length) {
        const paths = document.createElement("div");
        paths.className = "model-research-paths";
        paths.innerHTML = research.join(" · ");
        modelCell.appendChild(paths);
      }
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

  const controls = document.createElement("section");
  controls.className = "model-hub-controls";
  controls.innerHTML = `
    <h2>Explore the smart-glasses ecosystem</h2>
    <p><strong>The List is the central index for GlassesResearch.</strong> Search all canonical glasses, narrow by maker, status, or device type, then follow each row into its profile, Report Card, lineage research, model chapter, or strongest available source.</p>
    <div class="model-hub-links">
      <a href="/docs/COMPARISON_ENGINE/">Find & compare</a> ·
      <a href="/docs/REPORT_CARD/">Report Cards</a> ·
      <a href="/lineages/">Technology lineages</a> ·
      <a href="/models/ADJACENT_WEARABLES/">Adjacent wearable-HCI</a> ·
      <a href="/buyers/BUYER_AND_OPENNESS_GUIDE/">Buyer & openness guide</a> ·
      <a href="/hacking/">Development & hacking</a>
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
    <p><strong>Missing a model?</strong> <a href="/docs/faq/ASK_YOUR_OWN_QUESTION/">Ask us to investigate it</a> or <a href="/docs/CONTRIBUTE/">contribute what you know</a>.</p>
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
      const sibling = table.previousElementSibling;
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
  document$.subscribe(() => { enhanceTheList(); });
} else {
  document.addEventListener("DOMContentLoaded", () => { enhanceTheList(); });
}
