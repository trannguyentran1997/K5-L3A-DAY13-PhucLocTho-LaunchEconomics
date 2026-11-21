# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: PhucLocTho
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN, trả lời 4 câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Nhóm chia việc theo phần riêng để không ai phải chờ ai: Đức làm A + B, Ngọc làm D, Đăng làm C + E1/E2, Trân gắn nhãn thứ hai và tổng hợp hồ sơ ([PHAN_CONG_NHOM.md](../../PHAN_CONG_NHOM.md)). Mỗi người làm trên nhánh riêng; trưởng nhóm gộp vào `main`, chạy lại toàn bộ `src/lab13.py` và review từng phần trước khi viết hồ sơ.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): hàm `mo_hinh` cộng token và tool của mọi lần chạy, kể cả lần lỗi, cộng phút xem lại và làm lại [simulated], chia cho số việc thành công. Tách theo 4 loại yêu cầu, cộng chi phí cố định cho phạm vi pilot.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần chạy theo chi phí cả hệ thống, và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): gắn nhãn 20 ca theo 5 loại Google PAIR (đồng thuận 20/20 = 100%); bảng khắc phục 5 ca (14, 20, 16, 19, 5), mỗi dòng có event, ngưỡng và một vai trò.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho 3 cách chia trước khi chọn; chọn chia theo nhân viên 20 + 20, chấp nhận MDE +6 điểm; 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử, 2 chỉ số tự đề xuất, 12 event có `trace_id`, 4 dòng rủi ro kinh tế; hồ sơ 7 mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ**, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu [simulated]; giờ nhân viên chiếm 92,5%.
- So với nhân viên tự làm: cả hệ thống **0,49×** của 12.000 đ; phạm vi `noi_dia` + `hang_nang` đã cộng cố định **0,38×** [simulated]. `quoc_te` 1,88× nên loại.
- Yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated].
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Pilot: 20 + 20 nhân viên, n = 859/nhóm, m ≥ 299; power chỉ 0,64 nếu tác động thật là +5 điểm.
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, với 4 điều kiện có người phụ trách và ngày kiểm tra (xem hồ sơ).
- Nhóm mình chấm nhóm TENGICUNGDUOC: 25/30 (C6 10, C7 5 vì dòng `scope` thiếu nhãn simulated cho 2 số, C8 10), quyết định Go có điều kiện, 1 câu hỏi về luật dừng chi phí ([phieu_cham_TENGICUNGDUOC.md](phieu_cham_TENGICUNGDUOC.md)).
- Kết quả duyệt chéo Gate 2a nhóm nhận được: chờ phiếu của nhóm hội đồng.

## 5. Khó khăn và cách xử lý

- **Lỗi mã hoá tiếng Việt:** commit đầu của Đức (`80048f4`) bị đổi toàn bộ chữ có dấu thành ký tự rác khi thao tác nhánh trên PowerShell. Đức sửa ở `e383534`.
- **A4 chia nhầm mẫu số:** bản đầu chia số việc thành công cho 982 yêu cầu trong phạm vi thay vì 1.200 yêu cầu của mẫu; Đức phát hiện khi đối chiếu đáp án và sửa.
- **Xung đột khi gộp `src/lab13.py`:** nhánh của Ngọc đã gộp bản lỗi mã hoá của Đức, còn bản sửa của Đức đến sau. Git tự gộp phần lớn; xung đột duy nhất ở cuối khối main, giữ lời gọi phần D của Ngọc.
- **Review phát hiện 2 vấn đề ở nhiệm vụ C:** bảng khắc phục bản đầu trùng gần nguyên văn bài làm mẫu, nên đã viết lại bằng 5 ca khác. Cột nhãn người 2 bản đầu được điền khi Trân chưa gắn nhãn, nên đã gỡ; sau đó Trân hoàn thành gắn nhãn 20 ca và cập nhật lại `bang_loi.md` (đồng thuận 20/20 = 100%).
- **Môi trường:** máy trưởng nhóm thiếu `statsmodels`, phải tạo `src/.venv` theo `src/README.md` (lệnh `python -m venv .venv` rồi `pip install -r requirements.txt`) mới chạy được phần D. Mạng tới github.com chập chờn, một số lần push phải chạy lại.
- **Luật dừng dễ báo nhầm:** trước Gate 2a nhóm thấy 2 luật trong `pilot_plan.yaml` sẽ kích hoạt dù trợ lý chạy đúng như đợt thử: chênh 2 điểm so với đối chứng khi mới có 4 nhân viên (lệch ngẫu nhiên), và ngưỡng 8.000 đ nếu cộng 40 triệu cố định (khoảng 15.300 đ/việc ở bước 4 nhân viên). Đã sửa: chênh 2 điểm chỉ áp dụng từ bước 10 nhân viên, ngưỡng 8.000 đ chỉ tính token, tool và giờ người; báo "đã hoàn" mà sổ cái không ghi thì dừng ngay như hoàn trùng.

## 6. Tổng hợp đóng góp

Chi tiết từng việc, trạng thái và commit của mỗi thành viên nằm trong [TEAM.md](../../TEAM.md); bảng phân công ở [PHAN_CONG_NHOM.md](../../PHAN_CONG_NHOM.md).

| Người | Phần | Kết quả chính |
| --- | --- | --- |
| Trân | Tổng hợp, gắn nhãn 2, kiểm số A2, phiếu chấm | Gộp và review 3 nhánh; `kiem_so_A2.xlsx` khớp `lab13.py` (lệch lớn nhất 0,11%); nhãn 20/20; hồ sơ 7 mục; phiếu chấm TENGICUNGDUOC 25/30 |
| Đức | A + B | Qua 3 phép thử A1; 4.472 đ, gấp 16,3 lần [simulated]; B1–B4 khớp đáp án |
| Ngọc | D | Năm câu D1, power 0,64; `pilot_plan.yaml` chia 20 + 20 nhân viên |
| Đăng | C, E1, E2 | Bộ nhãn người 1; 3 chỉ số; 12 event có `trace_id`; 4 dòng rủi ro kinh tế |

Sửa khi review: A4 chia nhầm mẫu số (Đức tự sửa); số 12.415 đ và luật dừng trong `pilot_plan.yaml`; bảng khắc phục viết lại vì trùng bài mẫu; cột nhãn người 2 gỡ rồi nhập lại bằng nhãn thật của Trân. Về quy trình: Đức push một lần thay vì 2 mốc, Ngọc push 2 commit đầu thẳng lên `main`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; mọi kết luận chi phí phải tính lại bằng phút đo thật sau tuần 1 pilot.
- Đợt chạy thử không có đối chứng, nên 82,83% chưa nói được trợ lý làm chỉ số chính thay đổi bao nhiêu.
- Với 40 nhân viên, pilot chỉ đủ mẫu cho +6 điểm; nếu tác động thật là +5 điểm thì 36% khả năng bỏ sót.
- Chi phí cố định tính theo tỉ lệ thành công của mẫu 1.200 yêu cầu; khối lượng thật thấp hơn thì chi phí mỗi việc tăng.
- Bộ nhãn thứ hai ở nhiệm vụ C hoàn thành sát giờ Gate 2a; lần sau hai người gắn nhãn phải làm ngay đầu buổi (14:10) và lưu phiếu gốc ngay từ đầu.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
- Tài liệu của lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
