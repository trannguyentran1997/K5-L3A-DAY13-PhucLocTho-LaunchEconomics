# Team

## Thông tin nhóm

- Tên nhóm: PhucLocTho
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-PhucLocTho-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/trannguyentran1997/K5-L3A-DAY13-PhucLocTho-LaunchEconomics · nhánh `main` · commit chốt: (ghi mã commit cuối cùng trước deadline)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Trần Tú Trân | 2A202603603 | otis7797@gmail.com | trannguyentran1997 | Trưởng nhóm; người gắn nhãn 2 kiêm giữ hồ sơ; kiểm số A2 |
|   2 | Phạm Duy Đức | 2A202603611 | phamduclc3@gmail.com | DuyJob | Người viết code (A, B) |
|   3 | Phạm Thị Hồng Ngọc | 2A202603602 | ngockarryruby@gmail.com | (cần điền) | Người viết code (D) |
|   4 | Trần Tuấn Đăng | 2A202603618 | tuandang.04082004@gmail.com | TunDangg | Người gắn nhãn 1 (C, E1, E2, phiếu chấm) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

Nhóm không đổi vai sau giải lao mà chia việc theo phần riêng, mỗi người làm trên nhánh riêng, trưởng nhóm gộp vào `main` và review (xem [PHAN_CONG_NHOM.md](PHAN_CONG_NHOM.md)). Vẫn có hai người tự tay tính chi phí: Đức bằng code, Trân kiểm lại bằng Excel.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Báo cáo của nhóm: `report/team/2A202603603_NguyenTranTuTran.md`, `report/team/2A202603611_PhamDuyDuc.md`, `report/team/2A202603602_PhamThiHongNgoc.md`, `report/team/2A202603618_TranTuanDang.md`.

## NguyenTranTuTran-2A202603603

### Phần việc phụ trách

