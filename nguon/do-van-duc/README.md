# Nguồn đề thầy Đỗ Văn Đức — Hướng dẫn cho admin

## Thầy là ai

Thầy **Đỗ Văn Đức** (TENS) — giáo viên Toán 12 khóa 2k9, dạy online qua hệ thống khóa học có thu phí. Tài liệu của thầy được hệ thống lại từ sheet do thầy công bố, chỉ dùng nội bộ cho kho đề; không phát tán lại file gốc.

## Sheet nguồn

- **Tên sheet:** ĐỖ VĂN ĐỨC 2k9
- **Link:** https://docs.google.com/spreadsheets/d/1JJojTxelBFgd9tufxi-dDseKA2Scsq1vycJVl0WmUNI/edit?usp=drive_link
- **Các tab:** VIEW FULL, KHOA T, KHÓA T2, KHÓA T3: Toán thực tế, KHÓA E, KHÓA CHỮA SÁCH, KHÓA ĐOM ĐÓM.
- **Danh mục PDF đầy đủ đã hệ thống (2026-10-16):** `~/workspace/danh-sach-khoa-hoc-2027/thay-do-van-duc/He-thong-PDF-Thay-Do-Van-Duc-2k9.xlsx` — 271 file PDF khác nhau (~2,3 GB), phân theo khóa: Chữa sách 94, T 74, E 66, T2 53, Đom đóm 20, T3 13, Ebook 5; kèm 282 link video. Lưu ý: khóa Đom đóm là khóa tổ hợp 5 môn nên có cả PDF Lý, Hóa, Sinh, Anh.

## Các khóa của thầy (theo sheet gốc)

| Khóa | Nội dung chính |
|---|---|
| Khóa T | Khóa Toán 12 chính (lý thuyết + bài tập theo chương) |
| Khóa T2 | Khóa Toán 12 nâng cao/luyện đề |
| Khóa T3 | Toán thực tế |
| Khóa E | Khóa luyện thi (E) |
| Khóa Chữa sách | Chữa sách giáo khoa/bài tập theo từng bài học (mã BOOK…) |
| Khóa Đom đóm | Khóa tổ hợp 5 môn (Toán, Lý, Hóa, Sinh, Anh) |
| Ebook | Tài liệu ebook đi kèm |

## Bảng các lô đã gõ cho kho đề

| Lô | Bài nguồn | Nội dung gõ | Trạng thái |
|---|---|---|---|
| Lô 1 | BOOK2D1 – Bài 1: Mở đầu về nguyên hàm (Khóa Chữa sách) | Phần C. Bài tập rèn luyện: 30 câu (trắc nghiệm 15, đúng/sai 8, trả lời ngắn 7) | Staging xong 2026-11-04, chưa push |
| (Lô sau) | BOOK2D1 | Phần A. Tóm tắt kiến thức + Phần B. Ví dụ 1–5 | Chưa làm |

## Cách đọc provenance

- Mỗi lô có thư mục riêng: `nguon/do-van-duc/lot-NN/`.
- `nguon_goc.json`: một mục cho mỗi mã câu kho, gồm khóa, bài, dạng gốc, số câu gốc, link Tài liệu, link Bản viết tay, đáp án thầy, đáp án tự giải, trang bản viết tay.
- `nguon_goc.md`: cùng nội dung dạng bảng, kèm ghi chú về khác biệt giữa hai bản nguồn (nếu có).
- Mã kho dạng `de1.P<phần>.C<STT trong phần>`; bảng provenance luôn đối chiếu rõ mã kho ↔ câu gốc, vì số thứ tự trong phần khác số câu gốc ở Phần II và III (ví dụ P2.C1 = câu gốc 16, P3.C1 = câu gốc 24).
- Đáp án thầy lấy từ bản viết tay (chữ khoanh tròn/đánh dấu Đ/S), không lấy từ mô tả trang tải. Nếu tự giải lệch đáp án thầy hoặc chữ viết tay đọc không chắc, câu đó được đưa vào diện held kèm lý do trong báo cáo lô, không đoán.
- File đề JSON nằm ở `kho/de/lop12/<mã đề>/de1.json`, đúng chuẩn kho đề (meta, sections, questions, flags), chỉ staging — không tự push/commit/merge lên GitHub.
