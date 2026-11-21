# Phân công nhóm PhucLocTho · Lab 13 Launch Economics

Nhóm 4 người: **Trân (trưởng nhóm)**, **Đức**, **Ngọc**, **Đăng**. Mỗi người nhận **một phần riêng**, bắt đầu cùng lúc từ 14:10, không ai phải ngồi đợi ai; ai xong phần mình là xong. Đề bài gốc vẫn là [README.md](README.md), [CHECKPOINTS.md](CHECKPOINTS.md), [RUBRIC.md](RUBRIC.md), [SUBMISSION.md](SUBMISSION.md); cách làm từng bước và số tự đối chiếu nằm trong [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## 1. Cần nộp gì

Một bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN, sau đó bảo vệ trước hội đồng Gate 2a và chấm một nhóm khác.

| Mốc | Việc |
| --- | --- |
| 17:00 | `report/team/ho_so_launch_v0.md` đủ 7 mục, gửi nhóm hội đồng |
| 17:00–17:45 | Duyệt chéo Gate 2a, **cả nhóm có mặt** |
| 17:45–18:00 | Commit, push bản làm tại lớp |
| 23h59 GMT+7 ngày lab | Hạn nộp. **Mỗi người tự nộp link repo nhóm trên LMS**, ai không nộp thì không có điểm |

Điểm: 70 đối chiếu đáp án (A 20 · B 15 · C 10 · D 15 · E 10) + 30 hội đồng chấm. Số được nhận nếu lệch không quá 2%.

## 2. Bốn phần riêng

| Thành viên | Phần | Nhiệm vụ | File giữ (chỉ người này sửa) | Bắt đầu → xong dự kiến |
| --- | --- | --- | --- | --- |
| **Đức** | Chi phí | A + B | `src/lab13.py` (phần A, B), `report/team/bang_chi_phi.md` | 14:10 → 15:20 |
| **Ngọc** | Pilot | D | `src/nhap_pilot.py` (file nháp), `report/team/pilot_plan.yaml`; cuối cùng dán phần D vào `src/lab13.py` | 14:10 → 16:00 |
| **Đăng** | Lỗi và chỉ số | C + E1, E2 | `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/phieu_cham.md` | 14:10 → 15:45 |
| **Trân** (trưởng nhóm) | Tổng hợp | Gắn nhãn 2 cho C, hồ sơ E3, nộp bài | `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md` | 14:10 → 17:00 |

Mỗi người tự tạo báo cáo cá nhân `report/team/MSSV_HoTen.md` (copy từ file mẫu, **không sửa file mẫu**).

> Cột "Người phụ trách" trong các bảng hồ sơ ghi **một vai trò của LogiX-VN** (ví dụ "PM trợ lý hoàn phí", "Kỹ sư trưởng agent", "Trưởng nhóm CSKH", "Kế toán trưởng", "Giám đốc vận hành"), không ghi tên thành viên nhóm và không ghi "cả đội".

## 3. Ba điểm chạm không tránh được

Đề bài buộc có ba chỗ nối giữa các phần. Đã sắp để không ai phải ngồi chờ:

1. **Gắn nhãn C cần hai người độc lập.** Ngay 14:10, Trân và Đăng cùng gắn nhãn 20 ca, mỗi người một mình, 8 phút, không trao đổi, không xem bảng "Nhãn tham khảo". Trân chụp hoặc nhắn bộ nhãn của mình cho Đăng rồi quay về phần mình; phần so nhãn và bảng khắc phục do Đăng làm một mình.
2. **Hai dòng dùng số của Đức.** Dòng `scope` trong `pilot_plan.yaml` (Ngọc) cần tỉ lệ A3; bảng rủi ro E2 trong `chi_so.md` (Đăng) cần số độ nhạy B. Đức push `bang_chi_phi.md` theo hai mốc (xong A3 khoảng 14:50, xong B khoảng 15:20). Ngọc và Đăng **để hai dòng này làm cuối cùng** trong phần mình, lúc đó số đã có sẵn trên GitHub.
3. **Hồ sơ launch là bản tổng hợp.** Trân điền từng mục ngay khi file nguồn được push, không đợi đủ cả bốn mới bắt đầu.

Ngoài ra, cả nhóm cùng làm ba việc chung: duyệt chéo Gate 2a (17:00), báo cáo cá nhân, nộp link trên LMS.

## 4. Việc chi tiết từng phần

### Đức · Phần chi phí (A + B)

- [ ] Trong `src/lab13.py`, viết 3 hàm A1 ở dòng `TODO CP1`. **Chưa đạt cả ba (1,20 · 1,25 · 1,25) thì không làm tiếp.**
- [ ] Viết `mo_hinh(runs, reqs, …)` (A2): tử số tính **mọi** lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Số tự đối chiếu: khoảng 4.472 đ mỗi việc thành công [simulated], 978 việc thành công, gấp khoảng 16,3 lần hoá đơn chia số yêu cầu.
- [ ] A3: gọi lại `mo_hinh` cho 4 giá trị `loai`, tính thêm tỉ lệ ok theo từng lần thử. A4: cộng cố định 40 triệu/tháng cho phạm vi `noi_dia` + `hang_nang`.
- [ ] **Push mốc 1** (`lab13.py` + `bang_chi_phi.md` có A2, A3, A4).
- [ ] B1 (9 kịch bản), B2 (cặp), B3 (giới hạn 1/2/3 lần, chi phí cả hệ thống), B4 (xem lại 100%, ghi cả mức 9 phút và 15,3 phút).
- [ ] Điền đủ `bang_chi_phi.md`: A2 9 dòng (hai dòng xem lại, làm lại có nhãn `simulated`), A3 4 dòng, A4, B1 9 dòng, xếp hạng 3 yếu tố, B3, B4 (mỗi câu ≤ 3 dòng, có số).
- [ ] **Push mốc 2**, nhắn nhóm "lab13.py xong phần A, B". Sau mốc này Đức không sửa `lab13.py` nữa.
- **Xong khi:** `python lab13.py` in ba phép thử ĐẠT, bảng A2, A3, B; `bang_chi_phi.md` không còn `...`.

### Ngọc · Phần pilot (D)

- [x] Viết code D1 trong file nháp riêng `src/nhap_pilot.py` (đọc CSV như `lab13.py`, có `keep_default_na=False`) để không đụng file của Đức: 5 câu a–e (theo yêu cầu, nhân viên m = 75, 20 nhân viên mỗi nhóm, 6 depot mỗi nhóm, mức chênh 6 điểm); tỉ lệ `mo_lai_trong_7_ngay` hiện tại (toàn mẫu và phạm vi `noi_dia` + `hang_nang`); power khi n = 859 mà tác động thật chỉ 5 điểm.
- [x] `pilot_plan.yaml`: chú thích D1, D2 (5 câu "tách được tác động"), đánh đổi đã chấp nhận, mọi trường, ≥ 3 luật dừng (an toàn, chi phí, mức độ sử dụng) đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ. Ngưỡng an toàn không đặt thấp hơn tỉ lệ mở lại đang có.
- [ ] Làm cuối: dòng `scope`, lấy tỉ lệ A3 từ `bang_chi_phi.md` trên GitHub.
- [ ] Sau khi Đức báo xong mốc 2: `git pull`, dán phần D từ file nháp vào `src/lab13.py` (hàm đặt trên dòng `if __name__`, lời gọi đặt ở cuối khối main thay dòng `TODO CP4`), chạy `python lab13.py` hết không lỗi, **xoá `src/nhap_pilot.py`**, push.
- [x] Chạy 2 lệnh tự kiểm trong `src/`:
  ```bash
  python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"
  grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'    # không được in gì
  ```
- **Xong khi:** `pilot_plan.yaml` qua 2 lệnh trên; `lab13.py` in thêm 5 câu D1.

### Đăng · Phần lỗi và chỉ số (C + E1, E2)

- [ ] 14:10: gắn nhãn 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi") **một mình, 8 phút**, theo 5 loại Google PAIR (Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm). Gắn theo nguyên nhân gốc, không theo chỗ cần sửa. Lưu bản ghi trước khi xem nhãn của Trân.
- [ ] `bang_loi.md`: nhập cả hai bộ nhãn **đúng như lúc gắn độc lập, không sửa sau khi đã so**; tỉ lệ đồng thuận = số ca trùng ÷ 20 (cần ≥ 16/20, thấp hơn thì viết lại định nghĩa); một câu quy tắc cho mỗi ca lệch; bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách.
- [ ] `chi_so.md` E1: tự tính 3 chỉ số (chính, dùng, an toàn) bằng vài dòng pandas, ghi đoạn code vào file làm cách tính; thêm 1 chỉ số dùng + 1 chỉ số an toàn tự đề xuất; ≥ 6 event, mỗi event có `trace_id`; kiểm tra chéo chỉ số nào tính từ event nào. Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số".
- [ ] Làm cuối: E2, ≥ 2 dòng rủi ro kinh tế, số lấy từ bảng độ nhạy trong `bang_chi_phi.md`.
- [ ] Gate 2a: giữ `phieu_cham.md`, chấm nhóm n + 1 theo 3 tiêu chí, điểm nào cũng có lý do bằng số, kèm quyết định và một câu hỏi; ghi lại câu trả lời của đội trình.
- **Xong khi:** `bang_loi.md`, `chi_so.md` không còn `...`; sau Gate 2a thì `phieu_cham.md` đủ.

### Trân · Phần tổng hợp (trưởng nhóm)

- [ ] Trước buổi: mời Đức, Ngọc, Đăng làm collaborator (Settings → Collaborators); kiểm tra repo public hoặc đã mời giảng viên.
- [ ] 14:10: gắn nhãn 20 ca **một mình, 8 phút**, gửi bản ghi cho Đăng, rồi không tham gia phần C nữa.
- [ ] `TEAM.md`: tên nhóm, lớp, URL repo, bảng thành viên (họ tên, MSSV, email, GitHub, vai), đóng góp từng người, commit chốt.
- [ ] `ho_so_launch_v0.md`: điền mục nào ngay khi file nguồn của mục đó được push.

  | Mục hồ sơ | Lấy từ | Có khoảng |
  | --- | --- | --- |
  | 5 · Bảng lỗi | `bang_loi.md` (Đăng) | 15:00 |
  | 1 · Chi phí, 3 · So với nhân viên | `bang_chi_phi.md` mốc 1 (Đức) | 14:50 |
  | 2 · Ba yếu tố nhạy nhất | `bang_chi_phi.md` mốc 2 (Đức) | 15:20 |
  | 4 · Ba chỉ số, 7 · Rủi ro kinh tế | `chi_so.md` (Đăng) | 15:45 |
  | 6 · Pilot plan | `pilot_plan.yaml` (Ngọc) | 16:00 |

  Mỗi mục có con số chính, trạng thái (**Xong, có bằng chứng · Chưa · Giả lập**; mục 1, 2, 3, 7 ghi Giả lập), người phụ trách là một vai trò.
- [ ] Dòng cuối: **Go · Go có điều kiện · No-go**. Go có điều kiện thì mỗi điều kiện có người phụ trách và ngày kiểm tra. Nêu cả con số bất lợi (xem lại 100% thì không tiết kiệm; power chỉ khoảng 0,64 nếu tác động thật là 5 điểm) kèm cách xử lý.
- [ ] 16:45: soát cuối (mục 6) và chạy `python lab13.py` trên máy mình (đề yêu cầu chạy được trên một máy khác).
- [ ] 17:00: gửi hồ sơ cho hội đồng, trình bày 1 phút. 17:45: `group_report.md`, push cuối.

## 5. Trước Gate 2a: 10 phút đọc phần của nhau

Hội đồng và giảng viên có thể hỏi **bất kỳ ai** trong nhóm. Lúc 16:50, mỗi người đọc lướt ba phần còn lại để tự trả lời được:

1. Vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công (phần Đức).
2. Cỡ mẫu hiệu dụng khi chia theo cụm, vì sao số cụm quyết định chứ không phải tổng số yêu cầu (phần Ngọc).
3. Lý do của đề xuất cuối, kể cả con số bất lợi (phần Trân).

## 6. Quy ước làm chung

**Git.** Mỗi người clone repo nhóm (không làm trên repo đề bài):

```bash
git clone https://github.com/trannguyentran1997/K5-L3A-DAY13-PhucLocTho-LaunchEconomics.git
cd K5-L3A-DAY13-PhucLocTho-LaunchEconomics/src
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1   ·   macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
```

- Chỉ sửa file mình giữ (bảng mục 2). Cần đổi file người khác thì nhắn người đó.
- `src/lab13.py`: chỉ Đức sửa cho tới khi báo xong mốc 2; sau đó chỉ Ngọc dán phần D vào.
- Trước mỗi lần push: `git pull --rebase`, rồi `git add <file của mình>` (không dùng `git add .`), commit, push.
- Không force-push, không xoá commit, không commit `.venv/` hay `.env`. Không sửa hai file CSV.

**Số liệu.**

- Mọi con số do code của nhóm tính ra, hoặc tính tay có ghi cách tính. Không dùng AI để bịa số, nhãn lỗi hay kết quả chấm.
- Số lấy từ cột `phut_xem_lai_simulated`, `phut_lam_lai_simulated` (và mọi số tính từ chúng) luôn có nhãn `simulated`.
- Giảng viên vẫn chiếu slide chữa theo lịch lớp (A 14:50, B 15:20, C 16:05, D 16:33, E 16:57): ai giữ phần nào thì đối chiếu phần đó, lệch quá 2% thì tự sửa.
- Mỗi câu trả lời không quá 3 dòng, có ít nhất 1 con số.
- Không dùng từ tiếng Anh bị cấm ở quy tắc 5 trong `README.md` (Gate 2a chỉ duyệt kế hoạch pilot).

## 7. Soát trước khi gửi hội đồng (16:45, Trân)

Chạy trong `src/` sau khi `git pull`:

```bash
python lab13.py                                   # chạy hết, ba phép thử in ĐẠT
grep -rni production ../report/team               # không được in gì
grep -rn "\.\.\." ../report/team/*.md             # còn chỗ "..." chưa điền thì báo người giữ file
```

- [ ] Mọi số giả lập có nhãn `simulated`.
- [ ] Mỗi mục hồ sơ và mỗi dòng khắc phục / rủi ro có người phụ trách là một vai trò.
- [ ] Hồ sơ đủ 7 mục, dòng cuối là Go / Go có điều kiện / No-go.

## 8. Checklist nộp bài (Trân chịu trách nhiệm cuối)

| Việc | Người làm |
| --- | --- |
| `TEAM.md` đủ thông tin nhóm, thành viên, vai, đóng góp | Trân |
| 4 báo cáo cá nhân `report/team/MSSV_HoTen.md` (họ tên không dấu, ví dụ `20241234_NguyenVanAn.md`), có mục công cụ AI đã dùng và cách tự kiểm tra | Mỗi người |
| `src/lab13.py` chạy được trên máy khác; đã xoá `src/nhap_pilot.py` | Trân chạy thử, Ngọc xoá file nháp |
| Đủ 6 file hồ sơ đúng tên trong `report/team/`: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md` | Người giữ từng file |
| `group_report.md` | Trân |
| Push lên GitHub, repo mở được cho người chấm | Trân |
| **Nộp link repo trên LMS trước 23h59 GMT+7** | **Cả 4 người, mỗi người tự nộp** |

Ghi vai thật vào `TEAM.md`: Đức "người viết code (A, B)", Ngọc "người viết code (D)", Đăng "người gắn nhãn 1", Trân "người gắn nhãn 2 kiêm giữ hồ sơ". Cách chia này không theo đúng gợi ý "đổi người viết code sau giải lao" trong `TEAM.md`, nhưng rubric không chấm vai, và vẫn có hai người tự viết code.

Sửa sau deadline thì tạo commit mới và ghi rõ thay đổi, không sửa lịch sử commit.
