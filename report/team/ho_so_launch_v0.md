# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: PhucLocTho · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** mỗi việc thành công [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí (làm lại 51,8%, xem lại 40,7%) [simulated]. Chưa cộng chi phí cố định. Nguồn: `bang_chi_phi.md` A2 | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi **+51,8%** · 2. Tỉ lệ xem lại gấp đôi **+40,7%** · 3. Lương tăng 25% **+23,1%** [simulated]. Giá token gấp đôi chỉ +5,6%. Nguồn: B1, B2 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống **5.865 đ/yêu cầu = 0,49×** của 12.000 đ (đã tính 222 ca nhân viên làm thay) [simulated]. Phạm vi `noi_dia` + `hang_nang` cộng cố định 40 triệu/tháng: **4.599 đ = 0,38×** ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× nếu khối lượng còn một nửa [simulated]. `quoc_te` 1,88× và `doi_tac` 0,85× nên loại khỏi pilot | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại trong 7 ngày **4,25%** (51/1.200), 3,97% trong phạm vi pilot. 12 event đều có `trace_id`, 5 chỉ số đều tính được từ event. Đợt chạy thử không có đối chứng nên chưa kết luận được trợ lý làm chỉ số chính thay đổi bao nhiêu. Nguồn: `chi_so.md` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Bảng khắc phục 5 ca đủ 5 loại (ca 14, 20, 16, 19, 5), mỗi dòng có event, ngưỡng và một vai trò. **Mới có 1 bộ nhãn độc lập (Đăng)**; bộ nhãn thứ hai và tỉ lệ đồng thuận (cần ≥ 16/20) chưa xong. Hai lỗi sai tiền thật: báo "đã hoàn" khi sổ cái lỗi (ca 7), hoàn hai lần (ca 20). Nguồn: `bang_loi.md` | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên **20 + 20** (20 cụm mỗi nhóm), ngẫu nhiên phân tầng theo depot. Không cách chia theo cụm nào đủ mẫu cho +5 điểm (trần 1.000 < 1.251) nên chấp nhận **MDE +6 điểm**: n = 859/nhóm, m ≥ 299 yêu cầu/nhân viên, DE 6,96. **Bất lợi:** nếu tác động thật chỉ +5 điểm thì power còn **0,64**. 4 luật dừng có ngưỡng, thời hạn, người dừng; quyết định ngày 2027-01-05. Nguồn: `pilot_plan.yaml` | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%). **Xem lại 100%: 11.743 đ = 0,98×**, thành **12.415 đ = 1,03×** nếu làm lại 15,3 phút như dữ liệu, tức đắt hơn nhân viên tự làm; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút. Khối lượng còn một nửa: cố định +2.370 đ/việc [simulated]. Nguồn: `chi_so.md` E2 | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ `noi_dia` + `hang_nang`, 40 nhân viên chia 20 + 20, bắt đầu 2026-12-01. Mọi con số chi phí trong hồ sơ là simulated. Hai con số bất lợi nhóm không bỏ qua: xem lại 100% làm chi phí ngang hoặc vượt nhân viên tự làm (0,98–1,03×), và power chỉ 0,64 nếu tác động thật là +5 điểm. Bốn điều kiện phải đạt:

- Sửa khoá chống trùng và đối soát sổ cái (ca 20, ca 7), chạy thử đối soát ra 0 ca trùng. Phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-11-28.
- Ký chấp nhận MDE +6 điểm và rủi ro power 0,64 ở mức +5 điểm. Phụ trách: Giám đốc vận hành. Kiểm tra: 2026-11-28.
- Bật đủ 12 event có `trace_id`; sau tuần 1 thay phút simulated bằng phút đo thật và tính lại chi phí mỗi việc thành công. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2026-12-08.
- Giảm xem lại theo bậc: dưới 50% yêu cầu được xem lại ở cuối bước rollout 0.25, mỗi lần xem lại ≤ 5 phút, vì xem lại 100% thì không tiết kiệm (B4). Phụ trách: Trưởng nhóm CSKH. Kiểm tra: 2026-12-15.
