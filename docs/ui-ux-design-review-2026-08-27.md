# Capital Place — Design Review UI/UX khắt khe

**Ngày review:** 27/08/2026  
**Phạm vi:** toàn bộ website Capital Place trong repository `Ngh1aa/Capital`  
**Mục tiêu review:** đánh giá khả năng sử dụng, hierarchy, conversion, accessibility, responsive, tính nhất quán và mức độ sẵn sàng production.

## Kết luận điều hành

> **Capital Place đang có art direction tốt hơn UX architecture.** Giao diện tạo được cảm giác cao cấp, giàu hình ảnh và có cá tính; nhưng hiện tại website vẫn giống một bộ editorial microsite/prototype hơn là một hệ thống leasing thực sự sẵn sàng phục vụ quyết định kinh doanh.

Vấn đề lớn nhất không nằm ở việc thiếu hiệu ứng hoặc thiếu hình ảnh. Vấn đề nằm ở chỗ **mọi section đều muốn trở thành “hero”**, trong khi người dùng cần biết rất nhanh: tòa nhà phù hợp với mình không, có mặt bằng nào, làm sao xem thực tế, và bước tiếp theo là gì. Typography cỡ lớn, nhiều section gần full viewport, navigation thiếu các route quan trọng và copy “on request / reference only / verify current” xuất hiện dày khiến trải nghiệm bị chậm, thiếu chắc chắn và giảm lực chuyển đổi.

### Điểm review nội bộ

| Trục | Đánh giá | Nhận xét ngắn |
|---|---:|---|
| Art direction / brand | 8.5/10 | Có cá tính, nhất quán về ảnh, đen–kem–cam và cảm giác premium. |
| Visual hierarchy | 6/10 | Tiêu đề lớn và section full-screen bị lạm dụng nên thứ tự ưu tiên bị phẳng. |
| Information architecture | 5.5/10 | Visit và Resources khó tìm; nhiều route kể cùng một câu chuyện. |
| Conversion | 5.5/10 | CTA có mặt nhưng chưa tạo một “decision path” đủ rõ và đủ tin cậy. |
| Accessibility | 5.5/10 | Có focus style, alt text và reduced-motion ở nhiều nơi, nhưng còn lỗi semantic, contrast accent và state. |
| Performance / stability | 5.5/10 | Nhiều ảnh lớn; nhiều ảnh thiếu width/height; có rủi ro layout shift và tải nặng. |
| Production readiness | 4.5/10 | Language switcher chưa đổi ngôn ngữ; nhiều form còn nói rõ đây là prototype/chưa truyền dữ liệu. |

## Điều đang làm tốt và nên giữ lại

Chất lượng hình ảnh và hướng art direction là tài sản lớn nhất của sản phẩm. Hình ảnh tòa nhà, lobby, The Link, workplace và neighbourhood tạo được ngữ cảnh thật thay vì chỉ dùng ảnh stock. Palette đen, kem và cam tạo nhận diện rõ; các trang có cùng tinh thần nhưng vẫn có biến thể theo chủ đề.

Các interaction chính cũng được chọn đúng hướng: workday gallery, purpose tabs, brand directory, floor plan, stacking plan, technical topics, role finder và space finder đều có giá trị thực tế. Việc giữ các công cụ này tốt hơn nhiều so với biến toàn bộ website thành một chuỗi landing page tĩnh. Nhiều control đã có `type="button"`, `aria-selected`, `aria-pressed`, `aria-expanded` hoặc `:focus-visible`, cho thấy nền tảng accessibility không phải bắt đầu từ số 0.

## Các vấn đề nghiêm trọng cần xử lý trước khi polish tiếp

