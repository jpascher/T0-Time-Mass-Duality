# PDF Directory Structure

This directory contains all compiled PDF files from the T0-Time-Mass-Duality project.

## Directory Organization

### `nummeriert/`
Contains all standalone document PDFs, numbered according to the source filenames.

- **German documents**: Files ending with `_De.pdf`
- **English documents**: Files ending with `_En.pdf`
- Total: 205+ standalone documents (103 DE + 102 EN)

**Examples:**
- `001_T0_Book_Abstract_De.pdf`
- `018_T0_Anomale-g2-9_De.pdf`
- `003_T0_Grundlagen_En.pdf`

### Book PDFs

The compiled books are located in `2/tex/completed/`:
- **German books**: `2/tex/completed/deutsch/`
  - `Teil1_De.pdf`
  - `Teil2_De.pdf`
  - `Teil3_De.pdf`
  - `Test_Landscape_De.pdf`

- **English books**: `2/tex/completed/english/`
  - `Teil1_En.pdf`
  - `Teil2_En.pdf`
  - `Teil3_En.pdf`
  - `Test_Landscape_En.pdf`

## Notes

- All PDFs are generated from LaTeX source files in `2/tex/de_standalone/` and `2/tex/en_standalone/`
- Book PDFs are compiled from chapter files in `2/tex/de_chapters_new/` and `2/tex/en_chapters_new/`
- Compilation artifacts (`.aux`, `.log`, `.out`, `.toc`, etc.) are regularly cleaned up
