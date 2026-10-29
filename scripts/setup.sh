#!/bin/bash
# Setup lại môi trường làm việc trên VM mới.
# Nguyên tắc: cài tool vào ~/workspace/tools/, không dựa vào cài đặt hệ thống cũ.
# Script này hiện là khung — sẽ điền lệnh cài Kokoro / tool kiểm tra cụ thể
# khi chốt giọng kể và toolchain ở Giai đoạn 0.
set -e
echo "Project dir: $HOME/workspace/reading-project"
echo "TODO: install project tools into $HOME/workspace/tools/ here, then run scripts/validate.py"
ls "$HOME/workspace/reading-project/content/lessons" || true
ls "$HOME/workspace/reading-project/content/stories" || true
