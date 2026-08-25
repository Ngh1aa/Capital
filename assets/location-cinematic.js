(function initLocationCinematic(global, document) {
  'use strict';

  function initLifeGallery() {
    const root = document.querySelector('[data-lc-gallery]');
    if (!root) return;
    const image = root.querySelector('[data-lc-gallery-image]');
    const title = root.querySelector('[data-lc-gallery-title]');
    const copy = root.querySelector('[data-lc-gallery-copy]');
    const count = root.querySelector('[data-lc-gallery-count]');
    const link = root.querySelector('.lc-life-copy a');
    const tabs = Array.from(root.querySelectorAll('[data-lc-scene]'));
    if (!image || !title || !copy || !tabs.length) return;

    const select = (tab, index) => {
      tabs.forEach((item) => {
        const active = item === tab;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      if (count) count.textContent = `${String(index + 1).padStart(2, '0')} / ${String(tabs.length).padStart(2, '0')}`;
      if (image.src.endsWith(tab.dataset.image)) {
        title.textContent = tab.dataset.title || '';
        copy.textContent = tab.dataset.copy || '';
        if (link && tab.dataset.link) link.href = tab.dataset.link;
        return;
      }
      image.classList.add('is-changing');
      const update = () => {
        image.src = tab.dataset.image;
        image.alt = tab.dataset.alt || '';
        title.textContent = tab.dataset.title || '';
        copy.textContent = tab.dataset.copy || '';
        if (link && tab.dataset.link) link.href = tab.dataset.link;
        image.classList.remove('is-changing');
      };
      global.setTimeout(update, global.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 160);
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => select(tab, index));
      tab.addEventListener('keydown', (event) => {
        if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
        event.preventDefault();
        const nextIndex = (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
        tabs[nextIndex].focus();
        select(tabs[nextIndex], nextIndex);
      });
    });
  }

  function initMap() {
    const root = document.querySelector('.lc-map');
    if (!root) return;
    const pins = Array.from(root.querySelectorAll('.lc-map-pin'));
    const filters = Array.from(root.querySelectorAll('[data-lc-map-filter]'));
    const title = root.querySelector('[data-lc-map-title]');
    const meta = root.querySelector('[data-lc-map-meta]');
    const distance = root.querySelector('[data-lc-map-distance]');

    const selectPin = (pin) => {
      pins.forEach((item) => item.classList.toggle('is-active', item === pin));
      if (title) title.textContent = pin.dataset.title || '';
      if (meta) meta.textContent = pin.dataset.meta || '';
      if (distance) distance.textContent = pin.dataset.distance || '';
    };

    const filter = (category) => {
      filters.forEach((button) => button.classList.toggle('is-active', button.dataset.lcMapFilter === category));
      pins.forEach((pin) => {
        pin.hidden = category !== 'all' && pin.dataset.category !== category;
      });
      const firstVisible = pins.find((pin) => !pin.hidden);
      if (firstVisible) selectPin(firstVisible);
    };

    filters.forEach((button) => button.addEventListener('click', () => filter(button.dataset.lcMapFilter)));
    pins.forEach((pin) => pin.addEventListener('click', () => selectPin(pin)));
  }

  function init() {
    initLifeGallery();
    initMap();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})(window, document);
