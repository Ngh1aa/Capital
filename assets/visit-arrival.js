(function visitArrival(global, document) {
  'use strict';
  const params = new URLSearchParams(global.location.search);
  const context = document.querySelector('[data-visit-context]');
  const space = params.get('space');
  const intent = params.get('intent');
  if (context && (space || intent === 'viewing')) {
    context.hidden = false;
    const target = document.querySelector('[data-visit-space]');
    if (target) target.textContent = space || 'Private viewing requested · confirm details with Leasing';
    const bookingLink = document.querySelector('[data-visit-book]');
    if (bookingLink) bookingLink.href = `leasing.html?intent=viewing&space=${encodeURIComponent(space || '')}`;
    const copy = document.querySelector('[data-visit-context-copy]');
    if (copy) copy.textContent = 'Your viewing request is already in motion. Confirm the host, selected space, preferred time and building access before travelling.';
  }
})(window, document);
