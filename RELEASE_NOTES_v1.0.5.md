# T0 Theory v1.0.5 – Asymmetry Monograph & Book Mapping Update

**Release Date:** 2026-01-21  
**Version:** 1.0.5  
**DOI (unchanged):** 10.5281/zenodo.17522475

---

## 1. Overview

This public update adds a new compiled **Asymmetry Monograph** (German/English) to the T0/FFGFT book set and refines how the repository documents the mapping between published Amazon books and the canonical PDFs. The underlying T0 / FFGFT theory is unchanged; all new material is explanatory and structural.

---

## 2. New Asymmetry Monograph (Book 7)

### 2.1 New Compiled Internal Monograph

A new two-part **internal mathematical monograph** on fundamental asymmetries in physics has been compiled as a technical PDF in both German and English (currently **not intended for public Amazon publication**):

- **German PDF:** `2/pdf/144_Asymmetrie-Master_De.pdf`  
- **English PDF:** `2/pdf/144_Asymmetrie-Master_En.pdf`

These PDFs collect and extend the content of the former standalone documents `143_Asymmetrie-teil1_*` and `144_Asymmetrie-teil2_*` into a single coherent volume for further internal mathematical development.

### 2.2 Scientific Focus

The Asymmetry Monograph documents:

- How the FFGFT / T0 framework treats **asymmetry as a central structural feature** of spacetime and fields, not a perturbation.  
- A detailed analysis of what is lost when setting fundamental constants to 1 in natural units (\(c = 1\), \(\hbar = 1\), \(G = 1\), \(\alpha = 1\)), with emphasis on:
  - Loss of **dynamical information** when setting \(c = 1\).  
  - Loss of **fractal interaction structure** and geometric coupling scales when setting \(\alpha = 1\).  
- The role of **variable mass** and fractal geometry in distinguishing FFGFT from standard Relativity (RT) and conventional quantum field theory.
- A consistent **deterministic “theory of everything” perspective** where the mathematical model remains compatible with conscious agency and apparent free choice.

### 2.3 Ontological Perspective

The book explicitly addresses the ontological status of physical quantities and measurements:

- In practice we always measure **frequency changes**; which underlying quantity "really" changes (mass, time, length, or geometry) is **ontologically underdetermined**.
- No conceivable experiment can decide which of several ontologically equivalent reformulations is “truly real”; only mathematical consistency and predictive power matter.
- FFGFT keeps this **ontological freedom** explicit: mass can be made variable (as in RT), or other quantities could be held fixed – the theory is formulated so that different choices remain mathematically consistent.

The Asymmetry Monograph collects these arguments in one place for readers who want a clear, extended explanation beyond the brief remarks in earlier documents.

---

## 3. LaTeX Source Integration

The LaTeX sources for the Asymmetry Monograph are now fully integrated into the `2/tex-n/` tree:

- **Chapters (book integration):**  
  - `2/tex-n/en_chapters_new/143_Asymmetrie-teil1_En_ch.tex`  
  - `2/tex-n/en_chapters_new/144_Asymmetrie-teil2_En_ch.tex`  
  - `2/tex-n/de_chapters_new/143_Asymmetrie-teil1_De_ch.tex`  
  - `2/tex-n/de_chapters_new/144_Asymmetrie-teil2_De_ch.tex`

- **Master book files:**  
  - `2/tex-n/completed/144_Asymmetrie-Master_En.tex`  
  - `2/tex-n/completed/144_Asymmetrie-Master_De.tex`

- **Standalone versions (articles):**  
  - `2/tex-n/en_standalone/143_Asymmetrie-teil1_En.tex`, `144_Asymmetrie-teil2_En.tex`  
  - `2/tex-n/de_standalone/143_Asymmetrie-teil1_De.tex`, `144_Asymmetrie-teil2_De.tex`

Table of contents (TOC) handling has been cleaned so that all relevant sections appear correctly in both the book and standalone PDFs.

---

## 4. README & Structure Updates

The main READMEs have been updated to reflect the new state:

- **LaTeX source structure:**  
  - Now documented under `2/tex-n/` (instead of `2/tex/`).  
  - The number of compiled books has been updated from 6 to **7**, counting the new Asymmetry Monograph (DE/EN) as the seventh book.
- **Highlights section:**  
  - A new entry "Asymmetry Analysis – New FFGFT Monograph" links to the German and English Asymmetry-Master PDFs and briefly explains their role within the overall theory.

