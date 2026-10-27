# Hàng đợi kho đề

Cách nhận việc: điền tên (claude / cursor / codex / antigravity) vào cột **Người nhận** + bước đang làm, commit ngay.
Xong bước → đổi ⬜ thành ✅ (kèm số liệu), xóa tên. Quy trình: `docs/kho-de/HUONG-DAN-AI.md`.

Ký hiệu: ⬜ chưa làm · 🔄 đang làm · ✅ xong · ⏸ tạm dừng (có thể trùng web) · ⚠️ vướng (ghi chú).

## Lớp 10 — Đề rèn luyện cuối bài (TAP 1 + TAP 2)

Nguồn: `TAI LIEU DANG WEB/Toán 12/Đề thi/ĐỀ THI RÈN LUYỆN CUỐI BÀI/TAP <1|2>-DE REN CUOI BAI HỌC TOAN 10/`.
Chỉ dùng bản giáo viên (không có `-HS`, không `GHEP FULL`).
Các bản `-ALG` (chương 6–9) là đề **không có lời giải/đáp án** → pipeline bỏ qua, chỉ dùng bản thường. Đề chương 6–9 đánh dấu đáp án trắc nghiệm bằng **gạch chân chữ A/B/C/D** (không có dòng «Chọn X») — parser đã nhận.
Kết quả Toán 10 đã chép vào thư mục `KET QUA KHO DE/<bài>/` nằm cạnh file Word gốc trong `TAI LIEU DANG WEB` (04/10/2026): `de1–3.import.txt`, `preview.html`, `images/`, `de1–3.json`.

| Bài | MÁY (Word → câu) | OCR ảnh công thức | Sửa câu có cờ | Phân loại (dạng + mức độ) | Người nhận | Ghi chú |
|---|---|---|---|---|---|---|
| C1-B1-MENH DE | ✅ 3 đề/67 câu, đã bỏ 14 câu trùng web | ✅ không có |  | ✅ claude phân sẵn — **chờ thầy duyệt** |  | Web đã có đề «Bài 1: Mệnh đề và tập hợp» (20 câu) — có thể trùng |
| C1-B2-TAP HOP VA CAC PHEP TOAN TREN TAP HOP | ✅ 3 đề/68 câu, **bỏ cả đề 1** (16/24 câu trùng web) + 2 câu | ✅ không có |  | ✅ claude phân sẵn — **chờ thầy duyệt** |  | Web đã có đề «Bài 2. Tập hợp và các phép toán» (22 câu) — có thể trùng |
| C1-ON TAP CHUONG | ✅ 3 đề/67 câu, đã bỏ 6 câu trùng web | ✅ claude đã đọc 6 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C2-B1-BPT BAC NHAT HAI AN | ✅ 3 đề/66 câu, đã bỏ 3 câu trùng web | ✅ claude đã đọc 10 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C2-B2-HE BPT BAC NHAT HAI AN | ✅ 3 đề/66 câu | ✅ claude đã đọc 15 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C2-B3-ON TAP CUOI CHUONG 2 | ✅ 2 đề/44 câu | ✅ claude đã đọc 8 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C3-B1-GIA TRI LUONG GIAC CUA MOT GOC | ✅ 3 đề/66 câu | ✅ không có | ⬜ 5 câu có cờ (đề 2–3) | ✅ claude phân sẵn 42 câu — **chờ thầy duyệt** | | **Đề 1 = đề «Bài 5» đã có trên web (17/22 câu trùng) → đã BỎ ĐỀ 1**. Đề 2, 3: bỏ 2 câu trùng web (de2.P1.C5, de3.P1.C4) |
| C3-B2-HE THUC LUONG TRONG TAM GIAC | ✅ 3 đề/66 câu | ✅ claude (20 ảnh) | ⬜ 24 câu có cờ | ✅ claude phân sẵn 63 câu — **chờ thầy duyệt** | | Bỏ 3 câu trùng web (de1.P1.C3, de1.P1.C8, de2.P1.C7) |
| C4-B1-KHAI NIEM VECTO | ✅ 3 đề/55 câu | ✅ claude đã đọc 4 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C4-B2-TONG VA HIEU CUA HAI VECTO | ✅ 3 đề/66 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C4-B3-TICH CUA MOT SO VOI MOT VECTO | ✅ 3 đề/67 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C4-B4-TICH VO HUONG CUA HAI VECTO | ✅ 3 đề/67 câu, đã bỏ 1 câu trùng web | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C4-B5-ON TAP CHUONG 4 | ✅ 2 đề/47 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C5-B1-SO GAN DUNG VA SAI SO | ✅ 3 đề/67 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C5-B2-CAC SO DAC TRUNG DO XU THE TRUNG TAM | ✅ 3 đề/66 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C5-B3-CAC SO DAC TRUNG DO DO PHAN TAN | ✅ 3 đề/67 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C5-B4-ON TAP CUOI CHUONG 5 | ✅ 2 đề/44 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C6-B1-HAM SO | ✅ 3 đề/66 câu | ✅ claude đã đọc 71 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C6-B2-HAM SO BAC HAI | ✅ 3 đề/66 câu | ✅ claude đã đọc 5 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C6-B3-DAU TAM THUC BAC HAI | ✅ 3 đề/67 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C6-B4-PT QUY VE PT BAC HAI | ✅ 3 đề/66 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C6-B5-ON TAP CHUONG 6 | ✅ 3 đề/66 câu, đã bỏ 1 câu trùng web | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C7-B1-PHUONG TRINH DUONG THANG | ✅ 3 đề/66 câu | ✅ claude đã đọc 33 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C7-B2-VI TRI TUONG DOI GIUA HAI DUONG THANG.GOC VA KHOANG CACH | ✅ 3 đề/66 câu | ✅ claude đã đọc 88 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C7-B3-DUONG TRON TRONG MAT PHANG TOA DO | ✅ 3 đề/66 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C7-B4-BA DUONG CONIC | ✅ 3 đề/67 câu | ✅ claude đã đọc 3 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C7-B5-ON TAP CHUONG 7 | ✅ 3 đề/66 câu, đã bỏ 1 câu trùng web | ✅ claude đã đọc 9 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C8-B1-QUY TAC DEM | ✅ 3 đề/66 câu, đã bỏ 1 câu trùng web | ✅ claude đã đọc 11 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C8-B2-HOAN VI CHINH HOP VA TO HOP | ✅ 3 đề/66 câu | ✅ claude đã đọc 4 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C8-B3-NHI THUC NEWTON | ✅ 3 đề/66 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C8-B4-BAI TAP CUOI CHUONG 8 | ✅ 3 đề/66 câu | ✅ claude đã đọc 4 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C9-B1-BIEN CO VA DINH NGHIA CO DIEN CUA XAC SUAT | ✅ 3 đề/66 câu | ✅ claude đã đọc 2 ảnh | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C9-B2-THUC HANH TINH XAC SUAT THEO DINH NGHIA CO DIEN | ✅ 3 đề/68 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |
| C9-B3-ON TAP CHUONG 9 | ✅ 3 đề/68 câu | ✅ không có | ⬜ | ✅ claude phân sẵn — **chờ thầy duyệt** |  |  |

