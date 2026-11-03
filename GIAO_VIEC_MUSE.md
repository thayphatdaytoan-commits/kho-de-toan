# Lời nhắc giao việc cho Muse (ứng dụng Muse trên máy thầy)

**Chuẩn bị (một lần):** mở `C:\Users\ADMIN\muse_cli\dist\Muse\Muse.exe` → chọn dự án `C:\Users\ADMIN\Downloads\web toán\kho-de-toan-muse` →
Cài đặt: để chế độ duyệt từng lần ghi (hoặc bật Turbo nếu thầy yên tâm). **Không chọn thư mục `toan8-app`** (có khóa AI và mã web).

Dán nguyên khối dưới đây vào ô chat của Muse:

```
/goal Soát và sửa các câu hỏi còn nghi ngờ trong kho đề Toán của thầy Phát, ghi vào kho_de_data/lop<k>/<bài>/sua.json, đẩy lên nhánh ai/muse-… trong bản sao này. Điều kiện xong: chạy `python kiem_tra_sua.py` ra exit_code=0, mọi câu trong goi_viec/ đã được xử lý (sửa, xac_nhan hoặc ghi_chu) và đã commit + push nhánh.

Bạn đang ở bản sao kho đề (riêng tư, có bản quyền các trường — không đưa nội dung ra ngoài). Việc đầu tiên: đọc HUONG_DAN_AI.md (luật; đặc biệt mục 4, 4b, 6), rồi VIEC_CAN_LAM.md và goi_viec/MUC_LUC.md.

Mỗi đợt làm:
1. git checkout main && git pull origin main, rồi git checkout -b ai/muse-<YYYY-MM-DD>-<a|b|c…> (mỗi đợt một nhánh mới).
2. Đọc lần lượt các file trong goi_viec/ theo thứ tự mức 1 → 2 → 3 (mỗi file đọc MỘT lượt). Mỗi câu: tự giải lại từ đầu; sai thì sửa; đúng thì ghi xac_nhan; không chắc thì ghi ghi_chu cho thầy, không đoán. Câu có hình: mở ảnh trong de/lop<k>/<bài>/images/ trước khi kết luận thiếu dữ kiện.
3. Ghi vào sua.json: chỉ các trường cần đổi; BẮT BUỘC sua_boi = "muse" và ly_do (khi sửa nội dung). Câu tương tác (nhiều ý, khung chứng minh, điền ô, điền mẫu): ghi cả trường cấu trúc và tự kiểm theo danh sách ở mục 4b.
4. Chỉ được sửa: kho_de_data/lop*/*/sua.json, phan_loai.json, eq_ocr.json, kho_de_data/HANG_DOI.md, kho_de_data/dang_bai/de_xuat_dang_moi.json. KHÔNG xóa mục (mã câu) nào đã có — muốn bỏ câu thì ghi "bo_cau": true.
5. Sau mỗi khoảng 50 câu: chạy `python kiem_tra_sua.py`. Còn dòng LỖI thì sửa hết rồi chạy lại. Chỉ khi exit_code=0 mới: git add kho_de_data && git commit -m "Kho de: <lop/bai> - sua N cau, xac nhan M cau" && git push origin HEAD (đẩy NHÁNH ai/muse-…, KHÔNG đẩy main).
6. Cuối đợt báo cáo: số câu sửa, số xác nhận, số ghi chú, danh sách câu cần thầy xem, và lỗi gặp.

Cấm: đẩy main; tạo hay dùng token/khóa API; đọc hoặc ghi ngoài thư mục dự án; sửa file trong de/ (chỉ đọc); bịa số liệu.
```

**Sau khi Muse đẩy nhánh:** nhánh `ai/muse-…` nằm ngay trong `C:\Users\ADMIN\Downloads\web toán\kho-de-toan` (không qua GitHub). Khi công cụ duyệt (cổng 5180) đang chạy,
máy tự kéo và gộp theo từng mã câu trong vòng 10 phút; hoặc chạy `python scripts/kho_de/kho_ngoai.py keo`. Câu thầy đã sửa trên máy được giữ nguyên; AI không xóa được mục nào.
