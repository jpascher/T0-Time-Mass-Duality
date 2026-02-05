#!/bin/bash
# Iterative compilation - analyze and fix

FILE="001_T0_Book_Abstract_De.tex"
LOG="iterative_fix.log"

> "$LOG"

echo "=== Iteration 1: Minimal Preamble ===" | tee -a "$LOG"
rm -f 001_T0_Book_Abstract_De.aux 001_T0_Book_Abstract_De.log

lualatex -interaction=nonstopmode "$FILE" > /dev/null 2>&1

if [ -f "001_T0_Book_Abstract_De.log" ]; then
    echo "Errors found:" | tee -a "$LOG"
    grep "^!" 001_T0_Book_Abstract_De.log | grep -E "Undefined|Missing|Environment" | head -20 | tee -a "$LOG"
fi

echo "" | tee -a "$LOG"
echo "Missing packages/commands to add:" | tee -a "$LOG"
grep "Undefined control sequence" 001_T0_Book_Abstract_De.log | sed 's/.*\\/\\/' | sort -u | head -10 | tee -a "$LOG"
