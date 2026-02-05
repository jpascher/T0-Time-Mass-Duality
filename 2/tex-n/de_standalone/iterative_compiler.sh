#!/bin/bash
#================================================================
# Iterative LaTeX Compiler with Automatic Preamble Extension
# Compiles each .tex file individually and extends preamble based on errors
#================================================================

PREAMBLE="T0_preamble_standalone_De.tex"
LOGFILE="compilation_log.txt"
PREAMBLE_LOG="preamble_additions.txt"
SUCCESS_LIST="successful_compilations.txt"
FAIL_LIST="failed_compilations.txt"

# Initialize
> "$LOGFILE"
> "$PREAMBLE_LOG"
> "$SUCCESS_LIST"
> "$FAIL_LIST"

echo "============================================" | tee -a "$LOGFILE"
echo "Iterative LaTeX Compilation Started" | tee -a "$LOGFILE"
echo "Date: $(date)" | tee -a "$LOGFILE"
echo "============================================" | tee -a "$LOGFILE"
echo ""

# Get list of tex files (excluding preambles)
TEXFILES=$(ls -1 *.tex | grep -v "preamble" | sort)
TOTAL=$(echo "$TEXFILES" | wc -l)

echo "Found $TOTAL .tex files to compile" | tee -a "$LOGFILE"
echo ""

# Main compilation loop
iteration=1
MAX_ITERATIONS=5

while [ $iteration -le $MAX_ITERATIONS ]; do
    echo "========== ITERATION $iteration ==========" | tee -a "$LOGFILE"
    
    success_count=0
    fail_count=0
    file_num=0
    
    for texfile in $TEXFILES; do
        file_num=$((file_num + 1))
        basename="${texfile%.tex}"
        
        # Skip if already successful
        if grep -q "^$texfile$" "$SUCCESS_LIST" 2>/dev/null; then
            success_count=$((success_count + 1))
            continue
        fi
        
        # Clean auxiliary files
        rm -f "${basename}.aux" "${basename}.log" "${basename}.out" "${basename}.toc" "${basename}.pdf"
        
        # Compile
        if timeout 30 lualatex -interaction=nonstopmode "$texfile" >/dev/null 2>&1; then
            if [ -f "${basename}.pdf" ]; then
                echo "$texfile" >> "$SUCCESS_LIST"
                success_count=$((success_count + 1))
                [ $((success_count % 10)) -eq 0 ] && echo "  Progress: $success_count/$TOTAL compiled" | tee -a "$LOGFILE"
            fi
        else
            # Compilation failed - analyze error
            if [ -f "${basename}.log" ]; then
                # Look for missing packages
                if grep -q "! LaTeX Error: File.*not found" "${basename}.log"; then
                    MISSING_PKG=$(grep "! LaTeX Error: File.*not found" "${basename}.log" | head -1 | sed "s/.*File \`\(.*\)\.sty' not found.*/\1/")
                    if [ -n "$MISSING_PKG" ] && ! grep -q "usepackage{$MISSING_PKG}" "$PREAMBLE"; then
                        echo "\\usepackage{$MISSING_PKG}" >> "$PREAMBLE"
                        echo "Added package: $MISSING_PKG (for $texfile)" | tee -a "$PREAMBLE_LOG"
                    fi
                fi
                
                # Look for undefined commands
                if grep -q "Undefined control sequence" "${basename}.log"; then
                    CMD=$(grep -A1 "Undefined control sequence" "${basename}.log" | grep "^l\." | head -1 | sed 's/.*\\/\\/' | sed 's/[^a-zA-Z].*//')
                    if [ -n "$CMD" ] && ! grep -q "$CMD" "$PREAMBLE"; then
                        case "$CMD" in
                            "\\revolutionaer"|"\\wichtig")
                                echo "\\newcommand{$CMD}[1]{\\textbf{\\textcolor{t0red}{#1}}}" >> "$PREAMBLE"
                                ;;
                            "\\xii"|"\\alphaem")
                                echo "\\newcommand{$CMD}{\\ensuremath{\\xi}}" >> "$PREAMBLE"
                                ;;
                            "\\tzero"|"\\tplanck"|"\\lplanck"|"\\mplanck")
                                SYMBOL=$(echo "$CMD" | sed 's/\\t/T/' | sed 's/\\l/\\ell/' | sed 's/\\m/m/')
                                echo "\\newcommand{$CMD}{\\ensuremath{${SYMBOL}_{\\text{P}}}}" >> "$PREAMBLE"
                                ;;
                            *)
                                echo "\\newcommand{$CMD}{\\ensuremath{\\text{$(echo $CMD | sed 's/\\//')}}}" >> "$PREAMBLE"
                                ;;
                        esac
                        echo "Added command: $CMD (for $texfile)" | tee -a "$PREAMBLE_LOG"
                    fi
                fi
                
                # Look for undefined environments
                if grep -q "Environment.*undefined" "${basename}.log"; then
                    ENV=$(grep "Environment.*undefined" "${basename}.log" | head -1 | sed 's/.*Environment \([^ ]*\).*/\1/')
                    if [ -n "$ENV" ] && ! grep -q "newtcolorbox{$ENV}" "$PREAMBLE" && ! grep -q "newtheorem{$ENV}" "$PREAMBLE"; then
                        case "$ENV" in
                            "definition"|"beispiel"|"example")
                                echo "\\newtcolorbox{$ENV}[1][]{colback=blue!5,colframe=t0blue!80,fonttitle=\\bfseries,title={#1},breakable}" >> "$PREAMBLE"
                                ;;
                            "theorem"|"lemma"|"proposition"|"corollary")
                                echo "\\newtheorem{$ENV}{$(echo $ENV | sed 's/.*/\u&/')}[section]" >> "$PREAMBLE"
                                ;;
                            *)
                                echo "\\newtcolorbox{$ENV}[1][]{colback=gray!5,colframe=gray!80,fonttitle=\\bfseries,title={#1},breakable}" >> "$PREAMBLE"
                                ;;
                        esac
                        echo "Added environment: $ENV (for $texfile)" | tee -a "$PREAMBLE_LOG"
                    fi
                fi
            fi
            fail_count=$((fail_count + 1))
        fi
    done
    
    echo "Iteration $iteration: $success_count succeeded, $fail_count failed" | tee -a "$LOGFILE"
    
    # If all succeeded, break
    if [ $fail_count -eq 0 ]; then
        echo "✓ All files compiled successfully!" | tee -a "$LOGFILE"
        break
    fi
    
    # If no progress, break
    if [ $iteration -gt 1 ]; then
        PREV_SUCCESS=$(grep "Iteration $((iteration-1)):" "$LOGFILE" | grep -o "[0-9]* succeeded" | grep -o "[0-9]*")
        if [ "$success_count" = "$PREV_SUCCESS" ]; then
            echo "No progress made. Stopping iterations." | tee -a "$LOGFILE"
            break
        fi
    fi
    
    iteration=$((iteration + 1))
    echo ""
