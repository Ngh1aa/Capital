# Media Frame System

`media-frame.css` là một design primitive portable cho các project có photography, video, gallery và visual section. Hệ thống chuẩn hóa bốn quyết định: **tỷ lệ khung, cách fit media, focal point và responsive behavior**.

## Nguyên tắc bắt buộc

Photography và video dùng `object-fit: cover` để giữ tỷ lệ rồi crop phần dư. Logo, floor plan, diagram, bản đồ và technical visual dùng `object-fit: contain` để không cắt mất nội dung. Không dùng selector toàn cục kiểu `[class*="hero"] img` vì có thể làm hỏng asset không phải photography.

`object-fit` không thể khôi phục chi tiết của một ảnh nguồn có độ phân giải thấp. Ảnh phải có kích thước pixel đủ lớn so với kích thước hiển thị lớn nhất; ảnh portrait không nên bị ép vào khung ultra-wide nếu việc crop làm mất chủ thể.

## Markup cơ bản

```html
<div class="media-frame media-frame--cinematic" data-focus="right">
  <img src="green-station.webp" alt="Green Station at Capital Place" loading="lazy">
</div>
```

Có thể dùng `style="--media-position: 58% 45%"` cho trường hợp cần focal point chính xác. Các giá trị shortcut là `center`, `top`, `bottom`, `left` và `right` thông qua `data-focus`.

## Preset

| Preset | Tỷ lệ/chiều cao | Dùng cho |
|---|---:|---|
| `media-frame--hero` | `min-height: clamp(...)` | Hero lớn; giữ min-height editorial riêng nếu section full-bleed |
| `media-frame--cinematic` | `1.85 / 1` | Full visual và banner ảnh lớn |
| `media-frame--landscape` | `16 / 9` | Gallery, section image, card ngang |
| `media-frame--wide` | `3 / 2` | News, community, supporting photography |
| `media-frame--portrait` | `4 / 5` | Architecture/detail/portrait card |
| `media-frame--square` | `1 / 1` | Brand thumbnail và tile vuông |
| `media-frame--contain` | Fit modifier | Logo, map, diagram, floor plan, technical visual |

## Áp dụng cho Capital

Hero và full-bleed overlay của Home, Location, Office, Sustainability, Amenities, Availability, Space, Leasing, Retail, Visit, Resources và Occupiers vẫn giữ chiều cao, stacking và gradient riêng của page. Media Frame System được dùng như primitive cho các wrapper photography/card; không thay thế mù quáng các section có composition đặc biệt.

Các ảnh technical hiện có như tower section, floor plan, metro map, neighbourhood map và logo phải giữ `contain` hoặc rule chuyên biệt. Các ảnh photography trong gallery/mosaic/card dùng `cover` với `data-focus` khi cần giữ chủ thể khỏi vùng crop.

## Responsive image guidance

Khi có đủ biến thể nguồn, dùng `<picture>`/`srcset` và `sizes` để trình duyệt chọn asset phù hợp với viewport. Không tạo `srcset` giả bằng cách lặp cùng một file; nếu chỉ có một asset gốc, ưu tiên asset đủ độ phân giải và giữ `loading="lazy"` cho ảnh ngoài viewport.

Đối với mobile, kiểm tra lại focal point vì khung thường cao hơn và crop khác desktop. Không đặt chữ quan trọng trong vùng dễ bị crop. Mọi ảnh thay thế phải được kiểm tra cả natural dimensions, rendered dimensions, `object-fit`, `object-position` và trạng thái tải lazy. Trong Capital, chạy `python3 scripts/qa_media_frame_system.py` để kiểm tra stylesheet coverage, preset coverage, đường dẫn ảnh và cảnh báo nguồn ảnh nhỏ.
