# Copilot Task: Rebuild DE/EN Narrative Masters with Recursive Error Fixing

Branch: `copilot/reset-copilot-narrative` 
Directory: `2/narrative`

This document defines how Copilot should rebuild the German and English narrative master PDFs and fix LaTeX errors iteratively.

---

## 1. LaTeX Environment (Install ONCE at Start)

Before doing anything else (editing files, running `pdflatex`, etc.), ensure a minimal LaTeX environment is installed on the runner.

On Ubuntu-based runner, run **once**:

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

## 2. Master Documents and Preambles

Master files (both already wired to 6x9" Kindle preambles via `T0_preamble_shared_*.tex`):

- German master: 
 `FFGFT_Narrative_Master_De.tex`

- English master: 
 `FFGFT_Narrative_Master_En.tex`

Both now use:

```latex
\documentclass[12pt]{book}
% Use the shared preamble
\input{../../T0_preamble_shared_De} % or _En
```

Do **not** change the document class or shared preamble wiring.

---

## 3. Rebuild and Fix: German Master

1. Change into the narrative directory:

```bash
cd 2/narrative
```

2. Compile the German master multiple times:

```bash
for i in {1..4}; do
 pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex
done
```

3. Inspect `FFGFT_Narrative_Master_De.log` after the runs:
  - Look for any `! LaTeX Error:` lines.
  - Check for missing files, bad `\input` paths, unmatched `\begin{...}` / `\end{...}`.

4. Fix any DE-related issues **only where errors occur**, preferably in:
  - The DE chapter files included by the master.
  - The master itself if an `\input` or structure is wrong.

5. Repeat steps 2–4 until `FFGFT_Narrative_Master_De.tex` compiles **without LaTeX errors** (only non-critical warnings allowed).

> Note: DE standalones are the primary text source; keep their structure intact unless a LaTeX error forces a minimal fix.

---

## 4. Rebuild and Fix: English Master

1. From `2/narrative`, compile the English master multiple times:

```bash
for i in {1..4}; do
 pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex
done
```

2. Inspect `FFGFT_Narrative_Master_En.log` after the runs:
  - Look for `! LaTeX Error:` lines.
  - Check for:
   - missing `en_chapters/Kapitel_XX_Narrative_En.tex` files,
   - bad `\input` paths,
   - unmatched environments,
   - undefined commands or labels.

3. Fix errors by editing **only EN-related sources**:
  - `en_chapters/Kapitel_XX_Narrative_En.tex` (chapter structure, sections, environments),
  - `FFGFT_Narrative_Master_En.tex` (order and list of `\input` statements).

4. If necessary, regenerate missing EN chapter files from `en_standalone/Kapitel_XXa_Narrative_En.tex` following:
  - `CHAPTER_FORMAT_INSTRUCTIONS.md`
  - `COPILOT_NEXT_STEPS.md`
  - `COPILOT_EN_MASTER_FIX.md`

5. Repeat compilation and log analysis until the EN master compiles **without LaTeX errors**.

---

## 5. Constraints

- Do **not** commit or add PDF files to git; only `.tex` and related text sources are versioned.
- Do not change the shared preambles `T0_preamble_shared_De.tex` / `T0_preamble_shared_En.tex` in this task.
- Do not introduce new local symbol legend boxes inside chapters; use only:
 - `Zentrale_Zeichenerklaerung_De.tex`
 - `Zentrale_Zeichenerklaerung_En.tex`

---

## 6. Expected Result

- `FFGFT_Narrative_Master_De.tex` and `FFGFT_Narrative_Master_En.tex` both compile cleanly (no LaTeX errors) with the minimal LaTeX setup.
- The resulting PDFs have 6"x9" page size (driven by the shared preambles) and are suitable for KDP upload.


