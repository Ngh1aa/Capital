(function initOfficeCinematic(global, document) {
  'use strict';

  function initAnatomy() {
    const visual = document.querySelector('.oc-anatomy-visual');
    const buttons = Array.from(document.querySelectorAll('[data-anatomy-target]'));
    if (!visual || !buttons.length) return;
    buttons.forEach((button) => button.addEventListener('click', () => {
      const target = button.dataset.anatomyTarget;
      visual.className = `oc-anatomy-visual is-${target}`;
      buttons.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
    }));
  }

  function initFloorplate() {
    const visual = document.querySelector('.oc-floorplate-visual');
    const buttons = Array.from(document.querySelectorAll('[data-fit-state]'));
    if (!visual || !buttons.length) return;
    const groups = {
      empty: visual.querySelector('.oc-fit-empty'),
      open: visual.querySelector('.oc-fit-open'),
      executive: visual.querySelector('.oc-fit-executive')
    };
    const select = (button) => {
      const state = button.dataset.fitState;
      const label = visual.querySelector('.oc-floorplate-stage-label');
      const labels = { empty: 'Typical high-zone reference · 1,847 sqm · Empty shell', open: 'Typical high-zone reference · 1,847 sqm · Open plan reference', executive: 'Typical high-zone reference · 1,847 sqm · Executive reference' };
      if (label) label.textContent = labels[state] || labels.empty;
      visual.dataset.fitState = state;
      buttons.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      Object.entries(groups).forEach(([key, group]) => {
        if (group) group.style.opacity = key === state ? '1' : '0';
      });
    };
    buttons.forEach((button) => button.addEventListener('click', () => select(button)));
  }

  function floorRows() {
    const rows = [];
    for (let level = 37; level >= 1; level -= 1) {
      const zone = level >= 21 ? 'High zone' : level >= 7 ? 'Low zone' : 'Podium / arrival';
      const state = level === 24 ? 'reference' : level <= 6 ? 'technical' : 'on-request';
      rows.push({ level: `L${level}`, zone, state });
    }
    for (let basement = 1; basement <= 3; basement += 1) rows.push({ level: `B${basement}`, zone: 'Technical / basement', state: 'technical' });
    return rows;
  }

  function initStack() {
    const root = document.querySelector('[data-office-stack]');
    if (!root) return;
    const rows = floorRows();
    root.innerHTML = `<div class="oc-stack-table"><div class="oc-stack-table-head"><span>Tower 01</span><span>Zone</span><span>Tower 02</span></div>${rows.map((row) => {
      const label = row.state === 'reference' ? 'Reference plan' : row.state === 'technical' ? 'Technical' : 'Area on request';
      const stateClass = `is-${row.state}`;
      return `<div class="oc-stack-row"><button type="button" class="oc-stack-floor ${stateClass}" data-stack-tower="Tower 01" data-stack-level="${row.level}" data-stack-zone="${row.zone}" data-stack-state="${row.state}"><strong>${row.level}</strong><small>${label}</small></button><span class="oc-stack-zone">${row.zone}</span><button type="button" class="oc-stack-floor ${stateClass}" data-stack-tower="Tower 02" data-stack-level="${row.level}" data-stack-zone="${row.zone}" data-stack-state="${row.state}"><strong>${row.level}</strong><small>${label}</small></button></div>`;
    }).join('')}</div>`;

    const buttons = Array.from(root.querySelectorAll('[data-stack-tower]'));
    const detail = {
      kicker: document.querySelector('[data-office-detail-kicker]'),
      area: document.querySelector('[data-office-detail-area]'),
      zone: document.querySelector('[data-office-detail-zone]'),
      capacity: document.querySelector('[data-office-detail-capacity]'),
      view: document.querySelector('[data-office-detail-view]')
    };
    const select = (button) => {
      buttons.forEach((item) => item.classList.toggle('is-active', item === button));
      const level = button.dataset.stackLevel;
      const isReference = button.dataset.stackState === 'reference';
      if (detail.kicker) detail.kicker.textContent = `${button.dataset.stackTower} · ${level}`;
      if (detail.area) detail.area.textContent = isReference ? '1,847 m² reference plan' : 'Area on request';
      if (detail.zone) detail.zone.textContent = button.dataset.stackZone;
      if (detail.capacity) detail.capacity.textContent = isReference ? '184 people' : 'Planning reference';
      if (detail.view) detail.view.textContent = isReference ? 'Orientation on request' : 'View on request';
    };
    buttons.forEach((button) => button.addEventListener('click', () => select(button)));
    const first = root.querySelector('[data-stack-tower="Tower 01"][data-stack-level="L24"]') || buttons[0];
    if (first) select(first);
  }

  function initViews() {
    const buttons = Array.from(document.querySelectorAll('[data-view-direction]'));
    const image = document.querySelector('.oc-views > img');
    if (!buttons.length || !image) return;
    const images = {
      north: ['assets/images/official/location-hero.jpg', 'Panoramic Hanoi skyline and West Lake view from Capital Place'],
      east: ['assets/images/official/capital-place-towers.jpg', 'Capital Place towers and eastern Hanoi skyline'],
      south: ['assets/images/official/office-hero.jpg', 'Capital Place workplace view toward Hanoi'],
      west: ['assets/images/official/location-hero.jpg', 'West Lake and Hanoi view from Capital Place']
    };
    buttons.forEach((button) => button.addEventListener('click', () => {
      buttons.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      const [src, alt] = images[button.dataset.viewDirection] || images.north;
      image.src = src;
      image.alt = alt;
    }));
  }

  function init() {
    initAnatomy();
    initFloorplate();
    initStack();
    initViews();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})(window, document);
