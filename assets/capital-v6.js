(() => {
  'use strict';
  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const menuButton = document.querySelector('.cp6-menu');
  const navLinks = document.querySelector('.cp6-nav-links');
  if (menuButton && navLinks) {
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.addEventListener('click', () => {
      const open = navLinks.classList.toggle('is-open');
      menuButton.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });
    navLinks.addEventListener('click', e => {
      if (!e.target.closest('a')) return;
      navLinks.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
    addEventListener('resize', () => {
      if (innerWidth > 900) {
        navLinks.classList.remove('is-open');
        menuButton.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    }, {passive:true});
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
