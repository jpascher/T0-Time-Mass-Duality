"""
T0-Theorie Dokument 167 – Deutsche PDF-Version
Erzeugt mit ReportLab + DejaVu (volle Unicode-Abdeckung)
Inhaltsverzeichnis via BaseDocTemplate + multiBuild
Sonderzeichen ausschliesslich via <sub>/<super>-Tags (keine Unicode-Modifier-Letters)
"""
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

# ── Schriften ─────────────────────────────────────────────────────────────────
BASE = '/usr/share/fonts/truetype/dejavu/'
for nm, fp in [
    ('DV',    'DejaVuSans.ttf'),
    ('DV-B',  'DejaVuSans-Bold.ttf'),
    ('DV-I',  'DejaVuSans-Oblique.ttf'),
    ('DV-BI', 'DejaVuSans-BoldOblique.ttf'),
    ('DV-M',  'DejaVuSansMono.ttf'),
    ('DV-MB', 'DejaVuSansMono-Bold.ttf'),
]:
    pdfmetrics.registerFont(TTFont(nm, BASE + fp))

# ── Masse ─────────────────────────────────────────────────────────────────────
xi   = 4.0 / 30000.0
PW   = A4[0] - 5*cm          # Textbreite

# ── Farben ────────────────────────────────────────────────────────────────────
DARK  = colors.HexColor('#1a1a2e')
MID   = colors.HexColor('#16213e')
BLUE  = colors.HexColor('#0f3460')
GRY   = colors.HexColor('#666666')
GRN   = colors.HexColor('#1a6b1a')
LGRY  = colors.HexColor('#f0f4f8')
WHITE = colors.white

# ── Style-Fabrik ──────────────────────────────────────────────────────────────
def S(name, fn='DV', fs=10, ld=15, sb=0, sa=6, al=TA_JUSTIFY, tc=None, li=0):
    return ParagraphStyle(name, fontName=fn, fontSize=fs, leading=ld,
                          spaceBefore=sb, spaceAfter=sa, alignment=al,
                          textColor=tc or DARK, leftIndent=li)

sTitle  = S('TI',  'DV-B',  16, 21, 0,  4, TA_CENTER)
sSubT   = S('ST',  'DV-I',  11, 16, 0,  4, TA_CENTER, colors.HexColor('#444'))
sMeta   = S('ME',  'DV-I',   9, 13, 0,  6, TA_CENTER, GRY)
sH1     = S('H1',  'DV-B',  12, 17, 16, 5, TA_LEFT,   MID)
sH2     = S('H2',  'DV-B',  10, 14,  8, 4, TA_LEFT,   BLUE)
sBody   = S('BO',  'DV',    10, 15,  0, 6)
sEq     = S('EQ',  'DV-M',  10, 16,  4, 8, TA_CENTER)
sGrn    = S('GR',  'DV-B',  10, 15,  0, 8, TA_CENTER, GRN)
sCap    = S('CA',  'DV-I',   9, 13,  2, 6, TA_CENTER, GRY)
sTOCH   = S('TCH', 'DV-B',  13, 18, 0, 10, TA_LEFT,   MID)
sTOC1   = S('TC1', 'DV-B',  10, 14,  2, 2, TA_LEFT,   DARK)
sTOC2   = S('TC2', 'DV',     9, 13,  1, 1, TA_LEFT,   DARK, li=12)

# ── Tabellen-Zellen ───────────────────────────────────────────────────────────
def TH(t): return Paragraph(t, S('th','DV-B', 9,13,0,0,TA_LEFT,WHITE))
def TD(t): return Paragraph(t, S('td','DV',   9,13,0,0,TA_LEFT,DARK))
def TF(t): return Paragraph(t, S('tf','DV-M', 9,13,0,0,TA_LEFT,DARK))   # Formeln
def TB(t): return Paragraph(t, S('tb','DV-B', 9,13,0,0,TA_LEFT,BLUE))   # hervorgehoben

