# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51 / 1.200); trong phạm vi `noi_dia` + `hang_nang`: 3,97% |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được nhân viên mở bằng trợ lý | Số `agent_suggestion_shown` (arm = tro_ly, đếm theo request_id) chia số `refund_request_created` có arm = tro_ly, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền phát hiện qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | Số `audit_sample_checked` có `so_tien_da_hoan` ≠ `so_tien_dung` chia số đơn được kiểm tra (100 đơn/tuần) | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng nên con số này không cho biết trợ lý làm chỉ số thay đổi bao nhiêu so với mức 0,70.

**Cách tính** (chạy trong `src/`, dữ liệu giả lập):

```python
import pandas as pd
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)).mean()   # 0,8283 (994/1.200)
xem = reqs[reqs.duoc_xem_lai == 1]
bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()                       # 0,2712 (48/177)
an_toan = (reqs.mo_lai_trong_7_ngay == 1).mean()                                 # 0,0425 (51/1.200)
pham_vi = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
an_toan_pham_vi = pham_vi.mo_lai_trong_7_ngay.mean()                             # 0,0397 (39/982)
```

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, depot, arm, trace_id | Khi khách gửi yêu cầu |
| input_validation_failed | Agent | truong_loi (ma_van_don/loai_ly_do), gia_tri_nhap, trace_id | Khi đầu vào của khách không khớp định dạng hoặc không tra được |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| staff_review_decision | Nhân viên | staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi/sửa/bỏ |
| staff_rework_completed | Nhân viên | staff_id, phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| handoff_to_staff | Agent | reason (thieu_du_lieu/ngoai_pham_vi/het_lan_chay), tom_tat, trace_id | Khi chuyển nhân viên |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + không có `ticket_reopened` trong 7 ngày, nối bằng trace_id.
- Dùng (bỏ qua gợi ý): `staff_review_decision` có quyet_dinh là sua/bo, chia tổng số `staff_review_decision`.
- An toàn (lỗi lọt đến khách): `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia số `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown` chia `refund_request_created` có arm = tro_ly.
- An toàn (tự đề xuất): `audit_sample_checked` có so_tien_da_hoan ≠ so_tien_dung, chia số đơn được kiểm tra.
- Bảng khắc phục trong `bang_loi.md` dùng `input_validation_failed` (ca 9), `refund_ledger_write` (ca 7), `ticket_reopened` (ca 18), `handoff_to_staff` (ca 4), `audit_sample_checked` (ca 17); cả năm event đều có trong danh sách trên.
- Cả năm chỉ số đều tính được từ danh sách event trên. Chi phí mỗi việc thành công cũng tính được từ `agent_run_completed` cộng phút trong `staff_review_decision` và `staff_rework_completed`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Mọi tác động dưới đây tính từ cột `_simulated` nên đều là **simulated**.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng từ 4.472 đ lên 6.787 đ (+51,8%) [simulated]; đây là yếu tố nhạy nhất | Tỉ lệ `staff_rework_completed` / yêu cầu theo tuần > 7% (đợt chạy thử: 4,9%, tức 48/982 trong phạm vi) | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất trong 3 ngày | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ (làm lại 9 phút); 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (hoặc ≤ 4,8 phút) | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0.25; phút xem lại trung vị > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% trong 2 tuần | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: +1.185 đ/việc ở 33.750 việc thành công/tháng; +2.370 đ/việc nếu còn một nửa (4.599 đ thành 5.784 đ, tức 0,38× thành 0,48×) [simulated] | Số `ticket_closed` thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, đàm phán lại hợp đồng chi phí cố định | Giám đốc vận hành |
| Lương nhân viên tăng | +25% lương làm chi phí tăng lên 5.506 đ (+23,1%) [simulated], yếu tố nhạy thứ ba | Đơn giá phút nhân viên trong bảng lương quý | Cập nhật mô hình và kiểm tra lại mức 0,49× so với nhân viên tự làm | Kế toán trưởng |

Cách đối chiếu số E2: các số trên khớp bảng B1, B4 và A4 trong `bang_chi_phi.md`. Nếu số Đức chốt lệch thì sửa theo `bang_chi_phi.md`.
