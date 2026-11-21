# Báº£ng chi phÃ­ Â· Nhiá»‡m vá»¥ A vÃ  B

Sá»‘ tÃ­nh báº±ng `src/lab13.py`. Má»i con sá»‘ tÃ­nh tá»« cá»™t `_simulated` ghi nhÃ£n `simulated`. Má»—i cÃ¢u tráº£ lá»i khÃ´ng quÃ¡ ba dÃ²ng, cÃ³ Ã­t nháº¥t má»™t con sá»‘.

## A1 Â· Ba phÃ©p thá»­ Ä‘Ã¡p Ã¡n biáº¿t trÆ°á»›c

| PhÃ©p thá»­ (p = 0,8) | Káº¿t quáº£ cá»§a nhÃ³m |
| --- | --- |
| Sá»‘ láº§n cháº¡y trung bÃ¬nh, tá»‘i Ä‘a 2 láº§n | 1,20 |
| Sá»‘ láº§n cháº¡y trung bÃ¬nh, cháº¡y Ä‘áº¿n khi Ä‘Ãºng | 1,25 |
| Há»‡ sá»‘ chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng, tá»‘i Ä‘a 3 láº§n | 1,25 |

## A2 Â· MÃ´ hÃ¬nh chi phÃ­ tá»« trace

| Khoáº£n | Sá»‘ tiá»n (Ä‘) | Nguá»“n | NhÃ£n |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | Ä‘o tá»« trace |
| Tool | 84.000 | `logix_runs.csv` | Ä‘o tá»« trace |
| Trong Ä‘Ã³, pháº§n cá»§a láº§n cháº¡y thá»© 2 vÃ  3 | 93.804 | attempt lá»›n hÆ¡n 1 | Ä‘o tá»« trace |
| Xem láº¡i (890 phÃºt) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| LÃ m láº¡i (1.132 phÃºt) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tá»•ng chi phÃ­ | 4.373.585 | | cÃ³ pháº§n simulated |
| Sá»‘ viá»‡c thÃ nh cÃ´ng | 978 | `ket_qua` | |
| Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng | 4.472 | | simulated |
| HoÃ¡ Ä‘Æ¡n token vÃ  tool chia cho sá»‘ yÃªu cáº§u | 275 | | Ä‘o tá»« trace |

- Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng gáº¥p **16,3 láº§n** "hoÃ¡ Ä‘Æ¡n chia sá»‘ yÃªu cáº§u" (4.472 Ã· 275). LÃ½ do: tá»­ sá»‘ tÃ­nh má»i láº§n cháº¡y ká»ƒ cáº£ láº§n lá»—i, cÃ²n máº«u sá»‘ chá»‰ Ä‘áº¿m 978 viá»‡c thÃ nh cÃ´ng, khÃ´ng pháº£i 1.200 yÃªu cáº§u.
- Khoáº£n lá»›n nháº¥t lÃ  **lÃ m láº¡i, chiáº¿m 51,8%** tá»•ng chi phÃ­ [simulated]; tiáº¿p theo lÃ  xem láº¡i 40,7% [simulated]. Giá» nhÃ¢n viÃªn chiáº¿m 92,5% tá»•ng chi phÃ­.

## A3 Â· TÃ¡ch theo loáº¡i yÃªu cáº§u

| Loáº¡i | Sá»‘ yÃªu cáº§u | Tá»‰ lá»‡ thÃ nh cÃ´ng | Sá»‘ láº§n cháº¡y má»—i yÃªu cáº§u | Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng [sim] | So vá»›i 12.000 Ä‘ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 Ä‘ | 0,22Ã— |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 Ä‘ | 0,69Ã— |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 Ä‘ | 1,88Ã— |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 Ä‘ | 0,85Ã— |

- **quoc_te khÃ´ng Ä‘Ã¡ng Ä‘á»ƒ trá»£ lÃ½ xá»­ lÃ½** (1,88Ã—, tá»‰ lá»‡ thÃ nh cÃ´ng chá»‰ 27,3%). Cho cháº¡y láº¡i tá»›i 3 láº§n khÃ´ng giÃºp: láº§n 1 Ä‘Ãºng 30%, láº§n 2 chá»‰ 11,4%, láº§n 3 chá»‰ 2,2% â€” lá»—i láº·p láº¡i trÃªn cÃ¹ng yÃªu cáº§u, cháº¡y láº¡i chá»‰ tá»‘n thÃªm tiá»n.
- **doi_tac** (0,85Ã—) sÃ¡t ngÆ°á»¡ng vÃ  cÃ³ Ä‘iá»u khoáº£n riÃªng nÃªn cÅ©ng loáº¡i khá»i pháº¡m vi pilot. Pilot giá»›i háº¡n á»Ÿ **noi_dia + hang_nang**.

