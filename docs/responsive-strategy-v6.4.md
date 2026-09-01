# Capital Place V6.4 — Responsive & Device Strategy

Status date: 2026-09-01

## Scope

This is the mobile/device contract for the V6 Architectural Editorial × Leasing Blueprint implementation. It supplements the visual design contract without changing verified building facts or system reality.

## Skills applied

- `responsive-and-device-strategy`
- `accessibility`
- `interaction-patterns-and-form-ux`
- `ui-craft-and-visual-qa`

## Mobile problems remediated

1. Mobile navigation did not trap focus and used a basic `overflow:hidden` body lock.
2. The language control disappeared below 1180px.
3. The third home fact (`37 storeys each`) was hidden below 600px.
4. Hero CTAs could become cramped at 320–390px.
5. Footer/contact text links did not consistently expose 44px touch targets.
6. Mobile form fields needed an explicit 16px input size to avoid iOS focus zoom.
7. Fixed navigation and full-screen menu did not explicitly account for notch/home-indicator safe areas.
8. Location hero copy could run under the vertical address stripe on narrow screens.
9. Amenities montage became too dense at narrow mobile widths.
10. 320–360px and short landscape viewports did not have dedicated hardening rules.
11. Fixed-header anchor jumps needed `scroll-margin-top` protection.
12. Long email/contact strings needed explicit reflow protection.

## Breakpoint rationale

The existing V6 desktop-first architecture is retained to avoid unnecessary visual-system churn. The V6.4 responsive owner provides a final device contract at these content thresholds:

| Range | Role | Main decisions |
|---|---|---|
| `<= 900px` | tablet / mobile navigation mode | full-height menu, safe area, focus/scroll behavior, single-column page compositions |
| `<= 600px` | narrow content mode | stacked CTAs, tighter type scale, one-column task flows, mobile image/copy recomposition |
| `<= 360px` | small-mobile hardening | reduced logo/header footprint, 16px gutters, smaller display ceiling |
| short landscape `<= 900px` + `max-height:600px` | landscape hardening | 64px mobile nav, reduced vertical hero padding, dynamic viewport media |

These thresholds are based on content pressure rather than named device models.

## Mobile navigation contract

- Menu button is at least 44×44 CSS px.
- `aria-expanded`, `aria-controls` and accessible open/close labels are synchronized.
- Navigation receives an accessible name if source markup omitted one.
- Open menu locks page scroll while preserving and restoring scroll position.
- Focus remains inside the menu/button loop while open.
- Escape closes and returns focus to the menu button.
- Menu content scrolls independently on short screens.
- Language controls remain present on mobile when provided by the page.
- Safe-area top/right/left/bottom values are respected.

## Touch contract

For coarse pointers, primary/secondary CTA, inline action links, navigation links, footer links, contact links and FAQ summaries expose at least a 44px interaction height.

WCAG 2.2 AA requires a 24×24 CSS pixel minimum target or sufficient spacing; this project intentionally uses the more generous 44px product target for key mobile controls.

## Typography / reflow contract

- Mobile H1/display: `42–58px`, with a smaller 320–360px ceiling.
- Mobile H2: `36–50px`.
- Body remains 16px minimum in core mobile content.
- Inputs/selects/textarea are explicitly 16px on narrow mobile to avoid iOS auto-zoom.
- Long contact strings use `overflow-wrap:anywhere`.
- No primary building fact is hidden to make the layout fit.
- Hero action groups stack below 600px.

## Media contract

- Mobile media heights are reduced from desktop while preserving useful crop.
- Amenities hero drops decorative side montage pseudo-images below 600px instead of compressing three image columns into a narrow viewport.
- Floor-plan raster remains a constrained preview and is not promoted to a large mobile hero.
- Existing V6.3 text-on-image local contrast treatments remain in force.

## Safe area / viewport contract

Every public HTML route uses:

`width=device-width, initial-scale=1.0, viewport-fit=cover`

V6.4 consumes `safe-area-inset-*` for the fixed header, mobile navigation panel and footer.

## Test matrix

### P0 widths

- 320px — small mobile / reflow edge
- 360px — common Android narrow width
- 375px — standard mobile
- 390px — current iPhone-class width
- 414px — large mobile
- 600px — narrow/tablet transition
- 768px — tablet portrait

### Additional states

- short landscape viewport (`max-height:600px`)
- coarse pointer
- reduced motion
- forced colors
- keyboard menu open / Tab / Shift+Tab / Escape
- 200% browser zoom / effective narrow reflow
- form focus on iOS-class viewport
- anchor jumps under fixed navigation

## Automated regression gate

`scripts/qa_mobile_v6.mjs` verifies:

- all 15 routes load the V6.4 responsive owner;
- viewport zoom is not disabled;
- `viewport-fit=cover` is present;
- safe-area and `100dvh` contracts exist;
- 44px touch target rules exist;
- 16px mobile form field rule exists;
- home third fact is restored rather than hidden;
- narrow hero CTAs stack;
- 320–360px and landscape hardening exist;
- long-copy overflow protection exists;
- mobile language control is restored;
- location stripe collision guard exists;
- menu focus loop / Escape / scroll restoration exist.

## Evidence limitation

Static source and CI assertions are not a substitute for rendered visual QA. A final visual PASS still requires representative screenshots or a browser render at the matrix widths above. If that evidence is unavailable, report rendered mobile QA as `UNVERIFIED`, even when CI is green.
