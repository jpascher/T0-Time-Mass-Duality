#!/usr/bin/env python3
"""
Generate TTS audio for T0 Cinematic Short.

Creates per-scene MP3s and a combined full_audio.mp3.
Auto-detects best TTS engine: edge-tts → gTTS → pyttsx3.

Usage:
  python generate_cinematic_audio.py              # DE
  python generate_cinematic_audio.py --lang en     # EN
  python generate_cinematic_audio.py --lang both   # DE + EN
  python generate_cinematic_audio.py --engine gtts # Force engine

Prerequisites:
  pip install edge-tts gTTS pyttsx3
"""

import os, sys, subprocess, argparse, io

TEXTS = {
    "de": [
        "Was, wenn die gesamte Physik aus einer einzigen Zahl folgen wuerde? Keine 20 Parameter. Kein Feintuning. Eine einzige geometrische Zahl.",
        "Der Parameter Xi. Vier geteilt durch dreissigtausend. Ein dimensionsloses Verhaeltnis aus der tetraedrischen Kugelpackung. Die Windungszahl des fundamentalen Torus der Raumzeit.",
        "Aus Xi folgt jede Teilchenmasse. Elektron, Myon, Tau, alle Quarks. Jede einzelne Masse wird berechnet, nicht angepasst. Die Abweichungen vom Experiment liegen unter einem Prozent. Alles aus einer Zahl.",
        "Das Standardmodell braucht ueber 20 freie Parameter. T0 braucht genau einen. Gleiche experimentelle Uebereinstimmung. Zwanzigmal weniger Parameter. Ockhams Rasiermesser hat ein klares Urteil.",
        "Die Ableitungskaskade: Aus Xi folgt die Feinstrukturkonstante Alpha. Daraus alle Teilchenmassen. Die fraktale Korrektur K fraktal. Die Gravitationskonstante G, abgeleitet, nicht eingefuegt. Und schliesslich die Zeit-Masse-Dualitaet: T mal m gleich eins.",
        "Und das Beste: T0 ist testbar. Belle 2 kann die Tau-Anomalie messen. Die Rotverschiebung entsteht in T0 durch fraktale Wegverlaengerung. Die g minus 2 Korrektur stimmt auf null Komma null eins vier Prozent.",
        "T0-Theorie. Ein Parameter. Die gesamte Physik. Johann Pascher.",
    ],
    "en": [
        "What if all of physics came from one single number? Not twenty parameters. Not fine-tuning. One single geometric number.",
        "The parameter Xi. Four divided by thirty thousand. A dimensionless ratio from tetrahedral sphere packing. The winding number of spacetime's fundamental torus.",
        "From Xi follows every particle mass. Electron, muon, tau, all quarks. Each mass is calculated, not fitted. Deviations from experiment are below one percent. All from one number.",
        "The Standard Model needs over 20 free parameters. T-zero needs exactly one. Same experimental agreement. Twenty times fewer parameters. Occam's Razor has a clear verdict.",
        "The derivation cascade: From Xi follows the fine structure constant Alpha. Then all particle masses. The fractal correction K-fractal. The gravitational constant G, derived, not inserted. And finally time-mass duality: T times m equals one.",
        "And the best part: T-zero is testable. Belle Two can measure the tau anomaly. Redshift arises from fractal path lengthening. The g minus 2 correction matches to zero point zero one four percent.",
        "T-zero Theory. One parameter. All of physics. Johann Pascher.",
    ],
}

SCENE_NAMES = ["01_hook", "02_xi", "03_masses", "04_compare", "05_cascade", "06_testable", "07_cta"]


# ============================================================
# TTS ENGINES
# ============================================================
def gen_edge(text, lang, path):
    import edge_tts, asyncio
    voice = "de-DE-ConradNeural" if lang == "de" else "en-US-GuyNeural"
    asyncio.run(edge_tts.Communicate(text, voice).save(path))

def gen_gtts(text, lang, path):
    from gtts import gTTS
    gTTS(text=text, lang=lang, slow=False).save(path)

