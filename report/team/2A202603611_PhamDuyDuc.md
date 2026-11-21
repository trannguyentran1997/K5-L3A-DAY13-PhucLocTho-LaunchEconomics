# Báo cáo cá nhân — PhamDuyDuc-2A202603611

## 1. Thông tin thành viên

- Họ tên: Phạm Duy Đức
- MSSV: `2A202603611`
- Email: `phamduclc3@gmail.com`
- GitHub: `DuyJob`
- Vai trong nhóm: Người viết code (phần A, B)

## 2. Phần việc phụ trách

Theo phân công nhóm PhucLocTho (`PHAN_CONG_NHOM.md`), tôi phụ trách toàn bộ **Nhiệm vụ A (A1–A4)** và **Nhiệm vụ B (B1–B4)** — phần mô hình chi phí và bảng độ nhạy:

- Viết code phần A và B trong `src/lab13.py` (không sửa hai file CSV gốc, giữ nguyên vùng `TODO CP4` cho phần D của Ngọc).
- Hoàn thiện bảng số liệu và câu trả lời phân tích trong `report/team/bang_chi_phi.md`.
- Cung cấp các con số đầu vào cho đồng đội: tỉ lệ thành công và bội số chi phí theo loại (A3) cho `pilot_plan.yaml` của Ngọc; các chỉ số độ nhạy chi phí và kịch bản xem lại 100% (B1–B4) cho bảng rủi ro kinh tế trong `chi_so.md` của Đăng và hồ sơ tổng hợp `ho_so_launch_v0.md` của Trân.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A1:** Cài đặt 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` trong `src/lab13.py`, vượt qua cả 3 phép thử đáp án biết trước (`1,20` · `1,25` · `1,25`).
- **Nhiệm vụ A2:** Cài đặt hàm `mo_hinh(runs, reqs, …)` tính tử số trên mọi lần chạy kể cả lần lỗi và mẫu số chỉ đếm `ket_qua == 'thanh_cong'` (`978` việc). Kết quả: tổng chi phí `4.373.585 đ`, chi phí mỗi việc thành công `4.472 đ` (`simulated`), gấp `16,3` lần hoá đơn token + tool chia số yêu cầu (`274,7 đ`); làm lại chiếm lớn nhất (`51,8%`, `simulated`), xem lại chiếm `40,7%` (`simulated`); chi phí cả hệ thống đạt `5.865 đ/yêu cầu = 0,49×` (`simulated`).
- **Nhiệm vụ A3:** Tách chi phí theo 4 loại yêu cầu (`noi_dia` `0,22×`, `hang_nang` `0,69×`, `doi_tac` `0,85×`, `quoc_te` `1,88×`, `simulated`) và lập bảng tỉ lệ `status == ok` theo từng lần thử, chứng minh `quoc_te` không nên đưa vào pilot (lần 1: `30,0%`, lần 2: `11,4%`, lần 3: `2,2%`).
- **Nhiệm vụ A4:** Tính chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia` + `hang_nang` dựa trên tỉ lệ thành công toàn mẫu (`900 / 1.200`): ở `45.000` yêu cầu/tháng (`33.750` việc) cố định là `1.185 đ/việc`, tổng `4.599 đ = 0,38×` (`simulated`); ở nửa khối lượng (`16.875` việc) cố định là `2.370 đ/việc`, tổng `5.784 đ = 0,48×` (`simulated`).
- **Nhiệm vụ B1–B4:** Chạy đủ 9 kịch bản độ nhạy (B1), kịch bản kết hợp token × 2 và xem lại × 2 cho `6.543 đ (+46,3%, simulated)` và xếp hạng 3 yếu tố mạnh nhất: 1. Số ca làm lại (`+51,8%`) · 2. Tỉ lệ xem lại (`+40,7%`) · 3. Lương nhân viên (`+23,1%`) (B2); so sánh giới hạn 1/2/3 lần chạy theo chi phí cả hệ thống — 2 lần rẻ nhất `6.901.220 đ` (`simulated`) (B3); tính kịch bản xem lại 100% cho `noi_dia` + `hang_nang`: `11.743 đ = 0,98×` ở mức 9 phút làm lại và `12.415 đ = 1,03×` ở mức trung bình dữ liệu `15,3` phút làm lại (`simulated`), kèm mức hoà vốn lần lượt `≤ 5,1` phút và `≤ 4,8` phút (B4).

## 4. Bằng chứng

- **Nhánh làm việc:** `PhamDuyDuc-2A202603611` trên repo nhóm `https://github.com/trannguyentran1997/K5-L3A-DAY13-PhucLocTho-LaunchEconomics`.
- **Các file đã hoàn thiện:**
  - `src/lab13.py` (chạy hoàn chỉnh từ đầu đến cuối, in `Ba phép thử đáp án biết trước: ĐẠT` cùng toàn bộ bảng A2, A3, A4, B1–B4).
  - `report/team/bang_chi_phi.md` (đủ các bảng A1–A4, B1–B4, gắn nhãn `simulated` ở mọi con số tính từ cột `_simulated`, không còn chỗ trống chưa điền).
