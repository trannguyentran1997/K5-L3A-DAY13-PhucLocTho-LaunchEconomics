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

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | `ticket_closed` có `closed_by = khach_xac_nhan` mà trong 24 giờ không có `refund_ledger_write` thành công cùng `trace_id`, hoặc có `ticket_reopened` với `reason = chua_nhan_tien`; đếm hằng ngày, cảnh báo khi > 0,5% số yêu cầu do khách tự đóng | Chỉ hiện nút "Xác nhận đã nhận tiền" sau khi sổ cái ghi hoàn thành công; thêm bước xác nhận lần hai có ghi số tiền; cho khách mở lại trong 7 ngày bằng một chạm | PM ứng dụng khách hàng |
| 20 | Hệ thống | Đối soát mỗi giờ trên `refund_ledger_write`: đếm mã đơn có từ 2 bản ghi thành công; ngưỡng 0 ca, có 1 ca là kích luật dừng hoàn trùng trong `pilot_plan.yaml` | Sinh `idempotency_key` từ mã đơn + loại hoàn; yêu cầu gửi lại khi lệnh trước đang xử lý chỉ trả trạng thái "đang xử lý", không tạo lệnh hoàn mới | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | `customer_notification_sent` có `sent_at` trong khung 22:00–7:00, đếm theo tuần; kèm số `ticket_reopened` có `reason = lam_phien`; ngưỡng sau khi sửa: 0 tin gửi trong khung đêm | Thêm khung giờ yên lặng 22:00–7:00: tiền vẫn hoàn ngay, chỉ hoãn tin nhắn tới 7:00; khách tự chọn "nhận ngay" trong cài đặt nếu muốn | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | `handoff_to_staff` có `reason = qua_han_du_lieu`, đếm theo tuần và theo loại yêu cầu; cảnh báo khi > 2% số yêu cầu để cân nhắc mở quyền tra kho dữ liệu cũ | Kiểm tra ngày đơn ngay bước đầu: đơn quá 12 tháng thì báo rõ giới hạn và chuyển nhân viên kèm tóm tắt luôn, không chạy agent (không tốn token cho việc chắc chắn không làm được) | PM trợ lý hoàn phí |
| 5 | Ngầm | `audit_sample_checked` hằng tuần: 100 đơn ngẫu nhiên, trong đó lấy riêng ít nhất 30 đơn có mã giảm giá; ngưỡng > 1% đơn lệch tiền | Tool tính hoàn lấy giá sau giảm từ hoá đơn thay vì giá niêm yết; thêm ca kiểm thử "đơn có mã giảm giá" chạy trước mỗi lần cập nhật tool | Kế toán trưởng |
