#!/usr/bin/env python3
"""
Generate MP4 videos from FFGFT HTML presentations + MP3 audio.

Takes screenshots of each slide, combines with audio into a video.

Prerequisites:
  pip install playwright
  playwright install chromium
  
  # ffmpeg must be installed:
  # Windows: https://www.gyan.dev/ffmpeg/builds/ (download, add to PATH)
  # or: winget install ffmpeg
  # Mac: brew install ffmpeg
  # Linux: sudo apt install ffmpeg

Usage:
  python generate_video.py                    # Both videos
  python generate_video.py --only narrativ    # Only narrative
  python generate_video.py --only presentation # Only presentation
  python generate_video.py --lang de          # Presentation only German
  python generate_video.py --resolution 1920x1080  # Full HD (default)
  python generate_video.py --resolution 3840x2160  # 4K
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
import tempfile
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================
RESOLUTION = "1920x1080"  # width x height
FPS = 1  # Low FPS is fine for slides (saves space)
VIDEO_FPS = 30  # Output video FPS for smooth playback
TRANSITION_MS = 400  # Time to wait after slide change for animations
PAUSE_AFTER_SLIDE = 0.8  # Extra seconds of silence between slides
MIN_SLIDE_DURATION = 3.0  # Minimum seconds per slide (if no audio)

# ============================================================
# HELPERS
# ============================================================

def check_prerequisites():
    """Check that all required tools are available."""
    errors = []
    
    # Check ffmpeg
    if not shutil.which("ffmpeg"):
        errors.append(
            "ffmpeg nicht gefunden!\n"
            "  Windows: winget install ffmpeg  ODER  https://www.gyan.dev/ffmpeg/builds/\n"
            "  Mac:     brew install ffmpeg\n"
            "  Linux:   sudo apt install ffmpeg"
        )
    
    # Check ffprobe
    if not shutil.which("ffprobe"):
        errors.append("ffprobe nicht gefunden (kommt normalerweise mit ffmpeg)")
    
    # Check playwright
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        errors.append(
            "playwright nicht installiert!\n"
            "  pip install playwright\n"
            "  playwright install chromium"
        )
    
    if errors:
        print("FEHLER: Voraussetzungen nicht erfuellt:\n")
        for e in errors:
            print(f"  ✗ {e}\n")
        sys.exit(1)


def get_mp3_duration(path):
    """Get duration of an MP3 file in seconds using ffprobe."""
    if not os.path.exists(path):
        return MIN_SLIDE_DURATION
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=10
        )
        return float(result.stdout.strip()) + PAUSE_AFTER_SLIDE
    except Exception:
        return MIN_SLIDE_DURATION


def capture_slides(html_path, num_slides, screenshot_dir, width, height, lang=None):
    """Open HTML in headless browser, navigate slides, take screenshots."""
    from playwright.sync_api import sync_playwright
    
    html_url = Path(html_path).resolve().as_uri()
    print(f"  Browser oeffnen: {html_url}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(html_url, wait_until="networkidle")
        
        # Wait for fonts and KaTeX to load
        page.wait_for_timeout(2000)
        
        # Set language if needed (for presentation.html)
        if lang == "en":
            try:
                page.evaluate("setLang('en')")
                page.wait_for_timeout(500)
            except Exception:
                pass
        
        for i in range(num_slides):
            # Navigate to slide
            if i > 0:
                # Try different navigation functions
                try:
                    page.evaluate(f"showSlide({i})")
                except Exception:
                    try:
                        page.evaluate(f"go({i})")
                    except Exception:
                        pass
                page.wait_for_timeout(TRANSITION_MS)
            
            # Hide navigation bar for cleaner screenshots
            page.evaluate("""
                document.querySelectorAll('.nav, .nav-bar').forEach(el => el.style.display = 'none');
                document.querySelectorAll('.progress, #prog').forEach(el => el.style.display = 'none');
            """)
            page.wait_for_timeout(100)
            
            # Take screenshot
            screenshot_path = os.path.join(screenshot_dir, f"slide_{i:03d}.png")
            page.screenshot(path=screenshot_path, type="png")
            
            # Show nav again (in case it affects layout)
            page.evaluate("""
                document.querySelectorAll('.nav, .nav-bar').forEach(el => el.style.display = '');
                document.querySelectorAll('.progress, #prog').forEach(el => el.style.display = '');
            """)
            
            print(f"    Screenshot {i+1}/{num_slides}: slide_{i:03d}.png")
        
        browser.close()


def create_video(screenshot_dir, audio_dir, audio_prefix, num_slides, output_path, width, height):
    """Combine screenshots + audio into MP4 video using ffmpeg."""
    
    # Create a concat file for ffmpeg
    concat_file = os.path.join(screenshot_dir, "concat.txt")
    
    # First pass: create individual slide videos with audio
    slide_videos = []
    
    for i in range(num_slides):
        img_path = os.path.join(screenshot_dir, f"slide_{i:03d}.png")
        mp3_path = os.path.join(audio_dir, f"{audio_prefix}_{i:02d}.mp3")
        slide_video = os.path.join(screenshot_dir, f"sv_{i:03d}.mp4")
        
        if not os.path.exists(img_path):
            print(f"    ⚠ Kein Screenshot fuer Folie {i}")
            continue
        
        duration = get_mp3_duration(mp3_path)
        
        if os.path.exists(mp3_path):
            # Slide with audio
            cmd = [
                "ffmpeg", "-y", "-loop", "1",
                "-i", img_path,
                "-i", mp3_path,
                "-c:v", "libx264",
                "-tune", "stillimage",
                "-c:a", "aac", "-b:a", "192k",
                "-pix_fmt", "yuv420p",
                "-vf", f"scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black",
                "-shortest",
                "-t", str(duration),
                "-r", str(VIDEO_FPS),
                slide_video
            ]
        else:
            # Slide without audio (use minimum duration with silence)
            cmd = [
                "ffmpeg", "-y", "-loop", "1",
                "-i", img_path,
                "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=stereo",
                "-c:v", "libx264",
                "-tune", "stillimage",
                "-c:a", "aac",
                "-pix_fmt", "yuv420p",
                "-vf", f"scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black",
                "-t", str(duration),
                "-r", str(VIDEO_FPS),
                slide_video
            ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"    ✗ Fehler bei Folie {i}: {result.stderr[-200:]}")
            continue
        
        slide_videos.append(slide_video)
        dur_str = f"{duration:.1f}s"
        has_audio = "🔊" if os.path.exists(mp3_path) else "🔇"
        print(f"    {has_audio} Folie {i+1}/{num_slides} ({dur_str})")
    
    if not slide_videos:
        print("  ✗ Keine Folien-Videos erstellt!")
        return False
    
    # Write concat file
    with open(concat_file, "w") as f:
        for sv in slide_videos:
            f.write(f"file '{os.path.basename(sv)}'\n")
    
    # Concatenate all slide videos (copy, no re-encode → fast!)
    print(f"\n  Zusammenfuegen ({len(slide_videos)} Teile)...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_file,
        "-c", "copy",
        "-movflags", "+faststart",
        output_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    if result.returncode != 0:
        print(f"  ✗ Concat-Fehler: {result.stderr[-300:]}")
        return False
    
    # Get final video info
    size_mb = os.path.getsize(output_path) / 1024 / 1024
    dur_result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", output_path],
        capture_output=True, text=True
    )
    dur_min = float(dur_result.stdout.strip()) / 60 if dur_result.stdout.strip() else 0
    
    print(f"  ✓ {output_path} ({size_mb:.1f} MB, {dur_min:.1f} Minuten)")
    return True


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="FFGFT Video Generator")
    parser.add_argument("--only", choices=["narrativ", "presentation"],
                        help="Nur ein Video generieren")
    parser.add_argument("--lang", choices=["de", "en", "both"], default="de",
                        help="Sprache fuer Presentation (default: de)")
    parser.add_argument("--resolution", default=RESOLUTION,
                        help="Aufloesung WxH (default: 1920x1080)")
    parser.add_argument("--audio-dir", default="audio",
                        help="Ordner mit MP3-Dateien (default: audio)")
    parser.add_argument("--output-dir", default=".",
                        help="Ausgabe-Ordner (default: aktuelles Verzeichnis)")
    args = parser.parse_args()
    
    width, height = map(int, args.resolution.split("x"))
    
    print("=" * 60)
    print("FFGFT Video Generator")
    print(f"Aufloesung: {width}x{height}")
    print("=" * 60)
    
    check_prerequisites()
    
    # Check HTML files exist
    jobs = []
    
    if args.only != "presentation":
        if os.path.exists("narrativ.html"):
            jobs.append({
                "name": "FFGFT Narrativ (Deutsch)",
                "html": "narrativ.html",
                "slides": 18,
                "audio_prefix": "narrativ",
                "output": os.path.join(args.output_dir, "FFGFT_Narrativ_DE.mp4"),
                "lang": None,
            })
        else:
            print("⚠ narrativ.html nicht gefunden")
    
    if args.only != "narrativ":
        if os.path.exists("presentation.html"):
            if args.lang in ("de", "both"):
                jobs.append({
                    "name": "Buch-Praesentation (Deutsch)",
                    "html": "presentation.html",
                    "slides": 35,
                    "audio_prefix": "pres_de",
                    "output": os.path.join(args.output_dir, "T0_Presentation_DE.mp4"),
                    "lang": "de",
                })
            if args.lang in ("en", "both"):
                jobs.append({
                    "name": "Book Presentation (English)",
                    "html": "presentation.html",
                    "slides": 35,
                    "audio_prefix": "pres_en",
                    "output": os.path.join(args.output_dir, "T0_Presentation_EN.mp4"),
                    "lang": "en",
                })
        else:
            print("⚠ presentation.html nicht gefunden")
    
    if not jobs:
        print("Keine HTML-Dateien gefunden. Starte das Script im Ordner mit den HTML-Dateien.")
        sys.exit(1)
    
    # Check audio directory
    if not os.path.exists(args.audio_dir):
        print(f"\n⚠ Audio-Ordner '{args.audio_dir}' nicht gefunden!")
        print("  Videos werden ohne Audio erstellt (nur Bilder).")
        print("  Fuer Audio zuerst: python generate_audio.py")
    
    results = []
    
    for job in jobs:
        print(f"\n{'='*60}")
        print(f"📽  {job['name']}")
        print(f"{'='*60}")
        
        # Create temp directory for screenshots
        tmpdir = tempfile.mkdtemp(prefix="ffgft_video_")
        
        try:
            # Step 1: Capture screenshots
            print(f"\n  📸 Screenshots aufnehmen ({job['slides']} Folien)...")
            capture_slides(
                job["html"], job["slides"], tmpdir,
                width, height, job["lang"]
            )
            
            # Step 2: Create video
            print(f"\n  🎬 Video erstellen...")
            success = create_video(
                tmpdir, args.audio_dir, job["audio_prefix"],
                job["slides"], job["output"], width, height
            )
            
            results.append((job["name"], job["output"], success))
            
        finally:
            # Cleanup temp directory
            shutil.rmtree(tmpdir, ignore_errors=True)
    
    # Summary
    print(f"\n{'='*60}")
    print("ERGEBNIS")
    print(f"{'='*60}")
    for name, path, success in results:
        if success:
            size = os.path.getsize(path) / 1024 / 1024
            print(f"  ✓ {name}: {path} ({size:.1f} MB)")
        else:
            print(f"  ✗ {name}: FEHLER")
    
    print(f"\nFertig! Videos sind bereit zum Upload (z.B. YouTube).")


if __name__ == "__main__":
    main()