| ID | Vấn đề | Bằng chứng | Tác động | Mức độ | Effort | Hướng sửa |
|---|---|---|---|---|---|---|
| P0-01 | **Language switcher không thực sự đổi ngôn ngữ.** | `setLang(l)` trong `assets/main.js` chỉ bật class `.active` cho nút EN/VI, không thay text, route, locale hay `document.documentElement.lang`.[2] | Người dùng bấm VI nhưng nội dung vẫn tiếng Anh. Đây là lỗi niềm tin và accessibility, không chỉ là thiếu tính năng. | P0 | M | Hoặc triển khai bản dịch thật theo route/locale, hoặc bỏ switcher cho tới khi nội dung VI sẵn sàng. Không được để control giả hoạt động. |
| P0-02 | **Compact mode đang ẩn nội dung bằng CSS thay vì thiết kế progressive disclosure.** | Các rule `display:none` trong `home-cinematic.css`, `location-cinematic.css`, `amenities-cinematic.css`, `visit-arrival.css` và `resources-library.css`. | Nội dung bị loại khỏi luồng đọc, anchor có thể trỏ tới vùng không hiển thị, SEO và screen-reader semantics bị yếu; người dùng không biết còn nội dung gì. | P0 | M–L | Chuyển các nhóm bị rút gọn thành `<details>`, accordion hoặc tab có trạng thái accessible; giữ summary, `aria-controls`, `aria-expanded`, focus order và deep-link behavior. |
| P0-03 | **Có duplicate ID trong markup.** | `index.html` lặp `id="scale"` và `id="find-space"`; `leasing.html` lặp `id="la-route-title"`; Amenities có nhiều brand ID trùng.[4] | `getElementById`, fragment link, `aria-labelledby`, analytics và screen reader có thể tham chiếu sai phần tử. | P0 | S | Mỗi ID chỉ xuất hiện một lần; đổi ID của wrapper hoặc bỏ ID thừa. Thêm check duplicate ID vào CI. |
| P0-04 | **Accent cam không đủ contrast khi dùng như text trên nền trắng.** | Đo được `#ff6938` trên trắng khoảng `2.87:1`; WCAG SC 1.4.3 yêu cầu tối thiểu `4.5:1` cho text thường và `3:1` cho large text.[1] | Các label/link màu cam nhỏ có thể khó đọc, đặc biệt với low vision và ánh sáng màn hình ngoài trời. | P0 | S | Dùng cam làm nền với chữ đen, hoặc đổi text accent sang màu đậm hơn; không dùng cam nguyên bản cho body/link nhỏ trên nền sáng. |
| P0-05 | **Form và request flow chưa tạo cảm giác production-ready.** | Nhiều form và success state ghi rõ “prototype”, “does not transmit”, “reference only”, “on request”, “verify current”.[5] | Người dùng business không biết gửi yêu cầu đã thành công chưa, dữ liệu đi đâu, ai phản hồi và trong bao lâu. CTA bị biến thành bản demo. | P0 nếu đây là production; P1 nếu vẫn là prototype | M–L | Tách rõ prototype và production. Nếu production: thêm backend/status/email confirmation, consent, privacy link, error/retry và response-time expectation. Nếu chưa production: bỏ language switcher và các CTA giả khỏi public demo. |

## Các vấn đề UX/IA ưu tiên cao

### 1. Navigation không phản ánh toàn bộ hệ thống thông tin

Top navigation hiện chủ yếu có Home, Location, Office, Sustainability, Amenities và Find a Space. **Visit** và **Resources** là hai route quan trọng nhưng bị đẩy xuống footer/secondary discovery. Một visitor cần vào Visit; một broker/architect cần vào Resources. Việc bắt họ tìm qua footer là sai hierarchy, đặc biệt trên mobile nơi menu cũng không đưa hai route này lên nhóm chính.

Khuyến nghị là chuyển navigation thành ba nhóm rõ ràng: **Explore** gồm Location, Amenities, Visit; **Workplace** gồm Office, Availability, Resources; **Leasing** là CTA cố định. Không cần tăng số link hiển thị nếu dùng menu nhóm; điều cần tránh là để route quan trọng chỉ xuất hiện ở footer.

### 2. Trang đang kể chuyện nhiều hơn mức cần thiết cho quyết định thuê

Home, Location, Amenities, Visit và Resources đều có nhiều section editorial với heading display rất lớn. Việc rút gọn vừa triển khai đã làm page ngắn hơn, nhưng cách ẩn bằng CSS chỉ giải quyết phần bề mặt. Về UX, mỗi trang vẫn cần một câu trả lời rõ:

| Trang | Câu hỏi người dùng phải trả lời trong 10–20 giây đầu |
|---|---|
| Home | Capital Place là gì, khác biệt gì, và tôi có thể tìm mặt bằng ở đâu? |
| Location | Địa điểm có thuận tiện cho nhân viên, khách và đối tác không? |
| Amenities | Một ngày làm việc tại đây có đủ tiện ích không? |
| Visit | Tôi đến đâu, chuẩn bị gì và bước tiếp theo là gì? |
| Resources | Tôi cần tài liệu nào để quyết định hoặc đưa vào proposal? |
| Availability | Có mặt bằng phù hợp không và tôi phải làm gì tiếp theo? |

Hiện tại câu trả lời bị phân tán bởi các khối “brand story”, “context”, “scale”, “journey”, “day at address” và “future connectivity”. Hãy giữ ảnh lớn, nhưng giảm mỗi trang về **1 proposition, 1 proof module, 1 decision tool, 1 CTA**. Hình ảnh lớn không đồng nghĩa section phải cao 100svh.

### 3. CTA có nhiều nhưng chưa có một thứ tự ưu tiên đủ mạnh

