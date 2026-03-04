"""
T0-Theorie Dokument 168 – PDF-Generator (DE + EN)
Das Periodensystem als xi-Geometrie
ReportLab + DejaVu + multiBuild TOC
"""
import math
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
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

BASE = '/usr/share/fonts/truetype/dejavu/'
for nm, fp in [('DV','DejaVuSans.ttf'),('DV-B','DejaVuSans-Bold.ttf'),
               ('DV-I','DejaVuSans-Oblique.ttf'),('DV-M','DejaVuSansMono.ttf'),
               ('DV-MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(nm, BASE+fp))

xi   = 4.0/30000.0
E_P  = 1.221e28   # eV
m_e  = 0.511e6    # eV
m_P  = E_P
alpha= 1/137.036
R_inf= 13.5984    # eV
PW   = A4[0]-5*cm

DARK=colors.HexColor('#1a1a2e'); MID=colors.HexColor('#16213e')
BLUE=colors.HexColor('#0f3460'); GRY=colors.HexColor('#666666')
GRN=colors.HexColor('#1a6b1a');  LGRY=colors.HexColor('#f0f4f8')
WHITE=colors.white; RED=colors.HexColor('#8B0000')

def S(name,fn='DV',fs=10,ld=15,sb=0,sa=6,al=TA_JUSTIFY,tc=None,li=0):
    return ParagraphStyle(name,fontName=fn,fontSize=fs,leading=ld,
        spaceBefore=sb,spaceAfter=sa,alignment=al,textColor=tc or DARK,leftIndent=li)

sTitle=S('TI','DV-B',16,21,0,4,TA_CENTER); sSubT=S('ST','DV-I',11,16,0,4,TA_CENTER,colors.HexColor('#444'))
sMeta=S('ME','DV-I',9,13,0,6,TA_CENTER,GRY); sH1=S('H1','DV-B',12,17,16,5,TA_LEFT,MID)
sH2=S('H2','DV-B',10,14,8,4,TA_LEFT,BLUE); sBody=S('BO','DV',10,15,0,6)
sEq=S('EQ','DV-M',10,16,4,8,TA_CENTER); sCap=S('CA','DV-I',9,13,2,6,TA_CENTER,GRY)
sTOCH=S('TCH','DV-B',13,18,0,10,TA_LEFT,MID); sTOC1=S('TC1','DV-B',10,14,2,2,TA_LEFT,DARK)
sTOC2=S('TC2','DV',9,13,1,1,TA_LEFT,DARK,li=12)
sBox=S('BX','DV-B',11,17,0,0,TA_CENTER,BLUE)

def TH(t): return Paragraph(t,S('th','DV-B',9,13,0,0,TA_LEFT,WHITE))
def TD(t): return Paragraph(t,S('td','DV',9,13,0,0,TA_LEFT,DARK))
def TF(t): return Paragraph(t,S('tf','DV-M',9,13,0,0,TA_LEFT,DARK))
def TB(t): return Paragraph(t,S('tb','DV-B',9,13,0,0,TA_LEFT,BLUE))
def TR(t): return Paragraph(t,S('tr','DV-B',9,13,0,0,TA_LEFT,RED))

BASE_TS=[('BACKGROUND',(0,0),(-1,0),MID),('ROWBACKGROUNDS',(0,1),(-1,-1),[LGRY,WHITE]),
         ('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#bbb')),
         ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
         ('LEFTPADDING',(0,0),(-1,-1),7),('VALIGN',(0,0),(-1,-1),'MIDDLE')]

def mkt(rows,cols,extra=None):
    t=Table(rows,colWidths=cols,repeatRows=1)
    ts=list(BASE_TS)
    if extra: ts.extend(extra)
    t.setStyle(TableStyle(ts)); return t

def ibox(text,bg='#e8f4f8',bc=BLUE,fn='DV',fs=10,bold=False):
    fn2='DV-B' if bold else fn
    p=Paragraph(text,S('ib',fn2,fs,17,0,0,TA_CENTER if bold else TA_JUSTIFY,bc))
    t=Table([[p]],colWidths=[PW])
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1.5,bc),('BACKGROUND',(0,0),(-1,-1),colors.HexColor(bg)),
        ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14)]))
    return t

def H1(text):
    p=Paragraph(text,sH1); p._tocLevel=0; return p
def H2(text):
    p=Paragraph(text,sH2); p._tocLevel=1; return p

class T0Doc(BaseDocTemplate):
    def __init__(self,path,**kw):
        BaseDocTemplate.__init__(self,path,pagesize=A4,leftMargin=2.5*cm,
            rightMargin=2.5*cm,topMargin=2.5*cm,bottomMargin=2.5*cm,**kw)
        f=Frame(2.5*cm,2.5*cm,PW,A4[1]-5*cm,id='main')
        self.addPageTemplates([PageTemplate('main',[f])])
    def afterFlowable(self,flowable):
        lvl=getattr(flowable,'_tocLevel',None)
        if lvl is not None:
            self.notify('TOCEntry',(lvl,flowable.getPlainText(),self.page))

# ─── DATA ────────────────────────────────────────────────────────────────────
import math
xi_exp_me   = math.log(m_e/m_P)/math.log(xi)
xi_exp_a2   = math.log(alpha**2/2)/math.log(xi)
xi_exp_R    = xi_exp_me + xi_exp_a2

