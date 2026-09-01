(function capitalDataBootstrap(global) {
  'use strict';

  const facts = Object.freeze({
    name: 'Capital Place', city: 'Hanoi', address: '29 Lieu Giai, Ngoc Ha, Hanoi, Vietnam',
    addressShort: '29 Lieu Giai · Ngoc Ha · Hanoi', leasableAreaSqm: 93000, leasableAreaLabel: '93,000 sqm',
    towers: 2, storeysPerTower: 37, grade: 'Grade A', hotline: '1800 9289', hotlineHref: 'tel:18009289',
    leasingEmail: 'leasing@capitalplace.vn', leasingEmailHref: 'mailto:leasing@capitalplace.vn',
    certifications: 'Dual LEED-certified', dataSource: 'Capital Place official website',
    dataSourceUrl: 'https://capitalplace.com.vn/office/',
    sustainabilitySourceUrl: 'https://capitalplace.com.vn/sustainability-and-community/',
    dataChecked: 'September 2026'
  });

  const statusMeta = Object.freeze({
    'on-request': { label: 'Live Status via Leasing', order: 1, actionable: true }
  });

  // Public planning references only. Capital Place does not expose a verified
  // real-time commercial inventory feed in this static project.
  const spaces = Object.freeze([
    {
      id: 'reference-1847', tower: 'Both Towers', towerNumber: 0, floor: 'Reference Floor Plate A', floorNumber: 0,
      suite: 'Published planning reference', areaSqm: 1847, minimumAreaSqm: 1847, divisible: false,
      status: 'on-request', availableFrom: 'Current availability confirmed by leasing', fitOutStatus: 'Condition on request',
      viewDirection: 'Orientation on request', floorPlanId: 'typical-high-zone', planningHeadcount: 184, workstations: 156,
      offices: 16, managingDirectorOffices: 7, meetingSeats: 60, featured: true, evidence: 'OFFICIAL_PUBLIC_REFERENCE'
    },
    {
      id: 'reference-1240', tower: 'Both Towers', towerNumber: 0, floor: 'Reference Floor Plate B', floorNumber: 0,
      suite: 'Representative planning scenario', areaSqm: 1240, minimumAreaSqm: 1240, divisible: false,
      status: 'on-request', availableFrom: 'Current availability confirmed by leasing', fitOutStatus: 'Condition on request',
      viewDirection: 'Orientation on request', floorPlanId: 'typical-low-zone', planningHeadcount: 110, workstations: 100,
      offices: 10, managingDirectorOffices: 5, meetingSeats: 24, featured: true, evidence: 'REPRESENTATIVE_PROTOTYPE'
    }
  ]);

  const resources = Object.freeze([
    { id: 'facts', title: 'Building Fact Sheet', access: 'public', href: 'office.html#building-identity', description: 'Verified building scale, grade and workplace proposition.' },
    { id: 'availability', title: 'Planning References', access: 'public', href: 'availability.html#current-opportunities', description: 'Planning references with current availability confirmed directly by leasing.' },
    { id: 'floor-plans', title: 'Reference Floor Plans', access: 'public', href: 'office.html#floor-planning', description: 'Typical floor plates for early workplace evaluation.' },
    { id: 'specifications', title: 'Building Specifications', access: 'public', href: 'office.html#technical-specifications', description: 'Space, access, comfort and resilience specifications.' },
    { id: 'sustainability', title: 'Sustainability Overview', access: 'public', href: 'sustainability.html#dual-leed', description: 'LEED credentials and occupier value.' },
    { id: 'location', title: 'Location & Arrival Guide', access: 'public', href: 'visit.html', description: 'Address, transport, drop-off and visitor arrival.' },
    { id: 'technical', title: 'Detailed Technical Package', access: 'qualified', href: 'leasing.html?intent=technical-package', description: 'CAD, detailed plans and fit-out information through leasing.' }
  ]);

  // Compatibility anchors preserve previously published deep links while the
  // current IA uses clearer section IDs. They are runtime aliases, not new page roles.
  const legacyAnchorAliases = Object.freeze({
    'office.html': Object.freeze({
      'floor-explorer': '#floor-planning',
      'office-specifications': '#technical-specifications'
    }),
    'resources.html': Object.freeze({ 'specifications': '#technical-core' }),
    'location.html': Object.freeze({ 'transport': '.lc-connected' })
  });

  const documentMetadata = Object.freeze({
    'faq.html': Object.freeze({
      description: 'Frequently asked questions about Capital Place Hanoi, including Grade A office space, location, amenities, sustainability, availability and arranging a viewing.'
    })
  });

  global.CapitalData = Object.freeze({
    facts, statusMeta, spaces, resources, legacyAnchorAliases, documentMetadata,
    availabilityMode: 'leasing-confirmation',
    availabilityNotice: 'Planning references only. Current availability, areas, divisibility, pricing and commercial terms must be confirmed by the Capital Place leasing team.'
  });

  function applyDocumentCompatibility() {
    const page = global.location.pathname.split('/').pop() || 'index.html';
    const metadata = documentMetadata[page];
    if (metadata?.description && !document.querySelector('meta[name="description"]')) {
      const meta = document.createElement('meta');
      meta.name = 'description';
      meta.content = metadata.description;
      document.head.appendChild(meta);
    }

    const aliases = legacyAnchorAliases[page];
    if (!aliases) return;
    Object.entries(aliases).forEach(([legacyId, selector]) => {
      if (document.getElementById(legacyId)) return;
      const target = document.querySelector(selector);
      if (!target) return;
      const anchor = document.createElement('span');
      anchor.id = legacyId;
      anchor.setAttribute('aria-hidden', 'true');
      anchor.style.cssText = 'display:block;height:0;overflow:hidden;scroll-margin-top:110px';
      target.insertAdjacentElement('beforebegin', anchor);
      if (global.location.hash === `#${legacyId}`) {
        global.requestAnimationFrame(() => anchor.scrollIntoView({ block: 'start' }));
      }
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', applyDocumentCompatibility, { once: true });
  else applyDocumentCompatibility();
})(window);