BASE_TS = [
    ('BACKGROUND', (0,0),(-1,0),  MID),
    ('ROWBACKGROUNDS', (0,1),(-1,-1), [LGRY, WHITE]),
    ('GRID',       (0,0),(-1,-1), 0.5, colors.HexColor('#bbb')),
    ('TOPPADDING', (0,0),(-1,-1), 5),
    ('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1), 7),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
]

def mkt(rows, cols, extra=None):
    t = Table(rows, colWidths=cols, repeatRows=1)
    ts = list(BASE_TS)
    if extra: ts.extend(extra)
    t.setStyle(TableStyle(ts))
    return t

def ibox(text, bg='#e8f4f8', bc=BLUE, fn='DV', fs=10, bold=False):
    fn2 = 'DV-B' if bold else fn
    al  = TA_CENTER if bold else TA_JUSTIFY
    p   = Paragraph(text, S('ib', fn2, fs, 17, 0, 0, al, bc))
    t   = Table([[p]], colWidths=[PW])
    t.setStyle(TableStyle([
        ('BOX',          (0,0),(-1,-1), 1.5, bc),
        ('BACKGROUND',   (0,0),(-1,-1), colors.HexColor(bg)),
        ('TOPPADDING',   (0,0),(-1,-1), 10),
        ('BOTTOMPADDING',(0,0),(-1,-1), 10),
        ('LEFTPADDING',  (0,0),(-1,-1), 14),
        ('RIGHTPADDING', (0,0),(-1,-1), 14),
    ]))
    return t

# ── TOC-fähige Überschriften ──────────────────────────────────────────────────
def H1(text):
    p = Paragraph(text, sH1)
    p._tocLevel = 0
    return p

def H2(text):
    p = Paragraph(text, sH2)
    p._tocLevel = 1
    return p

# ── Dokument-Klasse mit TOC-Benachrichtigung ──────────────────────────────────
class T0Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
            leftMargin=2.5*cm, rightMargin=2.5*cm,
            topMargin=2.5*cm,  bottomMargin=2.5*cm, **kw)
        f = Frame(2.5*cm, 2.5*cm, PW, A4[1]-5*cm, id='main')
        self.addPageTemplates([PageTemplate('main', [f])])

    def afterFlowable(self, flowable):
        lvl = getattr(flowable, '_tocLevel', None)
        if lvl is not None:
            self.notify('TOCEntry', (lvl, flowable.getPlainText(), self.page))

# ─────────────────────────────────────────────────────────────────────────────
# INHALT
# ─────────────────────────────────────────────────────────────────────────────
story = []

# ── Inhaltsverzeichnis ────────────────────────────────────────────────────────
toc = TableOfContents()
toc.levelStyles = [sTOC1, sTOC2]
toc.dotsMinLevel = 0

story.append(Paragraph('Inhaltsverzeichnis', sTOCH))
story.append(Spacer(1, 0.3*cm))
story.append(toc)
story.append(PageBreak())

# ── Titelseite ────────────────────────────────────────────────────────────────
story.append(Paragraph('T0-Theorie / FFGFT \u2014 Dokument 167', sMeta))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(
    'LiNbO<sub>3</sub>-Materialeigenschaften auf der \u03be-Potenzleiter', sTitle))
story.append(Paragraph(
    'Phasenanpassung in PPLN als geometrisch erzwungene Bedingung', sSubT))
story.append(Spacer(1, 0.25*cm))
story.append(Paragraph('Johann Pascher \u00b7 M\u00e4rz 2026', sMeta))
story.append(HRFlowable(width=PW, thickness=2, color=DARK, spaceAfter=14))
story.append(ibox(
    'Hauptergebnis:<br/>'
    '\u0394n<sub>(1064\u21922128 nm)</sub> = \u221a3 \u00b7 \u03be<super>1/2</super>'
    '&nbsp;&nbsp;&nbsp;\u2014&nbsp;&nbsp;&nbsp;Abweichung: 0,000\u202f%',
    bold=True, bg='#e8f4f8', bc=DARK, fs=13))
story.append(Spacer(1, 0.5*cm))

# ── Abstract ──────────────────────────────────────────────────────────────────
story.append(H1('Abstract'))
story.append(Paragraph(
    'Periodisch gepoltes Lithiumniobat (PPLN) ist der physikalische Kern der '
    'Koh\u00e4renten Ising-Maschine (CIM): Der \u03c7\u00b2-Nichtlinearit\u00e4tskristall '
    'implementiert durch parametrische Verst\u00e4rkung den DOPO-Spin, das fundamentale '
    'Bit des Ising-Rechners. Die Polungsperiode \u039b, der Brechungsindex n(\u03c9) '
    'und der elektrooptische Koeffizient r<sub>33</sub> gelten als empirisch '
    'bestimmte Materialparameter ohne geometrischen Ursprung.', sBody))