These changes are purely organizational and documentation-oriented; no formulas or numerical predictions were altered.

---

## 5. Published Books → Repository PDFs (Recap)

The mapping between **published Amazon books** (Kindle / paperback / hardcover) and their canonical PDFs in this repository was already clarified in v1.0.4 and is now fully consistent with the updated README section **"Published Books – Repository PDFs"**. For convenience, the ten published books and their PDF counterparts are:

1. **T0 Theory: Time-Mass Duality: Unified Physics from a Single Number: Complete Spacetime Geometry Synthesis** (English)  
   - PDF: `2/tex-n/completed/Teil1.ebook_En.pdf`

2. **T0-Theorie Zeit Masse Dualität: Die vereinheitlichte Physik aus einer einzigen Zahl – Eine vollständige Synthese der Raumzeit-Geometrie** (Deutsch)  
   - PDF: `2/tex-n/completed/Teil1.ebook_De.pdf`

3. **T0-Theorie Teil (Teil2) Zeit- Masse Dualität: Vereinheitlichte Physik aus einer einzigen Zahl: Vollständige Synthese der Raumzeit-Geometrie** (Deutsch)  
   - PDF: `2/tex-n/completed/Teil2.ebook_De.pdf`

4. **T0 Theory 2- Time Mass Duality: A Geometric Framework for Unifying Time, Mass, and Quantum Realities** (English)  
   - PDF: `2/tex-n/completed/Teil2.ebook_En.pdf`

5. **T0 Theory (part 3) Time-Mass Duality: Unified Physics from a Single Number: Complete Spacetime Geometry Synthesis** (English)  
   - PDF: `2/tex-n/completed/Teil3.ebook_En.pdf`

6. **T0-Theorie: Zeit-Masse-Dualität – (Teil 3): Vereinheitlichte Physik aus einer einzigen Zahl: Vollständige Synthese der Raumzeit-Geometrie** (Deutsch)  
   - PDF: `2/tex-n/completed/Teil3.ebook_De.pdf`

7. **What Lies Behind the Seven Mysteries of Physics?: A Journey to the Universe's Deepest Secrets – and How a New Theory Connects Them** (English)  
   - PDF: `2/tex-n/completed/T0_Anwendungen_En.pdf`

8. **Was verbirgt sich hinter den sieben Rätseln der Physik?: Eine Reise zu den tiefsten Geheimnissen des Universums – und wie eine neue Theorie sie verbindet** (Deutsch)  
   - PDF: `2/tex-n/completed/T0_Anwendungen_De.pdf`

9. **Das Kosmische Gehirn: Von der Quantengravitation zum Bewusstsein. Fundamental Fraktalgeometrischen Feldtheorie (FFGFT)** (Deutsch)  
   - PDF: `2/pdf/FFGFT_Narrative_Master_De.pdf`

10. **The Cosmic Brain: From Quantum Gravity to Consciousness, fundamental Fractal-Geometric Field Theory (FFGFT)** (English)  
    - PDF: `2/pdf/FFGFT_Narrative_Master_En.pdf`

The new **Asymmetry Monograph** is currently documented and compiled in the repository but is **not yet tied to a specific public Amazon edition**; once published, it will be added to this list and the README mapping.

---

## 6. Recommended Reading Order with Asymmetry Monograph

For readers who want to understand the role of asymmetry and natural units within T0/FFGFT, a suggested path is:

1. Start with the narrative books (`FFGFT_Narrative_Master_*.pdf`) or the "Seven Mysteries" books (`T0_Anwendungen_*.pdf`) for an accessible overview.  
2. Study the core trilogy (`Teil1/2/3.ebook_*.pdf`) for full technical foundations and derivations.  
3. Read the **Asymmetry Monograph** (`144_Asymmetrie-Master_*.pdf`) for a focused, extended discussion of asymmetries, natural-unit choices (\(c, \hbar, G, \alpha\)), and the ontological limitations of measurement.  
4. Use the individual technical PDFs in `2/pdf/` for detailed references, numeric tables, and historical development.

---

## 7. Impact on Existing Work

- No existing prediction, derivation, or numerical result has been changed in this release.  
- All updates are **additive and clarifying**, consolidating earlier discussions about asymmetry, natural units, and ontology into a dedicated monograph and improving documentation for external readers.
