# Copilot Task: Fix English Narrative Master Build

Branch: `copilot/reset-copilot-narrative`  
Directory: `2/narrative`

This document defines the exact task for Copilot to fix the **English** master build while keeping the **German** side stable.

---

## 1. LaTeX Minimal Installation (ONE TIME at Start)

Before doing ANYTHING else (editing files, running `pdflatex`, etc.):

On an Ubuntu-based runner, run **once**:

```bash
sudo apt-get update
sudo apt-get install -y \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-science \
  texlive-lang-english \
  texlive-lang-german
```

After this, use `pdflatex` freely, but **do not reinstall** LaTeX in loops.

---

## 2. Current State

- The **German master** `FFGFT_Narrative_Master_De.tex` compiles locally without fatal errors.  
  → **Do NOT change** DE standalones, DE chapters or the DE master (read-only).
- The **English master** `FFGFT_Narrative_Master_En.tex` currently **does NOT build cleanly**.  
  → Your job is to bring the EN master to the same stable level.
- Guidance documents:
  - `CHAPTER_FORMAT_INSTRUCTIONS.md`
  - `COPILOT_NEXT_STEPS.md`
  - `KINDLE_OPTIMIZATION_GUIDE.md`

---

## 3. Recreate and Wire EN Chapter Files

Work only on **English** chapter-related files in `2/narrative`:

- EN standalones (sources):
  - `en_standalone/Kapitel_XXa_Narrative_En.tex` (44 files)
- EN chapters (targets to be recreated):
  - `en_chapters/Kapitel_XX_Narrative_En.tex` (44 files, currently empty directory)

For each chapter `XX = 01..44`:

1. Open `en_standalone/Kapitel_XXa_Narrative_En.tex`.
2. In the corresponding chapter file `en_chapters/Kapitel_XX_Narrative_En.tex`:
   - Do **NOT** include any preamble or `\\begin{document}`/`\\end{document}`.
   - Remove any old `\\title{...}`, `\\author{...}`, `\\date{...}`, `\\maketitle` if present.
   - Insert at the very top:
     ```latex
     \\chapter{Chapter XX: <TitleFromStandalone>}
     % optional: \\label{chap:XX-en}

     % then the rest of the chapter content
     ```
   - Copy over the remaining content from the EN standalone (sections, text, math),
     following the rules in `CHAPTER_FORMAT_INSTRUCTIONS.md` (e.g. Abstract handling).

### Abstract / Summary Handling (EN)

- If the standalone contains at the top:
  ```latex
  \\section*{Abstract}
  ...
  ```
  then in the **chapter file** this must become a **numbered** section:
  ```latex
  \\section{Abstract}
  ...
  ```

This ensures the abstract appears in the table of contents and in the correct place in the structure.

---

## 4. Master EN Document Wiring

In `FFGFT_Narrative_Master_En.tex`, ensure that inside the document body you only have `\\input` lines for the EN chapter files, e.g.:

```latex
\\input{en_chapters/Kapitel_01_Narrative_En}
\\input{en_chapters/Kapitel_02_Narrative_En}
...
\\input{en_chapters/Kapitel_44_Narrative_En}
```

There should be **no remaining references** to old `*_content` files or other legacy inputs.

The DE master file and DE-related inputs must not be changed.

---

## 5. Recursive EN Master Fix (Build Until Clean)

After all 44 EN chapter files have been recreated/updated and the master wiring is correct:

1. In `2/narrative`, compile the EN master multiple times:
   ```bash
   cd 2/narrative
   for i in {1..4}; do
     pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex
   done
   ```
2. After each run, inspect the `.log` file for:
   - Missing files or `! LaTeX Error` messages.
   - Unmatched `\\begin{...}` / `\\end{...}`.
   - Bad `\\input` paths or undefined control sequences.
3. Fix the corresponding EN chapter files or the EN master until:
   - `FFGFT_Narrative_Master_En.tex` compiles **without fatal errors**.
   - Only non-critical warnings (e.g. harmless underfull boxes) remain.

Do **not** touch the DE master or DE chapters during this process.

---

## 6. Constraints and Reminders

- DE side (standalones, chapters, master) is read-only: do not modify its structure or content.
- Do not add any new local symbol/legend boxes inside chapters or standalones; use only the central legend files:
  - `Zentrale_Zeichenerklaerung_De.tex`
  - `Zentrale_Zeichenerklaerung_En.tex`
- Do not commit or add PDF files to git; only `.tex` and related sources are versioned.

---

## 7. Expected Outcome

- `FFGFT_Narrative_Master_En.tex` compiles cleanly with the installed minimal LaTeX environment.
- All 44 EN chapter files exist in `en_chapters/` and follow the format defined in `CHAPTER_FORMAT_INSTRUCTIONS.md`.
- The DE master remains unchanged and continues to compile successfully.

