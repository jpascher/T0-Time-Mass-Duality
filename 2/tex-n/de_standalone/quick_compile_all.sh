#!/bin/bash
# Quick compilation of all files (1 pass each for speed)

success=0
fail=0
total=0

for f in *.tex; do
    [ "$f" = "T0_preamble_De.tex" ] && continue
    [ "$f" = "T0_preamble_standalone_De.tex" ] && continue
    
    total=$((total + 1))
    base="${f%.tex}"
    
    rm -f "${base}.aux" "${base}.log" "${base}.out" "${base}.toc" "${base}.pdf"
    
    if timeout 60 lualatex -interaction=nonstopmode "$f" >/dev/null 2>&1 && [ -f "${base}.pdf" ]; then
        success=$((success + 1))
        [ $((success % 10)) -eq 0 ] && echo "Progress: $success/$total succeeded"
    else
        fail=$((fail + 1))
        echo "FAILED: $f"
    fi
done

echo ""
echo "========================================="
echo "RESULTS: $success succeeded, $fail failed out of $total"
echo "Success rate: $(awk "BEGIN {printf \"%.1f%%\", $success * 100 / $total}")"
echo "========================================="
