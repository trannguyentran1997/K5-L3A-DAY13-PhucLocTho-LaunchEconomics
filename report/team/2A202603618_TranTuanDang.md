# Báo cáo cá nhân — TranTuanDang-2A202603618

## 1. Thông tin thành viên

- Họ tên: Trần Tuấn Đăng
- MSSV: 2A202603618
- Email: tuandang.04082004@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1

## 2. Phần việc phụ trách

Nhiệm vụ C (bảng lỗi và cách khắc phục), E1 (đặc tả chỉ số, danh sách event), E2 (rủi ro kinh tế) và phiếu chấm Gate 2a. File giữ: `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **C:** gắn nhãn độc lập 20 ca theo 5 loại Google PAIR trong 8 phút; so với bộ nhãn của Trân, đồng thuận 18/20 = 90%; viết quy tắc phân biệt cho 2 ca lệch (ca 6, ca 18) và các ca dễ lẫn (8, 15, 13, 12); lập bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có event, ngưỡng hoặc tần suất và một vai trò phụ trách.
- **E1:** tính thử 3 chỉ số trên 1.200 yêu cầu: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200; 3,97% trong phạm vi `noi_dia` + `hang_nang`); đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn; lập 11 event có `trace_id` và kiểm tra chéo chỉ số nào tính từ event nào.
- **E2:** 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy [simulated]: làm lại gấp đôi +51,8% (6.787 đ); xem lại 100% 0,98× (1,03× nếu làm lại 15,3 phút); chi phí cố định +1.185 đến +2.370 đ/việc; lương tăng 25% +23,1%.
- **Gate 2a:** chấm nhóm n + 1 vào `phieu_cham.md` (cập nhật sau buổi duyệt chéo 17:00).

## 4. Bằng chứng

- Commit `25ed0ac` trên branch `ttdang`: `report/team/bang_loi.md`, `report/team/chi_so.md`.
- `bang_loi.md`: hai bộ nhãn, tỉ lệ đồng thuận 18/20 = 90%, bảng khắc phục ca 9, 7, 18, 4, 17.
- `chi_so.md`: đoạn code pandas tính 3 chỉ số, bảng 11 event, bảng E2.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** đọc đề và lập kế hoạch phần việc; tính lại 3 chỉ số E1 và các số độ nhạy B1, B4, A4 dùng cho E2 bằng pandas trên hai file CSV; soạn bảng event và phần kiểm tra chéo; viết script nhỏ tính tỉ lệ đồng thuận từ hai bộ nhãn; soát chéo `bang_loi.md` với `chi_so.md`.
- **Không dùng AI** để gắn nhãn 20 ca hay chấm phiếu Gate 2a: hai việc này tôi tự làm theo quy định của lab.
- **Cách tự kiểm tra:** đối chiếu mọi số với số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%; riêng 12.415 đ so với 12.414 đ do làm tròn); chạy lại đoạn code trong `chi_so.md` ra đúng 994, 48/177, 51; số E2 sẽ đối chiếu lại với `bang_chi_phi.md` của Đức; `grep` không còn `...` và không có từ bị cấm.

## 6. Tự đánh giá

- Hoàn thành C, E1, E2 đúng hạn; đồng thuận 90%, vượt ngưỡng 80%; mọi số giả lập có nhãn simulated.
- Bài học: gắn nhãn theo nguyên nhân gốc chứ không theo chỗ cần sửa (ca 6, 18 lệch đều vì nhìn vào chỗ cần sửa); chỉ số nào không tính được từ event thì chưa đo được.
- Cần cải thiện: chủ động đồng bộ số với bảng độ nhạy của người làm B sớm hơn thay vì tự tính lại.
