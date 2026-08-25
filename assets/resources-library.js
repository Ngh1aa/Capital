(function resourcesLibrary(global, document) {
  'use strict';

  const params = new URLSearchParams(global.location.search);

  const planButtons = [...document.querySelectorAll('[data-plan-view]')];
  const planStates = [...document.querySelectorAll('[data-plan-state]')];
  function renderPlan(view) {
    planButtons.forEach((button) => {
      const active = button.dataset.planView === view;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', String(active));
    });
    planStates.forEach((state) => { state.hidden = state.dataset.planState !== view; });
  }
  planButtons.forEach((button) => button.addEventListener('click', () => renderPlan(button.dataset.planView)));
  renderPlan('empty');

  const documentPanel = document.querySelector('[data-document-panel="building"]');
  const documentOpen = document.querySelector('[data-document-view="building"]');
  const documentClose = document.querySelector('[data-document-close]');
  function setDocument(open) {
    if (!documentPanel) return;
    documentPanel.hidden = !open;
    if (open) documentPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  documentOpen?.addEventListener('click', () => setDocument(true));
  documentClose?.addEventListener('click', () => { setDocument(false); documentOpen?.focus(); });

  const stackingContent = {
    high: ['Typical high zone', 'Use the published reference floor plate to discuss larger workplace planning. Current floor area and availability are confirmed by Leasing.'],
    mid: ['Typical mid zone', 'A mid-tower planning reference for early workplace evaluation. Confirm the selected floor, area and current commercial position with Leasing.'],
    low: ['Lower zone / podium', 'The lower building context connects workplace, arrival and shared podium planning. Detailed floor information remains on request.']
  };
  const stackButtons = [...document.querySelectorAll('[data-stacking-zone]')];
  const stackTitle = document.querySelector('[data-stacking-title]');
  const stackCopy = document.querySelector('[data-stacking-copy]');
  function renderStack(key) {
    const content = stackingContent[key] || stackingContent.high;
    stackButtons.forEach((button) => button.classList.toggle('is-active', button.dataset.stackingZone === key));
    if (stackTitle) stackTitle.textContent = content[0];
    if (stackCopy) stackCopy.textContent = content[1];
  }
  stackButtons.forEach((button) => button.addEventListener('click', () => renderStack(button.dataset.stackingZone)));
  renderStack('high');

  const technicalContent = {
    vertical: ['Vertical transportation', 'The brochure reference describes 32 passenger elevators across two towers. Confirm the current controlled specification before relying on this figure.', 'LIFTS', '32 passenger elevators', 'STATUS', 'Published reference · verify current'],
    floor: ['Raised floor', 'The published reference describes a 150 mm raised floor. Confirm the latest fit-out and technical revision with Leasing.', 'FLOOR', '150 mm raised floor', 'STATUS', 'Published reference · verify current'],
    power: ['Power resilience', 'The brochure reference describes 100% backup power. Confirm current operational and technical parameters through the controlled package.', 'POWER', '100% backup power reference', 'STATUS', 'Published reference · verify current'],
    facade: ['Façade + height', 'The public fit-out reference includes façade and clear-height guidance. Current design decisions require the latest issued document.', 'HEIGHT', '2.7 m clear-height reference', 'STATUS', 'Published reference · verify current']
  };
  const techButtons = [...document.querySelectorAll('[data-tech-topic]')];
  const techTitle = document.querySelector('[data-tech-title]');
  const techCopy = document.querySelector('[data-tech-copy]');
  const techLabelOne = document.querySelector('[data-tech-label-one]');
  const techValueOne = document.querySelector('[data-tech-value-one]');
  const techLabelTwo = document.querySelector('[data-tech-label-two]');
  const techValueTwo = document.querySelector('[data-tech-value-two]');
  function renderTech(key) {
    const content = technicalContent[key] || ['Technical core', 'Choose a system to see the published reference context. Request the current issued specification before design or construction decisions.', 'DEPTH', 'On request', 'STATUS', 'Controlled by Leasing'];
    techButtons.forEach((button) => button.classList.toggle('is-active', button.dataset.techTopic === key));
    if (techTitle) techTitle.textContent = content[0];
    if (techCopy) techCopy.textContent = content[1];
    if (techLabelOne) techLabelOne.textContent = content[2];
    if (techValueOne) techValueOne.textContent = content[3];
    if (techLabelTwo) techLabelTwo.textContent = content[4];
    if (techValueTwo) techValueTwo.textContent = content[5];
  }
  techButtons.forEach((button) => button.addEventListener('click', () => renderTech(button.dataset.techTopic)));
  renderTech('vertical');

  const roleContent = {
    executive: { title: 'Executive / Tenant', copy: 'Frame the building, address, workplace scale and the next leasing conversation.', links: [['Building overview', 'office.html', 'Public →'], ['Reference floor plates', 'availability.html', 'Public →'], ['Sustainability overview', 'sustainability.html', 'Public →'], ['Tailored proposal package', 'leasing.html?intent=technical-package', 'On request →']] },
    broker: { title: 'Broker', copy: 'Move from building story to reference floor plates, brochure context and a qualified Leasing conversation.', links: [['Availability route', 'availability.html', 'Public →'], ['Reference floor plans', 'office.html#floor-explorer', 'Public →'], ['Building brochure', '#building-book', 'Public →'], ['Leasing contact', 'leasing.html', 'On request →']] },
    architect: { title: 'Architect', copy: 'Start with floor plan, fit-out and specifications, then request the current controlled drawings.', links: [['Reference floor plan', '#floor-plans', 'Public →'], ['Fit-out Guidelines', '#fit-out', 'Historical →'], ['Technical core', '#technical-core', 'Summary →'], ['CAD request', 'leasing.html?intent=technical-package&reference=CAD%20drawings', 'On request →']] },
    facility: { title: 'Facility / Technical', copy: 'Review systems, resilience and fit-out context before requesting the issued technical package.', links: [['Technical core', '#technical-core', 'Summary →'], ['Fit-out Guidelines', '#fit-out', 'Verify current →'], ['Building specifications', 'office.html#office-specifications', 'Public →'], ['Detailed MEP', 'leasing.html?intent=technical-package&reference=Detailed%20MEP', 'On request →']] },
    esg: { title: 'ESG', copy: 'Review LEED credentials, published performance evidence and the route to deeper ESG documentation.', links: [['Dual LEED evidence', '#sustainability-evidence', 'Public →'], ['Sustainability overview', 'sustainability.html', 'Public →'], ['Building operations', 'office.html#office-specifications', 'Summary →'], ['ESG package', 'leasing.html?intent=technical-package&reference=ESG%20package', 'On request →']] }
  };
  const roleButtons = [...document.querySelectorAll('[data-resource-role]')];
  const roleTitle = document.querySelector('[data-role-title]');
  const roleCopy = document.querySelector('[data-role-copy]');
  const roleList = document.querySelector('[data-role-list]');
  function renderRole(key) {
    const role = roleContent[key] || roleContent.executive;
    roleButtons.forEach((button) => {
      const active = button.dataset.resourceRole === key;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', String(active));
    });
    if (roleTitle) roleTitle.textContent = role.title;
    if (roleCopy) roleCopy.textContent = role.copy;
    if (roleList) {
      roleList.replaceChildren(...role.links.map(([label, href, status]) => {
        const link = document.createElement('a');
        link.href = href;
        link.innerHTML = `${label} <span>${status}</span>`;
        return link;
      }));
    }
  }
  roleButtons.forEach((button) => button.addEventListener('click', () => renderRole(button.dataset.resourceRole)));
  renderRole(params.get('role') || 'executive');

  const packageItems = [...document.querySelectorAll('[data-package-item]')];
  const packageCount = document.querySelector('[data-package-count]');
  const packageMessage = document.querySelector('[data-package-message]');
  const packageItemsText = document.querySelector('[data-package-items]');
  const packageCta = document.querySelector('[data-package-cta]');
  function renderPackage() {
    const selected = packageItems.filter((input) => input.checked).map((input) => input.value);
    if (packageCount) packageCount.textContent = String(selected.length);
    if (packageItemsText) packageItemsText.textContent = selected.length ? selected.join(' · ') : 'No resources selected yet.';
    if (packageMessage) packageMessage.textContent = selected.length ? 'Your selection will be routed to the right public reference or controlled package through Leasing.' : 'Select one or more resources to build a useful request.';
    if (packageCta) {
      const reference = selected.join(', ');
      packageCta.href = `leasing.html?intent=technical-package&reference=${encodeURIComponent(reference || 'Capital Place resource package')}`;
      packageCta.setAttribute('aria-disabled', String(!selected.length));
      packageCta.style.pointerEvents = selected.length ? 'auto' : 'none';
      packageCta.style.opacity = selected.length ? '1' : '.5';
    }
  }
  packageItems.forEach((input) => input.addEventListener('change', renderPackage));
  renderPackage();

  const selectedSpacePanel = document.querySelector('[data-selected-space-panel]');
  const selectedSpace = document.querySelector('[data-selected-space]');
  const selectedSpaceLink = document.querySelector('[data-selected-space-link]');
  const space = params.get('space');
  const tower = params.get('tower');
  const floor = params.get('floor');
  if (space || tower || floor) {
    const label = space || [tower, floor].filter(Boolean).join(' · ') || 'Selected space';
    if (selectedSpacePanel) selectedSpacePanel.hidden = false;
    if (selectedSpace) selectedSpace.textContent = label;
    if (selectedSpaceLink) {
      const href = new URL('space.html', global.location.href);
      if (params.get('id')) href.searchParams.set('id', params.get('id'));
      if (tower) href.searchParams.set('tower', tower);
      if (floor) href.searchParams.set('floor', floor);
      selectedSpaceLink.href = href.pathname + href.search;
    }
  }
})(window, document);
