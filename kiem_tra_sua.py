# -*- coding: utf-8 -*-
"""Kho đề — kiểm tra bản sửa của AI trước khi đẩy (chạy ở GỐC bản sao kho-de-toan):

    python kiem_tra_sua.py            # kiểm các mục ĐÃ ĐỔI so với origin/main
    python kiem_tra_sua.py --tat-ca   # kiểm mọi mục (chậm hơn, có thể báo lỗi cũ)

Quy tắc kiểm (mỗi lỗi in một dòng «LỖI …»; thoát mã 1 nếu có lỗi, mã 0 nếu sạch):
  • sua.json / phan_loai.json / eq_ocr.json phải là JSON hợp lệ, UTF-8 không BOM, gốc là đối tượng;
  • KHÔNG được xóa mục (mã câu) đã có ở origin/main — muốn bỏ câu thì ghi "bo_cau": true;
  • mục đổi nội dung phải có "sua_boi" (tên AI) và "ly_do";
  • options: đúng 4 chuỗi không rỗng; answer ∈ A–D; tf/tf_ans đủ a–d (tf_ans là true/false); short_correct không rỗng;
  • điền ô trống: mỗi {{n}} trong passage có đúng một blanks[id=n] có correctAnswer;
  • khung chứng minh (frame): mỗi {{n}} trong lines có blanks[id=n] có answers hoặc keywords; ô kéo thả có đáp án trong pool;
  • câu nhiều ý (parts): mỗi ý có id, label, type hợp lệ, question; short_answer có shortCorrect; proof_frame có frame hợp lệ;
  • điền theo mẫu (mau_spec): mỗi {{n}} có phần tử o[id=n] có dap_an;
  • phan_loai: dang phải có trong kho_de_data/dang_bai/lop<k>.json, muc_do ∈ NB/TH/VD/VDC.
Cuối cùng in một dòng tổng kết dạng pytest («==== N passed, M failed in Xs ====») để công cụ đọc kết quả test nhận diện.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "kho_de_data"
TOAN_BO = "--tat-ca" in sys.argv
CO_NOI_DUNG = {"question", "options", "answer", "tf", "tf_ans", "short_correct", "explanation", "type", "passage", "blanks", "parts", "frame", "mau_spec", "draw_spec"}
LOAI_Y = {"short_answer", "proof_frame", "form_mau", "multiple_choice", "essay", "draw"}
loi = []
dat = 0


def git(*a):
    r = subprocess.run(["git", "-c", "core.quotepath=off", *a], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else None


def ra(rel, k, msg):
    loi.append(f"LỖI {rel} · {k}: {msg}")


def doc(p):
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        return None, "có BOM — lưu UTF-8 không BOM"
    try:
        x = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return None, f"JSON hỏng: {str(e)[:80]}"
    if not isinstance(x, dict):
        return None, "gốc phải là đối tượng {mã_câu: {...}}"
    return x, None


def ids_trong(lines):
    return {m for l in lines for m in re.findall(r"\{\{(\w+)\}\}", str(l))}


def kiem_khung(rel, k, f, tag=""):
    if not isinstance(f, dict) or not isinstance(f.get("blocks"), list) or not f["blocks"]:
        return ra(rel, k, f"{tag}frame.blocks phải là mảng không rỗng")
    lines = []
    for b in f["blocks"]:
        if not isinstance(b, dict) or not isinstance(b.get("lines"), list) or not b["lines"]:
            return ra(rel, k, f"{tag}mỗi khối cần mảng lines")
        lines += b["lines"]
    blanks = {str(b.get("id")): b for b in f.get("blanks", []) if isinstance(b, dict)}
    pool = {str(x).strip() for x in f.get("pool", [])}
    for i in sorted(ids_trong(lines)):
        b = blanks.get(i)
        if not b:
            ra(rel, k, f"{tag}ô {{{{{i}}}}} trong lines không có trong frame.blanks")
            continue
        if not (b.get("answers") or b.get("keywords")):
            ra(rel, k, f"{tag}ô {{{{{i}}}}} thiếu answers/keywords")
        if (b.get("mode") or "drag") != "input" and not (pool & {str(a).strip() for a in b.get("answers", [])}):
            ra(rel, k, f"{tag}ô kéo thả {{{{{i}}}}}: đáp án phải có trong pool")


def kiem_mau(rel, k, m, tag=""):
    if not isinstance(m, dict) or m.get("kieu") not in ("dong", "bang"):
        return ra(rel, k, f"{tag}mau_spec.kieu phải là dong hoặc bang")
    lines = m.get("dong", []) if m["kieu"] == "dong" else [*(m.get("bang") or {}).get("header", []), *[c for r in (m.get("bang") or {}).get("rows", []) for c in r]]
    o = {str(x.get("id")): x for x in m.get("o", []) if isinstance(x, dict)}
    ids = ids_trong(lines)
    if not ids:
        ra(rel, k, f"{tag}mẫu chưa có ô {{{{n}}}}")
    for i in sorted(ids):
        if i not in o or not str(o[i].get("dap_an", "")).strip():
            ra(rel, k, f"{tag}ô {{{{{i}}}}} thiếu dap_an")


def kiem_muc(rel, k, e, cu):
    if not isinstance(e, dict):
        return ra(rel, k, "mục phải là đối tượng")
    doi = [f for f in CO_NOI_DUNG if f in e and (cu is None or e.get(f) != (cu or {}).get(f))]
    if doi and not e.get("bo_cau") and not e.get("bo_de"):
        if not e.get("sua_boi"):
            ra(rel, k, "đổi nội dung nhưng thiếu sua_boi")
        if not str(e.get("ly_do") or "").strip():
            ra(rel, k, "đổi nội dung nhưng thiếu ly_do")
    elif e.get("sua_boi") is None and e.get("xac_nhan") and not e.get("bo_cau"):
        ra(rel, k, "xac_nhan nhưng thiếu sua_boi")
    if "options" in e:
        o = e["options"]
        if not (isinstance(o, list) and len(o) == 4 and all(isinstance(x, str) and x.strip() for x in o)):
            ra(rel, k, "options phải là đúng 4 chuỗi không rỗng")
    if "answer" in e and str(e["answer"]) not in ("A", "B", "C", "D"):
        ra(rel, k, "answer phải là A, B, C hoặc D")
    if "tf" in e or "tf_ans" in e:
        tf, ta = e.get("tf") or {}, e.get("tf_ans") or {}
        for x in "abcd":
            if "tf" in e and not str(tf.get(x, "")).strip():
                ra(rel, k, f"tf thiếu ý {x}")
            if "tf_ans" in e and not isinstance(ta.get(x), bool):
                ra(rel, k, f"tf_ans.{x} phải là true/false")
    if "short_correct" in e and not str(e["short_correct"]).strip():
        ra(rel, k, "short_correct rỗng")
    if "passage" in e or "blanks" in e:
        bl = {str(b.get("id")): b for b in (e.get("blanks") or []) if isinstance(b, dict)}
        for i in sorted(ids_trong([e.get("passage", "")])):
            if i not in bl or not str(bl[i].get("correctAnswer", "")).strip():
                ra(rel, k, f"ô {{{{{i}}}}} trong passage thiếu blanks[id={i}].correctAnswer")
    if "frame" in e:
        kiem_khung(rel, k, e["frame"])
    if "mau_spec" in e:
        kiem_mau(rel, k, e["mau_spec"])
    if "parts" in e:
        if not isinstance(e["parts"], list) or not e["parts"]:
            ra(rel, k, "parts phải là mảng các ý")
        for i, p in enumerate(e["parts"] if isinstance(e["parts"], list) else []):
            tag = f"ý {p.get('label', i + 1) if isinstance(p, dict) else i + 1}: "
            if not isinstance(p, dict):
                ra(rel, k, tag + "phải là đối tượng")
                continue
            if p.get("type") not in LOAI_Y:
                ra(rel, k, tag + f"type «{p.get('type')}» không hợp lệ")
            if not str(p.get("question", "")).strip():
                ra(rel, k, tag + "thiếu question")
            if p.get("type") == "short_answer" and not str(p.get("shortCorrect", "")).strip():
                ra(rel, k, tag + "thiếu shortCorrect")
            if p.get("type") == "proof_frame":
                kiem_khung(rel, k, p.get("frame"), tag)
            if p.get("type") == "form_mau":
                kiem_mau(rel, k, p.get("mau_spec"), tag)


def dang_hop_le(lop):
    d = json.loads((DATA / "dang_bai" / f"lop{lop}.json").read_text(encoding="utf-8")) if (DATA / "dang_bai" / f"lop{lop}.json").exists() else {}
    return {dg.get("ma") for c in d.get("chuong", []) for b in c.get("bai", []) for dg in b.get("dang", [])}


def main():
    global dat
    t0 = time.time()
    cache_dang = {}
    for p in sorted(DATA.glob("lop*/*/*.json")):
        if p.name not in ("sua.json", "phan_loai.json", "eq_ocr.json"):
            continue
        rel = p.relative_to(DATA).as_posix()
        x, e = doc(p)
        if e:
            ra(rel, "-", e)
            continue
        cu_txt = git("show", f"origin/main:kho_de_data/{rel}")
        cu = None
        if cu_txt is not None:
            try:
                cu = json.loads(cu_txt.lstrip("﻿"))
            except ValueError:
                cu = None
        if cu is not None:
            for k in cu:
                if k not in x:
                    ra(rel, k, "mục bị XÓA so với origin/main — không được xóa; muốn bỏ câu thì ghi bo_cau: true")
        if cu is not None and cu == x and not TOAN_BO:
            continue
        lop = rel.split("/")[0][3:]
        for k, v in x.items():
            if cu is not None and not TOAN_BO and cu.get(k) == v:
                continue
            if p.name == "sua.json":
                kiem_muc(rel, k, v, (cu or {}).get(k))
            elif p.name == "phan_loai.json":
                if not isinstance(v, dict):
                    ra(rel, k, "mục phải là đối tượng")
                    continue
                if "muc_do" in v and v["muc_do"] not in ("NB", "TH", "VD", "VDC"):
                    ra(rel, k, f"muc_do «{v['muc_do']}» phải là NB/TH/VD/VDC")
                if "dang" in v:
                    if lop not in cache_dang:
                        cache_dang[lop] = dang_hop_le(lop)
                    if v["dang"] not in cache_dang[lop]:
                        ra(rel, k, f"dang «{v['dang']}» không có trong dang_bai/lop{lop}.json")
            dat += 1
    loi_so = len(loi)
    for l in loi[:200]:
        print(l)
    if loi_so > 200:
        print(f"… và {loi_so - 200} lỗi nữa")
    print(f"==== {dat} passed, {loi_so} failed in {time.time() - t0:.2f}s ====" if loi_so else f"==== {dat} passed in {time.time() - t0:.2f}s ====")
    sys.exit(1 if loi_so else 0)


if __name__ == "__main__":
    main()
