(function occupiersCommunity(document, global) {
  'use strict';

  const toggle = document.querySelector('[data-privilege-toggle]');
  const details = document.querySelector('[data-privilege-details]');
  if (toggle && details) {
    toggle.addEventListener('click', () => {
      const open = details.hidden;
      details.hidden = !open;
      toggle.setAttribute('aria-expanded', String(open));
      const icon = toggle.querySelector('span');
      if (icon) icon.textContent = open ? '−' : '+';
    });
  }

  // Optional, non-sensitive preference only. No credentials or tenant-specific data are stored.
  const preferenceKey = 'capital-place-occupier-preference';
  const savedPreference = global.sessionStorage?.getItem(preferenceKey);
  if (savedPreference === 'occupier') document.documentElement.dataset.occupierPreference = 'occupier';
})(document, window);
