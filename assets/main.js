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
    if (target === page) a.classList.add('active');
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

// ── UI Feedback Tool (Nhấn đồng thời Q + W + E để bật/tắt)
(function initUIFeedback() {
  const debugFeedback = ['1', 'true', 'on'].includes(new URLSearchParams(location.search).get('feedback') || '');
  const init = (mod) => {
    if (mod && typeof mod.createUIFeedback === 'function') {
      const instance = mod.createUIFeedback({
        storageKey: 'capital-ui-feedback',
        accent: '#c9a866',
        githubRepo: 'Ngh1aa/Capital',
        startActive: debugFeedback
      });
      document.documentElement.dataset.uiFeedback = instance ? 'ready' : 'unavailable';
      return instance;
    }
    document.documentElement.dataset.uiFeedback = 'unavailable';
    return null;
  };

  import('./ui-feedback.js').then(init).catch((error) => {
    document.documentElement.dataset.uiFeedback = 'error';
    console.warn('[Capital] UI feedback failed to load', error);
  });
})();

