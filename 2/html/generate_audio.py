#!/usr/bin/env python3
"""
Generate MP3 audio for FFGFT presentations.
Engines: gTTS (Google), edge-tts (Microsoft Neural), pyttsx3 (offline)

  pip install gTTS
  python generate_audio.py
"""
import os, sys, time, argparse, io
OUTPUT_DIR = "audio"

def generate_gtts(text, lang, path):
    from gtts import gTTS
    gTTS(text=text, lang=lang, slow=False).save(path)

def generate_edge(text, lang, path):
    import asyncio, edge_tts
    v = "de-DE-ConradNeural" if lang == "de" else "en-US-GuyNeural"
    async def run():
        await edge_tts.Communicate(text, v).save(path)
    asyncio.run(run())

def generate_pyttsx3(text, lang, path):
    import pyttsx3
    e = pyttsx3.init()
    for v in e.getProperty('voices'):
        t = 'german' if lang == 'de' else 'english'
        if t in v.name.lower(): e.setProperty('voice', v.id); break
    e.setProperty('rate', 160); e.save_to_file(text, path); e.runAndWait()

def detect_engine(preferred=None):
    order = [preferred] if preferred else ['edge', 'gtts', 'pyttsx3']
    for eng in order:
        try:
            if eng == 'edge':
                import edge_tts, asyncio
                async def test():
                    async for _ in edge_tts.Communicate("Test.", "de-DE-ConradNeural").stream(): return True
                asyncio.run(test()); print(f"  OK: edge-tts"); return 'edge'
            elif eng == 'gtts':
                from gtts import gTTS; buf = io.BytesIO(); gTTS("Test", lang="de").write_to_fp(buf)
                if buf.tell() > 0: print(f"  OK: gTTS"); return 'gtts'
            elif eng == 'pyttsx3':
                import pyttsx3; pyttsx3.init().stop(); print(f"  OK: pyttsx3"); return 'pyttsx3'
        except Exception as e:
            print(f"  X: {eng}: {e}")
    return None

def gen1(text, lang, path, engine, retries=2):
    fn = {'edge': generate_edge, 'gtts': generate_gtts, 'pyttsx3': generate_pyttsx3}[engine]
    for a in range(retries + 1):
        try:
            fn(text, lang, path); return os.path.getsize(path) / 1024
        except Exception as e:
            if a < retries: time.sleep(2 ** a); print(f"    retry...")
            else: print(f"    FEHLER: {e}"); return 0

