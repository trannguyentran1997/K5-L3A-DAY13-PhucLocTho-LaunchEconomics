# Phân công nhóm PhucLocTho · Lab 13 Launch Economics

Nhóm 4 người: **Trân (trưởng nhóm)**, **Đức**, **Ngọc**, **Đăng**. File này nói ai làm gì, lúc nào, giữ file nào. Đề bài gốc vẫn là [README.md](README.md), [CHECKPOINTS.md](CHECKPOINTS.md), [RUBRIC.md](RUBRIC.md), [SUBMISSION.md](SUBMISSION.md); cách làm từng bước và số tự đối chiếu nằm trong [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## 1. Cần nộp gì

Một bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN, trả lời 4 câu: có đáng chạy không (A, B), khi hỏng thì sao (C), pilot thiết kế thế nào (D), nhân viên có dùng không + đề xuất cuối (E). Sau đó bảo vệ trước hội đồng Gate 2a và chấm một nhóm khác.

| Mốc | Việc |
| --- | --- |
| 17:00 | `report/team/ho_so_launch_v0.md` đủ 7 mục, gửi nhóm hội đồng |
| 17:45–18:00 | Commit, push bản làm tại lớp |
| 23h59 GMT+7 ngày lab | Hạn nộp. **Mỗi người tự nộp link repo nhóm trên LMS**, ai không nộp thì không có điểm |

Điểm: 70 đối chiếu đáp án (A 20 · B 15 · C 10 · D 15 · E 10) + 30 hội đồng chấm. Số được nhận nếu lệch không quá 2%.

## 2. Phân vai

Lab có 4 vai cố định, và bắt buộc **đổi người viết code sau giờ giải lao** (15:35). Hai người gắn nhãn ở CP3 phải là hai người không giữ code, vì lúc họ gắn nhãn thì hai người kia đang hoàn thiện CP2.

| Thành viên | Vai trước giải lao (CP1–CP2) | Vai sau giải lao (CP3–CP5) | File giữ (chỉ người này sửa) |
| --- | --- | --- | --- |
| **Trân** (trưởng nhóm) | Người gắn nhãn 2, kiêm giữ hồ sơ | Người gắn nhãn 2, kiêm giữ hồ sơ; trình bày ở Gate 2a | `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md` |
| **Đức** | **Người viết code** (A, B) | Người kiểm số (D) | `src/lab13.py` tới 15:20 · `report/team/pilot_plan.yaml` |
| **Ngọc** | Người kiểm số (A, B) | **Người viết code** (D1, E1) | `report/team/bang_chi_phi.md` · `src/lab13.py` từ 15:35 |
| **Đăng** | Người gắn nhãn 1, theo dõi điều kiện "Xong khi" | Người gắn nhãn 1; giữ bảng lỗi, chỉ số và phiếu chấm | `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/phieu_cham.md` |

Mỗi người tự tạo báo cáo cá nhân `report/team/MSSV_HoTen.md` (copy từ file mẫu, **không sửa file mẫu**).

> Cột "Người phụ trách" trong các bảng hồ sơ ghi **một vai trò của LogiX-VN** (ví dụ "PM trợ lý hoàn phí", "Kỹ sư trưởng agent", "Trưởng nhóm CSKH", "Kế toán trưởng", "Giám đốc vận hành"), không ghi tên thành viên nhóm và không ghi "cả đội".

## 3. Lịch theo giờ

| Giờ | Trân | Đức | Ngọc | Đăng |
| --- | --- | --- | --- | --- |
| **14:00–14:10** Chuẩn bị | Mời 3 bạn vào repo; điền phần đầu `TEAM.md`; mở sẵn `ho_so_launch_v0.md` | Cài môi trường, chạy thử `python lab13.py` | Cài môi trường, mở `bang_chi_phi.md` | Cài môi trường, đọc lướt CHECKPOINTS, ghi các điều kiện "Xong khi" |
| **14:10–14:53** CP1 · A | Điền mục 1 và 3 của hồ sơ khi có số | Viết 3 hàm A1 → `mo_hinh` (A2) → tách theo `loai` (A3) → cộng cố định (A4) | Tính tay 1–2 con số để đối chiếu (ví dụ tiền token, số việc thành công 978); điền bảng A2, A3, A4 | Đối chiếu số in ra với số tự kiểm; nhắc nhãn `simulated`; đọc trước 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (chưa gắn nhãn) |
| **14:53–15:20** CP2 · B | Điền mục 2 của hồ sơ (3 yếu tố nhạy nhất) | Viết 9 kịch bản B1, cặp B2, giới hạn chạy B3, xem lại 100% B4 | Kiểm tra "giảm một nửa = nửa mức gấp đôi"; điền B1–B4 vào `bang_chi_phi.md` | Nháp sẵn khung `chi_so.md` (bảng event) |
| **15:20** | Giải lao | **Commit + push `lab13.py` trước khi nghỉ** | | |
| **15:35–15:43** CP3 · C gắn nhãn | **Gắn nhãn độc lập 20 ca**, ngồi riêng, không trao đổi | Cùng Ngọc chốt nốt B3, B4 nếu chưa xong | Pull `lab13.py`, nhận vai viết code | **Gắn nhãn độc lập 20 ca**, ngồi riêng, không trao đổi |
| **15:43–16:08** CP3 · C so nhãn | Gửi bộ nhãn cho Đăng; cùng thống nhất ca lệch; điền mục 5 hồ sơ | Tính tay trước câu D1-e (giải m ≥ 299) | Bắt đầu viết code D1 (cỡ mẫu) | Nhập 2 bộ nhãn vào `bang_loi.md`, tính tỉ lệ đồng thuận, ghi quy tắc cho ca lệch, điền bảng khắc phục 5 ca |
| **16:08–16:36** CP4 · D | Điền mục 6 hồ sơ | Điền `pilot_plan.yaml`: phần chú thích D1, D2, các trường, 3 luật dừng; chạy 2 lệnh tự kiểm | Code D1 (5 câu) + tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại, gửi số cho Đức | Soát luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ |
| **16:36–17:00** CP5 · E | Chốt hồ sơ đủ 7 mục + đề xuất cuối | Soát toàn bộ hồ sơ: nhãn `simulated`, từ cấm, người phụ trách | Code tính 3 chỉ số E1, gửi số cho Đăng | Điền `chi_so.md`: 3 chỉ số + 2 chỉ số tự đề xuất, ≥ 6 event có `trace_id`, ≥ 2 dòng rủi ro kinh tế |
| **17:00–17:45** Gate 2a | Gửi hồ sơ; trình bày 1 phút; trả lời câu hỏi | Đối chiếu số của nhóm được chấm với đáp án | Đối chiếu số của nhóm được chấm; chuẩn bị câu trả lời cho câu hỏi về cỡ mẫu | Đọc hồ sơ nhóm n + 1, viết `phieu_cham.md` (điểm, lý do có số, 1 câu hỏi) |
| **17:45–18:00** Đóng gói | Điền `group_report.md`, `TEAM.md` (đóng góp); push cuối | Chạy `python lab13.py` trên máy mình sau khi pull (kiểm "chạy được trên máy khác") | Viết báo cáo cá nhân, push | Viết báo cáo cá nhân, push |

Giờ ở trên theo lịch lớp 14:00–18:00. Nếu lớp học giờ khác thì giữ nguyên thứ tự và thời lượng.

## 4. Việc chi tiết từng người

### Trân · trưởng nhóm, người gắn nhãn 2, giữ hồ sơ

- [ ] Trước buổi: vào Settings → Collaborators của repo, mời Đức, Ngọc, Đăng (repo đã đúng tên `K5-L3A-DAY13-PhucLocTho-LaunchEconomics`). Kiểm tra repo public hoặc đã mời giảng viên.
- [ ] `TEAM.md`: tên nhóm, lớp, URL repo, bảng thành viên (họ tên, MSSV, email, GitHub, vai), cuối buổi ghi đóng góp từng người và commit chốt.
- [ ] `ho_so_launch_v0.md`: điền dần **từ đầu buổi**, không đợi 16:36. Mỗi mục có con số chính, trạng thái (**Xong, có bằng chứng · Chưa · Giả lập**; mục 1, 2, 3, 7 ghi Giả lập), người phụ trách là một vai trò.
- [ ] Dòng cuối hồ sơ: một trong ba **Go · Go có điều kiện · No-go**. Go có điều kiện thì mỗi điều kiện có người phụ trách và ngày kiểm tra. Nêu cả con số bất lợi (ví dụ xem lại 100% thì không tiết kiệm, power chỉ khoảng 0,64 nếu tác động thật là 5 điểm) kèm cách xử lý: đây là phần hội đồng chấm 10 điểm.
- [ ] CP3: gắn nhãn 20 ca **một mình, trước khi xem bảng nhãn tham khảo**. Ghi ra giấy hoặc file nháp rồi mới gửi Đăng.
- [ ] `group_report.md`: tóm tắt A–E, con số chính, kết quả hội đồng nhóm mình nhận được, khó khăn (nếu lỗi cài đặt thì kèm lệnh và output).
- [ ] Push cuối và chạy checklist ở mục 7.

### Đức · viết code trước giải lao, kiểm số sau giải lao

- [ ] CP1: trong `src/lab13.py`, viết 3 hàm A1 ở dòng `TODO CP1`. **Chưa đạt cả ba (1,20 · 1,25 · 1,25) thì không làm tiếp.**
- [ ] Viết `mo_hinh(runs, reqs, …)` cho A2: tử số tính **mọi** lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Đọc CSV yêu cầu bằng `keep_default_na=False`. Số tự đối chiếu: chi phí mỗi việc thành công khoảng 4.472 đ [simulated], 978 việc thành công, gấp khoảng 16,3 lần hoá đơn chia số yêu cầu.
- [ ] A3: gọi lại `mo_hinh` cho 4 loại; tính thêm tỉ lệ ok theo từng lần thử để trả lời "chạy lại có giúp không". A4: cộng cố định 40 triệu/tháng cho phạm vi `noi_dia` + `hang_nang`.
- [ ] CP2 (`TODO CP2`): 9 kịch bản B1, cặp B2, giới hạn 1/2/3 lần chạy với chi phí cả hệ thống B3, xem lại 100% B4.
- [ ] **15:20 commit + push `lab13.py`**, từ 15:35 không sửa file này nữa (Ngọc giữ).
- [ ] Sau giải lao: tính tay câu D1-e để đối chiếu với code của Ngọc. Giữ `pilot_plan.yaml`: điền chú thích D1, D2, đánh đổi đã chấp nhận, mọi trường, ≥ 3 luật dừng (an toàn, chi phí, mức độ sử dụng). Ngưỡng an toàn đặt sau khi xem tỉ lệ mở lại hiện tại (khoảng 4,25%), đừng đặt thấp hơn mức đang có.
- [ ] Chạy 2 lệnh tự kiểm trong `src/`:
  ```bash
  python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"
  grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'    # không được in gì
  ```
- [ ] 16:36: soát toàn bộ `report/team/` trước khi gửi hội đồng (xem mục 6).

### Ngọc · kiểm số trước giải lao, viết code sau giải lao

- [ ] CP1: tự tính tay (hoặc Excel) ít nhất một con số trong A2 để đối chiếu với code của Đức, ghi cách tính vào `bang_chi_phi.md`.
- [ ] Giữ `bang_chi_phi.md`: bảng A2 đủ 9 dòng (hai dòng xem lại, làm lại có nhãn `simulated`), A3 đủ 4 dòng, A4, B1 đủ 9 dòng, xếp hạng 3 yếu tố, câu trả lời B3 và B4 (mỗi câu ≤ 3 dòng, có số; B4 ghi cả hai mức 9 phút và 15,3 phút).
- [ ] CP2: tự kiểm "giảm một nửa làm chi phí giảm đúng nửa mức tăng của gấp đôi".
- [ ] 15:35: `git pull`, nhận `lab13.py`. Viết code D1 ở dòng `TODO CP4`: 5 câu cỡ mẫu (theo yêu cầu, nhân viên m = 75, 20 nhân viên mỗi nhóm, 6 depot mỗi nhóm, mức chênh 6 điểm). Tính `reqs.mo_lai_trong_7_ngay.mean()` (toàn mẫu và trong phạm vi `noi_dia` + `hang_nang`) và gửi Đức.
- [ ] CP5: thêm code tính 3 chỉ số E1 (chính, dùng, an toàn), gửi số cho Đăng.
- [ ] `lab13.py` phải chạy từ đầu đến cuối không lỗi, in đủ A1, A2, A3, B, D1. Push trước 17:00.

### Đăng · người gắn nhãn 1, giữ bảng lỗi, chỉ số, phiếu chấm

- [ ] Suốt buổi: theo dõi điều kiện "Xong khi" của từng CP, báo nhóm khi còn thiếu.
- [ ] CP3: gắn nhãn 20 ca **một mình, trước khi xem bảng nhãn tham khảo**, theo 5 loại Google PAIR (Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm). Gắn theo nguyên nhân gốc, không theo chỗ cần sửa.
- [ ] Giữ `bang_loi.md`: nhập cả hai bộ nhãn **đúng như lúc gắn độc lập, không sửa sau khi đã so**; tỉ lệ đồng thuận = số ca trùng ÷ 20 (cần ≥ 16/20, thấp hơn thì viết lại định nghĩa trước khi đi tiếp); một câu quy tắc cho mỗi ca lệch; bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách.
- [ ] Giữ `chi_so.md`: 3 chỉ số tính thử (số từ Ngọc), 1 chỉ số dùng + 1 chỉ số an toàn tự đề xuất, ≥ 6 event mỗi event có `trace_id`, kiểm tra chéo chỉ số nào dùng event nào, ≥ 2 dòng rủi ro kinh tế lấy số từ bảng độ nhạy. Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số".
- [ ] Gate 2a: giữ `phieu_cham.md`, chấm nhóm n + 1 theo 3 tiêu chí, mỗi điểm có lý do bằng số, kèm quyết định và một câu hỏi; ghi lại câu trả lời của đội trình.

## 5. Quy ước làm chung

**Git.** Mỗi người clone repo nhóm (không làm trên repo đề bài):

```bash
git clone https://github.com/trannguyentran1997/K5-L3A-DAY13-PhucLocTho-LaunchEconomics.git
cd K5-L3A-DAY13-PhucLocTho-LaunchEconomics/src
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1   ·   macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
```

- Chỉ sửa file mình giữ (bảng ở mục 2). Cần đổi file người khác thì nhắn người đó sửa, để không xung đột.
- Trước mỗi lần push: `git pull --rebase`, rồi `git add <file của mình>` (không dùng `git add .`), commit, push.
- Không force-push, không xoá commit, không commit `.venv/` hay `.env`. Không sửa hai file CSV.

**Số liệu.**

- Mọi con số phải do `src/lab13.py` tính ra, hoặc tính tay có ghi cách tính. Không dùng AI để bịa số, nhãn lỗi hay kết quả chấm.
- Số lấy từ cột `phut_xem_lai_simulated`, `phut_lam_lai_simulated` (và mọi số tính từ chúng) luôn có nhãn `simulated`.
- Khi giảng viên chiếu slide chữa: Ngọc (trước giải lao) hoặc Đức (sau giải lao) đối chiếu ngay, lệch quá 2% thì báo người viết code sửa trước khi sang nhiệm vụ sau.
- Mỗi câu trả lời không quá 3 dòng, có ít nhất 1 con số.
- Không dùng từ tiếng Anh bị cấm ở quy tắc 5 trong `README.md` (Gate 2a chỉ duyệt kế hoạch pilot).

**Gắn nhãn độc lập (C).** Trân và Đăng không xem bảng "Nhãn tham khảo" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và không trao đổi trước khi cả hai gắn xong. Đây là quy định liêm chính trong `RULES.md`.

**Cả nhóm phải tự giải thích được** (hội đồng và giảng viên có thể hỏi bất kỳ ai):

1. Vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công.
2. Cách tính cỡ mẫu hiệu dụng khi chia theo cụm, vì sao số cụm quyết định chứ không phải tổng số yêu cầu.
3. Lý do của đề xuất cuối, kể cả con số bất lợi.

## 6. Soát trước khi gửi hội đồng (16:55, Đức làm, Trân xác nhận)

Chạy trong `src/`:

```bash
python lab13.py                                   # chạy hết, ba phép thử in ĐẠT
grep -rni production ../report/team               # không được in gì
grep -rn "\.\.\." ../report/team/*.md             # còn chỗ "..." chưa điền thì điền nốt
```

- [ ] Mọi số giả lập có nhãn `simulated`.
- [ ] Mỗi mục hồ sơ và mỗi dòng khắc phục / rủi ro có người phụ trách là một vai trò.
- [ ] Hồ sơ đủ 7 mục, dòng cuối là Go / Go có điều kiện / No-go.

## 7. Checklist nộp bài (Trân chịu trách nhiệm cuối)

| Việc | Người làm |
| --- | --- |
| `TEAM.md` đủ thông tin nhóm, thành viên, vai, đóng góp | Trân |
| 4 báo cáo cá nhân `report/team/MSSV_HoTen.md` (họ tên không dấu, ví dụ `20241234_NguyenVanAn.md`), có mục công cụ AI đã dùng và cách tự kiểm tra | Mỗi người |
| `src/lab13.py` chạy được trên một máy khác trong nhóm | Đức chạy trên máy mình |
| Đủ 6 file hồ sơ đúng tên trong `report/team/`: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md` | Người giữ từng file |
| `group_report.md` | Trân |
| `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?`, ≥ 3 luật dừng đủ 4 vế | Đức |
| Push lên GitHub, repo mở được cho người chấm | Trân |
| **Nộp link repo trên LMS trước 23h59 GMT+7** | **Cả 4 người, mỗi người tự nộp** |

Sửa sau deadline thì tạo commit mới và ghi rõ thay đổi, không sửa lịch sử commit.
