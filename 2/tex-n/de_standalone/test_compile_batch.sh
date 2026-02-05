#!/bin/bash
# Test compilation on first 10 files

count=0
for texfile in *.tex; do
    if [[ "$texfile" == "T0_preamble_De.tex" ]] || [[ "$texfile" == "T0_preamble_standalone_De.tex" ]]; then
        continue
    fi
    
    count=$((count + 1))
    if [ $count -gt 10 ]; then
        break
    fi
    
    basename="${texfile%.tex}"
    echo "Testing: $texfile"
    
    rm -f "${basename}.aux" "${basename}.log" "${basename}.out" "${basename}.toc"
    
    if timeout 60 lualatex -interaction=nonstopmode "$texfile" >/dev/null 2>&1 && [ -f "${basename}.pdf" ]; then
        echo "  ✓ SUCCESS"
    else
        echo "  ✗ FAILED"
        # Show first error
        grep "^!" "${basename}.log" 2>/dev/null | head -3
    fi
done
