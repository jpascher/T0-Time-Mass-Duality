#!/usr/bin/env python3
"""
Automatisches, inkrementelles Kapitel-Skript mit Fehlererkennung,
gemeinsamer Kompilation aller bisherigen Kapitel und automatischer
Makro-Erzeugung, ohne Standard-LaTeX-Kommandos zu überschreiben.
Zusätzlich:
- Problematische Makros wie checkmarkx, warningx werden im generierten
  Text auf neue Namen (z.B. checkmarkxa, warningxa) umgebogen, damit
  bestehende Definitionen nicht kollidieren.
Optimierungen: Kompilierte Regex, erweiterte Standard-Makros, originale Hardcode-Liste.
Fixes: Alle Regex-Patterns als raw strings mit doppeltem Backslash (verhindert 'bad escape \\p'), geteilte Preamble.
"""
from pathlib import Path
import re
import json
import subprocess
import shutil
import sys

BASE = Path(__file__).parent
CHAPTER_DIR = BASE / "chapters_en"
FINAL_DIR = BASE / "chapters_en_final"
STATE_FILE = BASE / "state.json"
TEST_TEX = BASE / "_test_all_chapters.tex"
USE_LATEXMK = True  # Setze auf False für reines pdflatex

# Originale Hardcode-Liste für ENABLED_CHAPTERS (aus erster Anfrage)
ENABLED_CHAPTERS = [
    "T0_Grundlagen_En.tex",
    "T0_Modell_Uebersicht_En.tex",
    "T0_tm-erweiterung-x6_En.tex",
    "T0_Teilchenmassen_En.tex",
    "T0_Neutrinos_En.tex",
    "T0_xi-und-e_En.tex",
    "T0_xi_ursprung_En.tex",
    "xi_parmater_partikel_En.tex",
    "T0_Energie_En.tex",
    "T0_Feinstruktur_En.tex",
    "T0_Gravitationskonstante_En.tex",
    "T0_SI_En.tex",
    "T0_nat-si_En.tex",
    "NatEinheitenSystematikEn.tex",
    "T0_Vollstaendige_Berchnungen_En.tex",
    "T0_Anomale_Magnetische_Momente_En.tex",
    "T0_Anomale-g2-9_En.tex",
    "T0_QM-QFT-RT_En.tex",
    "T0_QAT_En.tex",
    "T0_QFT-ML_Addendum_En.tex",
    "Bell_En.tex",
    "T0_netze_En.tex",
    "T0_Kosmologie_En.tex",
    "T0_Geometrische_Kosmologie_En.tex",
    "T0_Analyse_MNRAS_Widerlegung_En.tex",
    "T0_7-fragen-3_En.tex",
    "T0_threeclock_En.tex",
    "T0_penrose_En.tex",
    "T0_g2-erweiterung-4_En.tex",
    "T0_umkehrung_En.tex",
    "T0_Theorie-vs-Synergetics_En.tex",
    "T0_QM-optimierung_En.tex",
    "QM_En.tex",
    "T0_peratt_En.tex",
    "Hannah_En.tex",
    "Markov_En.tex",
    "T0_lagrndian_En.tex",
    "LagrandianVergleichEn.tex",
    "diracVereinfachtEn.tex",
    "diracEn.tex",
    "Zwei-Dipoles-CMB_En.tex",
    "universale-ableitung_En.tex",
    "neutrino-Formel_En.tex",
    "T0_Dokumentenübersicht_En.tex",
    "TempEinheitenCMBEn.tex",
    "ParameterSystemdipendentEn.tex",
    "MathZeitMasseLagrangeEn.tex",
    "Ho_En.tex",
    "HdokumentEn.tex",
    "Zeit-konstant_En.tex",
    "Teilchenmassen_En.tex",
    "Mathematische_struktur_En.tex",
    "redshift_deflection_En.tex",
    "cosmic_En.tex",
    "gravitationskonstante_En.tex",
    "parameterherleitung_En.tex",
    "Zeit_En.tex",
    "Formeln_Energiebasiert_En.tex",
    "detailierte_formel_leptonen_anemal_En.tex",
    "FeinstrukturkonstanteEn.tex",
    "musical-spiral-137-En.tex",
    "Bewegungsenergie_En.tex",
    "T0vsESM_ConceptualAnalysis_En.tex",
    "systemEn.tex",
    "RSAtest_En.tex",
    "RSA_En.tex",
    "ResolvingTheConstantsAlfaEn.tex",
    "RelokativesZahlensystemEn.tex",
    "QM-testenEn.tex",
    "NoGoEn.tex",
    "Moll_CandelaEn.tex",
    "EliminationOfMassEn.tex",
    "E-mc2_En.tex",
    "DynMassePhotonenNichtlokalEn.tex",
    "Elimination_Of_Mass_Dirac_TabelleEn.tex",
    "Elimination_Of_Mass_Dirac_LagEn.tex",
    "QM-DetrmisticEn.tex",
    "QM-Detrmistic_p_En.tex",
    "Zusammenfassung_En.tex",
    "T0_Bibliography_En.tex",
    "T0_photonenchip-china_En.tex",
    "T0_photonenchip-umsetzung_En.tex",
    "T0_photonenchip-einführung_En.tex",
]