# ================================================================
# NARRATIV: 18 Folien (Deutsch) - STIMMT BEREITS
# ================================================================
NARRATIV = [
"Das fundamentale fraktalgeometrische Feld. Eine neue Sicht auf die Wirklichkeit. Das Universum als sich vertiefendes Gehirn, beschrieben durch einen einzigen Parameter: Xi gleich vier Drittel mal zehn hoch minus vier. Von Johann Pascher.",
"Kapitel 1: Eine einzige Zahl beschreibt das Universum. Diese Zahl lautet Xi gleich vier Drittel mal zehn hoch minus vier. Dimensionslos, eine reine Zahl ohne Einheit. Aus dieser winzigen Zahl erwachsen alle fundamentalen Eigenschaften unseres Universums. Die fraktale Dimension der Raumzeit betraegt nicht exakt drei, sondern ungefaehr 2,999867. Dieser winzige Unterschied reguliert alle Divergenzen der Quantenfeldtheorie und verhindert Singularitaeten.",
"Das Universum als wachsendes Gehirn. Waehrend ein Embryo heranwaechst, vergroessert sich das Gehirn nicht durch Expansion, sondern durch Zunahme seiner Windungen. Mehr Windungen bedeuten mehr Oberflaeche, mehr Komplexitaet. Aehnlich verhaelt es sich mit dem Universum: Die Raumzeit bleibt statisch, aber ihre fraktale Komplexitaet nimmt zu. Der Raum dehnt sich nicht aus. Die fraktale Struktur entfaltet sich und wird komplexer.",
"Kapitel 2: Warum die Raumzeit fraktal sein muss. Auf einer glatten Raumzeit erhalten wir unendliche Werte. In der Naehe von Schwarzen Loechern divergiert die Kruemmung. Die FFGFT loest beide Probleme. Bei einem perfekt glatten Raum waere die Dimension exakt drei, wie ein Gehirn ohne Windungen. Erst die fraktale Koernigkeit macht das Universum lebendig.",
"Zeit-Masse-Dualitaet: Zwei Seiten einer Medaille. T mal m gleich eins. In Regionen hoher Massendichte vergeht die Zeit langsamer. Wo weniger Masse ist, laeuft die Zeit schneller. Das Produkt bleibt konstant. Diese Dualitaet folgt zwingend aus der fraktalen Selbstaehnlichkeit.",
"Kapitel 3: Drei Probleme der Allgemeinen Relativitaetstheorie. Erstens: Singularitaeten. Die FFGFT haelt die Kruemmung endlich. Zweitens: Dunkle Materie und Dunkle Energie sind fraktale Effekte. Drittens: Quanteninkompatibilitaet. Die FFGFT ist ultraviolett finit.",
"Kapitel 4: Schwarze Loecher. Tiefe Falten, keine Risse. Die fraktale Dimension wird am Horizont zweidimensional, eine fraktale Membran. Es gibt keinen Riss, keine Singularitaet. Die Hawking-Strahlung entsteht durch Schwingungen der Membran. Information bleibt erhalten.",
"Kapitel 5: Bewegung als emergente Eigenschaft. Die Lichtgeschwindigkeit emergiert aus der fraktalen Hierarchie. Masse ist gespeicherte Zeit, Energie ist Zeit in Bewegung. Bei extrem hohen Energien sollten Abweichungen von der Lorentz-Invarianz auftreten.",
"Kapitel 6: Dunkle Energie als Stoffwechsel des kosmischen Gehirns. Die Diskrepanz von 120 Groessenordnungen wird parameterfrei geloest. Die Vakuumenergiedichte ist Xi-Quadrat mal die kritische Dichte, ungefaehr null Komma sieben. Ohne Feinabstimmung. Es gibt keine echte Expansion.",
"Kapitel 7: Das Universum wird entscheiden. Testbare Vorhersagen: Schwarzer-Loch-Schatten mit Abweichung. Gravitationswellen-Ringdown. Fraktale CMB-Muster. Zeitvariation fundamentaler Konstanten. Unsere Messgeraete sind selbst Teil des fraktalen Vakuums.",
"Kapitel 8: Emergenz statt Quantisierung. Quantenphaenomene emergieren aus der fraktalen Struktur. Die Unschaerferelation erhaelt eine logarithmische Korrektur. Gravitation ist eine emergente Phasenverschiebung des Vakuumfeldes. Quantengravitation ist bereits eingebaut.",
"Kapitel 9: Alle Kraefte aus einem Parameter. Die vier Kraefte sind verschiedene Melodien aus demselben Instrument. Xi ist die Saitenspannung. Die Feinstrukturkonstante, die Gravitationskonstante, die QCD-Skala und die Vakuumenergie, alles parameterfrei aus Xi.",
"Kapitel 10: Warum Neutrinos so leicht und Quarks so schwer sind. Teilchen sind fraktale Resonanzmoden. Die Masse skaliert mit Xi hoch n. Die drei Generationen sind fraktale Hierarchiestufen.",
"Kapitel 11: Kosmologie ohne Inflation. Fraktale Phasenkohaerenz loest das Horizontproblem. Die Abweichung von Flachheit ist Xi-Quadrat. Der spektrale Index stimmt exakt mit Planck-Daten ueberein.",
"Kapitel 12: Der Big Bang. Kein Knall, sondern ein Erwachen. Ein Phasenuebergang, in dem das kosmische Gehirn zu denken begann. Aus stiller Potentialitaet wird strukturierte Realitaet.",
"Expansion ohne Bewegung. Die Rotverschiebung entsteht durch Aenderung der fraktalen Skalenstruktur. Die Hubble-Konstante ist die Aenderungsrate von Xi.",
"Zwei Paradigmen. Standardmodell: Raum expandiert, sechs Parameter. FFGFT: Raum statisch, fraktale Vertiefung, ein Parameter Xi.",
"Wir leben nicht in einem expandierenden Ballon, sondern in einem sich vertiefenden Gewebe, einem kosmischen Gehirn. Xi gleich vier Drittel mal zehn hoch minus vier. Daraus folgt alles.",
]

