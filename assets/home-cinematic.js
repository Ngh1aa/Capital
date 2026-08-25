(function initHomeCinematic(global, document) {
  'use strict';

  function initScaleStory() {
    const stage = document.querySelector('.hc-scale-stage');
    if (!stage) return;
    const image = stage.querySelector('[data-scale-image]');
    const steps = Array.from(stage.querySelectorAll('[data-scale-step]'));
    if (!image || !steps.length) return;

    const select = (step) => {
      const index = steps.indexOf(step);
      if (index < 0) return;
      steps.forEach((item, itemIndex) => {
        const active = itemIndex === index;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-current', active ? 'true' : 'false');
      });
      if (image.getAttribute('src') !== step.dataset.image) {
        image.style.opacity = '.3';
        global.setTimeout(() => {
          image.src = step.dataset.image;
          image.alt = step.dataset.alt || '';
          image.style.opacity = '';
        }, global.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 180);
      }
    };

    steps.forEach((step) => step.addEventListener('click', () => select(step)));
    if ('IntersectionObserver' in global && !global.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => { if (entry.isIntersecting) select(entry.target); });
      }, { threshold: .65, rootMargin: '-8% 0px -8% 0px' });
      steps.forEach((step) => observer.observe(step));
    }
  }

  function initAnatomy() {
    const parts = Array.from(document.querySelectorAll('[data-anatomy-part]'));
    if (!parts.length) return;
    parts.forEach((part) => part.addEventListener('click', () => {
      parts.forEach((item) => {
        const active = item === part;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
    }));
  }

  function init() {
    initScaleStory();
    initAnatomy();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})(window, document);
