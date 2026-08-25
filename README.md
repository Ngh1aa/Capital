# Capital Place — Building & Leasing Experience

Static editorial website for Capital Place Hanoi, upgraded from a building
brochure into a usable leasing decision-support experience. The interface now
uses the official black, cream and orange visual system and public Capital
Place imagery rather than an unrelated black-and-gold luxury treatment.

Live site: https://ngh1aa.github.io/Capital/

## Experience scope

- Central building and contact data.
- Two public reference floor plates with leasing-led availability confirmation.
- Space Finder by area, headcount, move-in timing and tower.
- Interactive stacking plan and mobile opportunity list.
- Dynamic floor detail with illustrative plan, capacity and contextual CTAs.
- Office enquiry, viewing request, proposal, technical package and future-interest flows.
- Dedicated Retail / F&B enquiry routing.
- Visitor guide, leasing resources and occupier gateway.
- Accessible form states, reduced-motion support and privacy-safe analytics events.

No live inventory schedule or commercial terms are presented. Current floors,
divisibility, pricing and terms must be confirmed by the Capital Place leasing
team. Forms prepare an email and do not transmit personal data to a CRM.

## Brand and content basis

- Core palette: `#231F20`, `#252525`, `#F0EFE9`, `#FFFFFF`, `#D9D9D9`, `#F15F22`;
  `#A63C12` is reserved for accessible small orange text on light surfaces.
- Public facts and photography are based on capitalplace.com.vn.
- Capital Place opened in 2020; the project comprises two 37-storey towers and
  approximately 93,000 m² of office space.
- Gold appears only where it is part of the factual LEED Gold certification,
  not as a brand accent.

## Local preview

```bash
python3 -m http.server 4173
```

The HTML and shared assets in this repository are the deployable source for
GitHub Pages. The original generator scripts are retained as project history;
do not run them over the brand-aligned pages without first reconciling their
legacy templates.

## Quality checks

```bash
node --check assets/capital-data.js
node --check assets/capital-upgrade.js
node scripts/qa_capital.mjs
```

Implementation details are documented in
`docs/capital-building-ux-upgrade-implementation.md`.
