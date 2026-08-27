# CSS UI hotfix findings

## Observed regressions

The supplied screenshots showed three root causes: the UI/UX v2 layer added rounded pill backgrounds to active navigation links and language buttons; a global `overflow-wrap:anywhere` rule split headings and card labels at arbitrary characters; and feedback-export `translate` values moved Home/Location copy outside its grid, producing visible left/right clipping.

## Implemented corrections

The header now uses flat navigation links with an underline-only active state. EN/VI controls and Find a Space use square corners. Desktop header proportions were restored to the supplied legacy reference: opaque near-black background, 87px inner height, 89px official logo, compact nav gap, and a wider rectangular Find a Space outline. Headings use normal word-boundary wrapping with `text-wrap: balance/pretty`; emphasized phrases are allowed to remain within their parent column. The problematic Home, Location, Amenities and Availability feedback offsets are reset, while intentional image transforms are preserved.

The hero overlay stacking source was corrected in `hero-contrast.css`: elements intended to be viewport-anchored (`facts`, `stats`, `mark`, `status`, `context`, `docs`, and `proof` overlays) are no longer overwritten to `position:relative` by the generic overlay rule. The exception list also protects Home's `.hc-hero-content`. On narrow screens, Resources docs are hidden and Resources/Visit context blocks return to readable flow.

## Verification

The new header reference was measured at 1903×87. Reference groups show an approximately 87px dark header, logo group at x≈163–251, compact navigation cluster around x≈873–1523, language cluster near x≈1548–1565, and CTA outline around x≈1588–1741. The v11 header preserves the compact nav gap and CTA outline width while keeping all controls rectangular.

Round-two desktop/mobile captures covered Home, Location, Resources, Visit, Amenities, Availability, Office and Sustainability. Resources and Visit computed checks confirm their overlay context/docs are positioned correctly; Home confirms centered wordmark and bottom facts are absolute, visible and in-bounds. At the narrow 320px edge case, Home and Resources retain a compact 68px mobile header, readable natural line-breaks, no horizontal clipping, and a bottom action bar that stays below the hero content.

The final regression run passed all 15 route HTTP checks, syntax checks for every JavaScript asset, `git diff --check`, and `scripts/uiux_audit.py`: zero missing image alt text/dimensions, zero buttons without type, and zero duplicate IDs. Final screenshot set contains 18 images at 1521×968, 390×844 and 320×844 for six representative routes.
