#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ffgft_tts.py  —  Batch-Vertonung der FFGFT-Slide-Chunks mit Chatterbox.

Liest FFGFT_Chatterbox_Chunks.txt (60 Slides, 181 Haeppchen), erzeugt pro
Haeppchen ein nummeriertes WAV und kann sie optional pro Slide und/oder zu
einem durchgehenden Avatar-Ton zusammenhaengen.

Setup (einmalig):
    python -m venv .venv && source .venv/bin/activate      # optional
    pip install chatterbox-tts torchaudio

Lauf (alles in einem Durchlauf):
    python ffgft_tts.py --merge-slides --merge-full

Mit fester Sprecherstimme (empfohlen fuer gleichbleibenden Klang ueber alle 181):
    python ffgft_tts.py --voice meine_stimme.wav --merge-slides --merge-full

Nur planen, nichts rendern (prueft das Parsen ohne Modell zu laden):
    python ffgft_tts.py --dry-run
"""

import argparse
import re
import sys
import time
from pathlib import Path

SLIDE_RE = re.compile(r"SLIDE\s+(\d+)")
MARK_RE = re.compile(r"^\[(\d+)\.(\d+)\]")


# ---------------------------------------------------------------- parsing -----
def parse_chunks(path: Path):
    """Liefert eine Liste von dicts: {idx, slide, sub, text}."""
    chunks, cur = [], None
    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            # Slide-Kopfzeile: nur Kontext, kein Text
            if "====" in line and SLIDE_RE.search(line):
                if cur is not None and cur["text"]:
                    chunks.append(cur)
                    cur = None
                continue
            m = MARK_RE.match(line)
            if m:
                if cur is not None and cur["text"]:
                    chunks.append(cur)
                cur = {"slide": int(m.group(1)), "sub": int(m.group(2)), "text": ""}
                continue
            if cur is not None:
                if line.strip() == "":
                    if cur["text"]:
                        chunks.append(cur)
                        cur = None
                else:
                    cur["text"] = (cur["text"] + " " + line.strip()).strip()
    if cur is not None and cur["text"]:
        chunks.append(cur)

    for i, c in enumerate(chunks, start=1):
        c["idx"] = i
    return chunks


def chunk_filename(c):
    return f"{c['idx']:03d}_s{c['slide']:02d}.{c['sub']}.wav"


# ---------------------------------------------------------------- audio io ----
def load_model(device, turbo=False):
    import torch  # noqa
    if turbo:
        from chatterbox.tts_turbo import ChatterboxTurboTTS as Model
    else:
        from chatterbox.tts import ChatterboxTTS as Model
    print(f"[lade Modell auf {device} ...]")
    return Model.from_pretrained(device=device)


def pick_device(requested):
    if requested != "auto":
        return requested
    import torch
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def concat_wavs(paths, gap_s, sr):
    """Haengt mehrere WAVs mit Stille dazwischen aneinander (torch-Tensor)."""
    import torch
    import torchaudio as ta
    gap = torch.zeros(1, int(gap_s * sr))
    pieces = []
    for j, p in enumerate(paths):
        wav, file_sr = ta.load(str(p))
        if file_sr != sr:  # Sicherheitsnetz, sollte nie noetig sein
            wav = ta.functional.resample(wav, file_sr, sr)
        if j > 0:
            pieces.append(gap)
        pieces.append(wav)
    return torch.cat(pieces, dim=1)


# ---------------------------------------------------------------- main --------
def main():
    ap = argparse.ArgumentParser(description="FFGFT-Chunks -> WAV (Chatterbox)")
    ap.add_argument("--infile", default="FFGFT_Chatterbox_Chunks.txt", type=Path)
    ap.add_argument("--outdir", default="ffgft_audio", type=Path)
    ap.add_argument("--device", default="auto",
                    choices=["auto", "cuda", "mps", "cpu"])
    ap.add_argument("--turbo", action="store_true",
                    help="Chatterbox Turbo (braucht --voice Referenzclip).")
    ap.add_argument("--voice", default=None, type=Path,
                    help="Referenz-WAV (5-20 s) fuer gleichbleibende Stimme.")
    ap.add_argument("--exaggeration", default=0.5, type=float)
    ap.add_argument("--cfg-weight", default=0.5, type=float)
    ap.add_argument("--seed", default=None, type=int,
                    help="Fester Seed = reproduzierbarer Ton.")
    ap.add_argument("--gap", default=0.35, type=float,
                    help="Stille zwischen Haeppchen innerhalb eines Slides (s).")
    ap.add_argument("--slide-gap", default=0.9, type=float,
                    help="Stille zwischen Slides im Voll-Merge (s).")
    ap.add_argument("--merge-slides", action="store_true",
                    help="Pro Slide ein zusammengehaengtes WAV.")
    ap.add_argument("--merge-full", action="store_true",
                    help="Ein durchgehendes WAV ueber alle Slides.")
    ap.add_argument("--overwrite", action="store_true",
                    help="Vorhandene Chunk-WAVs neu rendern (sonst: ueberspringen = Resume).")
    ap.add_argument("--dry-run", action="store_true",
                    help="Nur parsen und Plan zeigen, kein Modell, kein Rendern.")
    args = ap.parse_args()

    if not args.infile.exists():
        sys.exit(f"Datei nicht gefunden: {args.infile}")

    chunks = parse_chunks(args.infile)
    slides = sorted({c["slide"] for c in chunks})
    longest = max(len(c["text"]) for c in chunks)
    print(f"{len(chunks)} Haeppchen, {len(slides)} Slides, "
          f"laengstes {longest} Zeichen.")

    if args.dry_run:
        for c in chunks[:3] + chunks[-3:]:
            print(f"  {chunk_filename(c)}  [{len(c['text'])}]  "
                  f"{c['text'][:60]}...")
        print("(--dry-run: nichts gerendert)")
        return

    chunk_dir = args.outdir / "chunks"
    chunk_dir.mkdir(parents=True, exist_ok=True)

    import torch
    import torchaudio as ta

    device = pick_device(args.device)
    if args.turbo and not args.voice:
        sys.exit("Turbo braucht --voice (Referenzclip).")
    model = load_model(device, turbo=args.turbo)
    sr = model.sr

    gen_kwargs = dict(exaggeration=args.exaggeration, cfg_weight=args.cfg_weight)
    if args.voice:
        gen_kwargs["audio_prompt_path"] = str(args.voice)

    t0 = time.time()
    for c in chunks:
        out = chunk_dir / chunk_filename(c)
        if out.exists() and not args.overwrite:
            continue  # Resume: schon erledigt
        if args.seed is not None:
            torch.manual_seed(args.seed)
        wav = model.generate(c["text"], **gen_kwargs)
        ta.save(str(out), wav, sr)
        el = time.time() - t0
        print(f"[{c['idx']:>3}/{len(chunks)}] {out.name}  "
              f"({len(c['text'])} Z, {el:6.1f}s)")

    print("Alle Haeppchen erzeugt.")

    # --- Merge pro Slide ---
    if args.merge_slides or args.merge_full:
        slide_dir = args.outdir / "slides"
        slide_dir.mkdir(parents=True, exist_ok=True)
        slide_wavs = {}
        for s in slides:
            paths = [chunk_dir / chunk_filename(c)
                     for c in chunks if c["slide"] == s]
            merged = concat_wavs(paths, args.gap, sr)
            sp = slide_dir / f"slide_{s:02d}.wav"
            ta.save(str(sp), merged, sr)
            slide_wavs[s] = sp
            print(f"  Slide {s:02d} -> {sp.name}")

        # --- Voll-Merge ---
        if args.merge_full:
            full = concat_wavs([slide_wavs[s] for s in slides],
                               args.slide_gap, sr)
            fp = args.outdir / "ffgft_full.wav"
            ta.save(str(fp), full, sr)
            dur = full.shape[1] / sr
            print(f"Voll-Merge -> {fp}  ({dur/60:.1f} min)")


if __name__ == "__main__":
    main()
