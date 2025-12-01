#!/usr/bin/env bash
set -euo pipefail

REPO_OWNER="jpascher"
REPO_NAME="T0-Time-Mass-Duality"
DEFAULT_REF="ce78d7b93bd940a3b3f12a2c3afd0d1c34d35a41"

# Parse optional --ref parameter and --apply flag
REF="${DEFAULT_REF}"
DRY_RUN=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --ref=*)
      REF="${1#--ref=}"
      shift
      ;;
    --ref)
      if [[ $# -ge 2 && ! "$2" =~ ^-- ]]; then
        REF="$2"
        shift 2
      else
        echo "Error: --ref requires a value"
        exit 1
      fi
      ;;
    --apply)
      DRY_RUN=0
      shift
      ;;
    *)
      echo "Unknown option: $1"
      shift
      ;;
  esac
done

TEX_FILES=(
  "2/tex/T0_7-fragen-3_De.tex"
  "2/tex/T0_7-fragen-3_En.tex"
  "2/tex/T0_Grundlagen_De.tex"
  "2/tex/T0_Grundlagen_en.tex"
  "2/tex/T0_Introduction_En.tex"
  "2/tex/T0_Modell_Uebersicht_De.tex"
  "2/tex/T0_Modell_Uebersicht_En.tex"
  "2/tex/chapters_en/T0_7-fragen-3_En_ch.tex"
  "2/tex/chapters_en/T0_Grundlagen_En_ch.tex"
  "2/tex/chapters_en/T0_Introduction_En_ch.tex"
  "2/tex/chapters_en/T0_Modell_Uebersicht_En_ch.tex"
)

OUT_BASE="book1/Book1_T0_erklaert_de"
CHAPTERS_DIR="${OUT_BASE}/chapters"
ORIGINALS_DIR="${OUT_BASE}/originals"
MAPPINGS_DIR="${OUT_BASE}/mappings"

mkdir -p "${CHAPTERS_DIR}" "${ORIGINALS_DIR}" "${MAPPINGS_DIR}"

echo "REF = ${REF}"
echo "Dry run mode: ${DRY_RUN}"

for tex in "${TEX_FILES[@]}"; do
  # Use the explicit path directly
  PATH_FOUND="${tex}"
  
  # Check if file exists in git at the specified ref
  if ! git cat-file -e "${REF}:${PATH_FOUND}" 2>/dev/null; then
    echo "WARN: Could not find ${tex} at ref ${REF}. Skipping."
    continue
  fi

  base=$(basename "${tex}" .tex)
  md_out="${CHAPTERS_DIR}/01_${base}.md"
  orig_out="${ORIGINALS_DIR}/${base}.tex.raw"
  map_out="${MAPPINGS_DIR}/mapping_${base}.yaml"
  blob_url="https://github.com/${REPO_OWNER}/${REPO_NAME}/blob/${REF}/${PATH_FOUND}"

  echo ""
  echo "Found: ${PATH_FOUND}"
  echo " -> Markdown: ${md_out}"
  echo " -> Original snapshot: ${orig_out}"
  echo " -> Mapping: ${map_out}"
  echo " -> Blob URL: ${blob_url}"

  echo "---- snippet of original (first 40 lines) ----"
  git show "${REF}:${PATH_FOUND}" 2>/dev/null | sed -n '1,40p' | sed 's/^/| /'
  echo "---- end snippet ----"

  if [ "${DRY_RUN}" -eq 0 ]; then
    cat > "${md_out}" <<MD
---
source_tex: ${blob_url}
original_ref: ${REF}
original_path: ${PATH_FOUND}
mapping: ${map_out}
---

# DRAFT: $(echo "${base}" | sed 's/_/ /g')

(Platzhalter. Die Überarbeitung wird strikt auf Basis der Original‑LaTeX erfolgen.
Die Original‑LaTeX‑Datei wird als Appendix angehängt, jede inhaltliche Vereinfachung
als Kommentar markiert. Siehe mapping: ${map_out})
MD

    git show "${REF}:${PATH_FOUND}" > "${orig_out}"

    cat > "${map_out}" <<YAML
rewritten_file: ${md_out}
original_file: ${PATH_FOUND}
repo_blob_url: ${blob_url}
original_ref: ${REF}
mappings: []
appendix:
  original_snapshot_file: ${orig_out}
YAML

    echo "WROTE ${md_out}, ${orig_out}, ${map_out}"
  else
    echo "(dry-run) not writing files. Re-run with --apply to create files."
  fi
done

echo ""
echo "Done. If you want files written, re-run with:"
echo "  ./tools/generate_mapping_from_tex.sh --apply"
echo "  ./tools/generate_mapping_from_tex.sh --ref <sha> --apply"