Cây dạng bài `kho_de_data/dang_bai/lop10|11|12.json` (nguồn Noctorium 04/10/2026, sinh bằng `scripts/kho_de/build_dang_bai.mjs` từ `noctorium_tree.txt`): lớp 10 = 79 dạng (chương 3 giữ 25 dạng soạn tay), lớp 11 = 118, lớp 12 = 151. Trạng thái **nháp — chờ thầy duyệt**. `dang_toan_web` lấy nguyên văn từ curriculum.

Phân loại sẵn Toán 10 (04/10/2026): 2.104 câu giữ lại đều đã có dạng + mức độ (`boi: claude`). Dạng chương 7, chương 6 bài 3–4, chương 1 bài 2… còn thô (xem `de_xuat_dang_moi.json`). Mức độ chủ yếu theo gợi ý vị trí của pipeline, chỉnh tay các câu rõ ràng khác; **chưa qua hiệu chuẩn 30 câu**. Dạng của nhiều câu chọn theo từ khóa đề nên cần thầy rà.

Quy ước mặc định: AI phân sẵn dạng + mức độ cho mọi câu; **câu trùng web mặc định `bo_cau`** (thầy bỏ cờ nếu muốn giữ). `dedupe_web.py` nay so cả phương án (trước chỉ so đề dẫn nên báo trùng nhầm câu chung chung).


## Lớp 12 — Đề rèn luyện cuối bài (TAP 1 + TAP 2)

Chạy ngày 04/10/2026 bằng `python scripts/kho_de/chay_lop.py 12` (kết quả chép vào `KET QUA KHO DE/` cạnh file Word). 22/23 bài đã tách: 1.254 câu, trùng web bỏ 167 câu, còn 479 câu có cờ.
- ✅ **C5-B3 (Công thức tính góc)** đã tách được (60 câu; Word chậm: ~1.400 công thức, 1 công thức treo MathType nên bỏ qua, lưu thành ảnh đã đọc tay). Dạng/mức độ do Claude gán theo từ khóa (D01 hai đường / D02 đường–mặt / D03 hai mặt) — soát lại.
- ✅ Ảnh công thức lớp 12: đã đọc hết (C1-B1, C1-ÔN, C2-B1, C2-B3, C2-ÔN, C4, C5-B2 cả lời giải, C5-ÔN, Tiệm cận). Còn 8 ảnh hỏng (WMF vỡ, đã gán chữ theo ngữ cảnh) và 2 hình vẽ .emf (BBT/hình hộp) vẫn là ảnh. Đề 3 phần trả lời ngắn của C5-B2: «Đáp số» là ảnh nhãn nên đáp án ngắn suy từ lời giải, cần xác nhận.
- ✅ Đúng/Sai lớp 12: 0 câu thiếu đáp án — 65 câu suy tự động từ lời giải (cờ `dung_sai_suy_tu_loi_giai_can_xac_nhan`), 18 câu Claude đọc lời giải ghi vào `sua.json`, 1 câu tự luận lẫn vào phần Đúng/Sai (C3-ÔN đề 1) đã bỏ.
- ✅ 06/10/2026: lớp 12 hết câu thiếu đáp án/thiếu đề (sus = 0): Claude điền ~90 đáp án trả lời ngắn + 9 đáp án trắc nghiệm vào `sua.json`; GT12-C1-B3 phần 0 lẫn Đúng/Sai + trả lời ngắn → `sua.json` có trường `type` (parser `apply_data` nhận). Sửa lệch tên ảnh `tex.docx` ≠ `goc.docx` (OCR đọc lại từ tex.docx); ảnh trong LỜI GIẢI (tier 2) chưa đọc, vẫn hiện dạng ảnh.
- ✅ 06/10/2026: lớp 12 hết câu thiếu đáp án/thiếu đề (sus = 0): Claude điền ~90 đáp án trả lời ngắn + 9 đáp án trắc nghiệm vào `sua.json`; GT12-C1-B3 phần 0 lẫn Đúng/Sai + trả lời ngắn → `sua.json` có trường `type` (parser `apply_data` nhận). Sửa lệch tên ảnh `tex.docx` ≠ `goc.docx` (OCR đọc lại từ tex.docx); ảnh trong LỜI GIẢI (tier 2) chưa đọc, vẫn hiện dạng ảnh.
- ✅ 06/10/2026 (rà soát cờ lỗi lớp 10–12): sửa/bổ sung ~120 câu (đáp án ngắn không ra số, câu Đúng/Sai thiếu mệnh đề, phương án trắc nghiệm không tách được, đáp án mâu thuẫn «Chọn X», lỗi KaTeX do «%»/«&»/chỉ số kép, mảnh hình vẽ OLE trong lời giải), gán dạng + mức độ cho 224 câu còn thiếu (dạng lấy theo câu giống nhất cùng bài, chờ thầy duyệt). Còn lại: ~780 câu đáp án suy từ lời giải chưa xác nhận từng câu; 45 câu còn ảnh công thức trong lời giải.
- Một số bài có ít câu bất thường (C5-B1 30, C4-ÔN 18, C6-ÔN 12) → cần xem lại việc tách đề.
- ✅ Đã phân sẵn dạng + mức độ cho 1.115 câu giữ lại (22 bài, boi=claude, ngày 04/10/2026): chương 1 đọc từng câu; chương 2–6 chủ yếu theo từ khóa đề (có thể lệch) — mức độ theo gợi ý vị trí/thẻ [Mức độ n]. Thầy chỉnh trong `kho_de_data/lop12/<bài>/phan_loai.json`. Ôn tập chương 3–6 (dạng B1/B2 lẫn nhau) cần soát kỹ hơn.