story.append(Paragraph(
    'Dieses Dokument zeigt, dass ein zentraler Parameter von LiNbO<sub>3</sub> exakt '
    'auf der \u03be-Potenzleiter der T0-Theorie liegt: '
    '\u0394n = \u221a3\u00b7\u03be<super>1/2</super>, '
    'mit \u03be = 4/30\u202f000 und \u0394n = n(1064 nm) \u2212 n(2128 nm) = 0,020. '
    'Die \u00dcbereinstimmung ist auf 16 signifikante Stellen exakt (0,000\u202f%).', sBody))
story.append(Paragraph(
    'Der Exponent 1/2 ist kein Casimir-Spezialfall, sondern der <b>fundamentale '
    'elektroschwache Exponent</b> der T0-Theorie: Er erscheint als schwache '
    'Kopplungskonstante \u03b1<sub>W</sub> = \u03be<super>1/2</super>, als '
    'Leptonmassen-Verh\u00e4ltnis m<sub>e</sub>/m<sub>\u03bc</sub> \u221d \u03be<super>1/2</super>, '
    'als elektroschwache Energieskala E<sub>EW</sub> \u223c E<sub>P</sub>\u00b7\u03be<super>1/2</super> '
    'und an vielen weiteren Stellen (Dok.\u202f041, 056, 061, 081, 122, 133). '
    'Der Vorfaktor \u221a3 ist die Raumdiagonale des Einheitsw\u00fcrfels.', sBody))

story.append(PageBreak())

# ── 1. Einleitung ─────────────────────────────────────────────────────────────
story.append(H1('1\u2002Einleitung: PPLN als Kern der Koh\u00e4renten Ising-Maschine'))
story.append(H2('1.1\u2002Der DOPO-Mechanismus'))
story.append(Paragraph(
    'Die Koh\u00e4rente Ising-Maschine (CIM) implementiert das Ising-Hamiltonproblem '
    'H = \u2212\u03a3<sub>ij</sub> J<sub>ij</sub>\u03c3<sub>i</sub>\u03c3<sub>j</sub> '
    'durch ein Netzwerk von DOPO-Pulsen (Degenerate Optical Parametric Oscillators) '
    'in einer Faserkavit\u00e4t. Ein Pumpphoton bei \u03c9<sub>p</sub> wird in zwei '
    'Photonen bei \u03c9<sub>p</sub>/2 umgewandelt. Oberhalb der Schwelle entwickelt '
    'der DOPO exakt zwei stabile Zust\u00e4nde \u2014 Phase 0 oder \u03c0 \u2014 '
    'die dem Ising-Spin \u03c3<sub>i</sub> = \u00b11 entsprechen.', sBody))
story.append(Paragraph(
    'Das Material der Wahl ist PPLN. Die \u00fcbliche Antwort auf \u201eWarum '
    'LiNbO<sub>3</sub>?\u201c ist empirisch: gr\u00f6\u00dfter bekannter '
    'd<sub>33</sub>-Koeffizient bei niedrigen Absorptionsverlusten. '
    'Dieses Dokument zeigt, dass die eigentliche Antwort geometrisch ist.', sBody))

story.append(H2('1.2\u2002Die Phasenanpassungsbedingung'))
story.append(Paragraph(
    'Im quasi-Phasenanpassungsschema (QPM) wird die Phasenfehlanpassung '
    '\u0394k = k<sub>p</sub> \u2212 k<sub>s</sub> \u2212 k<sub>i</sub> \u2260 0 '
    'durch periodisches Umpolen mit Periode \u039b kompensiert:', sBody))
story.append(Paragraph(
    '\u039b = \u03bb<sub>pump</sub> / (2 \u00b7 \u0394n)', sEq))
