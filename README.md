# Capital Place — Building & Leasing Experience

Static editorial website for Capital Place Hanoi, evolved from a building brochure into a leasing decision-support prototype. The experience uses first-party Capital Place facts and imagery, a white / graphite / cream system, restrained orange conversion accents, architectural composition and floor-plan information.

Live site: https://ngh1aa.github.io/Capital/

## Project mode

`INTERACTIVE_PROTOTYPE`

The site is deployed as static GitHub Pages HTML/CSS/JS. It is intentionally truthful about the limits of the prototype:

- no verified live commercial inventory feed;
- no public pricing or commercial terms;
- leasing forms validate locally and prepare an email rather than submitting to a CRM/server;
- English is the only implemented locale;
- analytics event collection outside the browser is not verified in this repository.

See `.uiux-profile.json` and `docs/system-reality.md` before making product, content, visual or integration changes.

## Experience scope

- Image-led homepage narrative establishing twin-tower scale and architectural identity.
- Location, workplace, amenities and sustainability decision pages.
- Central building/contact data with first-party evidence metadata.
- Published 1,847 m² planning reference plus clearly labelled representative prototype planning scenarios.
- Space Finder by area/headcount/timing/tower for early orientation.
- Stacking/floor exploration with leasing-confirmation states rather than fake live vacancy.
- Dynamic space detail with illustrative plan and contextual CTAs.
- Office, viewing, proposal, technical-package and future-interest enquiry routes.
- Retail/F&B, visitor, resources, FAQ and occupier-support routes.
- Keyboard/reduced-motion/mobile interaction support built into shared layers.

Current floors, divisibility, pricing, timing and terms must be confirmed by Capital Place Leasing.

## Brand and content basis

Core project palette:

- `#231F20` graphite/black
- `#252525` charcoal
- `#F0EFE9` cream
- `#FFFFFF` white
- `#D9D9D9` line/neutral
- `#F15F22` primary conversion accent token

Public facts and photography are based on Capital Place first-party sources. The current evidence review date is stored in `assets/capital-data.js`.

## V3.1 design direction

The shared v3 layer uses an **architectural editorial + building-directory + floor-plan precision** grammar:

- planar controls rather than generic rounded SaaS chrome;
- safe DOM section rules rather than pseudo-element overrides that can collide with cinematic overlays;
- wide-screen-only building directory navigation;
- route-aware navigation and truthful utility-page contrast;
- full-screen mobile navigation with focus/state synchronization;
- safe-area-aware mobile leasing actions;
- unavailable VI state until Vietnamese content is actually implemented;
- a clear bridge from the local prototype privacy explanation to Twin-Peaks' first-party privacy notice.

## Source ownership

The deployable source is the root HTML plus shared files under `assets/`.

`scripts/build_pages.py` is intentionally disabled. Its former generated templates contained stale visual/content assumptions and must not overwrite the current brand-aligned pages.

## Local preview

```bash
python3 -m http.server 4173
```

## Quality checks

```bash
node --check assets/main.js
node --check assets/capital-data.js
node --check assets/capital-upgrade.js
node --check assets/capital-vision.js
node --check assets/capital-uiux-v2.js
node scripts/qa_capital.mjs
```

GitHub Actions also runs these static/source checks on pushes to `main` and on pull requests via `.github/workflows/qa-capital.yml`.

A static QA pass is not a browser, screen-reader, WCAG-conformance or field-performance proof. See `docs/verification-matrix-v3.md` for verified and unverified gates.

## Key documentation

- `docs/CAPITAL-PRE-DESIGN-RESEARCH-V3.md`
- `docs/visual-signature.md`
- `docs/system-reality.md`
- `docs/verification-matrix-v3.md`
- `docs/capital-building-ux-upgrade-implementation.md`
