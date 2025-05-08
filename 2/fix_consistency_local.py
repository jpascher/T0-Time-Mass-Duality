from manim import *
import numpy as np
from pathlib import Path
import subprocess
from gtts import gTTS

# Configuration
OUTPUT_PATH = Path("./media/videos/")
FINAL_PATH = Path("./final_videos/")
AUDIO_PATH = Path("./audio/")

# Create directories
FINAL_PATH.mkdir(exist_ok=True)
AUDIO_PATH.mkdir(exist_ok=True)

class T0ModelSimple(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scene_name = self.__class__.__name__
        self.narrations = []
    
    def add_narration(self, text, lang='en'):
        """Adds narration text"""
        self.narrations.append((text, lang))
    
    def clear_scene(self):
        """Removes all objects from the scene with animation"""
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def construct(self):
        # Part 1: Foundations and Philosophy
        self.show_title()
        self.philosophical_foundation()
        self.systematic_derivation()
        self.empirical_confirmation()
        
        # Part 2: Core Concepts
        self.time_mass_duality()
        self.energy_fundamental()
        self.natural_units_visual()
        
        # Part 3: Cosmological Implications
        self.galaxy_rotation_corrected()
        self.universe_evolution()
        
        # Part 4: Quantum Implications
        self.wave_function_demo()
        self.conclusion()
    
    def show_title(self):
        """Opening title sequence"""
        title = Text("T0 Model: Time-Mass Duality", font_size=48)
        subtitle = Text("A Revolutionary Perspective on Physics", font_size=32)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        self.add_narration(
            "The T0 Model presents a revolutionary perspective on physics through "
            "time-mass duality. This presentation explores its philosophical foundations, "
            "mathematical derivations, and profound implications for our understanding "
            "of the universe."
        )
        
        self.wait(5)
        self.clear_scene()
    
    def philosophical_foundation(self):
        """Philosophical foundations with animations"""
        title = Text("Mathematical Models and Physical Reality", font_size=36)
        self.play(Write(title))
        
        self.add_narration(
            "All physical theories are mathematical models that attempt to describe "
            "reality. They can at best approximate the ontological reality, "
            "but never fully capture it."
        )
        self.wait(6)
        
        self.play(FadeOut(title))
        
        # Animated model-reality relationship
        model_circle = Circle(radius=1.5, color=BLUE)
        reality_circle = Circle(radius=1.5, color=RED)
        model_circle.shift(LEFT * 3)
        reality_circle.shift(RIGHT * 3)
        
        model_text = Text("Mathematical\nModel", font_size=24).move_to(model_circle)
        reality_text = Text("Physical\nReality", font_size=24).move_to(reality_circle)
        
        self.play(Create(model_circle), Create(reality_circle))
        self.play(Write(model_text), Write(reality_text))
        
        # Animate approximation arrows
        arrows = VGroup()
        for i in range(5):
            angle = (i - 2) * PI/8
            start = model_circle.get_right() + UP * np.sin(angle) * 0.5
            end = reality_circle.get_left() + UP * np.sin(angle) * 0.5
            arrow = Arrow(start, end, color=YELLOW)
            arrows.add(arrow)
        
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.1))
        
        approximation_text = Text("Approximation", font_size=24, color=YELLOW)
        approximation_text.move_to((model_circle.get_center() + reality_circle.get_center()) / 2)
        approximation_text.shift(UP * 2)
        
        self.play(Write(approximation_text))
        
        self.add_narration(
            "The T0 model is not an entirely new theory, but a systematic extension "
            "of existing concepts that leads to a dual description of physical reality."
        )
        
        self.wait(6)
        self.clear_scene()
    
    def systematic_derivation(self):
        """Systematic derivation with proper animations"""
        title = Text("No Arbitrary Assumptions!", font_size=36, color=RED)
        self.play(Write(title))
        
        self.add_narration(
            "A crucial point: Setting constants to one is NOT arbitrary! "
            "Everything is systematically derived from first principles."
        )
        self.wait(6)
        
        self.play(FadeOut(title))
        
        # Derivation steps with proper spacing and positioning
        derivations = VGroup(
            Text("β_T = 1", font_size=28, color=YELLOW),
            Text("Follows from renormalization group", font_size=22),
            Text("Infrared fixed point of the theory", font_size=20, color=BLUE),
            Text(" ", font_size=10),  # Spacer
            Text("α_EM = 1", font_size=28, color=YELLOW),
            Text("Makes charge dimensionless", font_size=22),
            Text("Simplifies Maxwell equations", font_size=20, color=BLUE),
            Text(" ", font_size=10),  # Spacer
            Text("α_W = 1", font_size=28, color=YELLOW),
            Text("Connects temperature and frequency", font_size=22),
            Text("Wien's law becomes fundamental", font_size=20, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)  # Increased spacing
        
        # Position the group properly
        derivations.move_to(ORIGIN)
        
        # Create separate groups for each derivation
        beta_group = VGroup(derivations[0], derivations[1], derivations[2])
        alpha_em_group = VGroup(derivations[4], derivations[5], derivations[6]) 
        alpha_w_group = VGroup(derivations[8], derivations[9], derivations[10])
        
        # Position them properly
        beta_group.move_to(UP * 2)
        alpha_em_group.move_to(ORIGIN)
        alpha_w_group.move_to(DOWN * 2)
        
        # Animate each group
        self.play(FadeIn(beta_group))
        self.wait(3)
        self.play(beta_group.animate.shift(LEFT * 10))  # Move out of view
        
        self.play(FadeIn(alpha_em_group))
        self.wait(3)
        self.play(alpha_em_group.animate.shift(LEFT * 10))  # Move out of view
        
        self.play(FadeIn(alpha_w_group))
        self.wait(3)
        
        self.add_narration(
            "Beta-T equals one follows as an infrared fixed point from the "
            "renormalization group. Alpha-EM equals one makes electric charge "
            "dimensionless and simplifies Maxwell's equations. Alpha-W equals one "
            "connects temperature and frequency in a fundamental way."
        )
        
        self.wait(10)
        self.clear_scene()
    
    def empirical_confirmation(self):
        """Empirical confirmation with simple formatting"""
        title = Text("Empirical Confirmation", font_size=36)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
        # Create comparison table with better layout
        table_title = Text("Natural Units vs SI Measurements", font_size=28, color=BLUE)
        table_title.to_edge(UP)
        self.play(Write(table_title))
        
        # Create table with two columns
        nat_header = Text("Natural Unit", font_size=24, color=GREEN)
        si_header = Text("SI Value", font_size=24, color=YELLOW)
        
        nat_header.shift(LEFT * 3 + UP * 2)
        si_header.shift(RIGHT * 3 + UP * 2)
        
        self.play(Write(nat_header), Write(si_header))
        
        # Table entries using only Text
        entries = [
            ("c = 1", "299,792,458 m/s"),
            ("h = 1", "1.055 × 10^-34 Js"),
            ("G = 1", "6.674 × 10^-11 m³/kg·s²"),
            ("α_EM = 1", "1/137.036"),
            ("β_T = 1", "0.0080...")
        ]
        
        for i, (nat, si) in enumerate(entries):
            nat_text = Text(nat, font_size=24)
            si_text = Text(si, font_size=24)
            
            nat_text.shift(LEFT * 3 + UP * (1 - i * 0.7))
            si_text.shift(RIGHT * 3 + UP * (1 - i * 0.7))
            
            self.play(Write(nat_text), Write(si_text))
            self.wait(0.5)
        
        self.add_narration(
            "Strong evidence for the non-arbitrariness of natural units "
            "is their high degree of consistency with empirical SI measurements. "
            "The deviations are less than one in a million."
        )
        
        self.wait(8)
        self.clear_scene()
        
        # Fine structure constant highlight
        alpha_title = Text("The 'Magical' Fine Structure Constant", font_size=32, color=YELLOW)
        self.play(Write(alpha_title))
        self.wait(2)
        
        self.play(FadeOut(alpha_title))
        
        magic_explanation = VGroup(
            Text("Not coincidence, but consequence!", font_size=28, color=GREEN),
            Text("α_EM (natural) = 1", font_size=36),
            Text("↓", font_size=40),
            Text("α_EM (SI) = 1/137.036", font_size=36),
            Text("Precision: 9 decimal places!", font_size=24, color=BLUE)
        ).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(magic_explanation))
        
        self.add_narration(
            "The famous number one over 137, which Feynman called one of the greatest "
            "mysteries of physics, is not a coincidence. It follows exactly when we "
            "set the fine structure constant to one in natural units and then convert "
            "to SI units. The precision is nine decimal places!"
        )
        
        self.wait(12)
        self.clear_scene()
    
    def time_mass_duality(self):
        """Time-mass duality with proper animation"""
        title = Text("Time-Mass Duality", font_size=36)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=5,
            axis_config={"color": BLUE},
        )
        
        labels = axes.get_axis_labels(
            x_label=Text("Mass (m)", font_size=24),
            y_label=Text("Intrinsic Time T(x)", font_size=24)
        )
        
        # Create the curve T(x) = h/mc²
        def time_field(x):
            return 4 / (x + 0.1)  # Avoid division by zero
        
        curve = axes.plot(time_field, color=YELLOW, x_range=[0.1, 10])
        
        self.play(Create(axes), Write(labels))
        self.play(Create(curve))
        
        # Add formula
        formula = Text("T(x) = h/(mc²)", font_size=36)
        formula.to_edge(UP)
        self.play(Write(formula))
        
        # Animate a point moving along the curve
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(1, time_field(1)))
        
        # Create value displays
        mass_value = DecimalNumber(1, num_decimal_places=1)
        time_value = DecimalNumber(time_field(1), num_decimal_places=2)
        
        mass_text = Text("Mass: ", font_size=24)
        time_text = Text("Time: ", font_size=24)
        
        mass_display = VGroup(mass_text, mass_value).arrange(RIGHT)
        time_display = VGroup(time_text, time_value).arrange(RIGHT)
        
        display_group = VGroup(mass_display, time_display).arrange(DOWN)
        display_group.to_edge(RIGHT)
        
        self.play(Create(dot), FadeIn(display_group))
        
        # Animate the dot moving
        def update_values(mob):
            x_val = axes.p2c(dot.get_center())[0]
            if x_val > 0:  # Avoid division by zero
                mass_value.set_value(x_val)
                time_value.set_value(time_field(x_val))
        
        display_group.add_updater(update_values)
        
        self.play(dot.animate.move_to(axes.c2p(5, time_field(5))), run_time=3)
        self.play(dot.animate.move_to(axes.c2p(0.5, time_field(0.5))), run_time=3)
        
        self.add_narration(
            "In the T0 model, intrinsic time is inversely proportional to mass. "
            "As mass increases, the intrinsic time decreases. This relationship "
            "forms the foundation of time-mass duality."
        )
        
        self.wait(8)
        display_group.clear_updaters()
        self.clear_scene()
    
    def energy_fundamental(self):
        """Energy as fundamental quantity"""
        title = Text("Energy as the Only Fundamental Dimension", font_size=32)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
        # Dimension reduction visualization
        dims = VGroup(
            Text("Systematic Dimension Reduction:", font_size=28, color=GREEN),
            Text("", font_size=10),
            Text("Length = [E⁻¹]", font_size=24),
            Text("Time = [E⁻¹]", font_size=24),
            Text("Mass = [E]", font_size=24),
            Text("Temperature = [E]", font_size=24),
            Text("Charge = [1] (dimensionless)", font_size=24),
            Text("Intrinsic Time T(x) = [E⁻¹]", font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        
        self.play(FadeIn(dims[0]))
        self.wait(1)
        
        for dim in dims[2:]:
            self.play(FadeIn(dim))
            self.wait(0.5)
        
        self.add_narration(
            "The reduction to energy as the only dimension is not arbitrary, "
            "but follows systematically from unification. Length and time "
            "both have dimension E to the minus one, mass and temperature "
            "have dimension E, and electric charge becomes dimensionless."
        )
        
        self.wait(10)
        self.clear_scene()
    
    def natural_units_visual(self):
        """Natural units visualization"""
        title = Text("Natural Units System", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create animated circles for constants - using Text
        constants = ["c", "h", "G", "k_B", "α_EM", "β_T"]
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        
        circles = VGroup()
        for i, (const, color) in enumerate(zip(constants, colors)):
            circle = Circle(radius=0.5, color=color)
            # Arrange in a 2x3 grid
            row = i // 3
            col = i % 3
            circle.shift(RIGHT * (col - 1) * 2.5 + UP * (0.5 - row) * 2)
            text = Text(const, color=color, font_size=36)
            text.move_to(circle)
            circles.add(VGroup(circle, text))
        
        self.play(LaggedStart(*[Create(c[0]) for c in circles], lag_ratio=0.1))
        self.play(LaggedStart(*[Write(c[1]) for c in circles], lag_ratio=0.1))
        
        # Animate them all becoming 1
        equals_one = VGroup()
        for circle_group in circles:
            eq = Text("= 1", color=circle_group[0].get_color(), font_size=28)
            eq.next_to(circle_group, DOWN)
            equals_one.add(eq)
        
        self.play(LaggedStart(*[Write(eq) for eq in equals_one], lag_ratio=0.1))
        
        self.add_narration(
            "In the natural units system, all fundamental constants are set to one. "
            "This isn't arbitrary - it reveals the underlying unity of physical laws."
        )
        
        self.wait(6)
        self.clear_scene()
    
    def galaxy_rotation_corrected(self):
        """Corrected galaxy rotation curve visualization"""
        title = Text("Galaxy Rotation Curves", font_size=36)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
        axes = Axes(
            x_range=[0, 30, 5],
            y_range=[0, 300, 50],
            x_length=8,
            y_length=5,
            axis_config={"color": BLUE},
        )
        
        labels = axes.get_axis_labels(
            x_label=Text("Radius (kpc)", font_size=24),
            y_label=Text("Velocity (km/s)", font_size=24)
        )
        
        self.play(Create(axes), Write(labels))
        
        # Observed data points (actual measurements)
        data_x = [1, 3, 5, 10, 15, 20, 25]
        data_y = [180, 215, 220, 225, 223, 220, 218]
        
        data_points = VGroup(*[
            Dot(axes.c2p(x, y), color=GREEN)
            for x, y in zip(data_x, data_y)
        ])
        
        self.play(Create(data_points))
        
        observed_label = Text("Observed Data", color=GREEN, font_size=24)
        observed_label.next_to(axes.c2p(15, 240), UP)
        self.play(Write(observed_label))
        
        # Newtonian prediction (declining curve)
        def newtonian(r):
            if r < 0.1:
                return 0
            return 220 * np.sqrt(1/r)
        
        newtonian_curve = axes.plot(
            newtonian, 
            color=BLUE, 
            x_range=[1, 30],
        )
        newtonian_label = Text("Newtonian", color=BLUE, font_size=24)
        newtonian_label.next_to(axes.c2p(20, newtonian(20)), DOWN)
        
        self.play(Create(newtonian_curve), Write(newtonian_label))
        
        # T0 model prediction (matches observed data)
        def t0_model(r):
            # Simplified for visualization - matches observed flat curve
            return 220 - 2 * np.exp(-r/10)
        
        t0_curve = axes.plot(
            t0_model, 
            color=RED, 
            x_range=[1, 30],
        )
        t0_label = Text("T0 Model", color=RED, font_size=24)
        t0_label.next_to(axes.c2p(10, t0_model(10)), UP)
        
        self.play(Create(t0_curve), Write(t0_label))
        
        self.add_narration(
            "Galaxy rotation curves show a major discrepancy with Newtonian predictions. "
            "The observed data shows a flat rotation curve, while Newtonian mechanics "
            "predicts a declining curve. The T0 model explains this without dark matter "
            "through its modified gravitational potential, matching the observed data."
        )
        
        self.wait(10)
        self.clear_scene()
    
    def universe_evolution(self):
        """Universe evolution comparison"""
        standard_title = Text("Standard Model", font_size=32)
        t0_title = Text("T0 Model", font_size=32)
        
        standard_title.shift(LEFT * 3 + UP * 3)
        t0_title.shift(RIGHT * 3 + UP * 3)
        
        self.play(Write(standard_title), Write(t0_title))
        
        # Standard model - expanding universe
        standard_dots = VGroup()
        for i in range(-2, 3):
            for j in range(-2, 3):
                dot = Dot(color=YELLOW, radius=0.08)
                dot.move_to(LEFT * 3 + RIGHT * i * 0.3 + UP * j * 0.3)
                standard_dots.add(dot)
        
        self.play(Create(standard_dots))
        
        # Animate expansion
        self.play(
            *[dot.animate.shift((dot.get_center() - LEFT * 3) * 0.5) 
              for dot in standard_dots],
            run_time=2
        )
        
        standard_text = Text("Expanding Universe", font_size=24)
        standard_text.next_to(standard_dots, DOWN)
        self.play(Write(standard_text))
        
        # T0 model - static universe with energy transfer
        t0_dots = VGroup()
        for i in range(-2, 3):
            for j in range(-2, 3):
                dot = Dot(color=YELLOW, radius=0.08)
                dot.move_to(RIGHT * 3 + RIGHT * i * 0.3 + UP * j * 0.3)
                t0_dots.add(dot)
        
        self.play(Create(t0_dots))
        
        # Animate energy transfer (color change)
        self.play(
            *[dot.animate.set_color(RED) for dot in t0_dots[::2]],
            run_time=1
        )
        self.play(
            *[dot.animate.set_color(YELLOW) for dot in t0_dots[::2]],
            *[dot.animate.set_color(RED) for dot in t0_dots[1::2]],
            run_time=1
        )
        self.play(
            *[dot.animate.set_color(YELLOW) for dot in t0_dots[1::2]],
            run_time=1
        )
        
        t0_text = Text("Static Universe\nwith Energy Transfer", font_size=24)
        t0_text.next_to(t0_dots, DOWN)
        self.play(Write(t0_text))
        
        self.add_narration(
            "While the standard model describes an expanding universe, "
            "the T0 model proposes a static universe where redshift "
            "results from energy transfer through the intrinsic time field."
        )
        
        self.wait(8)
        self.clear_scene()
    
    def wave_function_demo(self):
        """Wave function evolution demonstration"""
        title = Text("Modified Schrödinger Equation", font_size=36)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE},
        )
        
        # Use Text instead of MathTex for equations
        standard_eq = Text("ih∂Ψ/∂t = HΨ", font_size=32)
        standard_eq.to_edge(UP).shift(LEFT * 3)
        
        t0_eq = Text("ihT(x)∂Ψ/∂t = HΨ", font_size=32)
        t0_eq.to_edge(UP).shift(RIGHT * 3)
        
        self.play(Create(axes))
        self.play(Write(standard_eq), Write(t0_eq))
        
        # Wave function animations
        time_tracker = ValueTracker(0)
        
        def wave_standard(x, t):
            return np.exp(-x**2) * np.cos(2 * x - t)
        
        def wave_t0(x, t):
            # Modified by T(x) field
            return np.exp(-x**2) * np.cos(2 * x - t * (1 + 0.2 * x**2))
        
        standard_wave = always_redraw(lambda: axes.plot(
            lambda x: wave_standard(x, time_tracker.get_value()),
            color=BLUE
        ))
        
        t0_wave = always_redraw(lambda: axes.plot(
            lambda x: wave_t0(x, time_tracker.get_value()),
            color=RED
        ))
        
        standard_label = Text("Standard", color=BLUE, font_size=24).shift(LEFT * 3 + DOWN * 2.5)
        t0_label = Text("T0 Model", color=RED, font_size=24).shift(RIGHT * 3 + DOWN * 2.5)
        
        self.play(Create(standard_wave), Create(t0_wave))
        self.play(Write(standard_label), Write(t0_label))
        
        # Animate wave evolution
        self.play(time_tracker.animate.set_value(10), run_time=5)
        
        self.add_narration(
            "The T0 model modifies the Schrödinger equation to include "
            "the intrinsic time field. This leads to different wave function "
            "evolution, particularly for massive particles, introducing "
            "position-dependent time evolution rates."
        )
        
        self.wait(8)
        self.clear_scene()
    
    def conclusion(self):
        """Conclusion and summary"""
        title = Text("T0 Model: Key Insights", font_size=36)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))
        
        summary = VGroup(
            Text("1. Systematic derivation from first principles", font_size=24),
            Text("2. No arbitrary assumptions", font_size=24),
            Text("3. Natural units reveal fundamental unity", font_size=24),
            Text("4. Time-mass duality explains dark matter", font_size=24),
            Text("5. Static universe with energy transfer", font_size=24),
            Text("6. Modified quantum mechanics", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        for point in summary:
            self.play(FadeIn(point))
            self.wait(1)
        
        self.add_narration(
            "The T0 model provides a revolutionary perspective on physics through "
            "systematic derivation from first principles. It explains dark matter, "
            "redshift, and quantum phenomena through time-mass duality, all without "
            "arbitrary assumptions or ad-hoc parameters."
        )
        
        self.wait(10)
        self.clear_scene()
        
        final_text = Text(
            "T0 Model: A New Understanding of Reality",
            font_size=42,
            color=GOLD
        )
        
        self.play(Write(final_text))
        self.wait(5)
        self.play(FadeOut(final_text))
    
    def generate_audio(self):
        """Generates audio files for narration"""
        if not self.narrations:
            print("No narrations to generate audio for!")
            return None
            
        combined_text = " ... ".join([text for text, lang in self.narrations])
        print(f"Generating audio for {len(self.narrations)} narration segments")
        print(f"Total text length: {len(combined_text)} characters")
        
        audio_file = AUDIO_PATH / f"{self.scene_name}.mp3"
        
        try:
            tts = gTTS(combined_text, lang='en', slow=False)
            tts.save(str(audio_file))
            print(f"Audio saved to: {audio_file}")
            print(f"Audio file size: {audio_file.stat().st_size} bytes")
            return audio_file
        except Exception as e:
            print(f"Error generating audio: {e}")
            return None
    
    def combine_video_audio(self, video_path, audio_path):
        """Combines video and audio into final file"""
        output_path = FINAL_PATH / f"{self.scene_name}_with_audio.mp4"
        
        # First check if audio file exists and has content
        if not audio_path.exists():
            print(f"Audio file not found: {audio_path}")
            return None
            
        audio_size = audio_path.stat().st_size
        print(f"Audio file size: {audio_size} bytes")
        
        if audio_size == 0:
            print("Audio file is empty!")
            return None
        
        # FFmpeg command with better error handling
        cmd = [
            'ffmpeg', '-y',
            '-i', str(video_path),
            '-i', str(audio_path),
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-map', '0:v:0',
            '-map', '1:a:0',
            '-shortest',
            str(output_path)
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Final video created: {output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg error: {e}")
            print(f"FFmpeg stdout: {e.stdout}")
            print(f"FFmpeg stderr: {e.stderr}")
            return None

# Main execution
if __name__ == "__main__":
    # Create video
    scene = T0ModelSimple()
    scene.render()
    
    # Generate audio
    audio_file = scene.generate_audio()
    
    if audio_file and audio_file.exists():
        print(f"Audio file created successfully: {audio_file}")
        
        # Find rendered video path
        video_path = OUTPUT_PATH / "1080p60" / f"T0ModelSimple.mp4"
        
        if not video_path.exists():
            print(f"Video not found at: {video_path}")
            print("Searching for alternative paths...")
            video_files = list(OUTPUT_PATH.glob("**/T0ModelSimple.mp4"))
            if video_files:
                video_path = video_files[0]
                print(f"Found video at: {video_path}")
        
        if video_path.exists():
            final_video = scene.combine_video_audio(video_path, audio_file)
            if final_video:
                print(f"Video successfully created with audio: {final_video}")
            else:
                print("Failed to combine video and audio")
        else:
            print("Could not find the rendered video file")
    else:
        print("Failed to generate audio file")