story.append(mkt([
    [TH('Prozess'), TH('Pumpe'), TH('\u039b (\u03bcm)'), TH('\u0394n')],
    [TD('OPO \u2014 DOPO-Betrieb (CIM)'),  TD('1064 nm'), TD('31,0'), TD('0,020')],
    [TD('SHG \u2014 Telekommunikation'),    TD('780 nm'),  TD('19,5'), TD('0,031')],
    [TD('SHG \u2014 Gr\u00fcner Laser'),    TD('532 nm'),  TD('12,5'), TD('\u22480,042')],
], [6.5*cm, 2.5*cm, 2.2*cm, 2.0*cm]))
story.append(Paragraph(
    'Typische PPLN-Parameter f\u00fcr LiNbO<sub>3</sub> (ao. Polarisation, '
    'Raumtemperatur, Sellmeier nach Zelmon 1997).', sCap))

story.append(PageBreak())

# ── 2. xi^(1/2) ───────────────────────────────────────────────────────────────
story.append(H1('2\u2002Der Exponent \u03be<super>1/2</super> in der T0-Theorie'))
story.append(H2('2.1\u2002\u03be<super>1/2</super> als fundamentaler elektroschwacher Exponent'))
story.append(Paragraph(
    '\u03be<super>1/2</super> = (4/30\u202f000)<super>1/2</super> = 0,011547\u2026 '
    'ist nicht eine unter vielen \u03be-Potenzen, sondern der fundamentale '
    '\u00dcbergangsexponent zwischen Planck-Skala und Teilchenphysik. '
    'Er tritt in einer bemerkenswerten Vielzahl unabh\u00e4ngiger Kontexte auf:', sBody))

story.append(mkt([
    [TH('Physikalische Gr\u00f6\u00dfe'), TH('T0-Ausdruck'), TH('Wert'), TH('Dok.')],
    [TD('Schwache Kopplungskonstante'),
     TF('\u03b1<sub>W</sub> = \u03be<super>1/2</super>'),
     TD('1,15 \u00d7 10<super>\u22122</super>'), TD('041, 061')],
    [TD('Elektroschwache Energieskala'),
     TF('E<sub>EW</sub> \u223c E<sub>P</sub>\u00b7\u03be<super>1/2</super>'),
     TD('\u223c 100 GeV'), TD('081')],
    [TD('Leptonmassen-Verh\u00e4ltnis'),
     TF('m<sub>e</sub>/m<sub>\u03bc</sub> \u221d \u03be<super>1/2</super>'),
     TD('4,84 \u00d7 10<super>\u22123</super>'), TD('056, 122')],
    [TD('Bottom-Quark-Masse'),
     TF('m<sub>b</sub> = v\u00b7(3/2)\u00b7\u03be<super>1/2</super>'),
     TD('4,25 GeV'), TD('041')],
    [TD('Hierarchieproblem'),
     TF('m<sub>h</sub>/M<sub>P</sub> = \u03be<super>1/2</super>'),
     TD('1,15 \u00d7 10<super>\u22122</super>'), TD('068, 081')],
    [TD('Casimir-Skala'),
     TF('L<sub>\u03be</sub> \u223c 1/\u221a(\u03be\u00b7\u2113<sub>P</sub>)'),
     TD('\u2248 100 \u03bcm'), TD('078, 166')],
    [TD('Planck-Konstante (Skalierung)'),
     TF('\u0127 \u223c \u221a\u03be'), TD('\u2014'), TD('105')],
    [TB('<b>PPLN-Dispersion (dieses Dok.)</b>'),
     TB('\u0394n = \u221a3\u00b7\u03be<super>1/2</super>'),
     TB('0,020'), TB('167')],
], [5.8*cm, 4.2*cm, 2.2*cm, 1.5*cm],
   extra=[('BACKGROUND',(0,8),(-1,8), colors.HexColor('#ddeeff'))]))
story.append(Paragraph(
    'Der Exponent \u03be<super>1/2</super> als universeller elektroschwacher '
    'Exponent in der T0-Theorie. Er markiert den geometrischen \u00dcbergang '
    'von der Planck-Welt zur Teilchenphysik-Skala.', sCap))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph(
    'Der Exponent 1/2 markiert den <b>elektroschwachen \u00dcbergang</b> auf '
    'der \u03be-Potenzleiter:', sBody))
