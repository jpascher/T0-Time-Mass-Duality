# Erzeugt den Paperback-Umschlag (Rueckseite + Ruecken + Vorderseite) fuer die Gesamtserie,
# 8.5 x 11 in, Beschnitt 0.125 in, weisses Papier (0.002252 in/Seite).
# Aufruf: python3 make_wrap_cover_teil.py <teil> <de|en> <seitenzahl> <ausgabe.pdf> [pb|hc]
# pb = Paperback (Standard), hc = Hardcover/Case Laminate 8.25 x 11 in
import asyncio, math, sys, base64, io, os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))

def motif_b64(n, tag):
    im = Image.open(os.path.join(HERE, '..', 'cover', f'Teil{n}_Cover_{tag.capitalize()}.jpg')).convert('RGB')
    im = im.crop((316, 316, 1284, 1284)).resize((1380, 1380), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'PNG'); return base64.b64encode(b.getvalue()).decode()
from playwright.async_api import async_playwright

BLEED = 0.125; TW = 8.5; TH = 11.0
def spine(pages): return (pages + pages % 2) * 0.002252

TXT = {
'de': dict(
  t1='Fundamentale Fraktal-Geometrische<br>Feldtheorie (FFGFT)', t2='oder T0-Theorie: Zeit-Masse-Dualität',
  teil='Teil {n} von 8', sub='Kerndokumente', spine='FFGFT / T0-Theorie: Zeit-Masse-Dualität — Gesamtwerk Teil {n}',
  head='Alle Naturkonstanten aus einer einzigen geometrischen Zahl?',
  paras=[
   'Die T0-Theorie (Zeit-Masse-Dualität) formuliert die Grundlagen der theoretischen Physik neu: Nicht Zeit ist relativ, sondern Masse — verankert an einer absoluten Zeit T₀. Aus dieser Umkehrung folgt eine universelle geometrische Konstante <b>ξ = 4/30000</b>, die Teilchenmassen, Kopplungsstärken und Fundamentalkonstanten in einem gemeinsamen Rahmen vereint.',
   'Teil 1 des Gesamtwerks legt die mathematischen Grundlagen: die intrinsische Zeit-Feld-Masse-Beziehung <b>T̃·m = 1</b>, die Herleitung der Teilchenmassen und der Feinstrukturkonstante α ≈ 1/137, das anomale magnetische Moment g−2, die Gravitationskonstante G sowie die Neutrinomassen — alles aus einem einzigen geometrischen Parameter.',
   'Quantenmechanik, Relativitätstheorie und Kosmologie auf einer gemeinsamen geometrischen Grundlage.'],
  bio='Johann Pascher ist unabhängiger theoretischer Physiker und Autor der FFGFT / T0-Theorie. In über 300 Dokumenten entwickelt er einen geometrischen Rahmen, der die Fundamentalkonstanten der Physik aus einem einzigen dimensionslosen Parameter ξ herleitet. Alle Arbeiten sind offen zugänglich.'),
'en': dict(
  t1='Fundamental Fractal-Geometric<br>Field Theory (FFGFT)', t2='or T0 Theory – Time-Mass Duality',
  teil='Part {n} of 8', sub='Core Documents', spine='FFGFT / T0 Theory: Time-Mass Duality — Complete Works Part {n}',
  head='All constants of nature from a single geometric number?',
  paras=[
   'The T0 theory (time–mass duality) reformulates the foundations of theoretical physics: it is not time that is relative but mass — anchored to an absolute time T₀. This inversion yields a universal geometric constant <b>ξ = 4/30000</b> that unites particle masses, coupling strengths and fundamental constants in a single framework.',
   'Part 1 of the complete works lays the mathematical foundations: the intrinsic time–field–mass relation <b>T̃·m = 1</b>, the derivation of particle masses and of the fine-structure constant α ≈ 1/137, the anomalous magnetic moment g−2, the gravitational constant G and the neutrino masses — all from one geometric parameter.',
   'Quantum mechanics, relativity and cosmology on a common geometric foundation.'],
  bio='Johann Pascher is an independent theoretical physicist and author of FFGFT / T0 theory. In more than 300 documents he develops a geometric framework that derives the fundamental constants of physics from a single dimensionless parameter ξ. All work is openly accessible.'),
}


