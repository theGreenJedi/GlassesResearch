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


(() => {
  const root = document.getElementById("homepage-model-showcase");
  if (!root) return;

  const showcase = [
    { id: "GLS-0021", kind: "Audio", name: "HUAWEI Eyewear 2" },
    { id: "GLS-0047", kind: "Display", name: "Even G1" },
    { id: "GLS-0074", kind: "AR", name: "XREAL One" },
  ];

  fetch("/data/model-visuals.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error("visual registry unavailable");
      return response.json();
    })
    .then((registry) => {
      const records = registry?.records || {};
      const ready = showcase
        .map((item) => ({ ...item, visual: records[item.id] }))
        .filter(({ visual }) => visual?.state === "published" && visual?.primary_image);

      if (ready.length < 2) return;

      const cards = ready.map(({ id, kind, name, visual }) => {
        const link = document.createElement("a");
        link.href = `/models/catalog/${id.toLowerCase()}/`;
        link.className = "gr-hero-showcase__card";

        const media = document.createElement("span");
        media.className = "gr-hero-showcase__media";
        const image = document.createElement("img");
        image.src = visual.primary_image;
        image.alt = visual.alt || `${name} smart glasses`;
        image.loading = "eager";
        image.decoding = "async";
        media.append(image);

        const meta = document.createElement("span");
        meta.className = "gr-hero-showcase__meta";
        const label = document.createElement("span");
        label.textContent = kind;
        const title = document.createElement("strong");
        title.textContent = name;
        meta.append(label, title);

        link.append(media, meta);
        return link;
      });

      root.replaceChildren(...cards);
      root.hidden = false;
    })
    .catch(() => {
      root.hidden = true;
    });
})();