# ================================================================
# PRESENTATION: 35 Folien - KORRIGIERT, passend zum HTML
# ================================================================
PRES_DE = [
# 0: Titelfolie
"Von Alpha gleich eins zur vollstaendigen Physik. Wie die SI-Reform 2019 und ein verhaeltnisbasiertes Einheitensystem natuerlich zur Zeit-Masse-Dualitaet und zur Angepassten Dynamischen Vakuum-Feldtheorie fuehren. Johann Pascher, Linz, Februar 2026.",
# 1: Vorwort
"Vorwort. Eine einfache Frage: Was passiert, wenn man die Konventionen der Physik konsequent zu Ende denkt? Setzt man Alpha gleich eins, entfaltet sich ein vollstaendiges Bild der Physik. Aus einem einzigen geometrischen Parameter, Xi gleich 4 durch 30000, folgen die Massen aller Elementarteilchen, die Gravitationskonstante, die Planck-Laenge, die Struktur der Raumzeit. Ein einziger Messwert genuegt, um das gesamte Gebaeude der Physik zu rekonstruieren.",
# 2: Teil I
"Teil eins: Das Fundament. Von der SI-Reform zur Ableitungskaskade.",
# 3: SI-Reform 2019
"Die Natur spricht in Verhaeltnissen, nicht in Kilogramm. Die SI-Reform 2019. Am 20. Mai 2019 wurden vier Naturkonstanten auf exakte Werte festgelegt. Die Natur selbst wurde zum Massstab. Bis zu diesem Tag war das Kilogramm definiert durch einen Zylinder aus Platin-Iridium. Nach der Reform: definiert durch das Plancksche Wirkungsquantum.",
# 4: SI-Reform Kerngedanke
"Die unvollendete Revolution. Fixiert: c, h quer, e. Noch frei: Alpha, ungefaehr eins durch 137. Die SI-Reform hat die Richtung vorgegeben: Weg von Artefakten, hin zu Naturkonstanten. Aber sie hat den logischen naechsten Schritt nicht gewagt, naemlich zu fragen, ob alle Konstanten aus einer einzigen folgen koennten.",
# 5: α = 1
"Es ist keine neue Physik. Es ist dieselbe Physik, nur ehrlicher aufgeschrieben. Der logische naechste Schritt: c gleich h quer gleich Alpha gleich eins. Alpha gleich eins zu setzen ist kein physikalischer Widerspruch. Es ist eine Umdefinition der Ladungseinheit. Was sich aendert, sind Zahlenwerte. Was sich nicht aendert, sind alle physikalischen Vorhersagen.",
# 6: Parameter ξ
"Ein Messwert. Sonst nichts. Xi gleich 4 durch 30000. Der einzige geometrische Parameter. Xi gleich Alpha geteilt durch E null Quadrat, gleich vier Drittel mal zehn hoch minus vier. Aus Xi folgt alles: Alle Teilchenmassen, die Gravitationskonstante, die Planck-Laenge, die Lichtgeschwindigkeit, die Boltzmann-Konstante.",
# 7: Ableitungskaskade
"Wenn man genau eine Zahl kennt, kennt man alle. Die Kaskade: Alpha gemessen, daraus Xi geometrisch, daraus Teilchenmassen durch Xi-Quantisierung, daraus G gleich Xi-Quadrat durch vier Elektronmassen mal K fraktal, daraus die Planck-Laenge und die Sub-Planck-Laenge L null gleich Xi mal Planck-Laenge, und schliesslich Kosmologie, CMB und die Dualitaet T mal m gleich eins.",
# 8: Kaskade Kerngedanke
"Keine Zirkularitaet. Die SI-Konstanten sind keine unabhaengigen Groessen. Sie sind verschiedene Fenster auf eine geometrische Realitaet. Der Wert 4 durch 30000 ist kein Zufall. 30000 durch 4 gleich 7500 ist die Windungszahl des fundamentalen Torus. Und 7500 gleich 2 hoch 2 mal 3 mal 5 hoch 4 besitzt mit seinen 36 Teilern eine ideale Symmetriestruktur fuer Resonanzen. Die einzige empirische Eingabe ist Alpha. Alles andere ist Geometrie und Algebra.",
# 9: Teil II
"Teil zwei: Die Architektur der Natur. Zeit-Masse-Dualitaet, Vakuumfeld und Gravitation.",
# 10: Zeit-Masse-Dualität
"Masse ist nicht das Gegenteil von Leichtigkeit. Masse ist das Gegenteil von Zeit. Das Kernaxiom: T mal m gleich eins. Zeit und Masse sind dual zueinander, zwei Perspektiven auf dieselbe physikalische Realitaet. Wo die Masse hoeher ist, vergeht die lokale Zeit langsamer. Wo weniger Masse vorhanden ist, ticken die Uhren schneller.",
# 11: Drei Perspektiven
"Drei gleichberechtigte Lesarten. Alles ist Energie E als fundamentales Feld. Alles ist Masse: m gleich E durch c Quadrat gleich eins durch T. Alles ist Zeit: T gleich eins durch m. Die Zeit-Masse-Dualitaet ist keine Hypothese. Sie ist die logische Konsequenz eines Systems, das alle Konstanten auf Eins setzt und nur mit Verhaeltnissen arbeitet.",
# 12: Vakuumfeld
"Das Vakuum ist nicht leer. Es ist das dichteste, was es gibt. Das Vakuumfeld Phi gleich Rho mal e hoch i Theta. Rho ist die Vakuumamplitude, proportional zur lokalen Massendichte. Theta ist die Vakuumphase und beschreibt die Zeitentwicklung: Theta Punkt gleich m gleich eins durch T.",
# 13: Vier Säulen
"Aus einem Feld, alle Physik. Gravitation gleich Vakuumkonvergenz: keine separate Kraft, kohaerente Phasenkruemmung des Vakuumfeldes. Quantenmechanik gleich Vakuumkohaerenz: Interferenz, Superposition, Verschraenkung als Eigenschaften von Phi. Masse gleich Vakuumenergie: ein Elektron ist eine stabile Resonanz in Phi, Masse ist die Frequenz. Schwarze Loecher gleich stabile Kerne: keine Singularitaeten, stabile T0-Knoten stabilisieren die Torusstruktur.",
# 14: Gravitation abgeleitet
"Die Schwaeche der Gravitation ist keine Schwaeche, sie ist eine geometrische Verduennung. G ist abgeleitet: G gleich Xi Quadrat durch vier Elektronmassen, mal Konversionsfaktor, mal K fraktal. G geht wie Xi Quadrat, ungefaehr zehn hoch minus acht. Die Schwaeche der Gravitation ist die Tatsache, dass die Raumzeit fast perfekt dreidimensional ist. Es gibt kein Hierarchieproblem, nur eine geometrische Verduennung.",
# 15: Teil III
"Teil drei: Die Geometrie des Universums. Torus, Hirnwindungen, fraktale Korrekturen.",
# 16: Der Torus
"Unendlich und begrenzt zugleich. Kein Rand, kein Anfang, kein Ende. Das Universum ist ein statischer, vierdimensionaler Torsionskristall. Das fundamentale Element: der Torus. Endliches Volumen, keine Raender, keine Singularitaeten. Die Windungszahl 7500 erzeugt die Sub-Planck-Skala. Selbstaehnlich ueber alle Groessenordnungen.",
# 17: Torus Konsequenzen
"Was der Torus loest. Schwarze Loecher: keine Punktsingularitaet, stabile Vakuumkerne. Urknall: kein singulaerer Anfang, das Universum ist ewig. Feldtheorie: Propagatoren divergieren nie, keine Renormierung noetig. Der Torus ist das einzige geometrische Objekt, das gleichzeitig endlich, randlos, singularitaetsfrei und selbstaehnlich ist.",
# 18: Hirnwindungs-Torus
"Die Natur faltet, um zu verdichten, vom Gehirn bis zum Universum. Vom Torus zum Hirnwindungsgeflecht. Der glatte Torus verformt sich zu einer Topologie, die an die Gyri und Sulci der Grosshirnrinde erinnert. Dieselbe geometrische Loesung: Oberflaeche maximieren in begrenztem Volumen. Elementarteilchen sind stehende Wellen im Windungsgeflecht. Die drei Generationen sind drei Resonanzmoden desselben geometrischen Objekts.",
# 19: Fraktale Korrektur
"Die Raumzeit ist fast dreidimensional. Aber fast macht den Unterschied. K fraktal gleich null Komma 9867. Die fraktale Raumdimension betraegt 3 minus Xi, ungefaehr 2,9998667. Eine winzige Abweichung von der perfekten Drei. Aber ueber 17 Groessenordnungen Energielauf akkumuliert sie sich zu einer messbaren 1,3 Prozent Korrektur: K fraktal gleich eins minus hundert Xi.",
# 20: Fraktal Kerngedanke
"Warum K fraktal keine Wahl ist. Es gibt zwei unabhaengige Wege, das Massenverhaeltnis Elektron zu Myon zu berechnen. Die Forderung, dass beide denselben Wert liefern, bestimmt K fraktal eindeutig. Die fraktale Raumzeit wirkt als natuerlicher Regulator. K fraktal ist keine freie Wahl, kein Anpassungsparameter. Er ist eine geometrische Notwendigkeit.",
# 21: Teil IV
"Teil vier: Die Konsequenzen. Quantencomputer und experimentelle Vorhersagen.",
# 22: Quantencomputer
"Deterministische Quantenlogik. In T0 sind Qubits keine probabilistischen Zustaende, sondern Energiefeld-Konfigurationen. Das Hadamard-Gatter erhaelt eine Xi-Korrektur. Der Shor-Algorithmus verbessert sich leicht. Besonders vielversprechend: die fraktale Xi-Daempfung bietet natuerliche Stabilisierung gegen Dekohaerenz. Das Messproblem verschwindet: kein Wellenfunktionskollaps, nur kontinuierliche Zeitfeld-Evolution.",
# 23: Experimentelle Vorhersagen
"Eine Theorie ohne testbare Vorhersagen ist Philosophie. T0 liefert Zahlen. Bell-Test-Abweichungen in 73-Qubit-Systemen. Raeumliche Korrelationsverzoegerungen: ungefaehr 445 Nanosekunden bei 1000 Kilometer. Tau-Anomalie testbar bei Belle 2. Alpha s bei der Tau-Masse gleich null Komma 3224. Gravitationswellen-Korrekturen bei hohen Frequenzen.",
# 24: CMB und Kosmologie
"Kosmische Mikrowellenhintergrundstrahlung. In T0 entstehen die CMB-Anisotropien durch Zeitfeldvariationen, nicht durch inflationaere Expansion. Die Rotverschiebung ist keine Expansion des Raumes, sondern Folge der Zeitfeld-Dynamik.",
# 25: Teil V
"Teil fuenf: Das groessere Bild. Determinismus, Bewusstsein und die Grenzen der Beschreibung.",
# 26: Determinismus
"Gott wuerfelt nicht, aber der Schmetterling flattert auf allen Skalen. In T0 ist alles prinzipiell determiniert. Quantenzufall ist eine Illusion deterministischer Zeitfeld-Dynamik. Der fraktale Schmetterlingseffekt potenziert sich ueber alle Skalen. Die Born-Regel ist nicht fundamental, sie ist emergent.",
# 27: Determinismus Kerngedanke
"Determiniert und doch unvorhersagbar. Die Wahrscheinlichkeitsbeschreibung funktioniert nicht, weil die Natur zufaellig ist. Sie funktioniert, weil die deterministische Komplexitaet unsere Rechenkapazitaet uebersteigt. T0 vereint vollstaendigen Determinismus mit praktischer Unvorhersagbarkeit. Die Born-Regel ist der beste Kompass in einem Labyrinth, das zu komplex fuer eine exakte Karte ist.",
# 28: Bewusstsein
"Bewusstsein ist keine Substanz. Es ist eine Topologie. Fraktale Rekursion. Bewusstsein entsteht dort, wo ein System sich selbst beobachtet. Die fraktale Struktur ermoeglicht unendlich viele Rueckkopplungsebenen auf endlichem Volumen. Das Gehirn ist nicht zufaellig ein gefaltetes Objekt. Die Hirnwindungs-Topologie ist die Voraussetzung fuer Bewusstsein.",
# 29: Grenzen der Beschreibung
"Die Landkarte ist nicht das Territorium. Demut vor der Natur. Die Gleichungen sind Landkarten, nicht das Territorium. Was die Theorie leistet: zeigen, dass die Natur mit einem einzigen Parameter beschrieben werden kann. Was sie nicht leistet: erklaeren, warum es ueberhaupt etwas gibt statt nichts.",
# 30: Alles ist Information
"Am Anfang war das Wort, und das Wort war eine Zahl. Die vierte Perspektive: Energie, Masse, Zeit, und tiefer als alle drei: Information. Die gesamte T0-Physik reduziert sich auf drei Elemente: Eine Zahl, Xi gleich 4 durch 30000. Eine Geometrie, den Torus. Eine Regel, T mal m gleich eins. Das sind keine physikalischen Objekte. Das sind reine Relationen.",
# 31: Evolution
"Nicht zufaellig, sondern geometrisch. Evolution ist geometrisch gefuehrt. Die Xi-Geometrie definiert eine Energielandschaft, und die Evolution wandert auf dieser Landschaft. Das Gehirn mit seinen Windungen, die Lunge mit ihren Veraestelungen, die Blutgefaesse, alles geometrische Attraktoren im Raum der moeglichen Formen.",
# 32: Sub-Planck-Grenze
"Wo die Physik endet. Unterhalb der Sub-Planck-Skala hat die Raumzeit keine definierte Struktur im Sinne der T0-Feldgleichungen. Was dort geschieht, ist fuer die Physik prinzipiell unsichtbar. Hier oeffnet sich ein Nadeloehr: Eine Entitaet ausserhalb des Systems muesste keine Naturgesetze brechen, um zu wirken. Eine Verschiebung kleiner als Xi mal Planck-Laenge, physikalisch undetektierbar, kausal wirksam durch den fraktalen Schmetterlingseffekt.",
# 33: Der rote Faden
"Der rote Faden. SI-Reform 2019: Konstanten fixiert. Konsequent weiterdenken: Alpha gleich eins. Verhaeltnisbasiertes System ergibt Xi gleich 4 durch 30000. Torus, Hirnwindungsgeflecht, fraktale Korrektur K fraktal. Zeit-Masse-Dualitaet: T mal m gleich eins. FFGFT: Phi gleich Rho mal e hoch i Theta. Daraus folgen G, Teilchenmassen, Planck-Skala, Kosmologie, Quantencomputer.",
# 34: Schluss
"Die Natur ist einfacher als gedacht. Wir haben sie nur in zu vielen willkuerlichen Einheiten versteckt, und die Windungen des fundamentalen Torus uebersehen. Johann Pascher, T0-Theorie.",
]

