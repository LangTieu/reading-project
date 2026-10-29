# Content schema (bản nháp, sẽ chốt ở Giai đoạn 0)

Mỗi bài học / truyện là một file JSON với các trường bắt buộc:
- `id`: ví dụ `lesson-001`, không đổi sau khi phát hành.
- `level`: cấp độ, ví dụ `1`.
- `title`: tiêu đề.
- `focus_sounds`: danh sách âm trọng tâm, ví dụ `["s", "a", "t"]`.
- `words`: danh sách từ mới, chỉ dùng âm đã học.
- `text`: nội dung bài/truyện, câu ngắn.
- `questions`: (chỉ truyện hiểu bài) câu hỏi + đáp án.
- `audio`: đường dẫn file MP3 tương ứng.
- `images`: danh sách `{file, alt}`.
- `status`: `draft` | `qa_passed` | `published`. Chỉ `qa_passed` mới được tính vào đợt phát hành.
