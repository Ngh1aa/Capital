#!/usr/bin/env python3
"""Legacy page generator guard.

The current Capital Place GitHub Pages site is maintained as hand-authored,
brand-aligned HTML in the repository root. The former generator contains stale
navigation, typography, colours and contact data and must not overwrite those
production-candidate pages.
"""

import sys

LEGACY_GENERATOR_DISABLED = (
    "scripts/build_pages.py is intentionally disabled. "
    "Edit the current root HTML and shared assets directly, then run "
    "`node scripts/qa_capital.mjs`. See README.md and .uiux-profile.json."
)


def main() -> int:
    print(LEGACY_GENERATOR_DISABLED, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
