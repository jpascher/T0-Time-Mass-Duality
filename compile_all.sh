#!/bin/bash
REPO_ROOT=$(pwd)
outdir="$REPO_ROOT/2/pdf"
mkdir -p "$outdir"

# Clear error file
> tex_compile_errors.txt
> tex_compile_success.txt

count=0
success_count=0
error_count=0
total=$(wc -l < tex_master_files.txt)

echo "Starting compilation of $total LaTeX documents..."
echo ""

while read -r F; do
  count=$((count + 1))
  
  # Get directory and filename
  srcdir=$(dirname "$F")
  filename=$(basename "$F" .tex)
  
  # Print progress every 20 files
  if [ $((count % 20)) -eq 0 ]; then
    echo "Progress: [$count/$total] - Success: $success_count - Errors: $error_count"
  fi
  
  # Change to source directory for compilation
  cd "$REPO_ROOT/$srcdir"
  
  # Compile with latexmk
  if latexmk -lualatex -interaction=nonstopmode -halt-on-error "$(basename "$F")" >/dev/null 2>&1; then
    # Move PDF to output directory
    if [ -f "${filename}.pdf" ]; then
      mv "${filename}.pdf" "$outdir/"
      echo "$F" >> "$REPO_ROOT/tex_compile_success.txt"
      success_count=$((success_count + 1))
    else
      echo "$F" >> "$REPO_ROOT/tex_compile_errors.txt"
      error_count=$((error_count + 1))
    fi
  else
    echo "$F" >> "$REPO_ROOT/tex_compile_errors.txt"
    error_count=$((error_count + 1))
  fi
  
  # Cleanup auxiliary files
  rm -f "${filename}.aux" "${filename}.log" "${filename}.fls" "${filename}.fdb_latexmk" \
        "${filename}.out" "${filename}.toc" "${filename}.lof" "${filename}.lot"
  
  cd "$REPO_ROOT"
done < tex_master_files.txt

cd "$REPO_ROOT"
echo ""
echo "===== Compilation Complete ====="
echo "Total files: $count"
echo "Successful: $success_count"
echo "Errors: $error_count"
echo ""
if [ $error_count -gt 0 ]; then
  echo "First 20 errors:"
  head -20 tex_compile_errors.txt
fi
