# Tiêu chí mức độ (dùng chung cho mọi AI)

Bốn mức như web: **NB** (Nhận biết) · **TH** (Thông hiểu) · **VD** (Vận dụng) · **VDC** (Vận dụng cao).
Web đổi sang `recognize / understand / apply / apply_high` khi Import đề thi.

## Thứ tự quyết định

1. **Đề có ghi sẵn** (`[Mức độ 1]`, `Mức độ: NB`…) → dùng luôn (1=NB, 2=TH, 3=VD, 4=VDC).
2. Không có → chấm theo bảng dưới, dựa trên `dac_trung` trong `de<k>.json` (pipeline đã tính sẵn).
3. Lệch ≥ 2 mức so với `muc_do_goi_y_theo_vi_tri` → pipeline tự gắn cờ; chỉ giữ nếu có lý do rõ (ghi `ly_do`).

## Bảng chấm

| Mức | Dấu hiệu chính | `dac_trung` thường gặp |
|---|---|---|
| NB | Nhắc lại định nghĩa / công thức / giá trị đặc biệt; thay số 1 bước | `so_dau_bang` ≤ 2, `so_dong_loi_giai` ≤ 2 |
| TH | Áp dụng trực tiếp 1 công thức/định lí, 2–3 bước biến đổi | `so_dau_bang` 3–5 |
| VD | Kết hợp ≥ 2 kiến thức, hoặc mô hình hóa bài toán thực tế, hoặc biến đổi nhiều bước | `so_dau_bang` ≥ 6, hoặc `thuc_te` = true |
| VDC | Biện luận tham số, bài toán tối ưu, cần ý tưởng không mẫu mực, nhiều trường hợp | `tham_so` = true kèm biện luận, hoặc lời giải dài + ý tưởng mới |

Câu **Đúng/Sai** chấm theo ý khó nhất (thường ý d). Câu **trả lời ngắn** hiếm khi là NB.

## Hiệu chuẩn

Trước khi một AI được phân loại hàng loạt: thầy gán mức cho 30 câu mẫu (`kho_de_data/hieu_chuan/`),
AI phải khớp ≥ 85%. Ghi kết quả vào `HANG_DOI.md` mục «Hiệu chuẩn».
