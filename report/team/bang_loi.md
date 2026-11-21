# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Đăng** · Người gắn nhãn 2: **Trân** (gắn theo nguyên nhân gốc bằng quy tắc 5 bước: Ngầm → Do người dùng → Giới hạn hệ thống → Hệ thống → Ngữ cảnh).

| Ca | Nhãn người 1 (Đăng) | Nhãn người 2 (Trân) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt yêu cầu ≥ 80% / ≥ 16/20; phân bố: 4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn hệ thống · 3 Ngầm)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng giữa hai bộ nhãn (trùng 20/20 trên nhãn chính thức, đạt ≥ 80%). Một số ca có ghi chú phân vân trên phiếu người gắn nhãn 2 (ca 6: `ND (HT)`, ca 8: `HT (NG)`, ca 9: `ND (NC)`, ca 12: `NG (HT)`, ca 13: `GH (HT)`, ca 17: `NG (HT)`, ca 18: `NC (HT)`, ca 20: `HT (ND)`) đều thống nhất ở nhãn chính thức theo nguyên nhân gốc và thứ tự kiểm tra 5 bước.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | `ticket_closed` có `closed_by = khach_xac_nhan` mà trong 24 giờ không có `refund_ledger_write` thành công cùng `trace_id`, hoặc có `ticket_reopened` với `reason = chua_nhan_tien`; đếm hằng ngày, cảnh báo khi > 0,5% số yêu cầu do khách tự đóng | Chỉ hiện nút "Xác nhận đã nhận tiền" sau khi sổ cái ghi hoàn thành công; thêm bước xác nhận lần hai có ghi số tiền; cho khách mở lại trong 7 ngày bằng một chạm | PM ứng dụng khách hàng |
| 20 | Hệ thống | Đối soát mỗi giờ trên `refund_ledger_write`: đếm mã đơn có từ 2 bản ghi thành công; ngưỡng 0 ca, có 1 ca là kích luật dừng hoàn trùng trong `pilot_plan.yaml` | Sinh `idempotency_key` từ mã đơn + loại hoàn; yêu cầu gửi lại khi lệnh trước đang xử lý chỉ trả trạng thái "đang xử lý", không tạo lệnh hoàn mới | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | `customer_notification_sent` có `sent_at` trong khung 22:00–7:00, đếm theo tuần; kèm số `ticket_reopened` có `reason = lam_phien`; ngưỡng sau khi sửa: 0 tin gửi trong khung đêm | Thêm khung giờ yên lặng 22:00–7:00: tiền vẫn hoàn ngay, chỉ hoãn tin nhắn tới 7:00; khách tự chọn "nhận ngay" trong cài đặt nếu muốn | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | `handoff_to_staff` có `reason = qua_han_du_lieu`, đếm theo tuần và theo loại yêu cầu; cảnh báo khi > 2% số yêu cầu để cân nhắc mở quyền tra kho dữ liệu cũ | Kiểm tra ngày đơn ngay bước đầu: đơn quá 12 tháng thì báo rõ giới hạn và chuyển nhân viên kèm tóm tắt luôn, không chạy agent (không tốn token cho việc chắc chắn không làm được) | PM trợ lý hoàn phí |
| 5 | Ngầm | `audit_sample_checked` hằng tuần: 100 đơn ngẫu nhiên, trong đó lấy riêng ít nhất 30 đơn có mã giảm giá; ngưỡng > 1% đơn lệch tiền | Tool tính hoàn lấy giá sau giảm từ hoá đơn thay vì giá niêm yết; thêm ca kiểm thử "đơn có mã giảm giá" chạy trước mỗi lần cập nhật tool | Kế toán trưởng |
