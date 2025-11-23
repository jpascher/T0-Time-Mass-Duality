# English Book Skeleton

This directory contains a skeleton setup for building the unified English T0 book.

## Files

- 1_sceleton.py
  Placeholder script. Will be filled with logic to:
  - extract content between \begin{document} and \end{document},
  - strip document-local headers,
  - normalize labels and references,
  - replace unicode symbols,
  - generate chapters_en_sceleton/*.tex,
  - generate T0_Book_En_sceleton.tex.

- T0_Book_En_sceleton.tex
  Minimal book preamble. Intended to include generated chapter files.

- build_book_sceleton.bat
  Simple Windows batch to:
    1. run 'py 1_sceleton.py',
    2. run 'pdflatex' on 'T0_Book_En_sceleton.tex'.

- chapters_en_sceleton/
  Target directory for generated chapter files.

## Next steps

1. Run:

   cd 2\tex
   py setup_sceleton.py

2. Commit and push the newly created files and directories.

3. Copilot will then fill '1_sceleton.py' with the actual transformation logic,
   and use 'T0_Book_En_sceleton.tex' as the main book file for the unified English book.
