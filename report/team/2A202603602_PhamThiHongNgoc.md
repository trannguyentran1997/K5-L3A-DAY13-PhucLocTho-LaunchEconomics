# Báo cáo cá nhân — PhamThiHongNgoc-2A202603602

## 1. Thông tin thành viên

- Họ tên: Phạm Thị Hồng Ngọc
- MSSV: 2A202603602
- Email: ngockarryruby@gmail.com
- Vai trong nhóm: Người viết code (phần D — Pilot)

## 2. Phần việc phụ trách

- Phụ trách toàn bộ **Nhiệm vụ D (CP4 — Kế hoạch pilot & tính cỡ mẫu)** theo phân công của nhóm PhucLocTho:
  - Viết code tính cỡ mẫu D1 (5 câu a–e), tính `power` thực tế ở mức chênh +5 điểm khi `n = 859`/nhóm, và tính tỉ lệ `mo_lai_trong_7_ngay` từ `src/logix_requests.csv` trong file nháp `src/nhap_pilot.py` (để không xung đột `src/lab13.py` trong lúc Đức làm phần A, B).
  - Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` gồm chú thích D1, D2 (5 câu tách được tác động), đánh đổi đã chấp nhận, tỉ lệ mở lại hiện tại, các trường YAML đầy đủ và 3 luật dừng theo mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`.
  - Đối chiếu dòng `scope` với kết quả A3 từ `report/team/bang_chi_phi.md`, sau khi Đức hoàn thành mốc 2 sẽ ghép phần D vào `src/lab13.py`, chạy kiểm thử toàn bộ và xoá file nháp `src/nhap_pilot.py`.
  - Tham gia chuẩn bị bảo vệ và duyệt chéo Gate 2a cùng cả nhóm.

## 3. Đóng góp cụ thể

- **Thiết lập môi trường và viết code phần D (ghép vào `src/lab13.py`):**
  - Ban đầu viết độc lập trong `src/nhap_pilot.py` để tránh xung đột với phần A, B của Đức; sau khi Đức hoàn thành nhánh `PhamDuyDuc-2A202603611` (`80048f4`), đã ghép hàm `co_mau` và `phan_tich_pilot_d` vào `src/lab13.py`, chạy kiểm thử toàn bộ A + B + D không lỗi và xoá file nháp `src/nhap_pilot.py`.
  - Đọc dữ liệu `logix_requests.csv` với `keep_default_na=False` để tránh lỗi đọc ô trống thành `NaN`.
  - Xây dựng hàm `co_mau(p1, p2, alpha=0.05, power=0.80)` và hàm `phan_tich_pilot_d(reqs)` đối chiếu song song công thức chuẩn hai tỉ lệ với `statsmodels.stats.power.NormalIndPower`.
  - Tính đủ 5 câu D1:
    - Câu a (theo yêu cầu, MDE +5 điểm): `1.251` yêu cầu/nhóm (`NormalIndPower`: `1.250`).
    - Câu b (theo nhân viên, `m = 75`, `ICC = 0,02`): `DE = 2,48`; `n = 3.103` yêu cầu/nhóm → `42` nhân viên/nhóm (tổng `84 > 40`, không đủ người).
    - Câu c (`20` nhân viên/nhóm): cỡ mẫu hiệu dụng tối đa `20 / 0,02 = 1.000 < 1.251` (không đạt).
    - Câu d (`6` depot/nhóm): cỡ mẫu hiệu dụng tối đa `6 / 0,02 = 300 < 1.251` và chỉ có `6 < 20` cụm/nhóm (loại).
    - Câu e (MDE +6 điểm, `n = 859`/nhóm, `20` nhân viên/nhóm): `m >= 299` yêu cầu/nhân viên (`DE = 6,96`, `n_eff = 859,20`; cần ~`9,7` ngày ≈ 2 tuần ở bước `0.50`).
  - Tính rủi ro đánh đổi: với `n = 859`/nhóm, nếu tác động thật chỉ là `+5` điểm thì `power` chỉ còn `0,6417` (~`64,2%`).
  - Tính tỉ lệ `mo_lai_trong_7_ngay` thực tế từ đợt chạy thử: toàn mẫu `4,25%` (`51/1.200`), phạm vi `noi_dia` + `hang_nang` `3,97%` (`39/982`), làm căn cứ đặt ngưỡng an toàn không bị dừng oan ở tuần đầu.
