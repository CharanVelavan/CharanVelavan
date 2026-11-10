(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const button = document.querySelector('#motion');
  let paused = preference.matches;
  function render() {
    document.documentElement.classList.toggle('motion-paused', paused);
    button.disabled = preference.matches;
    button.textContent = preference.matches ? 'Reduced motion' : paused ? 'Resume motion' : 'Pause motion';
    button.setAttribute('aria-pressed', String(paused));
  }
  button.hidden = false;
  button.addEventListener('click', () => { paused = !paused; render(); });
  preference.addEventListener('change', event => { paused = event.matches; render(); });
  render();
})();
