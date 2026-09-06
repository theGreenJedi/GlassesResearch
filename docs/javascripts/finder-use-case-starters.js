(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const PRESETS = [
    { id: 'translation-display', label: 'Translation + display', filters: ['translation', 'display'] },
    { id: 'camera-video', label: 'Camera + video', filters: ['camera', 'video_recording'] },
    { id: 'prescription', label: 'Prescription daily wear', filters: ['prescription'] },
    { id: 'privacy-no-camera', label: 'Privacy-first · no camera', filters: ['no_camera'] },
    { id: 'developer-control', label: 'Developer / owner control', filters: ['sdk', 'custom_ai'] },
  ];

  const initialize = () => {
    const groups = host.querySelector('.finder-groups');
    if (!groups || host.querySelector('[data-finder-use-case-starters]')) return false;

    const panel = document.createElement('div');
    panel.className = 'finder-use-case-starters';
    panel.dataset.finderUseCaseStarters = '';
    panel.innerHTML = `
      <div class="finder-use-case-copy">
        <strong>Start with a use case</strong>
        <span>These are shortcuts into existing evidence-backed filters, not rankings.</span>
      </div>
      <div class="finder-use-case-buttons">
        ${PRESETS.map((preset) => `<button type="button" data-finder-preset="${preset.id}">${preset.label}</button>`).join('')}
      </div>`;

    groups.parentNode.insertBefore(panel, groups);

    panel.querySelectorAll('[data-finder-preset]').forEach((button) => {
      button.addEventListener('click', () => {
        const preset = PRESETS.find((entry) => entry.id === button.dataset.finderPreset);
        if (!preset) return;

        const boxes = [...host.querySelectorAll('.finder-options input[type="checkbox"]')];
        boxes.forEach((box) => { box.checked = preset.filters.includes(box.value); });

        const exactOnly = host.querySelector('#exact-only');
        if (exactOnly) exactOnly.checked = true;

        const scoreEnables = [...host.querySelectorAll('[data-score-enable]')];
        scoreEnables.forEach((box) => { box.checked = false; });
        [...host.querySelectorAll('[data-score-range]')].forEach((range) => { range.disabled = true; });

        const trigger = boxes.find((box) => box.checked) || boxes[0];
        trigger?.dispatchEvent(new Event('change', { bubbles: true }));

        panel.querySelectorAll('[data-finder-preset]').forEach((candidate) => {
          candidate.setAttribute('aria-pressed', candidate === button ? 'true' : 'false');
        });
      });
    });

    return true;
  };

  if (initialize()) return;
  const observer = new MutationObserver(() => {
    if (initialize()) observer.disconnect();
  });
  observer.observe(host, { childList: true, subtree: true });
})();