# Kompilierte Regex (alle als r"" für Sicherheit vor Escape-Warnings)
MACRO_RE = re.compile(r"\\([A-Za-z]+)")
BOX_BEGIN_RE = re.compile(r"^\\begin\{([a-zA-Z_]+)\}")
BOX_END_RE = re.compile(r"^\\end\{([a-zA-Z_]+)\}")
HEADING_MATH_DOLLAR = re.compile(r"\$[^$]*\$")
HEADING_BRACE = re.compile(r"({.*})")
HEADING_CMD = re.compile(r"\\[a-zA-z]+\*?(?:\[[^\]]*\])?")
HEADING_CARET = re.compile(r"\^\{[^}]*\}")
HEADING_CARET_SIMPLE = re.compile(r"\^[A-Za-z0-9]+")
TITLE_PATTERNS = [
    re.compile(r"^\\title\{(.*)\}\s*$"),
    re.compile(r"^\\chapter\*?\{([^}]*)\}"),
    re.compile(r"^\\section\*?\{([^}]*)\}")
]
CHAPTER_REPLACE = re.compile(r"^\\chapter\*?\{")
SECTION_BOLD = re.compile(r"^\\textbf\{([^}]*)\}\s*(\\\\)?\s*$")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(ref|eqref|autoref|cref|Cref)\{([^}]+)\}")
DOCUMENT_BEGIN = re.compile(r"\\begin\{document\}")
DOCUMENT_END = re.compile(r"\\end\{document\}")
BIB_BEGIN = re.compile(r"\\begin\{thebibliography\}")
BIB_END = re.compile(r"\\end\{thebibliography\}")

UNICODE_MAP = {
    "α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ", "δ": r"\delta ",
    "ε": r"\epsilon ", "ζ": r"\zeta ", "η": r"\eta ", "θ": r"\theta ",
    "ι": r"\iota ", "κ": r"\kappa ", "λ": r"\lambda ", "μ": r"\mu ",
    "ν": r"\nu ", "ξ": r"\xi ", "ο": r"o", "π": r"\pi ", "ρ": r"\rho ",
    "σ": r"\sigma ", "τ": r"\tau ", "υ": r"\upsilon ", "φ": r"\phi ",
    "χ": r"\chi ", "ψ": r"\psi ", "ω": r"\omega ",
    "Α": r"A", "Β": r"B", "Γ": r"\Gamma ", "Δ": r"\Delta ", "Ε": r"E",
    "Ζ": r"Z", "Η": r"H", "Θ": r"\Theta ", "Ι": r"I", "Κ": r"K",
    "Λ": r"\Lambda ", "Μ": r"M", "Ν": r"N", "Ξ": r"\Xi ", "Ο": r"O",
    "Π": r"\Pi ", "Ρ": r"P", "Σ": r"\Sigma ", "Τ": r"T", "Υ": r"\Upsilon ",
    "Φ": r"\Phi ", "Χ": r"X", "Ψ": r"X", "Ω": r"\Omega ",
    "∞": r"\infty ", "∂": r"\partial ", "∇": r"\nabla ", "√": r"\sqrt{}",
    "≈": r"\approx ", "≠": r"\neq ", "≤": r"\leq ", "≥": r"\geq ",
    "↔": r"\leftrightarrow ", "⇒": r"\Rightarrow ", "⇐": r"\Leftarrow ",
    "⇔": r"\Leftrightarrow ", "∈": r"\in ", "∉": r"\notin ",
    "∩": r"\cap ", "∪": r"\cup ", "∅": r"\emptyset ",
    "∑": r"\sum ", "∏": r"\prod ", "∫": r"\int ", "∝": r"\propto ",
    "★": r"\star ", "✓": r"\checkmark ", "ħ": r"\hbar ",
}

BOX_TO_SECTION = {
    "foundation": "Foundation",
    "