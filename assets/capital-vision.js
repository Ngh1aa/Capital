(function capitalVision(global, document) {
  'use strict';

  const data = global.CapitalData;
  if (!data) return;

  const escapeHtml = (value) => String(value ?? '').replace(/[&<>'"]/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
  })[character]);
  const area = (value) => Number(value).toLocaleString('en-US');

  function compactPlan(space) {
    const compact = space.floorPlanId === 'typical-low-zone';
    const outer = compact ? 'M70 68H630V382H70Z' : 'M42 54H658V396H42Z';
    const inner = compact ? 'M246 154H454V296H246Z' : 'M240 142H460V308H240Z';
    const wing = compact
      ? '<path d="M90 104H222V142H478V104H610M90 346H222V308H478V346H610" />'
      : '<path d="M66 92H214V130H486V92H634M66 358H214V320H486V358H634" />';
    return `<svg viewBox="0 0 700 450" role="img" aria-label="Illustrative ${escapeHtml(area(space.areaSqm))} square metre planning reference">
      <g fill="none" stroke="#F15F22" stroke-width="1.5"> <path d="${outer}" />${wing}<path d="${inner}" fill="#F0EFE9" />
      <path d="M270 174h42v44h-42zM329 174h42v44h-42zM388 174h42v44h-42zM278 236h64v48h-64zM358 236h64v48h-64z" />
      <path d="M92 126v190M608 126v190M112 112h94M494 112h94M112 338h94M494 338h94" stroke-dasharray="5 7" stroke-opacity=".58" /></g>
      <text x="350" y="230" text-anchor="middle" fill="#A63C12" font-size="11" letter-spacing="4" font-family="DM Sans, sans-serif">CORE</text>
      <text x="350" y="30" text-anchor="middle" fill="#A63C12" font-size="9" letter-spacing="3" font-family="DM Sans, sans-serif">NORTH</text>
    </svg>`;
  }

  function renderFloorplateShowcase() {
    const container = document.querySelector('[data-floorplate-showcase]');
    if (!container) return;
    container.innerHTML = data.spaces.map((space, index) => `<article class="floorplate-card">
      <div class="floorplate-plan">${compactPlan(space)}</div>
      <div class="floorplate-body">
        <div class="floorplate-kicker"><span>Planning reference 0${index + 1}</span><span>Both towers</span></div>
        <div class="floorplate-area">${area(space.areaSqm)} <small>m²</small></div>
        <div class="floorplate-stats">
          <div><strong>${escapeHtml(space.planningHeadcount || Math.round(space.areaSqm / 10))}</strong><span>people</span></div>
          <div><strong>${escapeHtml(space.workstations || '—')}</strong><span>workstations</span></div>
          <div><strong>${escapeHtml(space.meetingSeats || '—')}</strong><span>meeting seats</span></div>
        </div>
        <div class="floorplate-actions"><a href="space.html?id=${encodeURIComponent(space.id)}">Explore plan →</a><a href="leasing.html?intent=availability&space=${encodeURIComponent(space.id)}">Check live status</a></div>
      </div>
    </article>`).join('');
  }

  function initWorkdayGallery() {
    const gallery = document.querySelector('[data-workday-gallery]');
    if (!gallery) return;
    const image = gallery.querySelector('[data-workday-image]');
    const title = gallery.querySelector('[data-workday-title]');
    const copy = gallery.querySelector('[data-workday-copy]');
    const count = gallery.querySelector('[data-workday-count]');
    const tabs = Array.from(gallery.querySelectorAll('[data-gallery-index]'));
    let activeIndex = 0;

    tabs.slice(1).forEach((tab) => {
      const preload = new Image();
      preload.src = tab.dataset.image;
    });

    function select(nextIndex, focus = false) {
      const tab = tabs[nextIndex];
      if (!tab || nextIndex === activeIndex) return;
      activeIndex = nextIndex;
      tabs.forEach((item, index) => {
        const active = index === activeIndex;
        item.classList.toggle('active', active);
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      image.classList.add('is-changing');
      global.setTimeout(() => {
        image.src = tab.dataset.image;
        image.alt = tab.dataset.alt;
        title.textContent = tab.dataset.title;
        copy.textContent = tab.dataset.copy;
        count.textContent = `${String(activeIndex + 1).padStart(2, '0')} / ${String(tabs.length).padStart(2, '0')}`;
        image.classList.remove('is-changing');
      }, 180);
      if (focus) tab.focus();
    }

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => select(index));
      tab.addEventListener('keydown', (event) => {
        if (!['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) return;
        event.preventDefault();
        const direction = ['ArrowRight', 'ArrowDown'].includes(event.key) ? 1 : -1;
        select((index + direction + tabs.length) % tabs.length, true);
      });
    });
  }

  function init() {
    renderFloorplateShowcase();
    initWorkdayGallery();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})(window, document);
