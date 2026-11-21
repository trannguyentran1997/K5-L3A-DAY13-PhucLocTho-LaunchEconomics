# Báo cáo cá nhân — NguyenTranTuTran-2A202603603

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trần Tú Trân
- MSSV: 2A202603603
- Email: otis7797@gmail.com
- GitHub: trannguyentran1997
- Vai trong nhóm: Trưởng nhóm; người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Tạo repo nhóm, chia việc, gộp nhánh của các thành viên vào `main` và review từng phần.
- Giữ hồ sơ: `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.
- Người gắn nhãn 2 ở nhiệm vụ C: gắn nhãn độc lập 20 ca để so với bộ nhãn của Đăng.

## 3. Đóng góp cụ thể

- **Chia việc:** viết `PHAN_CONG_NHOM.md`, chia 4 phần riêng (A + B cho Đức, D cho Ngọc, C + E1/E2 cho Đăng, tổng hợp cho tôi), mỗi người giữ file riêng để không ai phải chờ ai; kèm mục cách gắn nhãn 20 ca và checklist nộp bài.
- **Gộp nhánh:** gộp 3 nhánh vào `main`; giải xung đột duy nhất ở cuối khối main của `src/lab13.py` (giữ lời gọi phần D); chạy lại toàn bộ, số khớp đáp án: 4.472 đ, 16,3 lần, B1 đủ 9 dòng, D1 1.251 · 3.103 · 1.000 · 300 · 299.
- **Review và sửa:**
  - `pilot_plan.yaml`: đổi 12.414 đ thành 12.415 đ cho khớp số code của nhóm; tách "hoàn tiền trùng" thành luật dừng riêng (1 ca trong 24 giờ là dừng, thay vì chờ 3 ngày liên tiếp); ghi ngày bắt đầu 2026-12-01 cho khớp ngày quyết định.
  - `bang_loi.md`: bảng khắc phục bản đầu trùng gần nguyên văn bài làm mẫu, đã viết lại bằng 5 ca khác (14, 20, 16, 19, 5); gỡ cột nhãn người 2 vì cột này được điền khi tôi chưa gắn nhãn.
  - `chi_so.md`: thêm event và thuộc tính mà 5 ca mới cần, sửa dòng kiểm tra chéo.
- **Kiểm số A2 bằng Excel:** `report/team/kiem_so_A2.xlsx` tính lại token, tool, xem lại, làm lại, số việc thành công và chi phí mỗi việc thành công bằng công thức Excel trên hai file CSV, không dùng `lab13.py`; khớp số của Đức, lệch lớn nhất 0,11% do làm tròn.
- **Hồ sơ:** viết `ho_so_launch_v0.md` (7 mục, mỗi mục có con số chính, trạng thái, vai trò phụ trách; đề xuất Go có điều kiện với 4 điều kiện có ngày kiểm tra), `TEAM.md`, `group_report.md`.
- **Chưa xong:** bộ nhãn độc lập 20 ca của tôi cho nhiệm vụ C.

## 4. Bằng chứng

- Commit `73380bc`, `986527f`: file phân công.
- Commit `3e9a486`: gộp nhánh của Đức, giải xung đột `src/lab13.py`.
- Commit `a8e1bde`, `b303cd3`: các sửa đổi khi review.
- Commit thêm `ho_so_launch_v0.md`, `TEAM.md`, `group_report.md` và báo cáo này.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude Opus) trong VS Code.
- **Dùng vào việc gì:** đọc đề và viết file phân công; gộp nhánh và giải xung đột; review các file hồ sơ, phát hiện bảng khắc phục trùng bài mẫu và cột nhãn chưa có thật; dựng workbook kiểm số A2 bằng Excel, soạn lại bảng khắc phục, luật dừng hoàn trùng, hồ sơ launch v0, `TEAM.md`, `group_report.md` và bản nháp báo cáo này.
- **Không dùng AI để gắn nhãn 20 ca:** khi được nhờ, Claude Code từ chối gắn nhãn thay vì quy định của lab; tôi tự gắn bằng phiếu trong `PHAN_CONG_NHOM.md` (chưa xong lúc viết báo cáo này).
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py` trong `src/` trên máy mình (máy khác với máy viết code), đối chiếu từng số với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
  - `pilot_plan.yaml` qua `yaml.safe_load`, không còn dấu `?` ngoài chú thích, cả 4 luật dừng đủ 4 vế.
  - Mọi số trong hồ sơ dẫn về một file nguồn (`bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`); `grep` không có từ bị cấm theo quy tắc 5.

## 6. Tự đánh giá

- Làm tốt: chia việc để 3 phần chạy song song; review bắt được 2 vấn đề liêm chính ở nhiệm vụ C trước khi nộp; hồ sơ nêu thẳng hai con số bất lợi (xem lại 100% là 0,98–1,03×, power 0,64).
- Cần cải thiện: gắn nhãn ngay đầu buổi như kế hoạch thay vì để tới cuối; tự đọc kỹ và giải thích được mọi phần AI soạn trước Gate 2a.
