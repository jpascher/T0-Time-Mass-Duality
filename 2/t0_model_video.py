from manim import *
import os
import subprocess
from pathlib import Path
from gtts import gTTS
import tempfile
import numpy as np

# Konfiguration
OUTPUT_PATH = Path("./media/videos/")
FINAL_PATH = Path("./final_videos/")
AUDIO_PATH = Path("./audio/")

# Verzeichnisse erstellen
FINAL_PATH.mkdir(exist_ok=True)
AUDIO_PATH.mkdir(exist_ok=True)

class T0ModelComplete(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scene_name = "t0_model_complete"
        self.narrations = []
        
    def add_narration(self, text, lang='de'):
        """Fügt einen Narrationtext hinzu"""
        self.narrations.append((text, lang))
    
    def construct(self):
        # Szene 1: Einführung
        self.create_introduction()
        
        # Szene 2: Intrinsisches Zeitfeld
        self.create_time_field_scene()
        
        # Szene 3: Vergleich der Modelle
        self.create_model_comparison()
        
        # Szene 4: Emergente Gravitation
        self.create_emergent_gravity()
        
        # Szene 5: Vorhersagen
        self.create_predictions()
        
    def create_introduction(self):
        """Erstellt die Einführungsszene"""
        title = Text("Das T0-Modell der Zeit-Masse-Dualität", font_size=40)
        self.play(Write(title))
        
        self.add_narration(
            "Willkommen zur Präsentation des T0-Modells der Zeit-Masse-Dualität. "
            "Dieses revolutionäre physikalische Modell stellt unsere fundamentalen "
            "Annahmen über Zeit und Masse in Frage."
        )
        self.wait(5)
        
        self.play(title.animate.to_edge(UP))
        
        subtitle = Text(
            "Eine alternative Sicht auf Raum, Zeit und Materie",
            font_size=30,
            color=BLUE
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(subtitle))
        
        self.add_narration(
            "Im Gegensatz zum Standardmodell der Physik, das von relativer Zeit "
            "und konstanter Masse ausgeht, postuliert das T0-Modell absolute Zeit "
            "und variable Masse."
        )
        self.wait(6)
        
        self.play(FadeOut(subtitle))
        
    def create_time_field_scene(self):
        """Erstellt die Szene für das intrinsische Zeitfeld"""
        # Titel
        section_title = Text("Das Intrinsische Zeitfeld", font_size=36, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))
        
        # Hauptgleichung
        time_field_eq = MathTex(
            r"T(x) = \frac{\hbar}{\max(mc^2, \omega)}",
            font_size=48
        )
        
        self.play(Write(time_field_eq))
        
        self.add_narration(
            "Das Herzstück des T0-Modells ist das intrinsische Zeitfeld T von x. "
            "Es ist definiert als h-quer geteilt durch das Maximum von Masse mal c-Quadrat "
            "oder der Photonenenergie Omega."
        )
        self.wait(6)
        
        # Erklärung der Komponenten
        self.play(time_field_eq.animate.shift(UP*2))
        
        explanation = VGroup(
            Text("Für massive Teilchen:", font_size=25),
            MathTex(r"T(x) = \frac{\hbar}{mc^2}", font_size=36),
            Text("Für Photonen:", font_size=25),
            MathTex(r"T(x) = \frac{\hbar}{\omega}", font_size=36)
        ).arrange(DOWN, center=True, buff=0.5)
        
        self.play(FadeIn(explanation, shift=UP))
        
        self.add_narration(
            "Für massive Teilchen reduziert sich diese Formel zu h-quer geteilt durch "
            "Masse mal c-Quadrat. Für Photonen ist es h-quer geteilt durch die "
            "Frequenz Omega."
        )
        self.wait(6)
        
        self.play(FadeOut(explanation), FadeOut(time_field_eq))
        
    def create_model_comparison(self):
        """Erstellt den Vergleich zwischen Standardmodell und T0-Modell"""
        # Titel
        comparison_title = Text("Modellvergleich", font_size=36, color=GREEN)
        self.play(Write(comparison_title))
        self.wait(1)
        self.play(comparison_title.animate.to_edge(UP))
        
        # Tabelle
        table = VGroup(
            Text("Standardmodell", font_size=28, color=BLUE).to_edge(LEFT, buff=2),
            Text("T0-Modell", font_size=28, color=RED).to_edge(RIGHT, buff=2)
        )
        
        divider = Line(UP*2, DOWN*2, color=WHITE).move_to(ORIGIN)
        
        self.play(Write(table), Create(divider))
        
        # Eigenschaften
        properties_left = VGroup(
            Text("• Relative Zeit", font_size=24),
            Text("• Konstante Masse", font_size=24),
            Text("• Expandierendes Universum", font_size=24),
            Text("• Dunkle Energie erforderlich", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(table[0], DOWN, buff=0.8)
        
        properties_right = VGroup(
            Text("• Absolute Zeit", font_size=24),
            Text("• Variable Masse", font_size=24),
            Text("• Statisches Universum", font_size=24),
            Text("• Keine Dunkle Energie", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(table[1], DOWN, buff=0.8)
        
        self.play(Write(properties_left), Write(properties_right))
        
        self.add_narration(
            "Hier sehen wir die fundamentalen Unterschiede zwischen den Modellen. "
            "Das Standardmodell verwendet relative Zeit und konstante Masse, "
            "während das T0-Modell absolute Zeit und variable Masse annimmt. "
            "Dies hat tiefgreifende Konsequenzen für unser Verständnis des Universums."
        )
        self.wait(8)
        
        self.play(FadeOut(VGroup(table, divider, properties_left, properties_right)))
        
    def create_emergent_gravity(self):
        """Erstellt die Szene für emergente Gravitation"""
        # Titel
        gravity_title = Text("Emergente Gravitation", font_size=36, color=ORANGE)
        self.play(Write(gravity_title))
        self.wait(1)
        self.play(gravity_title.animate.to_edge(UP))
        
        # Gravitationspotential
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True},
        )
        axes_labels = axes.get_axis_labels(
            x_label="r",
            y_label="\Phi(r)"
        )
        
        self.play(Create(axes), Write(axes_labels))
        
        # Newton'sches Potential
        newton_curve = axes.plot(
            lambda x: -2/x if x > 0.5 else -4,
            x_range=[0.5, 10],
            color=BLUE
        )
        newton_label = Text("Newton: Φ(r) = -GM/r", font_size=20, color=BLUE).to_corner(UL)
        
        self.play(Create(newton_curve), Write(newton_label))
        
        # T0-Modell Potential
        kappa = 0.1
        t0_curve = axes.plot(
            lambda x: -2/x + kappa*x if x > 0.5 else -4,
            x_range=[0.5, 10],
            color=RED
        )
        t0_label = Text("T0: Φ(r) = -GM/r + κr", font_size=20, color=RED).next_to(newton_label, DOWN)
        
        self.play(Create(t0_curve), Write(t0_label))
        
        self.add_narration(
            "Im T0-Modell emergiert Gravitation aus dem intrinsischen Zeitfeld. "
            "Das Gravitationspotential enthält einen zusätzlichen linearen Term κr, "
            "der flache Galaxien-Rotationskurven ohne Dunkle Materie erklärt."
        )
        self.wait(8)
        
        self.play(FadeOut(VGroup(axes, axes_labels, newton_curve, t0_curve, newton_label, t0_label)))
        
    def create_predictions(self):
        """Erstellt die Szene für experimentelle Vorhersagen"""
        # Titel
        predictions_title = Text("Experimentelle Vorhersagen", font_size=36, color=PURPLE)
        self.play(Write(predictions_title))
        self.wait(1)
        self.play(predictions_title.animate.to_edge(UP))
        
        # Vorhersagen
        predictions = VGroup(
            Text("1. Wellenlängenabhängige Rotverschiebung", font_size=28),
            MathTex(r"z(\lambda) = z_0 \left(1 + \ln\left(\frac{\lambda}{\lambda_0}\right)\right)", font_size=32),
            Text("2. CMB-Temperatur bei z=1100", font_size=28),
            MathTex(r"T_{CMB} \approx 24,000\text{ K}", font_size=32),
            Text("3. Flache Galaxien-Rotationskurven", font_size=28),
            MathTex(r"v(r) = \sqrt{\frac{GM}{r} + \kappa r}", font_size=32)
        ).arrange(DOWN, buff=0.5)
        
        for i, item in enumerate(predictions):
            if i % 2 == 0:  # Textzeilen
                item.set_color(WHITE)
            else:  # Gleichungen
                item.set_color(YELLOW)
        
        self.play(FadeIn(predictions, shift=UP))
        
        self.add_narration(
            "Das T0-Modell macht konkrete, testbare Vorhersagen. "
            "Erstens: Eine wellenlängenabhängige Rotverschiebung mit etwa 2,3 Prozent "
            "Variation pro Dekade. Zweitens: Die CMB-Temperatur zur Rekombinationszeit "
            "wäre etwa 24.000 Kelvin, nicht 3.000 Kelvin wie im Standardmodell. "
            "Drittens: Galaxien-Rotationskurven werden ohne Dunkle Materie erklärt."
        )
        self.wait(12)
        
        # Abschluss
        self.play(FadeOut(predictions))
        
        conclusion = Text(
            "Das T0-Modell: Eine neue Perspektive auf das Universum",
            font_size=36,
            color=GOLD
        )
        self.play(Write(conclusion))
        self.wait(3)
        
        self.add_narration(
            "Das T0-Modell bietet eine völlig neue Perspektive auf fundamentale "
            "physikalische Phänomene und könnte unser Verständnis des Universums "
            "revolutionieren."
        )
        self.wait(5)
        
        self.play(FadeOut(conclusion))
    
    def generate_audio(self):
        """Generiert die Audiodateien für die Narration"""
        combined_text = " ".join([text for text, lang in self.narrations])
        audio_file = AUDIO_PATH / f"{self.scene_name}.mp3"
        
        tts = gTTS(combined_text, lang='de')
        tts.save(str(audio_file))
        
        return audio_file
    
    def combine_video_audio(self, video_path, audio_path):
        """Kombiniert Video und Audio zu einer finalen Datei"""
        output_path = FINAL_PATH / f"{self.scene_name}_final.mp4"
        
        # FFmpeg-Befehl
        cmd = [
            'ffmpeg', '-y',
            '-i', str(video_path),
            '-i', str(audio_path),
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-map', '0:v:0',
            '-map', '1:a:0',
            '-shortest',  # Stoppt, wenn die kürzere Spur (Video oder Audio) endet
            str(output_path)
        ]
        
        subprocess.run(cmd, check=True)
        print(f"Finales Video erstellt: {output_path}")
        return output_path

# Hauptausführung
if __name__ == "__main__":
    # Video erstellen
    scene = T0ModelComplete()
    scene.render()
    
    # Audio generieren
    audio_file = scene.generate_audio()
    
    # Pfad zum gerenderten Video finden
    video_path = OUTPUT_PATH / "1080p60" / f"{scene.scene_name}.mp4"
    
    # Video und Audio kombinieren
    if video_path.exists():
        final_video = scene.combine_video_audio(video_path, audio_file)
        print(f"Video erfolgreich erstellt: {final_video}")
    else:
        print(f"Video nicht gefunden: {video_path}")