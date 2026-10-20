# Việc cần làm (tự sinh mỗi lần đẩy kho — đừng sửa tay)

Cập nhật: 2026-10-20 16:02. Kho có 19,496 câu; **3,924 câu còn cờ** cần xem. Danh sách đầy đủ (lớp, bài, file đề, mã câu, cờ) ở `viec_can_lam.json`. Cách sửa: `HUONG_DAN_AI.md`.

## Theo loại cờ

| Cờ | Số câu | Nghĩa / việc cần làm |
|---|---|---|
| `dap_an_tu_giai_can_xac_nhan` | 1105 | đề gốc không có đáp án, máy tự giải → giải lại, đúng thì xac_nhan |
| `import_web` | 692 | bộ import của web báo lỗi (thiếu đáp án, sai định dạng…) → sửa trường tương ứng |
| `dap_an_ngan_lay_tu_cuoi_loi_giai_can_xac_nhan` | 539 | đáp án trả lời ngắn lấy từ cuối lời giải → kiểm lại |
| `thieu_dap_an_Chon_X` | 391 | trắc nghiệm thiếu dòng «Chọn X» → giải và ghi answer |
| `dap_an_suy_tu_loi_giai_can_xac_nhan` | 338 | đáp án suy ra từ lời giải → kiểm lại |
| `dung_sai_suy_tu_loi_giai_can_xac_nhan` | 295 | đáp án đúng/sai suy từ lời giải → kiểm từng ý |
| `cong_thuc_ocr_AI_can_xem` | 222 | công thức do AI đọc ảnh → so với ảnh, sửa nếu sai |
| `dung_sai_thieu_dap_an` | 209 | đúng/sai thiếu đáp án → giải, ghi tf_ans |
| `khong_tach_duoc_4_phuong_an` | 192 | không tách được 4 phương án → ghi options (4 chuỗi) |
| `tn_y_a_tu_tu_luan_can_xac_nhan` | 179 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `muc_do_NB_lech_xa_goi_y_vi_tri_VD` | 152 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_b_tu_tu_luan_can_xac_nhan` | 145 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_ngan_trong_va_loi_giai_khong_ra_so` | 122 | trả lời ngắn chưa có số → giải, ghi short_correct |
| `cong_thuc_dang_anh_chua_OCR` | 90 | công thức còn là ảnh → đọc ảnh, ghi LaTeX vào eq_ocr.json |
| `dung_sai_thieu_y` | 73 | đúng/sai thiếu ý → bổ sung tf hoặc ghi ghi_chu |
| `dung_sai_tu_bang_menh_de_can_xac_nhan` | 64 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_c_tu_tu_luan_can_xac_nhan` | 54 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `le_dau_dollar` | 42 | số dấu $ bị lẻ → sửa LaTeX |
| `loi_giai_y_b_do_AI_tu_giai_can_duyet` | 42 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_tu_tu_luan_dap_an_nhieu_can_xac_nhan` | 38 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dung_sai_tu_y_abcd_trong_de_can_xac_nhan` | 36 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_a_do_AI_tu_giai_can_duyet` | 34 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_la_bieu_thuc_can_quy_uoc_cach_cham` | 25 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_do_AI_tu_giai_can_duyet` | 19 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_d_tu_tu_luan_can_xac_nhan` | 16 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_D_dung_nhung_chon_C` | 13 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_C_dung_nhung_chon_D` | 12 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_c_do_AI_tu_giai_can_duyet` | 12 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_A_dung_nhung_chon_C` | 10 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_B_dung_nhung_chon_C` | 10 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `katex` | 10 | công thức không hiển thị được bằng KaTeX → sửa LaTeX |
| `con_cong_thuc_MathType_chua_chuyen` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_A_dung_nhung_chon_D` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_B_dung_nhung_chon_D` | 9 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_ngan_khong_phai_so` | 8 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `phuong_an_rong` | 7 | có phương án rỗng → bổ sung |
| `dap_an_bang_dap_an_B_khac_A` | 6 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_C_khac_A` | 6 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `thieu_de_chung` | 5 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_2a_tu_tu_luan_can_xac_nhan` | 5 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_2b_tu_tu_luan_can_xac_nhan` | 5 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_B_khac_D` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_D_dung_nhung_chon_B` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_1a_tu_tu_luan_can_xac_nhan` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_1b_tu_tu_luan_can_xac_nhan` | 4 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_D_dung_nhung_chon_A` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_A_dung_nhung_chon_B` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_B_khac_C` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_D_khac_C` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_A_khac_D` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_2c_tu_tu_luan_can_xac_nhan` | 3 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_B_dung_nhung_chon_A` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_C_dung_nhung_chon_B` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_A_tu_tu_luan_can_xac_nhan` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_B_tu_tu_luan_can_xac_nhan` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_C_tu_tu_luan_can_xac_nhan` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_d_do_AI_tu_giai_can_duyet` | 2 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_A_khac_C` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_D_khac_A` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_noi_C_dung_nhung_chon_A` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `dap_an_bang_dap_an_A_khac_B` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `tn_y_D_tu_tu_luan_can_xac_nhan` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_A_do_AI_tu_giai_can_duyet` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
| `loi_giai_y_B_do_AI_tu_giai_can_duyet` | 1 | xem câu, sửa nếu sai; đúng rồi thì xac_nhan |
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
| 8 | `DT8GK1-06-DE GK1 THAM KHAO 8 - TINH NGUYEN` | 17 |
| 10 | `CK10-HCM-13` | 16 |
| 10 | `CK10-HCM-14` | 16 |
| 12 | `GK12-ST-08` | 16 |
| 8 | `DT8GK1-09-KTGHK1_T8_HIEP BINH - NGUYEN THI THANH TUYEN` | 16 |
| 12 | `C4-B1-NGUYEN HAM` | 15 |
| 12 | `PMT-T09` | 15 |
| 8 | `DT8GK1-19-TOAN 8 - GHK1 - NGUYEN THI MY LOAN` | 15 |
| 8 | `DT8GK1-24-DE THAM KHAO GIUA HK1 - HUNG TRUONG` | 15 |
| 8 | `DT8GK1-25-DE TK GIUA HK1 TOAN 8 THCS BINH THO - NGUYEN HON` | 15 |
| 8 | `DT8GK1-28-DE TK TOAN 8 GHKI_ THCS TAN PHU - LUU TO UYEN` | 15 |
| 8 | `DT8GK1-30-DE TK TOAN 8 GHK1 _THCS LINH DONG - DUC DUONG` | 15 |
| 12 | `C3-ON TAP CHUONG 3` | 14 |
| 12 | `PMT-T11` | 14 |
| 7 | `DT7GK1-03-7 COLETTE` | 14 |
| 8 | `DT8GK1-03-24_25_GOT_TOAN 8_DE THAM KHAO_GHKI - PHAN THANH` | 14 |
| 8 | `DT8GK1-05-DEGIUAHKI-TOAN8-2024-2025 - TRAN HUY` | 14 |
| 8 | `DT8GK1-12-T8-GIUA HKI 24-25 - PHUOC TRAN` | 14 |
| 8 | `DT8GK1-16-THCS BINHAN_TOAN 8_DETK_GKI 24_25 - HUONG VO KIM` | 14 |
| 8 | `DT8GK1-20-TOAN 8 GHK1 - THCS TRUONG THANH - 5. TRAN VAN LO` | 14 |

