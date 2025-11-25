#!/bin/bash
#
# Compile T0 Book LaTeX files to PDF
# Usage: ./compile_books.sh [book1|book2|book3|book4|all]
#
# Examples:
#   ./compile_books.sh          # Compile all four books
#   ./compile_books.sh book1    # Compile T0_Book1_En.tex only
#   ./compile_books.sh book2    # Compile T0_Book_En.tex only  
#   ./compile_books.sh book3    # Compile T0_Book3_En.tex only
#   ./compile_books.sh book4    # Compile T0_Book4_En.tex only (complete collection)
#   ./compile_books.sh all      # Compile all four books
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Book definitions
declare -A BOOKS
BOOKS["book1"]="T0_Book1_En.tex"
BOOKS["book2"]="T0_Book_En.tex"
BOOKS["book3"]="T0_Book3_En.tex"
BOOKS["book4"]="T0_Book4_En.tex"

compile_book() {
    local book_file="$1"
    local book_name="${book_file%.tex}"
    
    if [ ! -f "$book_file" ]; then
        echo -e "${RED}Error: $book_file not found${NC}"
        return 1
    fi
    
    echo -e "${YELLOW}Compiling $book_file...${NC}"
    
    # First pass
    echo "  Pass 1/2..."
    pdflatex -interaction=nonstopmode "$book_file" > /dev/null 2>&1 || {
        echo -e "${RED}  Error in first pass. Running with output...${NC}"
        pdflatex -interaction=nonstopmode "$book_file"
        return 1
    }
    
    # Second pass (for references and TOC)
    echo "  Pass 2/2..."
    pdflatex -interaction=nonstopmode "$book_file" > /dev/null 2>&1 || {
        echo -e "${RED}  Error in second pass. Running with output...${NC}"
        pdflatex -interaction=nonstopmode "$book_file"
        return 1
    }
    
    # Get page count
    if command -v pdfinfo &> /dev/null; then
        pages=$(pdfinfo "${book_name}.pdf" 2>/dev/null | grep Pages | awk '{print $2}')
        echo -e "${GREEN}  Success: ${book_name}.pdf ($pages pages)${NC}"
    else
        echo -e "${GREEN}  Success: ${book_name}.pdf${NC}"
    fi
}

clean_aux_files() {
    echo "Cleaning auxiliary files..."
    rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz 2>/dev/null || true
    echo "Done."
}

show_help() {
    echo "T0 Book Compilation Script"
    echo ""
    echo "Usage: $0 [OPTION]"
    echo ""
    echo "Options:"
    echo "  book1       Compile T0_Book1_En.tex (comprehensive, ~580 pages)"
    echo "  book2       Compile T0_Book_En.tex (original, ~88 pages)"
    echo "  book3       Compile T0_Book3_En.tex (no boxes, ~526 pages)"
    echo "  book4       Compile T0_Book4_En.tex (complete collection, all chapters)"
    echo "  all         Compile all four books (default)"
    echo "  clean       Remove auxiliary files (.aux, .log, .out, .toc, etc.)"
    echo "  help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0              # Compile all books"
    echo "  $0 book1        # Compile comprehensive book only"
    echo "  $0 book4        # Compile complete collection"
    echo "  $0 clean        # Clean up auxiliary files"
}

# Main
case "${1:-all}" in
    book1)
        compile_book "${BOOKS[book1]}"
        ;;
    book2)
        compile_book "${BOOKS[book2]}"
        ;;
    book3)
        compile_book "${BOOKS[book3]}"
        ;;
    book4)
        compile_book "${BOOKS[book4]}"
        ;;
    all)
        echo "Compiling all T0 Books..."
        echo ""
        compile_book "${BOOKS[book1]}"
        echo ""
        compile_book "${BOOKS[book2]}"
        echo ""
        compile_book "${BOOKS[book3]}"
        echo ""
        compile_book "${BOOKS[book4]}"
        echo ""
        echo -e "${GREEN}All books compiled successfully!${NC}"
        ;;
    clean)
        clean_aux_files
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown option: $1${NC}"
        show_help
        exit 1
        ;;
esac
