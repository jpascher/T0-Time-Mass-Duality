# Chapter File Format Instructions (DE/EN Narrative, 44 Chapters)

Branch: `copilot/reset-copilot-narrative`
Directory: `2/narrative`

This document defines the **exact** format for all DE/EN chapter files and how to convert from the existing standalone files.

**Current state:** The directories `de_chapters/` and `en_chapters/` are currently empty on branch `copilot/reset-copilot-narrative`. Copilot must (re)create all 44 DE/EN chapter files from the standalones using these rules.

---

## 1. Source and Target Files

For each chapter `XX = 01..44`:

- **German standalone (source)** 
 `2/narrative/de_standalone/Kapitel_XXa_Narrative_De.tex`

- **English standalone (source)** 
 `2/narrative/en_standalone/Kapitel_XXa_Narrative_En.tex`

- **German chapter (target)** 
 `2/narrative/de_chapters/Kapitel_XX_Narrative_De.tex`

- **English chapter (target)** 
 `2/narrative/en_chapters/Kapitel_XX_Narrative_En.tex`

The **standalone files keep their full LaTeX preamble** and are used for per-chapter PDFs. 
The **chapter files do NOT contain a preamble** and are included by the DE/EN master documents.

---

## 2. Chapter Heading Format

All chapters are **numbered** and use `\chapter{...}` (not `\chapter*`).

### 2.1 German chapters

At the top of each `de_chapters/Kapitel_XX_Narrative_De.tex`:

```latex
\chapter{Kapitel XX: <TitelAusStandalone>}
% optional: \label{chap:XX}

% then the rest of the chapter content
```

- `XX` is the two-digit chapter number (`01`, `02`, ..., `44`).
- `<TitelAusStandalone>` is taken from the German `\title{...}` in the corresponding standalone file.
- After `\chapter{...}` the existing content (sections, text, formulas, etc.) follows unchanged.

### 2.2 English chapters

At the top of each `en_chapters/Kapitel_XX_Narrative_En.tex`:

```latex
\chapter{Chapter XX: <TitleFromStandalone>}
% optional: \label{chap:XX-en}

% then the rest of the chapter content
```

- `XX` is the two-digit chapter number.
- `<TitleFromStandalone>` is taken from the English `\title{...}` in the EN standalone file.

No other special formatting is required directly after `\chapter{...}`.

---

## 3. Converting From Standalone to Chapter Files

For each chapter `XX`:

### 3.1 German

1. Open `de_standalone/Kapitel_XXa_Narrative_De.tex`.
2. Ignore and **do NOT copy**:
  - the entire preamble (everything before `\begin{document}`),
  - `\begin{document}` and `\end{document}`.
3. In the chapter file `de_chapters/Kapitel_XX_Narrative_De.tex`:
  - **Remove** the following if present:
   ```latex
   \title{...}
   \author{...}
   \date{...}
   \maketitle
   ```
  - **Insert instead** (at the top of the file):
   ```latex
   \chapter{Kapitel XX: <TitelAusStandalone>}
   % optional: \label{chap:XX}
   ```
  - Then copy over all remaining content from the standalone (sections, text, math).

### 3.2 English

1. Open `en_standalone/Kapitel_XXa_Narrative_En.tex`.
2. Again, **do NOT copy** the preamble, `\begin{document}` or `\end{document}`.
3. In the chapter file `en_chapters/Kapitel_XX_Narrative_En.tex`:
  - **Remove** any `\title{...}`, `\author{...}`, `\date{...}`, `\maketitle`.
  - **Insert instead**:
   ```latex
   \chapter{Chapter XX: <TitleFromStandalone>}
   % optional: \label{chap:XX-en}
   ```
  - Copy over all remaining content from the English standalone.

---

## 4. Handling Abstracts / Summaries

If a standalone contains an abstract or summary at the top, e.g.:

```latex
\section*{Abstract}
...
```

or

```latex
\section*{Zusammenfassung}
...
```

or an `abstract` environment, then **in the chapter files** this must become a **numbered** section:

### 4.1 English

```latex
% standalone:
\section*{Abstract}
...

% in the chapter file:
\section{Abstract}
...
```

### 4.2 German

```latex
% standalone:
\section*{Zusammenfassung}
...

% in the chapter file:
\section{Zusammenfassung}
...
```

This ensures the abstract appears in the table of contents.

---

## 5. Master Documents

The master documents include the chapter files (not the standalones):

- **German master:** `2/narrative/FFGFT_Narrative_Master_De.tex` 
 Should contain:
 ```latex
 % inside the document body
 \input{de_chapters/Kapitel_01_Narrative_De}
 \input{de_chapters/Kapitel_02_Narrative_De}
 ...
 \input{de_chapters/Kapitel_44_Narrative_De}
 ```

- **English master:** `2/narrative/FFGFT_Narrative_Master_En.tex` 
 Should contain:
 ```latex
 \input{en_chapters/Kapitel_01_Narrative_En}
 \input{en_chapters/Kapitel_02_Narrative_En}
 ...
 \input{en_chapters/Kapitel_44_Narrative_En}
 ```

The symbol legends are already included right after the table of contents:

- DE: `\input{Zentrale_Zeichenerklaerung_De}` 
- EN: `\input{Zentrale_Zeichenerklaerung_En}`

---

## 6. Summary for Automation (Copilot Agent)

For each chapter XX (01–44) and for both DE and EN:

1. Create/overwrite `de_chapters/Kapitel_XX_Narrative_De.tex` and `en_chapters/Kapitel_XX_Narrative_En.tex` from the corresponding standalone files, using the rules in sections 2–4.
2. Use **numbered** `\chapter{...}` with the full title string taken from the standalone `\title{...}`.
3. Convert `\section*{Abstract}` / `\section*{Zusammenfassung}` (or `abstract` environments) into numbered sections in the chapter files.
4. Ensure the master documents input all 44 DE/EN chapter files as listed in section 5.
5. Rebuild both master PDFs and check for LaTeX errors.

