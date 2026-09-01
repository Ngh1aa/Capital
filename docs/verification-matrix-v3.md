# Capital Place — Verification Matrix v3.1

Date: 2026-09-01

`PASS` means the named source/static/deployment check passed in the recorded environment. It does not mean browser, assistive-technology, WCAG-conformance, field-performance or business-outcome validation unless explicitly stated.

| Change | Expected outcome | Verification | Pass condition | Result |
|---|---|---|---|---|
| Project context profile | future agents read project truth before generic skill rules | GitHub Actions static QA | profile parses; source-of-truth and constraints registered | PASS |
| Legacy generator guard | stale black/gold/contact templates cannot overwrite current site by accident | GitHub Actions static QA | guard marker exists; obsolete email absent | PASS |
| Evidence ledger in data | official vs representative floor information stays distinguishable | GitHub Actions static QA | source date/URL + evidence labels present | PASS |
| V3 orange token reuse | no duplicate accent hardcode in v3 layer | GitHub Actions static QA | v3 uses `var(--cta-orange)` and no literal CTA hex | PASS |
| Architectural section rule | domain cue does not collide with cinematic pseudo-element overlays | source assertion | DOM `.cpv3-section-rule` exists; generic section pseudo-element override absent | PASS |
| Desktop directory guard | fixed directory does not cover normal 1280–1440 content | source assertion | only displayed at >=1760px; revealed after scroll | PASS at source level; rendered wide-screen QA UNVERIFIED |
| Mobile menu | full-screen menu, body lock, 48px targets, Escape/focus loop and icon sync | JS/CSS syntax + source QA | state sync + fixed menu + focus loop present | PASS at source level; manual keyboard/browser QA UNVERIFIED |
| Mobile action dock | fixed conversion actions do not collide with iOS home indicator | CSS source QA | safe-area inset included; body bottom space reserved | PASS at source level; device QA UNVERIFIED |
| Language integrity | VI control cannot make English content claim to be Vietnamese | source QA | `<html lang>` stays English; VI exposes unavailable state | PASS |
| Utility nav contrast | pages without image hero do not start with white-on-white navigation | source QA | no-hero detection adds `cu2-nav-solid` | PASS at source level; rendered contrast QA UNVERIFIED |
| Prototype privacy bridge | local mailto disclosure and first-party Twin-Peaks notice stay distinct | source QA + first-party web evidence | official notice link injected without changing prototype truth | PASS |
| Leasing success truth | form never claims server/CRM receipt | static HTML assertion | prepared-not-transmitted copy remains | PASS |
| Availability truth | reference data never becomes live inventory by implication | data/source QA | leasing-confirmation mode + representative evidence label retained | PASS |
| Legacy deep links | existing fragment URLs still reach equivalent current sections | source QA + runtime alias contract | known obsolete fragments mapped to current sections | PASS at source-contract level; browser fragment smoke UNVERIFIED |
| Repository QA workflow | every push/PR checks syntax, local dependencies, evidence and reality contracts | GitHub Actions run #2 | workflow conclusion success | PASS |
| GitHub Pages deployment | latest tested source is accepted by Pages | Pages deployment run #115 | conclusion success | PASS |

## Recorded CI / deploy evidence

- Source commit tested: `e042778cf74c1b61d3237555a3f78bd9705d43c6`.
- `Capital website QA` run #2: `SUCCESS`.
- `pages build and deployment` run #115: `SUCCESS`.
- The custom QA currently covers 15 public HTML routes plus shared CSS/JS/data contracts.

## Rendered / browser status

The current execution environment could not fetch `https://ngh1aa.github.io/Capital/` after deployment because of network/cache restrictions. Therefore post-deploy rendered smoke remains `UNVERIFIED`, even though the Pages deployment itself succeeded.

Before a production claim, still test:

- Chromium: ~375, ~768, ~1280, 1760+.
- Safari/WebKit: mobile safe-area, fixed menu/dock, backdrop-filter fallback.
- Firefox: sticky/fixed nav and form controls.
- Keyboard: menu open/Tab loop/Shift+Tab/Escape/focus return; tabs; leasing form errors.
- Zoom/reflow: 200% desktop and narrow mobile.
- Screen reader: current-page state, form labels/errors, prepared-not-sent state, dynamic directory.

## Performance status

No field RUM/CrUX baseline was available in this implementation pass. No Core Web Vitals improvement claim is made. V3.1 adds no framework or third-party runtime dependency; it uses native DOM, IntersectionObserver and existing assets.

## Known remaining issues

- `capital-upgrade.js` still uses analytics event names beginning with `submit_` for a mailto-preparation flow. The visible UI is truthful, but analytics naming should be migrated to `prepare_*` before a real measurement schema is locked. Priority: P2.
- FAQ description is supplied through the central document-metadata compatibility layer rather than static head markup. Direct static metadata is preferable for SEO when that page is next edited. Priority: P2.
- Live CRM, authoritative vacancy feed, Vietnamese locale, cross-browser/AT proof and field performance telemetry remain unconnected/unverified by design. See `docs/system-reality.md`.

## Release / rollback

The pre-v3.1 source checkpoint is `d17a5325d157093ce65c61438bef017943b5b522`. Prefer a safe revert or prior GitHub Pages deployment rollback if a rendered regression is discovered; do not rewrite history as the default rollback mechanism.