def gen_pyttsx3(text, lang, path):
    import pyttsx3
    e = pyttsx3.init()
    e.setProperty('rate', 160)
    for v in e.getProperty('voices'):
        if lang == "de" and ('german' in v.name.lower() or 'de' in v.id.lower()):
            e.setProperty('voice', v.id); break
        if lang == "en" and ('english' in v.name.lower()):
            e.setProperty('voice', v.id); break
    e.save_to_file(text, path)
    e.runAndWait()


def detect_engine():
    """Auto-detect best available TTS engine."""
    # edge-tts (best quality)
    try:
        import edge_tts, asyncio
        async def test():
            await edge_tts.Communicate("Test", "de-DE-ConradNeural").save("_tts_test.mp3")
        asyncio.run(test())
        if os.path.exists("_tts_test.mp3") and os.path.getsize("_tts_test.mp3") > 1000:
            os.remove("_tts_test.mp3")
            return "edge"
    except:
        pass
    if os.path.exists("_tts_test.mp3"): os.remove("_tts_test.mp3")

    # gTTS (good quality)
    try:
        from gtts import gTTS
        buf = io.BytesIO()
        gTTS("Test", lang="de").write_to_fp(buf)
        if buf.tell() > 500:
            return "gtts"
    except:
        pass

    # pyttsx3 (offline fallback)
    try:
        import pyttsx3
        pyttsx3.init()
        return "pyttsx3"
    except:
        pass

    return None


def generate(text, lang, path, engine):
    """Generate TTS audio file."""
    try:
        fn = {"edge": gen_edge, "gtts": gen_gtts, "pyttsx3": gen_pyttsx3}[engine]
        fn(text, lang, path)
        return os.path.exists(path) and os.path.getsize(path) > 500
    except Exception as ex:
        print(f"    ❌ {ex}")
        return False


def get_duration(path):
    """Get audio duration in seconds."""
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=10)
        return float(r.stdout.strip())
    except:
        return 0


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="T0 Cinematic Audio Generator")
    parser.add_argument("--lang", default="de", choices=["de", "en", "both"])
    parser.add_argument("--engine", default=None, choices=["edge", "gtts", "pyttsx3"])
    parser.add_argument("--outdir", default="audio")
    args = parser.parse_args()

    engine = args.engine or detect_engine()
    if not engine:
        print("❌ No TTS engine found! Install: pip install edge-tts gTTS pyttsx3")
        sys.exit(1)
    print(f"🎤 TTS Engine: {engine}")

    languages = ["de", "en"] if args.lang == "both" else [args.lang]

    for lang in languages:
        outdir = os.path.join(args.outdir, f"cinematic_{lang}")
        os.makedirs(outdir, exist_ok=True)

        print(f"\n{'='*50}")
        print(f"  CINEMATIC SHORT — {lang.upper()}")
        print(f"{'='*50}")

        texts = TEXTS[lang]
        files = []
        total_dur = 0

        for i, text in enumerate(texts):
            path = os.path.join(outdir, f"{SCENE_NAMES[i]}.mp3")
            print(f"\n  Scene {i+1}/7: {SCENE_NAMES[i]}")

            if generate(text, lang, path, engine):
                dur = get_duration(path)
                total_dur += dur
                files.append(path)
                print(f"    ✅ {dur:.1f}s — {path}")
            else:
                print(f"    ❌ Failed!")

        # Concat to full audio
        if files and len(files) == 7:
            concat_file = os.path.join(outdir, "concat.txt")
            with open(concat_file, "w") as f:
                for fp in files:
                    f.write(f"file '{os.path.basename(fp)}'\n")

            full = os.path.join(outdir, f"cinematic_{lang}_full.mp3")
            cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
                   "-i", concat_file, "-c", "copy", full]
            subprocess.run(cmd, capture_output=True, cwd=outdir, timeout=60)
            os.remove(concat_file)

            if os.path.exists(full):
                dur = get_duration(full)
                print(f"\n  📻 Full audio: {full}")
                print(f"     Duration: {dur:.1f}s")
                print(f"     Size: {os.path.getsize(full)/1024:.0f} KB")

        print(f"\n  📂 Files in: {outdir}/")
        print(f"  ⏱️  Total: {total_dur:.1f}s")

    print("\n🎬 Done!")


if __name__ == "__main__":
    main()