- **Các commit đã push:**
  - `80048f4` — `feat(Duc): hoan thanh phan A va B - mo hinh chi phi va bang do nhay`
  - `e383534` — `fix(Duc): sua loi encoding UTF-8, cong thuc A4 va bo sung A3/B4`

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI tích hợp trong IDE (Antigravity) dùng để gợi ý cấu trúc code Python cho phần A, B, rà soát công thức, kiểm tra lỗi hiển thị UTF-8 và đối chiếu checklist rubric.
- **Cách tự kiểm tra kết quả:**
  - Tự chạy trực tiếp `python lab13.py` trên dữ liệu gốc `src/logix_runs.csv` và `src/logix_requests.csv` (có `keep_default_na=False`), xác nhận cả 3 phép thử A1 đạt `1,20` · `1,25` · `1,25`.
  - Kiểm tra tính đối xứng độ nhạy B1 (các kịch bản giảm một nửa giảm đúng bằng nửa mức tăng của kịch bản gấp đôi: `+5,6% / −2,8%`, `+40,7% / −20,3%`, `+51,8% / −25,9%`) và tính tuyến tính ở B2 (`5,6% + 40,7% = 46,3%`).
  - Đối chiếu số đầu ra với tài liệu hướng dẫn (`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`), qua đó phát hiện và sửa kịp thời 2 lỗi ở lần push đầu: lỗi font UTF-8 khi chuyển nhánh trên PowerShell và lỗi chia mẫu số ở A4 (chia `982` thay vì `1.200`), đưa toàn bộ số về khớp chính xác trong ngưỡng 0%.
  - Kiểm tra tự động không còn dấu ba chấm chưa điền, không còn từ bị cấm theo quy tắc 5, và không chỉnh sửa file chung hay file mẫu `MSSV_HoTen.md`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ 100% phạm vi nhiệm vụ A và B được phân công, giữ sạch phạm vi file cá nhân để không xung đột khi ghép nhánh với các thành viên khác.
- Hiểu rõ bản chất kinh tế của mô hình chi phí agent: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, vì sao giờ nhân viên (làm lại và xem lại) mới là yếu tố chi phối chi phí thay vì giá token, và sự khác biệt giữa tối ưu chi phí mỗi việc thành công (1 lần chạy) với tối ưu tổng chi phí cả hệ thống (2 lần chạy).
- Bài học rút ra: luôn xác định rõ mẫu số gốc khi quy đổi từ mẫu sang quy mô tháng (A4) và luôn kiểm tra lại mã hoá UTF-8 khi thao tác file trên PowerShell Windows trước khi push.

## 7. Đánh giá chéo phần làm của nhóm bạn (nhóm TENGICUNGDUOC)

- **Repo được chấm:** `https://github.com/haanh293/K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics` (nhánh `main`, commit `1da04c2`; phần A & B do Nguyễn Hà Anh — `2A202603605` phụ trách tại commit `5c78f6d`).
- **Phạm vi chấm:** Phần Nhiệm vụ A (A1–A4), Nhiệm vụ B (B1–B4) trong `src/lab13.py` và `report/team/bang_chi_phi.md`, cùng phần liên kết số liệu chi phí vào `report/team/ho_so_launch_v0.md` và `report/team/pilot_plan.yaml`.

### Điểm chấm phần A & B (thang Rubric C1–C2)