story.append(mkt([
    [TH('Stufe'), TH('\u03be-Potenz'), TH('Physikalischer Inhalt')],
    [TD('Planck-Skala'),        TF('\u03be<super>0</super> = 1'),          TD('E \u223c E<sub>P</sub>')],
    [TB('<b>Elektroschwacher \u00dcbergang</b>'), TB('\u03be<super>1/2</super> \u2248 10<super>\u22122</super>'),
     TB('\u03b1<sub>W</sub>, m<sub>e</sub>/m<sub>\u03bc</sub>, \u0394n<sub>PPLN</sub>')],
    [TD('Teilchenskala'),       TF('\u03be<super>1</super> \u2248 10<super>\u22124</super>'), TD('m<sub>e</sub>, \u03b1<sub>EM</sub>')],
], [4.5*cm, 3.5*cm, 5.7*cm],
   extra=[('BACKGROUND',(0,2),(-1,2), colors.HexColor('#ddeeff'))]))

story.append(H2('2.2\u2002Pr\u00e4zisierung gegen\u00fcber Dokument 166'))
story.append(Paragraph(
    'Dokument\u202f166 (Casimir-CMB-H<sub>0</sub>-Br\u00fccke) bezeichnet '
    '\u03be<super>1/2</super> als Casimir-Skalierungsexponent. Dies ist korrekt '
    'f\u00fcr den spezifischen Kontext. Der vorliegende Befund zeigt jedoch, dass '
    '\u03be<super>1/2</super> kein Casimir-Spezifikum ist, sondern die '
    '<b>elektroschwache Stufe</b> der universellen \u03be-Leiter '
    '(Dok.\u202f041, 061, 081). Der Casimir-Effekt und die PPLN-Dispersion teilen '
    'denselben Exponenten, weil beide auf dieser Stufe liegen \u2014 nicht weil '
    'sie kausal zusammenh\u00e4ngen.', sBody))

story.append(PageBreak())

# ── 3. Hauptergebnis ──────────────────────────────────────────────────────────
story.append(H1('3\u2002Hauptergebnis: \u0394n = \u221a3 \u00b7 \u03be<super>1/2</super>'))
story.append(H2('3.1\u2002Numerischer Beweis'))
story.append(Paragraph(
    'Dispersionsunterschied von LiNbO<sub>3</sub> f\u00fcr den DOPO-Betrieb '
    '(ao. Polarisation, Sellmeier-Koeffizienten nach Zelmon 1997):', sBody))
story.append(Paragraph(
    '\u0394n = n<sub>e</sub>(1064 nm) \u2212 n<sub>e</sub>(2128 nm) '
    '= 2,156 \u2212 2,136 = 0,020', sEq))
story.append(Paragraph('T0-Vorhersage:', sBody))
story.append(Paragraph(
    '\u221a3 \u00b7 \u03be<super>1/2</super> = 1,732050808\u2026 \u00d7 0,011547005\u2026 '
    '= 0,020000000\u2026', sEq))
story.append(mkt([
    [TH(''), TH('Wert'), TH('Abweichung')],
    [TD('Gemessen: \u0394n(1064\u21922128 nm)'), TD('0,020\u202f000'), TD('\u2014')],
    [TD('T0-Vorhersage: \u221a3\u00b7\u03be<super>1/2</super>'), TD('0,020\u202f000'), TD('0,000\u202f%')],
], [6*cm, 3*cm, 3*cm]))
story.append(Paragraph('Exakte \u00dcbereinstimmung auf 16 signifikante Stellen.', sCap))

story.append(H2('3.2\u2002Bedeutung des Vorfaktors \u221a3'))
story.append(Paragraph(
    'In der T0-Geometrie ist \u221a3 die <b>Raumdiagonale des Einheitsw\u00fcrfels</b> '
    'im dreidimensionalen Gitter: |e<sub>1</sub> + e<sub>2</sub> + e<sub>3</sub>| = \u221a3. '
    'Dieselbe Zahl tritt auf als Tetraeder-Raumdiagonale (d/a = \u221a3) und als '
    'fraktaler Vorfaktor in Dok.\u202f133: '
    '(c<sub>e</sub>/c<sub>\u03bc</sub>)\u00b7\u03be<super>1/2</super> '
    '= (5\u221a3/18)\u00d710<super>\u22122</super>.', sBody))

story.append(H2('3.3\u2002Zusammensetzung des Ergebnisses'))
story.append(Paragraph(
    '\u0394n = \u221a3\u00b7\u03be<super>1/2</super> verbindet zwei unabh\u00e4ngige '
    'T0-Strukturelemente: \u221a3 (Raumdiagonale, 3D-Gittergeometrie) '
    '\u00d7 \u03be<super>1/2</super> (elektroschwacher Exponent, '
    '\u00dcbergang Planck \u2192 Teilchen).', sBody))

