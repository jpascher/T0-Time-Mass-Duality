#!/usr/bin/env python3
"""
T0 Explorer — Tool-Demo Video Generator

Creates a screen-capture-style video demonstrating the T0_Explorer.html tool:
- Shows the interface, moves the slider, clicks through tabs
- Captures value changes in real time
- Adds narration explaining what's happening

Prerequisites:
  pip install playwright gTTS
  playwright install chromium
  # ffmpeg must be installed

Usage:
  python generate_explorer_demo.py                # 1920x1080 landscape
  python generate_explorer_demo.py --portrait     # 1080x1920 vertical (Short)
  python generate_explorer_demo.py --lang en      # English narration
  python generate_explorer_demo.py --no-audio     # No narration
"""

import os, sys, time, shutil, subprocess, tempfile, argparse, io
from pathlib import Path

OUTPUT_FPS = 10  # frames per second in final video

# ============================================================
# DEMO SCENES
# ============================================================
DEMO_SCENES = [
    {
        "name": "opening",
        "min_duration": 12,
        "actions": [
            {"type": "wait", "ms": 1500},
        ],
        "de": "Der T0 Explorer. Ein interaktives Tool, das zeigt, wie ein einziger Parameter die gesamte Physik bestimmt. Bewege den Schieberegler und beobachte, was passiert.",
        "en": "The T0 Explorer. An interactive tool that shows how a single parameter determines all of physics. Move the slider and watch what happens.",
    },
    {
        "name": "masses_default",
        "min_duration": 14,
        "actions": [
            {"type": "click_tab", "tab": 0},
            {"type": "wait", "ms": 800},
        ],
        "de": "Bei Xi gleich vier durch dreissigtausend, dem T0-Wert, stimmen alle neun Teilchenmassen mit dem Experiment ueberein. Die gruenen Balken zeigen: Abweichungen unter zwei Prozent.",
        "en": "At Xi equals four over thirty thousand, the T0 value, all nine particle masses match experiment. The green bars show: deviations under two percent.",
    },
    {
        "name": "slider_up",
        "min_duration": 16,
        "actions": [
            {"type": "click_tab", "tab": 0},
            {"type": "slider_animate", "from": 0.00013333, "to": 0.00016, "steps": 50, "step_ms": 120},
        ],
        "de": "Jetzt erhoehen wir Xi. Beobachte, wie sich die Teilchenmassen sofort aendern. Die Abweichungen wachsen, die Balken werden rot. Nur beim korrekten Wert stimmt alles.",
        "en": "Now we increase Xi. Watch how particle masses change instantly. Deviations grow, bars turn red. Only at the correct value does everything match.",
    },
    {
        "name": "slider_down",
        "min_duration": 16,
        "actions": [
            {"type": "slider_animate", "from": 0.00016, "to": 0.0001, "steps": 50, "step_ms": 120},
        ],
        "de": "Und jetzt nach unten. Die Massen aendern sich in die andere Richtung. Jeder Wert von Xi erzeugt ein komplett anderes Universum mit anderen Teilchen.",
        "en": "And now downward. Masses shift the other direction. Every value of Xi produces a completely different universe with different particles.",
    },
    {
        "name": "reset_perfect",
        "min_duration": 14,
        "actions": [
            {"type": "slider_animate", "from": 0.0001, "to": 0.00013333, "steps": 40, "step_ms": 100},
            {"type": "wait", "ms": 800},
        ],
        "de": "Zurueck zum T0-Wert. Alle Balken werden gruen. Neun Teilchenmassen, drei Fundamentalkonstanten, alle aus einer einzigen Zahl berechnet.",
        "en": "Back to the T0 value. All bars turn green. Nine particle masses, three fundamental constants, all calculated from one single number.",
    },
    {
        "name": "chain",
        "min_duration": 16,
        "actions": [
            {"type": "click_tab", "tab": 1},
            {"type": "wait", "ms": 800},
        ],
        "de": "Der Ketten-Tab zeigt die Ableitungskaskade. Von Xi ueber Alpha, die Teilchenmassen, die fraktale Korrektur, bis hin zur Gravitationskonstante G und der Planck-Laenge. Jeder Schritt berechenbar.",
        "en": "The Chain tab shows the derivation cascade. From Xi through Alpha, particle masses, fractal correction, all the way to the gravitational constant G and the Planck length. Every step computable.",
    },
    {
        "name": "compare",
        "min_duration": 14,
        "actions": [
            {"type": "click_tab", "tab": 2},
            {"type": "wait", "ms": 800},
        ],
        "de": "Der Vergleich: Das Standardmodell braucht ueber zwanzig freie Parameter. T0 braucht genau einen. Gleiche experimentelle Uebereinstimmung, zwanzigmal weniger Parameter.",
        "en": "The comparison: The Standard Model needs over twenty free parameters. T-zero needs exactly one. Same experimental agreement, twenty times fewer parameters.",
    },
    {
        "name": "falsify",
        "min_duration": 14,
        "actions": [
            {"type": "click_tab", "tab": 3},
            {"type": "wait", "ms": 800},
        ],
        "de": "Der Falsifizierungs-Tab: T0 macht konkrete, testbare Vorhersagen. Belle 2, KATRIN, das James Webb Teleskop. Wenn die Messungen nicht stimmen, ist die Theorie widerlegt.",
        "en": "The Falsify tab: T-zero makes concrete, testable predictions. Belle Two, KATRIN, the James Webb Telescope. If measurements disagree, the theory is falsified.",
    },
    {
        "name": "g2",
        "min_duration": 18,
        "actions": [
            {"type": "click_tab", "tab": 4},
            {"type": "wait", "ms": 800},
        ],
        "de": "Und der g minus 2 Tab. Die anomalen magnetischen Momente von Elektron und Myon, berechnet aus der Torus-Geometrie. Die fraktale Korrektur trifft das Experiment auf null Komma null eins vier Prozent. Eine parameterfreie Vorhersage fuer das Tau-Lepton, testbar bei Belle 2.",
        "en": "And the g minus 2 tab. Anomalous magnetic moments of electron and muon, calculated from torus geometry. The fractal correction matches experiment to zero point zero one four percent. A parameter-free prediction for the tau lepton, testable at Belle Two.",
    },
    {
        "name": "final_sweep",
        "min_duration": 14,
        "actions": [
            {"type": "click_tab", "tab": 0},
            {"type": "wait", "ms": 300},
            {"type": "slider_animate", "from": 0.0001, "to": 0.00017, "steps": 50, "step_ms": 80},
            {"type": "slider_animate", "from": 0.00017, "to": 0.00013333, "steps": 40, "step_ms": 80},
            {"type": "wait", "ms": 500},
        ],
        "de": "Ein Parameter. Die gesamte Physik. Probiere es selbst aus. T0 Explorer, von Johann Pascher.",
        "en": "One parameter. All of physics. Try it yourself. T0 Explorer, by Johann Pascher.",
    },
]