# Teilspezifische Rueckseitentexte (De); Teil 1 steht in TXT['de'].
PARTS_DE = {
 2: dict(sub='Mathematische Grundlagen<br>und Formeln',
  head='Dieselbe Idee — geometrisch, algebraisch, feldtheoretisch.',
  paras=['Band 2 vertieft die Grundlagen aus Band 1 mathematisch. Er entwickelt den Lagrange-Formalismus der Theorie in mehreren Zugängen, eliminiert die Masse aus der Dirac-Gleichung und stellt die Verbindung zu Quantenfeldtheorie und Quantenmechanik her.',
   'Die Zeit-Masse-Dualität <b>T̃·m = 1</b> wird universell abgeleitet, energiebasiert formuliert und in vollständigen Rechnungen bis zu Teilchenmassen und physikalischen Konstanten durchgeführt — einschließlich des vollständigen Teilchenspektrums und der erweiterten Analyse der Bell-Tests.',
   'Wiederholungen sind beabsichtigt: Jedes Konzept erscheint aus einem anderen Blickwinkel und mit größerer mathematischer Tiefe.']),
 3: dict(sub='Quantenmechanik, Anwendungen<br>und Photonik',
  head='Von der Geometrie zur Messung.',
  paras=['Band 3 schließt die ursprüngliche Drei-Band-Konzeption ab und wendet die Theorie an: CMB-Temperatur, Hubble-Konstante und geometrische Kosmologie, Bell-Ungleichungen, Verschränkung und Quantencomputing, Casimir-Effekt und die Verbindung zur Quantenfeldtheorie.',
   'Hinzu kommen Vergleiche mit anderen theoretischen Ansätzen, die Auseinandersetzung mit Einwänden und die erste Darstellung des FFGFT-Formalismus — der Fundamentalen Fraktalen Geometrischen Feldtheorie.',
   'Der Parameter <b>ξ = 4/30000</b> erscheint hier in kosmologischen, quantenphysikalischen und feldtheoretischen Zusammenhängen — konsistent in jedem Kontext.']),
 4: dict(sub='Neuere Dokumente und<br>Erweiterungen (2025–2026)',
  head='Numerische Vorhersagen und neue Reihen.',
  paras=['Band 4 versammelt 37 Dokumente, die nach der ursprünglichen Drei-Band-Konzeption entstanden sind: Erweiterungen zu Bell-Tests, Asymmetrie und Lagrangian, eine zusammenhängende Reihe numerischer Vorhersagen — Koide-Relation, g−2, Lepton-Lebensdauern, H₀-Verhältnis und die LiNbO₃-Dispersion auf 16 Stellen exakt.',
   'Weitere Reihen behandeln Photonik und Qubit-Zustände, den Shor-Algorithmus, Spin-Stabilität sowie die frühen Begründungen der Torus-Geometrie und der Länge L₀.',
   'Bis Dok. 184 wird die Theorie auf Schicht 1 erarbeitet: kompaktes T⁴, korrekturfreie Beschreibung in natürlichen Einheiten.']),
 5: dict(sub='Schichten, Hilbertraum-Brücke<br>und jüngste Klärungen',
  head='Die methodische Konsolidierung.',
  paras=['Band 5 trägt das methodische Gerüst der Theorie. Die Hilbertraum-Brücke setzt die FFGFT formal zur Quantenmechanik in Beziehung: operationale Äquivalenz bei interpretativer Divergenz.',
   'Die Schichten- und Skalenleiter-Dokumente arbeiten die Beschreibung in Schicht 1 (statisch, kompakt) und Schicht 2 (dynamisch, SI-projiziert) systematisch durch. Dazu kommen die vollständige Feldtheorie-Darstellung, der Rekursionsoperator, der Informationsformalismus und das Korrekturregister.',
   'Den Abschluss bildet die epistemische Selbstpositionierung in Dok. 262: Akzeptanz ohne Anschauung und die Innensicht der dekompaktifizierten Zeit.']),
 6: dict(sub='Holografie, HLV-Brücke<br>und die Struktur der Zeit',
  head='Wie wird aus dem kompakten T⁴ die beobachtete Welt?',
  paras=['Band 6 umfasst die Dokumente 263 bis 310. Er beginnt mit dem holografischen Prinzip in fraktaler Lesart, der kosmologischen Entartung zwischen ΛCDM und FFGFT und den CMB-Peak-Verhältnissen aus dem T⁴.',
   'Es folgt die Projektionskette vom T⁴ in den Beobachtungsraum bis zur gerechneten Brücke zum Helix-Light-Vortex-Ansatz. Der dynamische Sektor trennt Betrag und Phase in den vier Fermion-Sektoren und zeigt die doppelte Herkunft des Winkels <b>θ = 2/9</b>.',
   'Zeit und Information bilden den vierten Teil: Zeit als logarithmische Spirale, Information als Ausgang statt Grundeinheit, die native Zeit-Energie-Reziprozität.']),
 7: dict(sub='Gitter im Hilbertraum,<br>Spektraltheorie und Galois-Struktur',
  head='Die algebraische Struktur der kompakten Geometrie.',
  paras=['Band 7 umfasst die Dokumente 311 bis 343. Das Gitter wird als Indexmenge der Fouriermoden gelesen — Geometrie wird zu Spektrum und Faser. Es folgen die Spektraltheorie der FFGFT-Tori, die algebraische Herleitung von <b>SU(3)<sub>c</sub></b> aus der ℤ₃-Trialität und der Weinberg-Winkel bei M<sub>Z</sub> mit vollständigem Renormierungsgruppenlauf.',
   'Weitere Dokumente behandeln den Hawking-Mechanismus, die Selbstadjungiertheit des fundamentalen Operators, Resonanz und Synchronisation und zwei Wege vom Diskreten zum Kontinuum.',
   'Die Galois-Brücke schließt den Band: Frobenius-Automorphismus und Sektorpaarung sind strukturgleich; über <b>GF(27)*</b> folgen Massenverhältnisse, Neutrino-Hierarchie und die Zeta-Funktion des T⁴/ℤ₃-Torus.']),
 8: dict(sub='Standardmodell aus GF(27),<br>Leptonmassen und Schnittstellen',
  head='Vom endlichen Körper zum Standardmodell.',
  paras=['Band 8 umfasst die Dokumente 344 bis 389 und schließt die Sammlung auf dem Stand Oktober 2026 ab. Aus <b>GF(27)*</b> folgen Ladungsquantisierung, die Gell-Mann-Nishijima-Relation, die Generationenstruktur und die SU(2)<sub>L</sub>-Chiralität.',
   'Die Leptonmassen werden aus mehreren Richtungen erschlossen: Koide-Amplitude d/c = √2, θ = p₀ = 2/9 als zwei Lesarten eines Quotienten, Ikosaeder, Matrixelement-Prinzip und der Yukawa-Mechanismus als Folge von <b>T̃·m = 1</b>.',
   'Harmonik und Algebra erweisen sich als dieselbe Mathematik; die Schnittstellen zu anderen Rahmen sind vollständig dokumentiert. Für den Überblick: Dok. 384 (Kurzfassung), für offene Abweichungen Dok. 387.']),
}

