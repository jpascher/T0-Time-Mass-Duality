#!/bin/bash
# Final compilation of all DE standalone files with 2 passes each

LOGFILE="final_compilation.log"
> "$LOGFILE"

success=0
fail=0
total=0

echo "Starting full compilation..." | tee -a "$LOGFILE"
echo "Time: $(date)" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"

for texfile in *.tex; do
    # Skip preambles
    [[ "$texfile" == "T0_preamble"* ]] && continue
    
    total=$((total + 1))
    base="${texfile%.tex}"
    
    # Clean aux files
    rm -f "${base}.aux" "${base}.log" "${base}.out" "${base}.toc"
    
    # Two passes
    pass_ok=true
    for pass in 1 2; do
        if ! timeout 60 lualatex -interaction=nonstopmode "$texfile" >/dev/null 2>&1; then
            pass_ok=false
            break
        fi
    done
    
    if $pass_ok && [ -f "${base}.pdf" ]; then
        success=$((success + 1))
        [ $((success % 10)) -eq 0 ] && echo "Progress: $success files compiled..." | tee -a "$LOGFILE"
    else
        fail=$((fail + 1))
        echo "FAILED: $texfile" | tee -a "$LOGFILE"
    fi
done

echo "" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "FINAL RESULTS" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "Total:      $total files" | tee -a "$LOGFILE"
echo "Success:    $success files" | tee -a "$LOGFILE"
echo "Failed:     $fail files" | tee -a "$LOGFILE"
echo "Rate:       $(awk "BEGIN {printf \"%.1f%%\", $success * 100 / $total}")" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