- Trưởng nhóm: tạo repo nhóm, mời thành viên, chia việc, gộp nhánh, review và nộp bài.
- Người gắn nhãn 2 ở nhiệm vụ C.
- Giữ hồ sơ (E3): `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.
- Kiểm số A2 bằng Excel (nhận lại từ Ngọc).

### Đóng góp cụ thể

- Chia việc: viết `PHAN_CONG_NHOM.md` gồm 4 phần riêng để không ai phải chờ ai, ba điểm chạm bắt buộc, cách gắn nhãn 20 ca, checklist soát và nộp bài.
- Repo: tạo repo nhóm đúng tên, mời 3 thành viên làm collaborator.
- Gộp nhánh: gộp 3 nhánh vào `main`, giải xung đột ở cuối `src/lab13.py` (giữ lời gọi phần D); chạy lại toàn bộ `lab13.py` trên máy khác với máy viết code, số khớp đáp án.
- Review và sửa:
  - `pilot_plan.yaml`: đổi 12.414 đ thành 12.415 đ cho khớp code; tách hoàn tiền trùng thành luật dừng thứ 4 (1 ca trong 24 giờ là dừng); ghi ngày bắt đầu 2026-12-01.
  - `bang_loi.md`: viết lại bảng khắc phục bằng ca 14, 20, 16, 19, 5 vì bản đầu trùng gần nguyên văn bài mẫu; bỏ mục "quy tắc bổ sung"; gỡ cột nhãn người 2 được điền khi chưa có nhãn thật.
  - `chi_so.md`: thêm event `customer_notification_sent` và các thuộc tính `closed_by`, `co_ma_giam_gia`, `qua_han_du_lieu` cho 5 ca mới.
  - Báo cáo của Đăng: sửa các câu "đồng thuận 18/20" chưa đúng lúc đó, thêm ghi chú review.
- Kiểm số A2 bằng Excel: `report/team/kiem_so_A2.xlsx` tính lại token, tool, lần chạy 2–3, xem lại, làm lại, số việc thành công và chi phí mỗi việc thành công bằng công thức Excel trên hai file CSV, không dùng `lab13.py`; khớp 11/11 khoản, lệch lớn nhất 0,11% (do làm tròn 16,3).
- Gắn nhãn 20 ca (người gắn nhãn 2) theo nguyên nhân gốc, ghi cả mã phân vân; so với Đăng trùng 20/20 = 100%, không có ca lệch.
- Hồ sơ launch v0: 7 mục, mỗi mục có con số chính, trạng thái, một vai trò phụ trách; đề xuất Go có điều kiện cho pilot `noi_dia` + `hang_nang` với 4 điều kiện có người phụ trách và ngày kiểm tra; nêu 2 con số bất lợi (xem lại 100% là 0,98–1,03×; power 0,64 ở mức +5 điểm).
- `TEAM.md`, `group_report.md` (có bảng đối chiếu phân công), báo cáo cá nhân.
- Soát cuối: không có từ bị cấm, mọi số giả lập có nhãn `simulated`, `pilot_plan.yaml` đọc được và không còn dấu `?`.
- Soạn bản nháp `phieu_cham.md` chấm nhóm TENGICUNGDUOC (commit `1da04c2` của họ): điểm từng tiêu chí có lý do bằng số, quyết định Go có điều kiện, một câu hỏi về luật dừng chi phí.
- Chưa xong: gửi hồ sơ và trình bày 1 phút ở Gate 2a; điền commit chốt; push cuối.

### Bằng chứng

- Nhánh `NguyenTranTuTran-2A202603603`.
- `73380bc`, `986527f`: file phân công.
- `05cfcab`, `5b7a87b`, `3e9a486`, `59d4bdf`: gộp nhánh của Ngọc, Đăng, Đức.
- `a8e1bde`, `b303cd3`: review và sửa phần của Ngọc, Đăng.
- `96dd876`: hồ sơ launch v0, `TEAM.md`, `group_report.md`, báo cáo cá nhân.
- `1247fcb`: bảng đối chiếu phân công trong `group_report.md`.
- `d5fb4a5`: `report/team/kiem_so_A2.xlsx`.
- `fb47147`: bộ nhãn 20 ca của người gắn nhãn 2, tỉ lệ đồng thuận, hồ sơ mục 5.
- `64dd0ed`: bổ sung đóng góp từng người trong `TEAM.md`.

## PhamDuyDuc-2A202603611

### Phần việc phụ trách

- Nhiệm vụ A (A1–A4) và B (B1–B4): `src/lab13.py` phần A, B và `report/team/bang_chi_phi.md`.
- Cung cấp số A3 cho dòng `scope` của Ngọc và số độ nhạy B cho bảng rủi ro E2 của Đăng.

### Đóng góp cụ thể

- A1: 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, qua cả 3 phép thử (1,20 · 1,25 · 1,25).
- A2: `mo_hinh` tính tử số trên mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm 978 việc thành công: tổng 4.373.585 đ, 4.472 đ mỗi việc thành công, gấp 16,3 lần hoá đơn chia số yêu cầu; làm lại 51,8%, xem lại 40,7%; cả hệ thống 5.865 đ = 0,49× [simulated].
- A3: tách 4 loại (`noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88× [simulated]) và tỉ lệ ok theo từng lần thử, chỉ ra chạy lại không giúp `quoc_te` (30,0% → 11,4% → 2,2%).
- A4: cộng chi phí cố định 40 triệu/tháng: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× nếu còn một nửa [simulated]. Bản đầu chia nhầm 982 thay vì 1.200, Đức tự phát hiện và sửa.
- B1–B4: 9 kịch bản độ nhạy; cặp token × 2 + xem lại × 2 = 6.543 đ (+46,3%) và xếp hạng 3 yếu tố (làm lại · xem lại · lương); giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ); xem lại 100% là 11.743 đ = 0,98× và 12.415 đ = 1,03×, hoà vốn ≤ 5,1 và ≤ 4,8 phút [simulated].
- Điền đủ `bang_chi_phi.md`, mọi số từ cột `_simulated` có nhãn.
- Báo cáo cá nhân.
- Ghi chú quy trình: không tách 2 mốc push như phân công mà push một lần lúc 15:38; sửa tiếp `lab13.py` lúc 15:49 (lỗi mã hoá tiếng Việt, A4) sau khi Ngọc đã ghép phần D, gây một xung đột khi gộp, trưởng nhóm đã giải.

### Bằng chứng

- Nhánh `PhamDuyDuc-2A202603611`.
- `80048f4`: phần A và B; `e383534`: sửa mã hoá UTF-8, công thức A4, bổ sung A3/B4; `a631b86`: báo cáo cá nhân.
- Kiểm chéo độc lập: `report/team/kiem_so_A2.xlsx` khớp số A2 của Đức.

