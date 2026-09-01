(() => {
  'use strict';
  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const menuButton = document.querySelector('.cp6-menu');
  const navLinks = document.querySelector('.cp6-nav-links');
  if (menuButton && navLinks) {
    if (!navLinks.id) navLinks.id = 'primary-nav';
    menuButton.setAttribute('aria-controls', navLinks.id);
    menuButton.setAttribute('aria-expanded', 'false');
    const closeMenu = () => {
      navLinks.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };
    menuButton.addEventListener('click', () => {
      const open = navLinks.classList.toggle('is-open');
      menuButton.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) navLinks.querySelector('a')?.focus();
    });
    navLinks.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && navLinks.classList.contains('is-open')) {
        closeMenu();
        menuButton.focus();
      }
    });
    addEventListener('resize', () => { if (innerWidth > 900) closeMenu(); }, {passive:true});
  }

  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.cp6-nav-links a[href]').forEach(a => {
    const href = a.getAttribute('href').split('?')[0].split('#')[0].split('/').pop() || 'index.html';
    if (href === page) a.setAttribute('aria-current','page');
  });

  const reveals = [...document.querySelectorAll('.cp6-reveal')];
  if (reduce || !('IntersectionObserver' in window)) reveals.forEach(el => el.classList.add('is-in'));
  else {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, {threshold:.12, rootMargin:'0px 0px -8%'});
    reveals.forEach(el => io.observe(el));
  }

  document.querySelectorAll('[data-scroll]').forEach(a => a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block:'start'});
  }));
})();
