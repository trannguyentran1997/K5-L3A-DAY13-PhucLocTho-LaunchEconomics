"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng
KHOI_LUONG_THANG = 45_000     # yêu cầu / tháng (quy mô đầy đủ)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs_loc = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:  # dùng cho B1, B3
        runs_loc = runs_loc[runs_loc['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs_loc['tokens_in'] / 1000 * gia_vao + runs_loc['tokens_out'] / 1000 * gia_ra
    tien_tool = runs_loc['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    chay_lai = (tien_token + tien_tool)[runs_loc['attempt'] > 1].sum()
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=int(thanh_cong),
        cps=tong / thanh_cong,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu và kiểm tra an toàn pilot ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm để so sánh hai tỉ lệ độc lập (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (
        za * math.sqrt(2 * pb * (1 - pb))
        + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def phan_tich_pilot_d(
    reqs,
    p1=0.70,
    mde_muc_tieu=0.05,
    mde_chap_nhan=0.06,
    alpha=0.05,
    power=0.80,
    icc=0.02,
    tong_nhan_vien=40,
    tong_depot=12,
    yc_moi_ngay=1500,
):
    """Tính 5 câu D1 (a-e), power ở mức 5 điểm khi n=859, và tỉ lệ mở lại 7 ngày."""
    p2_muc_tieu = p1 + mde_muc_tieu
    p2_chap_nhan = p1 + mde_chap_nhan

    # Câu a: chia theo từng yêu cầu
    n_a = co_mau(p1, p2_muc_tieu, alpha=alpha, power=power)
    h_5 = proportion_effectsize(p2_muc_tieu, p1)
    n_a_sm = math.ceil(
        NormalIndPower().solve_power(
            effect_size=abs(h_5), power=power, alpha=alpha, ratio=1.0
        )
    )

    # Câu b: chia theo nhân viên, m = 75
    m_b = 75
    de_b = 1 + (m_b - 1) * icc
    n_b = math.ceil(n_a * de_b)
    so_nv_moi_nhom_b = math.ceil(n_b / m_b)
    tong_nv_can_b = so_nv_moi_nhom_b * 2

    # Câu c: chia theo nhân viên, 20 nhân viên mỗi nhóm (c = 20)
    c_nv = tong_nhan_vien // 2
    n_eff_max_nv = c_nv / icc

    # Câu d: chia theo depot, 6 depot mỗi nhóm (c = 6)
    c_depot = tong_depot // 2
    n_eff_max_depot = c_depot / icc

    # Câu e: chấp nhận mức chênh 6 điểm, chia 20 nhân viên mỗi nhóm
    n_e = co_mau(p1, p2_chap_nhan, alpha=alpha, power=power)
    m_e_exact = (n_e * (1 - icc)) / (c_nv - n_e * icc)
    m_e = math.ceil(m_e_exact)
    de_e = 1 + (m_e - 1) * icc
    n_eff_e = (c_nv * m_e) / de_e

    # Power thực tế khi chỉ có n_eff = 859 mỗi nhóm nhưng tác động thật chỉ là 5 điểm
    power_o_5_diem = NormalIndPower().power(
        effect_size=abs(h_5), nobs1=n_e, alpha=alpha, ratio=1.0
    )

    # Tỉ lệ mở lại trong 7 ngày hiện tại (toàn mẫu và phạm vi pilot)
    mo_lai_toan_mau = reqs['mo_lai_trong_7_ngay'].mean()
    so_mo_lai_toan_mau = int(reqs['mo_lai_trong_7_ngay'].sum())

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai_pham_vi = pham_vi['mo_lai_trong_7_ngay'].mean()
    so_mo_lai_pham_vi = int(pham_vi['mo_lai_trong_7_ngay'].sum())

    # Ước tính thời gian chạy bước 0.50 để đạt m_e yêu cầu mỗi nhân viên
    ti_trong_pham_vi = len(pham_vi) / len(reqs)
    yc_pham_vi_moi_nv_ngay = (yc_moi_ngay * ti_trong_pham_vi) / tong_nhan_vien
    so_ngay_dat_m_e = m_e / yc_pham_vi_moi_nv_ngay

    print('\n=== D1 · Cỡ mẫu và chỉ số an toàn pilot ===')
    print(f'a) Chia theo yêu cầu (MDE +5 điểm): {n_a:,} yêu cầu/nhóm '
          f'(statsmodels NormalIndPower: {n_a_sm:,})')
    print(f'b) Chia theo nhân viên (m = {m_b}): DE = {de_b:.2f}; '
          f'n = {n_b:,} yêu cầu/nhóm -> {so_nv_moi_nhom_b} NV/nhóm '
          f'(tổng {tong_nv_can_b} > {tong_nhan_vien}: KHÔNG ĐỦ NGƯỜI)')
    print(f'c) Chia theo nhân viên ({c_nv} NV/nhóm): '
          f'n_hiệu_dụng tối đa = {n_eff_max_nv:,.0f} < {n_a:,} (KHÔNG ĐẠT)')
    print(f'd) Chia theo depot ({c_depot} depot/nhóm): '
          f'n_hiệu_dụng tối đa = {n_eff_max_depot:,.0f} < {n_a:,} '
          f'(KHÔNG ĐẠT và < 20 cụm/nhóm)')
    print(f'e) Mức chênh +6 điểm (n = {n_e:,}/nhóm), {c_nv} NV/nhóm: '
          f'm >= {m_e} yêu cầu/NV (chính xác {m_e_exact:.2f}, '
          f'DE = {de_e:.2f}, n_hiệu_dụng = {n_eff_e:.2f})')
    print(f'   -> Đánh đổi: nếu tác động thật chỉ +5 điểm với n = {n_e:,}/nhóm, '
          f'power chỉ còn {power_o_5_diem:.4f} (~{power_o_5_diem * 100:.1f}%)')
    print(f'   -> Ước tính thời gian ở bước 0.50 (phạm vi noi_dia + hang_nang '
          f'chiếm {ti_trong_pham_vi * 100:.2f}%, ~{yc_pham_vi_moi_nv_ngay:.1f} yc/NV/ngày): '
          f'cần ~{so_ngay_dat_m_e:.1f} ngày (~2 tuần)')
    print(f'Tỉ lệ mo_lai_trong_7_ngay toàn mẫu: '
          f'{mo_lai_toan_mau * 100:.2f}% ({so_mo_lai_toan_mau}/{len(reqs)})')
    print(f'Tỉ lệ mo_lai_trong_7_ngay phạm vi noi_dia + hang_nang: '
          f'{mo_lai_pham_vi * 100:.2f}% ({so_mo_lai_pham_vi}/{len(pham_vi)})')

    return {
        'n_a': n_a,
        'n_a_sm': n_a_sm,
        'de_b': de_b,
        'n_b': n_b,
        'so_nv_moi_nhom_b': so_nv_moi_nhom_b,
        'n_eff_max_nv': n_eff_max_nv,
        'n_eff_max_depot': n_eff_max_depot,
        'n_e': n_e,
        'm_e': m_e,
        'de_e': de_e,
        'power_o_5_diem': power_o_5_diem,
        'mo_lai_toan_mau': mo_lai_toan_mau,
        'mo_lai_pham_vi': mo_lai_pham_vi,
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ---- A1 ----
    kiem_tra_dap_an_biet_truoc()

    # ---- A2 · Mô hình chi phí từ trace ----
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:20s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:20s} {gia_tri:>14,.0f}')
    khong_tc_a2 = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc_a2 * BASELINE) / len(reqs)
    print(f'\nChi phí/việc thành công gấp {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} lần hoá đơn/yêu cầu [simulated]')
    print(f'Làm lại chiếm {ket_qua["lam_lai"] / ket_qua["tong"] * 100:.1f}% tổng chi phí [simulated]')
    print(f'Xem lại chiếm {ket_qua["xem_lai"] / ket_qua["tong"] * 100:.1f}% tổng chi phí [simulated]')
    print(f'Chi phí cả hệ thống/yêu cầu: {he_thong_moi_yc:,.0f} đ = {he_thong_moi_yc / BASELINE:.2f}× của 12.000 đ [simulated]')

    # ---- A3 · Tách theo loại yêu cầu ----
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'{"Loại":<12} {"Số YC":>7} {"Tỉ lệ TC":>10} {"Lần chạy/YC":>13} {"CPS (đ) [sim]":>15} {"So 12.000đ":>12}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        n_yc = len(sub)
        runs_sub = runs[runs['request_id'].isin(sub['request_id'])]
        lc_moi_yc = len(runs_sub) / n_yc
        print(f'{loai:<12} {n_yc:>7} {r["thanh_cong"] / n_yc:>10.1%} {lc_moi_yc:>13.2f} {r["cps"]:>15,.0f} {r["cps"] / BASELINE:>12.2f}×')

    print('\nTỉ lệ status == ok theo từng lần thử và loại yêu cầu:')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    piv_ok = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    piv_ok = piv_ok.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'])
    for loai, row in piv_ok.iterrows():
        cols = '  '.join(f'Lần {int(att)}: {val:.1%}' for att, val in row.items() if pd.notna(val))
        print(f'  {loai:<10} {cols}')

    # ---- A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----
    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pilot = mo_hinh(runs, sub_pilot)
    n_pilot_tc = r_pilot['thanh_cong']
    # Tỉ lệ việc thành công trong phạm vi trên toàn bộ mẫu (900 / 1.200)
    tc_month_full = int(round(KHOI_LUONG_THANG * n_pilot_tc / len(reqs)))
    co_dinh_full = CHI_PHI_CO_DINH / tc_month_full
    cps_full = r_pilot['cps'] + co_dinh_full
    tc_month_half = int(round((KHOI_LUONG_THANG / 2) * n_pilot_tc / len(reqs)))
    co_dinh_half = CHI_PHI_CO_DINH / tc_month_half
    cps_half = r_pilot['cps'] + co_dinh_half
    print(f'  Phạm vi pilot: {len(sub_pilot)} YC, {n_pilot_tc} thành công, CPS chưa cố định = {r_pilot["cps"]:,.0f} đ [simulated]')
    print(f'  45.000 YC/tháng: {tc_month_full:,} việc/tháng, cố định = {co_dinh_full:,.0f} đ/việc, '
          f'CPS + cố định = {cps_full:,.0f} đ = {cps_full / BASELINE:.2f}× [simulated]')
    print(f'  Một nửa khối lượng: {tc_month_half:,} việc/tháng, cố định = {co_dinh_half:,.0f} đ/việc, '
          f'CPS + cố định = {cps_half:,.0f} đ = {cps_half / BASELINE:.2f}× [simulated]')

    # ---- B1 · Bảng độ nhạy ----
    print('\n=== B1 · Bảng độ nhạy ===')
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'  {"Kịch bản":<32} {"CPS (đ) [sim]":>14} {"Thay đổi":>10}')
    print(f'  {"Gốc (A2)":<32} {goc:>14,.0f} {"":>10}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'  {ten:<32} {cps:>14,.0f} {(cps / goc - 1) * 100:>+9.1f}%')

    # ---- B2 · Đổi một cặp và xếp hạng ----
    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'  Giá token gấp đôi + tỉ lệ xem lại gấp đôi: {b2:,.0f} đ ({(b2 / goc - 1) * 100:+.1f}%) [simulated]')
    print('  Xếp hạng ba yếu tố: 1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên')

    # ---- B3 · Giới hạn chạy lại có thật sự rẻ hơn ----
    print('\n=== B3 · Giới hạn chạy lại có thật sự rẻ hơn ===')
    print(f'  {"Giới hạn":<10} {"Tổng trợ lý [sim]":>18} {"Không TC":>10} {"Cả hệ thống [sim]":>18} {"CPS [sim]":>12}')
    for lim in [1, 2, 3]:
        r_lim = mo_hinh(runs, reqs, max_lan_chay=lim)
        khong_tc = len(reqs) - r_lim['thanh_cong']
        he_thong = r_lim['tong'] + khong_tc * BASELINE
        print(f'  {lim} lần{"":<5} {r_lim["tong"]:>18,.0f} {khong_tc:>10} {he_thong:>18,.0f} {r_lim["cps"]:>12,.0f}')

    # ---- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ----
    print('\n=== B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ===')
    sub_b4 = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_b4 = runs[runs['request_id'].isin(sub_b4['request_id'])]
    n_has_ok = runs_b4.loc[runs_b4['status'] == 'ok', 'request_id'].nunique()
    n_lam_lai_b4 = int((sub_b4['ket_qua'] == 'lam_lai').sum())
    tc_b4 = int((sub_b4['ket_qua'] == 'thanh_cong').sum())
    tien_token_tool_b4 = (
        runs_b4['tokens_in'] / 1000 * GIA_VAO
        + runs_b4['tokens_out'] / 1000 * GIA_RA
        + runs_b4['tool_calls'] * GIA_TOOL
    ).sum()

    # Mức 9 phút/ca làm lại (giả định đề bài)
    xem_lai_b4 = n_has_ok * 5 * LUONG_PHUT
    lam_lai_b4_9 = n_lam_lai_b4 * 9 * LUONG_PHUT
    tong_b4_9 = tien_token_tool_b4 + xem_lai_b4 + lam_lai_b4_9
    cps_b4_9 = tong_b4_9 / tc_b4
    hoa_von_9 = (BASELINE * tc_b4 - tien_token_tool_b4 - lam_lai_b4_9) / (n_has_ok * LUONG_PHUT)

    # Mức trung bình thực tế trong dữ liệu (~15,3 phút/ca trên toàn bộ ca lam_lai)
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    lam_lai_b4_tb = n_lam_lai_b4 * phut_lam_lai_tb * LUONG_PHUT
    tong_b4_tb = tien_token_tool_b4 + xem_lai_b4 + lam_lai_b4_tb
    cps_b4_tb = tong_b4_tb / tc_b4
    hoa_von_tb = (BASELINE * tc_b4 - tien_token_tool_b4 - lam_lai_b4_tb) / (n_has_ok * LUONG_PHUT)

    print(f'  Phạm vi noi_dia + hang_nang: {len(sub_b4)} YC, {n_has_ok} YC có status=ok, {n_lam_lai_b4} ca làm lại, {tc_b4} thành công')
    print(f'  Token + tool: {tien_token_tool_b4:,.0f} đ')
    print(f'  Làm lại 9 phút/ca: tổng = {tong_b4_9:,.0f} đ → CPS = {cps_b4_9:,.0f} đ = {cps_b4_9 / BASELINE:.2f}× [simulated] (hoà vốn ≤ {hoa_von_9:.1f} phút xem lại)')
    print(f'  Làm lại {phut_lam_lai_tb:.1f} phút/ca: tổng = {tong_b4_tb:,.0f} đ → CPS = {cps_b4_tb:,.0f} đ = {cps_b4_tb / BASELINE:.2f}× [simulated] (hoà vốn ≤ {hoa_von_tb:.1f} phút xem lại)')

    # ---- D1 · Cỡ mẫu và kiểm tra an toàn pilot ----
    phan_tich_pilot_d(reqs)
