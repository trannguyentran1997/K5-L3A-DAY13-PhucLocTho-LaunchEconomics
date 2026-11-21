"""Lab 13 Â· Äá»‹nh giÃ¡ agent vÃ  láº­p káº¿ hoáº¡ch pilot (Gate 2a) â€” bÃ i lÃ m cá»§a nhÃ³m (file ná»™p).
Cháº¡y trong thÆ° má»¥c src/: python3 lab13.py   (cáº§n pandas; Nhiá»‡m vá»¥ D cáº§n thÃªm statsmodels)
KhÃ´ng cáº§n khoÃ¡ API. Äiá»n cÃ¡c chá»— ghi VIáº¾T á»ž ÄÃ‚Y (Ä‘Ã¡nh dáº¥u TODO CP1â€¦CP4). Dá»¯ liá»‡u trong hai file CSV lÃ  giáº£ láº­p.
Báº£n gá»‘c chÆ°a sá»­a náº±m á»Ÿ lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Báº£ng giÃ¡ GIáº¢ Äá»ŠNH cá»§a lab (khÃ´ng pháº£i giÃ¡ tháº­t cá»§a nhÃ  cung cáº¥p nÃ o)
GIA_VAO = 26        # Ä‘á»“ng cho 1.000 token Ä‘áº§u vÃ o
GIA_RA = 130        # Ä‘á»“ng cho 1.000 token Ä‘áº§u ra
GIA_TOOL = 15       # Ä‘á»“ng cho 1 láº§n gá»i tool
LUONG_PHUT = 2000   # Ä‘á»“ng cho 1 phÃºt cá»§a nhÃ¢n viÃªn (Ä‘Ã£ gá»“m báº£o hiá»ƒm, vÄƒn phÃ²ng)
BASELINE = 12000    # Ä‘á»“ng cho 1 yÃªu cáº§u khi nhÃ¢n viÃªn tá»± lÃ m (6 phÃºt)


# ---------- Nhiá»‡m vá»¥ A1 Â· Kinh táº¿ cá»§a viá»‡c cháº¡y láº¡i ----------
def so_lan_chay_ky_vong(p, k=None):
    """Sá»‘ láº§n cháº¡y trung bÃ¬nh cho 1 yÃªu cáº§u khi má»—i láº§n Ä‘Ãºng vá»›i xÃ¡c suáº¥t p.
    k = sá»‘ láº§n cháº¡y tá»‘i Ä‘a; k=None nghÄ©a lÃ  cháº¡y láº¡i Ä‘áº¿n khi Ä‘Ãºng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """XÃ¡c suáº¥t yÃªu cáº§u thÃ nh cÃ´ng sau tá»‘i Ä‘a k láº§n cháº¡y."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng, tÃ­nh báº±ng bá»™i sá»‘ cá»§a giÃ¡ má»™t láº§n cháº¡y."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phÃ©p thá»­ báº¯t buá»™c Ä‘áº¡t 100% trÆ°á»›c khi tÃ­nh trÃªn dá»¯ liá»‡u."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tá»‘i Ä‘a 2 láº§n â†’ 1,20 láº§n cháº¡y'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, cháº¡y Ä‘áº¿n khi Ä‘Ãºng â†’ 1,25 láº§n cháº¡y'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tá»‘i Ä‘a 3 láº§n â†’ 1,25 láº§n giÃ¡ má»™t láº§n cháº¡y'
    print('Ba phÃ©p thá»­ Ä‘Ã¡p Ã¡n biáº¿t trÆ°á»›c: Äáº T')


# ---------- Nhiá»‡m vá»¥ A2 Â· MÃ´ hÃ¬nh chi phÃ­ tá»« trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tráº£ vá» dict gá»“m: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng).
    - token, tool: cá»™ng trÃªn Má»ŒI láº§n cháº¡y trong runs, ká»ƒ cáº£ láº§n lá»—i.
    - xem_lai, lam_lai: sá»‘ phÃºt (cá»™t *_simulated) Ã— LUONG_PHUT. ÄÃ¢y lÃ  sá»‘ GIáº¢ Láº¬P, pháº£i ghi nhÃ£n simulated khi bÃ¡o cÃ¡o.
    - thanh_cong: sá»‘ yÃªu cáº§u cÃ³ ket_qua == 'thanh_cong'.
    - CÃ¡c tham sá»‘ giÃ¡/há»‡ sá»‘/max_lan_chay dÃ¹ng cho Nhiá»‡m vá»¥ B (Ä‘á»™ nháº¡y, giá»›i háº¡n sá»‘ láº§n cháº¡y); giá»¯ máº·c Ä‘á»‹nh á»Ÿ A2.
    """
    reqs = reqs.copy()
    runs2 = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:  # dÃ¹ng cho B1, B3
        runs2 = runs2[runs2['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs2['tokens_in'] / 1000 * gia_vao + runs2['tokens_out'] / 1000 * gia_ra
    tien_tool = runs2['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    chay_lai = (tien_token + tien_tool)[runs2['attempt'] > 1].sum()
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)

    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=chay_lai,
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=int(thanh_cong), cps=tong / thanh_cong,
                hoa_don_moi_yc=hoa_don_moi_yc)


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

    # ---- A2 ----
    print('\n=== A2 Â· MÃ´ hÃ¬nh chi phÃ­ tá»« trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:20s} {gia_tri:>14,.0f}')
    print(f'\nChi phÃ­/viá»‡c thÃ nh cÃ´ng gáº¥p {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} láº§n hoÃ¡ Ä‘Æ¡n/yÃªu cáº§u')
    print(f'LÃ m láº¡i chiáº¿m {ket_qua["lam_lai"] / ket_qua["tong"] * 100:.1f}% tá»•ng chi phÃ­ [simulated]')
    print(f'Xem láº¡i chiáº¿m {ket_qua["xem_lai"] / ket_qua["tong"] * 100:.1f}% tá»•ng chi phÃ­ [simulated]')

    # ---- A3 Â· TÃ¡ch theo loáº¡i yÃªu cáº§u ----
    print('\n=== A3 Â· TÃ¡ch theo loáº¡i yÃªu cáº§u ===')
    print(f'{"Loáº¡i":<12} {"Sá»‘ YC":>7} {"Tá»‰ lá»‡ TC":>10} {"Láº§n cháº¡y/YC":>13} {"CPS (Ä‘)":>12} {"So 12.000Ä‘":>12}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        n_yc = len(sub)
        runs_sub = runs[runs['request_id'].isin(sub['request_id'])]
        lc_moi_yc = len(runs_sub) / n_yc
        print(f'{loai:<12} {n_yc:>7} {r["thanh_cong"] / n_yc:>10.1%} {lc_moi_yc:>13.2f} {r["cps"]:>12,.0f} {r["cps"] / BASELINE:>12.2f}Ã—')

    # Tá»‰ lá»‡ ok theo láº§n thá»­ cho tá»«ng loáº¡i
    print('\nTá»‰ lá»‡ ok theo láº§n thá»­ (quoc_te):')
    sub_qte = reqs[reqs['loai'] == 'quoc_te']
    runs_qte = runs[runs['request_id'].isin(sub_qte['request_id'])]
    piv = runs_qte.groupby('attempt')['status'].apply(lambda x: (x == 'ok').mean())
    for att, rate in piv.items():
        print(f'  Láº§n {att}: {rate:.1%}')

    # ---- A4 Â· Chi phÃ­ cá»‘ Ä‘á»‹nh ----
    print('\n=== A4 Â· Chi phÃ­ cá»‘ Ä‘á»‹nh (pháº¡m vi noi_dia + hang_nang) ===')
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pilot = mo_hinh(runs, sub_pilot)
    n_pilot_yc = len(sub_pilot)
    n_pilot_tc = r_pilot['thanh_cong']
    # Quy mÃ´ Ä‘áº§y Ä‘á»§ 45.000 yÃªu cáº§u/thÃ¡ng
    tc_month_full = int(45000 * n_pilot_tc / n_pilot_yc)
    co_dinh = 40_000_000
    co_dinh_full = co_dinh / tc_month_full
    cps_full = r_pilot['cps'] + co_dinh_full
    # Ná»­a khá»‘i lÆ°á»£ng
    tc_month_half = tc_month_full // 2
    co_dinh_half = co_dinh / tc_month_half
    cps_half = r_pilot['cps'] + co_dinh_half
    print(f'  pilot n_yc={n_pilot_yc}, thanh_cong={n_pilot_tc}, cps={r_pilot["cps"]:.0f} Ä‘ [simulated]')
    print(f'  Quy mÃ´ Ä‘áº§y Ä‘á»§: {tc_month_full} viá»‡c/thÃ¡ng, cá»‘ Ä‘á»‹nh/viá»‡c={co_dinh_full:.0f} Ä‘, '
          f'cps+cá»‘ Ä‘á»‹nh={cps_full:.0f} Ä‘ = {cps_full / BASELINE:.2f}Ã— [simulated]')
    print(f'  Ná»­a khá»‘i lÆ°á»£ng: {tc_month_half} viá»‡c/thÃ¡ng, cá»‘ Ä‘á»‹nh/viá»‡c={co_dinh_half:.0f} Ä‘, '
          f'cps+cá»‘ Ä‘á»‹nh={cps_half:.0f} Ä‘ = {cps_half / BASELINE:.2f}Ã— [simulated]')

    # ---- B1 Â· Báº£ng Ä‘á»™ nháº¡y ----
    print('\n=== B1 Â· Báº£ng Ä‘á»™ nháº¡y ===')
    kich_ban = {
        'GiÃ¡ token gáº¥p Ä‘Ã´i':          dict(gia_vao=52, gia_ra=260),
        'GiÃ¡ token giáº£m má»™t ná»­a':      dict(gia_vao=13, gia_ra=65),
        'Tá»‰ lá»‡ xem láº¡i gáº¥p Ä‘Ã´i':      dict(he_so_xem_lai=2),
        'Tá»‰ lá»‡ xem láº¡i giáº£m má»™t ná»­a': dict(he_so_xem_lai=0.5),
        'Sá»‘ ca lÃ m láº¡i gáº¥p Ä‘Ã´i':       dict(he_so_lam_lai=2),
        'Sá»‘ ca lÃ m láº¡i giáº£m má»™t ná»­a':  dict(he_so_lam_lai=0.5),
        'LÆ°Æ¡ng nhÃ¢n viÃªn tÄƒng 25%':    dict(luong_phut=2500),
        'Chá»‰ cho cháº¡y tá»‘i Ä‘a 2 láº§n':  dict(max_lan_chay=2),
        'Chá»‰ cho cháº¡y 1 láº§n':          dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'  {"Ká»‹ch báº£n":<35} {"CPS (Ä‘)":>10} {"Thay Ä‘á»•i":>10}')
    print(f'  {"Gá»‘c (A2)":<35} {goc:>10,.0f} {"":>10}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'  {ten:<35} {cps:>10,.0f} {(cps / goc - 1) * 100:>+9.1f}%')

    # ---- B2 Â· Äá»•i má»™t cáº·p ----
    print('\n=== B2 Â· Äá»•i má»™t cáº·p vÃ  xáº¿p háº¡ng ===')
    b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'  GiÃ¡ token gáº¥p Ä‘Ã´i + xem láº¡i gáº¥p Ä‘Ã´i: {b2:,.0f} Ä‘ ({(b2 / goc - 1) * 100:+.1f}%)')
    print('  Xáº¿p háº¡ng ba yáº¿u tá»‘: 1. Sá»‘ ca lÃ m láº¡i Â· 2. Tá»‰ lá»‡ xem láº¡i Â· 3. LÆ°Æ¡ng nhÃ¢n viÃªn')

    # ---- B3 Â· Giá»›i háº¡n cháº¡y láº¡i ----
    print('\n=== B3 Â· Giá»›i háº¡n cháº¡y láº¡i cÃ³ tháº­t sá»± ráº» hÆ¡n ===')
    print(f'  {"Giá»›i háº¡n":<10} {"Tá»•ng trá»£ lÃ½":>14} {"KhÃ´ng TC":>10} {"Cáº£ há»‡ thá»‘ng":>14} {"CPS":>10}')
    for lim in [1, 2, 3]:
        r_lim = mo_hinh(runs, reqs, max_lan_chay=lim)
        khong_tc = reqs.shape[0] - r_lim['thanh_cong']
        he_thong = r_lim['tong'] + khong_tc * BASELINE
        print(f'  {lim} láº§n{"":<6} {r_lim["tong"]:>14,.0f} {khong_tc:>10} {he_thong:>14,.0f} {r_lim["cps"]:>10,.0f}')

    # ---- B4 Â· Náº¿u pháº£i xem láº¡i táº¥t cáº£ ----
    print('\n=== B4 Â· Náº¿u pháº£i xem láº¡i táº¥t cáº£ (noi_dia + hang_nang) ===')
    sub_b4 = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_b4 = runs[runs['request_id'].isin(sub_b4['request_id'])]
    # Äáº¿m yÃªu cáº§u cÃ³ Ã­t nháº¥t má»™t láº§n cháº¡y status = ok
    req_has_ok = runs_b4[runs_b4['status'] == 'ok']['request_id'].unique()
    n_has_ok = len(req_has_ok)
    n_lam_lai_b4 = (sub_b4['ket_qua'] == 'lam_lai').sum()
    tc_b4 = (sub_b4['ket_qua'] == 'thanh_cong').sum()
    tien_token_b4 = (runs_b4['tokens_in'] / 1000 * GIA_VAO + runs_b4['tokens_out'] / 1000 * GIA_RA).sum()
    tien_tool_b4 = (runs_b4['tool_calls'] * GIA_TOOL).sum()

    # Vá»›i 9 phÃºt lÃ m láº¡i (Ä‘á» cho)
    xem_lai_b4 = n_has_ok * 5 * LUONG_PHUT          # 5 phÃºt xem láº¡i má»—i yÃªu cáº§u cÃ³ ok
    lam_lai_b4_9 = n_lam_lai_b4 * 9 * LUONG_PHUT
    tong_b4_9 = tien_token_b4 + tien_tool_b4 + xem_lai_b4 + lam_lai_b4_9
    cps_b4_9 = tong_b4_9 / tc_b4

    # Vá»›i 15,3 phÃºt lÃ m láº¡i (trung bÃ¬nh thá»±c táº¿ trong dá»¯ liá»‡u)
    lam_lai_b4_153 = n_lam_lai_b4 * 15.3 * LUONG_PHUT
    tong_b4_153 = tien_token_b4 + tien_tool_b4 + xem_lai_b4 + lam_lai_b4_153
    cps_b4_153 = tong_b4_153 / tc_b4

    print(f'  n_b4={len(sub_b4)}, yc cÃ³ ok={n_has_ok}, ca lÃ m láº¡i={n_lam_lai_b4}, viá»‡c thÃ nh cÃ´ng={tc_b4}')
    print(f'  Token+tool={tien_token_b4 + tien_tool_b4:,.0f} Ä‘')
    print(f'  Vá»›i 9 phÃºt lÃ m láº¡i: tá»•ng={tong_b4_9:,.0f} Ä‘ â†’ cps={cps_b4_9:.0f} Ä‘ = {cps_b4_9 / BASELINE:.2f}Ã— [simulated]')
    print(f'  Vá»›i 15,3 phÃºt lÃ m láº¡i: tá»•ng={tong_b4_153:,.0f} Ä‘ â†’ cps={cps_b4_153:.0f} Ä‘ = {cps_b4_153 / BASELINE:.2f}Ã— [simulated]')
    print('  Xem láº¡i 100% gáº§n nhÆ° xÃ³a háº¿t lá»£i tháº¿ tiáº¿t kiá»‡m. Pilot pháº£i há»c Ä‘Æ°á»£c tá»‰ lá»‡ xem láº¡i cÃ³ thá»ƒ giáº£m xuá»‘ng má»©c nÃ o an toÃ n.')

    # ---- D1 · Cỡ mẫu và kiểm tra an toàn pilot ----
    phan_tich_pilot_d(reqs)
