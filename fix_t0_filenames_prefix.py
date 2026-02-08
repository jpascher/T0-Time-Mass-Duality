import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DE_DIR = ROOT / "2" / "tex-n" / "de_standalone"
EN_DIR = ROOT / "2" / "tex-n" / "en_standalone"

PREAMBLE_PATTERN = re.compile(r"(Standardized preamble\s*-\s*)(T0_[^\s.]+\.pdf)")
DATEINAME_PATTERN = re.compile(r"(Dateiname:\s*)(T0_[^\s.]+\.pdf)")
FILENAME_PATTERN = re.compile(r"(Filename:\s*)(T0_[^\s.]+\.pdf)")


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    base = path.stem
    canonical_pdf = f"{base}.pdf"

    new_text = PREAMBLE_PATTERN.sub(rf"\\1{canonical_pdf}", text)
    new_text = DATEINAME_PATTERN.sub(rf"\\1{canonical_pdf}", new_text)
    new_text = FILENAME_PATTERN.sub(rf"\\1{canonical_pdf}", new_text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(f"Fixed T0 filename comments in {path.relative_to(ROOT)}")
        return True
    return False


def main() -> None:
    changed = 0
    for d in (DE_DIR, EN_DIR):
        if not d.exists():
            continue
        for tex in sorted(d.glob("*.tex")):
            if fix_file(tex):
                changed += 1
    print(f"Updated T0 filename comments in {changed} files.")


if __name__ == "__main__":
    main()
