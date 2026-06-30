#!/usr/bin/env python3
import re
from pathlib import Path

RE_PDF_ESC = re.compile(r'([0-9A-Za-z\\]+(?:\\_[0-9A-Za-z\\]+)*\.pdf)')

# Manual aliases for known historic names that don't match the canonical basename
MANUAL_ALIASES = {
    "xi_parameter_partikel_De.pdf": "042_xi_parmater_partikel_De.pdf",
    "xi_parameter_partikel_En.pdf": "042_xi_parmater_partikel_En.pdf",
}


def collect_standalone_docs(tex_root: Path):
    docs = {}
    for sub in ("de_standalone", "en_standalone"):
        d = tex_root / sub
        if not d.is_dir():
            continue
        for f in d.glob("*.tex"):
            name = f.stem  # without extension
            m = re.match(r"^([0-9]+)_([A-Za-z0-9_-]+)_(De|En)$", name)
            if not m:
                continue
            num, base, lang = m.groups()
            canon = f"{num}_{base}_{lang}.pdf"
            key1 = base + lang
            key2 = f"{base}_{lang}"
            key3 = canon[:-4]
            for k in {key1, key2, key3}:
                docs[k] = canon
    return docs


def scan_pdfs(tex_root: Path):
    usages = {}
    for f in tex_root.rglob("*.tex"):
        rel = f.relative_to(tex_root).as_posix()
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for ln, line in enumerate(lines, 1):
            stripped = line.lstrip()
            if stripped.startswith("%"):
                continue
            for m in RE_PDF_ESC.finditer(line):
                esc_name = m.group(1)
                pdf = esc_name.replace("\\_", "_")
                usages.setdefault(pdf, []).append((rel, ln))
    return usages


def classify_pdfs(usages, docs_map):
    prefixed = {}
    unprefixed = {}
    for pdf, where in usages.items():
        if re.match(r"^[0-9]+_", pdf):
            prefixed[pdf] = {"where": where, "mapped": pdf in docs_map.values()}
        else:
            # try to infer mapping for unprefixed/internal-style names
            base = pdf[:-4]
            target = MANUAL_ALIASES.get(pdf)

            # Handle patterns like Base_De.pdf, BaseDe.pdf, with optional underscore and hyphens
            if target is None:
                m = re.match(r"^([A-Za-z0-9_-]+?)(?:_)?([dDeEnN]{2})$", base)
                if m:
                    b_raw, lang = m.groups()
                    langN = "De" if lang.lower() == "de" else "En"
                    for b in {b_raw, b_raw.replace("-", "_")}:
                        for k in (b + langN, f"{b}_{langN}"):
                            if k in docs_map:
                                target = docs_map[k]
                                break
                        if target is not None:
                            break

            # Fallback: any Base(De|En) pattern, again with optional underscore
            if target is None:
                m2 = re.match(r"^(.+?)(?:_)?(De|En)$", base)
                if m2:
                    b_raw, lang = m2.groups()
                    for b in {b_raw, b_raw.replace("-", "_")}:
                        for k in (b + lang, f"{b}_{lang}"):
                            if k in docs_map:
                                target = docs_map[k]
                                break
                        if target is not None:
                            break

            unprefixed[pdf] = {"where": where, "target": target}
    return prefixed, unprefixed


def apply_replacements(tex_root: Path, unprefixed):
    # build mapping old_escaped -> new_escaped for all resolvable entries
    repl = {}
    for pdf, info in unprefixed.items():
        target = info["target"]
        if not target or target == pdf:
            continue
        old_esc = pdf.replace("_", "\\_")
        new_esc = target.replace("_", "\\_")
        repl[old_esc] = new_esc

    if not repl:
        return []

    changed_files = []
    for f in tex_root.rglob("*.tex"):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        orig = content
        for old_e, new_e in repl.items():
            content = content.replace(old_e, new_e)
        if content != orig:
            f.write_text(content, encoding="utf-8")
            changed_files.append(f.relative_to(tex_root).as_posix())
    return changed_files


def main():
    repo_root = Path(".").resolve()
    tex_root = repo_root / "2" / "tex-n"
    docs_map = collect_standalone_docs(tex_root)
    usages = scan_pdfs(tex_root)
    prefixed, unprefixed = classify_pdfs(usages, docs_map)

    changed = apply_replacements(tex_root, unprefixed)

    print("# Unprefixed PDF references (after auto-mapping)\n")
    print("| PDF | Uses | Mapped To | Example |")
    print("| --- | ---- | --------- | ------- |")
    for pdf in sorted(unprefixed.keys()):
        info = unprefixed[pdf]
        where = info["where"]
        target = info["target"] or "(no match)"
        example = f"{where[0][0]}:{where[0][1]}" if where else ""
        print(f"| {pdf} | {len(where)} | {target} | {example} |")

    print("\n# Prefixed PDF references summary\n")
    print("| PDF | Uses | In standalone list? | Example |")
    print("| --- | ---- | ------------------- | ------- |")
    for pdf in sorted(prefixed.keys()):
        info = prefixed[pdf]
        where = info["where"]
        ok = "yes" if info["mapped"] else "no"
        example = f"{where[0][0]}:{where[0][1]}" if where else ""
        print(f"| {pdf} | {len(where)} | {ok} | {example} |")

    if changed:
        print("\n# Files changed by auto-mapping")
        for p in sorted(set(changed)):
            print(p)


if __name__ == "__main__":
    main()
