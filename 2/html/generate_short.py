#!/usr/bin/env python3
"""
Generate YouTube Short videos (vertical 1080x1920, ~65s) from T0 HTML files.

Takes animated scene screenshots + generates TTS narration → combines to MP4.

Prerequisites:
  pip install playwright gTTS
  playwright install chromium
  # ffmpeg must be installed

Usage:
  python generate_short.py               # Both DE + EN
  python generate_short.py --lang de     # Only German
  python generate_short.py --lang en     # Only English
  python generate_short.py --engine gtts # Force TTS engine
  python generate_short.py --no-audio    # Video only, no narration
"""

import os, sys, time, shutil, subprocess, tempfile, argparse, io
from pathlib import Path

WIDTH = 1080
HEIGHT = 1920

# ============================================================
# SCENE DEFINITIONS with narration
# Each scene: { html_id, duration_sec, narration_de, narration_en }
# ============================================================
SCENES = [
    {
        "id": "scene-1",
        "duration": 8,
        "wait_before_screenshot": 2000,  # ms - wait for animations
        "de": "Was, wenn die gesamte Physik aus einer einzigen Zahl folgen wuerde? Keine 20 Parameter. Kein Feintuning. Eine einzige geometrische Zahl.",
        "en": "What if all of physics came from one single number? Not twenty parameters. Not fine-tuning. One single geometric number.",
    },
    {
        "id": "scene-2",
        "duration": 10,
        "wait_before_screenshot": 2500,
        "de": "Der Parameter Xi. Vier geteilt durch dreissigtausend. Ein dimensionsloses Verhaeltnis aus der tetraedrischen Kugelpackung. Die Windungszahl des fundamentalen Torus der Raumzeit.",
        "en": "The parameter Xi. Four divided by thirty thousand. A dimensionless ratio from tetrahedral sphere packing. The winding number of spacetime's fundamental torus.",
    },
    {
        "id": "scene-3",
        "duration": 12,
        "wait_before_screenshot": 3000,
        "de": "Aus Xi folgt jede Teilchenmasse. Elektron, Myon, Tau, alle Quarks. Jede einzelne Masse wird berechnet, nicht angepasst. Die Abweichungen vom Experiment liegen unter einem Prozent. Alles aus einer Zahl. Ohne Anpassung. Ohne freie Parameter.",
        "en": "From Xi follows every particle mass. Electron, muon, tau, all quarks. Each mass is calculated, not fitted. Deviations from experiment are below one percent. All from one number. No fitting. No free parameters.",
    },
    {
        "id": "scene-4",
        "duration": 10,
        "wait_before_screenshot": 2500,
        "de": "Das Standardmodell braucht ueber 20 freie Parameter. T0 braucht genau einen. Gleiche experimentelle Uebereinstimmung. Zwanzigmal weniger Parameter. Ockhams Rasiermesser hat ein klares Urteil.",
        "en": "The Standard Model needs over 20 free parameters. T-zero needs exactly one. Same experimental agreement. Twenty times fewer parameters. Occam's Razor has a clear verdict.",
    },
    {
        "id": "scene-5",
        "duration": 10,
        "wait_before_screenshot": 3000,
        "de": "Die Ableitungskaskade: Aus Xi folgt die Feinstrukturkonstante Alpha. Daraus alle Teilchenmassen. Die fraktale Korrektur K fraktal. Die Gravitationskonstante G, abgeleitet, nicht eingefuegt. Und schliesslich die Zeit-Masse-Dualitaet: T mal m gleich eins.",
        "en": "The derivation cascade: From Xi follows the fine structure constant Alpha. Then all particle masses. The fractal correction K-fractal. The gravitational constant G, derived, not inserted. And finally time-mass duality: T times m equals one.",
    },
    {
        "id": "scene-6",
        "duration": 8,
        "wait_before_screenshot": 2500,
        "de": "Und das Beste: T0 ist testbar. Belle 2 kann die Tau-Anomalie messen. Die Rotverschiebung entsteht in T0 durch fraktale Wegverlaengerung, nicht durch Expansion. Keine frequenzabhaengige Rotverschiebung, selbes Ergebnis wie im Standardmodell. Die g minus 2 Korrektur stimmt auf null Komma null eins vier Prozent.",
        "en": "And the best part: T-zero is testable. Belle Two can measure the tau anomaly. In T-zero, redshift arises from fractal path lengthening, not expansion. No frequency-dependent redshift, same result as the Standard Model. The g minus 2 correction matches to zero point zero one four percent.",
    },
    {
        "id": "scene-7",
        "duration": 7,
        "wait_before_screenshot": 2500,
        "de": "T0-Theorie. Ein Parameter. Die gesamte Physik. Johann Pascher.",
        "en": "T-zero Theory. One parameter. All of physics. Johann Pascher.",
    },
]


# ============================================================
# TTS ENGINES
# ============================================================
def gen_tts_gtts(text, lang, path):
    from gtts import gTTS
    gTTS(text=text, lang=lang, slow=False).save(path)

