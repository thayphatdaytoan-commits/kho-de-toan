# Hướng dẫn cho AI sửa lỗi kho đề (repo kho-de-toan)

Bạn là AI được thầy Phát (giáo viên Toán) giao **soát và sửa câu hỏi** trong kho đề Toán lớp 6–12 (chương trình GDPT 2018, Việt Nam).
Trả lời và ghi chú bằng **tiếng Việt có dấu**. Repo này **riêng tư**: đề có bản quyền của các trường, không đưa ra ngoài.

## 1. Repo có gì

| Đường dẫn | Nội dung | Được sửa? |
|---|---|---|
| `VIEC_CAN_LAM.md`, `viec_can_lam.json` | Các câu còn **cờ** (lỗi nghi ngờ), xếp theo bài — **bắt đầu từ đây** | Không (tự sinh) |
| `de/lop<k>/<bài>/de<n>.json` | Đề đã chuẩn hóa: mảng `questions`, mỗi câu có `ma`, `type`, `question`, `options`, `answer`, `tf`, `tf_ans`, `short_correct`, `explanation`, `flags`, `dang`, `muc_do` | **Không** — bản chụp, bị ghi đè mỗi lần thầy đẩy kho |
| `de/lop<k>/<bài>/images/…`, `anh.json` | Ảnh trong đề. `[[IMG:ten]]` trong chữ → mở `anh.json` lấy đường dẫn (không có thì `images/ten`) | Không |
| `kho_de_data/lop<k>/<bài>/sua.json` | **Nơi ghi sửa câu** | **Có** |
| `kho_de_data/lop<k>/<bài>/phan_loai.json` | Dạng bài + mức độ của câu | **Có** |
| `kho_de_data/lop<k>/<bài>/eq_ocr.json` | Công thức dạng ảnh → LaTeX | **Có** |
| `kho_de_data/lop<k>/<bài>/pdf_nhap*.txt` | Bản chép đề của bài nguồn PDF | Có (chỉ khi đề chép sai) |
| `kho_de_data/HANG_DOI.md` | Bảng nhận việc | Có |
| `kho_de_data/dang_bai/lop<k>.json`, `TIEU_CHI_MUC_DO.md` | Cây dạng bài, tiêu chí mức độ | Không (chỉ đọc); đề xuất dạng mới ghi `dang_bai/de_xuat_dang_moi.json` |

Máy của thầy chỉ nhận về các file được phép sửa ở trên; sửa chỗ khác sẽ bị bỏ qua.
Sau khi thầy kéo về, máy chạy lại toàn bộ khâu dựng đề + kiểm tra KaTeX + import web, nên **chỉ cần ghi đúng dữ liệu**.

## 2. Mã câu

Mỗi câu có mã cố định `de<n>.P<phần>.C<câu>` (trường `ma`), ví dụ `de2.P3.C5` = đề 2, Phần 3 (trả lời ngắn), câu 5.
Phần 1 = trắc nghiệm 4 phương án, Phần 2 = đúng/sai, Phần 3 = trả lời ngắn (đề cấp 2 có thêm phần tự luận).
Khóa trong `sua.json` / `phan_loai.json` chính là mã câu này.

## 3. Cách làm một bài

1. Chọn bài trong `VIEC_CAN_LAM.md` (bài nhiều cờ trước). Ghi tên bạn vào cột «Người nhận» của bài đó trong `kho_de_data/HANG_DOI.md`
   (thêm dòng nếu chưa có) để AI khác không làm trùng.
2. Mở `de/lop<k>/<bài>/de<n>.json`, đọc câu có cờ (`flags`) — bảng giải thích cờ ở `VIEC_CAN_LAM.md`. Cờ `trung_web:…` chỉ là thông tin, bỏ qua.
3. **Giải lại bài từ đầu** trước khi sửa. Có thể chạy Python/sympy để tính lại. Không chắc thì **không sửa**, ghi `ghi_chu` cho thầy.
4. Ghi vào `kho_de_data/lop<k>/<bài>/sua.json` (tạo file nếu chưa có; giữ nguyên các khóa đã có của người khác).
5. Commit lên **nhánh riêng** `ai/<tên-bạn>-<YYYY-MM-DD>` rồi mở pull request vào `main` (hoặc đẩy thẳng `main` nếu thầy cho phép).
   Commit message tiếng Việt không dấu: `Kho de: lop10 C3-B2 - sua 7 cau co co`.

