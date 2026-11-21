# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): PhucLocTho (L3A)
- Nhóm được chấm: TENGICUNGDUOC (L3A) · repo https://github.com/haanh293/K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics, nhánh `main`, commit `1da04c2`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện cho `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×, thành công 27,3%), khớp số của chính nhóm. Nêu cả hai số bất lợi kèm cách xử lý: xem lại 100% là 11.743–12.415 đ = 0,98–1,03× (điều kiện 4: giảm xem lại theo bậc) và power 0,64 ở mức +5 điểm (điều kiện 2: Giám đốc vận hành ký chấp nhận MDE 6 điểm). Mỗi điều kiện có ngày kiểm tra. Lưu ý nhỏ: điều kiện 3 và 4 ghi hai vai trò phụ trách thay vì một; mục 3 ghi "tiết kiệm 62%" theo 0,38× chưa tính 82 ca nhân viên làm thay trong phạm vi (dù có nêu 0,49× toàn hệ thống). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Phần A, B khớp đáp án (A2 4.472 đ, gấp 16,3 lần; B1 đủ 9 kịch bản; B4 0,98× và 1,03×) và có nhãn simulated ở `bang_chi_phi.md`, hồ sơ mục 1, 2, 3, 7, `chi_so.md` E2. Phạm vi thu hẹp có lý do bằng số (A3). Nhưng chưa đạt "nhãn ở **mọi** số giả lập": dòng `scope` trong `pilot_plan.yaml` ghi `quoc_te (22.515 đ = 1,88x …)` và `doi_tac (10.215 đ = 0,85x …)` không có nhãn simulated, dù hai số này tính từ cột `_simulated`; nhãn `[simulated]` của câu chỉ đặt sau phần `hang_nang`. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách được tác động: 20 + 20 nhân viên, bốc thăm ngẫu nhiên phân tầng theo 12 depot, đủ 20 cụm mỗi nhóm, giảm ảnh hưởng gián tiếp theo `staff_id`, `interim_looks` chỉ xem an toàn. D1 đúng (1.251 · 3.103 · 1.000 · 300 · m ≥ 299, DE 6,96), nêu rõ đánh đổi MDE 0,06 với power khoảng 0,64 ở mức 5 điểm. 3 luật dừng đủ 4 vế, có ngưỡng, thời hạn, vai trò cụ thể; ngưỡng mở lại +2 điểm so với đối chứng, trần 6%, không đặt dưới mức hiện tại 4,25% (3,97% trong phạm vi). Điểm yếu thiết kế đưa vào câu hỏi và điều kiện, không trừ điểm theo câu chữ rubric. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất khớp số và nêu thẳng hai con số bất lợi (xem lại 100% là 0,98–1,03×; power 0,64 ở mức +5 điểm); pilot tách được tác động với 20 cụm mỗi nhóm. Hội đồng thêm điều kiện trước ngày bắt đầu 2026-12-07:

1. Bỏ chi phí cố định 40 triệu/tháng khỏi ngưỡng 8.000 đ của luật dừng chi phí: ở bước 0.10 (4 nhân viên, khoảng 3.375 việc/tháng) cố định đã khoảng 11.852 đ/việc, tổng khoảng 15.266 đ; ở bước 0.25 (10 nhân viên, khoảng 8.438 việc/tháng) tổng khoảng 8.155 đ [simulated]. Cả hai tuần đầu đều vượt 8.000 đ nên luật tự kích hoạt trước bước 0.50 dù trợ lý không đổi.
2. Hoàn tiền trùng: dừng ngay khi có 1 ca, không chờ 3 ngày liên tiếp; điều kiện chênh 2 điểm so với đối chứng chỉ xét từ bước 10 nhân viên.
3. Gắn nhãn simulated cho hai số `quoc_te` 22.515 đ và `doi_tac` 10.215 đ trong `scope`.

**Một câu hỏi cho đội trình:** Luật dừng chi phí của nhóm tính gộp cả 40 triệu cố định với ngưỡng > 8.000 đ trong 2 tuần liên tiếp. Ở bước 0.10 chi phí khoảng 15.266 đ/việc, ở bước 0.25 khoảng 8.155 đ/việc [simulated], đều vượt 8.000 đ dù trợ lý chạy đúng như đợt thử. Vậy pilot có tự thu hẹp về `noi_dia` trước khi tới bước 0.50, khiến nhóm không đo được `hang_nang` không, và nhóm xử lý thế nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** (chưa có, điền nguyên văn câu trả lời của nhóm TENGICUNGDUOC sau phần hỏi đáp)

*Phân công chấm: C6 Trân; C7 Đức (kiểm phần A, B và nhãn, xem mục 7 báo cáo cá nhân của Đức) cùng phát hiện thiếu nhãn ở `scope` của Ngọc; C8 Ngọc (commit `53acc35`); tổng hợp và chốt: Trân làm thay phần của Đăng, soạn cùng Claude Code từ bằng chứng trong repo nhóm được chấm.*