Các động từ `Explore`, `Discover`, `View`, `Request`, `Book`, `See`, `Open` xuất hiện dày. Vấn đề không phải thiếu CTA mà là người dùng phải tự đoán CTA nào quan trọng nhất. Mỗi trang nên có một primary action duy nhất:

- Home: **Find available space**.
- Location/Amenities: **Book a private tour** hoặc **Explore available spaces**.
- Visit: **Plan your arrival** hoặc **Book a private viewing**.
- Resources: **Request the right package**.
- Availability/Office: **Send requirement to Leasing**.

Các CTA còn lại cần giảm thành secondary link. Tránh để hai nút ở cùng cấp nhưng dẫn tới hai funnel khác nhau nếu không nói rõ sự khác biệt.

### 4. Copy đang có các lỗi làm giảm độ tin cậy

Câu `Make Capital Place is your next address.` trong Home là lỗi ngữ pháp trực tiếp. Nên sửa thành **Make Capital Place your next address.** hoặc tự nhiên hơn là **Make your next address Capital Place.** Ngoài ra, việc dùng lẫn `Hanoi`, `Ha Noi`, `Hà Nội`, `Lieu Giai`, `Liễu Giai` và nhiều dấu `·` cần được chuẩn hoá theo một content style guide.

Các câu như “reference only”, “on request”, “verify current” là cần thiết trong domain leasing, nhưng hiện đang xuất hiện quá thường xuyên và gần như câu nào cũng tự rút lui. Hãy gom disclaimer thành một pattern rõ ở cuối component: **What is public / What Leasing confirms / When you will receive it**. Đừng đặt cảnh báo pháp lý cạnh mọi con số nếu nó làm người dùng mất cảm giác chắc chắn.

## UI visual review

### Typography

Typography có cá tính và phù hợp với bất động sản cao cấp, nhưng display type đang làm quá nhiều việc: hero, section title, card title, metric và CTA đều tranh giành sự chú ý. Thin display face ở kích thước lớn có thể đẹp trên desktop nhưng giảm khả năng đọc khi nằm trên ảnh, ở mobile hoặc khi người dùng zoom.

Nên giới hạn hệ thống về bốn vai trò: `display-xl`, `display-lg`, `heading`, `body/UI`. Heading nội dung nên có measure tối đa, line-height ổn định và không ép `white-space: nowrap` ở desktop rồi mới sửa ở mobile. Các rule `white-space:nowrap`/`text-wrap:nowrap` hiện là rủi ro trực tiếp với dịch thuật, text zoom và viewport hẹp.

### Grid và visual rhythm

Mỗi trang dùng token riêng (`--hc-*`, `--lc-*`, `--ac-*`, `--oc-*`, `--ss-*`…), nhưng nhiều token thực chất có cùng giá trị. Điều này làm code trông có hệ thống nhưng khó kiểm soát thống nhất. Nên có một global token layer cho ink, paper, dark, accent, border, ease, container và spacing; page-specific token chỉ giữ những giá trị thật sự khác.

Khoảng cách và chiều cao đang được điều khiển bởi nhiều `clamp()` và hơn một trăm rule có `svh`. Điều này tạo cảm giác cinematic nhưng khó dự đoán. Cần quyết định rõ section nào là **hero**, section nào là **content**, section nào là **tool**. Chỉ hero/CTA cuối nên gần full viewport; tool và content nên co theo nội dung.

### Imagery

Ảnh là điểm mạnh, nhưng audit thấy nhiều ảnh thiếu `width`/`height`: Amenities 8, Leasing 6, Occupiers 23, Resources 6, Retail 11, Space 4, Sustainability 16 và Visit 22.[4] Đây là rủi ro layout shift và làm trải nghiệm tải trang kém ổn định. Mỗi ảnh cần intrinsic dimensions hoặc `aspect-ratio` theo component. Đặc biệt các gallery chuyển state phải khoá ratio trước khi ảnh mới tải.

Ngoài ra, crop ảnh đang là một phần của hierarchy nhưng chưa có image focal-point system. Cần chuẩn hoá `object-position` theo metadata của từng ảnh thay vì sửa thủ công rải rác trong CSS. Một ảnh đẹp nhưng crop sai mặt người, logo hoặc landmark sẽ phá cảm giác premium ngay lập tức.

## Accessibility và interaction

Một số điểm đã làm tốt là sử dụng semantic button, `aria-selected`, `aria-pressed`, `aria-expanded`, `aria-current` và `:focus-visible` ở nhiều component. Tuy nhiên, không nên kết luận accessibility đạt chỉ vì có attribute. Cần test keyboard end-to-end: Tab vào nav, mở menu, chuyển tab, đổi filter, mở details, gửi form, nhận success/error và quay lại vị trí trước đó.

