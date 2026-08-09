#!/bin/sh
set -eu

PROJECT_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$PROJECT_ROOT"

PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
PYTHONPATH=src python3 -m wbc_handbook build-index --data-dir data --index var/handbook.sqlite
PYTHONPATH=src python3 -m wbc_handbook query "unreviewed question" --index var/handbook.sqlite
PYTHONPATH=src python3 -m wbc_handbook query "全身遥操作需要全局线速度吗？" --index var/handbook.sqlite
git diff --check