## A4 Â· Chi phÃ­ cá»‘ Ä‘á»‹nh (pháº¡m vi noi_dia + hang_nang)

| Khá»‘i lÆ°á»£ng | Viá»‡c thÃ nh cÃ´ng má»—i thÃ¡ng | Chi phÃ­ cá»‘ Ä‘á»‹nh má»—i viá»‡c | Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng + cá»‘ Ä‘á»‹nh [sim] | So vá»›i 12.000 Ä‘ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yÃªu cáº§u/thÃ¡ng (Ä‘áº§y Ä‘á»§) | 41.242 | 970 Ä‘ | 4.384 Ä‘ | 0,37Ã— |
| Má»™t ná»­a khá»‘i lÆ°á»£ng (~22.500 yc/thÃ¡ng) | 20.621 | 1.940 Ä‘ | 5.354 Ä‘ | 0,45Ã— |

- **Chi phÃ­ cá»‘ Ä‘á»‹nh khÃ´ng Ä‘á»•i káº¿t luáº­n á»Ÿ quy mÃ´ Ä‘áº§y Ä‘á»§** (váº«n 0,37Ã— so vá»›i 12.000 Ä‘), nhÆ°ng tÄƒng máº¡nh khi khá»‘i lÆ°á»£ng giáº£m: ná»­a khá»‘i lÆ°á»£ng â†’ 5.354 Ä‘ (0,45Ã—). Há»“ sÆ¡ launch ghi nhÃ£n simulated vÃ  nÃªu rÃµ á»Ÿ khá»‘i lÆ°á»£ng nÃ o.

## B1 Â· Äá»•i tá»«ng yáº¿u tá»‘

| Ká»‹ch báº£n | CÃ¡ch tÃ­nh | Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng [sim] | Thay Ä‘á»•i (%) |
| --- | --- | ---: | ---: |
| Gá»‘c (A2) | â€” | 4.472 Ä‘ | â€” |
| GiÃ¡ token gáº¥p Ä‘Ã´i | 52 Ä‘ vÃ  260 Ä‘ cho 1.000 token; giÃ¡ tool giá»¯ nguyÃªn | 4.723 Ä‘ | +5,6% |
| GiÃ¡ token giáº£m má»™t ná»­a | 13 Ä‘ vÃ  65 Ä‘ | 4.346 Ä‘ | âˆ’2,8% |
| Tá»‰ lá»‡ xem láº¡i gáº¥p Ä‘Ã´i | Tiá»n xem láº¡i Ã— 2 | 6.292 Ä‘ | +40,7% |
| Tá»‰ lá»‡ xem láº¡i giáº£m má»™t ná»­a | Tiá»n xem láº¡i Ã· 2 | 3.562 Ä‘ | âˆ’20,3% |
| Sá»‘ ca lÃ m láº¡i gáº¥p Ä‘Ã´i | Tiá»n lÃ m láº¡i Ã— 2 | 6.787 Ä‘ | +51,8% |
| Sá»‘ ca lÃ m láº¡i giáº£m má»™t ná»­a | Tiá»n lÃ m láº¡i Ã· 2 | 3.315 Ä‘ | âˆ’25,9% |
| LÆ°Æ¡ng nhÃ¢n viÃªn tÄƒng 25% | 2.500 Ä‘ má»—i phÃºt | 5.506 Ä‘ | +23,1% |
| Chá»‰ cho cháº¡y tá»‘i Ä‘a 2 láº§n | Bá» láº§n cháº¡y cÃ³ attempt > 2; yÃªu cáº§u cÃ³ so_lan_chay > 2 coi lÃ  chuyen_nhan_vien | 4.237 Ä‘ | âˆ’5,2% |
| Chá»‰ cho cháº¡y 1 láº§n | NhÆ° trÃªn vá»›i giá»›i háº¡n 1 | 4.111 Ä‘ | âˆ’8,1% |

## B2 Â· Äá»•i má»™t cáº·p vÃ  xáº¿p háº¡ng