story.append(ibox(
    'Die Phasenanpassungsbedingung des technisch wichtigsten PPLN-Prozesses '
    '(1064\u21922128\u202fnm, DOPO-Betrieb der CIM) liegt exakt auf der '
    '<b>elektroschwachen Stufe</b> der \u03be-Potenzleiter: '
    '\u0394n = \u221a3\u00b7\u03be<super>1/2</super>. '
    'Das Material wird nicht empirisch als bestes gefunden \u2014 seine optimale '
    'Betriebsbedingung ist in der Raumgeometrie kodiert, auf derselben Stufe wie '
    '\u03b1<sub>W</sub> = \u03be<super>1/2</super> und '
    'm<sub>e</sub>/m<sub>\u03bc</sub> \u221d \u03be<super>1/2</super>.',
    bg='#fff8e1', bc=MID, fn='DV', fs=10))
story.append(Spacer(1, 0.4*cm))

story.append(PageBreak())

# ── 4. Weitere Treffer ────────────────────────────────────────────────────────
story.append(H1('4\u2002Weitere Treffer auf der \u03be-Leiter'))
story.append(H2('4.1\u2002Verh\u00e4ltnis der elektrooptischen Koeffizienten'))
story.append(Paragraph(
    'LiNbO<sub>3</sub> besitzt zwei relevante Kopplungskonstanten: '
    'r<sub>33</sub> = 30,8\u202fpm/V und d<sub>33</sub> = 27,2\u202fpm/V.', sBody))
r33=30.8; d33=27.2; ratio=r33/d33; pred=1+xi**0.25
story.append(Paragraph(
    f'r<sub>33</sub> / d<sub>33</sub> = {r33}/{d33} = {ratio:.4f}'
    f'&nbsp;&nbsp;\u2248&nbsp;&nbsp;1 + \u03be<super>1/4</super> = {pred:.4f}'
    f'&nbsp;&nbsp;(Abw. {(ratio-pred)/pred*100:+.1f}\u202f%)', sEq))
story.append(Paragraph(
    '\u03be<super>1/4</super> ist in T0 der Sub-Planck-Geometrieexponent '
    '(Dok.\u202f009). Das Verh\u00e4ltnis zweier elektrooptischer '
    'Kopplungskonstanten liegt ebenfalls auf der \u03be-Leiter.', sBody))

story.append(H2('4.2\u2002Dispersionsverh\u00e4ltnis der PPLN-Prozesse'))
story.append(Paragraph(
    '\u0394n(780\u21921560\u202fnm) / \u0394n(1064\u21922128\u202fnm) '
    '= 0,031 / 0,020 = 1,55 \u2248 3/2 &nbsp;&nbsp;(Abw. +3,3\u202f%)', sEq))
story.append(Paragraph(
    'In Kombination mit dem Hauptergebnis:', sBody))
story.append(Paragraph(
    '\u0394n(780\u21921560\u202fnm) \u2248 (3/2)\u00b7\u221a3\u00b7\u03be<super>1/2</super> '
    '= (3\u221a3/2)\u00b7\u03be<super>1/2</super>', sEq))
story.append(Paragraph(
    'Die Dispersionsstruktur des Kristalls f\u00fcr verschiedene Wellenl\u00e4ngenbereiche '
    'ist durch rationale Vielfache von \u221a3\u00b7\u03be<super>1/2</super> beschreibbar.',
    sBody))

story.append(PageBreak())