## Bài đã có đề ôn tập trên web → tạm dừng (có thể trùng)

Kiểm tra ngày 04/10/2026 từ mục lục web (`public_catalog_v1/quizzes`, loại `lesson`).
Khi chạy lại các bài này: bước MÁY tự dò trùng (`dedupe_web.py`), chỉ bỏ đề/câu trùng — đề khác trong cùng file vẫn dùng được.

| Lớp | Bài | Đề trên web |
|---|---|---|
| 10 | C1-B1 Mệnh đề | «Bài 1: Mệnh đề và tập hợp» |
| 10 | C1-B2 Tập hợp | «BÀI 2. Tập hợp và các phép toán với tập hợp» |
| 10 | C3-B1 Giá trị lượng giác | «Bài 5: Giá trị lượng giác của một góc từ 0° đến 180°» = Đề 1 (đã bỏ) |
| 11 | C1-B1 Giá trị lượng giác góc lượng giác | 2 đề («Đề kiểm tra Bài 1… Đề 01», «C1-B1 — Đề ôn tập 1») |
| 11 | C1-B2 Công thức lượng giác | «Bài 2: Công thức lượng giác» |
| 11 | C1-B3 Hàm số lượng giác | «C1-B1 — Đề ôn tập 3: Hàm số lượng giác» |
| 11 | C1-B4 Phương trình lượng giác | «C1-B4: Phương trình lượng giác» |
| 11 | C1 Ôn tập chương | «C1-B5: Ôn tập chương» |
| 12 | C1 Bài 1, 2, 3, 4 · C2 Bài 6, 7, 8 · C3 Bài 9 | mỗi bài 1 đề |

Chưa dò: câu luyện tập trong bài giảng (`math_lessons_v2`) và Ngân hàng câu hỏi (`math_question_bank_v1`, không đọc công khai được).

## Lớp 11 — Đề rèn luyện cuối bài (TAP 1 + TAP 2)

Chạy ngày 05/10/2026 bằng `python scripts/kho_de/chay_lop.py 11` (kết quả chép vào `KET QUA KHO DE/` cạnh file Word). 36 bài (không có C8-B2: không có file). Còn **1.856 câu** giữ lại; 236 câu bị bỏ (trùng web + câu chứng minh/giải thích không có đáp án ngắn + câu thiếu ý Đúng/Sai trong file gốc). Đã có dạng + mức độ cho cả 1.856 câu.
`run_word_folder.py` đã nhận tên TAP 2 (`B1 - …`, `BAI TAP CUOI CHUONG 6` → thêm tiền tố `C<chương>-` theo thư mục).
**Lưu ý đánh số chương:** cây `dang_bai/lop11.json` theo Noctorium nên chương 7 Word (đạo hàm) = C9 trong cây; chương 8 Word (vuông góc) = C7; chương 9 Word (xác suất) = C8.
- ✅ Ảnh công thức: đã đọc hết (còn 10 công thức MathType Word không chuyển được, để ảnh; 4 câu trắc nghiệm C6-ÔN có đáp án là ảnh).
- ✅ Trả lời ngắn: Claude điền đáp án cho ~330 câu (từ kết luận lời giải, `short_correct` trong `sua.json`); 104 câu chương 4 + ~50 câu khác là chứng minh/giải thích/nhiều phần nên `bo_cau` (không chuyển tự luận). Một số đề/đáp án mâu thuẫn đã bỏ (C1-B2 3.P3.C1: đề 180–270° nhưng lời giải dùng 270–360°; C7-B1 2.P3.C2; C5-B1 2.P3.C6).
- ✅ Trắc nghiệm không ghi «Chọn X»: 243 câu máy tự suy từ kết luận lời giải (cờ `dap_an_suy_tu_loi_giai_can_xac_nhan`), 45 câu Claude đọc lời giải điền. Còn 5 câu (C6-ÔN, đáp án là ảnh) chưa có đáp án.
- ✅ Đúng/Sai: đủ đáp án; 14 câu thiếu ý trong file gốc đã bỏ.
- Phân dạng/mức độ do Claude gán **theo từ khóa đề** (mức độ theo gợi ý vị trí) — chưa đọc từng câu, cần soát, nhất là các bài ôn tập chương.
- Word treo ở 1 công thức của C6-ÔN: dùng `mtloop.sh` mẫu (ghi log idx, bỏ idx treo rồi chạy lại).

## Hiệu chuẩn mức độ

| AI | Số câu khớp / 30 | Đạt (≥ 85%) |
|---|---|---|
| claude | | |
| cursor | | |
| codex | | |
| antigravity | | |

## Nguồn PDF — Toán Từ Tâm lớp 12 (cuối chương HK1)

- ✅ `TTT-C1-ON CHUONG 1` (110 câu), `TTT-C2-ON CHUONG 2` (110 câu), `TTT-C3-ON CHUONG 3` (110 câu): 5 đề/chương, đáp án **Claude tự giải** (cờ `dap_an_tu_giai_can_xac_nhan`), đã gán dạng + mức độ; câu trùng web đã bỏ. Câu in sai/chưa chắc xem `ly_do` trong `sua.json` (ch3: de1.P1.C11, de2.P1.C1/C6/C9, de2.P3.C21, de3.P1.C4…).
- Chương 2 có nhiều câu trùng đề Word đã có trong kho (`C2-ON CHUONG 2`) — chưa có bước bỏ trùng trong kho.

## Nguồn PDF — Ngô Đức Tài «Bộ đề ôn định kì lớp 12 — học kì 1»

Nguồn: `C:/Users/ADMIN/Downloads/bo-de-on-tap-kiem-tra-dinh-ki-hoc-ki-1-mon-toan-12-ngo-duc-tai.pdf` (216 trang). 20 đề giữa kì 1 + 20 đề cuối kì 1. Mỗi đề có **bảng đáp án** cuối đề (không có lời giải). PDF chữ mất ký hiệu toán → gõ từ ảnh trang.