Focus indicator cần luôn nhìn thấy và không bị che bởi header/sticky section; đây là yêu cầu rõ trong WCAG 2.2 SC 2.4.7.[3] Các tab cần có arrow-key behavior, Home/End behavior nếu triển khai pattern tab chuẩn, và panel cần có `aria-labelledby`/`aria-controls` khớp một-một. Các `display:none` compact section cần tránh làm mất target focus hoặc deep-link.

Các form hiện có nhiều custom field và prototype language. Cần bổ sung trạng thái loading, error cụ thể, success thật, khả năng sửa dữ liệu, privacy/consent, response time và focus vào message sau submit. Một success message “Your brief is ready” nhưng không truyền dữ liệu không phải là completion; nó chỉ là bước chuẩn bị email.

## Responsive và performance

Responsive hiện dựa nhiều vào breakpoint và giảm grid về một cột, nhưng đó mới là responsive layout, chưa chắc là responsive task flow. Cần kiểm tra ở 320px, 375px, 768px, 1024px và text zoom 200%. Các điểm rủi ro lớn là title nowrap, hero content che ảnh/CTA, sticky header che focus, horizontal tab overflow, map label chồng nhau và form dài.

Performance cần được xem như một phần của luxury experience. Hình ảnh lớn là đúng với brand, nhưng cần `srcset`, `sizes`, AVIF/WebP, lazy loading đúng vùng dưới fold, preload có chọn lọc cho hero và không preload nhiều hero phụ. Không nên dùng nhiều ảnh full-resolution chỉ để giữ cảm giác “large image”; cảm giác cao cấp đến từ crop, composition và loading ổn định.

## Những việc cần giữ, sửa và kiểm chứng

| Nhóm | Quyết định |
|---|---|
| **Giữ lại** | Art direction ảnh lớn; palette đen–kem–cam; workday/brand/floor-plan interactions; primary leasing CTA; visible focus style; alt text hiện có; reduced-motion hooks. |
| **Sửa trước khi launch** | Language switcher giả; duplicate IDs; compact `display:none`; accent contrast; form/prototype trust language; navigation thiếu Visit/Resources; lỗi copy “Make Capital Place is…”; width/height ảnh; primary CTA hierarchy. |
| **Kiểm chứng tiếp** | Keyboard-only task completion; screen reader labels; mobile 320–390px; 200% text zoom; Core Web Vitals; form error/recovery; analytics scroll depth và CTA click; user test với tenant, broker, visitor và occupier. |

## Lộ trình đề xuất

**Sprint 1 — Trust và semantics.** Sửa language behavior, duplicate IDs, route navigation, copy lỗi, image dimensions và form states. Đây là nhóm impact cao, effort vừa phải, không cần redesign visual.

**Sprint 2 — Information architecture.** Thiết kế lại primary nav và rút mỗi trang về một decision path. Thay các khối `display:none` bằng accordion/tab có deep-link và accessibility contract. Giữ ảnh lớn nhưng giảm số section full-screen.

**Sprint 3 — Conversion system.** Chuẩn hoá primary/secondary CTA, route context từ Availability → Space Detail → Leasing, và success/error behavior. Đo task completion thay vì chỉ đo scroll depth.

**Sprint 4 — Visual and performance polish.** Gom tokens toàn cục, giới hạn type scale, chuẩn hoá image focal point, tối ưu asset delivery, kiểm tra contrast và responsive ở các viewport thực.

## Verdict cuối

Capital Place **đáng giữ hướng visual hiện tại**, nhưng chưa nên tiếp tục thêm section, thêm animation hoặc thêm card. Nếu chỉ polish thêm, website sẽ càng đẹp nhưng càng khó dùng. Bước đúng tiếp theo là làm cho hệ thống **ít khoe hơn, rõ đường đi hơn và trung thực hơn về trạng thái dữ liệu**.

Tiêu chuẩn để coi bản tiếp theo tốt hơn không phải là “trông premium hơn”. Tiêu chuẩn là: một tenant hiểu giá trị trong vài giây, một visitor tìm được hướng dẫn mà không cần đọc toàn bộ trang, một broker tới được tài liệu đúng trong một lần điều hướng, và một request thật sự cho biết nó đã đi đâu sau khi submit.

## References

[1]: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html "W3C WCAG 2.2 — Contrast (Minimum)"
[2]: https://github.com/Ngh1aa/Capital/blob/main/assets/main.js "Capital Place — assets/main.js"
[3]: https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html "W3C WCAG 2.2 — Focus Visible"
[4]: https://github.com/Ngh1aa/Capital/blob/main/scripts/uiux_audit.py "Capital Place — static UI/UX audit script"
[5]: https://github.com/Ngh1aa/Capital/tree/main "Capital Place — repository"