def gen_tts_edge(text, lang, path):
    import asyncio, edge_tts
    v = "de-DE-ConradNeural" if lang == "de" else "en-US-GuyNeural"
    async def run():
        await edge_tts.Communicate(text, v).save(path)
    asyncio.run(run())

def gen_tts_pyttsx3(text, lang, path):
    import pyttsx3
    e = pyttsx3.init()
    for v in e.getProperty('voices'):
        t = 'german' if lang == 'de' else 'english'
        if t in v.name.lower():
            e.setProperty('voice', v.id)
            break
    e.setProperty('rate', 160)
    e.save_to_file(text, path)
    e.runAndWait()

def detect_engine(preferred=None):
    order = [preferred] if preferred else ['gtts', 'edge', 'pyttsx3']
    for eng in order:
        if eng is None:
            continue
        try:
            if eng == 'gtts':
                from gtts import gTTS
                buf = io.BytesIO()
                gTTS("Test", lang="de").write_to_fp(buf)
                if buf.tell() > 0:
                    print(f"  ✓ gTTS verfuegbar")
                    return 'gtts'
            elif eng == 'edge':
                import edge_tts, asyncio
                async def test():
                    async for _ in edge_tts.Communicate("Test.", "de-DE-ConradNeural").stream():
                        return True
                asyncio.run(test())
                print(f"  ✓ edge-tts verfuegbar")
                return 'edge'
            elif eng == 'pyttsx3':
                import pyttsx3
                pyttsx3.init().stop()
                print(f"  ✓ pyttsx3 verfuegbar")
                return 'pyttsx3'
        except Exception as e:
            print(f"  ✗ {eng}: {e}")
    return None

def generate_audio(text, lang, path, engine):
    fn = {'gtts': gen_tts_gtts, 'edge': gen_tts_edge, 'pyttsx3': gen_tts_pyttsx3}[engine]
    for attempt in range(3):
        try:
            fn(text, lang, path)
            if os.path.exists(path) and os.path.getsize(path) > 100:
                return True
        except Exception as e:
            if attempt < 2:
                time.sleep(1)
            else:
                print(f"    ✗ Audio-Fehler: {e}")
    return False


def get_audio_duration(path):
    """Get MP3 duration in seconds."""
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=10
        )
        return float(r.stdout.strip())
    except:
        return 5.0


