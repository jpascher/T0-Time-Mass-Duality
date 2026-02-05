#!/bin/bash
# Automatische Preamble-Erweiterung basierend auf Fehlern

FILE="001_T0_Book_Abstract_De.tex"
PREAMBLE="T0_preamble_standalone_De.tex"

for iteration in {1..10}; do
    echo "=== Iteration $iteration ==="
    
    # Clean and compile
    rm -f *.aux *.log *.out *.toc 001*.pdf
    lualatex -interaction=nonstopmode "$FILE" >/dev/null 2>&1
    
    if [ -f "001_T0_Book_Abstract_De.pdf" ]; then
        echo "✓ SUCCESS - PDF created!"
        ls -lh 001_T0_Book_Abstract_De.pdf
        break
    fi
    
    # Analyze errors
    if [ ! -f "001_T0_Book_Abstract_De.log" ]; then
        echo "No log file found"
        break
    fi
    
    # Find first undefined command or environment
    ERROR=$(grep -m1 "^! " 001_T0_Book_Abstract_De.log)
    echo "Error: $ERROR"
    
    # Check for missing environment
    if echo "$ERROR" | grep -q "Environment.*undefined"; then
        ENV=$(echo "$ERROR" | sed 's/.*Environment \([^ ]*\).*/\1/')
        echo "Missing environment: $ENV"
        echo "\\newtcolorbox{$ENV}[1][]{colback=blue!5,colframe=t0blue!80,title={#1},breakable}" >> "$PREAMBLE"
    fi
    
    # Check for missing command
    if echo "$ERROR" | grep -q "Undefined control sequence"; then
        # Extract command from next line
        CMD=$(grep -A1 "^! Undefined control sequence" 001_T0_Book_Abstract_De.log | grep "^l\." | head -1 | sed 's/.*\\/\\/' | sed 's/[^a-zA-Z].*//')
        if [ -n "$CMD" ]; then
            echo "Missing command: $CMD"
            # Add simple definition
            echo "\\newcommand{$CMD}{\\ensuremath{\\text{$CMD}}}" >> "$PREAMBLE"
        fi
    fi
    
    echo "Preamble now has $(wc -l < $PREAMBLE) lines"
    echo ""
done