| Bài | Đề | Trạng thái |
|---|---|---|
| `NDT-GK1-ON TAP` | Giữa kì 1, đề số 1 (trang PDF 8–12) | ✅ 22 câu, bỏ 1 câu trùng web (`de1.P1.C5`), còn 21. Đối chiếu bảng đáp án và tính lại hết. Dạng gán theo câu giống nhất — chờ thầy duyệt |
| | Giữa kì 1, đề 2–20 | ⬜ |
| | Cuối kì 1, đề 1–20 | ⬜ |

## Nguồn Word — ĐGNL ĐHQG TP.HCM 2025

Nguồn: `TAI LIEU DANG WEB/Toán 12/Đề thi/Đề ĐGNL/ĐGNL TPHCM 2025` (file .doc có lời giải). Mỗi đề 120 câu trắc nghiệm. Thư mục không có đề 3 và đề 8.

| Bài | Trạng thái |
|---|---|
| `DGNL-HCM-01` … `02`, `04`–`07`, `09`–`20` | ✅ 18 đề × 120 câu. Đáp án lấy từ «Câu n: Đáp án X» hoặc «Câu n. Chọn đáp án X». Mức độ theo nhãn NB/TH/VD/VDC trong đề. Chỉ 30 câu Phần 2 (toán / logic / số liệu) được gán dạng — chờ thầy duyệt; 90 câu môn khác không gán dạng |
| | ⚠️ Đề 16 câu 70 và đề 17 câu 47: bốn phương án trong Word để trống (số nằm ngoài dòng chữ). Đề 15 câu 66 và đề 16 câu 81, 99: còn công thức dạng ảnh trong lời giải. Một số câu cờ «lời giải nói phương án khác đúng» — đáp án vẫn theo dòng Chọn |

## Nguồn Word — Đề trường/sở 2026, số 31–39

Nguồn: `TAI LIEU DANG WEB/Toán 12/Đề thi/ĐỀ TRƯỜNG SỞ/2026 TRƯỜNG SỞ 31-39`. Chỉ file `-GV` (có lời giải). Bỏ bản `-HS`. Mỗi đề 22 câu: 12 trắc nghiệm + 4 đúng/sai + 6 trả lời ngắn.

| Bài | Trạng thái |
|---|---|
| `DT26-31-KSCL SO HUNG YEN` … `DT26-39-CUM DONG HP` | ✅ 9 đề × 22 câu. 0 lỗi KaTeX, 0 lỗi import, 0 câu trùng web. Đáp án trả lời ngắn lấy từ dòng «Đáp án / Đáp số / Trả lời» đầu lời giải |
| | ⚠️ `DT26-34` phần 3 câu 2: lời giải gốc ghi \(n = 1/4 = 0{,}75\). Tích vô hướng bằng \(\dfrac{1}{4}a^{2}\), đã sửa đáp án thành \(0{,}25\). Dạng bài gán theo câu giống nhất — chờ thầy duyệt |

## Nguồn Word — 40 đề trường/sở 2026 (bản mới)

Nguồn: `TAI LIEU DANG WEB/Toán 12/Đề thi/40 đề trường sở/40 DE THI THU CAC TRUONG, CAC SO NEW NAM 2026`. Chỉ file giáo viên (có lời giải). Bỏ bản `-HS` và file «FULL GHÉP». Đề số 0–25 trong thư mục trùng `DT26-00` … `DT26-25` đã có trong kho — không nhập lại. Đề 31–39 của thư mục này khác bộ `DT26-31` … `DT26-39` (Hưng Yên … Cụm Đông HP), nên đánh mã `DT26-41` … `DT26-49`. Dạng bài gán theo câu giống nhất — chờ thầy duyệt.

| Mã kho | File nguồn | Trạng thái |
|---|---|---|
| `DT26-26` | 26. Chuyên Lê Thánh Tông Đà Nẵng | ✅ 22 câu. Bỏ 1 câu trùng web (phần 1 câu 11). Phần 3 câu 3 lỗi công thức; câu 6 còn công thức dạng ảnh |
| `DT26-27` | 27. Cụm trường THPT Hà Tĩnh lần 1 | ⛔ Bỏ cả đề: trùng từng câu với `DT26-25` |
| `DT26-28` | 28. THPT Đô Lương 2, Nghệ An | ✅ 22 câu, không cờ |
| `DT26-29` | 29. Sở Phú Thọ lần 1 | ✅ 22 câu, không cờ |
| `DT26-30` | 30. THPT Cửa Lò lần 1 | ✅ 22 câu. Phần 2 câu 3 còn công thức dạng ảnh |
| `DT26-40` | 40. Mã đề 104 — BGD 2025 | ✅ 22 câu. Phần 2 câu 1–2: đúng/sai suy từ lời giải, chờ xác nhận |
| `DT26-41` | 31. Nguyễn Khuyến – Lê Thánh Tông | ⚠️ 21/22: thiếu 1 câu trả lời ngắn. Phần 2 câu 1 thiếu ý d; câu 2 và câu 4 chưa tách được đúng/sai. Phần 1 câu 8 trùng web (đã bỏ) |
| `DT26-42` | 32. Than Uyên, Lai Châu | ✅ 22 câu. Còn 6 công thức MathType ở phần 3 câu 1 |
| `DT26-43` | 33. Nguyễn Tất Thành, Quảng Ngãi | ⚠️ Đã bỏ phần tự luận (PHẦN B). Phần đúng/sai và 4 câu trả lời ngắn còn công thức dạng ảnh, chưa có đáp án chữ. Hai câu tự luận dính phần 3 (`C1b`, `C2b`) cũng chưa có đáp án |
| `DT26-44` | 34. Bãi Cháy, Quảng Ninh | ✅ 22 câu. Phần 3 câu 2: lời giải vỡ công thức (chữ Việt nằm trong công thức) |
| `DT26-45` | 35. Chuyên Đại học Vinh | ✅ 22 câu. Bỏ 1 câu trùng web (phần 1 câu 12). Phần 2 câu 1, 3 chờ xác nhận đúng/sai |
| `DT26-46` | 36. THPT CG–TT–CG2, Hải Phòng | ✅ 22 câu. Bỏ 1 câu trùng web (phần 1 câu 7). Phần 2 câu 3 và phần 3 câu 2 thiếu đáp án |
| `DT26-47` | 37. Mã đề 101 — BGD 2025 | ⚠️ 22 câu. Phần 1 câu 1 không tách được 4 phương án. Phần 2 câu 3 chỉ có ý a |
| `DT26-48` | 38. Mã đề 103 — BGD 2025 | ⚠️ 21/22: thiếu 1 câu trắc nghiệm. Phần 2 câu 1–2 thiếu một số ý |
| `DT26-49` | 39. Mã đề 102 — BGD 2025 | ✅ 22 câu. Phần 2 câu 4 thiếu ý c |

