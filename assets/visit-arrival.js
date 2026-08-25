(function visitArrival(global, document) {
  'use strict';

  const params = new URLSearchParams(global.location.search);
  const assets = 'assets/images/official/';
  const purposes = {
    meeting: {
      label: 'MEETING',
      title: 'Meet at the<br><em>right destination.</em>',
      copy: 'Liễu Giai → Main Drop-off → Grand Lobby → Reception → Host / meeting floor.',
      route: '01 · Confirm your host and floor before travelling.',
      image: assets + 'peony-meeting-room.jpg',
      alt: 'Meeting destination at Capital Place'
    },
    viewing: {
      label: 'OFFICE VIEWING',
      title: 'Find your next<br><em>office.</em>',
      copy: 'Liễu Giai → Main Drop-off → Grand Lobby → Reception → Leasing representative → Tower / floor.',
      route: '01 · Your selected space can travel with you from Availability or Leasing.',
      image: assets + 'office-hero.jpg',
      alt: 'Office viewing destination at Capital Place'
    },
    nexus: {
      label: 'THE NEXUS',
      title: 'Meet the<br><em>workday.</em>',
      copy: 'Liễu Giai → Main Drop-off → Grand Lobby → Reception → The Nexus destination.',
      route: '01 · Confirm your host and access arrangements before travelling.',
      image: assets + 'the-nexus.jpg',
      alt: 'The Nexus at Capital Place'
    },
    link: {
      label: 'THE LINK',
      title: 'Find your way<br><em>to B1.</em>',
      copy: 'Kim Mã / Lobby → pedestrian route → B1 → The Link.',
      route: '01 · The Link is located at B1; confirm current access with your host.',
      image: assets + 'the-link.jpg',
      alt: 'The Link at Capital Place'
    },
    event: {
      label: 'AN EVENT',
      title: 'Arrive for<br><em>the occasion.</em>',
      copy: 'Liễu Giai → Main Drop-off → Grand Lobby → Reception → Event host / destination.',
      route: '01 · Event access and registration are confirmed by the event host.',
      image: assets + 'lily-event-space.jpeg',
      alt: 'Event space at Capital Place'
    }
  };

  const purposeButtons = [...document.querySelectorAll('[data-visit-purpose]')];
  const purposeLabel = document.querySelector('[data-visit-purpose-result] .v-index');
  const purposeTitle = document.querySelector('[data-visit-purpose-title]');
  const purposeCopy = document.querySelector('[data-visit-purpose-copy]');
  const purposeRoute = document.querySelector('[data-visit-purpose-route]');
  const purposeImage = document.querySelector('[data-visit-purpose-image]');

  function renderPurpose(key) {
    const item = purposes[key] || purposes.meeting;
    purposeButtons.forEach((button) => {
      const active = button.dataset.visitPurpose === key;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', String(active));
    });
    if (purposeLabel) purposeLabel.textContent = item.label;
    if (purposeTitle) purposeTitle.innerHTML = item.title;
    if (purposeCopy) purposeCopy.textContent = item.copy;
    if (purposeRoute) purposeRoute.textContent = item.route;
    if (purposeImage) {
      purposeImage.src = item.image;
      purposeImage.alt = item.alt;
    }
  }
  purposeButtons.forEach((button) => button.addEventListener('click', () => renderPurpose(button.dataset.visitPurpose)));
  renderPurpose(params.get('purpose') || 'meeting');

  const towerButtons = [...document.querySelectorAll('[data-visit-tower-choice]')];
  const towerStatus = document.querySelector('[data-visit-tower-status]');
  const towerHighlights = [...document.querySelectorAll('[data-visit-tower]')];
  let selectedTower = params.get('tower') || 'tower-01';

  function readableTower(value) {
    return value === 'tower-02' || /tower\s*0?2/i.test(value) ? 'Tower 02' : 'Tower 01';
  }
  function renderTower(value) {
    selectedTower = value === 'tower-02' ? 'tower-02' : 'tower-01';
    const label = readableTower(selectedTower);
    towerButtons.forEach((button) => {
      const active = button.dataset.visitTowerChoice === selectedTower;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    towerHighlights.forEach((node) => node.classList.toggle('is-selected', node.dataset.visitTower === selectedTower));
    if (towerStatus) towerStatus.innerHTML = `Selected destination: <strong>${label}</strong><span>Confirm your floor with the host or Leasing.</span>`;
  }
  towerButtons.forEach((button) => button.addEventListener('click', () => renderTower(button.dataset.visitTowerChoice)));
  renderTower(selectedTower);

  const contextLive = document.querySelector('[data-visit-context]');
  const contextEmpty = document.querySelector('[data-visit-context-empty]');
  const contextTarget = document.querySelector('[data-visit-space]');
  const contextCopy = document.querySelector('[data-visit-context-copy]');
  const contextDate = document.querySelector('[data-visit-date]');
  const contextTime = document.querySelector('[data-visit-time]');
  const hasContext = Boolean(params.get('space') || params.get('intent') === 'viewing' || params.get('tower') || params.get('floor'));
  const space = params.get('space');
  const floor = params.get('floor');
  const displayContext = space || [params.get('tower') ? readableTower(params.get('tower')) : '', floor || ''].filter(Boolean).join(' · ') || 'Private viewing requested · confirm details with Leasing';

  if (hasContext) {
    if (contextLive) contextLive.hidden = false;
    if (contextEmpty) contextEmpty.hidden = true;
    if (contextTarget) contextTarget.textContent = displayContext;
    if (contextCopy) contextCopy.textContent = 'Your viewing route is ready to orient. Confirm the host, selected space, preferred time and building access with Leasing before travelling.';
    if (contextDate && params.get('date')) contextDate.textContent = `Preferred date · ${params.get('date')}`;
    if (contextTime && params.get('time')) contextTime.textContent = `Preferred time · ${params.get('time')}`;
  }

  const bookingLinks = [...document.querySelectorAll('[data-visit-book]')];
  bookingLinks.forEach((link) => {
    const booking = new URL('leasing.html', global.location.href);
    booking.searchParams.set('intent', 'viewing');
    ['space', 'tower', 'floor', 'date', 'time'].forEach((key) => {
      const value = params.get(key);
      if (value) booking.searchParams.set(key, value);
    });
    link.href = booking.pathname + booking.search;
  });
})(window, document);
