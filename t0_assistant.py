# t0_assistant.py - Speichere diesen Code in der Datei
import json
from datetime import datetime

class T0ResearchAssistant:
    def __init__(self):
        self.knowledge_base = self.load_knowledge()
        self.conversation_history = []
        
    def load_knowledge(self):
        try:
            with open('t0_knowledge_base.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"core_concepts": [], "writing_style": []}
    
    def generate_response(self, user_input):
        question_lower = user_input.lower()
        
        if "xi" in question_lower or "ξ" in question_lower:
            return """Der ξ-Parameter ist eine fundamentale geometrische Konstante mit dem Wert ξ = 4/3 × 10⁻⁴. 
Er leitet sich aus der tetraedrischen Packungsgeometrie ab und beschreibt die fundamentale Kopplung 
zwischen geometrischer Struktur und dynamischer Entwicklung in der T0-Theorie."""
            
        elif "mass" in question_lower or "massen" in question_lower:
            return """Die Massenhierarchie der Leptonen folgt der exponentiellen Beziehung m_i = m_0 · e^(ξ·n_i). 
Mit den Quantenzahlen n_e = -14998, n_μ = -7499, n_τ = 0 ergibt sich eine präzise Beschreibung 
der experimentell gemessenen Massenverhältnisse."""
            
        elif "fractal" in question_lower or "fraktal" in question_lower:
            return """Die fraktale Raumzeit-Dimension D_f = 2.94 ergibt sich aus der fundamentalen geometrischen 
Struktur. Bei hohen Energien wird die fraktale Natur der Raumzeit sichtbar, was das Renormierungsverhalten 
in Quantenfeldtheorien erklärt."""
            
        elif "euler" in question_lower or "e" in question_lower:
            return """Die Eulersche Zahl e dient als natürlicher Operator in der T0-Theorie. Sie übersetzt die 
diskrete geometrische Struktur in kontinuierliche dynamische Entwicklung. Die Beziehung e^(ξ·n) 
beschreibt fundamentale exponentielle Skalierungen."""
            
        else:
            return """Ihre Frage zur T0-Theorie wird analysiert. Die T0-Theorie basiert auf tiefen geometrischen 
Prinzipien und beschreibt fundamentale physikalische Zusammenhänge durch den ξ-Parameter und 
exponentielle Beziehungen der Form e^(ξ·n). Könnten Sie Ihre Frage präzisieren?"""