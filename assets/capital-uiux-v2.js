(() => {
  'use strict';
  const body = document.body;
  if (!body || body.dataset.uiuxReady === 'true') return;
  body.dataset.uiuxReady = 'true';
  body.classList.add('capital-uiux-v3');

  const reduceMotion = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches === true;
  const page = location.pathname.split('/').pop() || 'index.html';
  const isAvailability = /availability|space/.test(page);
  const isConversionForm = /^(leasing|retail)\.html$/.test(page);
  const primaryHref = isAvailability ? 'leasing.html?intent=office' : 'availability.html';
  const primaryLabel = isAvailability ? 'Talk to Leasing' : 'Find a Space';
  const secondaryHref = /visit/.test(page) ? 'leasing.html?intent=viewing' : 'visit.html';
  const secondaryLabel = /visit/.test(page) ? 'Book a Viewing' : 'Plan a Visit';
  const officialPrivacyUrl = 'https://capitalplace.com.vn/capital-place-is-a-grade-a-office-building-comprises-of-2-towers-of-37-floors-13/';

  const toast = document.createElement('div');
  toast.className = 'cu2-toast';
  toast.setAttribute('role', 'status');
  toast.setAttribute('aria-live', 'polite');
  document.body.appendChild(toast);
  let toastTimer;
  const showToast = (message) => {
    toast.textContent = message;
    toast.classList.add('is-visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('is-visible'), 3200);
  };

  const progress = document.createElement('div');
  progress.className = 'cu2-progress';
  progress.setAttribute('aria-hidden', 'true');
  progress.innerHTML = '<span></span>';
  document.body.appendChild(progress);
  const progressBar = progress.firstElementChild;
  const updateProgress = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    progressBar.style.width = `${max > 0 ? Math.min(100, Math.max(0, scrollY / max * 100)) : 0}%`;
  };
  addEventListener('scroll', updateProgress, { passive: true });
  addEventListener('resize', updateProgress, { passive: true });
  updateProgress();

  const backTop = document.createElement('button');
  backTop.type = 'button';
  backTop.className = 'cu2-backtop';
  backTop.setAttribute('aria-label', 'Back to top');
  backTop.innerHTML = '<span aria-hidden="true">↑</span>';
  backTop.addEventListener('click', () => scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }));
  document.body.appendChild(backTop);
  const updateBackTop = () => backTop.classList.toggle('is-visible', scrollY > innerHeight * .7);
  addEventListener('scroll', updateBackTop, { passive: true });
  updateBackTop();

  const mainNav = document.getElementById('main-nav');
  const firstMainSection = document.querySelector('#main-content > section:first-child');
  const hasVisualHero = Boolean(firstMainSection?.matches('[class*="hero"],#hero,[data-focus]'));
  if (mainNav && !hasVisualHero) mainNav.classList.add('cu2-nav-solid');

  document.querySelectorAll('#main-nav a[href], #mob-menu a[href]').forEach(link => {
    const href = link.getAttribute('href');
    if (!href || /^(#|mailto:|tel:|https?:)/.test(href)) return;
    const linkedPage = href.split('?')[0].split('#')[0].split('/').pop() || 'index.html';
    const matches = linkedPage === page;
    link.classList.toggle('active', matches);
    if (matches) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });

  const mobileActions = document.createElement('nav');
  mobileActions.className = 'cu2-mobile-actions';
  mobileActions.setAttribute('aria-label', 'Quick actions');
  mobileActions.innerHTML = `<a href="${primaryHref}">${primaryLabel}</a><a href="${secondaryHref}">${secondaryLabel}</a>`;
  if (/^(404|privacy)\.html$/.test(page) || isConversionForm) body.classList.add('cu2-no-mobile-actions');
  else document.body.appendChild(mobileActions);

  const ham = document.getElementById('hamburger');
  const menu = document.getElementById('mob-menu');
  const iconMenu = document.getElementById('icon-menu');
  const iconClose = document.getElementById('icon-close');
  let menuReturnFocus = null;
  const getMenuFocusable = () => menu ? [...menu.querySelectorAll('a[href],button:not([disabled]),[tabindex]:not([tabindex="-1"])')] : [];
  const syncMenuUi = (open) => {
    if (!ham || !menu) return;
    ham.setAttribute('aria-expanded', String(open));
    body.classList.toggle('cu2-menu-open', open);
    if (iconMenu) iconMenu.style.display = open ? 'none' : '';
    if (iconClose) iconClose.style.display = open ? '' : 'none';
  };
  const closeMenu = (restoreFocus = false) => {
    if (!ham || !menu) return;
    menu.classList.remove('open');
    syncMenuUi(false);
    if (restoreFocus && menuReturnFocus instanceof HTMLElement) menuReturnFocus.focus();
  };

  if (ham && menu) {
    const menuObserver = new MutationObserver(() => {
      const open = menu.classList.contains('open');
      syncMenuUi(open);
      if (open) {
        menuReturnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : ham;
        requestAnimationFrame(() => getMenuFocusable()[0]?.focus());
      }
    });
    menuObserver.observe(menu, { attributes: true, attributeFilter: ['class'] });
    menu.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(false); });
    document.addEventListener('click', event => {
      if (menu.classList.contains('open') && !menu.contains(event.target) && !ham.contains(event.target)) closeMenu(false);
    });
    document.addEventListener('keydown', event => {
      if (!menu.classList.contains('open')) return;
      if (event.key === 'Escape') {
        event.preventDefault();
        closeMenu(true);
        return;
      }
      if (event.key !== 'Tab') return;
      const focusable = getMenuFocusable();
      if (!focusable.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  // English is the only implemented locale. Keep document semantics truthful.
  document.documentElement.lang = 'en';
  try { localStorage.removeItem('capital-ui-lang'); } catch (_) {}
  document.querySelectorAll('.lang-btns button').forEach(button => {
    const code = button.textContent.trim();
    const isEnglish = code === 'EN';
    button.classList.toggle('active', isEnglish);
    button.setAttribute('aria-pressed', String(isEnglish));
    if (!isEnglish) {
      button.setAttribute('aria-disabled', 'true');
      button.title = 'Vietnamese content is not implemented in this static prototype.';
    } else {
      button.removeAttribute('aria-disabled');
    }
  });
  window.setLang = lang => {
    if (lang === 'VI') {
      showToast('Vietnamese content is not implemented in this static prototype. English remains active.');
      return;
    }
    document.documentElement.lang = 'en';
    showToast('English is active.');
  };

  document.querySelectorAll('[role="tablist"]').forEach(tablist => {
    const tabs = [...tablist.querySelectorAll('[role="tab"]')];
    tablist.addEventListener('keydown', event => {
      if (!['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp', 'Home', 'End'].includes(event.key) || !tabs.length) return;
      const current = Math.max(0, tabs.indexOf(document.activeElement));
      let next = current;
      if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (current + 1) % tabs.length;
      else next = (current - 1 + tabs.length) % tabs.length;
      event.preventDefault();
      tabs[next].focus();
      tabs[next].click();
    });
  });

  document.querySelectorAll('a[href="#"]').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      showToast('This prototype action is not connected to an external service.');
    });
  });

  // Real-world building-directory cue, kept to structural fidelity (L2).
  const sectionLabelOverrides = {
    scale: 'Building scale', architecture: 'Architecture & identity', workplace: 'Workplace', leed: 'Sustainability',
    'location-community': 'Location & community', 'find-space': 'Find a space', 'building-identity': 'Building anatomy',
    'floor-planning': 'Floor planning', finder: 'Space finder', 'tower-explorer': 'Tower explorer',
    'office-hero': 'Office overview', 'location-hero': 'Location overview', 'availability-hero': 'Availability overview'
  };
  const main = document.getElementById('main-content');
  const canShowDirectory = main && !/^(404|privacy|leasing|retail)\.html$/.test(page);
  if (canShowDirectory) {
    const topSections = [...main.querySelectorAll(':scope > section')];
    topSections.forEach((section, index) => {
      const heroLike = index === 0 || /hero/i.test(section.id) || section.matches('[class*="hero"],[data-focus]');
      if (heroLike || section.querySelector(':scope > .cpv3-section-rule')) return;
      section.classList.add('cpv3-rule-host');
      const rule = document.createElement('span');
      rule.className = 'cpv3-section-rule';
      rule.setAttribute('aria-hidden', 'true');
      section.prepend(rule);
    });

    const entries = topSections.filter(section => section.id && !/hero/i.test(section.id)).map(section => {
      const labelledBy = section.getAttribute('aria-labelledby');
      const heading = labelledBy ? document.getElementById(labelledBy) : section.querySelector('h1,h2,h3');
      const raw = sectionLabelOverrides[section.id] || heading?.textContent?.replace(/\s+/g, ' ').trim() || section.id.replace(/[-_]+/g, ' ');
      return { section, label: raw.length > 31 ? `${raw.slice(0, 28).trim()}…` : raw };
    }).filter(entry => entry.label);

    if (entries.length >= 3) {
      const directory = document.createElement('nav');
      directory.className = 'cpv3-directory';
      directory.setAttribute('aria-label', 'On this page');
      directory.innerHTML = entries.map((entry, index) => `<a href="#${entry.section.id}"><span>${String(index + 1).padStart(2, '0')}</span><span>${entry.label}</span></a>`).join('');
      document.body.appendChild(directory);
      const links = [...directory.querySelectorAll('a')];
      const updateDirectoryVisibility = () => directory.classList.toggle('cpv3-directory-ready', scrollY > innerHeight * .42);
      addEventListener('scroll', updateDirectoryVisibility, { passive: true });
      updateDirectoryVisibility();
      links.forEach((link, index) => link.addEventListener('click', event => {
        event.preventDefault();
        entries[index].section.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
        history.replaceState(null, '', `#${entries[index].section.id}`);
      }));
      const setActive = section => {
        const activeIndex = entries.findIndex(entry => entry.section === section);
        links.forEach((link, index) => {
          const active = index === activeIndex;
          link.classList.toggle('is-active', active);
          if (active) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      };
      if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(records => {
          const visible = records.filter(record => record.isIntersecting).sort((a, b) => Math.abs(a.boundingClientRect.top) - Math.abs(b.boundingClientRect.top));
          if (visible[0]) setActive(visible[0].target);
        }, { rootMargin: '-24% 0px -58% 0px', threshold: [0, .15, .5] });
        entries.forEach(entry => observer.observe(entry.section));
      }
    }
  }

  // The official Twin-Peaks notice is separate from this prototype's local/mailto behavior.
  const privacyTargets = [];
  const consent = document.querySelector('.la-form-consent');
  if (consent) privacyTargets.push(consent);
  const privacyCopy = page === 'privacy.html' ? document.querySelector('.ux-section-copy') : null;
  if (privacyCopy) privacyTargets.push(privacyCopy);
  privacyTargets.forEach(target => {
    if (target.parentElement?.querySelector('.cpv3-official-policy')) return;
    const note = document.createElement('p');
    note.className = 'cpv3-official-policy';
    note.innerHTML = `For the building owner's current first-party policy, read the <a href="${officialPrivacyUrl}" target="_blank" rel="noopener noreferrer">Twin-Peaks Personal Data Protection Policy and Processing Notice</a>. This is separate from this static prototype's email-preparation behavior.`;
    target.insertAdjacentElement('afterend', note);
  });
})();