- **Hoàn thiện `report/team/pilot_plan.yaml`:**
  - Chọn cách chia theo nhân viên (`20` can thiệp + `20` đối chứng, phân tầng theo 12 depot, bốc thăm ngẫu nhiên có seed cố định) để đảm bảo tách được tác động (đạt mốc `20` cụm/nhóm), đồng thời ghi rõ đánh đổi MDE từ `+5` lên `+6` điểm và rủi ro `power = 0,64` ở mức `+5` điểm.
  - Thu hẹp `scope` về `noi_dia` (`2.696 đ = 0,22×` [simulated]) và `hang_nang` (`8.221 đ = 0,69×` [simulated]); loại `quoc_te` (`22.515 đ = 1,88×` [simulated]) và `doi_tac` (`10.215 đ = 0,85×` [simulated]).
  - Viết 3 luật dừng (an toàn, chi phí, mức độ sử dụng) đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, có ngưỡng định lượng, thời hạn, và người phụ trách là vai trò cụ thể (`Giám đốc vận hành LogiX-VN`, `PM trợ lý hoàn phí`, `Trưởng nhóm CSKH`).
  - Gắn nhãn `simulated` cho mọi con số từ cột `_simulated` trong `scope`, `stop_rules`, và `simulated_inputs`; nêu rõ kế hoạch thay bằng số đo thật sau tuần 1 pilot.

## 4. Bằng chứng

- Code phần D tích hợp trong `src/lab13.py` (đã chạy toàn bộ A1, A2, A3, A4, B1–B4, D1 không lỗi; đã xoá file nháp `src/nhap_pilot.py`).
- File kế hoạch pilot: `report/team/pilot_plan.yaml` (đã đối chiếu dòng `scope` khớp 100% với bảng A3 trong `report/team/bang_chi_phi.md` của Đức; qua kiểm tra `yaml.safe_load`, không còn dấu `?` ngoài dòng chú thích, không có từ bị cấm theo quy tắc 5).
- Kết quả chạy `python lab13.py` trong `src/` (phần D1):
  - `a) 1.251 yêu cầu/nhóm (statsmodels: 1.250)`
  - `b) DE = 2,48; n = 3.103 yêu cầu/nhóm; 42 NV/nhóm (tổng 84 > 40)`
  - `c) n_eff tối đa = 1.000 < 1.251`
  - `d) n_eff tối đa = 300 < 1.251`
  - `e) m >= 299 yêu cầu/NV (DE = 6,96; n_eff = 859,20); power ở mức +5 điểm = 0,6417`
  - `mo_lai_trong_7_ngay`: toàn mẫu `4,25%` (`51/1.200`), phạm vi pilot `3,97%` (`39/982`).
- Nhánh & commit trên GitHub: nhánh `PhamThiHongNgoc-2A202603602` (gồm các commit `73aa3d3`, `40ec4ab`, và commit tích hợp phần D vào `src/lab13.py` sẵn sàng để nhóm trưởng merge).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI lập trình (Antigravity / Gemini) trong môi trường IDE.
- **Dùng vào việc gì:** Gợi ý cấu trúc hàm tính cỡ mẫu `co_mau` và `phan_tich_pilot_d` trong `src/nhap_pilot.py`, soát lại định dạng YAML và các tiêu chí rubric cho `report/team/pilot_plan.yaml`, và tổng hợp nháp báo cáo cá nhân.
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp `src/nhap_pilot.py` trên dữ liệu gốc `src/logix_requests.csv` (không bịa số) và đối chiếu công thức tính tay cho từng câu D1 (ví dụ: kiểm tra tay `20m >= 859 * (0,98 + 0,02m) => 2,82m >= 841,82 => m >= 298,52 -> 299`, kiểm tra trần `c / ICC = 20 / 0,02 = 1.000` và `6 / 0,02 = 300`).
  - Đối chiếu số liệu của code với `statsmodels.stats.power.NormalIndPower` và hướng dẫn tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai lệch < 0,2%, nằm trong ngưỡng cho phép 2%).
  - Chạy lệnh kiểm tra tự động `yaml.safe_load(open('../report/team/pilot_plan.yaml'))`, `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` và lệnh kiểm tra từ bị cấm theo quy tắc 5 trong `README.md` để chắc chắn đúng cú pháp và không vi phạm quy tắc.
  - Tự rà soát lại phần giải thích về hệ số thiết kế `DE`, cỡ mẫu hiệu dụng khi chia theo cụm và lý do chấp nhận đánh đổi MDE `+6` điểm để sẵn sàng trả lời trực tiếp trước hội đồng Gate 2a.

## 6. Tự đánh giá

- **Điểm làm tốt:** Hoàn thành đầy đủ Nhiệm vụ D đúng phân công, đảm bảo độc lập về file để không gây xung đột Git với các thành viên khác; tất cả con số đều tính từ code chạy trên CSV gốc, có nhãn `simulated` đầy đủ và nêu thẳng con số bất lợi (`power = 0,64` ở mức `+5` điểm) kèm cách kiểm soát.
- **Điểm cần lưu ý / hoàn thiện tiếp:** Chờ nhóm trưởng merge các nhánh vào `main`, đọc kỹ phần A, B, C, E của các thành viên để chuẩn bị bảo vệ và duyệt chéo Gate 2a (17:00), sau đó tự nộp link repo nhóm trên LMS trước 23h59 GMT+7.
