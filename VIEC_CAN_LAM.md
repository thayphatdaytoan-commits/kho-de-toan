# Việc cần làm (tự sinh mỗi lần đẩy kho — đừng sửa tay)

Cập nhật: 2026-10-21 23:56. Kho có 19,496 câu; **4,032 câu còn cờ** cần xem. Danh sách đầy đủ (lớp, bài, file đề, mã câu, cờ) ở `viec_can_lam.json`. Cách sửa: `HUONG_DAN_AI.md`.

## Theo loại cờ

| Cờ | Số câu | Nghĩa / việc cần làm |
|---|---|---|
| `dap_an_tu_giai_can_xac_nhan` | 1297 | đề gốc không có đáp án, máy tự giải → giải lại, đúng thì xac_nhan |
| `import_web` | 691 | bộ import của web báo lỗi (thiếu đáp án, sai định dạng…) → sửa trường tương ứng |
| `dap_an_ngan_lay_tu_cuoi_loi_giai_can_xac_nhan` | 539 | đáp án trả lời ngắn lấy từ cuối lời giải → kiểm lại |
| `thieu_dap_an_Chon_X` | 383 | trắc nghiệm thiếu dòng «Chọn X» → giải và ghi answer |
| `dap_an_suy_tu_loi_giai_can_xac_nhan` | 338 | đáp án suy ra từ lời giải → kiểm lại |
| `dung_sai_suy_tu_loi_giai_can_xac_nhan` | 295 | đáp án đúng/sai suy từ lời giải → kiểm từng ý |
| `cong_thuc_ocr_AI_can_xem` | 222 | công thức do AI đọc ảnh → so với ảnh, sửa nếu sai |
| `dung_sai_thieu_dap_an` | 209 | đúng/sai thiếu đáp án → giải, ghi tf_ans |
| `khong_tach_duoc_4_phuong_an` | 192 | không tách được 4 phương án → ghi options (4 chuỗi) |
| `tn_y_a_tu_tu_luan_can_xac_nhan` | 168 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `muc_do_NB_lech_xa_goi_y_vi_tri_VD` | 141 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_b_tu_tu_luan_can_xac_nhan` | 137 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_ngan_trong_va_loi_giai_khong_ra_so` | 122 | trả lời ngắn chưa có số → giải, ghi short_correct |
| `dung_sai_thieu_y` | 73 | đúng/sai thiếu ý → bổ sung tf hoặc ghi ghi_chu |
| `dung_sai_tu_bang_menh_de_can_xac_nhan` | 64 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `cong_thuc_dang_anh_chua_OCR` | 58 | công thức còn là ảnh → đọc ảnh, ghi LaTeX vào eq_ocr.json |
| `tn_y_c_tu_tu_luan_can_xac_nhan` | 48 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `le_dau_dollar` | 41 | số dấu $ bị lẻ → sửa LaTeX |
| `loi_giai_y_b_do_AI_tu_giai_can_duyet` | 38 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_tu_tu_luan_dap_an_nhieu_can_xac_nhan` | 38 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dung_sai_tu_y_abcd_trong_de_can_xac_nhan` | 36 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_a_do_AI_tu_giai_can_duyet` | 32 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_la_bieu_thuc_can_quy_uoc_cach_cham` | 22 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_d_tu_tu_luan_can_xac_nhan` | 15 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_D_dung_nhung_chon_C` | 13 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_do_AI_tu_giai_can_duyet` | 13 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_C_dung_nhung_chon_D` | 12 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_A_dung_nhung_chon_C` | 10 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_B_dung_nhung_chon_C` | 10 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `katex` | 10 | công thức không hiển thị được bằng KaTeX → sửa LaTeX |
| `con_cong_thuc_MathType_chua_chuyen` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_A_dung_nhung_chon_D` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_B_dung_nhung_chon_D` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_c_do_AI_tu_giai_can_duyet` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_ngan_khong_phai_so` | 8 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `phuong_an_rong` | 6 | có phương án rỗng → bổ sung |
| `dap_an_bang_dap_an_B_khac_A` | 6 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `thieu_de_chung` | 5 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_2a_tu_tu_luan_can_xac_nhan` | 5 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_2b_tu_tu_luan_can_xac_nhan` | 5 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_B_khac_D` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_C_khac_A` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_D_dung_nhung_chon_B` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_1a_tu_tu_luan_can_xac_nhan` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_1b_tu_tu_luan_can_xac_nhan` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_D_dung_nhung_chon_A` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_A_dung_nhung_chon_B` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_2c_tu_tu_luan_can_xac_nhan` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_B_dung_nhung_chon_A` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_B_khac_C` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_D_khac_C` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_C_dung_nhung_chon_B` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_A_khac_D` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_A_tu_tu_luan_can_xac_nhan` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_B_tu_tu_luan_can_xac_nhan` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_C_tu_tu_luan_can_xac_nhan` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_d_do_AI_tu_giai_can_duyet` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_A_khac_C` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_D_khac_A` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_C_dung_nhung_chon_A` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_D_tu_tu_luan_can_xac_nhan` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_e_tu_tu_luan_can_xac_nhan` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_1_tu_tu_luan_can_xac_nhan` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |

## Bài nhiều cờ nhất (làm trước)

| Lớp | Bài | Câu có cờ |
|---|---|---|
| 12 | `LMK-ON THI THPT 2026` | 518 |
| 12 | `TTT-C3-ON CHUONG 3` | 110 |
| 12 | `TTT-C1-ON CHUONG 1` | 108 |
| 12 | `TTT-C2-ON CHUONG 2` | 105 |
| 10 | `GK10-STR-02` | 43 |
| 11 | `C6-B3 - HAM SO MU VA HAM SO LOGARIT` | 32 |
| 11 | `C6-B2 - PHEP TINH LOGARIT` | 31 |
| 12 | `C3-B1` | 29 |
| 10 | `CK10-HCM-06` | 27 |
| 11 | `C9-B1-BIEN CO GIAO VA QUY TAC NHAN XAC SUAT` | 27 |
| 12 | `PMT-T06` | 27 |
| 11 | `C9-B2-BIEN CO HOP VA QUY TAC CONG XAC SUAT` | 26 |
| 12 | `PMT-T07` | 23 |
| 10 | `CK10-HCM-01` | 22 |
| 10 | `CK10-HCM-03` | 22 |
| 10 | `CK10-HCM-09` | 22 |
| 10 | `CK10-HCM-15` | 22 |
| 10 | `CK10-HCM-20` | 22 |
| 11 | `C8-BAI TAP CUOI CHUONG` | 22 |
| 11 | `GK11-TDC-03` | 22 |
| 12 | `GK12-ST-02` | 22 |
| 10 | `CK10-HCM-10` | 21 |
| 11 | `C8-B4-KHOANG CACH TRONG KHONG GIAN` | 21 |
| 12 | `GK12-ST-09` | 21 |
| 10 | `CK10-HCM-12` | 20 |
| 10 | `CK10-HCM-17` | 20 |
| 11 | `C6-BAI TAP CUOI CHUONG 6` | 20 |
| 11 | `C9-BAI TAP CUOI CHUONG` | 20 |
| 12 | `C2-ON CHUONG 2` | 20 |
| 12 | `GK12-ST-03` | 20 |
| 12 | `GK12-ST-04` | 20 |
| 12 | `PMT-T14` | 20 |
| 10 | `GK10-STR-01` | 19 |
| 12 | `GK12-ST-05` | 19 |
| 12 | `GK12-ST-06` | 19 |
| 12 | `GK12-ST-07` | 19 |
| 10 | `CK10-HCM-16` | 18 |
| 11 | `C6-B4 - PHUONG TRINH - BAT PHUONG TRINH MU VA LOGARIT` | 18 |
| 12 | `GK12-ST-01` | 17 |
| 12 | `PMT-T08` | 17 |
| 10 | `CK10-HCM-13` | 16 |
| 10 | `CK10-HCM-14` | 16 |
| 12 | `GK12-ST-08` | 16 |
| 8 | `DT8GK1-06-DE GK1 THAM KHAO 8 - TINH NGUYEN` | 16 |
| 8 | `DT8GK1-09-KTGHK1_T8_HIEP BINH - NGUYEN THI THANH TUYEN` | 16 |
| 12 | `C4-B1-NGUYEN HAM` | 15 |
| 12 | `PMT-T09` | 15 |
| 8 | `DT8GK1-25-DE TK GIUA HK1 TOAN 8 THCS BINH THO - NGUYEN HON` | 15 |
| 12 | `C3-ON TAP CHUONG 3` | 14 |
| 12 | `PMT-T11` | 14 |
| 8 | `DT8CK2-05-KIEN THIET` | 14 |
| 8 | `DT8GK1-19-TOAN 8 - GHK1 - NGUYEN THI MY LOAN` | 14 |
| 8 | `DT8GK1-20-TOAN 8 GHK1 - THCS TRUONG THANH - 5. TRAN VAN LO` | 14 |
| 8 | `DT8GK1-24-DE THAM KHAO GIUA HK1 - HUNG TRUONG` | 14 |
| 8 | `DT8GK1-29-DE TK TOAN 8 GHK 1 THCS THAI VAN LUNG - CUC NGUY` | 14 |
| 10 | `CK10-HCM-07` | 13 |
| 10 | `HK10-SP-01` | 13 |
| 11 | `GK11-NBV-05` | 13 |
| 12 | `C4-ON TAP CHUONG 4` | 13 |
| 12 | `C6-B2-CONG THUC XAC SUAT TOAN PHAN - BAYES` | 13 |

## 6 ảnh đề nhắc tới nhưng không có file

Câu dùng ảnh này hiển thị thiếu hình. Không tự vẽ lại; ghi `ghi_chu` trong `sua.json` để thầy xử lý.

- lop12/CK12-WT-01/de1.json: image34.wmf
- lop6/DT6CK2-07-RD6_HKII_2425/de1.json: image4.png
- lop7/DT7CK1-03-CKI-7-34-BQT/de1.json: image9.png
- lop8/DT8CK2-08-LE LOI/de1.json: image7.png
- lop8/DT8CK2-08-LE LOI/de1.json: image8.png
- lop9/DT9TK2-15-TQT-TKCK2-TOAN 9 (2024-2025)/de1.json: image4.emf
