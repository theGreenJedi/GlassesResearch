(() => {
  const CADENCES = ["as_verified", "daily", "weekly", "monthly", "annually"];
  const DEFAULT_ENDPOINT = "https://subscriptions.glassesresearch.org/api/subscribe";

  function normalizeList(value) {
    return value.split(",").map((item) => item.trim()).filter(Boolean).slice(0, 50);
  }

  function payloadFrom(form) {
    const cadence = form.elements.cadence.value;
    if (!CADENCES.includes(cadence)) throw new Error("Choose a valid delivery cadence.");

    return {
      schema: 1,
      email: form.elements.email.value.trim(),
      cadence,
      include: {
        models: normalizeList(form.elements.include_models.value),
        brands_lineages: normalizeList(form.elements.include_brands.value),
        topics: Array.from(form.querySelectorAll('input[name="include_topics"]:checked')).map((el) => el.value),
      },
      exclude: {
        models: normalizeList(form.elements.exclude_models.value),
        brands_lineages: normalizeList(form.elements.exclude_brands.value),
        topics: Array.from(form.querySelectorAll('input[name="exclude_topics"]:checked')).map((el) => el.value),
      },
      source: "research_news",
    };
  }

  function init(form) {
    const status = form.querySelector("[data-alert-status]");
    const button = form.querySelector('button[type="submit"]');
    const endpoint = form.dataset.endpoint || DEFAULT_ENDPOINT;

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      status.textContent = "";

      let payload;
      try {
        payload = payloadFrom(form);
        if (!payload.email || !payload.email.includes("@")) throw new Error("Enter a valid email address.");
      } catch (error) {
        status.textContent = error.message;
        return;
      }

      button.disabled = true;
      status.textContent = "Submitting…";

      try {
        const response = await fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
        if (!response.ok) throw new Error("Subscription service is not available yet.");
        const result = await response.json().catch(() => ({}));
        status.textContent = result.message || "Check your email to confirm your subscription.";
        if (result.ok !== false) form.reset();
      } catch (error) {
        status.textContent = error.message || "Subscription service is not available yet.";
      } finally {
        button.disabled = false;
      }
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-verified-research-alerts]").forEach(init);
  });
})();