# ============================================================
# SCREENSHOT CAPTURE
# ============================================================
def capture_scenes(html_path, tmpdir, scenes, lang):
    """Capture each scene as a screenshot with animations played."""
    from playwright.sync_api import sync_playwright

    html_url = Path(html_path).resolve().as_uri()
    print(f"  Browser: {html_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT})

        for i, scene in enumerate(scenes):
            # Fresh page load for each scene — guarantees zero overlap
            page.goto(html_url, wait_until="networkidle")
            page.wait_for_timeout(1000)

            # Remove ALL scenes from DOM except the target one
            page.evaluate(f"""
                document.querySelectorAll('.scene').forEach(s => {{
                    if (s.id !== '{scene["id"]}') s.remove();
                }});
                const active = document.getElementById('{scene["id"]}');
                active.classList.add('active');
                active.style.display = 'flex';
                active.style.opacity = '1';
            """)

            # Wait for animations
            page.wait_for_timeout(scene.get("wait_before_screenshot", 2000))

            # Screenshot
            path = os.path.join(tmpdir, f"scene_{i:02d}.png")
            page.screenshot(path=path, type="png")
            print(f"    📸 Szene {i+1}/{len(scenes)}: {scene['id']}")

        browser.close()


# ============================================================
# VIDEO CREATION
# ============================================================
def create_short_video(tmpdir, scenes, lang, output_path, engine=None, no_audio=False):
    """Combine scene screenshots + audio into MP4."""

    slide_videos = []
    total_duration = 0

    for i, scene in enumerate(scenes):
        img_path = os.path.join(tmpdir, f"scene_{i:02d}.png")
        audio_path = os.path.join(tmpdir, f"audio_{i:02d}.mp3")
        slide_mp4 = os.path.join(tmpdir, f"sv_{i:02d}.mp4")

        if not os.path.exists(img_path):
            print(f"    ⚠ Kein Screenshot fuer Szene {i}")
            continue

        # Generate narration
        has_audio = False
        duration = scene["duration"]

        if not no_audio and engine:
            text = scene.get(lang, scene.get("en", ""))
            if text and generate_audio(text, lang, audio_path, engine):
                has_audio = True
                # Use audio duration + 1s padding, but at least the scene duration
                audio_dur = get_audio_duration(audio_path)
                duration = max(scene["duration"], audio_dur + 2.5)

        total_duration += duration

        if has_audio:
            cmd = [
                "ffmpeg", "-y", "-loop", "1",
                "-i", img_path, "-i", audio_path,
                "-c:v", "libx264", "-tune", "stillimage",
                "-c:a", "aac", "-b:a", "192k",
                "-pix_fmt", "yuv420p",
                "-vf", f"scale={WIDTH}:{HEIGHT}",
                "-shortest", "-t", str(duration),
                "-r", "30", slide_mp4
            ]
        else:
            cmd = [
                "ffmpeg", "-y", "-loop", "1",
                "-i", img_path,
                "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                "-c:v", "libx264", "-tune", "stillimage",
                "-c:a", "aac", "-pix_fmt", "yuv420p",
                "-vf", f"scale={WIDTH}:{HEIGHT}",
                "-t", str(duration),
                "-r", "30", slide_mp4
            ]

        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            print(f"    ✗ Fehler Szene {i}: {r.stderr[-200:]}")
            continue

        icon = "🔊" if has_audio else "🔇"
        print(f"    {icon} Szene {i+1}: {duration:.1f}s")
        slide_videos.append(slide_mp4)

    if not slide_videos:
        print("  ✗ Keine Videos erstellt!")
        return False

    # Concatenate
    concat_file = os.path.join(tmpdir, "concat.txt")
    with open(concat_file, "w") as f:
        for sv in slide_videos:
            f.write(f"file '{os.path.basename(sv)}'\n")

    print(f"\n  🎬 Zusammenfuegen...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_file,
        "-c", "copy",
        "-movflags", "+faststart",
        output_path
    ]

    r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    if r.returncode != 0:
        print(f"  ✗ Concat-Fehler: {r.stderr[-300:]}")
        return False

    size_mb = os.path.getsize(output_path) / 1024 / 1024
    print(f"  ✓ {output_path} ({size_mb:.1f} MB, ~{total_duration:.0f}s)")
    return True


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="T0 YouTube Short Generator")
    parser.add_argument("--lang", choices=["de", "en", "both"], default="both")
    parser.add_argument("--engine", choices=["gtts", "edge", "pyttsx3"], default=None)
    parser.add_argument("--no-audio", action="store_true", help="Nur Video, kein Audio")
    parser.add_argument("--output-dir", default=".", help="Ausgabeverzeichnis")
    args = parser.parse_args()

    print("=" * 60)
    print("T0 YouTube Short Generator")
    print(f"Format: {WIDTH}×{HEIGHT} (9:16 vertikal)")
    print("=" * 60)

    # Check prerequisites
    if not shutil.which("ffmpeg"):
        print("✗ ffmpeg nicht gefunden!"); sys.exit(1)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("✗ playwright nicht installiert: pip install playwright && playwright install chromium")
        sys.exit(1)

    # Detect TTS engine
    engine = None
    if not args.no_audio:
        print("\nTTS-Engine pruefen...")
        engine = detect_engine(args.engine)
        if not engine:
            print("⚠ Keine TTS-Engine! Video wird ohne Audio erstellt.")
            print("  Installiere: pip install gTTS")

    # Jobs
    jobs = []
    if args.lang in ("de", "both"):
        if os.path.exists("T0_Short_DE.html"):
            jobs.append(("de", "T0_Short_DE.html", "T0_Short_DE.mp4"))
        else:
            print("⚠ T0_Short_DE.html nicht gefunden")

    if args.lang in ("en", "both"):
        if os.path.exists("T0_Short_EN.html"):
            jobs.append(("en", "T0_Short_EN.html", "T0_Short_EN.mp4"))
        else:
            print("⚠ T0_Short_EN.html nicht gefunden")

    if not jobs:
        print("Keine HTML-Dateien gefunden!"); sys.exit(1)

    results = []
    for lang, html, output in jobs:
        print(f"\n{'='*60}")
        name = "Deutsch" if lang == "de" else "English"
        print(f"📽  T0 Short ({name})")
        print(f"{'='*60}")

        tmpdir = tempfile.mkdtemp(prefix="t0short_")
        output_path = os.path.join(args.output_dir, output)

        try:
            print(f"\n  📸 Screenshots aufnehmen...")
            capture_scenes(html, tmpdir, SCENES, lang)

            print(f"\n  🎤 Audio + Video erstellen...")
            ok = create_short_video(tmpdir, SCENES, lang, output_path, engine, args.no_audio)
            results.append((name, output_path, ok))
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

    # Summary
    print(f"\n{'='*60}")
    print("ERGEBNIS")
    print(f"{'='*60}")
    for name, path, ok in results:
        if ok:
            mb = os.path.getsize(path) / 1024 / 1024
            print(f"  ✓ {name}: {path} ({mb:.1f} MB)")
        else:
            print(f"  ✗ {name}: FEHLER")

    print(f"\n📱 Videos sind bereit fuer YouTube Shorts / TikTok / Instagram Reels!")
    print(f"   Format: {WIDTH}×{HEIGHT} (9:16), unter 60 Sekunden")


if __name__ == "__main__":
    main()
