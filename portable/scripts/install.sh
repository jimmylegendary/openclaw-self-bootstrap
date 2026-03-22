#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-$HOME/.openclaw/workspace}"
STAMP="$(date +%Y%m%d%H%M%S)"

mkdir -p "$TARGET"
mkdir -p "$TARGET/skills"

backup_if_exists() {
  local path="$1"
  if [ -e "$path" ]; then
    mv "$path" "${path}.bak.${STAMP}"
  fi
}

copy_file() {
  local src="$1"
  local dst="$2"
  backup_if_exists "$dst"
  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
}

copy_dir() {
  local src="$1"
  local dst="$2"
  backup_if_exists "$dst"
  mkdir -p "$(dirname "$dst")"
  cp -R "$src" "$dst"
}

echo "[1/3] Installing template markdown files..."
for f in "$SRC_DIR"/templates/*.md; do
  name="$(basename "$f")"
  copy_file "$f" "$TARGET/$name"
done

echo "[2/3] Installing skills..."
for d in "$SRC_DIR"/skills/*; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  copy_dir "$d" "$TARGET/skills/$name"
done

echo "[3/3] Installing MCP examples..."
copy_dir "$SRC_DIR/mcp-examples" "$TARGET/mcp-examples"

echo

echo "Installed OpenClaw Portable Kit to: $TARGET"
echo "Backups use suffix: .bak.${STAMP}"
echo

echo "Next steps:"
echo "  openclaw status"
echo "  python3 $TARGET/mcp-examples/test_mcp_server.py"
