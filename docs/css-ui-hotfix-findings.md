# CSS UI hotfix findings

## Observed regressions

The supplied screenshots showed three root causes: the UI/UX v2 layer added rounded pill backgrounds to active navigation links and language buttons; a global `overflow-wrap:anywhere` rule split headings and card labels at arbitrary characters; and feedback-export `translate` values moved Home/Location copy outside its grid, producing visible left/right clipping.

## Implemented corrections

The header now uses flat navigation links with an underline-only active state. EN/VI controls and Find a Space use square corners. Headings use normal word-boundary wrapping with `text-wrap: balance/pretty`; emphasized phrases are allowed to remain within their parent column. The problematic Home, Location, Amenities and Availability feedback offsets are reset, while intentional image transforms are preserved.

## Verification

Home and Location were reloaded with cache-busting version 8. Computed checks show active nav radius `0px`, CTA radius `0px`, normal heading wrapping, no horizontal overflow on the Home viewport, and no horizontal overflow on Location after the phrase block fix. Final static QA passed across all 15 routes: JavaScript syntax, HTTP responses, diff check, and the existing accessibility audit.
