// ── Nav scroll
window.addEventListener('scroll', () =>
  document.getElementById('main-nav').classList.toggle('scrolled', scrollY > 60),
  { passive: true }
);

// ── Mobile menu
const ham = document.getElementById('hamburger');
const mob = document.getElementById('mob-menu');
const iM  = document.getElementById('icon-menu');
const iC  = document.getElementById('icon-close');

ham.addEventListener('click', () => {
  const o = mob.classList.toggle('open');
  ham.setAttribute('aria-expanded', String(o));
  iM.style.display = o ? 'none' : '';
  iC.style.display = o ? '' : 'none';
});

function closeMob() {
  mob.classList.remove('open');
  ham.setAttribute('aria-expanded', 'false');
  iM.style.display = '';
  iC.style.display = 'none';
}

function setLang(l) {
  document.querySelectorAll('.lang-btns button').forEach(b =>
    b.classList.toggle('active', b.textContent === l)
  );
}

// ── Active nav link — highlight current page
(function highlightNav() {
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, #mob-menu a').forEach(a => {
    const href = a.getAttribute('href') || '';
    const target = href.split('/').pop();
    if (target === page) {
      a.classList.add('active');
      a.setAttribute('aria-current', 'page');
    }
  });
})();

// ── IntersectionObserver for fade-up
const fadeIO = new IntersectionObserver(
  es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); fadeIO.unobserve(e.target); } }),
  { threshold: 0.2 }
);
document.querySelectorAll('.fade-up').forEach(el => fadeIO.observe(el));

// ── Count-up helper (used on Home)
function ease(t) { return t < .5 ? 2*t*t : -1+(4-2*t)*t; }

function countUp(el) {
  const tgt = +el.dataset.target, comma = el.dataset.fmt === 'comma';
  const current = +(el.textContent || '').replace(/,/g, '') || 0;
  const format = value => comma ? value.toLocaleString() : value;
  if (current >= tgt) {
    el.textContent = format(tgt);
    return;
  }
  const dur = 2000, t0 = performance.now();
  const tick = t => {
    const p = Math.min((t - t0) / dur, 1), v = Math.round(ease(p) * tgt);
    el.textContent = format(v);
    if (p < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

const countIO = new IntersectionObserver(
  es => es.forEach(e => { if (e.isIntersecting) { countUp(e.target); countIO.unobserve(e.target); } }),
  { threshold: 0.5 }
);
document.querySelectorAll('.stat-num[data-target]').forEach(el => countIO.observe(el));

// ── Background video autoplay and reduced-motion fallback
(function initHeroMediaPlayback() {
  const video = document.querySelector('.hero-bg:is(video)');
  if (!video) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    video.pause();
  }
})();

// ── Architectural motion system
(function initCapitalMotionSystem() {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const selector = [
    'main > section',
    'main article',
    'main [class$="-card"]',
    'main [class*="-card "]',
    'main [class$="-row"]',
  ].join(',');
  let observer;

  document.documentElement.classList.add('capital-motion-ready');

  const prepare = (scope = document) => {
    const nodes = [
      ...(scope instanceof Element && scope.matches(selector) ? [scope] : []),
      ...scope.querySelectorAll(selector),
    ];

    nodes.forEach((node) => {
      if (node.dataset.capitalMotionReady === 'true' || node.closest('[data-no-motion]')) return;
      node.dataset.capitalMotionReady = 'true';
      node.classList.add('capital-motion-item');

      const siblings = [...node.parentElement.children].filter((child) => child.matches?.(selector));
      const index = Math.max(0, siblings.indexOf(node));
      node.style.setProperty('--capital-motion-delay', `${Math.min(index, 4) * 75}ms`);

      const hero = node.matches('#hero, .page-header, main > section:first-of-type');
      if (hero || reducedMotion || !observer) node.classList.add('is-motion-visible');
      else observer.observe(node);
    });
  };

  if (!reducedMotion && 'IntersectionObserver' in window) {
    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-motion-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: .11, rootMargin: '0px 0px -8% 0px' });
  }

  prepare();
  let revealQueued = false;
  const revealViewport = () => {
    revealQueued = false;
    document.querySelectorAll('.capital-motion-item:not(.is-motion-visible)').forEach((node) => {
      const rect = node.getBoundingClientRect();
      if (rect.top <= innerHeight * 1.08 && rect.bottom >= -innerHeight * .08) {
        node.classList.add('is-motion-visible');
        observer?.unobserve(node);
      }
    });
  };
  const queueViewportReveal = () => {
    if (revealQueued) return;
    revealQueued = true;
    requestAnimationFrame(revealViewport);
  };
  queueViewportReveal();
  setTimeout(queueViewportReveal, 180);
  window.addEventListener('scroll', queueViewportReveal, { passive: true });
  window.addEventListener('hashchange', queueViewportReveal);
  const mutations = new MutationObserver((records) => {
    records.forEach((record) => record.addedNodes.forEach((node) => {
      if (node instanceof Element) prepare(node);
    }));
  });
  mutations.observe(document.body, { childList: true, subtree: true });
})();

// ── UI Feedback Tool (Nhấn đồng thời Q + W + E để bật/tắt)
(function initUIFeedback() {
  const debugFeedback = ['1', 'true', 'on'].includes(new URLSearchParams(location.search).get('feedback') || '');
  const init = (mod) => {
    if (mod && typeof mod.createUIFeedback === 'function') {
      const instance = mod.createUIFeedback({
        storageKey: 'capital-ui-feedback',
        accent: '#231F20',
        githubRepo: 'Ngh1aa/Capital',
        startActive: debugFeedback
      });
      document.documentElement.dataset.uiFeedback = instance ? 'ready' : 'unavailable';
      return instance;
    }
    document.documentElement.dataset.uiFeedback = 'unavailable';
    return null;
  };

  import('./ui-feedback.js?v=4ef8421').then(init).catch((error) => {
    document.documentElement.dataset.uiFeedback = 'error';
    console.warn('[Capital] UI feedback failed to load', error);
  });
})();
