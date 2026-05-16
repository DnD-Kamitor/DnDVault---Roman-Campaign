#!/usr/bin/env bash
# Launch MapTool — all data stays in ./data/ (standalone)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BINARY="$SCRIPT_DIR/app/maptool/opt/maptool/bin/MapTool"

if [ ! -x "$BINARY" ]; then
    echo "ERROR: MapTool binary not found. Run: bash setup.sh"
    exit 1
fi

exec "$BINARY" "$@"