PARTS_EN = {
 2: dict(sub='Mathematical Foundations<br>and Formulas',
  head='One idea — geometric, algebraic, field-theoretic.',
  paras=['Volume 2 deepens the foundations of Volume 1 mathematically. It develops the Lagrangian formalism of the theory along several routes, eliminates mass from the Dirac equation and establishes the connection to quantum field theory and quantum mechanics.',
   'The time–mass duality <b>T̃·m = 1</b> is derived universally, formulated in terms of energy and carried through complete calculations up to particle masses and physical constants — including the full particle spectrum and the extended analysis of the Bell tests.',
   'Repetition is intended: every concept appears from a different angle and with greater mathematical depth.']),
 3: dict(sub='Quantum Mechanics, Applications<br>and Photonics',
  head='From geometry to measurement.',
  paras=['Volume 3 completes the original three-volume plan and applies the theory: CMB temperature, the Hubble constant and geometric cosmology, Bell inequalities, entanglement and quantum computing, the Casimir effect and the connection to quantum field theory.',
   'It adds comparisons with other theoretical approaches, a discussion of objections and the first presentation of the FFGFT formalism — the Fundamental Fractal Geometric Field Theory.',
   'The parameter <b>ξ = 4/30000</b> appears here in cosmological, quantum-physical and field-theoretic settings — consistent in every context.']),
 4: dict(sub='Newer Documents<br>and Extensions (2025–2026)',
  head='Numerical predictions and new series.',
  paras=['Volume 4 collects 37 documents written after the original three-volume plan: extensions on Bell tests, asymmetry and the Lagrangian, and a connected series of numerical predictions — the Koide relation, g−2, lepton lifetimes, the H₀ ratio and the LiNbO₃ dispersion exact to 16 digits.',
   'Further series cover photonics and qubit states, Shor’s algorithm, spin stability and the early justifications of the torus geometry and of the length L₀.',
   'Up to Doc. 184 the theory is worked out on layer 1: compact T⁴, correction-free description in natural units.']),
 5: dict(sub='Layers, Hilbert-Space Bridge<br>and Recent Clarifications',
  head='The methodological consolidation.',
  paras=['Volume 5 carries the methodological framework of the theory. The Hilbert-space bridge relates FFGFT formally to quantum mechanics: operational equivalence with interpretive divergence.',
   'The layer and scale-ladder documents work through the description in layer 1 (static, compact) and layer 2 (dynamic, SI-projected) systematically. They are joined by the complete field-theory presentation, the recursion operator, the information formalism and the correction register.',
   'The volume closes with the epistemic self-positioning of Doc. 262: acceptance without visualisation and the inside view of decompactified time.']),
 6: dict(sub='Holography, the HLV Bridge<br>and the Structure of Time',
  head='How does the compact T⁴ become the observed world?',
  paras=['Volume 6 covers Docs. 263 to 310. It opens with the holographic principle in its fractal reading, the cosmological degeneracy between ΛCDM and FFGFT, and the CMB peak ratios derived from T⁴.',
   'Next comes the projection chain from T⁴ to observation space, up to the computed bridge to the Helix–Light–Vortex approach. The dynamical sector separates modulus and phase in the four fermion sectors and shows the twofold origin of the angle <b>θ = 2/9</b>.',
   'Time and information form the fourth part: time as a logarithmic spiral, information as an output rather than a basic unit, and the native time–energy reciprocity.']),
 7: dict(sub='The Lattice in Hilbert Space,<br>Spectral Theory and Galois Structure',
  head='The algebraic structure of the compact geometry.',
  paras=['Volume 7 covers Docs. 311 to 343. The lattice is read as the index set of the Fourier modes — geometry becomes spectrum and fibre. Then follow the spectral theory of the FFGFT tori, the algebraic derivation of <b>SU(3)<sub>c</sub></b> from ℤ₃ triality and the Weinberg angle at M<sub>Z</sub> with full renormalisation-group running.',
   'Further documents treat the Hawking mechanism, the self-adjointness of the fundamental operator, resonance and synchronisation, and two routes from the discrete to the continuum.',
   'The Galois bridge closes the volume: the Frobenius automorphism and the sector pairing are structurally identical; via <b>GF(27)*</b> follow mass ratios, the neutrino hierarchy and the zeta function of the T⁴/ℤ₃ torus.']),
 8: dict(sub='The Standard Model from GF(27),<br>Lepton Masses and Interfaces',
  head='From the finite field to the Standard Model.',
  paras=['Volume 8 covers Docs. 344 to 389 and brings the collection up to its October 2026 state. From <b>GF(27)*</b> follow charge quantisation, the Gell-Mann–Nishijima relation, the generation structure and SU(2)<sub>L</sub> chirality.',
   'The lepton masses are approached from several directions: the Koide amplitude d/c = √2, θ = p₀ = 2/9 as two readings of one quotient, the icosahedron, the matrix-element principle and the Yukawa mechanism as a consequence of <b>T̃·m = 1</b>.',
   'Harmonics and algebra turn out to be the same mathematics; the interfaces with other frameworks are fully documented. For an overview: Doc. 384 (summary); for remaining deviations: Doc. 387.']),
}
PARTS = {'de': PARTS_DE, 'en': PARTS_EN}

