# Reading Project — Open Source, cho mọi trẻ em

## Tên dự án — cảnh báo trùng tên (2026-10-29)
Tên ứng cử "English for Kids" đã bị dùng rất nhiều, không nên dùng làm thương hiệu riêng:
- App "English For Kids" của LangsForKids trên Google Play từ tháng 8/2020, 8,1 triệu lượt cài, 4,53 sao.
- Nhiều website: englishforkids.site, .info, .ru, .com.es, .com.ve và nhiều repo/bài tập cùng cụm từ này.
- Repo GitHub thì tên chỉ duy nhất trong một tài khoản, nên về kỹ thuật vẫn tạo được repo `english-for-kids` dưới tài khoản của bạn, nhưng người dùng sẽ nhầm với các app/website trên.
Khuyến nghị: chọn tên riêng khác biệt cho dự án, giữ "English for kids" chỉ làm mô tả ("open English reading for kids").

## Giao diện
Toàn bộ giao diện bằng tiếng Anh (chốt 2026-10-29).

Dự án đọc gốc, lấy cảm hứng từ vòng lặp học của Reading Eggs nhưng KHÔNG copy nội dung, nhân vật, sách hay thương hiệu của Reading Eggs.

## Mục tiêu
- Làm thật tốt 20–30 bài đầu, rồi nhân lên 4.000 bài/truyện ở mọi cấp độ.
- Ai cũng tiếp cận được: miễn phí, mã nguồn mở, chạy máy yếu, không cần API key trả phí, không quảng cáo, không thu thập dữ liệu trẻ em.

## Ba trụ chất lượng, ngang nhau
1. Nội dung đúng lộ trình khoa học đọc: chữ → âm → ghép âm → từ decodable → câu → truyện.
2. Audio chuẩn, nhất quán: một giọng kể người lớn, rõ, chậm, ấm; đọc đúng âm phonics, không dùng giọng TTS trình duyệt cho sản phẩm thật.
3. Minh họa đúng phong cách, đúng nghĩa: một style duy nhất, nhân vật cố định, hình khớp câu chữ, có alt text.

## Cách tiếp tục làm việc này, kể cả khi đổi VM hay đổi cuộc trò chuyện
ĐỌC FILE NÀY TRƯỚC, rồi đọc `STATUS.md` và `ROADMAP.md`. Mọi quyết định quan trọng đều ghi vào file, không chỉ nằm trong trí nhớ chat hay trong đầu một phiên làm việc. Xem chi tiết ở `docs/PERSISTENCE.md`.

## Cấu trúc
- `docs/` — curriculum, audio guide, illustration guide, QA checklist, persistence.
- `content/lessons/` — bài học, mỗi bài một file JSON theo schema ở `content/schema.md`.
- `content/stories/` — truyện, mỗi truyện một file JSON, chỉ dùng âm/từ đã học ở cấp độ đó.
- `assets/audio/` — file MP3 đã tạo, đặt tên theo id bài/truyện, không đặt tên lung tung.
- `assets/images/` — hình WebP đã tối ưu, có alt text trong file JSON tương ứng.
- `scripts/` — script kiểm tra chất lượng, chạy được lại trên máy mới.
- `app/` — code app (sẽ tách repo app riêng khi chốt, hoặc giữ ở đây cho tới lúc đó).

## Giấy phép (dự kiến, chưa chốt cuối)
Mã nguồn và nội dung gốc: Apache-2.0 hoặc MIT, để ai cũng dùng, sửa, dịch được. Model TTS/hình ảnh dùng kèm phải có giấy phép mở tương thích, ghi rõ trong từng guide.
