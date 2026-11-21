# Team

## Thông tin nhóm

- Tên nhóm: PhucLocTho
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-PhucLocTho-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/trannguyentran1997/K5-L3A-DAY13-PhucLocTho-LaunchEconomics · Nhánh nộp: `main` · Commit chốt: (ghi mã commit cuối cùng trước deadline)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Trần Tú Trân | 2A202603603 | otis7797@gmail.com | trannguyentran1997 | Trưởng nhóm; người gắn nhãn 2 kiêm giữ hồ sơ |
|   2 | Phạm Duy Đức | 2A202603611 | phamduclc3@gmail.com | DuyJob | Người viết code (A, B) |
|   3 | Phạm Thị Hồng Ngọc | 2A202603602 | ngockarryruby@gmail.com | (cần điền) | Người viết code (D) |
|   4 | Trần Tuấn Đăng | 2A202603618 | tuandang.04082004@gmail.com | (cần điền) | Người gắn nhãn 1 (C, E1, E2) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Nhóm không đổi vai sau giải lao mà chia việc theo phần riêng, mỗi người làm trên nhánh riêng, trưởng nhóm gộp và review (xem [PHAN_CONG_NHOM.md](PHAN_CONG_NHOM.md)). Hai người tự viết code: Đức tính chi phí (A, B), Ngọc tính cỡ mẫu (D).

## Cá nhân

Báo cáo riêng của từng thành viên nằm trong `report/team/`:

- `report/team/2A202603603_NguyenTranTuTran.md`
- `report/team/2A202603611_PhamDuyDuc.md`
- `report/team/2A202603602_PhamThiHongNgoc.md`
- `report/team/2A202603618_TranTuanDang.md`

## NguyenTranTuTran-2A202603603

### Phần việc phụ trách

- Trưởng nhóm: tạo repo nhóm, chia việc, gộp nhánh và review.
- Giữ hồ sơ: `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.
- Người gắn nhãn 2 ở nhiệm vụ C.

### Đóng góp cụ thể

- Viết `PHAN_CONG_NHOM.md`: chia 4 phần riêng (A + B, D, C + E, tổng hợp) để không ai phải chờ ai, kèm cách gắn nhãn và checklist nộp bài.
- Gộp 3 nhánh vào `main`, giải xung đột `src/lab13.py`, chạy lại toàn bộ và đối chiếu số với đáp án.
- Review từng phần, sửa: số 12.415 đ trong `pilot_plan.yaml`; tách luật dừng hoàn trùng; viết lại bảng khắc phục cho khác bài mẫu; gỡ cột nhãn người 2 chưa có thật.
- Kiểm số A2 độc lập bằng Excel (`report/team/kiem_so_A2.xlsx`), khớp `lab13.py`, lệch lớn nhất 0,11%.
- Viết hồ sơ launch v0 (7 mục, đề xuất Go có điều kiện), `TEAM.md`, `group_report.md`.
- Bộ nhãn độc lập 20 ca: chưa xong.

### Bằng chứng

- Commit `73380bc`, `986527f` (file phân công); `3e9a486` (gộp nhánh); `a8e1bde`, `b303cd3` (review và sửa); commit thêm hồ sơ, `TEAM.md`, `group_report.md`.

## PhamDuyDuc-2A202603611

### Phần việc phụ trách

- Nhiệm vụ A (A1–A4) và B (B1–B4): `src/lab13.py` phần A, B và `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- 3 hàm A1 qua cả 3 phép thử (1,20 · 1,25 · 1,25); `mo_hinh` cho chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu.
- A3 theo 4 loại và tỉ lệ ok theo lần thử; A4 cộng chi phí cố định (4.599 đ = 0,38× [simulated]).
- B1 đủ 9 kịch bản, B2 xếp hạng 3 yếu tố, B3 giới hạn 2 lần rẻ nhất cho cả hệ thống, B4 xem lại 100% (0,98× và 1,03× [simulated]).

### Bằng chứng

- Nhánh `PhamDuyDuc-2A202603611`, commit `80048f4`, `e383534`, `a631b86`.

## PhamThiHongNgoc-2A202603602

### Phần việc phụ trách

- Nhiệm vụ D: code D1 (ghép vào `src/lab13.py`) và `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Code 5 câu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299), đối chiếu với `statsmodels`, power 0,64 ở mức +5 điểm, tỉ lệ mở lại hiện tại 4,25% và 3,97%.
- `pilot_plan.yaml` đủ trường, D1 và D2 trong chú thích, chia theo nhân viên 20 + 20, luật dừng đủ 4 vế, không còn dấu `?`.
- Ghép phần D vào `src/lab13.py` và xoá file nháp.

### Bằng chứng

- Nhánh `PhamThiHongNgoc-2A202603602`, commit `73aa3d3`, `40ec4ab`, `33bfa71`.

## TranTuanDang-2A202603618

### Phần việc phụ trách

- Nhiệm vụ C (`report/team/bang_loi.md`), E1 và E2 (`report/team/chi_so.md`), phiếu chấm Gate 2a (`report/team/phieu_cham.md`).

### Đóng góp cụ thể

- Bộ nhãn độc lập 20 ca của người gắn nhãn 1.
- Tính 3 chỉ số E1 (82,83% · 27,12% · 4,25%), đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, danh sách event có `trace_id` và kiểm tra chéo.
- E2: 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy [simulated].

### Bằng chứng

- Nhánh `ttdang`, commit `25ed0ac`, `5389a32`.
