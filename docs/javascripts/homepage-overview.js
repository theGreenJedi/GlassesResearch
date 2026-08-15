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
      const built = new Date(status.generated_at);
      if (!Number.isNaN(built.valueOf())) {
        set("freshness", built.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }));
      }
    })
    .catch(() => {});
})();
