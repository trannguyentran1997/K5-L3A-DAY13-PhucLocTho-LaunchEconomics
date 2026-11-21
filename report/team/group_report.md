# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: PhucLocTho
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN, trả lời 4 câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Nhóm chia việc theo phần riêng để không ai phải chờ ai: Đức làm A + B, Ngọc làm D, Đăng làm C + E1/E2, Trân gắn nhãn thứ hai và tổng hợp hồ sơ ([PHAN_CONG_NHOM.md](../../PHAN_CONG_NHOM.md)). Mỗi người làm trên nhánh riêng; trưởng nhóm gộp vào `main`, chạy lại toàn bộ `src/lab13.py` và review từng phần trước khi viết hồ sơ.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): hàm `mo_hinh` cộng token và tool của mọi lần chạy, kể cả lần lỗi, cộng phút xem lại và làm lại [simulated], chia cho số việc thành công. Tách theo 4 loại yêu cầu, cộng chi phí cố định cho phạm vi pilot.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần chạy theo chi phí cả hệ thống, và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): gắn nhãn 20 ca theo 5 loại Google PAIR; bảng khắc phục 5 ca (14, 20, 16, 19, 5), mỗi dòng có event, ngưỡng và một vai trò.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho 3 cách chia trước khi chọn; chọn chia theo nhân viên 20 + 20, chấp nhận MDE +6 điểm; 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử, 2 chỉ số tự đề xuất, 12 event có `trace_id`, 4 dòng rủi ro kinh tế; hồ sơ 7 mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ**, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu [simulated]; giờ nhân viên chiếm 92,5%.
- So với nhân viên tự làm: cả hệ thống **0,49×** của 12.000 đ; phạm vi `noi_dia` + `hang_nang` đã cộng cố định **0,38×** [simulated]. `quoc_te` 1,88× nên loại.
- Yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated].
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Pilot: 20 + 20 nhân viên, n = 859/nhóm, m ≥ 299; power chỉ 0,64 nếu tác động thật là +5 điểm.
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, với 4 điều kiện có người phụ trách và ngày kiểm tra (xem hồ sơ).
- Kết quả duyệt chéo Gate 2a nhóm nhận được: ghi sau buổi duyệt chéo.

## 5. Khó khăn và cách xử lý

