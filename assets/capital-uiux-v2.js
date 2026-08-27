(() => {
  const body = document.body;
  if (!body || body.dataset.uiuxReady === 'true') return;
  body.dataset.uiuxReady = 'true';

  const page = location.pathname.split('/').pop() || 'index.html';
  const isAvailability = /availability|space/.test(page);
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
  backTop.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));
  document.body.appendChild(backTop);
  const updateBackTop = () => backTop.classList.toggle('is-visible', scrollY > innerHeight * .7);
  addEventListener('scroll', updateBackTop, { passive: true });
  updateBackTop();

  const mobileActions = document.createElement('nav');
  mobileActions.className = 'cu2-mobile-actions';
  mobileActions.setAttribute('aria-label', 'Quick actions');
  mobileActions.innerHTML = `<a href="${primaryHref}">${primaryLabel}</a><a href="${secondaryHref}">${secondaryLabel}</a>`;
  if (/^(404|privacy)\.html$/.test(page)) {
    body.classList.add('cu2-no-mobile-actions');
    mobileActions.remove();
  } else {
    document.body.appendChild(mobileActions);
  }

  const ham = document.getElementById('hamburger');
  const menu = document.getElementById('mob-menu');
  const closeMenu = () => {
    if (!ham || !menu) return;
    menu.classList.remove('open');
    ham.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('cu2-menu-open');
  };
  if (ham && menu) {
    const menuObserver = new MutationObserver(() => {
      const open = menu.classList.contains('open');
      document.body.classList.toggle('cu2-menu-open', open);
      if (open) menu.querySelector('a')?.focus();
    });
    menuObserver.observe(menu, { attributes: true, attributeFilter: ['class'] });
    menu.addEventListener('click', (event) => {
      if (event.target.closest('a')) closeMenu();
    });
    document.addEventListener('click', (event) => {
      if (menu.classList.contains('open') && !menu.contains(event.target) && !ham.contains(event.target)) closeMenu();
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        closeMenu();
        if (document.activeElement === ham) ham.blur();
      }
    });
  }

  const applyLang = (lang, notify = true) => {
    const normalized = lang === 'VI' ? 'vi' : 'en';
    document.documentElement.lang = normalized;
    document.documentElement.dataset.uiLang = normalized;
    document.querySelectorAll('.lang-btns button').forEach(button => {
      button.classList.toggle('active', button.textContent.trim() === lang);
      button.setAttribute('aria-pressed', String(button.textContent.trim() === lang));
    });
    try { localStorage.setItem('capital-ui-lang', normalized); } catch (_) {}
    if (notify) showToast(normalized === 'vi'
      ? 'Vietnamese preview selected. Content translation is not connected in this UI prototype.'
      : 'English preview selected.');
  };
  window.setLang = (lang) => applyLang(lang, true);
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
})();
