(function retailFunnel(document) {
  'use strict';
  const buttons = Array.from(document.querySelectorAll('[data-retail-filter]'));
  const cards = Array.from(document.querySelectorAll('[data-retail-brand]'));
  const zones = Array.from(document.querySelectorAll('[data-retail-zone]'));
  const locationPanel = document.querySelector('[data-retail-location-panel]');
  const locationLabel = document.querySelector('[data-retail-location-label]');
  const locationInput = document.querySelector('[name="selectedLocation"]');
  const detailLabel = document.querySelector('[data-retail-selected-location]');
  const detailCta = document.querySelector('[data-retail-detail-cta]');
  const form = document.querySelector('[data-retail-form]');
  const success = document.querySelector('[data-retail-success]');
  const emailFallback = document.querySelector('[data-retail-email]');
  const resultCount = document.querySelector('[data-retail-result-count]');

  function updateFilter(category, activeButton) {
    buttons.forEach((button) => {
      const active = button === activeButton;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    cards.forEach((card) => { card.hidden = category !== 'all' && card.dataset.retailBrand !== category; });
    if (resultCount) resultCount.textContent = `${cards.filter((card) => !card.hidden).length} public references shown`;
  }

  buttons.forEach((button) => button.addEventListener('click', () => updateFilter(button.dataset.retailFilter, button)));

  function selectZone(label, zone) {
    zones.forEach((item) => item.classList.toggle('is-active', item === zone));
    if (locationPanel) locationPanel.hidden = false;
    if (locationLabel) locationLabel.textContent = `The Link · B1 · ${label}`;
    if (detailLabel) detailLabel.textContent = `The Link · B1 · ${label}`;
    if (locationInput) locationInput.value = `The Link · B1 · ${label}`;
    if (detailCta) detailCta.href = `#retail-enquiry`;
    document.querySelector('#retail-enquiry')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  zones.forEach((zone) => zone.addEventListener('click', () => selectZone(zone.dataset.retailZone, zone)));

  if (form && success && emailFallback) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      let valid = true;
      form.querySelectorAll('[required]').forEach((field) => {
        const ok = field.type === 'checkbox' ? field.checked : field.value.trim() && field.validity.valid;
        field.setAttribute('aria-invalid', String(!ok));
        if (!ok) valid = false;
      });
      if (!valid) {
        form.querySelector('[aria-invalid="true"]')?.focus();
        return;
      }
      const data = new FormData(form);
      const lines = [];
      for (const [key, value] of data.entries()) {
        if (value && key !== 'consent') lines.push(`${key}: ${value}`);
      }
      emailFallback.href = `mailto:leasing@capitalplace.vn?subject=${encodeURIComponent('Retail leasing enquiry · Capital Place')}&body=${encodeURIComponent(lines.join('\n'))}`;
      form.hidden = true;
      success.hidden = false;
      success.focus();
    });
  }
})(document);
