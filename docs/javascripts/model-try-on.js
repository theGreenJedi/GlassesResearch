(() => {
  let stream = null;
  let animationFrame = 0;
  let faceLandmarker = null;

  const MEDIAPIPE_VERSION = '0.10.22-rc.20250304';
  const MEDIAPIPE_MODULE = `https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@${MEDIAPIPE_VERSION}/vision_bundle.mjs`;
  const MEDIAPIPE_WASM = `https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@${MEDIAPIPE_VERSION}/wasm`;
  const FACE_MODEL = 'https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task';

  const stop = () => {
    cancelAnimationFrame(animationFrame);
    animationFrame = 0;
    if (stream) stream.getTracks().forEach((track) => track.stop());
    stream = null;
  };

  const close = (dialog) => {
    stop();
    if (dialog?.open) dialog.close();
  };

  const ensureLandmarker = async () => {
    if (faceLandmarker) return faceLandmarker;
    const vision = await import(MEDIAPIPE_MODULE);
    const fileset = await vision.FilesetResolver.forVisionTasks(MEDIAPIPE_WASM);
    faceLandmarker = await vision.FaceLandmarker.createFromOptions(fileset, {
      baseOptions: { modelAssetPath: FACE_MODEL, delegate: 'GPU' },
      runningMode: 'VIDEO',
      numFaces: 1,
      outputFaceBlendshapes: false,
      outputFacialTransformationMatrixes: false
    });
    return faceLandmarker;
  };

  const placeAsset = (video, glasses, landmarks) => {
    // MediaPipe canonical outer-eye landmarks. Coordinates are normalized to
    // the unmirrored camera frame; the preview is mirrored, so X is inverted.
    const rightOuter = landmarks[33];
    const leftOuter = landmarks[263];
    if (!rightOuter || !leftOuter) return;
    const x1 = 1 - rightOuter.x;
    const x2 = 1 - leftOuter.x;
    const y1 = rightOuter.y;
    const y2 = leftOuter.y;
    const cx = ((x1 + x2) / 2) * 100;
    const cy = ((y1 + y2) / 2) * 100;
    const dx = (x2 - x1) * video.clientWidth;
    const dy = (y2 - y1) * video.clientHeight;
    const eyeDistance = Math.hypot(dx, dy);
    const angle = Math.atan2(dy, dx) * 180 / Math.PI;
    glasses.style.left = `${cx}%`;
    glasses.style.top = `${cy}%`;
    glasses.style.width = `${Math.max(80, eyeDistance * 2.25)}px`;
    glasses.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;
    glasses.hidden = false;
  };

  const track = async (video, glasses, status) => {
    let tracker;
    try {
      tracker = await ensureLandmarker();
      status.textContent = 'Face tracking active. Move naturally to preview the frame.';
    } catch (_) {
      status.textContent = 'Live camera is active, but face tracking could not load. No camera frames were uploaded.';
      return;
    }
    const render = () => {
      if (!stream || video.readyState < 2) {
        animationFrame = requestAnimationFrame(render);
        return;
      }
      try {
        const result = tracker.detectForVideo(video, performance.now());
        const face = result?.faceLandmarks?.[0];
        if (face) placeAsset(video, glasses, face);
        else glasses.hidden = true;
      } catch (_) {}
      animationFrame = requestAnimationFrame(render);
    };
    render();
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
          <img class="gr-try-on-glasses" alt="" aria-hidden="true" hidden>
        </div>
        <div class="gr-try-on-controls">
          <p data-gr-try-on-status><strong>Private preview.</strong> Camera frames stay in this browser and are not uploaded or recorded.</p>
          <p>This visualization follows your face but does not establish physical or prescription fit.</p>
          <button type="button" class="gr-button gr-button-secondary" data-gr-try-on-close>Close camera</button>
        </div>`;
      root.append(dialog);
      dialog.querySelector('[data-gr-try-on-close]').addEventListener('click', () => close(dialog));
      dialog.addEventListener('close', stop);
    }

    const video = dialog.querySelector('video');
    const glasses = dialog.querySelector('.gr-try-on-glasses');
    const status = dialog.querySelector('[data-gr-try-on-status]');
    glasses.src = asset;
    dialog.showModal();

    if (!navigator.mediaDevices?.getUserMedia) {
      status.textContent = 'Camera preview is not supported by this browser.';
      return;
    }

    try {
      stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: { facingMode: 'user', width: { ideal: 1280 }, height: { ideal: 720 } }
      });
      video.srcObject = stream;
      await video.play();
      track(video, glasses, status);
    } catch (error) {
      stop();
      status.textContent = error?.name === 'NotAllowedError'
        ? 'Camera permission was not granted. Nothing was captured or uploaded.'
        : 'Camera preview is unavailable in this browser.';
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
