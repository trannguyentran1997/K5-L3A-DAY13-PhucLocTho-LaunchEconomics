# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Đăng** · Người gắn nhãn 2: **Trân** (gắn trong 8 phút, không trao đổi). **Chưa xong:** Trân chưa gắn nhãn; cột người 2, cột "Trùng?", "Nhãn thống nhất" và tỉ lệ đồng thuận điền sau khi có phiếu thật của Trân.

| Ca | Nhãn người 1 (Đăng) | Nhãn người 2 (Trân) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | (chờ Trân) |  |  |
| 2 | Hệ thống | (chờ Trân) |  |  |
| 3 | Ngữ cảnh | (chờ Trân) |  |  |
| 4 | Giới hạn hệ thống | (chờ Trân) |  |  |
| 5 | Ngầm | (chờ Trân) |  |  |
| 6 | Do người dùng | (chờ Trân) |  |  |
| 7 | Hệ thống | (chờ Trân) |  |  |
| 8 | Hệ thống | (chờ Trân) |  |  |
| 9 | Do người dùng | (chờ Trân) |  |  |
| 10 | Ngữ cảnh | (chờ Trân) |  |  |
| 11 | Giới hạn hệ thống | (chờ Trân) |  |  |
| 12 | Ngầm | (chờ Trân) |  |  |
| 13 | Giới hạn hệ thống | (chờ Trân) |  |  |
| 14 | Do người dùng | (chờ Trân) |  |  |
| 15 | Hệ thống | (chờ Trân) |  |  |
| 16 | Ngữ cảnh | (chờ Trân) |  |  |
| 17 | Ngầm | (chờ Trân) |  |  |
| 18 | Ngữ cảnh | (chờ Trân) |  |  |
| 19 | Giới hạn hệ thống | (chờ Trân) |  |  |
| 20 | Hệ thống | (chờ Trân) |  |  |

**Tỉ lệ đồng thuận:** chờ bộ nhãn của Trân

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chờ so nhãn: mỗi ca lệch giữa Đăng và Trân ghi một câu quy tắc phân biệt tại đây.
- **Quy tắc phân biệt bổ sung cho các ca dễ lẫn:**
  - *Ca 8, 15 là Hệ thống, không phải Ngầm:* Sai sót đã lộ diện rõ ràng (dẫn sai điều khoản văn bản hoặc bị nhân viên review phát hiện trước khi gửi).
  - *Ca 13 là Giới hạn hệ thống:* Yêu cầu nằm ngoài phạm vi dịch vụ của LogiX-VN thì bản chất là giới hạn nghiệp vụ, bất kể trợ lý trả lời chung chung hay từ chối thẳng.
  - *Ca 12 là Ngầm:* Kết quả nghiệp vụ vẫn trả về đúng nhưng phát sinh bất thường âm thầm về chi phí token gấp 3 lần suốt 3 tuần mà không có cảnh báo hệ thống nào kích hoạt.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo kích hoạt khi tỷ lệ vượt quá 2% số yêu cầu/ngày | Tự động nhận diện mã sàn TMĐT và tra cứu sang mã vận đơn tương ứng; nếu không tra cứu được thì hiển thị hướng dẫn kèm hình ảnh minh hoạ vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: tin nhắn "đã hoàn" nhưng không có bản ghi sổ cái trạng thái ok cùng `trace_id`; ngưỡng cảnh báo: 0 ca | Chỉ gửi thông báo "đã hoàn" khi sổ cái xác nhận ok; nếu gặp lỗi 503 sau 3 lần retry thì thông báo "đang xử lý" và chuyển ticket sang luồng nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Báo cáo tuần: tỷ lệ mở lại yêu cầu vì thắc mắc số tiền hoàn mà qua hậu kiểm xác nhận đã tính đúng chính sách | Cập nhật template tin nhắn phản hồi luôn ghi rõ công thức tính chi tiết (Ví dụ: "Phí giao 30.000 đ × 50% = 15.000 đ") | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `reason = thieu_du_lieu`, tổng hợp theo từng phân loại yêu cầu | Duy trì luồng bàn giao kèm tóm tắt ngữ cảnh cho nhân viên; chính thức loại phân loại yêu cầu `quoc_te` ra khỏi phạm vi triển khai pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm toán mẫu ngẫu nhiên 100 đơn hoàn/tuần đối chiếu với bảng giá hiện hành; ngưỡng cảnh báo: tỷ lệ đơn lệch tiền > 1% | Thiết lập cơ chế tự động xoá cache bảng giá ngay khi phát hành bản giá mới, đồng thời ghi log phiên bản bảng giá vào trace của từng lượt xử lý | Kế toán trưởng |