## Nguồn Word — Giữa kỳ I Toán 11

Nguồn: `TAI LIEU DANG WEB/Toán 11/Đề thi/ĐỀ HKI`. Mười file `GK1-11-DE n-LG.docx` (có lời giải). Bỏ `PHIEU TRA LOI.docx`. Mỗi đề: 12 trắc nghiệm + 2 đúng/sai + 4 trả lời ngắn. Phần 4 tự luận không đưa vào kho. Dạng bài gán theo câu giống nhất — chờ thầy duyệt. Mở kho, nhóm «Giữa kỳ I Toán 11».

| Mã | Trạng thái |
|---|---|
| `GK11-01-DE 1` | ✅ 18 câu. Bỏ 1 câu trùng web. Câu 2 chốt C, câu 9 chốt B (dòng «Chọn A» trong lời giải sai so với phép tính). Câu 5 còn công thức dạng ảnh |
| `GK11-02-DE 2` | ✅ 18 câu. Bỏ 1 câu trùng web. Câu 2 còn công thức dạng ảnh |
| `GK11-03-DE 3` | ✅ 18 câu. Bỏ 1 câu trùng web |
| `GK11-04-DE 4` | ✅ 18 câu, không cờ. Phần 2 câu 2: cả bốn ý đúng |
| `GK11-05-DE 5` | ✅ 18 câu. Câu 5 đã ghép lại 4 phương án (phương án thứ ba trong file gốc ghi nhầm chữ B). Câu 3 phần 3 còn công thức dạng ảnh |
| `GK11-06-DE 6` | ✅ 18 câu. Phần 2 câu 2: a Đúng, b Sai, c Đúng, d Đúng |
| `GK11-07-DE 7` | ✅ 18 câu. Phần 2 câu 1: a Đúng, b Sai, c Sai, d Đúng |
| `GK11-08-DE 8` | ✅ 18 câu, không cờ |
| `GK11-09-DE 9` | ✅ 17 câu. Bỏ 1 câu trùng web. Phần 2 chỉ có 1 câu đúng/sai trong file |
| `GK11-10-DE 10` | ✅ 18 câu. Bỏ 1 câu trùng web. Phần 3 câu 4 đáp án lấy ở cuối lời giải, chờ xác nhận |

## Nguồn Word — Bộ ôn thi THPTQG 2023 (5/30 đề có trong thư mục)

Nguồn: `TAI LIEU DANG WEB/Toán 12/Đề thi/12. BỘ 30 ĐỀ ÔN THI TOÁN THPTQG 2023 WORD`. Thư mục chỉ có đề 1–5 (file `D1.docx` … `D5.docx`, có lời giải). Bỏ bản `D1HS` … `D5HS`. Mỗi đề là 50 câu trắc nghiệm (khuôn tốt nghiệp cũ). Dạng bài gán theo câu giống nhất — chờ thầy duyệt. Mở kho, tìm «Ôn thi THPTQG 2023».

| Mã kho | Trạng thái |
|---|---|
| `TN23-01-DE 1` | ✅ 50 câu. Phần 1 câu 33 và 39 còn công thức dạng ảnh |
| `TN23-02-DE 2` | ✅ 50 câu. Câu 45 lệch dấu `$`; câu 46 lời giải vỡ môi trường `align` |
| `TN23-03-DE 3` | ✅ 50 câu, không cờ |
| `TN23-04-DE 4` | ✅ 50 câu, không cờ |
| `TN23-05-DE 5` | ✅ 50 câu. Câu 1: lời giải kết luận 2 nghiệm, đã chốt phương án C |

## Nguồn Word — Cuối kỳ I và Giữa kỳ I Toán 10

Nguồn: `TAI LIEU DANG WEB/Toán 10/Đề thi/L10-HK1` và `L10-GK1`. Bỏ 3 file ma trận. Phần tự luận của đề trường không đưa vào kho. Dạng bài gán theo câu giống nhất — chờ thầy duyệt.

Đã vào kho nhóm «Cuối kỳ I Toán 10». Giữa kỳ I đang chuyển tiếp: Trần Đình Cư đề 1–4 và đề 10 đã vào nhóm «Giữa kỳ I Toán 10» (đề 1: 23 câu, đề 2: 22, đề 3: 23, đề 4: 21, đề 10: 22).

| Mã | Trạng thái |
|---|---|
| `CK10-DH-01` … `CK10-DH-18` | Dương Hùng. Hầu hết 22 câu (12+4+6). Đề 3 còn 21 câu (phần 3 thiếu 1). Một số câu trùng web đã bỏ. Vài câu thiếu dòng «Chọn» nên cờ thiếu đáp án |
| `CK10-TDC-01` … `CK10-TDC-03` | Trần Đình Cư. 22 câu. File in đề hai lần; chỉ giữ bản có lời giải |
| `CK10-EB-01` … `CK10-EB-10` | Ebook. 19–22 câu. Vài đề thiếu 1–2 câu so với dòng «từ câu 1 đến câu 12» |
| `CK10-HCM-01` … `CK10-HCM-21` | Đề trường TP.HCM. Nhiều file không có bảng đáp án (cả đề gắn cờ thiếu đáp án — không tự điền). Đề 2 Võ Trường Toản: 25 trắc nghiệm, có bảng đáp án. Đề 8 Phú Nhuận: 12 trắc nghiệm + 4 đúng/sai có đáp án; 6 câu trả lời ngắn chưa tách (bảng: 0,8 / 1,75 / 10 / 22,1 / 42 / 28). Bỏ phần tự luận |
| `HK10-SP-01` … `HK10-SP-10` | GV Sư phạm. Đề 3, 4, 6, 9, 10 đủ 22 câu. Đề 5 tách được 16 câu. Đề 8 có 24 câu (phần 3 dư). Đề 1–2 còn 21 câu |

