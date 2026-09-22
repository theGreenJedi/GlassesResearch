(() => {
  const activate = (event) => {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    const control = event.target.closest('.gr-search-button, .gr-menu-button');
    if (!control) return;
    event.preventDefault();
    control.click();
  };
  document.addEventListener('keydown', activate);
})();