- GiÃ¡ token gáº¥p Ä‘Ã´i cÃ¹ng lÃºc tá»‰ lá»‡ xem láº¡i gáº¥p Ä‘Ã´i: **6.543 Ä‘ (+46,3%)** [simulated], Ä‘Ãºng báº±ng tá»•ng hai tÃ¡c Ä‘á»™ng riÃªng (5,6% + 40,7%) vÃ¬ mÃ´ hÃ¬nh cá»™ng tuyáº¿n tÃ­nh.
- Xáº¿p háº¡ng ba yáº¿u tá»‘ áº£nh hÆ°á»Ÿng máº¡nh nháº¥t: **1. Sá»‘ ca lÃ m láº¡i (+51,8%) Â· 2. Tá»‰ lá»‡ xem láº¡i (+40,7%) Â· 3. LÆ°Æ¡ng nhÃ¢n viÃªn (+23,1%).**

## B3 Â· Giá»›i háº¡n cháº¡y láº¡i cÃ³ tháº­t sá»± ráº» hÆ¡n

| Giá»›i háº¡n | Tá»•ng chi phÃ­ trá»£ lÃ½ [sim] | Sá»‘ yÃªu cáº§u khÃ´ng thÃ nh cÃ´ng | Chi phÃ­ cáº£ há»‡ thá»‘ng [sim] | Chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng [sim] |
| --- | ---: | ---: | ---: | ---: |
| 1 láº§n | 3.621.781 Ä‘ | 319 | 7.449.781 Ä‘ | 4.111 Ä‘ |
| 2 láº§n | 4.093.220 Ä‘ | 234 | **6.901.220 Ä‘** (ráº» nháº¥t) | 4.237 Ä‘ |
| 3 láº§n | 4.373.585 Ä‘ | 222 | 7.037.585 Ä‘ | 4.472 Ä‘ |

- Giá»›i háº¡n **2 láº§n ráº» nháº¥t cho cáº£ há»‡ thá»‘ng** (6.901.220 Ä‘), nhÆ°ng khÃ´ng trÃ¹ng vá»›i giá»›i háº¡n cho chi phÃ­ má»—i viá»‡c thÃ nh cÃ´ng tháº¥p nháº¥t (1 láº§n = 4.111 Ä‘). Tá»‘i Æ°u riÃªng CPS sáº½ Ä‘áº©y thÃªm 85 viá»‡c sang nhÃ¢n viÃªn lÃ m thay.

## B4 Â· Náº¿u pháº£i xem láº¡i táº¥t cáº£

- Vá»›i noi_dia + hang_nang (982 yÃªu cáº§u, 948 yÃªu cáº§u cÃ³ ok, 48 ca lÃ m láº¡i, 900 viá»‡c thÃ nh cÃ´ng), token+tool=224.513 Ä‘. Xem láº¡i 100% (5 phÃºt má»—i ca) + lÃ m láº¡i **9 phÃºt**: tá»•ng **10.568.513 Ä‘ â†’ 11.743 Ä‘ = 0,98Ã— cá»§a 12.000 Ä‘** [simulated]. Náº¿u dÃ¹ng má»©c lÃ m láº¡i thá»±c táº¿ **15,3 phÃºt/ca** (trung bÃ¬nh trong dá»¯ liá»‡u): 11.173.313 Ä‘ â†’ **12.415 Ä‘ = 1,03Ã—** [simulated] â€” Ä‘áº¯t hÆ¡n nhÃ¢n viÃªn tá»± lÃ m.
- Káº¿t quáº£ nÃ y nÃ³i lÃªn ráº±ng: **xem láº¡i 100% thÃ¬ trá»£ lÃ½ gáº§n nhÆ° khÃ´ng tiáº¿t kiá»‡m Ä‘Æ°á»£c gÃ¬**, vÃ¬ tiá»n xem láº¡i chiáº¿m ~90% chi phÃ­. Pilot pháº£i há»c Ä‘Æ°á»£c tá»‰ lá»‡ xem láº¡i cÃ³ thá»ƒ giáº£m an toÃ n xuá»‘ng má»©c nÃ o, vÃ  má»—i láº§n xem láº¡i cÃ³ ngáº¯n hÆ¡n 5 phÃºt khÃ´ng (má»©c hoÃ  vá»‘n vá»›i 9 phÃºt lÃ m láº¡i lÃ  5,1 phÃºt; vá»›i 15,3 phÃºt lÃ  4,8 phÃºt).
