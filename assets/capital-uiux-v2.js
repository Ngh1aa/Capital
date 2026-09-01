(() => {
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

  // Make the page location explicit in the persistent navigation.
  document.querySelectorAll('#main-nav a[href], #mob-menu a[href]').forEach(link => {
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;
    let linkedPage = href.split('?')[0].split('#')[0].split('/').pop() || 'index.html';
    if (linkedPage === '') linkedPage = 'index.html';
    const matches = linkedPage === page || (page === '' && linkedPage === 'index.html');
    link.classList.toggle('active', matches);
    if (matches) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });

  const mobileActions = document.createElement('nav');
  mobileActions.className = 'cu2-mobile-actions';
  mobileActions.setAttribute('aria-label', 'Quick actions');
  mobileActions.innerHTML = `<a href="${primaryHref}">${primaryLabel}</a><a href="${secondaryHref}">${secondaryLabel}</a>`;
  if (/^(404|privacy)\.html$/.test(page) || isConversionForm) {
    body.classList.add('cu2-no-mobile-actions');
  } else {
    document.body.appendChild(mobileActions);
  }

  const ham = document.getElementById('hamburger');
  const menu = document.getElementById('mob-menu');
  let menuReturnFocus = null;
  const getMenuFocusable = () => menu ? [...menu.querySelectorAll('a[href],button:not([disabled]),[tabindex]:not([tabindex="-1"])')] : [];
  const closeMenu = (restoreFocus = false) => {
    if (!ham || !menu) return;
    menu.classList.remove('open');
    ham.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('cu2-menu-open');
    if (restoreFocus && menuReturnFocus instanceof HTMLElement) menuReturnFocus.focus();
  };

  if (ham && menu) {
    const menuObserver = new MutationObserver(() => {
      const open = menu.classList.contains('open');
      document.body.classList.toggle('cu2-menu-open', open);
      ham.setAttribute('aria-expanded', String(open));
      if (open) {
        menuReturnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : ham;
        requestAnimationFrame(() => getMenuFocusable()[0]?.focus());
      }
    });
    menuObserver.observe(menu, { attributes: true, attributeFilter: ['class'] });

    menu.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu(false);
    });
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
      if (event.key === 'Tab') {
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
      }
    });
  }

  const applyLang = (lang, notify = true) => {
    const normalized = lang === 'VI' ? 'vi' : 'en';
    document.documentElement.lang = normalized;
    document.documentElement.dataset.uiLang = normalized;
    document.querySelectorAll('.lang-btns button').forEach(button => {
      const selected = button.textContent.trim() === lang;
      button.classList.toggle('active', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    try { localStorage.setItem('capital-ui-lang', normalized); } catch (_) {}
    if (notify) showToast(normalized === 'vi'
      ? 'Vietnamese preview selected. Full Vietnamese content is not connected in this static prototype.'
      : 'English preview selected.');
  };
  window.setLang = lang => applyLang(lang, true);
  try {
    const saved = localStorage.getItem('capital-ui-lang');
    if (saved === 'vi') applyLang('VI', false);
    else applyLang('EN', false);
  } catch (_) { applyLang('EN', false); }

  document.querySelectorAll('[role="tablist"]').forEach(tablist => {
    const tabs = [...tablist.querySelectorAll('[role="tab"]')];
    tablist.addEventListener('keydown', event => {
      if (!['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp', 'Home', 'End'].includes(event.key) || !tabs.length) return;
      const current = Math.max(0, tabs.indexOf(document.activeElement));
      let next = current;
      if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (current + 1) % tabs.length;
      else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (current - 1 + tabs.length) % tabs.length;
      event.preventDefault();
      tabs[next].focus();
      tabs[next].click();
    });
  });

  document.querySelectorAll('a[href="#"]').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      showToast('This prototype action is ready for the next connected flow.');
    });
  });

  // A page-directory pattern adapted from physical building wayfinding / floor-plan indexing.
  // It improves orientation on long decision pages without changing the existing IA.
  const sectionLabelOverrides = {
    scale: 'Building scale',
    architecture: 'Architecture & identity',
    workplace: 'Workplace',
    leed: 'Sustainability',
    'location-community': 'Location & community',
    'find-space': 'Find a space',
    'building-identity': 'Building anatomy',
    'floor-planning': 'Floor planning',
    finder: 'Space finder',
    'tower-explorer': 'Tower explorer',
    'office-hero': 'Office overview',
    'location-hero': 'Location overview',
    'availability-hero': 'Availability overview'
  };

  const main = document.getElementById('main-content');
  const canShowDirectory = main && !/^(404|privacy|leasing|retail)\.html$/.test(page);
  if (canShowDirectory) {
    const sections = [...main.querySelectorAll(':scope > section[id]')]
      .filter(section => !/\bhero\b/i.test(section.id) || section.id === 'office-hero' || section.id === 'location-hero' || section.id === 'availability-hero');

    const entries = sections.map(section => {
      const labelledBy = section.getAttribute('aria-labelledby');
      const heading = labelledBy ? document.getElementById(labelledBy) : section.querySelector('h1,h2,h3');
      const raw = sectionLabelOverrides[section.id] || heading?.textContent?.replace(/\s+/g, ' ').trim() || section.id.replace(/[-_]+/g, ' ');
      const label = raw.length > 31 ? `${raw.slice(0, 28).trim()}…` : raw;
      return { section, label };
    }).filter(entry => entry.label);

    if (entries.length >= 3) {
      const directory = document.createElement('nav');
      directory.className = 'cpv3-directory';
      directory.setAttribute('aria-label', 'On this page');
      directory.innerHTML = entries.map((entry, index) =>
        `<a href="#${entry.section.id}"><span>${String(index + 1).padStart(2, '0')}</span><span>${entry.label}</span></a>`
      ).join('');
      document.body.appendChild(directory);

      const links = [...directory.querySelectorAll('a')];
      links.forEach((link, index) => {
        link.addEventListener('click', event => {
          event.preventDefault();
          entries[index].section.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
          history.replaceState(null, '', `#${entries[index].section.id}`);
        });
      });

      const setActiveDirectory = section => {
        const index = entries.findIndex(entry => entry.section === section);
        links.forEach((link, linkIndex) => {
          const active = linkIndex === index;
          link.classList.toggle('is-active', active);
          if (active) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      };

      if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(records => {
          const visible = records
            .filter(record => record.isIntersecting)
            .sort((a, b) => Math.abs(a.boundingClientRect.top) - Math.abs(b.boundingClientRect.top));
          if (visible[0]) setActiveDirectory(visible[0].target);
        }, { rootMargin: '-25% 0px -58% 0px', threshold: [0, .15, .5] });
        entries.forEach(entry => observer.observe(entry.section));
      } else {
        setActiveDirectory(entries[0].section);
      }
    }
  }
})();
