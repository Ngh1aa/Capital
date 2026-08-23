(function capitalDataBootstrap(global) {
  'use strict';

  const facts = Object.freeze({
    name: 'Capital Place',
    city: 'Hanoi',
    address: '29 Lieu Giai, Ngoc Ha, Hanoi, Vietnam',
    addressShort: '29 Lieu Giai · Ngoc Ha · Hanoi',
    leasableAreaSqm: 93000,
    leasableAreaLabel: '93,000 sqm',
    towers: 2,
    storeysPerTower: 37,
    grade: 'Grade A',
    hotline: '1800 9289',
    hotlineHref: 'tel:18009289',
    leasingEmail: 'leasing@capitalplace.vn',
    leasingEmailHref: 'mailto:leasing@capitalplace.vn',
    certifications: 'Dual LEED-certified',
    dataSource: 'Capital Place official website',
    dataChecked: 'August 2026'
  });

  const statusMeta = Object.freeze({
    available: { label: 'Available', order: 1, actionable: true },
    'available-soon': { label: 'Available Soon', order: 2, actionable: true },
    'under-offer': { label: 'Under Offer', order: 3, actionable: true },
    'future-availability': { label: 'Future Availability', order: 4, actionable: true },
    'on-request': { label: 'On Request', order: 5, actionable: true },
    leased: { label: 'Leased', order: 6, actionable: false }
  });

  // Demonstration inventory only. Every public surface labels this data as
  // indicative and routes users to leasing for current commercial terms.
  const spaces = Object.freeze([
    {
      id: 't1-l24', tower: 'Tower 01', towerNumber: 1, floor: 'Level 24', floorNumber: 24,
      suite: 'Full floor opportunity', areaSqm: 1329, minimumAreaSqm: 650, divisible: true,
      status: 'available', availableFrom: 'Available now · confirmation required',
      fitOutStatus: 'Condition on request', viewDirection: 'Orientation on request',
      floorPlanId: 'typical-high-zone', featured: true
    },
    {
      id: 't2-l18', tower: 'Tower 02', towerNumber: 2, floor: 'Level 18', floorNumber: 18,
      suite: 'Full floor opportunity', areaSqm: 1847, minimumAreaSqm: 1000, divisible: true,
      status: 'available-soon', availableFrom: 'Timing confirmed by leasing',
      fitOutStatus: 'Condition on request', viewDirection: 'Orientation on request',
      floorPlanId: 'typical-low-zone', featured: true
    },
    {
      id: 't1-l15', tower: 'Tower 01', towerNumber: 1, floor: 'Level 15', floorNumber: 15,
      suite: 'Full floor opportunity', areaSqm: 1240, minimumAreaSqm: 620, divisible: true,
      status: 'under-offer', availableFrom: 'Register backup interest',
      fitOutStatus: 'Condition on request', viewDirection: 'Orientation on request',
      floorPlanId: 'typical-low-zone', featured: false
    },
    {
      id: 't2-l10', tower: 'Tower 02', towerNumber: 2, floor: 'Level 10', floorNumber: 10,
      suite: 'Future opportunity', areaSqm: 1240, minimumAreaSqm: 620, divisible: true,
      status: 'future-availability', availableFrom: 'Future timing on request',
      fitOutStatus: 'Condition on request', viewDirection: 'Orientation on request',
      floorPlanId: 'typical-low-zone', featured: false
    },
    {
      id: 't1-l30', tower: 'Tower 01', towerNumber: 1, floor: 'Level 30', floorNumber: 30,
      suite: 'High-zone opportunity', areaSqm: 1847, minimumAreaSqm: 1000, divisible: true,
      status: 'on-request', availableFrom: 'Commercial status on request',
      fitOutStatus: 'Condition on request', viewDirection: 'Orientation on request',
      floorPlanId: 'typical-high-zone', featured: false
    },
    {
      id: 't2-l24', tower: 'Tower 02', towerNumber: 2, floor: 'Level 24', floorNumber: 24,
      suite: 'Reference floor', areaSqm: 1240, minimumAreaSqm: 1240, divisible: false,
      status: 'leased', availableFrom: 'Not currently available',
      fitOutStatus: 'Not published', viewDirection: 'Not published',
      floorPlanId: 'typical-high-zone', featured: false
    }
  ]);

  const resources = Object.freeze([
    { id: 'facts', title: 'Building Fact Sheet', access: 'public', href: 'office.html#building-overview', description: 'Verified building scale, grade and workplace proposition.' },
    { id: 'availability', title: 'Availability Overview', access: 'public', href: 'availability.html#current-opportunities', description: 'Indicative space opportunities and availability states.' },
    { id: 'floor-plans', title: 'Illustrative Floor Plans', access: 'public', href: 'office.html#floor-explorer', description: 'Typical floor plates for early workplace evaluation.' },
    { id: 'specifications', title: 'Building Specifications', access: 'public', href: 'office.html#office-specifications', description: 'Space, access, comfort and resilience specifications.' },
    { id: 'sustainability', title: 'Sustainability Overview', access: 'public', href: 'sustainability.html#sustainability-resources', description: 'LEED credentials and occupier value.' },
    { id: 'location', title: 'Location & Arrival Guide', access: 'public', href: 'visit.html', description: 'Address, transport, drop-off and visitor arrival.' },
    { id: 'technical', title: 'Detailed Technical Package', access: 'qualified', href: 'leasing.html?intent=technical-package', description: 'CAD, detailed plans and fit-out information through leasing.' }
  ]);

  global.CapitalData = Object.freeze({
    facts,
    statusMeta,
    spaces,
    resources,
    availabilityMode: 'illustrative',
    availabilityNotice: 'Indicative opportunities for website demonstration. Current availability, areas and commercial terms must be confirmed by the Capital Place leasing team.'
  });
})(window);