## PhamThiHongNgoc-2A202603602

### Phần việc phụ trách

- Nhiệm vụ D: code D1 (ghép vào `src/lab13.py`) và `report/team/pilot_plan.yaml`.
- Kiểm số A2 bằng Excel (đã chuyển cho Trân).

### Đóng góp cụ thể

- Code D1 viết trong file nháp riêng rồi ghép: chia theo yêu cầu 1.251/nhóm (đối chiếu `statsmodels` 1.250); theo nhân viên m = 75: DE 2,48, 3.103/nhóm, cần 84 > 40 người; 20 nhân viên/nhóm: trần 1.000 < 1.251; 6 depot/nhóm: trần 300; MDE +6 điểm: m ≥ 299, DE 6,96.
- Con số bất lợi: power chỉ 0,64 nếu tác động thật là +5 điểm với n = 859/nhóm; ước tính khoảng 9,7 ngày ở bước 0.50.
- Tỉ lệ mở lại hiện tại trước khi đặt ngưỡng an toàn: 4,25% toàn mẫu, 3,97% trong phạm vi pilot.
- `pilot_plan.yaml`: đủ mọi trường; D1, D2 và đánh đổi trong chú thích; chia theo nhân viên 20 + 20 phân tầng theo depot; `scope` lấy số A3; luật dừng đủ 4 vế; qua 2 lệnh tự kiểm. Khi review: đổi 12.414 thành 12.415, thêm luật dừng hoàn trùng thứ 4.
- Ghép phần D vào `src/lab13.py`, chạy hết không lỗi, xoá `src/nhap_pilot.py`.
- Báo cáo cá nhân.
- Kiểm số A2 bằng Excel: việc thêm vào phân công sau khi Ngọc đã làm xong phần D; Trân làm thay khi review.
- Ghi chú quy trình: 2 commit đầu (`73aa3d3`, `40ec4ab`) push thẳng lên `main` thay vì nhánh riêng; không ảnh hưởng nội dung.

### Bằng chứng

- Nhánh `PhamThiHongNgoc-2A202603602`.
- `73aa3d3`: kế hoạch pilot, code D1 nháp, báo cáo cá nhân; `40ec4ab`: cập nhật báo cáo; `33bfa71`: ghép phần D vào `lab13.py`, xoá file nháp.

## TranTuanDang-2A202603618

### Phần việc phụ trách

- Nhiệm vụ C (`report/team/bang_loi.md`), E1 và E2 (`report/team/chi_so.md`), phiếu chấm Gate 2a (`report/team/phieu_cham.md`).
- Người gắn nhãn 1.

### Đóng góp cụ thể

- Gắn nhãn 20 ca (người gắn nhãn 1) theo 5 loại Google PAIR; bộ nhãn này là cột "Nhãn người 1" trong `bang_loi.md`, trùng 20/20 với người gắn nhãn 2.
- `bang_loi.md`: dựng bảng hai bộ nhãn và bảng khắc phục 5 ca. Khi review, bảng khắc phục được viết lại (bản đầu trùng bài mẫu) và cột người 2 được gỡ rồi nhập lại bằng nhãn thật của Trân.
- E1: tính 3 chỉ số bằng pandas, ghi code vào file: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200; 3,97% trong phạm vi); đề xuất thêm 1 chỉ số dùng, 1 chỉ số an toàn.
- Danh sách 11 event có `trace_id` và kiểm tra chéo chỉ số nào tính từ event nào (review thêm 1 event cho bảng khắc phục mới, thành 12).
- E2: 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy (làm lại gấp đôi, xem lại 100%, khối lượng thấp, lương tăng) [simulated].
- Báo cáo cá nhân (review sửa các câu về đồng thuận).
- `phieu_cham.md` (chấm nhóm TENGICUNGDUOC): Trân soạn bản nháp từ bằng chứng trong repo của họ; Đăng và cả nhóm hội đồng chốt điểm, ghi câu trả lời của đội trình tại buổi.

### Bằng chứng

- Nhánh `ttdang`.
- `25ed0ac`: `bang_loi.md`, `chi_so.md`; `5389a32`: báo cáo cá nhân.
