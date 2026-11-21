"""File nháp Nhiệm vụ D (Pilot & Cỡ mẫu) — Ngọc phụ trách.
Chạy trong thư mục src/: python3 nhap_pilot.py
Sau khi Đức hoàn thành mốc 2 của src/lab13.py:
  1. Dán các hàm (co_mau, phan_tich_pilot_d) lên trước dòng `if __name__ == '__main__':` của src/lab13.py.
  2. Dán lời gọi `phan_tich_pilot_d(reqs)` vào cuối khối main thay dòng `# TODO CP4`.
  3. Chạy `python3 lab13.py` kiểm tra không lỗi, rồi xoá file src/nhap_pilot.py này.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize


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
    # Giải: c_nv * m / (1 + (m - 1) * icc) >= n_e
    # => (c_nv - n_e * icc) * m >= n_e * (1 - icc)
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

    print('\n========== NHIỆM VỤ D1 · CỠ MẪU & CHỈ SỐ AN TOÀN PILOT ==========')
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
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    phan_tich_pilot_d(reqs)
