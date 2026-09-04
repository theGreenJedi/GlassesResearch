(() => {
  "use strict";

  const MODEL_ID = /\b(GLS-\d{4})\b/i;
  const MAX_CAPABILITY_GAPS = 8;
  const MAX_SCORE_GAPS = 5;

  function modelIdFromPage() {
    const heading = document.querySelector("h1");
    const match = heading?.textContent?.match(MODEL_ID);
    return match ? match[1].toUpperCase() : null;
  }

  function findGapHeading() {
    return [...document.querySelectorAll("h2")].find(
      (heading) => heading.textContent.trim().toLowerCase() === "corrections and research gaps"
    );
  }

  function labelMap(fields = []) {
    return new Map(fields.map((field) => {
      if (typeof field === "string") return [field, field.replaceAll("_", " ").replace(/\b\w/g, (c) => c.toUpperCase())];
      return [field.id, field.label || field.id];
    }));
  }

  function unknownCapabilityLabels(dataset, modelId) {
    const record = dataset.records?.find((item) => item.id === modelId);
    if (!record) return [];
    const labels = labelMap(dataset.capability_fields || []);
    return Object.entries(record.capabilities || {})
      .filter(([, state]) => state?.value === "unknown")
      .map(([field]) => labels.get(field) || field.replaceAll("_", " "));
  }

  function unknownScoreLabels(dataset, modelId) {
    const record = dataset.records?.find((item) => item.id === modelId);
    if (!record) return [];
    const labels = labelMap(dataset.dimensions || []);
    return Object.entries(record.scores || {})
      .filter(([, value]) => String(value).toLowerCase() === "unknown")
      .map(([field]) => labels.get(field) || field.replaceAll("_", " "));
  }

  function makeList(title, items, limit) {
    if (!items.length) return null;
    const wrapper = document.createElement("div");
    wrapper.className = "gr-research-gap-group";

    const strong = document.createElement("strong");
    strong.textContent = title;
    wrapper.append(strong);

    const list = document.createElement("ul");
    items.slice(0, limit).forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      list.append(li);
    });
    wrapper.append(list);

    if (items.length > limit) {
      const remainder = document.createElement("p");
      remainder.textContent = `Plus ${items.length - limit} additional unresolved field${items.length - limit === 1 ? "" : "s"}.`;
      wrapper.append(remainder);
    }
    return wrapper;
  }

  async function render() {
    const modelId = modelIdFromPage();
    const heading = findGapHeading();
    if (!modelId || !heading || document.querySelector(".gr-actionable-research-gaps")) return;

    try {
      const [capResponse, scoreResponse] = await Promise.all([
        fetch("/data/finder-capabilities.json", { credentials: "same-origin" }),
        fetch("/data/report-card-scores.json", { credentials: "same-origin" }),
      ]);
      if (!capResponse.ok || !scoreResponse.ok) return;

      const [capabilities, scores] = await Promise.all([capResponse.json(), scoreResponse.json()]);
      const capGaps = unknownCapabilityLabels(capabilities, modelId);
      const scoreGaps = unknownScoreLabels(scores, modelId);
      if (!capGaps.length && !scoreGaps.length) return;

      const section = document.createElement("div");
      section.className = "gr-actionable-research-gaps";

      const intro = document.createElement("p");
      intro.textContent = "These are unresolved evidence fields, not known product limitations. Primary documentation, reproducible testing, or other appropriately classified evidence can close them.";
      section.append(intro);

      const capList = makeList("Capability evidence still needed", capGaps, MAX_CAPABILITY_GAPS);
      const scoreList = makeList("Report Card dimensions still unscored", scoreGaps, MAX_SCORE_GAPS);
      if (capList) section.append(capList);
      if (scoreList) section.append(scoreList);

      heading.insertAdjacentElement("afterend", section);
    } catch (_error) {
      // Enhancement only: model pages remain fully usable if datasets cannot be loaded.
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render, { once: true });
  } else {
    render();
  }
})();
