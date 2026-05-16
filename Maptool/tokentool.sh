#!/usr/bin/env bash
# Launch TokenTool — token portrait creator
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BINARY="$SCRIPT_DIR/app/tokentool/opt/tokentool/bin/TokenTool"

if [ ! -x "$BINARY" ]; then
    echo "ERROR: TokenTool binary not found. Run: bash setup.sh"
    exit 1
fi

exec "$BINARY" "$@"
