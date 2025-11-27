#!/bin/bash
# Compile all English documents with unified settings

cd "$(dirname "$0")"

success=0
fail=0

for f in *_En.tex; do
  # Skip Book files
  if [[ "$f" == *"Book"* ]]; then
    continue
  fi
  
  echo "Compiling: $f"
  pdflatex -interaction=nonstopmode "$f" > /dev/null 2>&1
  pdflatex -interaction=nonstopmode "$f" > /dev/null 2>&1  # Second pass
  
  if [ -f "${f%.tex}.pdf" ]; then
    ((success++))
    echo "  ✓ Success"
  else
    ((fail++))
    echo "  ✗ Failed"
  fi
done

echo ""
echo "================================"
echo "Success: $success, Failed: $fail"
echo "================================"