- **Lỗi mã hoá tiếng Việt:** commit đầu của Đức (`80048f4`) bị đổi toàn bộ chữ có dấu thành ký tự rác khi thao tác nhánh trên PowerShell. Đức sửa ở `e383534`.
- **A4 chia nhầm mẫu số:** bản đầu chia số việc thành công cho 982 yêu cầu trong phạm vi thay vì 1.200 yêu cầu của mẫu; Đức phát hiện khi đối chiếu đáp án và sửa.
- **Xung đột khi gộp `src/lab13.py`:** nhánh của Ngọc đã gộp bản lỗi mã hoá của Đức, còn bản sửa của Đức đến sau. Git tự gộp phần lớn; xung đột duy nhất ở cuối khối main, giữ lời gọi phần D của Ngọc.
- **Review phát hiện 2 vấn đề ở nhiệm vụ C:** bảng khắc phục bản đầu trùng gần nguyên văn bài làm mẫu, nên đã viết lại bằng 5 ca khác. Cột nhãn người 2 được điền khi Trân chưa gắn nhãn, nên đã gỡ; bộ nhãn thứ hai và tỉ lệ đồng thuận đang chờ Trân tự gắn.
- **Môi trường:** máy trưởng nhóm thiếu `statsmodels`, phải tạo `src/.venv` theo `src/README.md` (lệnh `python -m venv .venv` rồi `pip install -r requirements.txt`) mới chạy được phần D. Mạng tới github.com chập chờn, một số lần push phải chạy lại.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`. Bảng dưới đối chiếu từng việc trong [PHAN_CONG_NHOM.md](../../PHAN_CONG_NHOM.md) với kết quả thật trên repo (giờ lấy từ `git log`, ngày 21/11).

**Trạng thái:** ✅ xong · 🔧 xong, đã sửa khi review · ⏳ chưa làm hoặc chờ.

| Người | Việc được giao | Trạng thái | Bằng chứng / ghi chú |
| --- | --- | --- | --- |
| Đức | A1: 3 hàm, qua 3 phép thử | ✅ | `lab13.py` in "ĐẠT" (1,20 · 1,25 · 1,25) |
| Đức | A2–A4: `mo_hinh`, tách theo loại, chi phí cố định | 🔧 | 4.472 đ, 16,3 lần, A4 4.599 đ = 0,38× [simulated]; A4 bản đầu chia nhầm 982, Đức tự sửa ở `e383534` |
| Đức | B1–B4 và `bang_chi_phi.md` đủ, không còn `...` | ✅ | B1 đủ 9 dòng, xếp hạng, B3, B4 khớp đáp án |
| Đức | Push mốc 1 (~14:50) và mốc 2 (~15:20); sau mốc 2 không sửa `lab13.py` | ⏳ trễ | Push một lần lúc 15:38 (`80048f4`); sửa tiếp `lab13.py` lúc 15:49 sau khi Ngọc đã ghép phần D (15:44), gây xung đột khi gộp |
| Đức | Báo cáo cá nhân | ✅ | `2A202603611_PhamDuyDuc.md` (`a631b86`) |
| Ngọc → Trân | Kiểm số A2 bằng Excel | ✅ | Ngọc chưa làm (việc thêm sau); Trân làm khi review: `kiem_so_A2.xlsx`, công thức Excel trên CSV, khớp `lab13.py`, lệch lớn nhất 0,11% |
| Ngọc | Code D1 (5 câu, power, tỉ lệ mở lại) | ✅ | 1.251 · 3.103 · 1.000 · 300 · m ≥ 299; power 0,64; 4,25% và 3,97% |
| Ngọc | `pilot_plan.yaml` đủ trường, luật dừng 4 vế, qua 2 lệnh tự kiểm | 🔧 | Review đổi 12.414 thành 12.415 cho khớp code, tách luật hoàn trùng thành luật thứ 4 |
| Ngọc | Ghép phần D vào `lab13.py`, xoá file nháp | ✅ | `33bfa71`; `src/nhap_pilot.py` không còn |
| Ngọc | Làm trên nhánh riêng | ⏳ | `73aa3d3`, `40ec4ab` push thẳng lên `main` (15:30, 15:39) |
| Ngọc | Báo cáo cá nhân | ✅ | `2A202603602_PhamThiHongNgoc.md` |
| Đăng | Bộ nhãn độc lập 20 ca (người gắn nhãn 1) | ✅ | Cột "Nhãn người 1" trong `bang_loi.md` |
| Đăng | Nhập 2 bộ nhãn, tỉ lệ đồng thuận, quy tắc ca lệch | ⏳ | Chờ bộ nhãn của Trân; cột người 2 bản đầu được điền khi Trân chưa gắn, đã gỡ khi review |
| Đăng | Bảng khắc phục 5 ca đủ 5 loại | 🔧 | Bản đầu trùng gần nguyên văn bài mẫu; viết lại bằng ca 14, 20, 16, 19, 5 |
| Đăng | `chi_so.md`: 3 chỉ số, 2 chỉ số tự đề xuất, ≥ 6 event, E2 ≥ 2 dòng | 🔧 | 82,83% · 27,12% · 4,25%; 12 event; 4 dòng rủi ro; review thêm event cho 5 ca mới |
| Đăng | `phieu_cham.md` | ⏳ | Điền tại buổi Gate 2a |
| Đăng | Báo cáo cá nhân | 🔧 | `2A202603618_TranTuanDang.md`; review sửa các câu "đồng thuận 18/20" |
| Trân | Mời collaborator | ✅ | 3 thành viên đã push được nhánh lên repo nhóm |
| Trân | Gắn nhãn 20 ca (người gắn nhãn 2) | ⏳ | Chưa gắn |
| Trân | Gộp nhánh, chạy lại `lab13.py` trên máy khác | ✅ | `3e9a486`, `59d4bdf`; chạy hết, số khớp đáp án |
| Trân | `ho_so_launch_v0.md` 7 mục + đề xuất | ✅ | Go có điều kiện, 4 điều kiện có ngày; mục 5 còn trạng thái "Chưa" |
| Trân | `TEAM.md`, `group_report.md`, báo cáo cá nhân | ✅ | `96dd876`; còn trống GitHub của Ngọc, Đăng và commit chốt |
| Trân | Soát cuối (từ cấm, `...`, `simulated`, YAML) | ✅ | Không có từ cấm; YAML đọc được, không còn `?` |
| Cả nhóm | 10 phút đọc phần nhau, Gate 2a, nộp link LMS | ⏳ | Sau 17:00 |

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; mọi kết luận chi phí phải tính lại bằng phút đo thật sau tuần 1 pilot.
- Đợt chạy thử không có đối chứng, nên 82,83% chưa nói được trợ lý làm chỉ số chính thay đổi bao nhiêu.
- Với 40 nhân viên, pilot chỉ đủ mẫu cho +6 điểm; nếu tác động thật là +5 điểm thì 36% khả năng bỏ sót.
- Chi phí cố định tính theo tỉ lệ thành công của mẫu 1.200 yêu cầu; khối lượng thật thấp hơn thì chi phí mỗi việc tăng.
- Nhiệm vụ C còn thiếu bộ nhãn thứ hai; lần sau hai người gắn nhãn phải gắn ngay đầu buổi và lưu phiếu gốc làm bằng chứng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
- Tài liệu của lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
