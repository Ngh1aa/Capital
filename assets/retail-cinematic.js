(function retailFunnel(document) {
  'use strict';
  const buttons = Array.from(document.querySelectorAll('[data-retail-filter]'));
  const cards = Array.from(document.querySelectorAll('[data-retail-brand]'));
  if (!buttons.length || !cards.length) return;
  buttons.forEach((button) => button.addEventListener('click', () => {
    const category = button.dataset.retailFilter;
    buttons.forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
    cards.forEach((card) => { card.hidden = category !== 'all' && card.dataset.retailBrand !== category; });
    const count = document.querySelector('[data-retail-result-count]');
    if (count) count.textContent = `${cards.filter((card) => !card.hidden).length} brand references shown`;
  }));
})(document);
