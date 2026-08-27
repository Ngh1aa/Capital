# UI/UX audit evidence — observed 2026-08-27

## Browser observations at desktop viewport 1280×1100

| Trang | Quan sát trực tiếp |
|---|---|
| Visit | Compact mode còn Hero, purpose tabs, prepared, lobby, leasing, directions và final CTA. `purposeButtons=5`, active state là `meeting`; section bổ trợ đã được ẩn. Sau khi sửa selector, `scrollHeight≈8154px`. |
| Amenities | Hero vẫn ưu tiên ảnh lớn; The Link directory còn 11 brand buttons và brand state `Highlands Coffee`. Compact mode còn day track, The Link, directory và final CTA; `scrollHeight≈6615px`. |
| Location | Hero, context map, route map, life gallery, day track, neighbourhood map và CTA còn hiển thị; gallery có 4 tab. Business, metro và arrival section riêng đã ẩn; `scrollHeight≈8262px`. |
| Resources | Hero, floor plans, stacking, technical core, role finder, package builder và technical CTA còn hiển thị. Plan tabs có 2 trạng thái, stacking có 20 buttons, technical core có 4 buttons, role finder có 5 tabs; kích thước panel giữ ổn định khi đổi trạng thái. `scrollHeight≈9229px`. |
| Home | Hero và các khối ảnh chính vẫn hiển thị; các min-height editorial đã giảm. Tại desktop, `.hc-community-number` computed font-size là `72px`; finder có 2 mode buttons. `scrollHeight≈12412px`. |

## Content and structure observations

Các trang có phong cách editorial mạnh, sử dụng hero ảnh lớn, tiêu đề display cỡ lớn, nhiều section full-viewport và CTA dạng uppercase nhỏ. Điều này tạo cảm giác premium nhưng làm user phải cuộn nhiều trước khi đến hành động quyết định.

Các interaction chính hiện hữu gồm tabs cho gallery/purpose, brand directory, floor plan, stacking plan, technical topics, role finder và home space finder. Các chức năng này cần được ưu tiên hơn các section kể chuyện bổ trợ.

## Static audit observations

CSS có nhiều pattern `100svh`, `min-height` lớn, `overflow:hidden`, `white-space:nowrap`/`text-wrap:nowrap` và `display:none` do compact mode. Đây là các điểm cần kiểm tra thêm ở breakpoint hẹp, text zoom và anchor behavior. Các trang cần audit sâu hơn về accessible semantics, focus order, reduced motion, image loading và performance.

## Additional static evidence

- `assets/main.js` defines `setLang(l)` only by toggling the `.active` class on the EN/VI buttons; it does not load or swap translated content. This makes the language switcher look functional while not changing the page language.
- The primary navigation exposes Home, Location, Office, Sustainability and Amenities plus Find a Space. Visit and Resources are absent from the desktop and mobile primary menus and are mainly discoverable through footer/secondary routes.
- Static audit found duplicate IDs: `index.html` repeats `scale` and `find-space`; `leasing.html` repeats `la-route-title`; `amenities.html` repeats several brand IDs. These can make fragment links, `getElementById`, `aria-labelledby` and analytics targeting ambiguous.
- `space.html` contains two `<h1>` elements in its file-level audit because the invalid/empty state markup adds its own heading alongside the valid detail state. This needs an explicit state/semantic audit rather than assuming one page state.
- Several pages contain images without explicit width/height attributes: Amenities (8), Leasing (6), Occupiers (23), Resources (6), Retail (11), Space (4), Sustainability (16), Visit (22). This creates avoidable layout-shift risk and weakens perceived performance.
- `retail.html` contains four buttons without explicit `type="button"`; if they ever sit inside or are moved into a form context, they can submit unexpectedly.
- The codebase contains repeated trust qualifiers such as “prototype”, “does not transmit”, “reference only”, “verify current”, “on request” and “subject to confirmation”. These are honest, but their density makes the site feel like a concept/prototype rather than a confident production leasing experience.
- Contrast calculations for sampled token pairs: white on graphite 18.88:1; white 62% on graphite 7.67:1; ink 58% on paper 4.43:1; orange accent `#ff6938` on white 2.87:1. The orange must not be used as normal-size text on white; W3C WCAG 2.2 SC 1.4.3 expects at least 4.5:1 for normal text and 3:1 for large text.[1]
- The design system repeats near-identical per-page tokens (`--ac-*`, `--av-*`, `--hc-*`, `--lc-*`, `--oc-*`, `--sp-*`, `--ss-*`) and many bespoke `clamp()` sizes. The visual language is recognisable, but the implementation currently behaves more like several related microsites than one governed design system.