| Tiêu chí | Điểm tối đa | Điểm chấm | Nhận xét dựa trên bằng chứng |
| --- | ---: | ---: | --- |
| C1 — Nhiệm vụ A (CP1: A1–A4) | 20 | **20 / 20** | `python lab13.py` chạy sạch từ đầu đến cuối, in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`). A2 khớp 0% sai số (`4.472 đ` `simulated`, gấp `16,3×` hoá đơn `274,7 đ`, `978` thành công, làm lại `51,8%`, xem lại `40,7%`). A3 tách đủ 4 loại kèm bảng tỉ lệ `ok` theo lần thử (`quoc_te`: `30,0% → 11,4% → 2,2%`). A4 tính đúng trên mẫu `1.200` (`4.599 đ = 0,38×` ở `33.750` việc/tháng; `5.784 đ = 0,48×` ở `16.875` việc/tháng, `simulated`) và còn tính thêm điểm hoà vốn khối lượng (`~4.659` việc/tháng). |
| C2 — Nhiệm vụ B (CP2: B1–B4) | 15 | **15 / 15** | B1 đủ 9 kịch bản đơn lẻ, khớp 0% sai số và đúng tính đối xứng (`+5,6%/−2,8%`, `+40,7%/−20,3%`, `+51,8%/−25,9%`). B2 đúng kịch bản cặp (`6.543 đ`, `+46,3%`) và xếp hạng top 3 (`1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên`). B3 chỉ rõ giới hạn 2 lần rẻ nhất cả hệ thống (`6.901.220 đ` so với 1 lần `7.449.781 đ`, `simulated`). B4 nêu đủ cả 2 mức `9` phút (`11.743 đ = 0,98×`) và `15,3` phút (`12.415 đ = 1,03×`, `simulated`) cùng mức hoà vốn (`≤ 5,1` và `≤ 4,8` phút). |
| **Tổng phần A & B** | **35** | **35 / 35** | Đủ nhãn `simulated`, không còn dấu ba chấm chưa điền, không có từ cấm theo quy tắc 5, code cấu trúc rõ ràng và đã tích hợp luôn phần D. |

### Nhận xét chi tiết & điểm cần góp ý (góc nhìn duyệt chéo Gate 2a)

1. **Điểm mạnh nổi bật:**
   - Code `src/lab13.py` tổ chức gọn theo từng hàm (`in_ket_qua_cp1`, `in_ket_qua_cp2`, `in_ket_qua_cp4`), tự kiểm chứng được cả A, B lẫn D trong một lần chạy.
   - `report/team/bang_chi_phi.md` trình bày đầy đủ, ngắn gọn, có nhãn `simulated` nhất quán, bổ sung phân tích rất tốt như điểm hoà vốn khối lượng ở A4 (`~6.212` yêu cầu/tháng) và mức chênh chi phí cả hệ thống ở B3 (`+548.561 đ` khi cắt từ 2 xuống 1 lần chạy).
   - Hồ sơ `ho_so_launch_v0.md` giữ đề xuất **Go có điều kiện** nhất quán với bằng chứng, nêu thẳng các con số bất lợi (xem lại 100% lên `11.743–12.415 đ`, power `0,64` ở mức chênh 5 điểm).
2. **Điểm cần lưu ý / góp ý cải thiện (kèm câu hỏi phản biện):**
   - **Bẫy chi phí cố định trong luật dừng `> 8.000 đ` (`pilot_plan.yaml`):** Nhóm viết luật dừng chi phí *"đo gộp `noi_dia + hang_nang` cả chi phí cố định `> 8.000 đ` trong 2 tuần liên tiếp"*. Tuy nhiên ở bước rollout `0.10` (`4` nhân viên ≈ `3.375` việc/tháng), riêng chi phí cố định `40 triệu đ/tháng` đã là `11.852 đ/việc` (tổng `~15.266 đ/việc`); ở bước `0.25` (`10` nhân viên ≈ `8.438` việc/tháng), cố định là `4.741 đ/việc` (tổng `~8.155 đ/việc`). Cả 2 tuần đầu đều vượt `8.000 đ` và tự kích hoạt luật dừng trước khi kịp lên bước `0.50` (`5.784 đ/việc`). Nhóm nên quy định rõ luật dừng ở bước `0.10–0.25` đo theo **chi phí biến đổi** hoặc chỉ cộng chi phí cố định từ bước `0.50`.
   - **Diễn đạt ở mục 3 (`ho_so_launch_v0.md`):** Câu *"đạt `0,38×` so với `12.000 đ` của nhân viên (tiết kiệm 62% chi phí)"* dễ gây hiểu nhầm vì `4.599 đ` là chi phí trên mỗi việc **trợ lý làm xong**, chưa cộng `82` ca `noi_dia + hang_nang` không thành công do nhân viên làm thay; nên nhấn mạnh thêm con số chi phí cả hệ thống để tránh lạc quan quá mức.
   - **Chi tiết hình thức nhỏ:** `src/lab13.py` còn sót 2 dòng comment `# TODO CP1`, và điều kiện 3–4 trong `ho_so_launch_v0.md` gán 2 vai trò phụ trách cùng lúc thay vì chốt đúng 1 người chịu trách nhiệm cuối cùng.
- **Câu hỏi phản biện dành cho nhóm bạn:** *"Nếu luật dừng chi phí của nhóm cộng cả chi phí cố định 40 triệu đ/tháng vào mức trần 8.000 đ/việc, thì ngay ở tuần 1 (rollout 0.10, ~3.375 việc/tháng → ~15.266 đ/việc) và tuần 2 (rollout 0.25, ~8.438 việc/tháng → ~8.155 đ/việc), luật dừng sẽ tự kích hoạt trước khi đạt bước 0.50 — nhóm sẽ điều chỉnh cách đo chi phí ở hai bước đầu như thế nào?"*