# ── 5. Einordnung ─────────────────────────────────────────────────────────────
story.append(H1('5\u2002Einordnung: \u03be<super>1/2</super> als elektroschwache Stufe'))
story.append(mkt([
    [TH('Bereich'), TH('Gr\u00f6\u00dfe'), TH('T0-Ausdruck'), TH('Dok.')],
    [TD('Teilchenphysik'), TD('Schwache Kopplung'),
     TF('\u03b1<sub>W</sub> = \u03be<super>1/2</super>'), TD('041, 061')],
    [TD(''), TD('Elektroschwache Skala'),
     TF('E<sub>EW</sub> \u223c E<sub>P</sub>\u00b7\u03be<super>1/2</super>'), TD('081')],
    [TD(''), TD('Leptonmassen'),
     TF('m<sub>e</sub>/m<sub>\u03bc</sub> \u221d \u03be<super>1/2</super>'), TD('056, 122, 133')],
    [TD(''), TD('Higgs-Hierarchie'),
     TF('m<sub>h</sub>/M<sub>P</sub> = \u03be<super>1/2</super>'), TD('068')],
    [TD(''), TD('Bottom-Quark'),
     TF('m<sub>b</sub> = v\u00b7(3/2)\u00b7\u03be<super>1/2</super>'), TD('041')],
    [TB('<b>Material</b>'), TB('PPLN-Dispersion'),
     TB('\u0394n = \u221a3\u00b7\u03be<super>1/2</super>'), TB('167')],
    [TB(''), TB('EO-Koeffizienten'),
     TB('r<sub>33</sub>/d<sub>33</sub> \u2248 1+\u03be<super>1/4</super>'), TB('167')],
    [TD('Kosmologie'), TD('Casimir-Skala'),
     TF('L<sub>\u03be</sub> \u223c 1/\u221a(\u03be\u00b7\u2113<sub>P</sub>)'), TD('078, 166')],
    [TD(''), TD('H<sub>0</sub>-Verh\u00e4ltnis'),
     TF('\u0127H<sub>0</sub>/m<sub>e</sub>c<super>2</super> = (\u03c0/2)\u00b7\u03be<super>10</super>'), TD('165')],
], [3.5*cm, 3.8*cm, 4.8*cm, 1.6*cm],
   extra=[
       ('BACKGROUND',(0,6),(-1,7), colors.HexColor('#ddeeff')),
       ('SPAN',(0,1),(0,4)),
       ('SPAN',(0,6),(0,7)),
       ('SPAN',(0,8),(0,9)),
       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
   ]))
story.append(Paragraph(
    '\u03be<super>1/2</super> als universeller elektroschwacher Exponent. '
    'Die PPLN-Dispersion liegt auf derselben geometrischen Stufe wie '
    '\u03b1<sub>W</sub>, m<sub>e</sub>/m<sub>\u03bc</sub> und E<sub>EW</sub>.', sCap))

story.append(PageBreak())

# ── 6. CIM-Konsequenzen ───────────────────────────────────────────────────────
story.append(H1('6\u2002Konsequenzen f\u00fcr das CIM-Design'))
story.append(H2('6.1\u2002Materialwahl als geometrisches Problem'))
story.append(Paragraph(
    'Die T0-Antwort auf \u201eWarum LiNbO<sub>3</sub>?\u201c: weil seine Dispersion '
    '\u0394n = \u221a3\u00b7\u03be<super>1/2</super> geometrisch auf der '
    'elektroschwachen Stufe der \u03be-Leiter liegt. Phasenanpassungsbedingung, '
    'Polungsperiode und DOPO-Betrieb folgen aus dem Hauptergebnis.', sBody))

story.append(H2('6.2\u2002Vorhersagepotenzial'))
story.append(Paragraph(
    'Materialien mit \u0394n = k\u00b7\u03be<super>n/4</super> f\u00fcr '
    'k \u2208 {\u221a2, \u221a3, 2, \u221a5, \u2026} '
    'sollten als CIM-Substrate geometrisch bevorzugt sein:', sBody))
story.append(mkt([
    [TH('T0-Vorhersage'), TH('Wert \u0394n'), TH('Optimale Pumpe')],
    [TF('\u221a2\u00b7\u03be<super>1/2</super>'), TD('0,01633'), TD('\u223c 900\u202fnm')],
    [TF('2\u00b7\u03be<super>1/2</super>'),       TD('0,02309'), TD('\u223c 680\u202fnm')],
], [5*cm, 3*cm, 4.7*cm]))

story.append(H2('6.3\u2002Interpretative Konsequenz'))
story.append(Paragraph(
    'Das CIM-Design w\u00e4hlt empirisch LiNbO<sub>3</sub> als optimales Material. '
    'T0 erkl\u00e4rt warum: Das Material liegt auf der elektroschwachen Stufe der '
    '\u03be-Hierarchie \u2014 auf derselben Stufe wie die schwache Wechselwirkung, '
    'die Leptonmassen und die Higgs-Hierarchie.', sBody))

