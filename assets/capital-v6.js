(() => {
  'use strict';

  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches === true;
  const query = new URLSearchParams(window.location.search);
  const userAgent = navigator.userAgent || '';
  const captureMode =
    query.get('figma') === '1' ||
    document.documentElement.dataset.figmaCapture === 'true' ||
    navigator.webdriver === true ||
    /HeadlessChrome|Playwright|Puppeteer/i.test(userAgent);

  const reveals = [...document.querySelectorAll('.cp6-reveal')];

  function showReveal(element, { immediate = false } = {}) {
    element.classList.add('is-in');
    if (immediate) {
      element.style.opacity = '1';
      element.style.transform = 'none';
      element.style.transition = 'none';
    }
  }

  function prepareCaptureAssets() {
    if (!captureMode) return;

    document.documentElement.dataset.figmaCapture = 'true';
    const imagePreloads = [];

    document.querySelectorAll('img').forEach((img) => {
      if (img.getAttribute('loading') === 'lazy') {
        img.setAttribute('loading', 'eager');
        try { img.loading = 'eager'; } catch (_) {}
      }

      const src = img.currentSrc || img.getAttribute('src');
      if (src) {
        const preload = new Image();
        preload.decoding = 'async';
        preload.src = src;
        imagePreloads.push(preload);
      }

      const srcset = img.getAttribute('srcset');
      if (srcset) {
        const preload = new Image();
        preload.decoding = 'async';
        preload.srcset = srcset;
        preload.sizes = img.getAttribute('sizes') || '100vw';
        imagePreloads.push(preload);
      }
    });

    reveals.forEach((element) => showReveal(element, { immediate: true }));

    Promise.allSettled(imagePreloads.map((preload) => new Promise((resolve) => {
      if (preload.complete) return resolve();
      preload.addEventListener('load', resolve, { once: true });
      preload.addEventListener('error', resolve, { once: true });
    }))).then(() => {
      document.documentElement.dataset.figmaAssetsReady = 'true';
      window.dispatchEvent(new Event('capital:assets-ready'));
    });
  }

  function initRevealMotion() {
    if (!reveals.length) return;

    if (captureMode || reduce || !('IntersectionObserver' in window)) {
      reveals.forEach((element) => showReveal(element, { immediate: captureMode || reduce }));
      return;
    }

    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        showReveal(entry.target);
        currentObserver.unobserve(entry.target);
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -7% 0px'
    });

    // Fail-safe readiness gate: CSS only hides reveal targets after the observer
    // has been created successfully. If this runtime never executes, content stays visible.
    document.documentElement.classList.add('cp-motion-ready');
    reveals.forEach((element) => observer.observe(element));
  }

  prepareCaptureAssets();
  initRevealMotion();

  const menuButton = document.querySelector('.cp6-menu');
  const navLinks = document.querySelector('.cp6-nav-links');
  const brand = document.querySelector('.cp6-brand');

  if (brand && !brand.getAttribute('aria-label')) {
    brand.setAttribute('aria-label', 'Capital Place Hanoi home');
  }

  if (navLinks && !navLinks.getAttribute('aria-label')) {
    navLinks.setAttribute('aria-label', 'Primary navigation');
  }

  if (menuButton && navLinks) {
    if (!navLinks.id) navLinks.id = 'primary-nav';
    menuButton.setAttribute('aria-controls', navLinks.id);
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open navigation');

    let lockedScrollY = 0;

    const menuFocusables = () => [
      menuButton,
      ...navLinks.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])')
    ].filter((el) => !el.hasAttribute('disabled') && el.getClientRects().length > 0);

    const unlockBody = () => {
      const top = document.body.style.top;
      document.body.classList.remove('cp6-menu-open');
      document.body.style.top = '';
      if (top) window.scrollTo(0, lockedScrollY);
    };

    const closeMenu = ({ restoreFocus = false } = {}) => {
      if (!navLinks.classList.contains('is-open')) return;
      navLinks.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Open navigation');
      unlockBody();
      if (restoreFocus) menuButton.focus();
    };

    const openMenu = () => {
      lockedScrollY = window.scrollY || window.pageYOffset || 0;
      navLinks.classList.add('is-open');
      menuButton.setAttribute('aria-expanded', 'true');
      menuButton.setAttribute('aria-label', 'Close navigation');
      document.body.style.top = `-${lockedScrollY}px`;
      document.body.classList.add('cp6-menu-open');
      requestAnimationFrame(() => navLinks.querySelector('a[href]')?.focus());
    };

    menuButton.addEventListener('click', () => {
      if (navLinks.classList.contains('is-open')) closeMenu({ restoreFocus: true });
      else openMenu();
    });

    navLinks.addEventListener('click', (event) => {
      if (event.target.closest('a[href]')) closeMenu();
    });

    document.addEventListener('keydown', (event) => {
      if (!navLinks.classList.contains('is-open')) return;

      if (event.key === 'Escape') {
        event.preventDefault();
        closeMenu({ restoreFocus: true });
        return;
      }

      if (event.key === 'Tab') {
        const focusables = menuFocusables();
        if (!focusables.length) return;
        const first = focusables[0];
        const last = focusables[focusables.length - 1];
        const current = document.activeElement;

        if (event.shiftKey && current === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && current === last) {
          event.preventDefault();
          first.focus();
        }
      }
    });

    addEventListener('resize', () => {
      if (innerWidth > 900) closeMenu();
    }, { passive: true });

    addEventListener('pagehide', () => closeMenu(), { passive: true });
  }

  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.cp6-nav-links a[href]').forEach((anchor) => {
    const href = anchor.getAttribute('href').split('?')[0].split('#')[0].split('/').pop() || 'index.html';
    if (href === page) anchor.setAttribute('aria-current', 'page');
  });

  document.querySelectorAll('[data-scroll]').forEach((anchor) => anchor.addEventListener('click', (event) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
  }));
})();
