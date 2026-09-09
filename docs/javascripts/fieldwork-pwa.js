(() => {
  const app = document.getElementById('fieldwork-app');
  if (!app) return;

  const manifest = document.createElement('link');
  manifest.rel = 'manifest';
  manifest.href = '/docs/fieldwork.webmanifest';
  document.head.appendChild(manifest);

  const theme = document.createElement('meta');
  theme.name = 'theme-color';
  theme.content = '#111111';
  document.head.appendChild(theme);

  const installButton = document.getElementById('fw-install');
  let deferredPrompt = null;

  window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    deferredPrompt = event;
    if (installButton) installButton.hidden = false;
  });

  installButton?.addEventListener('click', async () => {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
    installButton.hidden = true;
  });

  window.addEventListener('appinstalled', () => {
    if (installButton) installButton.hidden = true;
  });

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/docs/fieldwork-sw.js', {scope: '/docs/FIELDWORK_APP/'}).catch(() => {});
    });
  }
})();
