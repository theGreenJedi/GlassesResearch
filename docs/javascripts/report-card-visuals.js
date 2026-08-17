/* GlassesResearch original data visualization: progressively enhances Report Card score tables. */
(() => {
  const SCORE = /^\s*(10(?:\.0)?|[0-9](?:\.\d+)?)\s*$/;

  function enhance(table) {
    const headings = [...table.querySelectorAll("thead th")].map((cell) => cell.textContent.trim().toLowerCase());
    const dimensionIndex = headings.indexOf("dimension");
    const scoreIndex = headings.indexOf("score");
    if (dimensionIndex < 0 || scoreIndex < 0 || table.dataset.grScoreVisuals === "true") return;

    let enhanced = 0;
    table.querySelectorAll("tbody tr").forEach((row) => {
      const cells = row.querySelectorAll("td");
      if (cells.length <= scoreIndex) return;
      const raw = cells[scoreIndex].textContent.trim();
      const match = raw.match(SCORE);
      if (!match) return;
      const score = Math.max(0, Math.min(10, Number(match[1])));
      const label = cells[dimensionIndex]?.textContent.trim() || "Report Card dimension";
      cells[scoreIndex].innerHTML = `<span class="gr-score-value">${raw}</span><span class="gr-score-track" role="img" aria-label="${label}: ${score} out of 10"><span class="gr-score-fill" style="--gr-score:${score * 10}%"></span></span>`;
      enhanced += 1;
    });

    if (enhanced) {
      table.dataset.grScoreVisuals = "true";
      table.classList.add("gr-report-card-table");
    }
  }

  function run() {
    document.querySelectorAll("article table").forEach(enhance);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
  document.addEventListener("DOMContentSwitch", run);
})();
