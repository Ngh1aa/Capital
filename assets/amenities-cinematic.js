(function initAmenitiesCinematic(global, document) {
  'use strict';

  function initBrandDirectory() {
    const root = document.querySelector('.ac-directory');
    if (!root) return;
    const brands = Array.from(root.querySelectorAll('[data-am-brand]'));
    const pins = Array.from(root.querySelectorAll('[data-brand-id]'));
    const filters = Array.from(root.querySelectorAll('[data-am-brand-filter]'));
    const image = root.querySelector('[data-am-brand-image]');
    const category = root.querySelector('[data-am-brand-category]');
    const title = root.querySelector('[data-am-brand-title]');
    const location = root.querySelector('[data-am-brand-location]');
    const hours = root.querySelector('[data-am-brand-hours]');
    const description = root.querySelector('[data-am-brand-description]');
    const link = root.querySelector('[data-am-brand-link]');
    if (!brands.length || !image || !title) return;

    const selectBrand = (brand) => {
      brands.forEach((item) => item.classList.toggle('is-active', item === brand));
      pins.forEach((pin) => pin.classList.toggle('is-active', pin.dataset.brandId === brand.dataset.brandId));
      image.src = brand.dataset.image || '';
      image.alt = `${brand.dataset.title || ''} at ${brand.dataset.location || 'The Link'}`;
      if (category) category.textContent = brand.dataset.category || '';
      title.textContent = brand.dataset.title || '';
      if (location) location.textContent = brand.dataset.location || '';
      if (hours) hours.textContent = brand.dataset.hours || '';
      if (description) description.textContent = brand.dataset.description || '';
      if (link) link.href = brand.dataset.category === 'wellness' || brand.dataset.category === 'family' ? 'amenities.html#brand-directory' : 'retail.html';
    };

    const filter = (value) => {
      filters.forEach((button) => button.classList.toggle('is-active', button.dataset.amBrandFilter === value));
      brands.forEach((brand) => { brand.hidden = value !== 'all' && brand.dataset.category !== value; });
      const firstVisible = brands.find((brand) => !brand.hidden);
      if (firstVisible) selectBrand(firstVisible);
    };

    brands.forEach((brand) => brand.addEventListener('click', () => selectBrand(brand)));
    pins.forEach((pin) => pin.addEventListener('click', () => {
      const brand = brands.find((item) => item.dataset.brandId === pin.dataset.brandId);
      if (brand && !brand.hidden) selectBrand(brand);
    }));
    filters.forEach((button) => button.addEventListener('click', () => filter(button.dataset.amBrandFilter)));
    const initial = brands.find((brand) => brand.classList.contains('is-active')) || brands[0];
    if (initial) selectBrand(initial);
  }

  function init() {
    initBrandDirectory();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})(window, document);
