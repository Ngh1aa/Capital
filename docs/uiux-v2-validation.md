
# UI/UX v2 validation notes

## Shell integration

At the 1280px desktop viewport, the primary navigation now exposes Home, Location, Office, Sustainability, Amenities, Visit, Resources and Find a Space without clipping. Language buttons have accessible labels and the mobile action shell is present in the DOM for narrow viewports.

The Home flow was exercised through the team-size mode of the space finder. The result reported the expected mode change, language preview state, 100% scroll progress at page end and visible back-to-top control. The four Home content tabs support ArrowRight keyboard navigation and move focus to the next selected tab.

The mobile menu regression was identified and fixed: the original `main.js` hamburger handler was being double-bound by the v2 shell, causing a click to open and immediately close the menu. The duplicate listener was removed; the shell now observes the existing menu state, supports outside click and Escape close, and keeps `aria-expanded` synchronized.

## Main flow validation

Availability loaded with area/team-size controls, timing/tower/fit-out filters, floor stack buttons, reference cards, floor detail links and save/compare actions. The floor selection flow produced the expected `space.html` and `leasing.html` context links.

Leasing loaded with `intent=viewing`, changed its route title and conditional fields, preserved the live route note, and produced seven validation messages when submitted empty. The success state remained hidden until validation passes.

## Static quality gates

All JavaScript files pass `node --check`; all 15 HTML routes pass local HTTP smoke tests; `git diff --check` passes. The static UI audit now reports zero missing image dimensions, zero missing alt attributes, zero buttons without explicit type and no duplicate IDs on the audited pages.

## Visual smoke findings

Chromium headless screenshots were generated at 1440×1000 and 390×844 for Home, Availability, Leasing, Visit and Resources. Home mobile keeps the landmark image dominant, displays a readable header/hamburger and a clear two-action fixed bar. Leasing mobile keeps the hero image/copy strong and the fixed CTA bar remains separated from the hero content rather than covering the main copy. The screenshot review confirms the image-first direction is preserved on narrow screens.
