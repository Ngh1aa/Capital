# Capital Place — Verification Matrix v3.1

Date: 2026-09-01

`PASS` below means the named source/static check passed in the recorded environment. It does not mean browser, accessibility conformance, field performance or business-outcome validation unless explicitly stated.

| Change | Expected outcome | Verification | Pass condition | Current result |
|---|---|---|---|---|
| Project context profile | future agents read project truth before generic skill rules | static QA parses `.uiux-profile.json` | profile exists; source-of-truth and constraints registered | PENDING CI |
| Legacy generator guard | stale black/gold/contact templates cannot overwrite current site by accident | static QA | guard marker exists; obsolete email absent | PENDING CI |
| Evidence ledger in data | official vs representative floor information stays distinguishable | static QA | source date/URL + evidence labels present | PENDING CI |
| V3 orange token reuse | no duplicate accent hardcode in v3 layer | static QA | v3 uses `var(--cta-orange)` and no literal CTA hex | PENDING CI |
| Architectural section rule | domain cue does not collide with cinematic pseudo-element overlays | source assertion | DOM `.cpv3-section-rule` exists; generic section `::before` pattern absent | PENDING CI |
| Desktop directory guard | fixed directory does not cover normal 1280–1440 content | CSS assertion | only displayed at >=1760px; shown after scroll | PENDING CI |
| Mobile menu | full-screen menu, body lock, 48px link targets, Escape/focus loop and icon sync | source/static QA | state sync + fixed menu + focus loop present | PENDING CI; browser keyboard test UNVERIFIED |
| Mobile action dock | fixed conversion actions do not collide with iOS home indicator | CSS assertion | safe-area inset included; body bottom space reserved | PENDING CI; device test UNVERIFIED |
| Language integrity | VI control cannot make English content claim to be Vietnamese | source/static QA | `<html lang>` remains English; VI exposes unavailable state | PENDING CI |
| Utility nav contrast | pages without image hero do not start with white-on-white navigation | source/static QA | no-hero detection adds `cu2-nav-solid` | PENDING CI; rendered contrast UNVERIFIED |
| Prototype privacy bridge | local mailto disclosure and first-party Twin-Peaks notice remain distinct | source/static QA + first-party web evidence | official notice link injected without changing prototype truth | PENDING CI |
| Leasing success truth | form never claims server/CRM receipt | static HTML assertion | prepared-not-transmitted copy remains | PENDING CI |
| Availability truth | reference data never becomes live commercial inventory by implication | data/static QA | leasing-confirmation mode + representative evidence label retained | PENDING CI |

## Browser / device matrix still required before a production claim

- Chromium: ~375, ~768, ~1280, 1760+.
- Safari/WebKit: mobile safe-area, fixed menu/dock, backdrop-filter fallback.
- Firefox: sticky/fixed nav and form controls.
- Keyboard: menu open/Tab loop/Shift+Tab/Escape/focus return; tabs; leasing form errors.
- Zoom/reflow: 200% desktop and narrow mobile.
- Screen reader: nav current-state, form labels/errors, prepared-not-sent state, dynamic directory.

Status: `UNVERIFIED` in the current connector-only execution environment.

## Performance status

No field RUM/CrUX baseline was available in this implementation pass. No claim of Core Web Vitals improvement is made. The v3.1 change adds no framework or third-party runtime dependency; it uses native DOM, IntersectionObserver and existing assets. A lab/field performance pass remains required if this becomes a production release target.

## Release / rollback

The previous known-good source commit before v3.1 is `d17a5325d157093ce65c61438bef017943b5b522`. Prefer a safe revert or prior GitHub Pages deployment rollback if post-deploy smoke reveals a regression; do not rewrite history as the default rollback mechanism.
