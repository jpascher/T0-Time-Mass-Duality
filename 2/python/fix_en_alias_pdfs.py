import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Mapping of wrong -> right PDF names (basename only)
ALIASES = {
    "DerivationVonBetaEn": "093_DerivationVonBeta_En.pdf",
    "Ho_EnergieEn": "064_Ho_En.pdf",
    "EliminationOfMassEn": "052_EliminationOfMass_En.pdf",
    "Moll_CandelaEn": "062_Moll_Candela_En.pdf",
}

# Only touch tex sources in tex-n tree
TARGET_DIRS = [
    ROOT / "2" / "tex-n" / "en_standalone",
    ROOT / "2" / "tex-n" / "en_chapters_new",
    ROOT / "2" / "tex-n" / "de_chapters_new",
]

# We only modify URLs to GitHub/jpascher or plain filenames ending with these aliases
GITHUB_PREFIX = "https://github.com/jpascher/"


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text

    # 1) Fix occurrences inside \url{...} and \href{...}{...}
    def repl_url(m: re.Match) -> str:
        full = m.group(0)
        inner = m.group(1)
        if not inner.startswith(GITHUB_PREFIX):
            return full
        for wrong, right in ALIASES.items():
            if inner.endswith(f"/{wrong}.pdf"):
                return full.replace(f"{wrong}.pdf", right)
        return full

    text = re.sub(r"\\url\{([^}]*)\}", repl_url, text)

    def repl_href(m: re.Match) -> str:
        url = m.group(1)
        label = m.group(2)
        if not url.startswith(GITHUB_PREFIX):
            return m.group(0)
        new_url = url
        for wrong, right in ALIASES.items():
            if url.endswith(f"/{wrong}.pdf"):
                new_url = url.replace(f"{wrong}.pdf", right)
                break
        return f"\\href{{{new_url}}}{{{label}}}"

    text = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}", repl_href, text)

    # 2) Fix bare filenames (not in URLs)
    for wrong, right in ALIASES.items():
        # protect URLs by only replacing standalone tokens followed by .pdf
        text = re.sub(rf"(?<![A-Za-z0-9_/]){re.escape(wrong)}\.pdf", right, text)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        print(f"Fixed aliases in {path.relative_to(ROOT)}")
        return True
    return False


def main() -> None:
    changed = 0
    for d in TARGET_DIRS:
        if not d.exists():
            continue
        for tex in sorted(d.glob("*.tex")):
            if fix_file(tex):
                changed += 1
    print(f"Alias fixes applied in {changed} files.")


if __name__ == "__main__":
    main()
