(function spacePdp(global, document) {
  'use strict';
  const page = document.querySelector('[data-space-page]');
  if (!page) return;
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const params = new URLSearchParams(global.location.search);
  const readShortlist = () => { try { return JSON.parse(global.localStorage.getItem('capitalShortlist') || '[]'); } catch (error) { return []; } };
  const writeShortlist = (items) => global.localStorage.setItem('capitalShortlist', JSON.stringify(items));
  const field = (name) => $(`[data-space-field="${name}"]`);
  const currentId = () => page.dataset.spaceId || params.get('id') || `${params.get('tower') || ''}-${params.get('floor') || ''}`;
  const currentContext = () => ({
    id: currentId(),
    tower: field('tower')?.textContent.trim() || 'Capital Place',
    floor: field('floor')?.textContent.trim() || '',
    label: field('tower-floor')?.textContent.trim() || 'Selected floor',
    area: Number((field('area')?.dataset.area || '').replace(/,/g, '')) || null,
    capacity: Number((field('capacity')?.textContent || '').replace(/\D/g, '')) || null,
    zone: field('zone')?.textContent.trim() || 'Zone on request',
    view: field('view')?.textContent.trim() || 'Orientation on request',
    fitOut: field('fitout')?.textContent.trim() || 'Condition on request',
    status: field('status')?.textContent.trim() || 'Availability on request'
  });
  function syncSaveState() {
    const button = $('[data-space-save]');
    if (!button) return;
    const items = readShortlist();
    const saved = items.some((item) => item.id === currentId());
    button.textContent = saved ? '✓ Saved to shortlist' : '♡ Save this space';
    button.setAttribute('aria-pressed', String(saved));
    button.classList.toggle('is-saved', saved);
    const count = $('[data-space-shortlist-count]');
    if (count) count.textContent = `${items.length} saved`;
  }
  function toggleSave() {
    const context = currentContext();
    if (!context.id) return;
    const items = readShortlist();
    const index = items.findIndex((item) => item.id === context.id);
    if (index >= 0) items.splice(index, 1);
    else if (items.length < 2) items.push(context);
    writeShortlist(items);
    syncSaveState();
    const note = $('[data-space-save-note]');
    if (note) { note.textContent = index >= 0 ? 'Removed from your shortlist.' : items.length > 1 ? 'Saved. Compare it with another space in Availability.' : 'Saved. Add one more space to compare.'; note.classList.add('is-visible'); global.setTimeout(() => note.classList.remove('is-visible'), 3200); }
  }
  function initViews() {
    const image = $('[data-space-view-image]');
    const caption = $('[data-space-view-caption]');
    const copy = $('[data-space-view-copy]');
    const views = {
      north: ['assets/images/official/location-hero.jpg', 'Hanoi skyline and West Lake from Capital Place', 'North-facing outlook is confirmed with the final floor and test-fit package.'],
      east: ['assets/images/official/capital-place-towers.jpg', 'Capital Place towers and eastern Hanoi skyline', 'East-facing outlook is confirmed with the final floor and test-fit package.'],
      south: ['assets/images/official/office-hero.jpg', 'Workplace interior view toward Hanoi', 'South-facing outlook is confirmed with the final floor and test-fit package.'],
      west: ['assets/images/official/location-hero.jpg', 'West Lake and western Hanoi outlook', 'West-facing outlook is confirmed with the final floor and test-fit package.']
    };
    $$('[data-space-view-direction]').forEach((button) => button.addEventListener('click', () => {
      $$('[data-space-view-direction]').forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      const [src, alt, text] = views[button.dataset.spaceViewDirection] || views.north;
      if (image) { image.src = src; image.alt = alt; }
      if (copy) copy.textContent = text;
      if (caption) caption.textContent = `${button.textContent.trim()} · orientation on request`;
    }));
  }
  function initPlan() {
    const target = $('[data-space-plan]');
    $$('[data-space-plan-mode]').forEach((button) => button.addEventListener('click', () => {
      $$('[data-space-plan-mode]').forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      if (target) target.dataset.planMode = button.dataset.spacePlanMode;
      const note = $('[data-space-plan-note]');
      if (note) note.textContent = button.dataset.spacePlanMode === 'testfit' ? 'Published workplace reference · not for construction' : 'Indicative planning diagram · not for construction';
    }));
  }
  $('[data-space-save]')?.addEventListener('click', toggleSave);
  $('[data-space-compare]')?.addEventListener('click', () => { global.location.href = 'availability.html#compare-spaces'; });
  initViews();
  initPlan();
  syncSaveState();
})(window, document);