## Nguồn Word — Cuối kỳ I và Giữa kỳ I Toán 12

Nguồn: `TAI LIEU DANG WEB/Toán 12/Đề thi/L12-HK1` và `L12-GK1`. Chỉ lấy file có «Lời giải» trong tên (54 đề). Bỏ đề TP.HCM không có lời giải và phần tự luận. Dạng bài gán theo câu giống nhất — chờ thầy duyệt. Xem trên http://localhost:5180, nhóm «Cuối kỳ I Toán 12» và «Giữa kỳ I Toán 12».

| Mã | Trạng thái |
|---|---|
| `CK12-TV-01` … `CK12-TV-10` | Thư viện học liệu. 22–24 câu. Nhiều đề phần 2 có 5 câu trong khi đầu đề ghi 4 (đề 4 có 6). Đúng/sai thường cần xác nhận |
| `CK12-WT-01` … `CK12-WT-07` | Word Toán 2025. Đề 2–7 đủ khoảng 22 câu. Đề 1 chỉ tách được 13 (phần 1 có 6/12, phần 3 có 3/6) |
| `CK12-TDC-01` … `CK12-TDC-03` | Trần Đình Cư. Đủ 22 câu, gần như sạch |
| `HK12-SP-01` … `HK12-SP-19` | GV Sư phạm. Đề 2 treo MathType, chưa vào kho. Đề 5 chỉ 10 câu (phần 1 không tách được). Đề 16 chỉ 14 câu (phần 1 có 4/12). Còn lại khoảng 21–23 câu |
| `GK12-ST-01` … `GK12-ST-15` | Sưu tầm biên soạn, nhóm giữa kỳ. Đề 11 sạch (22 câu, 1 ảnh công thức). Đề 14 khá sạch. Đề 1–9 (trừ 11) hầu hết không tách được 4 phương án trắc nghiệm và thiếu đáp án «Chọn» — cần thầy xem, không tự điền |

## Nguồn Word — Kiểm tra theo bài Phan Nhật Linh (Toán 12 HK1)

Nguồn: `Bộ đề kiểm tra theo bài và cuối chương 12_HK1`. Chỉ lấy bản giáo viên `_GV`. Bỏ `_HS` và PDF. Chương 2 bài 3 dùng bản trong thư mục «Chỉnh lại». Tên đề: **Kiểm tra theo bài Phan Nhật Linh**. Nhóm cùng tên trên http://localhost:5180.

24 đề giáo viên chương 1–6 đã vào kho (20/10/2026). Không còn đề nào trong bộ này đang chờ chuyển công thức.

| Mã | Trạng thái |
|---|---|
| `C1KT-B01` | Bài 1. 21 câu. Vài đáp án lấy từ lời giải, cần xác nhận |
| `C1KT-B02` | Bài 2. 21 câu. 1 câu thiếu «Chọn», 6 câu trả lời ngắn cần xác nhận, 2 câu lệch `$` |
| `C1KT-B03` | Bài 3. 22 câu. 6 câu trả lời ngắn cần xác nhận |
| `C1KT-B04` | Bài 4. 22 câu. 2 câu trùng web bài khảo sát đồ thị. 1 câu thiếu «Chọn» |
| `C1KT-B05` | Bài 5. 20 câu. 1 câu trùng đề ôn tập giữa kỳ. 4 câu trả lời ngắn cần xác nhận |
| `C1KT-KS` | Khảo sát chương hàm số. 20 câu. 5 câu trả lời ngắn cần xác nhận, 2 câu lệch `$` |
| `C2KT-B01` | Vectơ. 21 câu. 5 câu trả lời ngắn cần xác nhận. 2 câu trùng web bài vectơ |
| `C2KT-B02` | Hệ tọa độ. 22 câu. 5 câu trả lời ngắn cần xác nhận. 7 câu trùng web (6 bài hệ tọa độ, 1 đề ôn tập giữa kỳ) |
| `C2KT-B03` | Biểu thức tọa độ, bản «Chỉnh lại». 21 câu. 5 câu trả lời ngắn cần xác nhận, 2 câu lệch `$` |
| `C2KT-KS` | Khảo sát chương vectơ. 22 câu. 1 trắc nghiệm lấy từ lời giải, 6 câu trả lời ngắn cần xác nhận, 2 câu lệch `$` |
| `C3KT-B01` | Chỉ tách được 16 câu. 3 câu không tách phương án, 1 đúng/sai thiếu mệnh đề |
| `C3KT-B02` | 15 câu, không cờ. Đề ngắn hơn khung 22 câu |
| `C3KT-KS` | Khảo sát. 18 câu. 1 đúng/sai thiếu đáp án, 2 câu trả lời ngắn cần xác nhận |
| `C4KT-B01` | 21 câu. 5 câu trả lời ngắn cần xác nhận, 2 câu lệch `$` |
| `C4KT-B02` | 22 câu. 6 câu trả lời ngắn cần xác nhận |
| `C4KT-B03` | Chỉ 10 câu. 5 câu trả lời ngắn cần xác nhận. Không phải đề đủ |
| `C4KT-KS` | Khảo sát. 21 câu. 5 câu trả lời ngắn cần xác nhận, 2 câu lệch `$` |
| `C5KT-B01` | 22 câu. 6 câu trả lời ngắn cần xác nhận |
| `C5KT-B02` | 18 câu. 5 câu trả lời ngắn cần xác nhận |
| `C5KT-B03` | Mặt cầu. 18 câu. 3 câu trả lời ngắn cần xác nhận, 1 công thức còn ảnh, lỗi công thức khi đưa lên web |
| `C5KT-KS` | Khảo sát phương pháp tọa độ. 19 câu. 5 câu trả lời ngắn cần xác nhận |
| `C6KT-B01` | Xác suất có điều kiện. 20 câu. 4 câu trả lời ngắn cần xác nhận, 1 đúng/sai thiếu đáp án |
| `C6KT-B02` | Xác suất toàn phần và Bayes. 22 câu. 6 câu trả lời ngắn cần xác nhận |
| `C6KT-KS` | Khảo sát chương xác suất. 22 câu. 6 câu trả lời ngắn cần xác nhận |

