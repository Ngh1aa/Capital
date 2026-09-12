(() => {
  'use strict';

  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

  /*
   * Figma / HTML-to-design compatibility layer.
   *
   * Several pages intentionally use lazy-loaded images and scroll reveal effects for
   * the live website. Static importers usually render the page without scrolling,
   * which means off-screen images may never be requested and reveal blocks can remain
   * at opacity: 0. Eagerly request every image and expose every reveal block as soon
   * as the DOM is parsed so the complete page is available to design import tools.
   */
  const imagePreloads = [];
  document.querySelectorAll('img').forEach(img => {
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

  document.querySelectorAll('.cp6-reveal').forEach(el => {
    el.classList.add('is-in');
    el.style.opacity = '1';
    el.style.transform = 'none';
  });

  /* Keep strong references until load/error so importers can reach network-idle only
     after the page's visual assets have actually been requested. */
  Promise.allSettled(imagePreloads.map(preload => new Promise(resolve => {
    if (preload.complete) return resolve();
    preload.addEventListener('load', resolve, { once: true });
    preload.addEventListener('error', resolve, { once: true });
  }))).then(() => {
    document.documentElement.dataset.figmaAssetsReady = 'true';
    window.dispatchEvent(new Event('capital:assets-ready'));
  });

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
    ].filter(el => !el.hasAttribute('disabled') && el.getClientRects().length > 0);

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

    navLinks.addEventListener('click', event => {
      if (event.target.closest('a[href]')) closeMenu();
    });

    document.addEventListener('keydown', event => {
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
  document.querySelectorAll('.cp6-nav-links a[href]').forEach(anchor => {
    const href = anchor.getAttribute('href').split('?')[0].split('#')[0].split('/').pop() || 'index.html';
    if (href === page) anchor.setAttribute('aria-current', 'page');
  });

  /* Reveal blocks are intentionally visible immediately for reliable static capture.
     The is-in class preserves the final visual state defined by the stylesheet. */
  const reveals = [...document.querySelectorAll('.cp6-reveal')];
  reveals.forEach(el => {
    el.classList.add('is-in');
    el.style.opacity = '1';
    el.style.transform = 'none';
    if (reduce) el.style.transition = 'none';
  });

  document.querySelectorAll('[data-scroll]').forEach(anchor => anchor.addEventListener('click', event => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
  }));
})();
