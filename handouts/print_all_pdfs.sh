#!/usr/bin/env bash
# Generate print-ready PDFs for all handouts.
# Run from the handouts/ directory or from repo root.
# Requires wkhtmltopdf (sudo dnf install wkhtmltopdf  OR  sudo apt install wkhtmltopdf)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PDF_DIR="$SCRIPT_DIR/pdf"
mkdir -p "$PDF_DIR"

cd "$SCRIPT_DIR"

OPTS="--enable-local-file-access --print-media-type --page-size A4 --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 --quiet"

ok=0
fail=0

for html in handout_*.html s2_*.html; do
  [ -f "$html" ] || continue
  name="${html%.html}"
  out="$PDF_DIR/${name}.pdf"
  if wkhtmltopdf $OPTS "$SCRIPT_DIR/$html" "$out" 2>/dev/null; then
    echo "  OK  $out"
    ((ok++)) || true
  else
    echo "FAIL  $html"
    ((fail++)) || true
  fi
done

echo ""
echo "Done: $ok PDF(s) generated in handouts/pdf/"
[ "$fail" -gt 0 ] && echo "      $fail file(s) failed (check wkhtmltopdf is installed)" || true
