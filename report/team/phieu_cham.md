# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): PhucLocTho (Lớp L3A)
- Nhóm được chấm: TENGICUNGDUOC (Lớp L3A — https://github.com/haanh293/K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | (Trân chấm C6) | (Trân điền sau khi đọc `ho_so_launch_v0.md`) |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | (Đức chấm C7) | (Đức điền sau khi đọc `bang_chi_phi.md` và mục 1, 2, 3, 7; lưu ý kiểm tra vế sau của `scope` trong `pilot_plan.yaml` về nhãn `simulated` cho `quoc_te` 22.515 đ và `doi_tac` 10.215 đ) |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách được tác động (20 + 20 NV, bốc thăm ngẫu nhiên phân tầng 12 depot, đủ 20 cụm/nhóm, có giảm spillover theo `staff_id` và `interim_looks` chỉ xem an toàn); tính đúng D1 (`1.251 · 3.103 · 1.000 · 300 · m ≥ 299`, `DE = 6,96`) và nêu rõ đánh đổi `MDE = 0,06` (`power ≈ 0,64` ở mức 5 điểm); 3 luật dừng đủ 4 vế có ngưỡng, thời hạn và vai trò cụ thể, ngưỡng mở lại `+2 điểm / trần 6%` tránh bẫy `4,25%` (`3,97%` phạm vi) hiện tại. Kiến nghị sửa trước khi chạy: (1) luật dừng 2 cộng gộp 40 tr/tháng cố định khiến bước `0.10` (~15.266 đ [simulated]) và `0.25` (~8.155 đ [simulated]) đều vượt `8.000 đ` 2 tuần liên tiếp và tự kích hoạt trước khi sang bước `0.50`; (2) tách `>= 1 ca hoàn tiền trùng` thành tắt ngay thay vì chờ `3 ngày liên tiếp`. |
| **Tổng** | | | | **(Đăng chốt) / 30** | |

**Quyết định của hội đồng:** Go · Go có điều kiện · No-go (cả nhóm chốt sau khi gộp C6, C7, C8; từ góc độ C8 đề xuất **Go có điều kiện** yêu cầu sửa luật dừng 1 và 2 trước khi bật rollout)

**Lý do:** (Đăng tổng hợp từ C6, C7, C8; riêng C8: thiết kế tách được tác động và đủ mẫu với MDE 6 điểm, nhưng cần bỏ chi phí cố định 40 tr/tháng khỏi ngưỡng dừng `8.000 đ` ở bước `0.10`–`0.25` và tách lỗi hoàn tiền trùng thành tắt ngay để pilot không bị dừng sai hoặc chậm phản ứng an toàn.)

**Một câu hỏi cho đội trình:** Ở luật dừng chi phí, nhóm đo gộp cả 40 triệu đ/tháng cố định với ngưỡng `> 8.000 đ` trong 2 tuần liên tiếp; trong khi ở bước rollout `0.10` (4 người, ~15.266 đ/việc [simulated]) và `0.25` (10 người, ~8.155 đ/việc [simulated]) chi phí đều vượt `8.000 đ`, vậy luật này có làm pilot tự động thu hẹp ngay trước khi kịp tới bước `0.50` không và nhóm xử lý thế nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** (ghi lại trong phiên trình bày Gate 2a)
