# Capital Place Building / Leasing UX Upgrade

## Outcome

Capital Place uses a brand-aligned Grade-A visual language — DM Sans
typography, graphite / cream / brand-orange palette, architectural imagery,
large spacing, editorial composition and restrained motion — while adding the
decision-support layer required for office leasing.

## Verified building foundation

The public-facing facts are centralised in `assets/capital-data.js` and aligned
with the Capital Place official office page as checked in August 2026:

- 93,000 sqm leasable office and retail area.
- Two office towers.
- 37 storeys per tower.
- Grade A office building.
- Dual LEED certification.
- 29 Lieu Giai, Ngoc Ha, Hanoi, Vietnam.
- Hotline: 1800 9289.
- Leasing email: leasing@capitalplace.vn.

This removes the previous 93,700 / 41-storey / `.com.vn` inconsistencies from
the generated public pages.

## P0 — Leasing conversion implemented

### Availability data model

The browser receives a central space entity containing:

- ID, tower, floor and suite reference.
- Area and minimum divisible area.
- Divisibility.
- Availability state and timing copy.
- Fit-out and orientation disclosure.
- Floor-plan relationship.

Supported states:

- Available.
- Available Soon.
- Under Offer.
- Future Availability.
- On Request.
- Leased.

State is communicated by text, line and opacity rather than bright marketplace
badges. Public floor plates are presented as planning references and are not
presented as live commercial data.

### Space Finder

Users can search by:

- Required area.
- Team size with a clearly labelled 10–12 sqm/person planning assumption.
- Target move-in.
- Optional tower preference.

No-match results return the closest opportunities plus future-interest and
leasing actions instead of a dead end.

### Stacking plan and floor detail

The existing stacking-plan visual is retained. It now receives availability
states from central data, routes known opportunities to a detail page, and
provides a compact mobile list instead of forcing users to manipulate the full
tower diagram.

`space.html?id=…` works as the office-space “PDP” with:

- Tower, floor, area and status.
- Timing, divisibility and fit-out disclosure.
- Public illustrative floor plan.
- Indicative capacity and planning range.
- Request Viewing, Request Proposal and detailed-plan actions.
- Graceful invalid or outdated opportunity state.

### Qualified enquiry and viewing

`leasing.html` routes Office, Viewing and Retail enquiries separately. It
preserves selected-space context and captures area, timeline, viewing date /
time, retail brand and category only when relevant.

The public GitHub Pages prototype has no CRM endpoint. Submitting validates the
form, excludes personal data from analytics, and prepares a mailto action rather
than claiming that a request was received by a backend.

## P1 — Building ecosystem implemented

- Retail / F&B landing and dedicated enquiry fields without invented units.
- Existing amenity directory retained and connected to leasing / occupier routes.
- Visitor journey covering address, drop-off, parking, reception and access.
- Leasing resources hub with public and qualified-access layers.
- Occupier gateway that does not expose secure tenant information.
- Sustainability-to-occupier value and resource links.
- Business-focused location shortcut to the visitor guide.
- 404, outdated-space and empty-availability states.

## Accessibility, privacy and measurement

- One main landmark per page and a keyboard skip link.
- Semantic labels, inline errors and focusable success state.
- Keyboard-operable filters and controls.
- Reduced-motion compatibility inherited and extended.
- Mobile sticky CTA on office, availability, floor and retail routes.
- Analytics event names describe intent and exclude personal data.
- Prototype privacy notice explains the mailto-only form behaviour.

## Deferred by design

The following require confirmed business scope or external systems and are not
invented in the static prototype:

- Live inventory or leasing calendar.
- CRM submission and lead-status automation.
- Secure tenant portal, notices and service requests.
- Venue / event hire inventory.
- Public occupier directory.
- CAD, MEP and construction-grade downloadable packages.
- Real-time viewing-slot confirmation.

## Build and validation

Run:

```bash
python3 scripts/build_pages.py
node --check assets/capital-data.js
node --check assets/capital-upgrade.js
node scripts/qa_capital.mjs
```

The QA script validates all generated routes, local dependencies, duplicate
IDs, central facts, availability states and the required leasing-flow hooks.
