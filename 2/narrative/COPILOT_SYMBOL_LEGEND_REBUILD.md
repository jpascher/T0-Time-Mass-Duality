# Copilot Task: Rebuild and Extend Central Symbol Legend (DE/EN)

Branch: `copilot/reset-copilot-narrative`  
Directory: `2/narrative`

Goal: Create a **consistent, comprehensive symbol legend** for all DE/EN narrative chapters, and update:
- `Zentrale_Zeichenerklaerung_De.tex`
- `Zentrale_Zeichenerklaerung_En.tex`

so that they actually match the notation used across all 44 chapters.

---

## 1. Source Files to Scan

Scan the following LaTeX sources for symbols, units, and abbreviations:

- DE standalones (semantic ground truth):
  - `de_standalone/Kapitel_XXa_Narrative_De.tex` for `XX = 01..44`
- EN standalones:
  - `en_standalone/Kapitel_XXa_Narrative_En.tex` for `XX = 01..44`
- DE/EN chapters (structure/usage check):
  - `de_chapters/Kapitel_XX_Narrative_De.tex`
  - `en_chapters/Kapitel_XX_Narrative_En.tex`

Do **not** change the semantics of the chapters; use them only to see which symbols and units appear.

---

## 2. What to Collect

For each symbol/notation that appears in formulas or text, collect:

- The raw symbol (as used in LaTeX), e.g.:
  - `\xi`, `D_f`, `a_0`, `m_0^\nu`, `H_0`, `c`, `\hbar`, `G`, `\alpha`, etc.
- A **short, precise description** in:
  - German (for DE legend)
  - English (for EN legend)
- The physical unit (if applicable), using `siunitx`, e.g.:
  - `\si{\meter}`, `\si{\joule}`, `\si{\eV}`, `\si{\second}`, `\si{\kilo\gram}`.
- The **typical role** (parameter, field, coordinate, observable, etc.).

Focus especially on:
- Core theory parameters: `\xi`, `D_f`, `l_0`, time/mass variables.
- Cosmological quantities: `H_0`, `\Omega`, redshift `z`, CMB quantities, etc.
- Quantum/mechanics constants: `\hbar`, `c`, `\alpha`, particle masses, neutrino parameters.
- Any custom-defined commands/macros from the preambles and chapters.

---

## 3. Structure of the New Legend Files

Update **both**:
- `Zentrale_Zeichenerklaerung_De.tex`
- `Zentrale_Zeichenerklaerung_En.tex`

so that they share the same structure, with language-specific descriptions.

### 3.1 Suggested structure

Use a table-based structure with clear columns, for example:

```latex
\chapter*{Zentrale Zeichenerklärung}
\addcontentsline{toc}{chapter}{Zentrale Zeichenerklärung}

\begin{longtable}{p{0.18\textwidth}p{0.22\textwidth}p{0.45\textwidth}}
  \toprule
  \textbf{Symbol} & \textbf{Einheit} & \textbf{Bedeutung} \\
  \midrule
  \endfirsthead

  \toprule
  \textbf{Symbol} & \textbf{Einheit} & \textbf{Bedeutung} \\
  \midrule
  \endhead

  % ... entries ...

  \bottomrule
\end{longtable}
```

For English:

```latex
\chapter*{Central Symbol Legend}
\addcontentsline{toc}{chapter}{Central Symbol Legend}

\begin{longtable}{p{0.18\textwidth}p{0.22\textwidth}p{0.45\textwidth}}
  \toprule
  \textbf{Symbol} & \textbf{Unit} & \textbf{Meaning} \\
  \midrule
  \endfirsthead

  \toprule
  \textbf{Symbol} & \textbf{Unit} & \textbf{Meaning} \\
  \midrule
  \endhead

  % ... entries ...

  \bottomrule
\end{longtable}
```

Use `siunitx` for units:
- `\si{\meter}`, `\si{\second}`, `\si{\joule}`, `\si{\eV}`, etc.
- Leave unit column blank for dimensionless parameters where appropriate.

---

## 4. How to Build the Legend Systematically

1. For each symbol found in the sources, classify it into one of these categories:
   - Fundamental constants (e.g. `c`, `\hbar`, `G`, `k_B`).
   - Theory parameters (`\xi`, `D_f`, `l_0`, etc.).
   - Fields and variables (\(\Phi\), coordinates, time, mass, etc.).
   - Cosmological parameters.
   - Particle physics parameters (masses, couplings, mixing angles).

2. For each category, sort symbols alphabetically.
3. Create parallel entries in DE and EN legend files with matching ordering.
4. Ensure every **non-trivial** symbol used in the narrative (and not obvious like `x`, `t`) appears in the legend.
5. Remove or update any outdated entries from previous legend versions that no longer match the current notation.

---

## 5. Constraints

- Do **not** change the chapter content semantically; only **read** it to infer the correct descriptions.
- Keep both legend files synchronized in structure and ordering.
- Do not introduce new notations that are not used in the chapters.
- Do not add symbol legend boxes back into individual chapters; the legend stays central.

---

## 6. Final Checks

1. After updating both legend files, recompile:
   - `FFGFT_Narrative_Master_De.tex`
   - `FFGFT_Narrative_Master_En.tex`

2. Verify:
   - The legend chapters appear right after the table of contents (already wired in masters).
   - The tables render correctly without overfull boxes.
   - No unknown symbol in the legend (all appear in the chapters), and no important symbol used in chapters is missing from the legend.

Once done, commit the updated `Zentrale_Zeichenerklaerung_De.tex` and `Zentrale_Zeichenerklaerung_En.tex` and push to `copilot/reset-copilot-narrative`.

