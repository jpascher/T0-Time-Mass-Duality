#!/bin/bash
FILE="$1"
BASEDIR="/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
SRC_DIR="$BASEDIR/2/tex-n/de_standalone"
PROC_DIR="$BASEDIR/2/tex-n/de_standalone_processed"
PDF_DIR="$BASEDIR/2/pdf"

mkdir -p "$PROC_DIR" "$PDF_DIR"
cp "$SRC_DIR/$FILE" "$PROC_DIR/"
cd "$PROC_DIR"

for i in 1 2 3; do
  lualatex -interaction=nonstopmode "$FILE" >/dev/null 2>&1
done

BASENAME="${FILE%.tex}"
if [ -f "${BASENAME}.pdf" ]; then
  mv "${BASENAME}.pdf" "$PDF_DIR/"
  echo "SUCCESS: $FILE"
  exit 0
else
  echo "FAILED: $FILE"
  exit 1
fi
