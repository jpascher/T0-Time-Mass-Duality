#!/usr/bin/env python3
"""
Script to recompile all successfully compiled documents with ebook preamble.
Temporarily modifies .tex files to use ebook preamble, compiles, then restores.
"""

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality")

# Successfully compiled German documents (001-150)
DE_DOCS = [
    "001_T0_Book_Abstract_De", "001a_T0_Book_Abstract_De", "003_T0_Grundlagen_v1_De",
    "004_T0_Modell_Uebersicht_De", "007_T0_Neutrinos_De", "008_T0_xi-und-e_De",
    "009_T0_xi_ursprung_De", "010_T0_Energie_De", "011_T0_Feinstruktur_De",
    "013_T0_SI_De", "014_T0_nat-si_De", "016_T0_Vollstaendige_Berchnungen_De",
    "018_T0_Anomale-g2-9_De", "019_T0_lagrndian_De", "022_T0-QFT-ML_Addendum_De",
    "024_T0_netze_De", "025_T0_Kosmologie_De", "028_T0_7-fragen-3_De",
    "029_T0_threeclock_De", "032_T0_umkehrung_De", "033_T0-Theory-vs-Synergetics_De",
    "035_QM_De", "038_Markov_De", "040_Hdokument_De", "041_parameterherleitung_De",
    "042_xi_parmater_partikel_De", "043_ResolvingTheConstantsAlfa_De",
    "044_Feinstrukturkonstante_De", "046_Teilchenmassen_De", "047_neutrino-Formel_De",
    "048_detailierte_formel_leptonen_anemal_De", "052_EliminationOfMass_De",
    "054_Elimination_Of_Mass_Dirac_Tabelle_De", "056_universale-ableitung_De",
    "057_RelokativesZahlensystem_De", "058_Formeln_Energiebasiert_De", "059_system_De",
    "060_musical-spiral-137-_De", "061_TempEinheitenCMB_De", "062_Moll_Candela_De",
    "063_cosmic_De", "064_Ho_De", "065_redshift_deflection_De",
    "066_ParameterSystemdipendent_De", "067_MathZeitMasseLagrange_De",
    "068_T0vsESM_ConceptualAnalysis_De", "069_Zeit-konstant_De",
    "070_Mathematische_struktur_De", "071_QM-Detrmistic_De", "072_QM-Detrmistic_p_De",
    "073_QM-testen_De", "074_NoGo_De", "075_RSA-copie_De", "076_RSAtest_De",
    "077_E-mc2_De", "078_Zeit_De", "080_Bewegungsenergie_De", "081_Zusammenfassung_De",
    "082_T0_Bibliography_De", "083_T0_photonenchip-china_De",
    "084_T0_photonenchip-umsetzung_De", "085_T0_photonenchip-einführung_De",
    "086_T0_Dokumentenübersicht_De", "087_137_De", "089_Amper_Low_De", "091_Casimir_De",
    "093_DerivationVonBeta_De", "095_Notwendigkeit_zwei_lagrange_De", "097_QFT_De",
    "098_T0_Dunkle_Materie_Energie_De", "100_T0_Book_Analyse_Pleiades_De",
    "101_T0_CMBR_Dipole_De", "103_T0_Wirkungsgrad_De", "104_T0_Higgs_De",
    "105_T0_Casimir_De", "106_T0_Spin_De", "110_T0_QCD_De", "111_T0_QED_De",
    "112_T0_EWK_De", "115_T0_CMBR_Analyse_De", "120_T0_CMB_Donoghue_Analyse_De",
    "130_T0_Vakuumpolarisation_De", "140_T0_CMB_Donoghue_Analyse_De",
    "150_Rotverschiebung_De"
]


def compile_document(tex_file: Path, lang: str) -> bool:
    """Compile a single document with ebook preamble"""
    if not tex_file.exists():
        print(f"  [SKIP] Not found: {tex_file.name}")
        return False
    
    # Read original content
    try:
        original_content = tex_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  [FAIL] Cannot read {tex_file.name}: {e}")
        return False
    
    # Replace preamble references
    if lang == "de":
        modified_content = original_content.replace(
            "T0_preamble_shared_De.tex",
            "T0_preamble_shared-ebook_De.tex"
        )
    else:
        modified_content = original_content.replace(
            "T0_preamble_shared_En.tex",
            "T0_preamble_shared-ebook_En.tex"
        )
    
    # Write modified content temporarily
    try:
        tex_file.write_text(modified_content, encoding='utf-8')
    except Exception as e:
        print(f"  [FAIL] Cannot write {tex_file.name}: {e}")
        return False
    
    # Compile with LuaLaTeX
    try:
        result = subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "-file-line-error", tex_file.name],
            cwd=tex_file.parent,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=120
        )
        success = result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"  [FAIL] Timeout for {tex_file.name}")
        success = False
    except Exception as e:
        print(f"  [FAIL] Compilation error for {tex_file.name}: {e}")
        success = False
    finally:
        # Restore original content
        try:
            tex_file.write_text(original_content, encoding='utf-8')
        except Exception as e:
            print(f"  [WARN] Cannot restore {tex_file.name}: {e}")
    
    # Clean up auxiliary files
    base_name = tex_file.stem
    for ext in ['.aux', '.log', '.out', '.toc', '.synctex.gz', '.fls', '.fdb_latexmk']:
        aux_file = tex_file.parent / f"{base_name}{ext}"
        if aux_file.exists():
            aux_file.unlink()
    
    if success:
        pdf_file = tex_file.parent / f"{base_name}.pdf"
        if pdf_file.exists():
            print(f"  [OK] {tex_file.name} → {pdf_file.name}")
            return True
        else:
            print(f"  [FAIL] No PDF generated for {tex_file.name}")
            return False
    else:
        print(f"  [FAIL] Compilation failed for {tex_file.name}")
        return False


def main():
    print("=" * 60)
    print("Compiling documents with ebook preamble")
    print("=" * 60)
    
    de_dir = REPO_ROOT / "2/tex-n/de_standalone"
    en_dir = REPO_ROOT / "2/tex-n/en_standalone"
    
    # Compile German documents
    print("\nGerman documents:")
    print("-" * 60)
    de_success = 0
    de_fail = 0
    
    for doc_name in DE_DOCS:
        tex_file = de_dir / f"{doc_name}.tex"
        if compile_document(tex_file, "de"):
            de_success += 1
        else:
            de_fail += 1
    
    print(f"\nGerman: {de_success} successful, {de_fail} failed")
    
    # Compile English documents (001-150, excluding problematic ones)
    print("\nEnglish documents:")
    print("-" * 60)
    en_success = 0
    en_fail = 0
    
    for i in range(1, 151):
        num_str = f"{i:03d}"
        
        # Skip problematic documents
        if num_str in ["065", "075"]:
            continue
        
        # Find all files matching pattern
        for tex_file in en_dir.glob(f"{num_str}_*.tex"):
            if compile_document(tex_file, "en"):
                en_success += 1
            else:
                en_fail += 1
    
    print(f"\nEnglish: {en_success} successful, {en_fail} failed")
    
    print("\n" + "=" * 60)
    print(f"TOTAL: {de_success + en_success} successful, {de_fail + en_fail} failed")
    print("=" * 60)
    
    return 0 if (de_fail + en_fail) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