def build(lang):
    DE = (lang=='de')
    out = f'/mnt/user-data/outputs/T0_168_Periodensystem_xi_{"De" if DE else "En"}.pdf'
    title_main = ('Das Periodensystem als \u03be-Geometrie' if DE else
                  'The Periodic Table as \u03be-Geometry')
    title_sub  = ('Radiale Massenleiter und angulare Schalenstruktur aus einem gemeinsamen Ursprung' if DE else
                  'Radial Mass Ladder and Angular Shell Structure from a Common Origin')

    story=[]

    # TOC
    toc=TableOfContents(); toc.levelStyles=[sTOC1,sTOC2]; toc.dotsMinLevel=0
    story.append(Paragraph('Inhaltsverzeichnis' if DE else 'Table of Contents',sTOCH))
    story.append(Spacer(1,0.3*cm)); story.append(toc); story.append(PageBreak())

    # Title
    story.append(Paragraph('T0-Theorie / FFGFT \u2014 Dokument 168' if DE else 'T0 Theory / FFGFT \u2014 Document 168',sMeta))
    story.append(Spacer(1,0.2*cm))
    story.append(Paragraph(title_main,sTitle))
    story.append(Paragraph(title_sub,sSubT))
    story.append(Spacer(1,0.25*cm))
    story.append(Paragraph('Johann Pascher \u00b7 M\u00e4rz 2026' if DE else 'Johann Pascher \u00b7 March 2026',sMeta))
    story.append(HRFlowable(width=PW,thickness=2,color=DARK,spaceAfter=14))
    story.append(ibox(
        ('Kernaussage: Das Periodensystem liegt auf Stufe \u03be<super>7</super> der \u03be-Potenzleiter.<br/>'
         'Dieselbe Quantenzahl <i>n</i> indiziert die radiale Massenleiter m<sub>n</sub> \u223c \u03be<super>\u2212n</super>'
         ' und die angulare Schalenfüllung g<sub>n</sub> = 2n<super>2</super>.'
         ' Dualitätsprinzip: E<sub>n</sub> · g<sub>n</sub> = 2R<sub>\u221e</sub> = const') if DE else
        ('Core result: The periodic table lies on rung \u03be<super>7</super> of the \u03be-power ladder.<br/>'
         'The same quantum number <i>n</i> indexes the radial mass ladder m<sub>n</sub> \u223c \u03be<super>\u2212n</super>'
         ' and the angular shell filling g<sub>n</sub> = 2n<super>2</super>.'
         ' Duality: E<sub>n</sub> · g<sub>n</sub> = 2R<sub>\u221e</sub> = const'),
        bold=True,bg='#e8f4f8',bc=DARK,fs=11))
    story.append(Spacer(1,0.4*cm))

    # Abstract
    story.append(H1('Abstract' if DE else 'Abstract'))
    story.append(Paragraph(
        'Das Periodensystem der Elemente und die Teilchenmassen-Leiter der T0-Theorie teilen '
        'dieselbe geometrische Quantenzahl n, jedoch in verschiedenen Rollen. '
        'Die Teilchenmassen folgen einer <b>radialen</b> exponentiellen Skalierung '
        'm<sub>n</sub> \u223c \u03be<super>\u2212n</super> \u00b7 m<sub>P</sub>, '
        'während die Schalenstruktur einer <b>angularen</b> quadratischen Entartung '
        'g<sub>n</sub> = 2n<super>2</super> gehorcht. Beide entstehen aus der '
        'dreidimensionalen Gittergeometrie der T0-Theorie: \u03be ist das Packungsdefizit '
        'des 3D-Gitters (radiale Richtung), 2n<super>2</super> ist der Entartungsgrad '
        'der n-ten Kugelschale (angulare Richtung). Die Rydberg-Energie liegt auf '
        'Stufe \u03be<super>6,956</super> \u2248 \u03be<super>7</super> der \u03be-Leiter.' if DE else
        'The periodic table of the elements and the particle-mass ladder of T0 theory share '
        'the same geometric quantum number n, but in different roles. '
        'Particle masses follow a <b>radial</b> exponential scaling '
        'm<sub>n</sub> \u223c \u03be<super>\u2212n</super> \u00b7 m<sub>P</sub>, '
        'while the shell structure obeys an <b>angular</b> quadratic degeneracy '
        'g<sub>n</sub> = 2n<super>2</super>. Both arise from the three-dimensional '
        'lattice geometry of T0 theory: \u03be is the packing deficit of the 3D lattice '
        '(radial direction), 2n<super>2</super> is the degeneracy of the n-th spherical '
        'shell (angular direction). The Rydberg energy lies on rung '
        '\u03be<super>6.956</super> \u2248 \u03be<super>7</super> of the \u03be-ladder.',
        sBody))
    story.append(PageBreak())

    # ── 1. Einleitung ──────────────────────────────────────────────────────
    story.append(H1('1\u2002Einleitung und Fragestellung' if DE else '1\u2002Introduction and Problem Statement'))
    story.append(Paragraph(
        'Die T0-Theorie leitet alle physikalischen Konstanten aus dem geometrischen '
        'Parameter \u03be = 4/30\u2009000 = 1,333\u202f\u00d7\u202f10<super>\u22124</super> ab. '
        'Die Teilchenmassen des Standardmodells organisieren sich auf einer exponentiellen Leiter '
        'm<sub>n</sub> \u223c \u03be<super>\u2212n</super> \u00b7 m<sub>P</sub>, '
        'und das Periodensystem zeigt das Muster g<sub>n</sub> = 2n<super>2</super> '
        'für die Schalenkapazitäten.' if DE else
        'T0 theory derives all physical constants from the geometric parameter '
        '\u03be = 4/30\u2009000 = 1.333\u202f\u00d7\u202f10<super>\u22124</super>. '
        'The particle masses of the Standard Model organise on an exponential ladder '
        'm<sub>n</sub> \u223c \u03be<super>\u2212n</sup> \u00b7 m<sub>P</sub>, '
        'and the periodic table shows the pattern g<sub>n</sub> = 2n<super>2</super> '
        'for shell capacities.',sBody))
    story.append(Paragraph(
        ('<b>Fragestellung:</b> Das Periodensystem und die Teilchenmassen haben beide '
         'Quantenzahlen und Muster — aber die Skalierung ist grundverschieden: '
         'Teilchenmassen folgen einer <i>exponentiellen</i> ξ-Leiter, '
         'Schalenkapazitäten folgen einer <i>quadratischen</i> n<super>2</super>-Regel. '
         'Welcher gemeinsame geometrische Ursprung verbindet diese scheinbar unvereinbaren Muster? '
         '<b>Antwort:</b> Die T0-Geometrie hat zwei Achsen — eine radiale (\u03be<super>n</super>-Skalierung) '
         'und eine angulare (2n<super>2</super>-Entartung), beide aus der 3D-Gitterstruktur.') if DE else
        ('<b>Problem statement:</b> The periodic table and the particle masses both exhibit '
         'quantum numbers and patterns — but their scaling is fundamentally different: '
         'particle masses follow an <i>exponential</i> ξ-ladder, '
         'shell capacities follow a <i>quadratic</i> n<super>2</super> rule. '
         'What common geometric origin connects these apparently incompatible patterns? '
         '<b>Answer:</b> T0 geometry has two axes — a radial one (\u03be<super>n</super> scaling) '
         'and an angular one (2n<super>2</super> degeneracy), both from the 3D lattice structure.'),
        sBody))

    # ── 2. xi-Leiter ──────────────────────────────────────────────────────
    story.append(H1('2\u2002Die \u03be-Potenzleiter und ihre Stufen' if DE else
                    '2\u2002The \u03be-Power Ladder and Its Rungs'))
    story.append(Paragraph(
        'Tabelle\u202f1 zeigt die vollständige \u03be-Potenzleiter (Stand März 2026) '
        'inklusive der neuen atomaren Stufe.' if DE else
        'Table\u202f1 shows the complete \u03be-power ladder (as of March 2026) '
        'including the new atomic rung.',sBody))

    story.append(mkt([
        [TH('Verhältnis' if DE else 'Ratio'),
         TH('\u03be-Exponent des Verh.' if DE else '\u03be-exp. of ratio'),
         TH('Näherung' if DE else 'Approx.'),
         TH('Physikalischer Inhalt' if DE else 'Physical content'),
         TH('Dok.' if DE else 'Doc.')],
        [TD('m<sub>e</sub>/m<sub>\u03bc</sub>'),
         TF('\u03be<super>0,598</super>' if DE else '\u03be<super>0.598</super>'),
         TF('\u2248 \u03be<super>1/2</super>'),
         TD('Lepton-Massenverhältnis' if DE else 'Lepton mass ratio'), TD('041, 056')],
        [TD('m<sub>e</sub>/m<sub>\u03c4</sub>'),
         TF('\u03be<super>0,914</super>' if DE else '\u03be<super>0.914</super>'),
         TF('\u2248 \u03be<super>1</super>'),
         TD('Lepton-Massenverhältnis' if DE else 'Lepton mass ratio'), TD('056')],
        [TD('m<sub>\u03bc</sub>/m<sub>\u03c4</sub>'),
         TF('\u03be<super>0,316</super>' if DE else '\u03be<super>0.316</super>'),
         TF('\u2248 \u03be<super>1/3</super>'),
         TD('Lepton-Massenverhältnis' if DE else 'Lepton mass ratio'), TD('056')],
        [TD('m<sub>e</sub>/m<sub>P</sub>'),
         TF('\u03be<super>5,775</super>' if DE else '\u03be<super>5.775</super>'),
         TF('\u2248 \u03be<super>23/4</super>'),
         TD('Elektronmasse (absolut)' if DE else 'Electron mass (absolute)'), TD('056')],
        [TR('<b>R<sub>\u221e</sub>/m<sub>e</sub>c\u00b2</b>'),
         TR('\u03be<super>1,181</super>' if DE else '\u03be<super>1.181</super>'),
         TR('\u2248 \u03be<super>6/5</super>'),
         TR('<b>Atom\u2194Teilchen: \u03b1\u00b2/2 \u2248 \u03be</b>' if DE else
            '<b>Atom\u2194particle: \u03b1\u00b2/2 \u2248 \u03be</b>'), TR('<b>168</b>')],
        [TR('<b>R<sub>\u221e</sub>/m<sub>P</sub>c\u00b2</b>'),
         TR('\u03be<super>6,956</super>' if DE else '\u03be<super>6.956</super>'),
         TR('\u2248 \u03be<super>7</super>'),
         TR('<b>Rydberg-Skala (absolut) \u2192 Periodensystem</b>' if DE else
            '<b>Rydberg scale (absolute) \u2192 periodic table</b>'), TR('<b>168</b>')],
        [TD('H\u2080\u00b7\u210f/m<sub>e</sub>c\u00b2'),
         TF('\u03be<super>5,225</super>' if DE else '\u03be<super>5.225</super>'),
         TF('\u2248 \u03be<sup>5</sup>'),
         TD('Hubble-Verhältnis' if DE else 'Hubble ratio'), TD('165')],
    ],[3.5*cm,3.0*cm,2.5*cm,4.0*cm,1.7*cm],
       extra=[('BACKGROUND',(0,4),(-1,5),colors.HexColor('#ffe8e8'))]))
    story.append(Paragraph(
        ('Verhältnisse auf der \u03be-Leiter (analog zu Teilchenmassen-Verhältnissen). '
         'Rot hervorgehoben: die Schlüsselverhältnisse, die die atomare Skala (Periodensystem) erschließen.') if DE else
        ('Ratios on the \u03be-ladder (analogous to particle-mass ratios). '
         'Red: the key ratios that unlock the atomic scale (periodic table).'), sCap))

    story.append(Paragraph(
        'Die Rydberg-Energie liegt zwischen den Stufen 6 und 7:' if DE else
        'The Rydberg energy lies between rungs 6 and 7:',sBody))
    story.append(Paragraph(
        'R<sub>\u221e</sub> / E<sub>P</sub> = (m<sub>e</sub>/m<sub>P</sub>) \u00b7 (\u03b1\u00b2/2)'
        f' = \u03be<super>5,775</super> \u00b7 \u03be<super>1,181</super>'
        f' = \u03be<super>{xi_exp_R:.3f}</super>' if DE else
        'R<sub>\u221e</sub> / E<sub>P</sub> = (m<sub>e</sub>/m<sub>P</sub>) \u00b7 (\u03b1\u00b2/2)'
        f' = \u03be<super>5.775</super> \u00b7 \u03be<super>1.181</super>'
        f' = \u03be<super>{xi_exp_R:.3f}</super>',sEq))
    story.append(PageBreak())

    # ── 3. Zwei Achsen ─────────────────────────────────────────────────────
    story.append(H1('3\u2002Zwei Achsen der \u03be-Geometrie' if DE else '3\u2002Two Axes of \u03be-Geometry'))

    story.append(H2('3.1\u2002Radiale Achse: Exponentielle Massenleiter' if DE else
                    '3.1\u2002Radial Axis: Exponential Mass Ladder'))
    story.append(Paragraph(
        'Die Teilchenmassen organisieren sich auf der <b>radialen</b> Achse. '
        'Entscheidend sind die <b>Verhältnisse</b> benachbarter Massen — '
        'nicht der absolute Exponent einzelner Massen:' if DE else
        'Particle masses organise along the <b>radial</b> axis. '
        'The physically meaningful quantity is the <b>ratio</b> of consecutive masses — '
        'not the absolute exponent of a single mass:',sBody))
    story.append(mkt([
        [TH('Verhältnis' if DE else 'Ratio'),
         TH('Wert'),
         TH('\u03be-Exp. des Verh.' if DE else '\u03be-exp. of ratio'),
         TH('Näherung' if DE else 'Approx.'),
         TH('Quantenzahl\u0394n' if DE else '\u0394n')],
        [TD('m<sub>\u03bc</sub>/m<sub>e</sub>'), TD('206,8' if DE else '206.8'),
         TF('\u03be<super>\u22120,598</super>' if DE else '\u03be<super>\u22120.598</super>'),
         TF('\u2248 \u03be<super>\u22121/2</super>'), TD('\u0394n = \u00bd')],
        [TD('m<sub>\u03c4</sub>/m<sub>\u03bc</sub>'), TD('16,82' if DE else '16.82'),
         TF('\u03be<super>\u22120,316</super>' if DE else '\u03be<super>\u22120.316</super>'),
         TF('\u2248 \u03be<super>\u22121/3</super>'), TD('\u0394n = \u2153')],
        [TD('m<sub>\u03c4</sub>/m<sub>e</sub>'), TD('3477'),
         TF('\u03be<super>\u22120,914</super>' if DE else '\u03be<super>\u22120.914</super>'),
         TF('\u2248 \u03be<super>\u22121</super>'), TD('\u0394n = 1')],
        [TD('m<sub>c</sub>/m<sub>s</sub> (Quarks)'), TD('13,4'),
         TF('\u03be<super>\u22120,280</super>' if DE else '\u03be<super>\u22120.280</super>'),
         TF('\u2248 \u03be<super>\u22121/4</super>'), TD('\u0394n = \u00bc')],
        [TD('m<sub>t</sub>/m<sub>b</sub> (Quarks)'), TD('41,4'),
         TF('\u03be<super>\u22120,417</super>' if DE else '\u03be<super>\u22120.417</super>'),
         TF('\u2248 \u03be<super>\u22125/12</super>'), TD('\u0394n \u2248 5/12')],
    ],[3.8*cm,2.2*cm,3.2*cm,3.0*cm,2.0*cm]))
    story.append(Paragraph(
        ('Teilchenmassen-Verhältnisse auf der radialen \u03be-Achse. '
         'Das Verhältnis m<sub>\u03bc</sub>/m<sub>e</sub> \u2248 \u03be<super>\u22121/2</super> '
         'entspricht der Halbstufe — dem elektroschwachen Exponenten (Dok.\u202f041, 167).') if DE else
        ('Particle-mass ratios on the radial \u03be-axis. '
         'The ratio m<sub>\u03bc</sub>/m<sub>e</sub> \u2248 \u03be<super>\u22121/2</super> '
         'corresponds to the half-rung — the electroweak exponent (Doc.\u202f041, 167).'), sCap))

    story.append(H2('3.2\u2002Angulare Achse: Quadratische Entartungsleiter' if DE else
                    '3.2\u2002Angular Axis: Quadratic Degeneracy Ladder'))
    story.append(Paragraph(
        'Die <b>angulare</b> Achse bestimmt die Entartungsgrade. '
        'Analog zu den Massenverhältnissen zeigen die <b>Schalen-Verhältnisse</b> '
        'die Quantenzahl-Struktur — jedoch <i>rational</i> (nicht exponentiell):' if DE else
        'The <b>angular</b> axis determines the degeneracies. '
        'Analogous to the mass ratios, the <b>shell ratios</b> show the quantum-number '
        'structure — but they are <i>rational</i> (not exponential):',sBody))
    story.append(mkt([
        [TH('Verhältnis' if DE else 'Ratio'),
         TH('Wert'),
         TH('Rationaler Ausdruck' if DE else 'Rational expression'),
         TH('\u03be-Exp. (nur f. Vergl.)' if DE else '\u03be-exp. (comparison only)'),
         TH('Bedeutung' if DE else 'Meaning')],
        [TD('g<sub>2</sub>/g<sub>1</sub>'), TD('8/2 = 4'),   TF('(2/1)\u00b2 = 4'),   TF('\u03be<super>\u22120,155</super>' if DE else '\u03be<super>\u22120.155</super>'), TD('n=1\u2192n=2')],
        [TD('g<sub>3</sub>/g<sub>1</sub>'), TD('18/2 = 9'),  TF('(3/1)\u00b2 = 9'),  TF('\u03be<super>\u22120,246</super>' if DE else '\u03be<super>\u22120.246</super>'), TD('n=1\u2192n=3')],
        [TD('g<sub>4</sub>/g<sub>1</sub>'), TD('32/2 = 16'), TF('(4/1)\u00b2 = 16'), TF('\u03be<super>\u22120,311</super>' if DE else '\u03be<super>\u22120.311</super>'), TD('n=1\u2192n=4')],
        [TD('g<sub>3</sub>/g<sub>2</sub>'), TD('18/8 = 9/4'), TF('(3/2)\u00b2 = 9/4'), TF('\u03be<super>\u22120,091</super>' if DE else '\u03be<super>\u22120.091</super>'), TD('n=2\u2192n=3')],
        [TD('g<sub>4</sub>/g<sub>2</sub>'), TD('32/8 = 4'),   TF('(4/2)\u00b2 = 4'),   TF('\u03be<super>\u22120,155</super>' if DE else '\u03be<super>\u22120.155</super>'), TD('n=2\u2192n=4')],
    ],[3.2*cm,2.5*cm,3.0*cm,3.0*cm,2.5*cm]))
    story.append(Paragraph(
        ('g<sub>n</sub>/g<sub>m</sub> = (n/m)\u00b2 — immer ein rationaler Bruch. '
         'Das ist der Unterschied zur radialen Achse: Massenverhältnisse sind \u03be-Potenzen (irrational), '
         'Schalenverhältnisse sind Quadrate ganzer Zahlen (rational).') if DE else
        ('g<sub>n</sub>/g<sub>m</sub> = (n/m)\u00b2 — always a rational fraction. '
         'This is the difference from the radial axis: mass ratios are \u03be-powers (irrational), '
         'shell ratios are squares of integers (rational).'), sCap))

    story.append(H2('3.3\u2002Die Verbindung durch die Quantenzahl n' if DE else
                    '3.3\u2002The Connection through Quantum Number n'))
    story.append(Paragraph(
        'Dieselbe Quantenzahl n erscheint in beiden Systemen. '
        'Das <b>zentrale strukturelle Ergebnis</b>: die Massenverhältnisse sind '
        '\u03be-Potenzen, die Schalenverhältnisse sind rationale Quadrate — '
        'aber <b>beide nutzen denselben Radius-Index n</b>.' if DE else
        'The same quantum number n appears in both systems. '
        'The <b>central structural result</b>: mass ratios are \u03be-powers, '
        'shell ratios are rational squares — but <b>both use the same radius index n</b>.',sBody))
    story.append(mkt([
        [TH('System'), TH('Verhältnis' if DE else 'Ratio'),
         TH('Ausdruck' if DE else 'Expression'),
         TH('Typ'), TH('Achse' if DE else 'Axis')],
        [TD('Teilchenmassen' if DE else 'Particle masses'),
         TD('m<sub>\u03bc</sub>/m<sub>e</sub>'),
         TF('\u03be<super>\u22121/2</super> \u2248 0,012' if DE else '\u03be<super>\u22121/2</super> \u2248 0.012'),
         TD('irrational, \u03be-Potenz' if DE else 'irrational, \u03be-power'), TD('radial')],
        [TD('Teilchenmassen' if DE else 'Particle masses'),
         TD('m<sub>\u03c4</sub>/m<sub>e</sub>'),
         TF('\u03be<super>\u22121</super> \u2248 0,00013' if DE else '\u03be<super>\u22121</super> \u2248 0.00013'),
         TD('irrational, \u03be-Potenz' if DE else 'irrational, \u03be-power'), TD('radial')],
        [TD('Schalenfüllung' if DE else 'Shell filling'),
         TD('g<sub>2</sub>/g<sub>1</sub>'),
         TF('(2/1)\u00b2 = 4'),
         TD('rational, n\u00b2-Folge' if DE else 'rational, n\u00b2 sequence'), TD('angular')],
        [TD('Schalenfüllung' if DE else 'Shell filling'),
         TD('g<sub>3</sub>/g<sub>2</sub>'),
         TF('(3/2)\u00b2 = 9/4'),
         TD('rational, n\u00b2-Folge' if DE else 'rational, n\u00b2 sequence'), TD('angular')],
        [TD('Schalenenergie' if DE else 'Shell energy'),
         TD('E<sub>2</sub>/E<sub>1</sub>'),
         TF('(1/2)\u00b2 = 1/4'),
         TD('rational, 1/n\u00b2-Folge' if DE else 'rational, 1/n\u00b2 sequence'), TD('angular')],
    ],[3.5*cm,2.8*cm,3.5*cm,3.2*cm,1.8*cm]))
    story.append(Paragraph(
        ('Der Typ unterscheidet die Achsen: irrational (\u03be-Potenz) = radial, '
         'rational (Bruch) = angular. Beide Achsen teilen denselben Index n.') if DE else
        ('The type distinguishes the axes: irrational (\u03be-power) = radial, '
         'rational (fraction) = angular. Both axes share the same index n.'), sCap))
    story.append(PageBreak())

    # ── 4. Dualitätsprinzip ────────────────────────────────────────────────
    story.append(H1('4\u2002Das Dualitätsprinzip' if DE else '4\u2002The Duality Principle'))
    story.append(Paragraph(
        'Auf der atomaren Skala (wasserstoffähnlich) gilt:' if DE else
        'On the atomic scale (hydrogen-like):',sBody))

    story.append(mkt([
        [TH('n'), TH('E<sub>n</sub> (eV)'), TH('g<sub>n</sub> = 2n\u00b2'),
         TH('E<sub>n</sub> \u00b7 g<sub>n</sub> (eV)'), TH('= 2R<sub>\u221e</sub>?')],
        [TD('1'), TD('13,600' if DE else '13.600'), TD('2'),  TD('27,200' if DE else '27.200'), TD('\u2713 exakt' if DE else '\u2713 exact')],
        [TD('2'), TD('3,400' if DE else '3.400'),   TD('8'),  TD('27,200' if DE else '27.200'), TD('\u2713 exakt' if DE else '\u2713 exact')],
        [TD('3'), TD('1,511' if DE else '1.511'),   TD('18'), TD('27,200' if DE else '27.200'), TD('\u2713 exakt' if DE else '\u2713 exact')],
        [TD('4'), TD('0,850' if DE else '0.850'),   TD('32'), TD('27,200' if DE else '27.200'), TD('\u2713 exakt' if DE else '\u2713 exact')],
        [TD('n'), TF('R<sub>\u221e</sub>/n<super>2</super>'), TF('2n<super>2</super>'),
         TF('2R<sub>\u221e</sub>'), TD('\u2713 allgemein' if DE else '\u2713 general')],
    ],[1.2*cm,3.0*cm,3.0*cm,3.8*cm,3.2*cm],
       extra=[('BACKGROUND',(0,5),(-1,5),colors.HexColor('#fff0cc'))]))
    story.append(Spacer(1,0.3*cm))
    story.append(ibox(
        'E<sub>n</sub> \u00b7 g<sub>n</sub> = (R<sub>\u221e</sub>/n<super>2</super>) \u00b7 (2n<super>2</super>) = 2R<sub>\u221e</sub> = const<br/>'
        + ('Geometrische Äquipartition: Jede Schale trägt dieselbe Gesamtenergie 2R<sub>\u221e</sub>.' if DE else
           'Geometric equipartition: every shell contributes the same total energy 2R<sub>\u221e</sub>.'),
        bold=True,bg='#fff8e1',bc=MID,fs=12))
    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        'Dies ist kein Zufall: E<sub>n</sub>\u00b7g<sub>n</sub> = const ist eine <b>geometrische Äquipartition</b> '
        'der Energie über alle Zustände einer Schale. '
        'Die 1/n<super>2</super>-Energieleiter und die n<super>2</super>-Füllleiter sind <b>invers dual</b>.' if DE else
        'This is not coincidental: E<sub>n</sub>\u00b7g<sub>n</sub> = const is a <b>geometric equipartition</b> '
        'of energy over all states of a shell. '
        'The 1/n<super>2</super> energy ladder and the n<super>2</super> filling ladder are <b>inversely dual</b>.',sBody))
    story.append(PageBreak())

    # ── 5. Fraktale Dimension ──────────────────────────────────────────────
    story.append(H1('5\u2002Die Rolle der fraktalen Dimension' if DE else '5\u2002The Role of Fractal Dimension'))
    story.append(Paragraph(
        'In T0 gilt (Dok.\u202f009, 133): D<sub>f</sub> = 3 \u2212 \u03be = 2,999867. '
        'Der Raum ist fast, aber nicht exakt 3-dimensional.' if DE else
        'In T0 (Doc.\u202f009, 133): D<sub>f</sub> = 3 \u2212 \u03be = 2.999867. '
        'Space is almost, but not exactly, 3-dimensional.',sBody))
    story.append(mkt([
        [TH('D<sub>f</sub>-Grenzfall' if DE else 'D<sub>f</sub> limit'),
         TH('Konsequenz für g<sub>n</sub>' if DE else 'Consequence for g<sub>n</sub>'),
         TH('Bedeutung' if DE else 'Meaning')],
        [TD('D<sub>f</sub> \u2192 3 (\u03be \u2192 0)'),
         TD('g<sub>n</sub> = 2n\u00b2 <b>exakt</b>'),
         TD('Reine Kugelsymmetrie im \u2124\u00b3-Gitter' if DE else 'Pure spherical symmetry in \u2124\u00b3 lattice')],
        [TD('D<sub>f</sub> = 3 \u2212 \u03be = 2,9999' if DE else 'D<sub>f</sub> = 3 \u2212 \u03be = 2.9999'),
         TD('\u03b4g<sub>n</sub> \u223c \u03be\u00b7n\u00b2 \u2248 10<super>\u22124</super>'),
         TD('Vernachlässigbare Korrektur' if DE else 'Negligible correction')],
        [TD('T0-Realität' if DE else 'T0 reality'),
         TD('2n\u00b2 exakt auf 4 Dezimalstellen' if DE else '2n\u00b2 exact to 4 decimal places'),
         TD('Periodensystem ist geometrisch exakt' if DE else 'Periodic table is geometrically exact')],
    ],[4.2*cm,4.5*cm,5.5*cm]))
    story.append(Paragraph(
        'Das Periodensystem ist exakt, weil D<sub>f</sub> \u2248 3 auf 4 Dezimalstellen. '
        'Die winzige Abweichung \u03be \u2248 1,3\u202f\u00d7\u202f10<super>\u22124</super> '
        'generiert die gesamte Teilchenphysik — lässt aber das Periodensystem unberührt.' if DE else
        'The periodic table is exact because D<sub>f</sub> \u2248 3 to 4 decimal places. '
        'The tiny deviation \u03be \u2248 1.3\u202f\u00d7\u202f10<super>\u22124</super> '
        'generates all of particle physics — but leaves the periodic table intact.',sBody))

    # ── 6. Numerik ─────────────────────────────────────────────────────────
    story.append(H1('6\u2002Numerische Überprüfung' if DE else '6\u2002Numerical Verification'))
    me_mp = m_e/m_P; a2_2 = alpha**2/2
    story.append(mkt([
        [TH('Größe' if DE else 'Quantity'), TH('Wert' if DE else 'Value'), TH('\u03be-Exponent')],
        [TD('m<sub>e</sub> / m<sub>P</sub>'),    TF(f'{me_mp:.4e}'), TF(f'{xi_exp_me:.4f}')],
        [TD('\u03b1\u00b2 / 2'),                  TF(f'{a2_2:.4e}'),  TF(f'{xi_exp_a2:.4f}')],
        [TD('R<sub>\u221e</sub> / E<sub>P</sub>'),TF(f'{me_mp*a2_2:.4e}'),TF(f'{xi_exp_R:.4f}')],
        [TD('R<sub>\u221e</sub> (T0, Näherung \u03be\u2077)' if DE else 'R<sub>\u221e</sub> (T0, approx. \u03be\u2077)'),
         TD(f'\u2248 {xi**7*E_P:.2f} eV'), TF('7,000' if DE else '7.000')],
        [TB('<b>R<sub>\u221e</sub> (gemessen)</b>' if DE else '<b>R<sub>\u221e</sub> (measured)</b>'),
         TB(f'<b>{R_inf:.4f} eV</b>'), TB(f'<b>{xi_exp_R:.4f}</b>')],
    ],[5.5*cm,4.0*cm,4.7*cm],
       extra=[('BACKGROUND',(0,5),(-1,5),colors.HexColor('#ddeeff'))]))
    story.append(Paragraph(
        f'R\u221e/E_P = \u03be\u207b\u2076\u2027\u2079\u2075\u2076: Die Rydberg-Energie liegt auf Stufe 6,956 \u2248 7 der \u03be-Leiter.' if DE else
        f'R\u221e/E_P = \u03be\u207b\u2076\u2027\u2079\u2035\u2076: The Rydberg energy lies on rung 6.956 \u2248 7 of the \u03be-ladder.', sCap))
    story.append(PageBreak())

    # ── 7. Hierarchie ──────────────────────────────────────────────────────
    story.append(H1('7\u2002Das Periodensystem in der T0-Hierarchie' if DE else
                    '7\u2002The Periodic Table in the T0 Hierarchy'))
    story.append(mkt([
        [TH('\u03be-Stufe' if DE else '\u03be-Rung'), TH('Physik' if DE else 'Physics'), TH('Achse' if DE else 'Axis')],
        [TD('\u03be\u2070 = 1'),
         TD('Planck-Skala (L\u2080 = \u03be\u00b7\u2113<sub>P</sub>)' if DE else 'Planck scale (L\u2080 = \u03be\u00b7\u2113<sub>P</sub>)'), TD('\u2014')],
        [TD('\u03be<super>1/2</super>'),
         TD('Elektroschwach: \u03b1<sub>W</sub>, m<sub>e</sub>/m<sub>\u03bc</sub>' if DE else 'Electroweak: \u03b1<sub>W</sub>, m<sub>e</sub>/m<sub>\u03bc</sub>'), TD('radial')],
        [TD('\u03be<super>1</super>'),
         TD('\u03b1<sub>EM</sub>, EM-Kopplung' if DE else '\u03b1<sub>EM</sub>, EM coupling'), TD('radial')],
        [TD('\u03be<super>4</super>'),
         TD('CMB-Temperatur T<sub>CMB</sub>' if DE else 'CMB temperature T<sub>CMB</sub>'), TD('radial')],
        [TD('\u03be<super>4,9–5,8</super>' if DE else '\u03be<super>4.9–5.8</super>'),
         TD('Teilchenmassen: Leptonen, Quarks' if DE else 'Particle masses: leptons, quarks'), TD('radial')],
        [TR('\u03be<super>6,956</super>' if DE else '\u03be<super>6.956</super>'),
         TR('<b>Rydberg R<sub>\u221e</sub>, Periodensystem 2n\u00b2</b>' if DE else
            '<b>Rydberg R<sub>\u221e</sub>, periodic table 2n\u00b2</b>'),
         TR('<b>radial + angular</b>')],
        [TD('\u03be<super>10</super>'),
         TD('Hubble-Konstante H\u2080' if DE else 'Hubble constant H\u2080'), TD('radial')],
    ],[2.5*cm,8.5*cm,3.2*cm],
       extra=[('BACKGROUND',(0,6),(-1,6),colors.HexColor('#ffe8e8'))]))
    story.append(Paragraph(
        'Die atomare Stufe \u03be\u2077 ist die einzige, auf der beide Achsen gleichzeitig wirken. '
        'Das Periodensystem ist der angulare Querschnitt (2n\u00b2), die Teilchenmassen der radiale Querschnitt (\u03be<super>\u2212n</super>).' if DE else
        'The atomic rung \u03be\u2077 is the only one where both axes act simultaneously. '
        'The periodic table is the angular cross-section (2n\u00b2), the particle masses are the radial cross-section (\u03be<super>\u2212n</super>).',sCap))
    story.append(PageBreak())

    # ── 8. Zusammenfassung ─────────────────────────────────────────────────
    story.append(H1('8\u2002Zusammenfassung' if DE else '8\u2002Summary'))
    if DE:
        points = [
            '<b>Energieskala:</b> R<sub>\u221e</sub>/E<sub>P</sub> = \u03be<super>6,956</super> \u2248 \u03be<super>7</super>. '
            'Die Rydberg-Energie — und damit die gesamte Atomphysik — liegt auf Stufe\u202f7 der \u03be-Potenzleiter.',
            '<b>Radiale Achse:</b> Teilchenmassen folgen m<sub>n</sub> \u223c \u03be<super>\u2212n</super> \u00b7 m<sub>P</sub>. '
            'Der Exponent n ist der diskrete Gitterradius in der radialen \u03be-Richtung.',
            '<b>Angulare Achse:</b> Schalenkapazitäten folgen g<sub>n</sub> = 2n<super>2</super>. '
            'Der Index n ist derselbe Gitterradius, jetzt als Schalen-Index in der angularen 3D-Sphären-Richtung.',
            '<b>Dualitätsprinzip:</b> E<sub>n</sub>\u00b7g<sub>n</sub> = 2R<sub>\u221e</sub> = const. '
            'Die 1/n<super>2</super>-Energieleiter und die n<super>2</super>-Füllleiter sind invers dual. '
            'Jede Schale trägt dieselbe Gesamtenergie 2R<sub>\u221e</sub>.',
            '<b>Fraktale Dimension:</b> D<sub>f</sub> = 3 \u2212 \u03be \u2248 3 macht 2n<super>2</super> exakt '
            '(auf \u223c10<super>\u22124</super>). Das Periodensystem ist exakt, weil der Raum fast-ganzzahlig-dimensional ist.',
            '<b>Gemeinsamer Ursprung:</b> Teilchenmassen und Periodensystem entstehen aus derselben '
            '3D-Gittergeometrie mit Packungsdefizit \u03be. Das Periodensystem ist der <i>angulare Querschnitt</i> '
            'der \u03be-Geometrie auf Stufe \u03be<super>\u223c7</super>; die Leptonmassen sind der <i>radiale Querschnitt</i> '
            'auf Stufen \u03be<super>4,9</super>–\u03be<super>5,8</super>.',
        ]
    else:
        points = [
            '<b>Energy scale:</b> R<sub>\u221e</sub>/E<sub>P</sub> = \u03be<super>6.956</super> \u2248 \u03be<super>7</super>. '
            'The Rydberg energy — and hence all of atomic physics — lies on rung\u202f7 of the \u03be-power ladder.',
            '<b>Radial axis:</b> Particle masses follow m<sub>n</sub> \u223c \u03be<super>\u2212n</super> \u00b7 m<sub>P</sub>. '
            'The exponent n is the discrete lattice radius in the radial \u03be-direction.',
            '<b>Angular axis:</b> Shell capacities follow g<sub>n</sub> = 2n<super>2</super>. '
            'The index n is the same discrete lattice radius, now acting as a shell index in the angular 3D-sphere direction.',
            '<b>Duality principle:</b> E<sub>n</sub>\u00b7g<sub>n</sub> = 2R<sub>\u221e</sub> = const. '
            'The 1/n<super>2</super> energy ladder and the n<super>2</super> filling ladder are inversely dual. '
            'Every shell contributes the same total energy 2R<sub>\u221e</sub>.',
            '<b>Fractal dimension:</b> D<sub>f</sub> = 3 \u2212 \u03be \u2248 3 makes 2n<super>2</super> exact '
            '(to \u223c10<super>\u22124</super>). The periodic table is exact because space is almost-integer-dimensional.',
            '<b>Common origin:</b> Particle masses and the periodic table arise from the same '
            '3D lattice geometry with packing deficit \u03be. The periodic table is the <i>angular cross-section</i> '
            'of \u03be-geometry at rung \u03be<super>\u223c7</super>; the lepton masses are the <i>radial cross-section</i> '
            'at rungs \u03be<super>4.9</super>–\u03be<super>5.8</super>.',
        ]
    for i,txt in enumerate(points,1):
        story.append(Paragraph(f'{i}.\u2002{txt}',S(f'p{i}',sa=5,li=10)))

    story.append(Spacer(1,0.5*cm))
    story.append(HRFlowable(width=PW,thickness=1,color=GRY,spaceAfter=8))
    story.append(ibox(
        ('<b>Offenes Forschungsprogramm:</b> (1) Angulare \u03be-Korrekturen g<sub>n</sub><super>(T0)</super> = 2n\u00b2\u00b7(1\u2212\u03be\u00b7f(n)) ableiten. '
         '(2) Molekulare Bindungsenergien auf rationalen Vielfachen von \u03be<super>7/2</super>\u00b7R<sub>\u221e</sub> prüfen. '
         '(3) Ionisierungsenergien schwerer Elemente (Z > 54) auf der Halbstufe \u03be<super>13/2</super> analysieren.') if DE else
        ('<b>Open research programme:</b> (1) Derive angular \u03be-corrections g<sub>n</sub><super>(T0)</super> = 2n\u00b2\u00b7(1\u2212\u03be\u00b7f(n)). '
         '(2) Test molecular binding energies for rational multiples of \u03be<super>7/2</super>\u00b7R<sub>\u221e</sub>. '
         '(3) Analyse ionisation energies of heavy elements (Z > 54) at the half-rung \u03be<super>13/2</super>.'),
        bg='#f0fff0',bc=GRN,fn='DV',fs=10))
    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        ('<b>Verwandte Dokumente:</b> 009 (\u03be-Ursprung) \u00b7 011 (\u03b1<sub>EM</sub>) \u00b7 '
         '041 (\u03b1<sub>W</sub> = \u03be<super>1/2</super>) \u00b7 056 (Leptonmassen) \u00b7 '
         '122 (m<sub>e</sub>/m<sub>\u03bc</sub>) \u00b7 133 (K<sub>frak</sub>) \u00b7 '
         '165 (H\u2080-Verhältnis) \u00b7 166 (Casimir-CMB-H\u2080) \u00b7 167 (LiNbO\u2083)') if DE else
        ('<b>Related documents:</b> 009 (\u03be origin) \u00b7 011 (\u03b1<sub>EM</sub>) \u00b7 '
         '041 (\u03b1<sub>W</sub> = \u03be<super>1/2</super>) \u00b7 056 (lepton masses) \u00b7 '
         '122 (m<sub>e</sub>/m<sub>\u03bc</sub>) \u00b7 133 (K<sub>frak</sub>) \u00b7 '
         '165 (H\u2080 ratio) \u00b7 166 (Casimir-CMB-H\u2080) \u00b7 167 (LiNbO\u2083)'),
        S('ref',fs=9,sa=0,al=TA_LEFT,tc=GRY)))

    doc=T0Doc(out,
        title=f'T0 Dok.168: Periodensystem als xi-Geometrie' if DE else 'T0 Doc.168: Periodic Table as xi-Geometry',
        author='Johann Pascher')
    doc.multiBuild(story)
    print(f'{"DE" if DE else "EN"} PDF OK → {out}')

build('de')
build('en')
