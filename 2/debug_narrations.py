from manim import *
from pathlib import Path
from gtts import gTTS

class DebugNarrations(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.narrations = []
    
    def add_narration(self, text, lang='en'):
        """Adds narration text"""
        self.narrations.append((text, lang))
        print(f"Added narration: {text[:50]}...")
    
    def construct(self):
        title = Text("Debug Test", font_size=48)
        self.play(Write(title))
        
        self.add_narration("This is the first narration segment for testing.")
        self.wait(2)
        
        self.play(FadeOut(title))
        
        text2 = Text("Second Scene", font_size=48)
        self.play(Write(text2))
        
        self.add_narration("This is the second narration segment to verify audio generation.")
        self.wait(2)
        
        self.play(FadeOut(text2))
    
    def generate_audio(self):
        """Generates audio files for narration"""
        print(f"\nGenerating audio from {len(self.narrations)} narration segments")
        
        if not self.narrations:
            print("No narrations found!")
            return None
        
        combined_text = " ... ".join([text for text, lang in self.narrations])
        print(f"Combined text: {combined_text}")
        print(f"Total length: {len(combined_text)} characters")
        
        audio_file = Path("debug_audio.mp3")
        
        try:
            tts = gTTS(combined_text, lang='en')
            tts.save(str(audio_file))
            print(f"Audio saved to: {audio_file}")
            print(f"Audio file size: {audio_file.stat().st_size} bytes")
            return audio_file
        except Exception as e:
            print(f"Error generating audio: {e}")
            return None

# Test it
scene = DebugNarrations()
scene.render()
audio_file = scene.generate_audio()

if audio_file and audio_file.exists():
    print(f"\nSuccess! Audio file created: {audio_file}")
else:
    print("\nFailed to create audio file")