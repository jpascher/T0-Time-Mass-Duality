#!/bin/bash
# Safe test without deleting files

success=0
fail=0

for f in 001_T0_Book_Abstract_De.tex 002_reise_De.tex 003_T0_Grundlagen_v1_De.tex 004_T0_Modell_Uebersicht_De.tex 005_T0_tm-erweiterung-x6_De.tex 010_T0_Energie_De.tex 025_T0_Kosmologie_De.tex 063_cosmic_De.tex; do
    echo "Testing: $f"
    base="${f%.tex}"
    
    # Clean only aux files, keep tex
    rm -f "${base}.aux" "${base}.log" "${base}.out" "${base}.toc"
    
    if timeout 60 lualatex -interaction=nonstopmode "$f" >/dev/null 2>&1 && [ -f "${base}.pdf" ]; then
        echo "  ✓ SUCCESS"
        success=$((success + 1))
    else
        echo "  ✗ FAILED"
        fail=$((fail + 1))
        # Show first error
        grep "^!" "${base}.log" 2>/dev/null | head -1
    fi
done

echo ""
echo "Results: $success succeeded, $fail failed"