## Nguồn Word — 500 bài toán thực tế Phạm Minh Tuấn (Toán 12)

Nguồn: `500 BÀI THỰC TẾ PMT`. Chỉ file `(LỜI GIẢI) … TẬP n.docx`. Bỏ bản đề và PDF. Nhóm **500 bài toán thực tế Phạm Minh Tuấn** trên http://localhost:5180. Mỗi tập là một đề phần 3, trộn câu trả lời ngắn và câu đúng/sai.

Công thức trong khung «Đáp án» được chuyển thêm một lượt (MathType không thấy công thức trong khung chữ). Công thức còn là ảnh được đọc thành LaTeX trong `eq_ocr.json`.

Câu có bảng «Mệnh đề | Đúng | Sai» được tách thành câu đúng/sai a)–d). Đáp án lấy từ dấu X/Đ/S trong bảng của đề, nếu trống thì lấy kết luận trong lời giải; dấu trong bảng mâu thuẫn với lời giải sẽ bị gắn cờ (chưa có câu nào mâu thuẫn).

Đáp án trả lời ngắn lấy tự động từ cuối lời giải được rà lại bằng câu kết luận («Vậy … ≈ …»); các câu lệch đã giải lại và ghi trong `sua.json`. Bài nằm trong bảng «đề | hình» có đánh số «Bài n» được tách thành câu riêng; lời giải mở đầu «Phương pháp:» không có tiêu đề «Lời giải» cũng được nhận.

| Mã | Trạng thái |
|---|---|
| `PMT-T01` | Tập 1. 30 câu: 27 trả lời ngắn, 3 đúng/sai (16, 24, 28). Web đọc đủ. Câu 3: 12 nhãn hình (A′, B, C′, M, N, O, x, y, z…) đã đọc thành LaTeX; hình vẽ bằng nét Word đè lên ảnh nên chỉ giữ ảnh minh họa |
| `PMT-T02` | Tập 2. 30 câu: 21 trả lời ngắn, 9 đúng/sai (2, 3, 10, 18, 19, 27–30). Web đọc đủ |
| `PMT-T03` | Tập 3. 45 câu: 37 trả lời ngắn, 8 đúng/sai (6, 14, 15, 16, 22, 23, 39, 45). Một bài gõ tay «Câu 4:» giữa tập, đã đánh số liên tục. Câu 29 thiếu đáp án (không có ô đáp án, lời giải không ra số) |
| `PMT-T04` | Tập 4. 41 câu: 34 trả lời ngắn, 7 đúng/sai (17, 18, 24, 25, 26, 31, 32). Câu 10: ảnh công thức đọc thành $l$ |
| `PMT-T05` | Tập 5. 30 câu: 29 trả lời ngắn, 1 đúng/sai (14). Web đọc đủ |
| `PMT-T06` | Tập 6. 30 câu: 26 trả lời ngắn, 4 đúng/sai (1, 5, 10, 11). Khung «Đáp án» trống ở cả Word lẫn PDF: đáp án trả lời ngắn lấy từ cuối lời giải, cần thầy xác nhận cả tập. Câu 1 đã giải lại (S, Đ, S, Đ). Câu 4 (1,15) và câu 6 (8,42 phút) đã giải lại. Câu 7 thiếu đáp án (lời giải không ra số) |
| `PMT-T07` | Tập 7. 51 câu: 37 trả lời ngắn, 14 đúng/sai. Câu 6 và 10 dùng ký hiệu «$» cho đô la làm vỡ công thức: đã viết lại thành «đô la» và giải lại (câu 6 = 100; câu 10 Đ, Đ, Đ, S). Câu 32 ý c đã tính lại (Đúng). Câu 5 đã tính lại (3032 m) và bỏ phần lời giải bài khác dính vào; câu 8 = 6 điểm. Một bài xác suất «hệ thống an ninh 3 lớp» không đánh số trong Word (nằm sau câu 5) chưa vào kho. Câu 2: một ảnh công thức trống. Câu 7 và nhiều câu trả lời ngắn lấy đáp án từ cuối lời giải, cần xác nhận |
| `PMT-T08` | Tập 8. 35 câu trả lời ngắn. 44 ảnh công thức (câu 7 quãng đường X–M–N–Y, câu 26 lát gạch) đã đọc thành LaTeX từ `tex.docx`. Câu 33 đáp án tự động ra 0, đã giải lại: 18,4°. Câu 16: tháng thứ 18. 18 câu đáp án lấy từ cuối lời giải (1, 2, 4, 5, 6, 9, 15, 16, 18, 20, 21, 25, 27, 28, 30, 32, 34, 35), cần xác nhận |
| `PMT-T09` | Tập 9. 31 câu (web 30: câu 19 trùng tập 7 câu 6, đã bỏ): 24 trả lời ngắn, 7 đúng/sai. Câu 18 (8 cánh cửa sắt) nằm trong bảng, đã tách riêng. Câu 5, 7, 11, 15 đáp án tự động sai, đã giải lại (202,27; 0,124; 23,9; 574). Câu 22 đã giải lại (Đ, S, Đ, Đ) |
| `PMT-T10` | Tập 10. 30 câu: 20 trả lời ngắn, 10 đúng/sai. Web đọc đủ, không có ảnh công thức. Thẻ đáp án «<Key=…>» lộ trong đề (6 câu) đã chuyển thành đáp án. Câu 22, 23 kết luận dạng «(a) Đúng.» đã đọc được; đã tự kiểm tra lại |
| `PMT-T11` | Tập 11. 32 câu: 22 trả lời ngắn, 10 đúng/sai. Web đọc đủ, không có ảnh công thức. Các dòng hệ phương trình «x=t \\» mang số «Bài n» của Word từng bị tách thành 6 câu rỗng, đã gộp lại. Câu đúng/sai viết ý a)–d) thẳng trong đề (không kẻ bảng) đã nhận được. Câu 20 lời giải không ghi Đúng/Sai, đã giải lại (Đ, Đ, S, Đ) |
| `PMT-T12` | Tập 12. 29 câu: 21 trả lời ngắn, 8 đúng/sai; web 28 (câu 22 trùng web, đã bỏ). Không có ảnh công thức. Câu 5: đáp án đọc từ bảng «Câu \| a \| b \| c \| d» (S, S, Đ, Đ); lời giải gốc chỉ giải ý a. **Thầy xem ý d**: sách ghi Đúng «tốc độ giảm nhiệt độ tăng dần», nhưng $\|T'(t)\|=150e^{-2t}$ giảm dần — chỉ đúng nếu hiểu là $T'(t)$ tăng |
| `PMT-T13` | Tập 13. 27 câu: 22 trả lời ngắn, 5 đúng/sai. Web đọc đủ. Câu 8: ảnh công thức đọc thành $(D)$. Câu 21 đáp án trong bảng «\| a) \| Đúng \| lời giải \|» đã đọc được. Câu 27 ý b không có kết luận, đã giải lại (Đ, Đ, S, Đ) |
| `PMT-T14` | Tập 14. 47 câu: 34 trả lời ngắn, 13 đúng/sai. Web đọc đủ. Câu 1: công thức «${D(t)=…}$» bị Word ngắt thành đoạn có số «Bài n», bộ tách nay bỏ qua đoạn nằm giữa «${ … }$». Câu 3 đáp án 463 chiếc (462,344 làm tròn lên). Câu 42 ý d không có kết luận, đã giải lại (S, Đ, Đ, Đ) |
| `PMT-T15` | Tập 15. 30 câu: 23 trả lời ngắn, 7 đúng/sai. Web đọc đủ. Câu 3 là đúng/sai a)–d) bị đọc thành trả lời ngắn, đã đổi dạng qua sua.json (S, Đ, S, S). Câu 17 ý d theo bảng đáp án (Đ). Câu 27 lời giải bỏ trống kết quả, đã giải lại OM ≈ 34,1 m và viết lại lời giải |
| `PMT-T16` | Tập 16. 25 câu: 15 trả lời ngắn, 10 đúng/sai. Web đọc đủ. MathType chuyển rỗng khoảng 30 công thức trong lời giải (câu 1, 5, 7, 10, 14, 15, 16, 18, 22, 23, 24): đã điền lại theo ảnh xem trước trong file gốc và giải lại. Câu 11 và 24: ý c nằm sau ảnh trên cùng dòng nên bị gộp vào ý trước, bộ đọc đã sửa. **Câu 11 ý d cần thầy xem**: sách ghi Sai nhưng chính lời giải tính ra ≈ 20,6 ≈ 21 giây, trùng mệnh đề → đang để Đúng. Câu 25 ghi rõ đơn vị nghìn đồng (đáp án 585). Tập 15 câu 28 cũng mất công thức (*), (**), đã viết lại |

