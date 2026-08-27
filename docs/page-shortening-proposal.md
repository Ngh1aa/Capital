# Phương án rút gọn cấu trúc các trang Capital

## Mục tiêu

Các trang hiện tại đang ưu tiên cách kể chuyện theo dạng long-form editorial. Cách tiếp cận này giữ được nhiều ngữ cảnh nhưng làm tăng chiều dài cuộn, lặp lại thông điệp và khiến các CTA quan trọng bị phân tán. Phương án dưới đây rút gọn theo nguyên tắc **giữ lại thông tin phục vụ quyết định**, gom các nội dung bổ trợ vào nhóm có thể mở rộng và duy trì các anchor hiện có để không làm hỏng liên kết nội bộ.

> Không nên cắt đồng loạt chỉ bằng cách ẩn nội dung. Nên rút gọn theo từng vai trò của trang: trang thương hiệu kể chuyện ngắn hơn, trang quyết định giữ công cụ và dữ liệu, trang tài nguyên gom các module chuyên sâu.

## Audit nhanh

| Trang | Số section | Số heading | Độ dài HTML tương đối | Đánh giá |
|---|---:|---:|---:|---|
| Home | 7 | 13 | 21 KB | Có thể giảm số màn hình hero/editorial và đưa CTA tìm mặt bằng lên sớm hơn. |
| Location | 10 | 16 | 20 KB | Có thể gộp các khối bản đồ, kết nối và arrival thành một hành trình địa điểm. |
| Amenities | 12 | 23 | 24 KB | Dài do có nhiều khối trải nghiệm gần nhau; nên gom theo 3 nhóm chính. |
| Visit | 17 | 18 | 24 KB | Ưu tiên rút gọn mạnh nhất; nhiều section lặp lại ý định tham quan và hướng dẫn. |
| Resources | 14 | 28 | 28 KB | Nên giữ chiều sâu nhưng chuyển phần kỹ thuật sang tab/accordion hoặc trang con. |
| Sustainability | 13 | 18 | 18 KB | Gom các hệ thống môi trường thành một module có tab và giữ số liệu chính. |
| Office | 8 | 14 | 21 KB | Có thể giữ gần nguyên vì đây là trang phục vụ quyết định thuê. |
| Availability | 9 | 9 | 15 KB | Không cần rút gọn nhiều; đây là trang công cụ và chuyển đổi. |

## Thứ tự ưu tiên triển khai

### 1. Visit: rút gọn mạnh nhất

Giữ lại Hero, một module “plan your arrival”, một panel chọn mục đích, một module hướng dẫn đường đi và CTA cuối trang. Các phần `City context`, `Scale`, `Sequence`, `Boardroom`, `Access`, `Prepared`, `Lobby`, `Tower`, `Ground`, `Minutes` và `Beyond` nên được gom thành ba nhóm accordion: **đến nơi**, **di chuyển trong tòa nhà**, và **trải nghiệm sau khi đến**. Những nội dung có cùng mục đích như “Book a Private Viewing”, “Open in Maps” và “Explore Transport” chỉ nên xuất hiện ở panel mục đích và CTA cuối trang, tránh lặp lại ở nhiều section.

### 2. Amenities: gom theo ba nhu cầu

Giữ Hero, “A day at Capital Place”, The Link directory và CTA. Các khối `The Nexus`, `Meet & host`, `Work & focus`, `Workplace hospitality` và `Wellbeing` nên được gom thành ba tab: **Meet**, **Work**, **Recharge**. Mỗi tab chỉ hiển thị một hình ảnh chính, một đoạn mô tả ngắn và tối đa ba điểm nổi bật. Directory thương hiệu vẫn giữ độc lập vì có chức năng lọc và lựa chọn thương hiệu.

### 3. Location: chuyển thành hành trình một trang ngắn

Giữ Hero, Context, một bản đồ kết nối, Life gallery, Neighbourhood map và CTA. `Business + diplomacy`, `Future connectivity` và `Arrival experience` có thể hợp thành một module “Connected arrival” với ba tab; như vậy vẫn giữ đủ thông tin về môi trường kinh doanh, metro và trải nghiệm đến nơi mà không cần ba section full-height liên tiếp. “A day at the address” nên giữ dạng horizontal track nhưng giảm từ năm thẻ xuống ba thẻ đại diện: **Arrive**, **Work / Meet**, **Dine / Recharge**.

### 4. Home: giảm các màn hình kể chuyện trước CTA

