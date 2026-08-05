// Make every model name in models/THE_LIST.md a useful navigation link.
// Prefer a repository model chapter when one exists; otherwise use the row's
// canonical external source. This operates only on the rendered website and
// leaves the evidence/source column intact.

function linkModelNames() {
  const article = document.querySelector("article.md-content__inner");
  if (!article) return;

  const heading = article.querySelector("h1");
  if (!heading || !heading.textContent.includes("The List")) return;

  article.querySelectorAll("table").forEach((table) => {
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
}

if (typeof document$ !== "undefined") {
  document$.subscribe(linkModelNames);
} else {
  document.addEventListener("DOMContentLoaded", linkModelNames);
}
