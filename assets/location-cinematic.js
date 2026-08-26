(function initLocationCinematic(global, document) {
  'use strict';

  function initLifeGallery() {
    const root = document.querySelector('[data-lc-gallery]');
    if (!root) return;
    const image = root.querySelector('[data-lc-gallery-image]');
    const title = root.querySelector('[data-lc-gallery-title]');
    const copy = root.querySelector('[data-lc-gallery-copy]');
    const count = root.querySelector('[data-lc-gallery-count]');
    const link = root.querySelector('.lc-life-copy a');
    const tabs = Array.from(root.querySelectorAll('[data-lc-scene]'));
    if (!image || !title || !copy || !tabs.length) return;

    const select = (tab, index) => {
      tabs.forEach((item) => {
        const active = item === tab;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      if (count) count.textContent = `${String(index + 1).padStart(2, '0')} / ${String(tabs.length).padStart(2, '0')}`;
      if (image.src.endsWith(tab.dataset.image)) {
        title.textContent = tab.dataset.title || '';
        copy.textContent = tab.dataset.copy || '';
        if (link && tab.dataset.link) link.href = tab.dataset.link;
        return;
      }
      image.classList.add('is-changing');
      const update = () => {
        image.src = tab.dataset.image;
        image.alt = tab.dataset.alt || '';
        title.textContent = tab.dataset.title || '';
        copy.textContent = tab.dataset.copy || '';
        if (link && tab.dataset.link) link.href = tab.dataset.link;
        image.classList.remove('is-changing');
      };
      global.setTimeout(update, global.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 160);
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => select(tab, index));
      tab.addEventListener('keydown', (event) => {
        if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
        event.preventDefault();
        const nextIndex = (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
        tabs[nextIndex].focus();
        select(tabs[nextIndex], nextIndex);
      });
    });
  }

  function initMap() {
    const root = document.querySelector('[data-lc-map-root]');
    if (!root) return;
    const base = root.querySelector('[data-lc-map-base]');
    const status = root.querySelector('[data-lc-map-status]');
    const pins = Array.from(root.querySelectorAll('.map-poi'));
    const filters = Array.from(document.querySelectorAll('[data-lc-map-filter]'));
    const kicker = root.querySelector('[data-lc-map-kicker]');
    const title = root.querySelector('[data-lc-map-title]');
    const address = root.querySelector('[data-lc-map-address]');
    const meta = root.querySelector('[data-lc-map-meta]');
    const copy = root.querySelector('[data-lc-map-copy]');
    const directions = root.querySelector('[data-lc-map-directions]');
    const config = global.CAPITAL_LOCATION_MAP || {};
    const map = {
      center: config.center || { lat: Number(root.dataset.centerLat), lng: Number(root.dataset.centerLng) },
      zoom: Number(config.zoom || root.dataset.zoom || 15),
      width: Number(config.width || root.dataset.mapWidth || 640),
      height: Number(config.height || root.dataset.mapHeight || 480),
      scale: Number(config.scale || 2),
      maptype: config.maptype || 'hybrid',
      language: config.language || 'en',
      region: config.region || 'VN'
    };

    const project = (lat, lng) => {
      const world = 256 * Math.pow(2, map.zoom);
      const x = ((lng + 180) / 360) * world;
      const sinLat = Math.sin(lat * Math.PI / 180);
      const y = (0.5 - Math.log((1 + sinLat) / (1 - sinLat)) / (4 * Math.PI)) * world;
      return { x, y };
    };

    const center = project(Number(map.center.lat), Number(map.center.lng));
    pins.forEach((pin) => {
      const point = project(Number(pin.dataset.lat), Number(pin.dataset.lng));
      const x = map.width / 2 + (point.x - center.x);
      const y = map.height / 2 + (point.y - center.y);
      pin.style.left = `${(x / map.width) * 100}%`;
      pin.style.top = `${(y / map.height) * 100}%`;
      pin.style.right = 'auto';
      pin.style.bottom = 'auto';
    });

    const setStatus = (message) => {
      if (!status) return;
      status.textContent = message;
      status.hidden = !message;
    };

    const staticKey = typeof config.apiKey === 'string' ? config.apiKey.trim() : '';
    if (base && staticKey) {
      const params = new URLSearchParams({
        center: `${map.center.lat},${map.center.lng}`,
        zoom: String(map.zoom),
        size: `${map.width}x${map.height}`,
        scale: String(map.scale),
        maptype: map.maptype,
        language: map.language,
        region: map.region,
        format: 'jpg',
        key: staticKey
      });
      base.src = `https://maps.googleapis.com/maps/api/staticmap?${params.toString()}`;
      base.addEventListener('load', () => setStatus(''), { once: true });
      base.addEventListener('error', () => {
        base.src = config.fallbackImage || 'assets/images/location/road-map.jpg';
        base.classList.add('is-fallback');
        setStatus('Live Hybrid map unavailable — showing the verified local map layer.');
      }, { once: true });
    } else {
      base?.classList.add('is-fallback');
      setStatus('Add a referrer-restricted Google Maps key to activate the live Hybrid layer.');
    }

    const selectPin = (pin) => {
      pins.forEach((item) => {
        const active = item === pin;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      if (kicker) kicker.textContent = pin.dataset.kicker || '';
      if (title) title.textContent = pin.dataset.title || '';
      if (address) address.textContent = pin.dataset.address || '';
      if (meta) meta.textContent = pin.dataset.meta || '';
      if (copy) copy.textContent = pin.dataset.copy || '';
      if (directions) directions.href = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(`${pin.dataset.lat},${pin.dataset.lng}`)}`;
    };

    const applyFilter = (category) => {
      filters.forEach((button) => {
        const active = button.dataset.lcMapFilter === category;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-pressed', String(active));
      });
      pins.forEach((pin) => {
        const visible = category === 'all' || pin.dataset.category === category || pin.classList.contains('map-poi--capital');
        pin.hidden = !visible;
      });
      const firstVisible = pins.find((pin) => !pin.hidden);
      if (firstVisible) selectPin(firstVisible);
    };

    filters.forEach((button) => button.addEventListener('click', () => applyFilter(button.dataset.lcMapFilter)));
    pins.forEach((pin) => {
      pin.addEventListener('click', () => selectPin(pin));
      pin.addEventListener('keydown', (event) => {
        if (event.key !== 'Enter' && event.key !== ' ') return;
        event.preventDefault();
        selectPin(pin);
      });
    });
    const initial = pins.find((pin) => pin.classList.contains('map-poi--capital')) || pins[0];
    if (initial) selectPin(initial);
  }

  function init() {
    initLifeGallery();
    initMap();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})(window, document);
