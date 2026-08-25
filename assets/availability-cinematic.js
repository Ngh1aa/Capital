(function initAvailabilityCinematic(global, document) {
  'use strict';

  const referenceSpaces = [
    { id: 'reference-1847', label: 'Reference Floor Plate A', area: 1847, capacity: 184, workstations: 156, offices: 16, mdOffices: 7, meetingSeats: 60, zone: 'High zone', fitOut: 'Condition on request', view: 'Orientation on request', floorPlan: 'typical-high-zone' },
    { id: 'reference-1240', label: 'Reference Floor Plate B', area: 1240, capacity: 110, workstations: 100, offices: 10, mdOffices: 5, meetingSeats: 24, zone: 'Low zone', fitOut: 'Condition on request', view: 'Orientation on request', floorPlan: 'typical-low-zone' }
  ];
  let selected = { tower: 'Tower 01', level: 'Level 24', spaceId: null, area: null, capacity: null, zone: 'High zone', status: 'Availability on request', view: 'Orientation on request', technical: false };
  let shortlist = [];

  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

  function floorRows() {
    const rows = [];
    for (let floor = 37; floor >= 1; floor -= 1) rows.push({ level: `L${floor}`, zone: floor >= 21 ? 'High zone' : floor >= 7 ? 'Low zone' : 'Podium / arrival', technical: floor <= 6 });
    for (let floor = 1; floor <= 3; floor += 1) rows.push({ level: `B${floor}`, zone: 'Technical / basement', technical: true });
    return rows;
  }

  function renderStack() {
    const root = $('[data-av-stack]');
    if (!root) return;
    const rows = floorRows();
    root.innerHTML = `<div class="av-stack-table"><div class="av-stack-head"><span>Tower 01</span><span>Zone</span><span>Tower 02</span></div>${rows.map((row) => {
      const state = row.technical ? 'technical' : 'request';
      const label = row.technical ? 'Technical' : 'On request';
      return `<div class="av-stack-row"><button type="button" class="av-stack-floor is-${state}" data-av-floor data-tower="Tower 01" data-level="${row.level}" data-zone="${row.zone}" data-technical="${row.technical}" aria-label="Tower 01 ${row.level}, ${label}"><strong>${row.level}</strong><small>${label}</small></button><span class="av-stack-zone">${row.zone}</span><button type="button" class="av-stack-floor is-${state}" data-av-floor data-tower="Tower 02" data-level="${row.level}" data-zone="${row.zone}" data-technical="${row.technical}" aria-label="Tower 02 ${row.level}, ${label}"><strong>${row.level}</strong><small>${label}</small></button></div>`;
    }).join('')}</div>`;
    $$('[data-av-floor]', root).forEach((button) => button.addEventListener('click', () => selectFloor(button)));
  }

  function selectFloor(button) {
    $$('[data-av-floor]').forEach((item) => item.classList.toggle('is-active', item === button));
    const isTechnical = button.dataset.technical === 'true';
    const level = button.dataset.level.replace('L', 'Level ');
    selected = { tower: button.dataset.tower, level, spaceId: `${button.dataset.tower}-${button.dataset.level}`, area: null, capacity: null, zone: button.dataset.zone, status: isTechnical ? 'Technical / podium' : 'Availability on request', view: 'Orientation on request', fitOut: 'Condition on request', technical: isTechnical };
    updateDetail();
    document.querySelector('#floor-detail')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function selectReference(space) {
    selected = { tower: 'Both Towers', level: space.label, spaceId: space.id, ...space, status: 'Availability on request' };
    updateDetail();
    renderMatches();
    document.querySelector('#floor-detail')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function updateDetail() {
    const title = $('[data-av-detail-title]');
    const status = $('[data-av-detail-status]');
    const area = $('[data-av-detail-area]');
    const capacity = $('[data-av-detail-capacity]');
    const zone = $('[data-av-detail-zone]');
    const view = $('[data-av-detail-view]');
    if (title) title.textContent = `${selected.tower} · ${selected.level}`;
    if (status) status.textContent = selected.status || 'Availability on request';
    if (area) area.textContent = selected.area ? `${selected.area.toLocaleString()} m²` : 'Area on request';
    if (capacity) capacity.textContent = selected.capacity ? `${selected.capacity} people` : 'Planning reference';
    if (zone) zone.textContent = selected.zone || 'Zone on request';
    if (view) view.textContent = selected.view || 'Orientation on request';
    const book = $('[data-av-book]');
    const plans = $('[data-av-plans]');
    const query = encodeURIComponent(`${selected.tower} · ${selected.level}${selected.area ? ` · ${selected.area.toLocaleString()} m²` : ''}`);
    if (book) book.href = `leasing.html?intent=viewing&space=${query}`;
    if (plans) plans.href = `leasing.html?intent=technical-package&space=${query}`;
    const save = $('[data-av-save]');
    if (save) {
      const saved = selected.spaceId && shortlist.some((item) => (item.id || item.spaceId) === selected.spaceId);
      const unavailable = selected.technical;
      save.disabled = Boolean(unavailable);
      save.textContent = unavailable ? 'Technical level' : saved ? '✓ Space saved' : '♡ Save Space';
      save.setAttribute('aria-pressed', String(Boolean(saved)));
      save.classList.toggle('is-saved', Boolean(saved));
    }
  }

  function matchingSpaces() {
    const mode = $('[data-av-mode].is-active')?.dataset.avMode || 'area';
    const area = $('[data-av-area]')?.value || 'any';
    const headcount = Number($('#av-headcount')?.value || 0);
    return referenceSpaces.filter((space) => {
      if (mode === 'headcount' && headcount && space.capacity < headcount) return false;
      if (mode === 'area' && area !== 'any') {
        if (area === 'lt500' && space.area >= 500) return false;
        if (area === '500-1000' && (space.area < 500 || space.area > 1000)) return false;
        if (area === '1000-2000' && (space.area < 1000 || space.area > 2000)) return false;
        if (area === '2000plus' && space.area < 2000) return false;
      }
      return true;
    });
  }

  function renderMatches() {
    const root = $('[data-av-match-list]');
    if (!root) return;
    const spaces = matchingSpaces();
    const summary = $('[data-av-match-summary]');
    if (summary) summary.textContent = `${spaces.length} reference floor plate type${spaces.length === 1 ? '' : 's'} match this planning view. Exact vacant floors are confirmed by Leasing.`;
    root.innerHTML = spaces.length ? spaces.map((space) => {
      const isSelected = selected.spaceId === space.id;
      const isSaved = shortlist.some((item) => item.id === space.id);
      return `<article class="av-match-card${isSelected ? ' is-selected' : ''}" data-av-match-card="${space.id}"><span class="av-match-label">${space.label}</span><h3>Typical<br /><em>reference.</em></h3><strong class="av-match-area">${space.area.toLocaleString()} m²</strong><div class="av-match-meta"><span>~${space.capacity} people</span><span>${space.zone}</span><span>On request</span></div><p class="av-match-disclosure">Published planning reference. Availability, divisibility and handover timing are confirmed by Leasing.</p><div class="av-match-actions"><button type="button" data-av-view-reference="${space.id}">View floor</button><button type="button" data-av-save-reference="${space.id}">${isSaved ? '✓ Saved' : '♡ Save Space'}</button></div></article>`;
    }).join('') : '<div class="av-match-card"><h3>No reference match.</h3><p class="av-match-disclosure">Ask Leasing to review your requirement and return the current floor schedule.</p></div>';
    $$('[data-av-view-reference]', root).forEach((button) => button.addEventListener('click', () => selectReference(referenceSpaces.find((space) => space.id === button.dataset.avViewReference))));
    $$('[data-av-save-reference]', root).forEach((button) => button.addEventListener('click', () => { const space = referenceSpaces.find((item) => item.id === button.dataset.avSaveReference); if (space) toggleSave(space); }));
  }

  function updateEstimate() {
    const mode = $('[data-av-mode].is-active')?.dataset.avMode || 'area';
    const estimate = $('[data-av-estimate]');
    if (!estimate) return;
    if (mode === 'headcount') {
      const count = Number($('#av-headcount')?.value || 0);
      estimate.hidden = !count;
      estimate.innerHTML = count ? `<strong>Suggested planning range</strong><br />≈ ${Math.round(count * 10).toLocaleString()}–${Math.round(count * 12.5).toLocaleString()} m²<small>Planning estimate only, based on reference workplace ratios.</small>` : '';
    } else estimate.hidden = true;
  }

  function applyFilters() {
    const mode = $('[data-av-mode].is-active')?.dataset.avMode || 'area';
    const area = $('[data-av-area]')?.value || 'any';
    const headcount = Number($('#av-headcount')?.value || 0);
    const tower = $('#av-tower')?.value || 'all';
    $$('[data-av-floor]').forEach((floor) => {
      const isTechnical = floor.dataset.technical === 'true';
      const towerMatch = tower === 'all' || floor.dataset.tower === `Tower 0${tower}`;
      const requirementMatch = mode === 'area' ? area === 'any' || area === '1000-2000' || area === 'any' : !headcount || headcount <= 184;
      const match = !isTechnical && towerMatch && requirementMatch;
      floor.classList.toggle('is-dimmed', !match);
      floor.classList.toggle('is-match', match && !isTechnical);
    });
    renderMatches();
    updateEstimate();
  }

  function loadShortlist() {
    try { shortlist = JSON.parse(global.localStorage.getItem('capitalShortlist') || '[]'); } catch (error) { shortlist = []; }
  }

  function saveShortlist() { global.localStorage.setItem('capitalShortlist', JSON.stringify(shortlist)); }

  function toggleSave(space) {
    const id = space?.id || space?.spaceId;
    if (!id || space.technical) return;
    const index = shortlist.findIndex((item) => (item.id || item.spaceId) === id);
    if (index >= 0) shortlist.splice(index, 1);
    else if (shortlist.length < 2) shortlist.push({ ...space, id });
    saveShortlist();
    renderMatches(); updateDetail(); renderCompare();
  }

  function renderCompare() {
    const empty = $('[data-av-compare-empty]');
    const table = $('[data-av-compare-table]');
    const columns = $('[data-av-compare-columns]');
    const count = $('[data-av-compare-count]');
    if (!empty || !table || !columns) return;
    empty.hidden = shortlist.length > 0;
    table.hidden = shortlist.length === 0;
    if (count) count.textContent = `${shortlist.length} saved`;
    columns.innerHTML = shortlist.map((space) => {
      const title = space.label || `${space.tower} · ${space.level}`;
      const area = space.area ? `${space.area.toLocaleString()} m²` : 'Area on request';
      const capacity = space.capacity ? `${space.capacity} people` : 'Planning package';
      const workstations = space.workstations ? `${space.workstations}` : 'Confirmed with Leasing';
      return `<div class="av-compare-column"><strong>${area}</strong><h3>${title}</h3><span>Capacity · ${capacity}</span><span>Zone · ${space.zone || 'On request'}</span><span>Workstations · ${workstations}</span><span>Fit-out · ${space.fitOut || 'Condition on request'}</span><span>View · ${space.view || 'Orientation on request'}</span><span>Status · ${space.status || 'Availability on request'}</span></div>`;
    }).join('');
    const book = $('[data-av-compare-book]');
    if (book) {
      const context = shortlist.map((space) => space.label || `${space.tower} · ${space.level}`).join(' + ');
      book.href = `leasing.html?intent=viewing&space=${encodeURIComponent(context)}`;
    }
  }

  function initViews() {
    const buttons = $$('[data-av-view-direction]');
    const image = $('[data-av-view-image]');
    const copy = $('[data-av-view-copy]');
    if (!buttons.length || !image) return;
    const views = {
      north: ['assets/images/official/location-hero.jpg', 'Panoramic Hanoi skyline and West Lake view from Capital Place', 'Orientation is confirmed with the final floor and test-fit package.'],
      east: ['assets/images/official/capital-place-towers.jpg', 'Capital Place towers and eastern Hanoi skyline', 'East-facing outlook is confirmed with the final floor and test-fit package.'],
      south: ['assets/images/official/office-hero.jpg', 'Capital Place workplace view toward Hanoi', 'South-facing outlook is confirmed with the final floor and test-fit package.'],
      west: ['assets/images/official/location-hero.jpg', 'West Lake and Hanoi view from Capital Place', 'West-facing outlook is confirmed with the final floor and test-fit package.']
    };
    buttons.forEach((button) => button.addEventListener('click', () => {
      buttons.forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      const [src, alt, text] = views[button.dataset.avViewDirection] || views.north;
      image.src = src; image.alt = alt; if (copy) copy.textContent = text;
    }));
  }

  function init() {
    loadShortlist();
    renderStack();
    renderMatches();
    renderCompare();
    updateDetail();
    initViews();
    $$('[data-av-mode]').forEach((button) => button.addEventListener('click', () => {
      $$('[data-av-mode]').forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      const headcountField = $('[data-av-headcount-field]'); const areaField = $('[data-av-area-field]');
      if (headcountField) headcountField.hidden = button.dataset.avMode !== 'headcount';
      if (areaField) areaField.hidden = button.dataset.avMode === 'headcount';
      applyFilters();
    }));
    $$('[data-av-apply]').forEach((button) => button.addEventListener('click', applyFilters));
    $$('#av-headcount,#av-headcount,#av-area,#av-timing,#av-tower,#av-fitout').forEach((field) => field.addEventListener('input', () => { updateEstimate(); applyFilters(); }));
    $$('[data-av-plan]').forEach((button) => button.addEventListener('click', () => {
      $$('[data-av-plan]').forEach((item) => { const active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); });
      const empty = $('[data-av-plan-empty]'); const testfit = $('[data-av-plan-testfit]');
      if (empty) empty.style.opacity = button.dataset.avPlan === 'empty' ? '1' : '0';
      if (testfit) testfit.style.opacity = button.dataset.avPlan === 'testfit' ? '1' : '0';
    }));
    $('[data-av-save]')?.addEventListener('click', () => { if (selected.spaceId && !selected.technical) toggleSave(selected); });
    $('[data-av-clear]')?.addEventListener('click', () => { shortlist = []; saveShortlist(); renderMatches(); renderCompare(); updateDetail(); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})(window, document);
