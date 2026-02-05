#!/bin/bash
# Systematic compilation of all DE standalone LaTeX files
# Output: latex_output_<Name>_<i>.txt and latex_error_<Name>_<i>.txt

LOGFILE="compilation_results.log"
ERRORLIST="failed_compilations.txt"

> "$LOGFILE"
> "$ERRORLIST"

success_count=0
fail_count=0
total_count=0

echo "========================================" | tee -a "$LOGFILE"
echo "DE Standalone LaTeX Compilation" | tee -a "$LOGFILE"
echo "Date: $(date)" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"

# Get all .tex files excluding preambles
for texfile in *.tex; do
    # Skip preamble files
    if [[ "$texfile" == "T0_preamble_De.tex" ]] || [[ "$texfile" == "T0_preamble_standalone_De.tex" ]]; then
        continue
    fi
    
    total_count=$((total_count + 1))
    basename="${texfile%.tex}"
    
    echo "[$total_count] Compiling: $texfile" | tee -a "$LOGFILE"
    
    # Clean auxiliary files for this document
    rm -f "${basename}.aux" "${basename}.log" "${basename}.out" "${basename}.toc" \
          "${basename}.fls" "${basename}.fdb_latexmk" "${basename}.synctex.gz"
    
    # Compile 3 passes
    pass_success=true
    for pass in 1 2 3; do
        if ! timeout 60 lualatex -interaction=nonstopmode -synctex=1 "$texfile" \
             > "latex_output_${basename}_${pass}.txt" 2> "latex_error_${basename}_${pass}.txt"; then
            echo "  FAILED at pass $pass" | tee -a "$LOGFILE"
            pass_success=false
            break
        fi
    done
    
    if $pass_success && [ -f "${basename}.pdf" ]; then
        echo "  SUCCESS - PDF created" | tee -a "$LOGFILE"
        success_count=$((success_count + 1))
    else
        echo "  FAILED - No PDF" | tee -a "$LOGFILE"
        echo "$texfile" >> "$ERRORLIST"
        fail_count=$((fail_count + 1))
    fi
    
    # Progress every 10 files
    if [ $((total_count % 10)) -eq 0 ]; then
        echo "  Progress: $total_count files, $success_count succeeded, $fail_count failed"
    fi
done

echo "" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "COMPILATION SUMMARY" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "Total files:   $total_count" | tee -a "$LOGFILE"
echo "Successful:    $success_count" | tee -a "$LOGFILE"
echo "Failed:        $fail_count" | tee -a "$LOGFILE"
echo "Success rate:  $(awk "BEGIN {printf \"%.1f\", $success_count * 100 / $total_count}")%" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"

if [ $fail_count -gt 0 ]; then
    echo "" | tee -a "$LOGFILE"
    echo "Failed files:" | tee -a "$LOGFILE"
    cat "$ERRORLIST" | tee -a "$LOGFILE"
fi
