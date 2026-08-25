(function faqSearch(document) {
  'use strict';
  const items = Array.from(document.querySelectorAll('[data-faq-item]'));
  const filters = Array.from(document.querySelectorAll('[data-faq-filter]'));
  const input = document.querySelector('#faq-search');
  const count = document.querySelector('[data-faq-count]');
  const empty = document.querySelector('[data-faq-empty]');
  let category = 'all';
  function render() {
    const query = (input?.value || '').trim().toLowerCase();
    let visible = 0;
    items.forEach((item) => {
      const matchesCategory = category === 'all' || item.dataset.faqCategory === category;
      const matchesQuery = !query || item.textContent.toLowerCase().includes(query);
      item.hidden = !(matchesCategory && matchesQuery);
      if (!item.hidden) visible += 1;
    });
    if (count) count.textContent = `${visible} answer${visible === 1 ? '' : 's'} shown`;
    if (empty) empty.hidden = visible !== 0;
  }
  filters.forEach((button) => button.addEventListener('click', () => {
    category = button.dataset.faqFilter;
    filters.forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
    render();
  }));
  input?.addEventListener('input', render);
  render();
})(document);
