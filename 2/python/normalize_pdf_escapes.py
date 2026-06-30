import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DE_DIR = ROOT / "2" / "tex-n" / "de_standalone"
EN_DIR = ROOT / "2" / "tex-n" / "en_standalone"

TOKEN_PATTERN = re.compile(r"([0-9A-Za-z\\_]+\.(?:pdf|tex))")


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    def repl(match: re.Match) -> str:
        token = match.group(1)
        fixed = token.replace(r"\\_", r"\_")  # collapse any \\_ to \_
        return fixed

    new_text = TOKEN_PATTERN.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(f"Fixed escapes in {path.relative_to(ROOT)}")
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
    print(f"Normalized escapes in {changed} files.")


if __name__ == "__main__":
    main()