done

# Final statistics
> "$FAIL_LIST"
for texfile in $TEXFILES; do
    if ! grep -q "^$texfile$" "$SUCCESS_LIST" 2>/dev/null; then
        echo "$texfile" >> "$FAIL_LIST"
    fi
done

FINAL_SUCCESS=$(wc -l < "$SUCCESS_LIST")
FINAL_FAIL=$(wc -l < "$FAIL_LIST")

echo "" | tee -a "$LOGFILE"
echo "============================================" | tee -a "$LOGFILE"
echo "FINAL RESULTS" | tee -a "$LOGFILE"
echo "============================================" | tee -a "$LOGFILE"
echo "Total files:    $TOTAL" | tee -a "$LOGFILE"
echo "Successful:     $FINAL_SUCCESS" | tee -a "$LOGFILE"
echo "Failed:         $FINAL_FAIL" | tee -a "$LOGFILE"
echo "Success rate:   $(awk "BEGIN {printf \"%.1f%%\", $FINAL_SUCCESS * 100 / $TOTAL}")" | tee -a "$LOGFILE"
echo "Preamble lines: $(wc -l < $PREAMBLE)" | tee -a "$LOGFILE"
echo "============================================" | tee -a "$LOGFILE"

if [ $FINAL_FAIL -gt 0 ]; then
    echo ""
    echo "Failed files (first 20):"
    head -20 "$FAIL_LIST"
fi

