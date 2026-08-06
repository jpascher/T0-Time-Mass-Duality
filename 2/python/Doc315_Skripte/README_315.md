# Dok. 315 / Doc. 315 — Die Form von K_frak: additiv oder multiplikativ?
# The Form of K_frak: Additive or Multiplicative?

Arbeitsdokument (kein A-Serie-Dokument) · Working document (not part of the A-Series)
Stand / As of: 6. August 2026 · Autor / Author: Johann Pascher

## Inhalt / Contents
- Sources/ch/315_Kfrak_Form_De_ch.tex   — Kapitelinhalt Deutsch
- Sources/ch/315_Kfrak_Form_En_ch.tex   — chapter content English
- Sources/wr_standalone_A4/315_Kfrak_Form_De.tex — Header/Wrapper Deutsch (A4-Standalone)
- Sources/wr_standalone_A4/315_Kfrak_Form_En.tex — header/wrapper English (A4 standalone)
- pdf/315_Kfrak_Form_De.pdf, pdf/315_Kfrak_Form_En.pdf — kompilierte Fassungen / compiled versions
- python/315_Skripte/ — vier Prüfskripte, reine Standardbibliothek / four check scripts, standard library only

## Bauen / Build
Aus Sources/wr_standalone_A4/ (Präambeln ../pri-end/ aus dem Repo-Bestand):
  lualatex -interaction=nonstopmode 315_Kfrak_Form_De.tex   (3x, wegen TOC)
  lualatex -interaction=nonstopmode 315_Kfrak_Form_En.tex   (3x)
Umgebung: setup_build_env.sh im Repo-Root (Fonts Inter, JetBrains Mono, Libertinus Math).

## Verifikation / Verification
  python3 python/315_Skripte/euler_spirale_7limit.py
  python3 python/315_Skripte/pruefrechnung_kfrak_form.py
  python3 python/315_Skripte/pruefrechnung_p_identitaet.py
  python3 python/315_Skripte/pruefrechnung_rest_0p1xi.py

## Bezüge / References
A040, A130, A270, Dok. 190 (R67, R70, R72), Dok. 295/313 (Schließungsgabelung /
closure fork), Dok. 314 (D4 im Hilbertraum; Packungsdichte π²/16 / packing density).
Offene Punkte / open items: P-315-1, P-315-2, P-315-3, P35 (verengt / narrowed).
