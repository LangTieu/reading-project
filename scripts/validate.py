#!/usr/bin/env python3
"""Khung kiểm tra nội dung. Sẽ mở rộng ở Giai đoạn 0. Hiện tại: liệt kê các file JSON trong content/ và báo file nào thiếu trường bắt buộc."""
import json
import pathlib
import sys

root = pathlib.Path.home() / "workspace" / "reading-project" / "content"
required = ["id", "level", "title", "text", "status"]
errors = 0
count = 0
for path in sorted(root.rglob("*.json")):
    count += 1
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL {path}: invalid JSON ({e})")
        errors += 1
        continue
    for field in required:
        if field not in data:
            print(f"FAIL {path}: missing field {field}")
            errors += 1
print(f"Checked {count} files, {errors} errors.")
sys.exit(1 if errors else 0)