def star_svg():
    c = 300; lines = []
    for k in range(24):
        a = 2 * math.pi * k / 24
        r = 300 if k % 2 == 0 else 280
        lines.append(f'<line x1="{c}" y1="{c}" x2="{c+r*math.sin(a):.1f}" y2="{c-r*math.cos(a):.1f}"/>')
    return (f'<svg viewBox="0 0 600 600" width="100%" height="100%"><g stroke="#d4a537" stroke-width="2.6" opacity=".95">{"".join(lines)}</g>'
            f'<circle cx="{c}" cy="{c}" r="62" fill="#0b1324" stroke="#d4a537" stroke-width="4" opacity=".55"/>'
            f'<circle cx="{c}" cy="{c}" r="44" fill="none" stroke="#d4a537" stroke-width="3" opacity=".7"/>'
            f'<circle cx="{c}" cy="{c}" r="27" fill="#0b1324" stroke="#e0b44c" stroke-width="5"/></svg>')

def geometry(pages, kind):
    """Liefert Gesamtmass und die sichtbaren Felder (x, y, Breite, Hoehe) in Zoll.
    pb: Paperback 8.5x11, Beschnitt 0.125.  hc: Hardcover (Case Laminate) 8.25x11,
    Umschlag 0.591, Falz 0.197, Kantenueberstand 0.118, Ruecken = Seiten*0.002252 + 0.189."""
    if kind == 'pb':
        tw, th = TW, TH; s = spine(pages)
        W = 2*BLEED + 2*tw + s; H = th + 2*BLEED
        back = (BLEED, BLEED, tw, th); sx = BLEED + tw; front = (sx + s, BLEED, tw, th)
    else:
        tw, th, WR, HI, OV = 8.25, 11.0, 0.591, 0.197, 0.118
        s = (pages + pages % 2) * 0.002252 + 0.189
        W = 2*tw + s + 1.812; H = th + 2*WR + 2*OV
        back = (WR, WR, tw + OV, th + 2*OV); sx = WR + tw + OV + HI
        front = (sx + s + HI, WR, tw + OV, th + 2*OV)
    return W, H, s, back, sx, front