PRES_EN = [
# 0: Title
"From Alpha equals one to Complete Physics. How the 2019 SI reform and a ratio-based unit system naturally lead to time-mass duality and the Adapted Dynamic Vacuum Field Theory. Johann Pascher, Linz, February 2026.",
# 1: Preface
"Preface. A simple question: What happens if you follow the conventions of physics to their logical conclusion? Set Alpha to one, and a complete picture of physics unfolds. From a single geometric parameter, Xi equals 4 over 30,000, follow the masses of all elementary particles, the gravitational constant, the Planck length, the structure of spacetime.",
# 2: Part I
"Part one: The Foundation. From the SI reform to the derivation cascade.",
# 3: SI Reform
"Nature speaks in ratios, not in kilograms. The 2019 SI Reform. On May 20th 2019, four natural constants were fixed to exact values. Nature itself became the standard. Before: the kilogram was defined by a platinum-iridium cylinder. After: defined by the Planck constant.",
# 4: SI Key Insight
"The unfinished revolution. Fixed: c, h-bar, e. Still free: Alpha, approximately one over 137. The SI reform pointed the way: away from artifacts, toward natural constants. But it didn't dare ask whether all constants might follow from a single one.",
# 5: α = 1
"It's not new physics. It's the same physics, just written more honestly. The logical next step: c equals h-bar equals Alpha equals one. Setting Alpha to one is not a physical contradiction. It's a redefinition of the charge unit. What changes are numerical values. What doesn't change are all physical predictions.",
# 6: Parameter ξ
"One measurement. Nothing else. Xi equals 4 over 30,000. The only geometric parameter. Xi equals Alpha divided by E-zero squared, equals four thirds times ten to the minus four. From Xi follows everything: all particle masses, the gravitational constant, the Planck length, the speed of light, the Boltzmann constant.",
# 7: Derivation Cascade
"If you know exactly one number, you know them all. The cascade: Alpha measured, then Xi geometric, then particle masses through Xi-quantization, then G equals Xi squared over four electron masses times K-fractal, then the Planck length, and finally cosmology, CMB, and T times m equals one.",
# 8: Cascade Key Insight
"No circularity. The SI constants are not independent quantities. They are different windows onto a geometric reality. The value 4 over 30,000 is no coincidence. 30,000 over 4 equals 7,500, the winding number of the fundamental torus. And 7,500 has 36 divisors, an ideal symmetry structure for resonances. The only empirical input is Alpha. Everything else is geometry and algebra.",
# 9: Part II
"Part two: The Architecture of Nature. Time-mass duality, vacuum field and gravity.",
# 10: Time-Mass Duality
"Mass is not the opposite of lightness. Mass is the opposite of time. The core axiom: T times m equals one. Time and mass are dual to each other, two perspectives on the same physical reality. Where mass is higher, local time passes slower. Where less mass is present, clocks tick faster.",
# 11: Three Perspectives
"Three equivalent readings. Everything is energy E as the fundamental field. Everything is mass: m equals E over c squared equals one over T. Everything is time: T equals one over m. Time-mass duality is not a hypothesis. It is the logical consequence of a system that sets all constants to one and works only with ratios.",
# 12: Vacuum Field
"The vacuum is not empty. It is the densest thing there is. The vacuum field Phi equals Rho times e to the i Theta. Rho is the vacuum amplitude, proportional to local mass density. Theta is the vacuum phase and describes time evolution.",
# 13: Four Pillars
"From one field, all physics. Gravity equals vacuum convergence. Quantum mechanics equals vacuum coherence. Mass equals vacuum energy: an electron is a stable resonance in Phi. Black holes equal stable cores: no singularities.",
# 14: Gravity Derived
"The weakness of gravity is not a weakness, it's a geometric dilution. G is derived: G equals Xi squared over four electron masses, times the fractal correction. G scales as Xi squared, about ten to the minus eight. There is no hierarchy problem, only geometric dilution.",
# 15: Part III
"Part three: The Geometry of the Universe. Torus, brain windings, fractal corrections.",
# 16: The Torus
"Infinite and bounded at once. No edge, no beginning, no end. The universe is a static, four-dimensional torsion crystal. The fundamental element: the torus. Finite volume, no boundaries, no singularities. The winding number 7,500 generates the sub-Planck scale.",
# 17: Torus Consequences
"What the torus solves. Black holes: no point singularity, stable vacuum cores. Big Bang: no singular beginning, the universe is eternal. Field theory: propagators never diverge, no renormalization needed. The torus is the only geometric object that is simultaneously finite, boundaryless, singularity-free, and self-similar.",
# 18: Brain Torus
"Nature folds to densify, from the brain to the universe. From torus to brain-winding structure. The smooth torus deforms into a topology reminiscent of gyri and sulci. The same geometric solution: maximize surface in bounded volume. Particles are standing waves. Three generations are three resonance modes of the same geometric object.",
# 19: Fractal Correction
"Spacetime is almost three-dimensional. But almost makes all the difference. K-fractal equals 0.9867. The fractal spatial dimension is 3 minus Xi, approximately 2.9998667. A tiny deviation from perfect three. But over 17 orders of magnitude of energy running, it accumulates to a measurable 1.3 percent correction.",
# 20: Fractal Key Insight
"Why K-fractal is not a choice. There are two independent ways to calculate the electron-to-muon mass ratio. Requiring both to give the same experimental value uniquely determines K-fractal. Fractal spacetime acts as a natural regulator. K-fractal is a geometric necessity, not an adjustable parameter.",
# 21: Part IV
"Part four: The Consequences. Quantum computers and experimental predictions.",
# 22: Quantum Computers
"Deterministic quantum logic. In T-zero, qubits are not probabilistic states but energy field configurations. The Hadamard gate receives a Xi correction. The Shor algorithm improves slightly. Most promising: fractal Xi-damping offers natural stabilization against decoherence. The measurement problem vanishes.",
# 23: Experimental Predictions
"A theory without testable predictions is philosophy. T-zero delivers numbers. Bell test deviations in 73-qubit systems. Spatial correlation delays of about 445 nanoseconds at 1000 kilometers. Tau anomaly testable at Belle 2. Alpha-s at the tau mass equals 0.3224. Gravitational wave corrections at high frequencies.",
# 24: CMB
"Cosmic microwave background radiation. In T-zero, CMB anisotropies arise from time field variations, not from inflationary expansion. Redshift is not expansion of space, but a consequence of time field dynamics.",
# 25: Part V
"Part five: The Bigger Picture. Determinism, consciousness and the limits of description.",
# 26: Determinism
"God does not play dice, but the butterfly flutters at all scales. In T-zero, everything is in principle determined. Quantum randomness is an illusion of deterministic time field dynamics. The fractal butterfly effect amplifies across all scales. The Born rule is not fundamental, it is emergent.",
# 27: Determinism Key Insight
"Determined yet unpredictable. The probabilistic description works not because nature is random. It works because the deterministic complexity exceeds any possible computational capacity. T-zero unites complete determinism with practical unpredictability. The Born rule is the best compass in a labyrinth too complex for an exact map.",
# 28: Consciousness
"Consciousness is not a substance. It is a topology. Fractal recursion. Consciousness arises where a system observes itself. The fractal structure enables infinitely many feedback levels in finite volume. The brain is not accidentally a folded object. Brain-winding topology is the prerequisite for consciousness.",
# 29: Limits
"The map is not the territory. Humility before nature. The equations are maps, not the territory. What the theory achieves: showing that nature can be described with a single parameter. What it does not achieve: explaining why there is something rather than nothing.",
# 30: Information
"In the beginning was the Word, and the Word was a number. The fourth perspective: Energy, mass, time, and deeper than all three: information. All of T-zero physics reduces to three elements: A number, Xi. A geometry, the torus. A rule, T times m equals one. These are not physical objects. They are pure relations.",
# 31: Evolution
"Not random, but geometric. Evolution is geometrically guided. Xi-geometry defines an energy landscape. Brain folds, lung branches, blood vessels: geometric attractors in the space of possible forms.",
# 32: Sub-Planck
"Where physics ends. Below the sub-Planck scale, spacetime has no defined structure. What happens there is in principle invisible to physics. Here a needle's eye opens: an entity outside the system would not need to break any natural law to act. A shift smaller than Xi times Planck length, physically undetectable, causally effective through the fractal butterfly effect.",
# 33: Common Thread
"The common thread. SI reform 2019: constants fixed. Think further: Alpha equals one. Ratio-based system yields Xi equals 4 over 30,000. Torus, brain-winding structure, fractal correction. Time-mass duality: T times m equals one. FFGFT vacuum field Phi. From this follow G, particle masses, Planck scale, cosmology, quantum computers.",
# 34: Conclusion
"Nature is simpler than we thought. We merely hid it in too many arbitrary units, and overlooked the windings of the fundamental torus. Johann Pascher, T-zero Theory.",
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--engine', choices=['edge','gtts','pyttsx3'], default=None)
    args = parser.parse_args()
    print("="*60); print("FFGFT Audio Generator"); print("="*60)
    print("\nEngines pruefen...")
    engine = detect_engine(args.engine)
    if not engine:
        print("\nKeine Engine! pip install gTTS"); sys.exit(1)
    print(f"\n>>> Verwende: {engine}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = 0; total_kb = 0
    for label, texts, lang, prefix in [
        ("Narrativ DE", NARRATIV, "de", "narrativ"),
        ("Praesentation DE", PRES_DE, "de", "pres_de"),
        ("Praesentation EN", PRES_EN, "en", "pres_en"),
    ]:
        print(f"\n{'='*40}\n{label} ({len(texts)} Folien)\n{'='*40}")
        for i, text in enumerate(texts):
            fname = os.path.join(OUTPUT_DIR, f"{prefix}_{i:02d}.mp3")
            sz = gen1(text, lang, fname, engine)
            if sz > 0:
                print(f"  {prefix}_{i:02d}.mp3  ({sz:.0f} KB)")
                total += 1; total_kb += sz
    print(f"\n{'='*60}")
    print(f"Fertig! {total} MP3-Dateien ({total_kb/1024:.1f} MB)")
    print(f"Kopiere 'audio/' neben die HTML-Dateien.")

if __name__ == "__main__":
    main()
