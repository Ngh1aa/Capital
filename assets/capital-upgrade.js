(function capitalExperience(global, document) {
  'use strict';

  const data = global.CapitalData;
  if (!data) return;

  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));
  const params = new URLSearchParams(global.location.search);

  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>'"]/g, (character) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
    })[character]);
  }

  function formatArea(value) {
    return `${Number(value).toLocaleString('en-US')} m²`;
  }

  function getSpace(id) {
    return data.spaces.find((space) => space.id === id) || null;
  }

  function getStatus(space) {
    return data.statusMeta[space.status] || data.statusMeta['on-request'];
  }

  function capacityFor(space) {
    return {
      indicative: space.planningHeadcount || Math.max(1, Math.round(space.areaSqm / 10)),
      rangeLow: Math.max(1, Math.floor(space.areaSqm / 12)),
      rangeHigh: Math.max(1, Math.floor(space.areaSqm / 10))
    };
  }

  function track(eventName, detail = {}) {
    const safeDetail = Object.fromEntries(
      Object.entries(detail).filter(([key]) => !['name', 'email', 'phone', 'company', 'message'].includes(key))
    );
    global.dataLayer = global.dataLayer || [];
    global.dataLayer.push({ event: eventName, ...safeDetail });
    document.dispatchEvent(new CustomEvent('capital:analytics', { detail: { event: eventName, ...safeDetail } }));
  }
  global.capitalTrack = track;

  function hydrateFacts() {
    const values = {
      name: data.facts.name,
      address: data.facts.address,
      'address-short': data.facts.addressShort,
      'leasable-area': data.facts.leasableAreaLabel,
      towers: String(data.facts.towers),
      storeys: String(data.facts.storeysPerTower),
      grade: data.facts.grade,
      certifications: data.facts.certifications,
      hotline: data.facts.hotline,
      email: data.facts.leasingEmail
    };
    $$('[data-building-fact]').forEach((element) => {
      const value = values[element.dataset.buildingFact];
      if (value) element.textContent = value;
    });
    $$('[data-contact="phone"]').forEach((element) => {
      element.textContent = data.facts.hotline;
      if (element.tagName === 'A') element.href = data.facts.hotlineHref;
    });
    $$('[data-contact="email"]').forEach((element) => {
      element.textContent = data.facts.leasingEmail;
      if (element.tagName === 'A') element.href = data.facts.leasingEmailHref;
    });
  }

  function addSkipLink() {
    if ($('.skip-link') || !$('main')) return;
    const link = document.createElement('a');
    link.className = 'skip-link';
    link.href = '#main-content';
    link.textContent = 'Skip to content';
    document.body.prepend(link);
    $('main').id = $('main').id || 'main-content';
  }

  function availabilityRow(space) {
    const status = getStatus(space);
    const detailHref = status.actionable ? `space.html?id=${encodeURIComponent(space.id)}` : 'availability.html';
    const leasingHref = `leasing.html?intent=availability&space=${encodeURIComponent(space.id)}`;
    const capacity = space.planningHeadcount || Math.max(1, Math.round(space.areaSqm / 10));
    return `<article class="availability-card" data-status="${escapeHtml(space.status)}" data-space-id="${escapeHtml(space.id)}">
      <div class="availability-plan">${planSvg(space)}</div>
      <div class="availability-card-body">
        <div class="availability-card-kicker"><span>${escapeHtml(space.floor)}</span><span>${escapeHtml(space.tower)}</span></div>
        <div class="availability-card-area">${Number(space.areaSqm).toLocaleString('en-US')} <small>m²</small></div>
        <span class="availability-card-status">${escapeHtml(status.label)}</span>
        <div class="availability-card-stats">
          <div><strong>${escapeHtml(capacity)}</strong><span>planning headcount</span></div>
          <div><strong>${escapeHtml(space.workstations || '—')}</strong><span>workstations</span></div>
          <div><strong>${escapeHtml(space.meetingSeats || '—')}</strong><span>meeting seats</span></div>
        </div>
        <div class="availability-card-actions"><a href="${detailHref}" data-space-link="${escapeHtml(space.id)}">Explore floor plate →</a><a href="${leasingHref}">Check live status</a></div>
      </div>
    </article>`;
  }

  function renderAvailability(container, spaces, options = {}) {
    if (!container) return;
    if (!spaces.length) {
      container.innerHTML = `<div class="ux-empty"><h3>No reference floor plate matches exactly.</h3><p>Share your requirement and the leasing team can identify a current option, divisibility strategy or future opportunity.</p><div class="ux-actions"><a class="btn-accent" href="leasing.html?intent=future-availability">Register Your Requirement</a><a class="btn-outline-accent" href="leasing.html?intent=office">Talk to Leasing</a></div></div>`;
      return;
    }
    const prefix = options.heading ? `<p class="availability-count">${escapeHtml(options.heading)}</p>` : '';
    container.innerHTML = prefix + `<div class="availability-list">${spaces.map(availabilityRow).join('')}</div>`;
    $$('[data-space-link]', container).forEach((link) => link.addEventListener('click', () => {
      track('view_space', { spaceId: link.dataset.spaceLink, sourcePage: global.location.pathname });
    }));
  }

  function areaBounds(value) {
    const ranges = {
      lt500: [0, 500],
      '500-1000': [500, 1000],
      '1000-2000': [1000, 2000],
      '2000plus': [2000, Number.POSITIVE_INFINITY],
      unsure: [0, Number.POSITIVE_INFINITY],
      all: [0, Number.POSITIVE_INFINITY]
    };
    return ranges[value] || ranges.all;
  }

  function spaceCanFit(space, bounds) {
    const [requiredMin, requiredMax] = bounds;
    if (requiredMin === 0 && !Number.isFinite(requiredMax)) return true;
    const smallestOffer = space.divisible ? space.minimumAreaSqm : space.areaSqm;
    return space.areaSqm >= requiredMin && smallestOffer <= requiredMax;
  }

  function statusMatchesTimeline(status, timeline) {
    if (!timeline || timeline === 'all' || timeline === 'planning') return true;
    const accepted = {
      immediate: ['available', 'on-request'],
      '0-3': ['available', 'available-soon', 'on-request'],
      '3-6': ['available', 'available-soon', 'under-offer', 'on-request'],
      '6-12': ['available', 'available-soon', 'future-availability', 'on-request'],
      '12plus': ['available', 'available-soon', 'future-availability', 'on-request']
    };
    return (accepted[timeline] || []).includes(status);
  }

  function initAvailabilityPage() {
    const list = $('[data-availability-list]');
    if (!list) return;
    const controls = {
      area: $('[data-filter-area]'),
      tower: $('[data-filter-tower]'),
      timeline: $('[data-filter-timeline]'),
      status: $('[data-filter-status]')
    };
    if (params.get('area') && controls.area) controls.area.value = params.get('area');
    if (params.get('tower') && controls.tower) controls.tower.value = params.get('tower');
    if (params.get('timeline') && controls.timeline) controls.timeline.value = params.get('timeline');
    if (params.get('status') && controls.status) controls.status.value = params.get('status');

    const update = () => {
      const filtered = data.spaces.filter((space) => {
        const towerOk = !controls.tower?.value || controls.tower.value === 'all' || space.towerNumber === 0 || String(space.towerNumber) === controls.tower.value;
        const statusOk = !controls.status?.value || controls.status.value === 'all' || space.status === controls.status.value;
        const areaOk = spaceCanFit(space, areaBounds(controls.area?.value || 'all'));
        const timelineOk = statusMatchesTimeline(space.status, controls.timeline?.value || 'all');
        return towerOk && statusOk && areaOk && timelineOk;
      }).sort((a, b) => getStatus(a).order - getStatus(b).order || a.areaSqm - b.areaSqm);
      renderAvailability(list, filtered);
      const count = $('[data-availability-count]');
      if (count) count.textContent = `${filtered.length} ${filtered.length === 1 ? 'reference floor plate' : 'reference floor plates'} shown`;
    };
    Object.values(controls).filter(Boolean).forEach((control) => control.addEventListener('change', update));
    update();
    track('view_availability', { sourcePage: global.location.pathname });
  }

  function finderCandidates(requirement) {
    const active = data.spaces.filter((space) => space.status !== 'leased');
    const exact = active.filter((space) => {
      const towerOk = requirement.tower === 'all' || space.towerNumber === 0 || String(space.towerNumber) === requirement.tower;
      return towerOk && statusMatchesTimeline(space.status, requirement.timeline) && spaceCanFit(space, requirement.bounds);
    });
    if (exact.length) return { exact: true, spaces: exact.sort((a, b) => getStatus(a).order - getStatus(b).order || a.areaSqm - b.areaSqm) };
    const target = requirement.bounds[0] || (Number.isFinite(requirement.bounds[1]) ? requirement.bounds[1] : 1000);
    const closest = active
      .filter((space) => requirement.tower === 'all' || space.towerNumber === 0 || String(space.towerNumber) === requirement.tower)
      .sort((a, b) => Math.abs(a.areaSqm - target) - Math.abs(b.areaSqm - target))
      .slice(0, 3);
    return { exact: false, spaces: closest };
  }

  function initSpaceFinder() {
    $$('[data-space-finder]').forEach((finder) => {
      const modeButtons = $$('[data-finder-mode]', finder);
      const areaField = $('[data-finder-area-field]', finder);
      const headcountField = $('[data-finder-headcount-field]', finder);
      const estimate = $('[data-finder-estimate]', finder);
      const results = $('[data-finder-results]', finder);
      const form = $('form', finder);
      let mode = params.get('mode') === 'headcount' ? 'headcount' : 'area';

      const setMode = (nextMode) => {
        mode = nextMode;
        modeButtons.forEach((button) => {
          const active = button.dataset.finderMode === mode;
          button.classList.toggle('active', active);
          button.setAttribute('aria-pressed', active ? 'true' : 'false');
        });
        if (areaField) areaField.hidden = mode !== 'area';
        if (headcountField) headcountField.hidden = mode !== 'headcount';
        if (estimate) estimate.hidden = mode !== 'headcount';
      };

      modeButtons.forEach((button) => button.addEventListener('click', () => setMode(button.dataset.finderMode)));
      setMode(mode);

      const teamInput = $('[name="teamSize"]', finder);
      const updateEstimate = () => {
        if (!estimate) return;
        const team = Math.max(0, Number(teamInput?.value || 0));
        estimate.innerHTML = team
          ? `Estimated requirement: ${formatArea(team * 10)}–${formatArea(team * 12)}<small>Indicative only. Final requirement depends on workplace strategy, design and regulations.</small>`
          : 'Enter your team size to see an indicative area range.<small>We use 10–12 m² per person for early planning only.</small>';
      };
      teamInput?.addEventListener('input', updateEstimate);
      updateEstimate();

      form?.addEventListener('submit', (event) => {
        event.preventDefault();
        const area = $('[name="requiredArea"]', finder)?.value || 'unsure';
        const team = Math.max(0, Number(teamInput?.value || 0));
        if (mode === 'headcount' && !team) {
          teamInput?.focus();
          teamInput?.setAttribute('aria-invalid', 'true');
          return;
        }
        teamInput?.removeAttribute('aria-invalid');
        const requirement = {
          mode,
          area,
          team,
          bounds: mode === 'headcount' ? [team * 10, team * 12] : areaBounds(area),
          timeline: $('[name="timeline"]', finder)?.value || 'planning',
          tower: $('[name="tower"]', finder)?.value || 'all'
        };
        const result = finderCandidates(requirement);
        results.hidden = false;
        renderAvailability(results, result.spaces, {
          heading: result.exact
            ? `${result.spaces.length} ${result.spaces.length === 1 ? 'reference floor plate fits' : 'reference floor plates fit'} your requirement`
            : 'No exact match · closest reference floor plates'
        });
        if (!result.exact) {
          results.insertAdjacentHTML('beforeend', '<div class="ux-actions"><a class="btn-accent" href="leasing.html?intent=future-availability">Register Future Interest</a><a class="btn-outline-accent" href="leasing.html?intent=office">Talk to Leasing</a></div>');
        }
        results.scrollIntoView({ behavior: global.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
        track('complete_space_finder', { mode, area, teamSizeBand: team ? `${Math.floor(team / 50) * 50}+` : '', timeline: requirement.timeline, tower: requirement.tower, exactMatch: result.exact });
      });
      track('start_space_finder', { sourcePage: global.location.pathname });
    });
  }

  function hydrateStackingPlan() {
    const stack = $('.stack-shell');
    if (!stack) return;
    const map = new Map(data.spaces.map((space) => [`${space.towerNumber}-${space.floorNumber}`, space]));
    $$('.stack-floor', stack).forEach((button) => {
      const tower = button.classList.contains('stack-floor-one') ? 1 : 2;
      const floor = Number.parseInt(button.dataset.level, 10);
      if (!floor) return;
      const space = map.get(`${tower}-${floor}`);
      button.removeAttribute('onclick');
      if (space) {
        const status = getStatus(space);
        button.dataset.availabilityStatus = space.status;
        button.setAttribute('aria-label', `${space.tower} ${space.floor}, ${formatArea(space.areaSqm)}, ${status.label}`);
        button.title = `${formatArea(space.areaSqm)} · ${status.label}`;
        button.addEventListener('click', () => {
          track('select_floor', { spaceId: space.id, tower: space.towerNumber, floor: space.floorNumber });
          global.location.href = status.actionable ? `space.html?id=${encodeURIComponent(space.id)}` : 'availability.html';
        });
      } else {
        button.dataset.availabilityStatus = 'on-request';
        button.title = 'Commercial status on request';
        button.addEventListener('click', () => {
          const reference = `Tower ${String(tower).padStart(2, '0')} · Level ${floor}`;
          global.location.href = `leasing.html?intent=availability&reference=${encodeURIComponent(reference)}`;
        });
      }
    });
    if (!$('.stack-legend', stack.parentElement)) {
      stack.insertAdjacentHTML('afterend', '<div class="stack-legend" aria-label="Availability legend"><span>Available / Soon</span><span>Under Offer / Future</span><span>On Request</span><span>Leased</span></div>');
    }
    if (!$('.mobile-stack-list', stack.parentElement)) {
      const groups = [1, 2].map((tower) => {
        const rows = data.spaces.filter((space) => space.towerNumber === tower).sort((a, b) => b.floorNumber - a.floorNumber).map((space) => `<div class="mobile-stack-space"><a href="space.html?id=${encodeURIComponent(space.id)}">${escapeHtml(space.floor)} · ${formatArea(space.areaSqm)}</a><span>${escapeHtml(getStatus(space).label)}</span></div>`).join('');
        return `<div class="mobile-stack-tower"><h3>Tower 0${tower}</h3>${rows}</div>`;
      }).join('');
      stack.insertAdjacentHTML('afterend', `<div class="mobile-stack-list">${groups}</div>`);
    }
  }

  function syncOfficeExplorer() {
    const card = $('#floor-detail-card');
    if (!card) return;
    const selected = $('.floor-option.active');
    const towerButton = $('[data-explorer-tower].active');
    if (!selected || !towerButton) return;
    const towerNumber = towerButton.dataset.explorerTower.endsWith('02') ? 2 : 1;
    const floorNumber = Number.parseInt(selected.dataset.level.replace(/\D/g, ''), 10);
    const space = data.spaces.find((item) => item.towerNumber === towerNumber && item.floorNumber === floorNumber);
    const kicker = $('[data-floor-detail-kicker]', card);
    const area = $('[data-floor-detail-area]', card);
    const meta = $('.floor-detail-meta', card);
    const cta = $('a', card);
    if (!space) {
      if (kicker) kicker.textContent = `Tower 0${towerNumber} · Level ${floorNumber}`;
      if (area) area.textContent = 'Commercial status on request';
      if (meta) meta.innerHTML = '<div class="floor-meta-item"><span class="floor-meta-key">Availability</span><span class="floor-meta-value">On Request</span></div><div class="floor-meta-item"><span class="floor-meta-key">Detailed Plan</span><span class="floor-meta-value">Through Leasing</span></div>';
      if (cta) {
        cta.href = `leasing.html?intent=availability&reference=${encodeURIComponent(`Tower 0${towerNumber} · Level ${floorNumber}`)}`;
        cta.textContent = 'Ask About This Floor →';
      }
      return;
    }
    const status = getStatus(space);
    const capacity = capacityFor(space);
    if (kicker) kicker.textContent = `${space.tower} · ${space.floor}`;
    if (area) area.textContent = formatArea(space.areaSqm);
    if (meta) meta.innerHTML = `
      <div class="floor-meta-item"><span class="floor-meta-key">Availability</span><span class="floor-meta-value">${escapeHtml(status.label)}</span></div>
      <div class="floor-meta-item"><span class="floor-meta-key">Indicative Capacity</span><span class="floor-meta-value">~${capacity.indicative} people</span></div>
      <div class="floor-meta-item"><span class="floor-meta-key">Divisibility</span><span class="floor-meta-value">${space.divisible ? `From ${formatArea(space.minimumAreaSqm)}` : 'Full floor'}</span></div>
      <div class="floor-meta-item"><span class="floor-meta-key">Fit-out</span><span class="floor-meta-value">${escapeHtml(space.fitOutStatus)}</span></div>`;
    if (cta) {
      cta.href = status.actionable ? `space.html?id=${encodeURIComponent(space.id)}` : 'availability.html';
      cta.textContent = status.actionable ? 'View Floor Detail →' : 'View Other Opportunities →';
    }
  }

  function initOfficeExplorer() {
    if (!$('#floor-detail-card')) return;
    $$('.floor-option,[data-explorer-tower],[data-explorer-zone]').forEach((button) => button.addEventListener('click', () => global.setTimeout(syncOfficeExplorer, 0)));
    syncOfficeExplorer();
  }

  function planSvg(space) {
    const label = `${space.tower} · ${space.floor}`;
    return `<svg viewBox="0 0 760 500" role="img" aria-label="Illustrative planning diagram for ${escapeHtml(label)}">
      <rect x="35" y="35" width="690" height="430" fill="none" stroke="#F15F22" stroke-width="2"/>
      <rect x="285" y="155" width="190" height="190" fill="#D9D9D9" stroke="#F15F22" stroke-width="1.5"/>
      <rect x="310" y="180" width="42" height="55" fill="none" stroke="#F15F22"/><rect x="360" y="180" width="42" height="55" fill="none" stroke="#F15F22"/><rect x="410" y="180" width="42" height="55" fill="none" stroke="#F15F22"/>
      <rect x="310" y="250" width="60" height="62" fill="none" stroke="#F15F22"/><rect x="390" y="250" width="62" height="62" fill="none" stroke="#F15F22"/>
      <path d="M55 70H265V135H495V70H705M55 430H270V365H490V430H705" fill="none" stroke="#F15F22" stroke-width="1" stroke-dasharray="6 7"/>
      <path d="M70 90v320M690 90v320" stroke="#F15F22" stroke-width="1" stroke-dasharray="6 7"/>
      <text x="380" y="252" text-anchor="middle" fill="#F15F22" font-size="12" letter-spacing="4" font-family="sans-serif">CORE</text>
      <text x="380" y="22" text-anchor="middle" fill="#F15F22" font-size="11" letter-spacing="3" font-family="sans-serif">N</text>
      <text x="380" y="488" text-anchor="middle" fill="#F15F22" font-size="10" letter-spacing="2" font-family="sans-serif">PLANNING DIAGRAM · NOT FOR CONSTRUCTION</text>
      <line x1="650" y1="70" x2="650" y2="25" stroke="#F15F22"/><polygon points="650,16 644,29 656,29" fill="#F15F22"/>
    </svg>`;
  }

  function initSpacePage() {
    const page = $('[data-space-page]');
    if (!page) return;
    const id = params.get('id');
    const space = getSpace(id);
    const valid = $('[data-space-valid]', page);
    const invalid = $('[data-space-invalid]', page);
    if (!space) {
      if (valid) valid.hidden = true;
      if (invalid) invalid.hidden = false;
      document.title = 'Opportunity Not Available – Capital Place Hanoi';
      return;
    }
    const status = getStatus(space);
    const capacity = capacityFor(space);
    if (valid) valid.hidden = false;
    if (invalid) invalid.hidden = true;
    document.title = `${space.tower} ${space.floor} – Capital Place Hanoi`;
    const description = `${formatArea(space.areaSqm)} office opportunity at Capital Place Hanoi. ${status.label}; current terms confirmed by leasing.`;
    $('meta[name="description"]')?.setAttribute('content', description);
    $$('[data-space-field="tower-floor"]', page).forEach((element) => { element.textContent = `${space.tower} · ${space.floor}`; });
    $$('[data-space-field="area"]', page).forEach((element) => { element.textContent = formatArea(space.areaSqm); });
    $$('[data-space-field="status"]', page).forEach((element) => { element.textContent = status.label; });
    $$('[data-space-field="timing"]', page).forEach((element) => { element.textContent = space.availableFrom; });
    $$('[data-space-field="fitout"]', page).forEach((element) => { element.textContent = space.fitOutStatus; });
    $$('[data-space-field="divisibility"]', page).forEach((element) => { element.textContent = space.divisible ? `Subject to confirmation · from ${formatArea(space.minimumAreaSqm)}` : 'Full floor'; });
    $$('[data-space-field="view"]', page).forEach((element) => { element.textContent = space.viewDirection; });
    $$('[data-space-field="capacity"]', page).forEach((element) => { element.textContent = `~${capacity.indicative}`; });
    $$('[data-space-field="capacity-range"]', page).forEach((element) => { element.textContent = `${capacity.rangeLow}–${capacity.rangeHigh}`; });
    const plan = $('[data-space-plan]', page);
    if (plan) plan.innerHTML = planSvg(space);
    $$('[data-space-action="viewing"]', page).forEach((link) => {
      link.href = `leasing.html?intent=viewing&space=${encodeURIComponent(space.id)}`;
      if (!status.actionable) {
        link.href = 'availability.html';
        link.textContent = 'View Other Opportunities';
      }
    });
    $$('[data-space-action="proposal"]', page).forEach((link) => {
      link.href = `leasing.html?intent=proposal&space=${encodeURIComponent(space.id)}`;
      if (!status.actionable) link.hidden = true;
    });
    $$('[data-space-action="plan"]', page).forEach((link) => {
      link.href = `leasing.html?intent=technical-package&space=${encodeURIComponent(space.id)}`;
      if (!status.actionable) link.hidden = true;
    });
    track('view_space', { spaceId: space.id, status: space.status, areaSqm: space.areaSqm });
  }

  function setFieldError(field, message) {
    field.setAttribute('aria-invalid', message ? 'true' : 'false');
    const error = document.getElementById(`${field.id}-error`);
    if (error) error.textContent = message;
  }

  function initLeasingForm() {
    const form = $('[data-leasing-form]');
    if (!form) return;
    const intentInput = $('[name="intent"]', form);
    const contextInput = $('[name="spaceContext"]', form);
    const contextPanel = $('[data-leasing-context]');
    const intentButtons = $$('[data-intent]');
    const success = $('[data-form-success]');
    let intent = params.get('intent') || 'office';
    const space = getSpace(params.get('space'));
    const reference = params.get('reference');

    function updateIntent(nextIntent) {
      intent = nextIntent;
      intentInput.value = intent;
      intentButtons.forEach((button) => button.classList.toggle('active', button.dataset.intent === intent));
      $$('[data-conditional]', form).forEach((group) => {
        const modes = group.dataset.conditional.split(' ');
        group.hidden = !modes.includes(intent);
        $$('[data-required-when-visible]', group).forEach((field) => { field.required = !group.hidden; });
      });
      const title = $('[data-form-title]');
      const labels = {
        office: 'Office Leasing Enquiry',
        availability: 'Request Current Availability',
        proposal: 'Request a Proposal',
        viewing: 'Request a Viewing',
        'future-availability': 'Register Future Interest',
        retail: 'Retail / F&B Enquiry',
        'technical-package': 'Request Technical Package'
      };
      if (title) title.textContent = labels[intent] || labels.office;
    }

    intentButtons.forEach((button) => button.addEventListener('click', () => updateIntent(button.dataset.intent)));
    updateIntent(intent);

    if (space || reference) {
      const value = space ? `${space.tower} · ${space.floor} · ${formatArea(space.areaSqm)}` : reference;
      contextInput.value = value;
      if (contextPanel) {
        contextPanel.hidden = false;
        $('[data-leasing-context-value]', contextPanel).textContent = value;
      }
    }

    const dateInput = $('[name="preferredDate"]', form);
    if (dateInput) {
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      dateInput.min = tomorrow.toISOString().slice(0, 10);
    }

    $$('input,select,textarea', form).forEach((field) => field.addEventListener('input', () => setFieldError(field, '')));
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      let firstInvalid = null;
      $$('input,select,textarea', form).forEach((field) => {
        if (field.closest('[hidden]')) return;
        let message = '';
        if (field.required && !field.value.trim()) message = 'This field is required.';
        else if (field.type === 'email' && field.value && !field.validity.valid) message = 'Enter a valid work email.';
        else if (field.type === 'checkbox' && field.required && !field.checked) message = 'Please confirm before continuing.';
        setFieldError(field, message);
        if (message && !firstInvalid) firstInvalid = field;
      });
      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }

      const submit = $('button[type="submit"]', form);
      submit.disabled = true;
      submit.textContent = 'Preparing Request…';
      const formData = new FormData(form);
      const subjectLabels = {
        viewing: 'Viewing request', proposal: 'Proposal request', retail: 'Retail leasing enquiry',
        'future-availability': 'Future availability interest', 'technical-package': 'Technical package request',
        availability: 'Availability request', office: 'Office leasing enquiry'
      };
      const subject = `${subjectLabels[intent] || subjectLabels.office} · Capital Place`;
      const bodyLines = [];
      for (const [key, value] of formData.entries()) {
        if (!value || ['privacyConsent'].includes(key)) continue;
        bodyLines.push(`${key}: ${value}`);
      }
      const mailto = `${data.facts.leasingEmailHref}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyLines.join('\n'))}`;
      const fallback = $('[data-email-fallback]', success);
      if (fallback) fallback.href = mailto;
      form.hidden = true;
      success.hidden = false;
      success.focus();
      track(intent === 'viewing' ? 'submit_viewing_request' : 'submit_leasing_enquiry', {
        intent,
        selectedSpaceId: space?.id || '',
        sourcePage: global.location.pathname,
        campaign: params.get('utm_campaign') || ''
      });
    });
  }

  function initResources() {
    const list = $('[data-resource-list]');
    if (!list) return;
    list.innerHTML = data.resources.map((resource) => `<article class="resource-row">
      <div><h3>${escapeHtml(resource.title)}</h3><span class="resource-access">${resource.access === 'public' ? 'Public resource' : 'Available through leasing'}</span></div>
      <p>${escapeHtml(resource.description)}</p>
      <a class="availability-link" href="${escapeHtml(resource.href)}" data-resource-id="${escapeHtml(resource.id)}">${resource.access === 'public' ? 'View Resource' : 'Request Access'} →</a>
    </article>`).join('');
    $$('[data-resource-id]', list).forEach((link) => link.addEventListener('click', () => track('resource_open', { resourceId: link.dataset.resourceId })));
  }

  function hydrateHomeSnapshot() {
    const snapshot = $('[data-home-availability]');
    if (!snapshot) return;
    [1, 2].forEach((tower) => {
      const count = data.spaces.filter((space) => space.towerNumber === tower && space.status !== 'leased').length;
      const target = $(`[data-home-tower="${tower}"]`, snapshot);
      if (target) target.textContent = `${count} indicative ${count === 1 ? 'opportunity' : 'opportunities'}`;
    });
    const active = data.spaces.filter((space) => space.status !== 'leased');
    const minimum = Math.min(...active.map((space) => space.minimumAreaSqm || space.areaSqm));
    const maximum = Math.max(...active.map((space) => space.areaSqm));
    const range = $('[data-home-area-range]', snapshot);
    if (range) range.textContent = `From ${formatArea(minimum)} to ${formatArea(maximum)}`;
  }

  function addMobileCta() {
    if ($('.mobile-leasing-cta')) return;
    const page = global.location.pathname.split('/').pop() || 'index.html';
    const map = {
      'office.html': ['Find a Space', 'availability.html#space-finder'],
      'availability.html': ['Talk to Leasing', 'leasing.html?intent=office'],
      'space.html': ['Request a Viewing', `leasing.html?intent=viewing&space=${encodeURIComponent(params.get('id') || '')}`],
      'retail.html': ['Retail Enquiry', 'leasing.html?intent=retail']
    };
    if (!map[page]) return;
    const [label, href] = map[page];
    const wrapper = document.createElement('div');
    wrapper.className = 'mobile-leasing-cta';
    wrapper.innerHTML = `<a href="${href}">${label}</a>`;
    document.body.appendChild(wrapper);
    document.body.classList.add('has-mobile-cta');
  }

  document.addEventListener('DOMContentLoaded', () => {
    hydrateFacts();
    addSkipLink();
    hydrateHomeSnapshot();
    initAvailabilityPage();
    initSpaceFinder();
    hydrateStackingPlan();
    initOfficeExplorer();
    initSpacePage();
    initLeasingForm();
    initResources();
    addMobileCta();
  });
})(window, document);
