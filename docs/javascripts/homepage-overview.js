(() => {
  const root = document.getElementById("homepage-status");
  if (!root) return;
  const set = (name, value) => {
    const node = root.querySelector(`[data-site-stat="${name}"]`);
    if (node) node.textContent = value;
  };
  fetch("data/site-status.json")
    .then((response) => {
      if (!response.ok) throw new Error("status unavailable");
      return response.json();
    })
    .then((status) => {
      set("models", Number(status.canonical_model_count).toLocaleString());
      set("report-cards", Number(status.scored_report_card_count).toLocaleString());

      const rawDate = status.catalog_updated_at;
      if (typeof rawDate === "string" && /^\d{4}-\d{2}-\d{2}$/.test(rawDate)) {
        const [year, month, day] = rawDate.split("-").map(Number);
        const updated = new Date(year, month - 1, day);
        if (!Number.isNaN(updated.valueOf())) {
          set("freshness", updated.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }));
        }
      }
    })
    .catch(() => {});
})();