# ============================================================
# TTS
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

def detect_engine(preferred=None):
    order = [preferred] if preferred else ['gtts', 'edge', 'pyttsx3']
    for eng in order:
        if eng is None: continue
        try:
            if eng == 'gtts':
                from gtts import gTTS
                buf = io.BytesIO(); gTTS("Test", lang="de").write_to_fp(buf)
                if buf.tell() > 0: print(f"  OK: gTTS"); return 'gtts'
            elif eng == 'edge':
                import edge_tts, asyncio
                async def test():
                    async for _ in edge_tts.Communicate("Test.", "de-DE-ConradNeural").stream(): return True
                asyncio.run(test()); print(f"  OK: edge-tts"); return 'edge'
        except Exception as e:
            print(f"  X {eng}: {e}")
    return None

def generate_audio(text, lang, path, engine):
    fn = {'gtts': gen_tts_gtts, 'edge': gen_tts_edge}[engine]
    for a in range(3):
        try:
            fn(text, lang, path)
            if os.path.exists(path) and os.path.getsize(path) > 100: return True
        except: time.sleep(1)
    return False

def get_audio_duration(path):
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=10)
        return float(r.stdout.strip())
    except: return 5.0


# ============================================================
# CORE: Record one scene → produce MP4 with matching audio
# ============================================================
def record_scene(page, scene, scene_idx, tmpdir, lang, width, height, engine, no_audio):
    """
    1. Execute browser actions, capture frames
    2. Generate TTS audio
    3. target_dur = max(audio + 2.5s, min_duration)
    4. Pad last frame to fill target_dur at OUTPUT_FPS
    5. Encode to MP4
    """
    scene_dir = os.path.join(tmpdir, f"scene_{scene_idx:02d}")
    os.makedirs(scene_dir, exist_ok=True)

    frames = []

    def take_frame():
        path = os.path.join(scene_dir, f"f_{len(frames):05d}.png")
        page.screenshot(path=path, type="png")
        frames.append(path)

    # --- 1. Execute actions, capture frames ---
    for action in scene["actions"]:
        atype = action["type"]

        if atype == "wait":
            ms = action["ms"]
            n = max(1, int(ms / 1000 * OUTPUT_FPS))
            interval = ms / n
            for _ in range(n):
                take_frame()
                page.wait_for_timeout(int(interval))

        elif atype == "click_tab":
            page.evaluate(f"""
                const btns = document.querySelectorAll('.tab-btn');
                if (btns[{action['tab']}]) btns[{action['tab']}].click();
            """)
            page.wait_for_timeout(300)
            take_frame()

        elif atype == "slider_animate":
            fr = action["from"]
            to = action["to"]
            steps = action.get("steps", 40)
            step_ms = action.get("step_ms", 100)
            ms_per_frame = 1000 / OUTPUT_FPS
            ms_acc = 0

            for step in range(steps + 1):
                t = step / steps
                t_ease = t * t * (3 - 2 * t)
                val = fr + (to - fr) * t_ease

                page.evaluate(f"""
                    const sl = document.getElementById('xi-slider');
                    sl.value = {val};
                    sl.dispatchEvent(new Event('input'));
                """)
                page.wait_for_timeout(step_ms)
                ms_acc += step_ms

                if ms_acc >= ms_per_frame or step == 0 or step == steps:
                    take_frame()
                    ms_acc = 0

    if not frames:
        take_frame()

    action_frames = len(frames)

    # --- 2. Generate audio ---
    audio_path = os.path.join(scene_dir, "narration.mp3")
    has_audio = False
    audio_dur = 0

    if not no_audio and engine:
        text = scene.get(lang, scene.get("en", ""))
        if text and generate_audio(text, lang, audio_path, engine):
            has_audio = True
            audio_dur = get_audio_duration(audio_path)

    # --- 3. Target duration ---
    if has_audio:
        target_dur = max(audio_dur + 2.5, scene["min_duration"])
    else:
        target_dur = scene["min_duration"]

    # --- 4. Pad frames to fill target duration ---
    total_frames_needed = int(target_dur * OUTPUT_FPS)
    pad_count = max(0, total_frames_needed - len(frames))

    if pad_count > 0 and frames:
        last_frame = frames[-1]
        for _ in range(pad_count):
            dst = os.path.join(scene_dir, f"f_{len(frames):05d}.png")
            shutil.copy2(last_frame, dst)
            frames.append(dst)

    print(f"      {action_frames} Aktions + {pad_count} Halte = {len(frames)} Frames ({target_dur:.1f}s)")

    # --- 5. Encode MP4 ---
    scene_mp4 = os.path.join(tmpdir, f"scene_{scene_idx:02d}.mp4")
    frame_pattern = os.path.join(scene_dir, "f_%05d.png")

    if has_audio:
        cmd = [
            "ffmpeg", "-y",
            "-framerate", str(OUTPUT_FPS),
            "-i", frame_pattern,
            "-i", audio_path,
            "-c:v", "libx264", "-preset", "fast", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-vf", f"scale={width}:{height}",
            "-r", "30",
            "-t", f"{target_dur:.2f}",
            scene_mp4
        ]
    else:
        cmd = [
            "ffmpeg", "-y",
            "-framerate", str(OUTPUT_FPS),
            "-i", frame_pattern,
            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-c:v", "libx264", "-preset", "fast", "-tune", "stillimage",
            "-c:a", "aac",
            "-pix_fmt", "yuv420p",
            "-vf", f"scale={width}:{height}",
            "-r", "30",
            "-t", f"{target_dur:.2f}",
            scene_mp4
        ]

    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        print(f"      X ffmpeg: {r.stderr[-300:]}")
        return None

    # Verify actual duration
    icon = "🔊" if has_audio else "🔇"
    try:
        dr = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", scene_mp4],
            capture_output=True, text=True, timeout=10)
        actual = float(dr.stdout.strip())
    except:
        actual = target_dur

    print(f"      {icon} Ergebnis: {actual:.1f}s (Audio: {audio_dur:.1f}s, Ziel: {target_dur:.1f}s)")
    return scene_mp4


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="T0 Explorer Demo Video")
    parser.add_argument("--lang", choices=["de", "en"], default="de")
    parser.add_argument("--engine", choices=["gtts", "edge"], default=None)
    parser.add_argument("--no-audio", action="store_true")
    parser.add_argument("--portrait", action="store_true",
                        help="1080x1920 vertical (YouTube Short)")
    parser.add_argument("--landscape", action="store_true",
                        help="1920x1080 (default)")
    parser.add_argument("--html", default="T0_Explorer.html")
    args = parser.parse_args()

    if args.portrait:
        width, height = 1080, 1920
    else:
        width, height = 1920, 1080

    lang_name = "Deutsch" if args.lang == "de" else "English"

    print("=" * 60)
    print(f"T0 Explorer — Demo Video ({lang_name})")
    print(f"Format: {width}x{height} | {OUTPUT_FPS} fps Aufnahme")
    print("=" * 60)

    if not shutil.which("ffmpeg"):
        print("X ffmpeg nicht gefunden!"); sys.exit(1)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("X pip install playwright && playwright install chromium"); sys.exit(1)
    if not os.path.exists(args.html):
        print(f"X {args.html} nicht gefunden!"); sys.exit(1)

    engine = None
    if not args.no_audio:
        print("\nTTS-Engine...")
        engine = detect_engine(args.engine)
        if not engine: print("! Kein TTS. pip install gTTS")

    suffix = "DE" if args.lang == "de" else "EN"
    output = f"T0_Explorer_Demo_{suffix}.mp4"

    tmpdir = tempfile.mkdtemp(prefix="t0demo_")
    try:
        from playwright.sync_api import sync_playwright
        html_url = Path(args.html).resolve().as_uri()
        print(f"\n  Browser: {html_url}")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(html_url, wait_until="networkidle")
            page.wait_for_timeout(3000)

            # Hide nav buttons and zoom the whole page to fill viewport
            page.evaluate("""
                // Hide home and language buttons completely
                document.querySelectorAll('a[href="index.html"]').forEach(el => el.parentElement.style.display='none');
                document.querySelectorAll('#btn-de, #btn-en').forEach(el => el.parentElement.style.display='none');

                // Hide footer to save space
                const footer = document.querySelector('.footer');
                if (footer) footer.style.display = 'none';

                // Zoom entire page to fill viewport — removes empty margins
                document.body.style.transformOrigin = 'top center';
                document.body.style.transform = 'scale(1.45)';
            """)

            scene_videos = []
            for si, scene in enumerate(DEMO_SCENES):
                print(f"\n    [{si+1}/{len(DEMO_SCENES)}] {scene['name']}")
                mp4 = record_scene(page, scene, si, tmpdir,
                                   args.lang, width, height, engine, args.no_audio)
                if mp4: scene_videos.append(mp4)

            browser.close()

        if not scene_videos:
            print("\n  X Keine Szenen!"); sys.exit(1)

        # Concat
        concat = os.path.join(tmpdir, "concat.txt")
        with open(concat, "w") as f:
            for sv in scene_videos:
                f.write(f"file '{os.path.basename(sv)}'\n")

        print(f"\n  Zusammenfuegen ({len(scene_videos)} Szenen)...")
        r = subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat,
            "-c", "copy", "-movflags", "+faststart", output
        ], capture_output=True, text=True, timeout=1800)

        if r.returncode != 0:
            print(f"  X {r.stderr[-300:]}"); sys.exit(1)

        mb = os.path.getsize(output) / 1024 / 1024
        try:
            dr = subprocess.run(
                ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", output],
                capture_output=True, text=True)
            secs = float(dr.stdout.strip())
        except: secs = 0

        print(f"\n{'='*60}")
        print(f"  FERTIG: {output}")
        print(f"  {mb:.1f} MB | {secs:.0f}s ({secs/60:.1f} min)")
        print(f"{'='*60}")

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
