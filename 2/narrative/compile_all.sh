#!/bin/bash
# Script to compile all narrative chapters

set -e

NARRATIVE_DIR="/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/narrative"
PDF_DIR="/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/pdf"

cd "$NARRATIVE_DIR"

# Compile all German chapters (14-44)
echo "Compiling German chapters..."
for i in {14..44}; do
    CHAPTER=$(printf "Kapitel_%02d_Narrative_De" $i)
    echo "  Compiling $CHAPTER..."
    for pass in {1..4}; do
        pdflatex -synctex=1 -interaction=nonstopmode "${CHAPTER}.tex" > /dev/null 2>&1 || {
            echo "    ERROR in pass $pass for $CHAPTER"
            exit 1
        }
    done
    # Check for errors
    if grep -q "^!" "${CHAPTER}.log"; then
        echo "    ERROR found in $CHAPTER.log"
        grep "^!" "${CHAPTER}.log"
        exit 1
    fi
    # Move PDF
    cp "${CHAPTER}.pdf" "$PDF_DIR/"
    echo "    ✓ $CHAPTER compiled successfully"
done

# Compile all English chapters (14-44)
echo "Compiling English chapters..."
for i in {14..44}; do
    CHAPTER=$(printf "Kapitel_%02d_Narrative_En" $i)
    echo "  Compiling $CHAPTER..."
    for pass in {1..4}; do
        pdflatex -synctex=1 -interaction=nonstopmode "${CHAPTER}.tex" > /dev/null 2>&1 || {
            echo "    ERROR in pass $pass for $CHAPTER"
            exit 1
        }
    done
    # Check for errors
    if grep -q "^!" "${CHAPTER}.log"; then
        echo "    ERROR found in $CHAPTER.log"
        grep "^!" "${CHAPTER}.log"
        exit 1
    fi
    # Move PDF
    cp "${CHAPTER}.pdf" "$PDF_DIR/"
    echo "    ✓ $CHAPTER compiled successfully"
done

echo "All chapters compiled successfully!"
