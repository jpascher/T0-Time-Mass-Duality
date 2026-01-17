#!/bin/bash

# Script to recompile all successfully compiled documents with ebook preamble
# Changes T0_preamble_shared to T0_preamble_shared-ebook

set -e

REPO_ROOT="/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
cd "$REPO_ROOT"

# List of successfully compiled German documents (001-150)
DE_DOCS=(
    "001_T0_Book_Abstract_De"
    "001a_T0_Book_Abstract_De"
    "003_T0_Grundlagen_v1_De"
    "004_T0_Modell_Uebersicht_De"
    "007_T0_Neutrinos_De"
    "008_T0_xi-und-e_De"
    "009_T0_xi_ursprung_De"
    "010_T0_Energie_De"
    "011_T0_Feinstruktur_De"
    "013_T0_SI_De"
    "014_T0_nat-si_De"
    "016_T0_Vollstaendige_Berchnungen_De"
    "018_T0_Anomale-g2-9_De"
    "019_T0_lagrndian_De"
    "022_T0-QFT-ML_Addendum_De"
    "024_T0_netze_De"
    "025_T0_Kosmologie_De"
    "028_T0_7-fragen-3_De"
    "029_T0_threeclock_De"
    "032_T0_umkehrung_De"
    "033_T0-Theory-vs-Synergetics_De"
    "035_QM_De"
    "038_Markov_De"
    "040_Hdokument_De"
    "041_parameterherleitung_De"
    "042_xi_parmater_partikel_De"
    "043_ResolvingTheConstantsAlfa_De"
    "044_Feinstrukturkonstante_De"
    "046_Teilchenmassen_De"
    "047_neutrino-Formel_De"
    "048_detailierte_formel_leptonen_anemal_De"
    "052_EliminationOfMass_De"
    "054_Elimination_Of_Mass_Dirac_Tabelle_De"
    "056_universale-ableitung_De"
    "057_RelokativesZahlensystem_De"
    "058_Formeln_Energiebasiert_De"
    "059_system_De"
    "060_musical-spiral-137-_De"
    "061_TempEinheitenCMB_De"
    "062_Moll_Candela_De"
    "063_cosmic_De"
    "064_Ho_De"
    "065_redshift_deflection_De"
    "066_ParameterSystemdipendent_De"
    "067_MathZeitMasseLagrange_De"
    "068_T0vsESM_ConceptualAnalysis_De"
    "069_Zeit-konstant_De"
    "070_Mathematische_struktur_De"
    "071_QM-Detrmistic_De"
    "072_QM-Detrmistic_p_De"
    "073_QM-testen_De"
    "074_NoGo_De"
    "075_RSA-copie_De"
    "076_RSAtest_De"
    "077_E-mc2_De"
    "078_Zeit_De"
    "080_Bewegungsenergie_De"
    "081_Zusammenfassung_De"
    "082_T0_Bibliography_De"
    "083_T0_photonenchip-china_De"
    "084_T0_photonenchip-umsetzung_De"
    "085_T0_photonenchip-einführung_De"
    "086_T0_Dokumentenübersicht_De"
    "087_137_De"
    "089_Amper_Low_De"
    "091_Casimir_De"
    "093_DerivationVonBeta_De"
    "095_Notwendigkeit_zwei_lagrange_De"
    "097_QFT_De"
    "098_T0_Dunkle_Materie_Energie_De"
    "100_T0_Book_Analyse_Pleiades_De"
    "101_T0_CMBR_Dipole_De"
    "103_T0_Wirkungsgrad_De"
    "104_T0_Higgs_De"
    "105_T0_Casimir_De"
    "106_T0_Spin_De"
    "110_T0_QCD_De"
    "111_T0_QED_De"
    "112_T0_EWK_De"
    "115_T0_CMBR_Analyse_De"
    "120_T0_CMB_Donoghue_Analyse_De"
    "130_T0_Vakuumpolarisation_De"
    "140_T0_CMB_Donoghue_Analyse_De"
    "150_Rotverschiebung_De"
)

# Function to compile a document
compile_doc() {
    local doc_name="$1"
    local lang_dir="$2"
    local tex_file="$REPO_ROOT/2/tex-n/${lang_dir}/${doc_name}.tex"
    
    if [ ! -f "$tex_file" ]; then
        echo "  [SKIP] File not found: $tex_file"
        return 1
    fi
    
    # Create temporary file with ebook preamble
    local temp_file=$(mktemp)
    sed 's/T0_preamble_shared_De\.tex/T0_preamble_shared-ebook_De.tex/g; s/T0_preamble_shared_En\.tex/T0_preamble_shared-ebook_En.tex/g' "$tex_file" > "$temp_file"
    
    # Compile with LuaLaTeX
    cd "$REPO_ROOT/2/tex-n/${lang_dir}"
    lualatex -interaction=nonstopmode -file-line-error "$temp_file" > /dev/null 2>&1
    local result=$?
    
    # Move PDF to correct name if successful
    if [ $result -eq 0 ]; then
        local temp_base=$(basename "$temp_file" .tex)
        if [ -f "${temp_base}.pdf" ]; then
            mv "${temp_base}.pdf" "${doc_name}.pdf"
            echo "  [OK] $doc_name.pdf"
        else
            echo "  [FAIL] No PDF generated for $doc_name"
            result=1
        fi
    else
        echo "  [FAIL] Compilation error for $doc_name"
    fi
    
    # Clean up
    rm -f "$temp_file"
    rm -f "${temp_base}".{aux,log,out,toc,synctex.gz}
    
    cd "$REPO_ROOT"
    return $result
}

echo "========================================="
echo "Compiling German documents with ebook preamble"
echo "========================================="

de_success=0
de_fail=0

for doc in "${DE_DOCS[@]}"; do
    if compile_doc "$doc" "de_standalone"; then
        ((de_success++))
    else
        ((de_fail++))
    fi
done

echo ""
echo "German documents: $de_success successful, $de_fail failed"
echo ""

# Now compile English documents
echo "========================================="
echo "Compiling English documents with ebook preamble"
echo "========================================="

# Find all successfully compiled English documents
cd "$REPO_ROOT/2/tex-n/en_standalone"
en_success=0
en_fail=0

# Compile range 001-150 (excluding known problematic ones)
for num in $(seq -w 1 150); do
    # Skip problematic documents
    if [ "$num" = "065" ] || [ "$num" = "075" ]; then
        continue
    fi
    
    # Find files matching pattern
    for tex_file in ${num}_*.tex; do
        if [ -f "$tex_file" ]; then
            doc_name=$(basename "$tex_file" .tex)
            if compile_doc "$doc_name" "en_standalone"; then
                ((en_success++))
            else
                ((en_fail++))
            fi
        fi
    done
done

echo ""
echo "English documents: $en_success successful, $en_fail failed"
echo ""
echo "========================================="
echo "TOTAL: $((de_success + en_success)) successful, $((de_fail + en_fail)) failed"
echo "========================================="