Home nên giữ bảy nhóm chính nhưng giảm chiều cao của các section editorial. `Architecture`, `Workplace`, `Workday` và `LEED` nên có chiều cao theo nội dung thay vì mỗi khối chiếm gần một viewport. CTA “Find your place” nên xuất hiện ngay sau Workday hoặc được ghim một lần ở cuối màn hình đầu tiên trên desktop. Không nên loại bỏ các section này hoàn toàn vì chúng tạo khác biệt thương hiệu; chỉ cần giảm khoảng đệm, số ảnh phụ và số liệu lặp.

### 5. Resources: giữ nội dung nhưng chia tầng thông tin

Resources là trang có lý do chính đáng để dài. Nên giữ các vùng tìm kiếm, floor plans, technical core và role finder ở tầng đầu. Building book, fit-out, sustainability evidence và package builder nên chuyển thành các accordion hoặc liên kết tới trang tài liệu chuyên sâu. Mục tiêu là giúp người dùng đạt được thông tin quyết định trong khoảng ba đến bốn màn hình đầu, thay vì bắt buộc cuộn qua toàn bộ thư viện.

## Quy tắc nội dung đề xuất

| Quy tắc | Cách áp dụng |
|---|---|
| Một section, một nhiệm vụ | Mỗi section chỉ có một heading, một thông điệp và một CTA chính. |
| Giới hạn chiều cao kể chuyện | Các section editorial thường dùng `min-height: 70–85svh`; chỉ Hero và CTA cuối trang nên giữ gần full viewport. |
| Không lặp CTA | Một CTA chính cho mỗi nhóm nội dung; CTA phụ chuyển thành link trong panel hoặc footer. |
| Gom nội dung tương đồng | Dùng tab/accordion cho các nhóm có cùng mục đích thay vì tạo nhiều section full-height. |
| Giữ anchor | Không xóa ID hiện có; nếu gộp section, giữ anchor cũ trên wrapper mới hoặc thêm redirect nội bộ. |
| Mobile ưu tiên nội dung | Trên mobile, ảnh dùng aspect ratio cố định, nội dung bổ trợ có thể thu gọn sau phần tóm tắt. |

## Trạng thái triển khai compact mode

Bản compact mode đã được áp dụng cho **Home, Location, Amenities, Visit và Resources**. Các khối hình ảnh chính, gallery, directory, floor plan, technical core, role finder, package builder và CTA vẫn được giữ; các section mô tả lặp hoặc tài liệu chuyên sâu được ẩn khỏi luồng cuộn chính bằng CSS để ưu tiên ảnh lớn và giảm chữ. Những section bị ẩn vẫn còn trong HTML và Git, vì vậy có thể khôi phục hoặc chuyển thành accordion ở bước tiếp theo.

| Trang | Cách rút gọn đã áp dụng |
|---|---|
| Home | Giảm các min-height full-screen lặp lại, không loại bỏ ảnh chính. |
| Location | Giữ Hero, context, route map, gallery, day track, neighbourhood map và CTA; ẩn các khối business/metro/arrival riêng lẻ. |
| Amenities | Giữ Hero, day track, The Link directory và CTA; ẩn các khối mô tả Nexus/Meet/Focus/Hospitality/Wellbeing/Community/Value. |
| Visit | Giữ Hero, purpose, prepared, lobby, leasing, directions và CTA; ẩn các chuỗi context/sequence/boardroom/access/tower/ground/minutes/beyond. |
| Resources | Giữ floor plans, stacking, technical core, role finder, package builder và CTA; ẩn building book, fit-out, sustainability evidence, location resource và library. |

## Lộ trình triển khai an toàn

Giai đoạn đầu chỉ nên áp dụng cho **Visit, Amenities và Location**, vì đây là ba trang có nhiều section lặp lại nhất. Sau khi kiểm tra analytics, scroll depth và tỷ lệ click CTA, mới quyết định rút gọn Home và Resources. Không nên cắt nội dung Sustainability, Office hoặc Availability trước khi xác định mục tiêu chuyển đổi của từng trang.

Bản compact mode hiện được triển khai trực tiếp trên route hiện tại. Khi đã xác nhận analytics, scroll depth và tỷ lệ click CTA, các section đang ẩn có thể được chuyển thành accordion hoặc feature flag thay vì xóa khỏi HTML. Các anchor chính, tab, form tìm mặt bằng và CTA vẫn cần được kiểm tra trong từng breakpoint trước khi phát hành chính thức.