## Nguồn PDF — Lê Minh Kha «Ôn thi THPT QG 2026 môn Toán» (lớp 12)
- ✅ `LMK-ON THI THPT 2026`: 525 câu (300 trắc nghiệm, 100 Đúng/Sai, 125 Trả lời ngắn; 15 đề giả lập theo thứ tự câu). Đáp án đối chiếu sách (`dapan_sach.json`): trắc nghiệm khớp 300/300; Đúng/Sai lệch ở 32, 95, 99, 100 (soát lại) và thiếu đáp án sách ở 41, 42, 70, 71, 90, 92–94. Trả lời ngắn lấy đáp án cuối lời giải sách.
- Skill đóng gói: `docs/kho-de/skill-chuyen-doi/SKILL.md`.

## Rà soát toàn kho (07/10/2026)
- Đã sửa: 17 câu trắc nghiệm trùng phương án, 11 câu mất dấu «−» khi chuyển công thức, 6 câu đáp án chữ → trắc nghiệm/đáp án ngắn, 5 lỗi bộ Import web đọc nhầm, ~50 đáp án trả lời ngắn điền sai (lấy nhầm số cuối lời giải), 2 câu bỏ (trùng web / đáp án là văn bản).
- Bẫy bộ Import web: đáp án ngắn chỉ gồm 1 chữ a–d bị hiểu là chữ cái phương án → viết «a|$a$»; dòng lời giải bắt đầu «Phương án A:» làm mất phương án → dùng «Xét (A):».
- `kho_de_data/CAU_TRUNG_TRONG_KHO.md`: 213 câu trùng nội dung trong kho (chưa xoá).
- LMK: câu Đúng/Sai và trả lời ngắn chưa có lời giải (sách có, chưa chép).

## Rà soát THCS lớp 6-9 — muse (20/10/2026)
- Người nhận: **muse** — đợt rà soát lại toàn bộ 130 câu lỗi nghiêm trọng đã phát hiện ở khối THCS (báo cáo rà soát trước đó), đối chiếu với VIEC_CAN_LAM.md.
- Đã ghi vào `sua.json`: sửa 48 câu (đổi/thêm đáp án, sửa phương án, mẫu điền, lời giải, câu chữ mất ký hiệu), ghi `ghi_chu` 57 câu chờ thầy xem (đề có hai phương án cùng đúng, không có phương án đúng, thiếu dữ kiện — cần sửa bản đề gốc). Mọi entry đều có `sua_boi: muse`, entry sửa kèm `ly_do`.
- 25 câu còn lại trong danh sách đã có sẵn entry của grokbot/claude trong sua.json: giữ nguyên theo quy định, muse chỉ kiểm chứng (21 câu đáp án đã khớp nhưng lời giải trong entry vẫn còn dòng tính sai; chi tiết trong PR).
- Nhánh: `ai/muse-2026-10-20` (PR vào main). Không sửa file nào trong `de/`.

## Soat co VIEC_CAN_LAM — muse (27/10/2026)

- Nguoi nhan: **muse** — soat 841 cau co cua 4 bai nhieu co nhat: LMK-ON THI THPT 2026 (518), TTT-C3-ON CHUONG 3 (110), TTT-C1-ON CHUONG 1 (108), TTT-C2-ON CHUONG 2 (105). Tat ca chi mang co dap_an_tu_giai_can_xac_nhan.
- Ket qua: 820 khoa moi trong sua.json (788 xac_nhan, 2 sua, 30 ghi_chu); 21 cau da co entry san giu nguyen. 2 cau sua: TTT-C2 de1.P2.C14 (tf_ans y d true → false), LMK de9.P2.C67 (tf_ans y c true → false).
- Nhanh: `ai/muse-2026-10-27` (PR vao main). Khong sua file nao trong `de/`.
