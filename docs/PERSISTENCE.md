# PERSISTENCE — Làm sao vẫn nhất quán khi thay VM

Vấn đề: VM của Lara có thể bị thay thế thường xuyên. Cuộc trò chuyện cũng bị tóm tắt (compaction) và mất chi tiết. Nếu dự án chỉ nằm trong chat, nó sẽ mất hoặc lệch dần.

## Nguyên tắc: file là sự thật, chat chỉ là nơi làm việc

1. **Một nguồn sự thật duy nhất: thư mục này.**
   Mọi quyết định, lộ trình, chuẩn chất lượng, danh sách bài, trạng thái đều nằm trong file ở `~/workspace/reading-project/`, không chỉ trong MEMORY.md hay trong chat.

2. **Cái gì sống sót qua thay VM, cái gì không:**
   - SỐNG SÓT: mọi thứ trong `~` (home), gồm `~/workspace/`, `~/MEMORY.md`, `~/workspace/tools/`.
   - KHÔNG SỐNG SÓT: `/tmp`, các gói cài bằng apt vào hệ thống, tiến trình đang chạy, file ngoài home, cài đặt hệ thống tùy chỉnh.
   - Vì vậy: KHÔNG để tài sản dự án ở `/tmp`, KHÔNG dựa vào tool cài hệ thống mà không có script cài lại, KHÔNG để trạng thái chỉ trong tiến trình chạy nền.

3. **Remote là bản sao an toàn nhất:**
   Đẩy repo này lên GitHub (khi có tài khoản và người dùng đồng ý) sau mỗi đợt làm việc. Khi đó VM mới chỉ cần `git clone` là lấy lại toàn bộ lịch sử, quyết định và nội dung. Home chỉ là bản làm việc, GitHub mới là bản công khai và bền vững.
   - Chưa đẩy lên GitHub thì vẫn phải giữ nguyên thư mục này, không xóa, không di chuyển lung tung.
   - Mỗi đợt xong: commit với thông điệp rõ ràng, ví dụ `content: add lessons 01-05, QA passed`.

4. **Khởi động lại trên VM mới, theo đúng thứ tự này:**
   1. Đọc `README.md`, `STATUS.md`, `ROADMAP.md` trong thư mục này.
   2. Chạy `scripts/setup.sh` để cài lại tool vào `~/workspace/tools/` (không cài lung tung ra hệ thống nếu không cần).
   3. Chạy script kiểm tra `scripts/validate.py` để xem nội dung hiện tại còn đủ và đúng chuẩn không.
   4. Làm tiếp từ mục "Bài tiếp theo cần làm" trong `STATUS.md`, không làm lại từ đầu, không đoán lại quyết định cũ.
   5. Cập nhật `STATUS.md` ngay khi xong đợt.

5. **Đặt tên và id ổn định:**
   - Bài học: `lesson-001`, `lesson-002`, ... không đổi id khi sửa nội dung.
   - Truyện: `story-001`, ...
   - Audio: `assets/audio/lesson-001.mp3`, `assets/audio/story-001.mp3`.
   - Hình: `assets/images/story-001-01.webp`, ...
   - Đổi tên file sau khi đã phát hành sẽ làm vỡ liên kết, nên tránh.

6. **Nội dung dạng text, không dạng nhị phân khó đọc:**
   Bài và truyện lưu dạng JSON/Markdown có cấu trúc, để git diff đọc được, để kiểm tra tự động được, để người khác sửa được. Audio và hình là tài sản đi kèm, không phải nơi chứa nội dung chính.

7. **Kiểm tra chất lượng tự động trước mỗi đợt mở rộng:**
   Script phải kiểm tra: đủ trường, không trùng id, từ vựng trong truyện chỉ dùng âm/từ đã học, có file audio, có hình, có alt text. Bài nào rớt kiểm tra thì không nhập đợt.