def html(n, tag, pages, kind='pb'):
    t = dict(TXT[tag]); W, H, s, back, sx, front = geometry(pages, kind)
    motif = star_svg()
    if n != 1:
        t.update(PARTS[tag][n]); motif = f'<img src="data:image/png;base64,{motif_b64(n, tag)}" style="width:100%;height:100%">'
    paras = ''.join(f'<p>{p}</p>' for p in t['paras'])
    return W, H, s, f'''<html><head><meta charset="utf-8"><style>
@page{{size:{W}in {H}in;margin:0}} html,body{{margin:0;padding:0}}
body{{width:{W}in;height:{H}in;position:relative;overflow:hidden;background:#070d1e;font-family:Inter,'DejaVu Sans',sans-serif;color:#e6e9f0}}
.bg{{position:absolute;inset:0;background:{'linear-gradient(180deg,#0a1226 0%,#060b1a 100%)' if n==1 else '#081023'}}}
.gold{{color:#d4a537}}
.front{{position:absolute;left:{front[0]}in;top:{front[1]}in;width:{front[2]}in;height:{front[3]}in}}
.fin{{position:absolute;left:0.55in;top:0.45in;width:{front[2]-1.1}in;height:{front[3]-0.9}in;text-align:center}}
.hr{{height:2px;background:#d4a537}} .hr2{{height:1px;background:#6b6f7a;margin:0 0.7in}}
.t1{{font-size:21pt;line-height:1.2;color:#d4a537;margin-top:.28in}}
.t2{{font-size:19pt;color:#d4a537;margin-top:.08in}}
.teil{{font-size:23pt;font-weight:700;color:#f2cc5c;margin:.14in 0 .16in}}
.star{{width:4.6in;height:4.6in;margin:.35in auto .3in}}
.sub{{font-size:{'30' if n==1 else '25'}pt;line-height:1.2;font-weight:700;color:#fff;margin-top:.22in}}
.fbot{{position:absolute;bottom:0;left:0;right:0}}
.fauth{{font-size:20pt;font-weight:700;color:#f2cc5c;margin-top:.18in}}
.forc{{font-size:11pt;color:#b8bfcc;margin:.06in 0 .2in}}
.spine{{position:absolute;left:{sx}in;top:0;width:{s}in;height:{H}in}}
.sp{{position:absolute;left:50%;top:50%;width:{front[3]-0.8}in;transform:translate(-50%,-50%) rotate(90deg);display:flex;justify-content:space-between;align-items:center;white-space:nowrap}}
.sp .st{{font-size:13pt;color:#d4a537}} .sp .sa{{font-size:16pt;font-weight:700;color:#fff}}
.back{{position:absolute;left:{back[0]+0.75}in;top:{back[1]+0.8}in;width:{back[2]-1.5}in}}
h1{{font-size:24pt;line-height:1.2;color:#f2cc5c;margin:0 0 .3in;font-weight:700}}
p{{font-size:12.5pt;line-height:1.5;margin:0 0 .17in;hyphens:auto}} p b{{color:#f2cc5c;font-weight:600}}
.rule{{width:1.6in;height:2px;background:#d4a537;margin:.35in 0 .22in}}
.bio{{font-size:11pt;line-height:1.5;color:#c8cfdb}} .auth{{font-size:15pt;font-weight:700;color:#fff;margin-bottom:.08in}}
.meta{{font-size:10pt;color:#9fb0c8;line-height:1.5;margin-top:.12in}}
</style></head><body><div class="bg"></div>
<div class="back"><h1>{t['head']}</h1>{paras}<div class="rule"></div>
<div class="auth">Johann Pascher</div><div class="bio">{t['bio']}</div>
<div class="meta">ORCID 0009-0000-6518-4064<br>github.com/jpascher/T0-Time-Mass-Duality</div></div>
<div class="spine"><div class="sp"><span class="st">{t['spine'].format(n=n)}</span><span class="sa">Johann Pascher</span></div></div>
<div class="front"><div class="fin"><div class="hr"></div>
<div class="t1">{t['t1']}</div><div class="t2">{t['t2']}</div><div class="teil">{t['teil'].format(n=n)}</div><div class="hr2"></div>
<div class="star">{motif}</div><div class="hr2"></div><div class="sub">{t['sub']}</div>
<div class="fbot"><div class="hr" style="margin:0 .25in"></div><div class="fauth">Johann Pascher</div><div class="forc">ORCID 0009-0000-6518-4064</div><div class="hr"></div></div>
</div></div></body></html>'''

async def main(n, tag, pages, out, kind='pb'):
    W, H, s, doc = html(n, tag, pages, kind)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.set_content(doc); await pg.wait_for_timeout(300)
        await pg.pdf(path=out, width=f'{W}in', height=f'{H}in', print_background=True)
        await b.close()
    print(f'{out}: {W:.4f} x {H:.4f} in, Ruecken {s:.4f} in ({pages} S.)')

if __name__ == '__main__':
    asyncio.run(main(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else 'pb'))
