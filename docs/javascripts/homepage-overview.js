(() => {
  const root = document.getElementById("homepage-status");
  if (!root) return;
  const set = (name, value) => {
    const node = root.querySelector(`[data-site-stat="${name}"]`);
    if (node) node.textContent = value;
  };
  const setNumber = (name, value) => {
    const number = Number(value);
    if (Number.isFinite(number)) set(name, number.toLocaleString());
  };
  fetch("/data/site-status.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error("status unavailable");
      return response.json();
    })
    .then((status) => {
      setNumber("models", status.canonical_model_count);
      setNumber("report-cards", status.scored_report_card_count);

      const rawDate = status.catalog_updated_at;
      if (typeof rawDate === "string" && /^\d{4}-\d{2}-\d{2}$/.test(rawDate)) {
        const [year, month, day] = rawDate.split("-").map(Number);
        const updated = new Date(year, month - 1, day);
        if (!Number.isNaN(updated.valueOf())) {
          set("freshness", updated.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }));
        }
      }
    })
    .catch(() => {
      // The build already renders canonical values into the HTML. If a refresh
      // request fails, preserve those values rather than blanking the status.
    });
})();
