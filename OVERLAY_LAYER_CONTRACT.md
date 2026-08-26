# Image Overlay Layer Contract

All image-led sections use the same stacking order: **image/media at layer 0, gradient overlay at layer 1, and text or controls at layer 2**. The shared contract is appended to `assets/hero-contrast.css` and loaded by the 13 static pages that contain image-led sections.

The patch corrects legacy `z-index: -1` shade rules that placed gradients behind images inside isolated sections. It preserves existing typography, layout and image treatment while ensuring the gradient remains between the media and foreground copy.

## Covered section families

The contract covers the Home, Location, Office, Availability, Sustainability, Amenities, Space, Leasing, Retail, Visit, Resources and Occupiers overlay sections, plus the FAQ/shared page-header treatment. It includes the naming variants used by the markup, notably `.la-scale-section` and `.rl-full-band`.

## Special media structures

Home Address uses `.hc-address-media` as an image wrapper, so the wrapper is explicitly assigned layer 0. Home Community uses `.hc-community-media` for the image and `::after` for its existing gradient; these are explicitly assigned layers 0 and 1, while `.hc-community-copy` is layer 2. Amenities' hero montage is kept as a single layer-0 image plane. LEED panels on Home and Sustainability use a card-level image 0 → shade 1 → copy 2 stack.

All shade layers have `pointer-events: none`, so links, buttons and other interactive controls remain usable. No Google Static Maps credential is part of this change.
