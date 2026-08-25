(function initSustainabilityCinematic(document) {
  'use strict';
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const systems = {
    facade: { name: 'Façade', copy: 'Low-E glazing helps reduce solar heat gain, supporting the building\'s cooling performance.', stat: 'Up to 69% cooling energy saved' },
    lighting: { name: 'Lighting', copy: 'Smart sensors respond to occupancy and daylight to reduce unnecessary lighting demand.', stat: '27,636 kWh saved annually' },
    hvac: { name: 'HVAC', copy: 'High-efficiency systems and intelligent monitoring help the building perform with less demand.', stat: 'Engineered for efficient operations' },
    power: { name: 'Power', copy: 'IE3 motors and active harmonic filtering support cleaner, more efficient electrical performance.', stat: '30% energy saving vs IE1 motors' },
    water: { name: 'Water', copy: 'Water reuse and responsible green-space maintenance keep resource cycles working beyond daily use.', stat: '2,000+ m³ water saved annually' },
    management: { name: 'Building management', copy: 'A building management system helps monitor and optimise energy use across the workplace.', stat: 'Performance monitored every day' }
  };

  function activateSystem(button) {
    const key = button.dataset.ssSystem;
    const system = systems[key] || systems.facade;
    const cutaway = $('.ss-cutaway');
    $$('.ss-system-list button').forEach((item) => {
      const active = item === button;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-selected', String(active));
    });
    cutaway?.classList.remove('is-facade', 'is-lighting', 'is-hvac', 'is-power', 'is-water', 'is-management');
    cutaway?.classList.add(`is-${key}`);
    const name = $('[data-ss-system-name]');
    const copy = $('[data-ss-system-copy]');
    const stat = $('[data-ss-system-stat]');
    if (name) name.textContent = system.name;
    if (copy) copy.textContent = system.copy;
    if (stat) stat.textContent = system.stat;
  }

  function init() {
    $$('.ss-system-list button').forEach((button) => button.addEventListener('click', () => activateSystem(button)));
    $$('.ss-system-list button').forEach((button, index, buttons) => button.addEventListener('keydown', (event) => {
      if (!['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      let next = index;
      if (event.key === 'ArrowDown') next = (index + 1) % buttons.length;
      if (event.key === 'ArrowUp') next = (index - 1 + buttons.length) % buttons.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = buttons.length - 1;
      buttons[next].focus();
      activateSystem(buttons[next]);
    }));
    const details = $$('.ss-data-grid details');
    details.forEach((item) => item.addEventListener('toggle', () => {
      if (!item.open) return;
      details.filter((other) => other !== item).forEach((other) => { other.open = false; });
    }));
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})(document);