## 370 ảnh đề nhắc tới nhưng không có file

Câu dùng ảnh này hiển thị thiếu hình. Không tự vẽ lại; ghi `ghi_chu` trong `sua.json` để thầy xử lý.

- lop10/C2-B1-BPT BAC NHAT HAI AN/de3.json: image54.emf
- lop10/C2-B3-ON TAP CUOI CHUONG 2/de2.json: image31.emf
- lop10/C2-B3-ON TAP CUOI CHUONG 2/de2.json: image30.emf
- lop10/C2-B3-ON TAP CUOI CHUONG 2/de2.json: image32.png
- lop10/C2-B3-ON TAP CUOI CHUONG 2/de2.json: image35.emf
- lop10/C3-B1-GIA TRI LUONG GIAC CUA MOT GOC/de1.json: image15.png
- lop10/C4-B1-KHAI NIEM VECTO/de3.json: image52.png
- lop10/C4-B1-KHAI NIEM VECTO/de3.json: image50.png
- lop10/C5-B3-CAC SO DAC TRUNG DO DO PHAN TAN/de1.json: image11.png
- lop10/C6-B4-PT QUY VE PT BAC HAI/de3.json: image18.png
- lop10/C6-B5-ON TAP CHUONG 6/de2.json: image23.png
- lop10/CK10-DH-03/de1.json: image5.png
- lop10/CK10-DH-04/de1.json: image15.emf
- lop10/CK10-DH-07/de1.json: image8.emf
- lop10/CK10-DH-10/de1.json: image10.png
- lop10/CK10-DH-10/de1.json: image12.emf
- lop10/CK10-DH-13/de1.json: image12.png
- lop10/CK10-DH-15/de1.json: image5.png
- lop10/CK10-DH-17/de1.json: image3.png
- lop10/CK10-EB-01/de1.json: image6.png
- lop10/CK10-EB-02/de1.json: image6.png
- lop10/CK10-EB-07/de1.json: image16.png
- lop10/CK10-EB-08/de1.json: image14.tmp
- lop10/CK10-EB-09/de1.json: image3.png
- lop10/CK10-EB-09/de1.json: image11.emf
- lop10/CK10-EB-10/de1.json: image49.png
- lop10/CK10-EB-10/de1.json: image35.emf
- lop10/CK10-HCM-06/de1.json: image1.png
- lop10/CK10-HCM-06/de1.json: image14.png
- lop10/CK10-HCM-06/de1.json: image4.png
- lop10/CK10-HCM-06/de1.json: image13.emf
- lop10/CK10-HCM-06/de1.json: image2.png
- lop10/CK10-HCM-13/de1.json: image18.png
- lop10/CK10-HCM-18/de1.json: image4.png
- lop10/CK10-TDC-01/de1.json: image4.png
- lop10/GK10-NBV-03/de1.json: image7.emf
- lop10/GK10-NBV-05/de1.json: image2.png
- lop10/GK10-STR-02/de1.json: image20.png
- lop10/GK10-TDC-04/de1.json: image10.png
- lop10/GK10-TDC-06/de1.json: image5.png
- lop10/GK10-TDC-09/de1.json: image7.png
- lop10/GKF10-03-GK 2 TOAN 10 - AN MAMA/de1.json: image2.png
- lop10/HK10-SP-02/de1.json: image8.png
- lop10/HK10-SP-10/de1.json: image6.png
- lop11/C1-B3-HAM SO LUONG GIAC VA DO THI/de3.json: image17.png
- lop11/C4-B1-DIEM, DUONG THANG VA MAT PHANG/de2.json: image40.emf
- lop11/C4-B1-DIEM, DUONG THANG VA MAT PHANG/de2.json: image36.emf
- lop11/C4-B1-DIEM, DUONG THANG VA MAT PHANG/de3.json: image57.png
- lop11/C4-B1-DIEM, DUONG THANG VA MAT PHANG/de3.json: image60.png
- lop11/C4-B2-HAI DUONG THANG SONG SONG/de1.json: image21.png
- lop11/C4-B2-HAI DUONG THANG SONG SONG/de2.json: image36.png
- lop11/C4-B3-DUONG THANG SONG SONG VOI MAT PHANG/de1.json: image16.png
- lop11/C4-B3-DUONG THANG SONG SONG VOI MAT PHANG/de2.json: image39.emf
- lop11/C4-B3-DUONG THANG SONG SONG VOI MAT PHANG/de3.json: image61.png
- lop11/C4-B4-HAI MAT PHANG SONG SONG/de1.json: image22.png
- lop11/C4-B4-HAI MAT PHANG SONG SONG/de2.json: image39.emf
- lop11/C4-B4-HAI MAT PHANG SONG SONG/de2.json: image41.png
- lop11/C4-B5-PHEP CHIEU SONG SONG/de1.json: image16.png
- lop11/C6-B3 - HAM SO MU VA HAM SO LOGARIT/de2.json: image22.png
- lop11/C6-B3 - HAM SO MU VA HAM SO LOGARIT/de2.json: image23.png
- lop11/C6-B3 - HAM SO MU VA HAM SO LOGARIT/de2.json: image21.png
- lop11/C6-B3 - HAM SO MU VA HAM SO LOGARIT/de2.json: image20.png
- lop11/C6-BAI TAP CUOI CHUONG 6/de1.json: image28.png
- lop11/C6-BAI TAP CUOI CHUONG 6/de1.json: image29.png
- lop11/C7-B2-CAC QUY TAC TINH DAO HAM/de2.json: image13.png
- lop11/C8-B1-HAI DUONG THANG VUONG GOC/de1.json: image29.png
- lop11/C8-B1-HAI DUONG THANG VUONG GOC/de1.json: image30.png
- lop11/C8-B1-HAI DUONG THANG VUONG GOC/de3.json: image68.png
- lop11/C8-B3-HAI MAT PHANG VUONG GOC/de1.json: image29.png
- lop11/C8-B3-HAI MAT PHANG VUONG GOC/de1.json: image30.png
- lop11/C8-B3-HAI MAT PHANG VUONG GOC/de2.json: image41.png
- lop11/C8-B3-HAI MAT PHANG VUONG GOC/de2.json: image33.png
- lop11/C8-B4-KHOANG CACH TRONG KHONG GIAN/de1.json: image30.tmp
- lop11/C8-B4-KHOANG CACH TRONG KHONG GIAN/de1.json: image29.tmp
- lop11/C8-B4-KHOANG CACH TRONG KHONG GIAN/de2.json: image39.png
- lop11/C8-B4-KHOANG CACH TRONG KHONG GIAN/de2.json: image49.emf
- lop11/C8-B4-KHOANG CACH TRONG KHONG GIAN/de2.json: image48.emf
- lop11/C8-BAI TAP CUOI CHUONG/de2.json: image63.tmp
- lop11/C8-BAI TAP CUOI CHUONG/de2.json: image33.png
- lop11/C8-BAI TAP CUOI CHUONG/de2.json: image38.emf
- lop11/C8-BAI TAP CUOI CHUONG/de3.json: image80.emf
- lop11/CK11-DH-03/de1.json: image4.png
- lop11/CK11-EB-01/de1.json: image11.png
- lop11/CK11-EB-02/de1.json: image4.png
- lop11/CK11-EB-04/de1.json: image7.png
- lop11/CK11-EB-09/de1.json: image7.png
- lop11/CK11-EB-10/de1.json: image10.png
- lop11/CK11-VN-01/de1.json: image13.jpeg
- lop11/CK11-VN-05/de1.json: image7.png
- lop11/CK11-VN-05/de1.json: image4.png
- lop11/CK11-VN-05/de1.json: image2.png
- lop11/GK11-02-DE 2/de1.json: image12.png
- lop11/GK11-08-DE 8/de1.json: image4.png
- lop11/GK11-08-DE 8/de1.json: image5.png
- lop11/GK11-TDC-10/de1.json: image6.emf
- lop11/GKF11-07-TO 7. DOT 8. DE GK2.CCST 11-DE 1 - AN MAMA/de1.json: image9.png
- lop11/GKF11-07-TO 7. DOT 8. DE GK2.CCST 11-DE 1 - AN MAMA/de1.json: image8.png
- lop11/HK11-SP-04/de1.json: image1.png
- lop11/HK11-SP-04/de1.json: image3.jpeg
- lop11/HK11-SP-08/de1.json: image1.png
- lop11/HK11-SP-08/de1.json: image3.emf
- lop11/HK11-SP-08/de1.json: image2.jpeg
- lop11/HK11-SP-09/de1.json: image2.png
- lop12/C1-B1/de1.json: image21.emf
- lop12/C1-B1/de1.json: image20.emf
- lop12/C1-B2/de2.json: image39.png
- lop12/C1-B2/de3.json: image49.png
- lop12/C1-B2/de3.json: image43.emf
- lop12/C1-B2/de3.json: image47.png
- lop12/C1-B4/de2.json: image36.png
- lop12/C1-B4/de3.json: image63.png
- lop12/C1-ON CHUONG 1/de1.json: image13.emf
- lop12/C1-ON CHUONG 1/de1.json: image25.png
- lop12/C1-ON CHUONG 1/de1.json: image21.emf
- lop12/C1-ON CHUONG 1/de1.json: image14.emf
- lop12/C1-ON CHUONG 1/de1.json: image11.emf
- lop12/C1-ON CHUONG 1/de1.json: image17.png
- lop12/C1-ON CHUONG 1/de3.json: image55.png
- lop12/C1-ON CHUONG 1/de3.json: image65.png
- lop12/C1-ON CHUONG 1/de3.json: image66.png
- lop12/C1KT-B01/de1.json: image8.png
- lop12/C1KT-B02/de1.json: image14.jpeg
- lop12/C1KT-B02/de1.json: image2.png
- lop12/C1KT-B04/de1.json: image14.png
- lop12/C1KT-B04/de1.json: image6.png
- lop12/C1KT-B04/de1.json: image5.png
- lop12/C1KT-B05/de1.json: image2.png
- lop12/C2-B1/de1.json: image23.emf
- lop12/C2-B1/de2.json: image43.emf
- lop12/C2-B1/de2.json: image50.emf
- lop12/C2-B2/de1.json: image19.jpg
- lop12/C2-B2/de2.json: image26.png
- lop12/C2KT-B02/de1.json: image6.png
- lop12/C2KT-B02/de1.json: image5.png
- lop12/C3-B2/de2.json: image14.png
- lop12/C4-B3- UNG DUNG HH TICH PHAN/de1.json: image22.png
- lop12/C4-B3- UNG DUNG HH TICH PHAN/de1.json: image21.jpeg
- lop12/C4-ON TAP CHUONG 4/de3.json: image49.jpeg
- lop12/C4KT-B03/de1.json: image6.png
- lop12/C4KT-B03/de1.json: image13.png
- lop12/C4KT-KS/de1.json: image9.png
- lop12/C4KT-KS/de1.json: image11.png
- lop12/C5-B3- CONG THUC TINH GOC TRONG KHONG GIAN/de3.json: image28.png
- lop12/C5KT-B02/de1.json: image2.png
- lop12/C5KT-B03/de1.json: image7.png
- lop12/C5KT-B03/de1.json: image3.jpeg
- lop12/C5KT-B03/de1.json: image8.png
- lop12/C5KT-B03/de1.json: image4.jpeg
- lop12/C5KT-B03/de1.json: image5.png
- lop12/CK12-TDC-03/de1.json: image7.png
- lop12/CK12-TV-01/de1.json: image14.png
- lop12/CK12-TV-01/de1.json: image15.png
- lop12/CK12-TV-01/de1.json: image17.png
- lop12/CK12-TV-01/de1.json: image8.png
- lop12/CK12-TV-01/de1.json: image13.png
- lop12/CK12-TV-03/de1.json: image1.png
- lop12/CK12-TV-03/de1.json: image9.png
- lop12/CK12-TV-04/de1.json: image3.png
- lop12/CK12-TV-04/de1.json: image2.png
- lop12/CK12-TV-05/de1.json: image9.png
- lop12/CK12-TV-05/de1.json: image13.emf
- lop12/CK12-TV-06/de1.json: image6.png
- lop12/CK12-TV-06/de1.json: image13.emf
- lop12/CK12-TV-06/de1.json: image7.png
- lop12/CK12-TV-07/de1.json: image8.png
- lop12/CK12-TV-08/de1.json: image7.png
- lop12/CK12-TV-08/de1.json: image5.png
- lop12/CK12-TV-09/de1.json: image8.emf
- lop12/CK12-TV-09/de1.json: image10.emf
- lop12/CK12-TV-10/de1.json: image6.png
- lop12/CK12-WT-01/de1.json: image36.png
- lop12/CK12-WT-01/de1.json: image34.wmf
- lop12/CK12-WT-02/de1.json: image6.png
- lop12/CK12-WT-03/de1.json: image1.png
- lop12/CK12-WT-06/de1.json: image5.png
- lop12/DT26-00-DE KSCL-THPT LE THANH TONG-HCM/de1.json: image17.png
- lop12/DT26-04-KSCL THPT -LIEN CAP DAI HOC HONG DUC/de1.json: image4.png
- lop12/DT26-11-THPT NGUYEN KHUYEN - BINH DUONG/de1.json: image1.png
- lop12/DT26-13-KSCL THPT NGUYEN KHUYEN - LTT - TPHCM/de1.json: image10.png
- lop12/DT26-13-KSCL THPT NGUYEN KHUYEN - LTT - TPHCM/de1.json: image4.png
- lop12/DT26-13-KSCL THPT NGUYEN KHUYEN - LTT - TPHCM/de1.json: image11.png
- lop12/DT26-13-KSCL THPT NGUYEN KHUYEN - LTT - TPHCM/de1.json: image16.emf
- lop12/DT26-14-SO NINH BINH-L1/de1.json: image6.png
- lop12/DT26-14-SO NINH BINH-L1/de1.json: image11.png
- lop12/DT26-16-CHUYEN HA LONG - QUANG NINH/de1.json: image10.png
- lop12/DT26-16-CHUYEN HA LONG - QUANG NINH/de1.json: image13.png
- lop12/DT26-16-CHUYEN HA LONG - QUANG NINH/de1.json: image5.png
- lop12/DT26-17-KSCL THPT LE QUY DON LAN 1 - HA NOI/de1.json: image11.png
- lop12/DT26-18-KSCL THPT NGUYEN KHUYEN - HCM/de1.json: image20.png
- lop12/DT26-20-THPT THIEU HOA -THANH HOA/de1.json: image7.png
- lop12/DT26-20-THPT THIEU HOA -THANH HOA/de1.json: image8.png
- lop12/DT26-21-THPT CHUYEN TRAN PHU LAN 1 -HAI PHONG/de1.json: image4.png
- lop12/DT26-22-KSCL THPT DONG HY - THAI NGUYEN/de1.json: image1.png
- lop12/DT26-22-KSCL THPT DONG HY - THAI NGUYEN/de1.json: image3.png
- lop12/DT26-22-KSCL THPT DONG HY - THAI NGUYEN/de1.json: image10.png
- lop12/DT26-22-KSCL THPT DONG HY - THAI NGUYEN/de1.json: image12.png
- lop12/DT26-22-KSCL THPT DONG HY - THAI NGUYEN/de1.json: image2.png
- lop12/DT26-25-CUM TRUONG THPT HA-TINH - L1/de1.json: image13.png
- lop12/DT26-27-CUM TRUONG THPT HA TINH - L1/de1.json: image13.png
- lop12/DT26-29-SO PHU THO - L1/de1.json: image4.png
- … và 170 ảnh nữa