## 4. Định dạng `sua.json`

```json
{
  "de1.P1.C3": {
    "explanation": "Tam giác $ABC$ đều nên … Vậy chọn B.",
    "answer": "B",
    "sua_boi": "muse",
    "ly_do": "Lời giải gốc ghi «C đúng» nhưng tính ra B",
    "xac_nhan": true
  },
  "de2.P3.C5": { "short_correct": "-3,57", "question": "… (làm tròn đến hàng phần trăm).", "sua_boi": "muse", "ly_do": "…", "xac_nhan": true },
  "de2.P1.C9": { "xac_nhan": true, "sua_boi": "muse" },
  "de3.P1.C2": { "bo_cau": true, "sua_boi": "muse", "ly_do": "Câu chứng minh, không có đáp số" },
  "de4.P2.C1": { "ghi_chu": "Đề thiếu số liệu bảng tần số, không giải được — nhờ thầy xem ảnh gốc", "sua_boi": "muse" },
  "de5": { "bo_de": true, "sua_boi": "muse", "ly_do": "Cả đề trùng đề 2" }
}
```
- Trường sửa được: `question`, `options` (mảng đúng 4 chuỗi, không ghi «A.»), `answer` (`"A"`–`"D"`), `tf` (`{"a": "…", "b": "…"}`),
  `tf_ans` (`{"a": true, "b": false, …}`), `short_correct` (nhiều cách ghi nối bằng `|`, vd `-0,65|-13/20`), `explanation`, `type`.
- `xac_nhan: true` = đã kiểm cả câu và câu đúng → xóa cờ. Câu không sai gì thì chỉ cần `{"xac_nhan": true, "sua_boi": "…"}`.
- `bo_cau: true` = bỏ câu (hỏng, trùng, không có đáp án). Bỏ cả đề: khóa `"de<n>": {"bo_de": true}`.
- **Bắt buộc** `sua_boi` (tên AI của bạn) ở mọi câu bạn ghi — thiếu thì máy thầy từ chối câu đó. `ly_do` bắt buộc khi sửa nội dung.
- Chỉ ghi các trường cần đổi (máy gộp vào câu gốc). Công thức LaTeX trong `$...$` (KaTeX), trong JSON nhớ viết `\\frac`, `\\sqrt`.
- Giữ văn phong đề gốc; không bịa số liệu; không viết lại câu đang đúng.

## 5. `phan_loai.json` và `eq_ocr.json`

```json
{ "de1.P1.C1": { "dang": "L10.C3.B2.D08", "muc_do": "NB", "boi": "muse" } }
```
`dang` phải là mã có trong `kho_de_data/dang_bai/lop<k>.json`; `muc_do` ∈ NB, TH, VD, VDC theo `kho_de_data/TIEU_CHI_MUC_DO.md`.
Không có mã phù hợp → ghi đề xuất vào `kho_de_data/dang_bai/de_xuat_dang_moi.json` (`{"ma_cau", "bai", "ten_de_xuat", "ly_do"}`).

`eq_ocr.json`: `{ "image13.wmf": " $ABC$ " }` — giá trị thay thẳng vào chỗ ảnh công thức (gồm cả dấu `$`).

## 6. Quy tắc thầy đã chốt (bắt buộc)

- **Cấp 3 (lớp 10–12) không có tự luận**: chỉ trắc nghiệm / đúng-sai / trả lời ngắn. Câu chứng minh/chứng tỏ không có đáp số → `bo_cau`
  (hoặc viết lại thành câu có đáp số duy nhất).
- Đáp án là **chữ, khoảng, biểu thức, tập nghiệm** hoặc nhiều giá trị (không phải một số ngắn) → đổi sang **trắc nghiệm 4 phương án**:
  `type: "multiple_choice"`, `options` (1 đúng + 3 nhiễu từ sai lầm thường gặp), `answer`.