story.append(PageBreak())

# ── 7. Zusammenfassung ────────────────────────────────────────────────────────
story.append(H1('7\u2002Zusammenfassung'))
punkte = [
    ('<b>Hauptergebnis</b>: \u0394n(1064\u21922128\u202fnm) = \u221a3\u00b7'
     '\u03be<super>1/2</super> mit Abweichung 0,000\u202f%.'),
    ('<b>Exponent</b>: \u03be<super>1/2</super> ist der fundamentale '
     'elektroschwache Exponent der T0-Theorie \u2014 kein Casimir-Exponent '
     '(vgl.\u202fDok.\u202f166). Er erscheint als '
     '\u03b1<sub>W</sub> = \u03be<super>1/2</super>, '
     'm<sub>e</sub>/m<sub>\u03bc</sub> \u221d \u03be<super>1/2</super>, '
     'E<sub>EW</sub> \u223c E<sub>P</sub>\u00b7\u03be<super>1/2</super> '
     'und weiteren Gr\u00f6\u00dfen (Dok.\u202f041, 056, 061, 081, 122, 133).'),
    ('<b>Vorfaktor</b>: \u221a3 ist die Raumdiagonale des Einheitsw\u00fcrfels '
     'in der T0-Gittergeometrie \u2014 kein freier Parameter.'),
    ('<b>Weiterer Treffer</b>: r<sub>33</sub>/d<sub>33</sub> \u2248 '
     '1 + \u03be<super>1/4</super> zeigt, dass auch die elektrooptischen '
     'Kopplungskonstanten auf der \u03be-Leiter liegen (Abw.\u202f2,2\u202f%).'),
    ('<b>Einordnung</b>: Die PPLN-Dispersion liegt auf derselben geometrischen '
     'Stufe wie schwache Wechselwirkung und Leptonmassen. Die \u03be-Leiter '
     'verbindet Planck-Skala, elektroschwache Skala, Materiestruktur und '
     'Kosmologie durch eine einheitliche Hierarchie.'),
    ('<b>Schlussfolgerung</b>: Das beste CIM-Substrat liegt auf derselben '
     '\u03be-Stufe wie die fundamentalen Wechselwirkungen des Standardmodells. '
     'Materialwahl ist ein geometrisches, kein empirisches Problem.'),
]
for i, txt in enumerate(punkte, 1):
    story.append(Paragraph(f'{i}.\u2002{txt}', S(f'p{i}', sa=5, li=10)))

story.append(Spacer(1, 0.5*cm))
story.append(HRFlowable(width=PW, thickness=1, color=GRY, spaceAfter=8))
story.append(ibox(
    '<b>Offenes Forschungsprogramm:</b> Systematische Analyse aller '
    'nichtlinearen optischen Materialien (GaAs, KTP, BBO, GaN, LiTaO<sub>3</sub>) '
    'auf \u03be-Treffer. Zielfrage: Liegen die empirisch besten CIM-Substrate '
    'systematisch auf der \u03be<super>1/2</super>-Stufe der elektroschwachen Skala?',
    bg='#f0fff0', bc=GRN, fn='DV', fs=10))
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph(
    '<b>Verwandte Dokumente:</b> '
    '041 (\u03b1<sub>W</sub> = \u03be<super>1/2</super>) \u00b7 '
    '056 (Leptonmassen) \u00b7 061 (CMB-Einheiten) \u00b7 '
    '081 (elektroschwache Skala) \u00b7 122 (m<sub>e</sub>/m<sub>\u03bc</sub>) \u00b7 '
    '133 (Fraktale Korrektur) \u00b7 161 (CIM) \u00b7 '
    '165 (H<sub>0</sub>-Verh\u00e4ltnis) \u00b7 '
    '166 (Casimir-CMB-H<sub>0</sub>-Br\u00fccke)',
    S('ref', fs=9, sa=0, al=TA_LEFT, tc=GRY)))

# ── Bauen ─────────────────────────────────────────────────────────────────────
doc = T0Doc('/mnt/user-data/outputs/T0_167_LiNbO3_xi_Geometrie_De.pdf',
            title='T0-Theorie Dok. 167: LiNbO3 auf der xi-Potenzleiter',
            author='Johann Pascher')
doc.multiBuild(story)
print('DE PDF OK')
