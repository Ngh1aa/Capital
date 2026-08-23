# Capital Place — Building & Leasing Experience

Static editorial website for Capital Place Hanoi, upgraded from a building
brochure into a usable leasing decision-support experience while preserving
the original premium visual direction.

Live site: https://ngh1aa.github.io/Capital/

## Experience scope

- Central building and contact data.
- Indicative office availability with six meaningful states.
- Space Finder by area, headcount, move-in timing and tower.
- Interactive stacking plan and mobile opportunity list.
- Dynamic floor detail with illustrative plan, capacity and contextual CTAs.
- Office enquiry, viewing request, proposal, technical package and future-interest flows.
- Dedicated Retail / F&B enquiry routing.
- Visitor guide, leasing resources and occupier gateway.
- Accessible form states, reduced-motion support and privacy-safe analytics events.

Availability on this public portfolio prototype is explicitly labelled as
illustrative. Current inventory and commercial terms must be confirmed by the
Capital Place leasing team. Forms prepare an email and do not transmit personal
data to a CRM.

## Build

```bash
python3 scripts/build_pages.py
```

The original page generator remains the base visual source. The build-time
upgrade in `scripts/ux_upgrade.py` applies the leasing UX layer and creates the
additional routes.

## Quality checks

```bash
node --check assets/capital-data.js
node --check assets/capital-upgrade.js
node scripts/qa_capital.mjs
```

Implementation details are documented in
`docs/capital-building-ux-upgrade-implementation.md`.