- **Trả lời ngắn**: đáp án là một số (tối đa 4 ký tự kiểu đề THPT, dấu phẩy thập phân). Đáp án thập phân từ 2 chữ số thập phân trở lên mà đề
  không có «làm tròn» → thêm «Làm tròn kết quả đến chữ số thập phân thứ nhất.» và chỉnh đáp án (gặp 5 thì làm tròn lên). Đáp án chính xác chỉ
  1–2 chữ số thập phân thì không cần làm tròn; số gần đúng (≈) vẫn phải có yêu cầu làm tròn. Làm tròn ra 0,0 / 1,0 (mất nghĩa) → hỏi thầy qua `ghi_chu`.
- **Thống kê / ghép nhóm**: luôn tính lại bằng máy (hay sai: lấy nhầm số trung bình thay độ lệch chuẩn, thiếu Q1/Q2, đề thiếu số liệu).
- Câu trùng đề đã có trên web (cờ `trung_web`) do máy thầy xử lý — không cần làm gì.
- Câu có hình: xem ảnh trước khi kết luận đề thiếu dữ kiện. Ảnh bị thiếu file (liệt kê cuối `VIEC_CAN_LAM.md`) → `ghi_chu`, không tự vẽ.

## 7. Đề mới bạn tự soạn / chép và HÌNH ẢNH

- Đề mới đặt ở `de/lop<k>/<mã bài mới>/de1.json` (cùng định dạng với đề có sẵn, `meta.soan_boi` = tên bạn). Mã bài mới phải **khác mọi bài
  đang có** và nên chứa tên bạn, ví dụ `DT12GK1-MUSE-06-…`. Máy thầy không xóa thư mục bài do bạn tạo; bài có sẵn thì vẫn không được sửa.
- **Hình**: nếu công cụ GitHub của bạn chỉ ghi được file chữ (không đẩy được file ảnh nhị phân), hãy gửi mỗi hình dưới dạng **base64**:
  - file `de/lop<k>/<bài>/images/<tên ảnh>.b64`, ví dụ `images/image1.png.b64` cho `[[IMG:image1.png]]`;
  - nội dung là chuỗi base64 của file ảnh (được phép có tiền tố `data:image/png;base64,`); đuôi hợp lệ: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`;
  - hình vẽ đơn giản (bảng biến thiên, đồ thị, hình học) có thể gửi thẳng file `.svg` (là file chữ, không cần base64).
  Máy thầy tự kiểm 10 phút một lần: giải mã thành ảnh thật, xóa file `.b64` và đẩy ảnh lên lại `main`. File `.b64` hỏng được giữ nguyên
  và báo cho thầy — khi đó gửi lại.
- Đẩy đề mới + hình lên `main` (hoặc nhánh `ai/…` rồi mở pull request). Commit message nêu rõ số đề, số hình.

## 8. Trang xem kho (GitHub Pages: index.html)

- `catalog.json` và `cap_nhat.json` do **máy thầy tự sinh** mỗi lần đẩy kho (đủ mọi đề trong `de/`, kể cả đề bạn soạn; bỏ đề thầy «bỏ cả đề»;
  `nq` không tính câu đã bỏ; thêm `co` = số câu còn cờ, `soan_boi`). **Đừng sửa tay** hai file này — sẽ bị ghi đè.
- `index.html` là giao diện, bạn được sửa, nhưng giữ các điều đã chốt:
  - không biến đổi LaTeX: trong kho `\\` là **xuống dòng** của `cases`/`aligned`/`array` (khoảng 16.600 chỗ), không phải dấu `\` bị gấp đôi;
  - tìm ảnh theo `anh.json` của bài trước (thẻ `[[IMG:ảnh.emf#x,y,w,h]]` có vùng cắt → file ảnh đã cắt sẵn), rồi mới đoán `images/<tên>`;
  - ẩn câu có `bo_cau: true`;
  - `grade` là SỐ, không phải chuỗi.
- Trang này **công khai** (ai có link cũng xem được) — đừng đưa thêm dữ liệu nhạy cảm (khóa API, thông tin học sinh) vào repo.

## 9. Xong một bài khi

- Mọi câu có cờ đã có `xac_nhan`, sửa, `bo_cau` hoặc `ghi_chu` trong `sua.json`.
- Câu thiếu `dang` / `muc_do` đã có trong `phan_loai.json` (nếu bạn được giao phân loại).
- File JSON hợp lệ, UTF-8 không BOM, không xóa khóa của người khác.
- Ghi «xong» vào `HANG_DOI.md`, commit, mở pull request.
