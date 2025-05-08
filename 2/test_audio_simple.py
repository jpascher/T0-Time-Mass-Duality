from manim import *
from gtts import gTTS
import subprocess
from pathlib import Path

class AudioTest(Scene):
    def construct(self):
        # Simple visual
        text = Text("Testing Audio Narration", font_size=48)
        self.play(Write(text))
        self.wait(5)
        self.play(FadeOut(text))

# Create the scene
scene = AudioTest()
scene.render()

# Generate simple audio
narration = "Hello, this is a test of the audio narration system. If you can hear this, the audio is working correctly."
audio_path = Path("test_narration.mp3")

tts = gTTS(narration, lang='en')
tts.save(str(audio_path))

print(f"Audio file created: {audio_path}")
print(f"File size: {audio_path.stat().st_size} bytes")

# Find video
video_files = list(Path("./media/videos/").glob("**/AudioTest.mp4"))
if video_files:
    video_path = video_files[0]
    output_path = Path("test_with_audio.mp4")
    
    # Combine with ffmpeg
    cmd = [
        'ffmpeg', '-y',
        '-i', str(video_path),
        '-i', str(audio_path),
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-shortest',
        str(output_path)
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Combined video created: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error combining video and audio: {e}")
else:
    print("Video file not found")