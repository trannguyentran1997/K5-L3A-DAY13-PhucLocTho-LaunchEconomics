# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): PhucLocTho (L3A)
- Nhóm được chấm: TENGICUNGDUOC (L3A) · repo https://github.com/haanh293/K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics, nhánh `main`, commit `1da04c2`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện cho `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×, thành công 27,3%), khớp số của chính nhóm. Nêu cả hai số bất lợi kèm cách xử lý: xem lại 100% là 11.743–12.415 đ = 0,98–1,03× (điều kiện 4: giảm xem lại theo bậc) và power 0,64 ở mức +5 điểm (điều kiện 2: Giám đốc vận hành ký chấp nhận MDE 6 điểm). Mỗi điều kiện có ngày kiểm tra. Lưu ý nhỏ: điều kiện 3 và 4 ghi hai vai trò phụ trách thay vì một; mục 3 ghi "tiết kiệm 62%" theo 0,38× chưa tính phần nhân viên làm thay các ca không thành công trong phạm vi (dù có nêu 0,49× toàn hệ thống). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số tính từ phút xem lại / làm lại đều có nhãn simulated: hồ sơ mục 1, 2, 3, 7; `bang_chi_phi.md` A2–B4; `chi_so.md` E2; `pilot_plan.yaml` có mục `simulated_inputs` liệt kê đủ nguồn giả lập. Phạm vi thu hẹp có lý do bằng số theo A3 (1,88× và 0,85× bị loại). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, ngẫu nhiên có seed, phân tầng theo depot, đối chứng cùng tuần: đủ 20 cụm mỗi nhóm. Đủ năm câu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299, DE 6,96), chấp nhận MDE 6 điểm có nêu power 0,64. 3 luật dừng đủ 4 vế, có ngưỡng, thời hạn và người dừng; ngưỡng an toàn so với đối chứng + trần 6%, không đặt 3% dưới mức hiện tại 4,25%. Điểm yếu đưa vào câu hỏi: luật dừng chi phí gộp cả 40 triệu cố định nên sẽ kích hoạt ở bước 4 và 10 người dù trợ lý chạy đúng như đợt thử (khoảng 15.300 đ và 8.155 đ > 8.000 đ); luật an toàn dùng chênh 2 điểm ngay từ bước 4 người, dễ báo nhầm. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất khớp số và nêu thẳng hai con số bất lợi (xem lại 100% là 0,98–1,03×; power 0,64 ở mức +5 điểm); pilot tách được tác động với 20 cụm mỗi nhóm. Hội đồng thêm một điều kiện trước ngày bắt đầu 2026-12-07: tách chi phí cố định khỏi ngưỡng 8.000 đ của luật dừng chi phí (với 4 nhân viên, 40 triệu chia cho khoảng 3.375 việc thành công mỗi tháng là khoảng 11.900 đ/việc, cộng 3.414 đ là khoảng 15.300 đ; với 10 nhân viên khoảng 8.155 đ, luật vẫn kích hoạt dù trợ lý không đổi), và chỉ dùng điều kiện "chênh 2 điểm so với đối chứng" từ bước 10 nhân viên; hoàn tiền trùng thì dừng ngay, không chờ 3 ngày.

**Một câu hỏi cho đội trình:** Luật dừng chi phí của nhóm tính gộp cả 40 triệu cố định. Ở bước 4 nhân viên, chi phí mỗi việc thành công đã khoảng 15.300 đ, ở bước 10 nhân viên khoảng 8.155 đ, đều vượt 8.000 đ dù trợ lý chạy đúng như đợt thử. Vậy pilot có bị thu hẹp về `noi_dia` trước khi tới bước 20 người, và nhóm sẽ không đo được `hang_nang` không?

**Câu trả lời của đội trình (ghi lại tại buổi):** (chưa có, điền nguyên văn câu trả lời của nhóm TENGICUNGDUOC sau phần hỏi đáp)

*Ghi chú: Trân soạn phiếu cùng Claude Code từ bằng chứng trong repo nhóm được chấm (commit `1da04c2`). Điểm C8 giữ 10 theo đúng câu chữ rubric (có đối chứng, đủ mẫu, luật dừng có ngưỡng, thời hạn, người dừng); lỗi luật dừng chi phí là lỗi thiết kế nên đưa vào câu hỏi, không trừ điểm.*
