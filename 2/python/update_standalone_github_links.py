import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

DE_STANDALONE_DIR = ROOT / "2" / "tex-n" / "de_standalone"
EN_STANDALONE_DIR = ROOT / "2" / "tex-n" / "en_standalone"
REF_LIST_PATH = ROOT / "2" / "tex-n" / "de_standalone_reference_list.txt"

GITHUB_PREFIX = "https://github.com/jpascher/"


def load_reference_mapping():
    """Load DE standalone reference list and build mapping from basename variants -> canonical PDF name.

    - Input file contains lines like '003_T0_Grundlagen_v1_De.tex'.
    - Canonical PDF name is with .pdf extension.
    - We create keys:
      * full basename without extension (lowercase)
      * basename without leading numeric prefix (\d+_)
    - Extension of the href (tex/pdf) is ignored on lookup; we always map to .pdf.
    - Special case: Grundlagen-Dokument – 'grundlagen' ohne v1 wird ebenfalls auf 003_T0_Grundlagen_v1_De.pdf gemappt.
    """
    mapping = {}
    if not REF_LIST_PATH.exists():
        print(f"Reference list not found: {REF_LIST_PATH}")
        return mapping

    with REF_LIST_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if not name or name.startswith("#"):
                continue
            if not name.lower().endswith(".tex"):
                continue
            base = name[:-4]  # drop .tex
            canonical_pdf = base + ".pdf"

            key_full = base.lower()
            mapping[key_full] = canonical_pdf

            # strip leading numeric prefix NNN_ if present
            m = re.match(r"^(\d+_)(.+)$", base)
            if m:
                without_prefix = m.group(2).lower()
                mapping[without_prefix] = canonical_pdf

            # Spezialfall Grundlagen: auch Varianten ohne _v1 oder ohne De auf dieses Dokument mappen
            base_l = base.lower()
            if "grundlagen" in base_l:
                # ein paar heuristische Aliase rund um den Namen ohne führende Nummer
                without_num = re.sub(r"^\d+_", "", base_l)
                variants = set()
                variants.add(without_num)
                variants.add(without_num.replace("_v1", ""))
                for v in list(variants):
                    if v.endswith("_de"):
                        variants.add(v[:-3])
                for v in variants:
                    mapping.setdefault(v, canonical_pdf)

    return mapping


HREF_PATTERN = re.compile(r"\\href\{([^}]*)\}\{([^}]*)\}")
URL_PATTERN = re.compile(r"\\url\{([^}]*)\}")
# Dateinamen im Text (LaTeX-Kontext), inkl. ggf. mit "\\_" als Unterstrich
FILE_PATTERN = re.compile(r"([0-9A-Za-z\\_\-]+)\.(?:tex|pdf)")


def _lookup_canonical(base_no_ext: str, ref_map: dict) -> str | None:
    """Finde den kanonischen PDF-Namen für einen Basisnamen (ohne Extension).

    - Ignoriert Groß-/Kleinschreibung.
    - Probiert auch Varianten ohne numerischen Präfix.
    """
    key = base_no_ext.lower()
    if key in ref_map:
        return ref_map[key]

    m = re.match(r"^(\d+_)(.+)$", base_no_ext)
    if m:
        k2 = m.group(2).lower()
        return ref_map.get(k2)

    return None


def process_tex_file(path: Path, ref_map: dict):
    text = path.read_text(encoding="utf-8")

    def replace_href(match: re.Match) -> str:
        url = match.group(1)
        label = match.group(2)

        # Nur Links auf GitHub des Users bearbeiten
        if not url.startswith(GITHUB_PREFIX):
            return match.group(0)

        # Dateinamen aus der URL extrahieren (letztes Segment)
        tail = url.split("/")[-1]
        tail = tail.split("?")[0].split("#")[0]

        if not tail:
            # Kein sinnvoller Dateiname -> Link entfernen, Text behalten
            return label

        # Basisname ohne Extension
        if "." in tail:
            base_no_ext = ".".join(tail.split(".")[:-1])
        else:
            base_no_ext = tail

        canonical_pdf = _lookup_canonical(base_no_ext, ref_map)

        if canonical_pdf is None:
            # Kein Match in Referenzliste -> Link entfernen, Text behalten
            return label

        # Pfad beibehalten, nur Dateinamen ersetzen
        parts = url.split("/")
        parts[-1] = canonical_pdf
        new_url = "/".join(parts)
        return f"\\href{{{new_url}}}{{{label}}}"

    # Zuerst nur GitHub-Links anpassen
    new_text = HREF_PATTERN.sub(replace_href, text)

    def replace_url(match: re.Match) -> str:
        url = match.group(1)
        # Nur Links auf GitHub des Users bearbeiten
        if not url.startswith(GITHUB_PREFIX):
            return match.group(0)

        tail = url.split("/")[-1]
        tail = tail.split("?")[0].split("#")[0]
        if not tail:
            return match.group(0)

        if "." in tail:
            base_no_ext = ".".join(tail.split(".")[:-1])
        else:
            base_no_ext = tail

        canonical_pdf = _lookup_canonical(base_no_ext, ref_map)
        if canonical_pdf is None:
            # Kein Mapping -> GitHub-URL entfernen
            return ""

        parts = url.split("/")
        parts[-1] = canonical_pdf
        new_url = "/".join(parts)
        return f"\\url{{{new_url}}}"

    text_after_links = URL_PATTERN.sub(replace_url, new_text)

    # Dann direkte Dateinamen im restlichen Text ersetzen (außer in URLs)
    def replace_filename(match: re.Match) -> str:
        start = match.start()
        # Kontext vor dem Match (für URL-Erkennung)
        prefix = text_after_links[max(0, start - 16):start]
        if "http://" in prefix or "https://" in prefix or "://" in prefix:
            # Teil einer URL -> nicht anfassen
            return match.group(0)

        raw_base = match.group(1)
        # LaTeX-"\\_" wieder in "_" zurückwandeln für das Mapping
        decoded_base = raw_base.replace(r"\\_", "_")

        canonical_pdf = _lookup_canonical(decoded_base, ref_map)
        if canonical_pdf is None:
            return match.group(0)

        # Im Text wollen wir einen reinen Dateinamen (ohne Pfad) mit LaTeX-escaped Unterstrichen
        escaped_pdf = canonical_pdf.replace("_", r"\\_")
        return escaped_pdf

    newer_text = FILE_PATTERN.sub(replace_filename, text_after_links)

    if newer_text != text:
        path.write_text(newer_text, encoding="utf-8")
        print(f"Updated hrefs/filenames in {path.relative_to(ROOT)}")
    else:
        print(f"No GitHub href or filename changes in {path.relative_to(ROOT)}")


def main():
    ref_map = load_reference_mapping()
    if not ref_map:
        print("No reference mapping loaded; aborting.")
        return

    for dir_path in (DE_STANDALONE_DIR, EN_STANDALONE_DIR):
        if not dir_path.exists():
            print(f"Skip missing directory: {dir_path}")
            continue
        for tex_path in sorted(dir_path.glob("*.tex")):
            process_tex_file(tex_path, ref_map)


if __name__ == "__main__":
    main()
