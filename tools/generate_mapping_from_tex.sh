#!/usr/bin/env bash
set -euo pipefail
REPO_OWNER="jpascher"
REPO_NAME="T0-Time-Mass-Duality"
REF="ce78d7b93bd940a3b3f12a2c3afd0d1c34d35a41"
TEX_FILES=(
  "T0_abstract_De.tex"
  "T0_Introduction_De.tex"
  "reise_De.tex"
  "T0_Grundlagen_De.tex"
  "T0_Modell_Uebersicht_De.tex"
  "T0_7-fragen-3_De.tex"
)
OUT_BASE="book1/Book1_T0_erklaert_de"
CHAPTERS_DIR="${OUT_BASE}/chapters"
ORIGINALS_DIR="${OUT_BASE}/originals"
MAPPINGS_DIR="${OUT_BASE}/mappings"
DRY_RUN=1
if [ "${1-}" = "--apply" ]; then
  DRY_RUN=0
fi
mkdir -p "${CHAPTERS_DIR}" "${ORIGINALS_DIR}" "${MAPPINGS_DIR}"
echo "REF = ${REF}"
echo "Dry run mode: ${DRY_RUN}"
for tex in "${TEX_FILES[@]}"; do
  PATH_FOUND=$(git ls-files | grep -F "/${tex}$" || true)
  if [ -z "$PATH_FOUND" ]; then
    PATH_FOUND=$(git ls-files | grep -F "${tex}$" || true)
  fi
  if [ -z "$PATH_FOUND" ]; then
    echo "WARN: Could not find ${tex} in the git index. Skipping."
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
  cat > /tmp/preview.txt <<EOF
# DRAFT: ${base}
<!--
SOURCE:
Original LaTeX: ${PATH_FOUND}
Repository blob URL (ref ${REF}):
${blob_url}
-->
<!--
NOTE: The main text below is a placeholder draft. When rewriting, I will:
- Keep all factual statements from the original .tex unchanged.
- Add an 'Appendix: Original LaTeX' containing the full .tex snapshot.
- Create a mapping YAML listing original line ranges -> rewritten sections.
-->
EOF
  cat > /tmp/map_preview.yaml <<EOF
rewritten_file: ${md_out}
original_file: ${PATH_FOUND}
repo_blob_url: ${blob_url}
original_ref: ${REF}
mappings: []
appendix:
  original_snapshot_file: ${orig_out}
EOF
  echo "---- snippet of original (first 40 lines) ----"
  git show "${REF}:${PATH_FOUND}" | sed -n '1,40p' | sed 's/^/| /'
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
