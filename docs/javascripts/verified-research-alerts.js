(() => {
  const CADENCES = ["as_verified", "daily", "weekly", "monthly", "annually"];
  const FORM_SELECTOR = 'form[data-verified-research-alerts]';

  function normalizeList(value) {
    return String(value || "").split(",").map((item) => item.trim()).filter(Boolean).slice(0, 50);
  }

  function payloadFrom(form) {
    const cadence = form.elements.cadence?.value || "";
    if (!CADENCES.includes(cadence)) throw new Error("Choose a valid delivery cadence.");

    return {
      schema: 1,
      email: (form.elements.email?.value || "").trim(),
      cadence,
      include: {
        models: normalizeList(form.elements.include_models?.value),
        brands_lineages: normalizeList(form.elements.include_brands?.value),
        topics: Array.from(form.querySelectorAll('input[name="include_topics"]:checked')).map((el) => el.value),
      },
      exclude: {
        models: normalizeList(form.elements.exclude_models?.value),
        brands_lineages: normalizeList(form.elements.exclude_brands?.value),
        topics: Array.from(form.querySelectorAll('input[name="exclude_topics"]:checked')).map((el) => el.value),
      },
      source: "research_news",
    };
  }

  document.addEventListener("submit", async (event) => {
    const form = event.target instanceof HTMLFormElement ? event.target.closest(FORM_SELECTOR) : null;
    if (!form) return;

    event.preventDefault();

    const status = form.querySelector("[data-alert-status]");
    const button = form.querySelector('button[type="submit"]');
    const endpoint = form.dataset.endpoint || "";

    if (!status || !button) return;

    if (!endpoint) {
      status.textContent = "Verified Research Alerts are not available right now.";
      return;
    }

    status.textContent = "";

    let payload;
    try {
      payload = payloadFrom(form);
      if (!payload.email || !payload.email.includes("@")) throw new Error("Enter a valid email address.");
    } catch (error) {
      status.textContent = error instanceof Error ? error.message : "Check the subscription form and try again.";
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
      const result = await response.json().catch(() => ({}));
      if (!response.ok || result.ok === false) {
        throw new Error(result.message || "Subscription service is temporarily unavailable.");
      }
      status.textContent = result.message || "Check your email to confirm your subscription.";
      form.reset();
    } catch (error) {
      status.textContent = error instanceof Error ? error.message : "Subscription service is temporarily unavailable.";
    } finally {
      button.disabled = false;
    }
  });
})();
