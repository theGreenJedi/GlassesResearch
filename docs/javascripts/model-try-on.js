(() => {
  let stream = null;
  const stop = () => {
    if (stream) stream.getTracks().forEach((track) => track.stop());
    stream = null;
  };

  const close = (dialog) => {
    stop();
    if (dialog?.open) dialog.close();
  };

  const openTryOn = async (root) => {
    const asset = root.dataset.asset;
    if (!asset) return;
    let dialog = root.querySelector('.gr-try-on-dialog');
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.className = 'gr-try-on-dialog';
      dialog.innerHTML = `
        <div class="gr-try-on-stage">
          <video autoplay muted playsinline aria-label="Live camera preview"></video>
          <img class="gr-try-on-glasses" alt="" aria-hidden="true">
        </div>
        <div class="gr-try-on-controls">
          <p><strong>Private preview.</strong> Camera frames stay in this browser and are not uploaded or recorded.</p>
          <p>This first-stage preview is visual only and does not establish physical or prescription fit.</p>
          <button type="button" class="gr-button gr-button-secondary" data-gr-try-on-close>Close camera</button>
        </div>`;
      root.append(dialog);
      dialog.querySelector('[data-gr-try-on-close]').addEventListener('click', () => close(dialog));
      dialog.addEventListener('close', stop);
    }

    const video = dialog.querySelector('video');
    const glasses = dialog.querySelector('.gr-try-on-glasses');
    glasses.src = asset;
    dialog.showModal();

    if (!navigator.mediaDevices?.getUserMedia) {
      dialog.querySelector('.gr-try-on-controls p').textContent = 'Camera preview is not supported by this browser.';
      return;
    }

    try {
      stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: { facingMode: 'user', width: { ideal: 1280 }, height: { ideal: 720 } }
      });
      video.srcObject = stream;
    } catch (error) {
      close(dialog);
      if (error?.name !== 'NotAllowedError') console.warn('GlassesResearch camera preview unavailable', error);
    }
  };

  document.addEventListener('click', (event) => {
    const button = event.target.closest('[data-gr-try-on-open]');
    if (!button) return;
    const root = button.closest('[data-gr-try-on]');
    if (root) openTryOn(root);
  });

  window.addEventListener('pagehide', stop);
})();
