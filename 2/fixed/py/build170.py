"""
T0-Theorie / FFGFT – Dokument 170
Analoge Vorverarbeitung als Rechenprinzip:
Das Gehör, die Cochlea und hybride photonische Systeme
Johann Pascher, März 2026
"""
import math
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, PageBreak, Image)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

BASE = '/usr/share/fonts/truetype/dejavu/'
for nm, fp in [('DV','DejaVuSans.ttf'),('DV-B','DejaVuSans-Bold.ttf'),
               ('DV-I','DejaVuSans-Oblique.ttf'),('DV-M','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(nm, BASE+fp))

PW = A4[0]-5*cm

DARK = colors.HexColor('#1a1a2e')
MID  = colors.HexColor('#16213e')
BLUE = colors.HexColor('#0f3460')
GRY  = colors.HexColor('#888888')
GRN  = colors.HexColor('#1a6b1a')
LGRY = colors.HexColor('#f0f4f8')
TEAL = colors.HexColor('#006b6b')
ORG  = colors.HexColor('#7a3800')
WHITE= colors.white

def S(name,fn='DV',fs=10,ld=15,sb=0,sa=6,al=TA_JUSTIFY,tc=None,li=0,ri=0):
    return ParagraphStyle(name,fontName=fn,fontSize=fs,leading=ld,
        spaceBefore=sb,spaceAfter=sa,alignment=al,
        textColor=tc or DARK,leftIndent=li,rightIndent=ri)

sTitle = S('TI','DV-B',17,23,0,4,TA_CENTER)
sSubT  = S('ST','DV-I',11,16,0,4,TA_CENTER,colors.HexColor('#444'))
sMeta  = S('ME','DV-I',9,13,0,6,TA_CENTER,GRY)
sH1    = S('H1','DV-B',12,17,18,5,TA_LEFT,MID)
sH2    = S('H2','DV-B',10,14,10,4,TA_LEFT,BLUE)
sH3    = S('H3','DV-B',10,14,6,3,TA_LEFT,TEAL)
sBody  = S('BO','DV',10,15.5,0,6)
sQuote = S('QU','DV-I',10,15,6,6,TA_JUSTIFY,DARK,li=18,ri=18)
sCap   = S('CA','DV-I',9,13,2,6,TA_CENTER,GRY)
sTOCH  = S('TCH','DV-B',13,18,0,10,TA_LEFT,MID)
sTOC1  = S('TC1','DV-B',10,14,2,2,TA_LEFT,DARK)
sTOC2  = S('TC2','DV',9,13,1,1,TA_LEFT,DARK,li=12)
sBullet= S('BU','DV',10,15,0,3,TA_JUSTIFY,DARK,li=14)

def TH(t): return Paragraph(t,S('th','DV-B',9,13,0,0,TA_LEFT,WHITE))
def TD(t): return Paragraph(t,S('td','DV',9,13,0,0,TA_LEFT,DARK))
def TI(t): return Paragraph(t,S('ti','DV-I',9,13,0,0,TA_LEFT,DARK))
def TB(t): return Paragraph(t,S('tb','DV-B',9,13,0,0,TA_LEFT,TEAL))
def TF(t): return Paragraph(t,S('tf','DV-M',9,13,0,0,TA_LEFT,DARK))

BASE_TS = [
    ('BACKGROUND',(0,0),(-1,0),MID),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[LGRY,WHITE]),
    ('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#bbb')),
    ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
    ('LEFTPADDING',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP'),
]

def mkt(rows,cols,extra=None):
    t = Table(rows,colWidths=cols,repeatRows=1)
    ts = list(BASE_TS)
    if extra: ts.extend(extra)
    t.setStyle(TableStyle(ts)); return t

def ibox(text, bg='#e8f4f8', bc=BLUE, fs=10, italic=False):
    fn = 'DV-I' if italic else 'DV'
    p = Paragraph(text, S('ib',fn,fs,16,0,0,TA_JUSTIFY,bc))
    t = Table([[p]], colWidths=[PW])
    t.setStyle(TableStyle([
        ('BOX',(0,0),(-1,-1),1.5,bc),
        ('BACKGROUND',(0,0),(-1,-1),colors.HexColor(bg)),
        ('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12),
        ('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),16),
    ]))
    return t

def bullet(text):
    return Paragraph(f'\u2022\u2002{text}', sBullet)

def H1(text):
    p = Paragraph(text, sH1); p._tocLevel=0; return p
def H2(text):
    p = Paragraph(text, sH2); p._tocLevel=1; return p
def H3(text):
    p = Paragraph(text, S('h3s','DV-B',10,14,6,3,TA_LEFT,TEAL)); return p

class T0Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
            leftMargin=2.5*cm, rightMargin=2.5*cm,
            topMargin=2.5*cm, bottomMargin=2.5*cm, **kw)
        f = Frame(2.5*cm, 2.5*cm, PW, A4[1]-5*cm, id='main')
        self.addPageTemplates([PageTemplate('main',[f])])
    def afterFlowable(self, flowable):
        lvl = getattr(flowable,'_tocLevel',None)
        if lvl is not None:
            self.notify('TOCEntry',(lvl,flowable.getPlainText(),self.page))


def build(lang):
    DE = (lang == 'de')
    out = f'/mnt/user-data/outputs/T0_170_Analog_Gehoer_{"De" if DE else "En"}.pdf'

    story = []

    # ── TOC ──────────────────────────────────────────────────────────────
    toc = TableOfContents(); toc.levelStyles=[sTOC1,sTOC2]; toc.dotsMinLevel=0
    story.append(Paragraph('Inhaltsverzeichnis' if DE else 'Table of Contents', sTOCH))
    story.append(Spacer(1,0.3*cm)); story.append(toc); story.append(PageBreak())

    # ── Titelseite ────────────────────────────────────────────────────────
    story.append(Paragraph(
        'Dokument 170' if DE else 'Document 170', sMeta))
    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        'Analoge Vorverarbeitung als Rechenprinzip' if DE else
        'Analogue Pre-processing as a Computational Principle', sTitle))
    story.append(Paragraph(
        'Das Gehör, die Cochlea und hybride photonische Systeme' if DE else
        'The Auditory System, the Cochlea, and Hybrid Photonic Systems', sSubT))
    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        'Johann Pascher \u00b7 M\u00e4rz 2026' if DE else
        'Johann Pascher \u00b7 March 2026', sMeta))
    story.append(HRFlowable(width=PW, thickness=2, color=DARK, spaceAfter=16))

    story.append(ibox(
        ('<b>Kernthese:</b> Die anhaltende \u00dcberlegenheit des biologischen Geh\u00f6rs '
         'gegen\u00fcber digitalen Systemen in bestimmten Aufgaben '
         '(Cocktailpartyproblem, transiente Ereignisse, Quelltrennung) '
         'hat eine strukturelle Ursache: Das Geh\u00f6r nutzt physikalische '
         'Relaxation als Rechenprinzip. Die Cochlea l\u00f6st die Spektralzerlegung, '
         'weil ihre Mechanik so beschaffen ist \u2014 nicht weil etwas berechnet wird. '
         'Dasselbe Prinzip liegt Coherent Ising Machines und hybrider Photonik '
         'zugrunde. Dies er\u00f6ffnet einen neuen Entwurfsraum f\u00fcr '
         'Audioverarbeitungssysteme.') if DE else
        ('<b>Core thesis:</b> The persistent superiority of the biological auditory '
         'system over digital systems in certain tasks '
         '(cocktail-party problem, transient events, source separation) '
         'has a structural cause: the auditory system uses physical '
         'relaxation as a computational principle. The cochlea performs '
         'spectral decomposition because its mechanics are so constructed '
         '\u2014 not because something is calculated. '
         'The same principle underlies Coherent Ising Machines and hybrid photonics. '
         'This opens a new design space for audio processing systems.'),
        bg='#e8f4f8', bc=DARK, fs=10))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════
    # Kapitel 1: Einleitung
    # ══════════════════════════════════════════════════════════════════════
    story.append(H1(
        '1\u2002Einleitung: Das Rechnen vor dem Rechnen' if DE else
        '1\u2002Introduction: Computing Before Computing'))

    # 1.1
    story.append(H2(
        '1.1\u2002Eine Beobachtung \u00fcber mehrere Jahrzehnte' if DE else
        '1.1\u2002An Observation Spanning Several Decades'))
    story.append(Paragraph(
        ('Wer sich \u00fcber Jahrzehnte mit der digitalen Analyse von Tonsignalen besch\u00e4ftigt, '
         'st\u00f6\u00dft unweigerlich auf eine hartn\u00e4ckige Diskrepanz: Die F\u00e4higkeit '
         'eines Menschen \u2014 oder eines Tieres \u2014 Kl\u00e4nge in Bruchteilen einer '
         'Sekunde zu unterscheiden, einzuordnen, aus \u00fcberlagerten Signalen herauszul\u00f6sen '
         'und auf ihren Ursprung zur\u00fcckzuf\u00fchren, wird von digitalen Systemen trotz '
         'enormer Fortschritte in Rechenleistung und Datenmengen nicht vollst\u00e4ndig erreicht.') if DE else
        ('Anyone who has worked with digital audio signal analysis over several decades '
         'inevitably encounters a persistent discrepancy: the ability of a human \u2014 '
         'or an animal \u2014 to distinguish sounds in fractions of a second, to classify them, '
         'to isolate them from overlapping signals and trace them to their source, '
         'is not fully matched by digital systems despite enormous advances in '
         'computing power and data volume.'), sBody))

    story.append(Paragraph(
        ('Spracherkennung hat sich in den letzten Jahren dramatisch verbessert. '
         'Dennoch gibt es Bereiche, in denen das menschliche oder tierische Geh\u00f6rsystem '
         'nach wie vor \u00fcberlegen ist:') if DE else
        ('Speech recognition has improved dramatically in recent years. '
         'Nevertheless, there are domains in which the human or animal auditory system '
         'remains superior:'), sBody))

    for txt in ([
        'Das Trennen gleichzeitiger Sprecher in einem lauten, diffusen Schallfeld (Cocktailpartyproblem)',
        'Das Identifizieren eines einzelnen Instruments im vollen Orchesterklang',
        'Das Erkennen kurzer transienter Ereignisse unterhalb der Takt-Aufl\u00f6sung digitaler Systeme',
        'Das Hören weit unterhalb von Signal-Rausch-Verh\u00e4ltnissen, bei denen digitale Verfahren versagen',
        'Die sofortige Quellenlokalisation im dreidimensionalen Raum aus zwei Ohrsignalen',
    ] if DE else [
        'Separating simultaneous speakers in a loud, diffuse sound field (cocktail-party problem)',
        'Identifying a single instrument within a full orchestral texture',
        'Detecting short transient events below the frame resolution of digital systems',
        'Hearing well below signal-to-noise ratios at which digital methods fail',
        'Immediate source localisation in three-dimensional space from two ear signals',
    ]):
        story.append(bullet(txt))

    story.append(Spacer(1,0.3*cm))
    story.append(ibox(
        ('Diese Arbeit argumentiert, dass die Ursache f\u00fcr diese Diskrepanz '
         '<b>strukturell</b> ist \u2014 nicht eine Frage besserer Algorithmen, '
         'gr\u00f6\u00dferer Trainingsmengen oder schnellerer Prozessoren. '
         'Das biologische Geh\u00f6rsystem folgt einem grundlegend anderen '
         'Verarbeitungsprinzip: <b>physikalische Relaxation als Rechenprinzip</b>.') if DE else
        ('This work argues that the cause of this discrepancy is <b>structural</b> \u2014 '
         'not a matter of better algorithms, larger training sets, or faster processors. '
         'The biological auditory system follows a fundamentally different processing '
         'principle: <b>physical relaxation as a computational principle</b>.'),
        bg='#fff8e1', bc=ORG, fs=10))

    # 1.2
    story.append(H2(
        '1.2\u2002Das Geh\u00f6r als mehrstufig analoger Verarbeiter' if DE else
        '1.2\u2002The Auditory System as a Multi-stage Analogue Processor'))
    story.append(Paragraph(
        ('Das Geh\u00f6r ist kein biologisches Mikrofon, dem ein neuronaler Computer '
         'nachgeschaltet ist. Es ist ein <b>mehrstufiges analoges Verarbeitungssystem</b>, '
         'das das Signal weit gehend strukturiert, bevor auch nur eine einzige '
         'Nervenzelle feuert. Jede Stufe nutzt Physik als Vorverarbeiter.') if DE else
        ('The auditory system is not a biological microphone followed by a neural computer. '
         'It is a <b>multi-stage analogue processing system</b> that substantially '
         'structures the signal before a single nerve cell fires. '
         'Each stage uses physics as a pre-processor.'), sBody))

    # Ear anatomy figure
    img_path = '/home/claude/ear_anatomy.png'
    img_w = PW
    img_h = PW * (1090/2000)
    story.append(Spacer(1, 0.2*cm))
    story.append(Image(img_path, width=img_w, height=img_h))
    story.append(Paragraph(
        ('Anatomie des menschlichen Geh\u00f6rs: Au\u00dfenhelix, Geh\u00f6rgang, Trommelfell, '
         'Geh\u00f6rkn\u00f6chelchen (Hammer, Amboss, Steigb\u00fcgel), Cochlea (H\u00f6rschnecke) '
         'und vestibulokochle\u00e4rer Nerv. Jede Stufe ist ein analoger Vorverarbeiter.') if DE else
        ('Anatomy of the human ear: helix, ear canal, tympanic membrane, '
         'ossicles (malleus, incus, stapes), cochlea, and vestibulocochlear nerve. '
         'Every stage is an analogue pre-processor.'), sCap))
    story.append(Spacer(1, 0.3*cm))

    story.append(H3('Ohrmuschel und \u00e4u\u00dferer Geh\u00f6rgang' if DE else
                    'Pinna and External Ear Canal'))
    story.append(Paragraph(
        ('Die Geometrie der Ohrmuschel filtert eintreffende Schallwellen '
         'frequenz- und richtungsabh\u00e4ngig \u2014 passiv, ohne Energieverbrauch. '
         'Diese geometrische Filterung kodiert r\u00e4umliche Information '
         '(Elevationswinkel, Vorder-Hinter-Unterscheidung) in das Amplitudenspektrum. '
         'Ein digitales System, das dieselbe Information gewinnen will, '
         'muss sie durch Kreuzkorrelation von Mikrofonsignalen berechnen. '
         'Die Ohrmuschel <i>berechnet</i> sie durch Physik.') if DE else
        ('The geometry of the pinna filters incoming sound waves as a function of '
         'frequency and direction \u2014 passively, without energy expenditure. '
         'This geometric filtering encodes spatial information '
         '(elevation angle, front-back discrimination) into the amplitude spectrum. '
         'A digital system seeking the same information must compute it '
         'through cross-correlation of microphone signals. '
         'The pinna <i>computes</i> it through physics.'), sBody))

    story.append(H3('Mittelohr' if DE else 'Middle Ear'))
    story.append(Paragraph(
        ('Das Mittelohr f\u00fchrt Impedanzanpassung zwischen Luft und Perilymphe durch '
         'und komprimiert den Dynamikbereich aktiv \u00fcber den Stapediusreflex. '
         'Diese nichtlineare Kompression \u2014 schnell bei transienten Ereignissen, '
         'langsam bei kontinuierlichen Signalen \u2014 entspricht einem adaptiven '
         'analogen Kompander, der in Echtzeit auf Signalstatistik reagiert. '
         'Kein digitaler Algorithmus kann diese Funktion ohne Latenz replizieren.') if DE else
        ('The middle ear performs impedance matching between air and perilymph '
         'and actively compresses the dynamic range via the stapedius reflex. '
         'This non-linear compression \u2014 fast for transient events, '
         'slow for continuous signals \u2014 corresponds to an adaptive '
         'analogue compander responding to signal statistics in real time. '
         'No digital algorithm can replicate this function without latency.'), sBody))

    story.append(H3('Cochlea: mechanischer Fourier-Analysator' if DE else
                    'Cochlea: Mechanical Fourier Analyser'))
    story.append(Paragraph(
        ('Die Basilarmembran der Cochlea ist ein <b>ortsaufgel\u00f6ster Resonator</b>. '
         'Jeder Punkt entlang ihrer L\u00e4nge schwingt bei einer anderen Frequenz: '
         'ca.\u202f20\u2009kHz an der Basis, ca.\u202f20\u2009Hz am Apex, '
         'kontinuierlich und <i>logarithmisch</i> abgestuft. '
         'Eine Schallwelle teilt sich ohne jeden Berechnungsschritt auf dieses '
         'Spektrum-Analysesystem auf \u2014 die Fourier-Zerlegung <i>geschieht</i>, '
         'weil die Mechanik des Systems so beschaffen ist.') if DE else
        ('The basilar membrane of the cochlea is a <b>spatially distributed resonator</b>. '
         'Each point along its length resonates at a different frequency: '
         'approximately 20\u2009kHz at the base, 20\u2009Hz at the apex, '
         'continuously and <i>logarithmically</i> graded. '
         'A sound wave is decomposed onto this spectral analysis system '
         'without any computation step \u2014 the Fourier decomposition <i>happens</i> '
         'because the mechanics of the system are so constructed.'), sBody))
    story.append(Paragraph(
        ('Dies ist fundamental verschieden von der digitalen Fast-Fourier-Transformation: '
         'Die FFT ist ein Algorithmus, der sequentiell auf gespeicherten Abtastwerten '
         'operiert und eine Mindestfensterlänge ben\u00f6tigt. '
         'Die Cochlea analysiert kontinuierlich, in Echtzeit, ohne Fenster, ohne Takt.') if DE else
        ('This is fundamentally different from the digital Fast Fourier Transform: '
         'the FFT is an algorithm operating sequentially on stored sample values, '
         'requiring a minimum window length. '
         'The cochlea analyses continuously, in real time, without windows, without a clock.'), sBody))

    story.append(H3('\u00c4u\u00dfere Haarzellen: aktive R\u00fcckkopplung' if DE else
                    'Outer Hair Cells: Active Feedback'))
    story.append(Paragraph(
        ('Das entscheidende Merkmal, das die cochle\u00e4re Aufl\u00f6sung weit \u00fcber das '
         'passive mechanische Limit treibt, sind die <b>\u00e4u\u00dferen Haarzellen</b>. '
         'Sie sind elektromechanisch aktiv: das Membranprotein Prestin '
         'kontrahiert und expandiert in Abh\u00e4ngigkeit vom elektrischen Potential '
         'und verst\u00e4rkt selektiv die mechanische Schwingung der Basilarmembran '
         'durch positive R\u00fcckkopplung. '
         'Das Geh\u00f6r enth\u00e4lt einen biologischen analogen R\u00fcckkopplungsverst\u00e4rker '
         'mit frequenzselektiver Verst\u00e4rkung \u2014 auf jedem Frequenzkanal gleichzeitig.') if DE else
        ('The decisive feature that drives cochlear resolution far above the '
         'passive mechanical limit is the <b>outer hair cells</b>. '
         'They are electromechanically active: the membrane protein prestin '
         'contracts and expands as a function of electrical potential, '
         'selectively amplifying the mechanical vibration of the basilar membrane '
         'through positive feedback. '
         'The auditory system contains a biological analogue feedback amplifier '
         'with frequency-selective gain \u2014 on every frequency channel simultaneously.'), sBody))

    story.append(Paragraph(
        ('Das Ergebnis: Das Signal, das die inneren Haarzellen erreicht und '
         'in neuronale Impulse umgewandelt wird, ist bereits '
         'spektral analysiert, logarithmisch komprimiert, r\u00e4umlich kodiert '
         'und nichtlinear gefiltert. '
         'Die Verarbeitungszeit betr\u00e4gt weniger als 10 Millisekunden. '
         'Das Gehirn empf\u00e4ngt keine Rohdaten \u2014 '
         'es empf\u00e4ngt eine bereits strukturierte Repr\u00e4sentation '
         'der akustischen Szene.') if DE else
        ('The result: the signal that reaches the inner hair cells and is '
         'converted into neural impulses is already '
         'spectrally analysed, logarithmically compressed, spatially encoded, '
         'and non-linearly filtered. '
         'The processing time is less than 10 milliseconds. '
         'The brain receives no raw data \u2014 '
         'it receives an already structured representation of the acoustic scene.'), sBody))

    # 1.3 Tiere
    story.append(H2(
        '1.3\u2002Tiere als Extremfall des Prinzips' if DE else
        '1.3\u2002Animals as Extreme Cases of the Principle'))
    story.append(Paragraph(
        ('Bei manchen Tierarten wird das Prinzip in seiner reinsten Form sichtbar. '
         'Flederm\u00e4use l\u00f6sen durch Echolokation r\u00e4umliche '
         'Rekonstruktionsprobleme in Millisekunden, die ein digitales System '
         'auf der Basis von Rechenleistung und Gehirngr\u00f6\u00dfe dieser Tiere '
         'nie l\u00f6sen k\u00f6nnte. '
         'Delfine analysieren Ultraschallreflexe so pr\u00e4zise, dass sie Objekte '
         'hinter Hindernissen orten und Materialien unterscheiden k\u00f6nnen. '
         'Das Nervensystem dieser Tiere ist daf\u00fcr nicht gro\u00df genug \u2014 '
         'wenn man annimmt, dass Rechnen dasselbe bedeutet wie in einem digitalen Computer.') if DE else
        ('In certain animal species the principle becomes visible in its purest form. '
         'Bats solve spatial reconstruction problems via echolocation in milliseconds '
         'that a digital system based on the computing power and brain size of '
         'these animals could never solve. '
         'Dolphins analyse ultrasonic reflections so precisely that they can '
         'locate objects behind obstacles and distinguish materials. '
         'The nervous systems of these animals are not large enough for this \u2014 '
         'if one assumes that computing means the same as in a digital computer.'), sBody))
    story.append(ibox(
        'Die Physik rechnet. Das Nervensystem interpretiert.' if DE else
        'Physics computes. The nervous system interprets.',
        bg='#f0fff0', bc=GRN, fs=12, italic=True))

    # 1.4 Strukturelle Ursache
    story.append(H2(
        '1.4\u2002Die strukturelle Ursache der Diskrepanz' if DE else
        '1.4\u2002The Structural Cause of the Discrepancy'))
    story.append(Paragraph(
        ('Die anh\u00e4ltende \u00dcberlegenheit des biologischen Geh\u00f6rs '
         'in bestimmten Aufgaben ist kein Trainings- oder Datenproblem. '
         'Sie hat eine strukturelle Ursache, die sich auf drei Ebenen formulieren l\u00e4sst:') if DE else
        ('The persistent superiority of the biological auditory system in certain tasks '
         'is not a training or data problem. '
         'It has a structural cause that can be formulated on three levels:'), sBody))

    levels = ([
        ('Ebene\u202f1: Vorverarbeitung durch Physik',
         'Das biologische System l\u00f6st einen wesentlichen Teil des Verarbeitungsproblems '
         'durch den physikalischen Aufbau des Sensors \u2014 nicht durch Algorithmen. '
         'Die digitale Audiotechnik trennt Sensor (m\u00f6glichst linear) '
         'und Verarbeitung (alles folgt danach numerisch). '
         'Diese Trennung verschenkt das Rechenpotenzial des physikalischen Systems.'),
        ('Ebene\u202f2: Zeitkontinu\u00e4t',
         'Digitale Systeme arbeiten mit abgetasteten, gespeicherten, dann verarbeiteten Frames. '
         'Zwischen Aufnahme und Analyse liegt immer eine Fensterlatenz. '
         'Das biologische System arbeitet kontinuierlich: die Basilarmembran reagiert '
         'auf Signale, die k\u00fcrzer sind als jeder sinnvolle digitale Frame.'),
        ('Ebene\u202f3: Skalierte Komplexit\u00e4t',
         'Das Cocktailpartyproblem ist f\u00fcr digitale Systeme nach wie vor anspruchsvoll. '
         'Das menschliche Geh\u00f6r l\u00f6st es m\u00fchelos, weil die Quelltrennung '
         'bereits in der physikalischen Vorverarbeitung beginnt: r\u00e4umliche Filterung '
         'durch Ohrmuschel, interaurale Zeitdifferenzen, harmonische Struktur von Stimmen. '
         'Das digitale System muss diese physikalische Information nachtr\u00e4glich rekonstruieren.'),
    ] if DE else [
        ('Level\u202f1: Pre-processing through physics',
         'The biological system solves an essential part of the processing problem '
         'through the physical construction of the sensor \u2014 not through algorithms. '
         'Digital audio technology separates sensor (as linear as possible) '
         'and processing (everything follows numerically afterwards). '
         'This separation wastes the computational potential of the physical system.'),
        ('Level\u202f2: Temporal continuity',
         'Digital systems work with sampled, stored, then processed frames. '
         'Between capture and analysis there is always a window latency. '
         'The biological system operates continuously: the basilar membrane responds '
         'to signals shorter than any sensible digital frame.'),
        ('Level\u202f3: Scaled complexity',
         'The cocktail-party problem remains demanding for digital systems. '
         'The human auditory system solves it effortlessly because source separation '
         'already begins in the physical pre-processing: spatial filtering by the pinna, '
         'interaural time differences, harmonic structure of voices. '
         'The digital system must reconstruct this physical information after the fact.'),
    ])
    for title, body in levels:
        story.append(Paragraph(f'<b>{title}.</b>\u2002{body}', S('lv','DV',10,15,4,6,li=10)))

    # 1.5 Photonik
    story.append(H2(
        '1.5\u2002Parallelen zur hybriden Photonik' if DE else
        '1.5\u2002Parallels to Hybrid Photonics'))
    story.append(Paragraph(
        ('Die in den letzten Jahren aufkommenden hybriden photonischen Rechensysteme \u2014 '
         'insbesondere die Coherent Ising Machine (CIM) \u2014 verfolgen dasselbe '
         'Grundprinzip auf einem anderen physikalischen Substrat.') if DE else
        ('The hybrid photonic computing systems that have emerged in recent years \u2014 '
         'in particular the Coherent Ising Machine (CIM) \u2014 pursue the same '
         'fundamental principle on a different physical substrate.'), sBody))
    story.append(Paragraph(
        ('In einem CIM werden kombinatorische Optimierungsprobleme als Ising-Hamiltonian '
         'kodiert. Optische parametrische Oszillatoren nehmen Phasenzust\u00e4nde '
         '(0\u00b0 oder 180\u00b0) an, die den Spin-Zust\u00e4nden \u00b11 des '
         'Ising-Modells entsprechen. Das System relaxiert physikalisch in ein '
         'Energieminimum \u2014 das ist die L\u00f6sung des Optimierungsproblems. '
         'Ein digitaler Computer \u00fcberpr\u00fcft anschlie\u00dfend das Ergebnis.') if DE else
        ('In a CIM, combinatorial optimisation problems are encoded as Ising Hamiltonians. '
         'Optical parametric oscillators adopt phase states (0\u00b0 or 180\u00b0) '
         'corresponding to the spin states \u00b11 of the Ising model. '
         'The system relaxes physically to an energy minimum \u2014 '
         'this is the solution to the optimisation problem. '
         'A digital computer then reads and verifies the result.'), sBody))

    # Comparison table
    story.append(mkt([
        [TH('Cochlea / Geh\u00f6r' if DE else 'Cochlea / Auditory system'),
         TH('CIM / Hybride Photonik' if DE else 'CIM / Hybrid photonics')],
        [TD('Mechanische Resonanz der Basilarmembran' if DE else 'Mechanical resonance of the basilar membrane'),
         TD('Optische Resonatoren, parametrische Oszillatoren' if DE else 'Optical resonators, parametric oscillators')],
        [TD('Frequenztrennung durch Geometrie' if DE else 'Frequency separation through geometry'),
         TD('Problemkodierung durch Phasenkopplung' if DE else 'Problem encoding through phase coupling')],
        [TD('Analog, massiv parallel, kein Takt' if DE else 'Analogue, massively parallel, no clock'),
         TD('Analog, massiv parallel, Lichtgeschwindigkeit' if DE else 'Analogue, massively parallel, speed of light')],
        [TD('\u00c4u\u00dfere Haarzellen: aktive R\u00fcckkopplung' if DE else 'Outer hair cells: active feedback'),
         TD('Phasen-sensitiver Verst\u00e4rker, Feedbackschleife' if DE else 'Phase-sensitive amplifier, feedback loop')],
        [TD('Haarzellen: Analog \u2192 Nervenimpuls' if DE else 'Hair cells: analogue \u2192 neural spike'),
         TD('Messung: Analog \u2192 bin\u00e4r (0\u00b0/180\u00b0)' if DE else 'Measurement: analogue \u2192 binary (0\u00b0/180\u00b0)')],
        [TD('Gehirn verarbeitet vorstrukturierte Information' if DE else 'Brain processes pre-structured information'),
         TD('Digitaler Computer liest relaxierten Zustand' if DE else 'Digital computer reads relaxed state')],
    ],[PW/2, PW/2]))
    story.append(Paragraph(
        'Strukturelle Analogie zwischen biologischem Geh\u00f6rsystem und CIM.' if DE else
        'Structural analogy between the biological auditory system and CIM.', sCap))

    story.append(Spacer(1,0.3*cm))
    story.append(ibox(
        ('<b>Das gemeinsame Prinzip:</b> Ein physikalisches System mit geeigneter innerer '
         'Struktur relaxiert in einen Zustand, der ein hartes analytisches oder '
         'kombinatorisches Problem l\u00f6st. Die Verarbeitung <i>ist</i> die Physik \u2014 '
         'nicht eine Berechnung, die danach auf physikalischen Messdaten l\u00e4uft. '
         'Die Cochlea l\u00f6st kontinuierliche Spektralzerlegung durch mechanische Resonanz. '
         'Die CIM l\u00f6st NP-schwere Ising-Probleme durch optische Phasenrelaxation. '
         'Beide sind hybride Systeme: das analoge Substrat \u00fcbernimmt den '
         'rechnerisch teuren Teil, ein digitales System \u00fcbernimmt '
         'Kodierung, Dekodierung und sequentielle Logik.') if DE else
        ('<b>The common principle:</b> A physical system with suitable internal structure '
         'relaxes into a state that solves a hard analytical or combinatorial problem. '
         'The processing <i>is</i> the physics \u2014 not a computation that runs '
         'afterwards on physical measurement data. '
         'The cochlea solves continuous spectral decomposition through mechanical resonance. '
         'The CIM solves NP-hard Ising problems through optical phase relaxation. '
         'Both are hybrid systems: the analogue substrate handles the '
         'computationally expensive part; a digital system handles '
         'encoding, decoding, and sequential logic.'),
        bg='#e8f0ff', bc=BLUE, fs=10))

    # 1.6 Aufbau
    story.append(H2('1.6\u2002Aufbau dieses Dokuments' if DE else
                    '1.6\u2002Structure of this Document'))
    story.append(Paragraph(
        ('Das vorliegende Dokument entwickelt diese Analogien in mehreren Richtungen '
         'und arbeitet heraus, was daraus f\u00fcr den Entwurf k\u00fcnftiger '
         'Audioverarbeitungssysteme folgt.') if DE else
        ('This document develops these analogies in several directions and '
         'draws out what follows for the design of future audio processing systems.'), sBody))

    chapters = ([
        ('Kapitel\u202f2: Die Cochlea als Informationssystem',
         'Mechanische Eigenschaften, aktive Verst\u00e4rkung, logarithmische Skalierung, zeitliche Aufl\u00f6sung.'),
        ('Kapitel\u202f3: Strukturelle Grenzen digitaler Audioanalyse',
         'Wo und warum digitale Systeme an Grenzen sto\u00dfen, die nicht durch mehr '
         'Rechenleistung \u00fcberwunden werden k\u00f6nnen.'),
        ('Kapitel\u202f4: Hybride photonische Rechensysteme',
         'Coherent Ising Machines, neuronale photonische Netze und ihre strukturelle '
         'Verwandtschaft mit dem biologischen Geh\u00f6rsystem.'),
        ('Kapitel\u202f5: Ausblick \u2014 Architekturen f\u00fcr analoge Audiokognition',
         'Analog-vorverarbeitende Sensoren, neuromorphe Cochlea-Chips, '
         'photonisch-neuronale Hybridsysteme f\u00fcr Echtzeit-Audiokognition.'),
    ] if DE else [
        ('Chapter\u202f2: The Cochlea as an Information System',
         'Mechanical properties, active amplification, logarithmic scaling, temporal resolution.'),
        ('Chapter\u202f3: Structural Limits of Digital Audio Analysis',
         'Where and why digital systems encounter limits that cannot be overcome '
         'by more computing power.'),
        ('Chapter\u202f4: Hybrid Photonic Computing Systems',
         'Coherent Ising Machines, neural photonic networks and their structural '
         'kinship with the biological auditory system.'),
        ('Chapter\u202f5: Outlook \u2014 Architectures for Analogue Audio Cognition',
         'Analogue pre-processing sensors, neuromorphic cochlea chips, '
         'photonic-neural hybrid systems for real-time audio cognition.'),
    ])
    for title, body in chapters:
        story.append(Paragraph(f'<b>{title}.</b>\u2002{body}',
                               S('ch','DV',10,15,4,4,li=10)))

    # ── 1.7  ξ ist in der Physik kodiert ─────────────────────────────────
    story.append(PageBreak())
    story.append(H2(
        '1.7\u2002\u03be ist in der Physik kodiert: Kristalle, Cochlea und nat\u00fcrliche Signale' if DE else
        '1.7\u2002\u03be is Encoded in Physics: Crystals, Cochlea, and Natural Signals'))

    story.append(Paragraph(
        ('Die vorangegangenen Abschnitte beschrieben die Cochlea als physikalischen '
         'Vorverarbeiter. Es gibt eine tiefere Ebene: '
         '<b>Die relevante Mathematik ist nicht in Algorithmen kodiert \u2014 '
         'sie ist in der Physik selbst kodiert.</b> '
         'Das gilt f\u00fcr Kristalle ebenso wie f\u00fcr die Basilarmembran, '
         'und in der T0-Theorie hat beides denselben Ursprung: '
         'den geometrischen Parameter\u00a0\u03be.') if DE else
        ('The preceding sections described the cochlea as a physical pre-processor. '
         'There is a deeper level: '
         '<b>The relevant mathematics is not encoded in algorithms \u2014 '
         'it is encoded in physics itself.</b> '
         'This applies to crystals as much as to the basilar membrane, '
         'and in T0 theory both share the same origin: '
         'the geometric parameter\u00a0\u03be.'), sBody))

    story.append(H3('Kristalle: Die Geometrie ist die L\u00f6sung' if DE else
                    'Crystals: The Geometry is the Solution'))
    story.append(Paragraph(
        ('Ein Kristall l\u00f6st kein Eigenwertproblem \u2014 er <i>ist</i> die L\u00f6sung. '
         'Bandstruktur, Phononen, dielektrische Funktion entstehen dadurch, '
         'dass das periodische Gitter Wellen nach Maßgabe seiner Geometrie in '
         'Eigenmoden zerlegt. Kein Algorithmus rechnet \u2014 die Physik propagiert.') if DE else
        ('A crystal does not solve an eigenvalue problem \u2014 it <i>is</i> the solution. '
         'Band structure, phonons, and the dielectric function arise because '
         'the periodic lattice decomposes waves into eigenmodes according to its geometry. '
         'No algorithm computes \u2014 physics propagates.'), sBody))
    story.append(Paragraph(
        ('Die Gitterkonstante ist durch atomare Radien und Bindungsl\u00e4ngen bestimmt, '
         'die auf der atomaren L\u00e4ngenskala a\u2080 liegen. '
         'In T0 ist diese Skala die Stufe \u03be\u2077 der \u03be-Potenzleiter:') if DE else
        ('The lattice constant is determined by atomic radii and bond lengths '
         'at the atomic length scale a\u2080. '
         'In T0 this scale is the rung \u03be\u2077 of the \u03be-power ladder:'), sBody))
    story.append(Paragraph(
        'a\u2080 \u2248 \u03be<super>\u22126,326</super> \u00b7 \u2113<sub>P</sub>'
        '\u2003\u2003R<sub>\u221e</sub> \u2248 \u03be<super>6,956</super> \u00b7 E<sub>P</sub>',
        S('eq2','DV-M',10,16,4,8,TA_CENTER)))

    story.append(mkt([
        [TH('Gr\u00f6\u00dfe' if DE else 'Quantity'),
         TH('Wert' if DE else 'Value'),
         TH('\u03be-Exponent'),
         TH('Bedeutung' if DE else 'Meaning')],
        [TD('Bohr-Radius a\u2080'),       TD('0,0529\u2009nm' if DE else '0.0529\u2009nm'),
         TF('\u03be<super>\u22126,326</super>'), TD('Atomskala / atomic scale')],
        [TD('NaCl-Gitterkonstante'),      TD('0,282\u2009nm' if DE else '0.282\u2009nm'),
         TF('\u03be<super>\u22126,514</super>'), TD('Ionenkristall / ionic crystal')],
        [TD('Si-Gitterkonstante'),        TD('0,543\u2009nm' if DE else '0.543\u2009nm'),
         TF('\u03be<super>\u22126,587</super>'), TD('Halbleiter / semiconductor')],
        [TB('<b>Rydberg R<sub>\u221e</sub></b>'),
         TB('<b>13,598\u2009eV</b>' if DE else '<b>13.598\u2009eV</b>'),
         TB('<b>\u03be<super>+6,956</super></b>'),
         TB('<b>Atomenergie / Cochlea-Skala</b>')],
    ],[3.5*cm,2.5*cm,3.0*cm,5.2*cm],
       extra=[('BACKGROUND',(0,4),(-1,4),colors.HexColor('#e8f0ff'))]))
    story.append(Paragraph(
        'Alle atomaren L\u00e4ngenskalen und Gitterkonstanten liegen auf Stufe |\u03be\u2077| der \u03be-Leiter.' if DE else
        'All atomic length scales and lattice constants lie on rung |\u03be\u2077| of the \u03be-ladder.', sCap))

    story.append(H3('Die Cochlea als biologischer \u03be\u2077-Resonator' if DE else
                    'The Cochlea as a Biological \u03be\u2077 Resonator'))
    story.append(Paragraph(
        ('Die Basilarmembran besteht aus Kollagen, Proteoglykanen und Wasser. '
         'Der Elastizit\u00e4tsmodul dieses Gewebes entstammt den chemischen Bindungen '
         'zwischen Molek\u00fclen \u2014 also der molekularen Skala, der \u03be\u2077-Stufe. '
         'Die Steifigkeit an Position\u00a0x entlang der Cochlea:') if DE else
        ('The basilar membrane consists of collagen, proteoglycans, and water. '
         'The elastic modulus of this tissue arises from chemical bonds '
         'between molecules \u2014 i.e. the molecular scale, the \u03be\u2077 rung. '
         'The stiffness at position\u00a0x along the cochlea:'), sBody))
    story.append(Paragraph(
        'k(x) \u223c E \u00b7 t(x)\u00b3 / w(x)'
        '\u2003\u2003\u21d2\u2003\u2003f(x) \u221d \u221a(k(x)/\u03c1)',
        S('eq3','DV-M',10,16,4,8,TA_CENTER)))
    story.append(Paragraph(
        ('Der Elastizit\u00e4tsmodul\u00a0E ist durch chemische Bindungsenergien bestimmt. '
         'Chemische Bindungsenergien sind Vielfache von R<sub>\u221e</sub> (Dok.\u202f169). '
         'R<sub>\u221e</sub> liegt auf Stufe \u03be\u2077. '
         '<b>Die Cochlea ist ein \u03be\u2077-System, das \u03be\u2077-Frequenzen analysiert.</b> '
         'Die Geometrie ist biologisch optimiert, die Skala ist durch \u03be vorgegeben \u2014 '
         'wie bei Kristallen.') if DE else
        ('The elastic modulus\u00a0E is determined by chemical bond energies. '
         'Chemical bond energies are multiples of R<sub>\u221e</sub> (Doc.\u202f169). '
         'R<sub>\u221e</sub> lies on rung \u03be\u2077. '
         '<b>The cochlea is a \u03be\u2077 system analysing \u03be\u2077 frequencies.</b> '
         'The geometry is biologically optimised; the scale is set by \u03be \u2014 '
         'as with crystals.'), sBody))

    story.append(H3('Die Greenwood-Abbildung als \u03be-Leiter in biologischer Materie' if DE else
                    'The Greenwood Map as \u03be-Ladder in Biological Matter'))
    story.append(Paragraph(
        ('Die tonotope Abbildung der Cochlea folgt der Greenwood-Funktion '
         'f(x) = A\u00b710<super>a\u00b7x</super> mit a = 0,06\u2009mm<super>\u22121</super>: '
         'eine Oktave entspricht \u0394x \u2248 5\u2009mm. '
         'Der gesamte H\u00f6rbereich von 10\u00a0Okaven entspricht auf der \u03be-Leiter:') if DE else
        ('The tonotopic map of the cochlea follows the Greenwood function '
         'f(x) = A\u00b710<super>a\u00b7x</super> with a = 0.06\u2009mm<super>\u22121</super>: '
         'one octave corresponds to \u0394x \u2248 5\u2009mm. '
         'The full hearing range of 10\u00a0octaves corresponds on the \u03be-ladder to:'), sBody))
    story.append(Paragraph(
        '10 \u00d7 log<sub>\u03be</sub>(2) = 10 \u00d7 (\u22120,0777) \u2248 \u22120,78 \u03be-Stufen',
        S('eq4','DV-M',10,16,4,8,TA_CENTER)))
    story.append(Paragraph(
        ('Die logarithmische Struktur der Greenwood-Abbildung <i>ist</i> '
         'die logarithmische Struktur der \u03be-Leiter \u2014 '
         'physikalisch realisiert in biologischem Gewebe.') if DE else
        ('The logarithmic structure of the Greenwood map <i>is</i> '
         'the logarithmic structure of the \u03be-ladder \u2014 '
         'physically realised in biological tissue.'), sBody))

    story.append(H3('1/f-Rauschen, \u03be-Leiter und optimale Kodierung' if DE else
                    '1/f Noise, \u03be-Ladder, and Optimal Encoding'))
    story.append(Paragraph(
        ('Nat\u00fcrliche Schallsignale haben ein 1/f-Spektrum (rosa Rauschen): '
         'pro Oktave wird dieselbe Energie abgestrahlt. '
         'Das ist die statistische Signatur selbst\u00e4hnlicher physikalischer Prozesse '
         '(Sprache, Musik, Umgebungsger\u00e4usche). '
         'Die \u03be-Leiter ist logarithmisch \u00e4quidistant: '
         'jeder Schritt multipliziert die Energie mit \u03be<super>\u22121</super> = 7500. '
         'Die \u03be-Leiter hat damit dieselbe Struktur wie rosa Rauschen. '
         '<b>Die Cochlea ist optimal f\u00fcr Signale mit \u03be-Leiter-Statistik '
         '\u2014 weil sie selbst eine Realisierung der \u03be\u2077-Stufe ist.</b>') if DE else
        ('Natural sound signals have a 1/f spectrum (pink noise): '
         'equal energy per octave. '
         'This is the statistical signature of self-similar physical processes '
         '(speech, music, ambient sounds). '
         'The \u03be-ladder is logarithmically equidistant: '
         'each step multiplies the energy by \u03be<super>\u22121</super> = 7500. '
         'The \u03be-ladder therefore has the same structure as pink noise. '
         '<b>The cochlea is optimally tuned for signals with \u03be-ladder statistics '
         '\u2014 because it is itself a realisation of the \u03be\u2077 rung.</b>'), sBody))

    story.append(H3('Drei Ebenen der \u03be-Kodierung' if DE else 'Three Levels of \u03be Encoding'))
    story.append(mkt([
        [TH('Ebene' if DE else 'Level'),
         TH('Kristall'),
         TH('Cochlea')],
        [TD('Materielle Basis' if DE else 'Material basis'),
         TD('Ionenbindung, a\u2080 \u223c \u03be\u207b\u2076\u00b3' if DE else
            'Ionic bond, a\u2080 \u223c \u03be\u207b\u2076\u00b3'),
         TD('Kollagenbindung, E-Modul aus chem. Bindungen' if DE else
            'Collagen bond, E-modulus from chem. bonds')],
        [TD('\u03be-Stufe'),
         TD('Gitterkonstante \u223c \u03be\u207b\u2076\u2075' if DE else
            'Lattice constant \u223c \u03be\u207b\u2076\u2075'),
         TD('Membransteifigkeit \u223c \u03be\u2077' if DE else
            'Membrane stiffness \u223c \u03be\u2077')],
        [TD('Rechenprinzip' if DE else 'Computing principle'),
         TD('Wellenpropagation im Potential' if DE else 'Wave propagation in potential'),
         TD('Mechanische Resonanz entlang Membran' if DE else 'Mechanical resonance along membrane')],
        [TD('Ergebnis' if DE else 'Result'),
         TD('Bandstruktur, Phononenmoden' if DE else 'Band structure, phonon modes'),
         TD('Tonotope Frequenzabbildung' if DE else 'Tonotopic frequency map')],
        [TD('Was berechnet wird' if DE else 'What is computed'),
         TD('Nichts \u2014 Physik propagiert' if DE else 'Nothing \u2014 physics propagates'),
         TD('Nichts \u2014 Mechanik relaxiert' if DE else 'Nothing \u2014 mechanics relaxes')],
    ],[3.2*cm,5.4*cm,5.6*cm]))

    story.append(Spacer(1,0.4*cm))
    story.append(ibox(
        ('<b>Das Grundprinzip in T0-Sprache:</b> \u03be = 4/30\u2009000 ist das geometrische '
         'Packungsdefizit des 3D-Gitters, aus dem alle Fundamentalkonstanten folgen. '
         'Kristallgitter, Bohr-Radius, Rydberg-Energie, Elastizit\u00e4tsmodul biologischen Gewebes, '
         'Cochleafrequenzen \u2014 alle liegen auf der \u03be\u2077-Stufe. '
         'Jedes physikalische System auf dieser Stufe <i>rechnet</i> automatisch auf der atomaren Skala '
         '\u2014 durch seine blo\u00dfe Existenz.<br/><br/>'
         'Mathematik ist in \u03be-Geometrie kodiert. '
         'Physik realisiert diese Geometrie in Materie. '
         'Rechnen ist Propagation.') if DE else
        ('<b>The fundamental principle in T0 language:</b> \u03be = 4/30\u2009000 is the geometric '
         'packing deficit of the 3D lattice from which all fundamental constants follow. '
         'Crystal lattices, Bohr radius, Rydberg energy, elastic modulus of biological tissue, '
         'cochlear frequencies \u2014 all lie on the \u03be\u2077 rung. '
         'Every physical system at this rung <i>computes</i> automatically at the atomic scale '
         '\u2014 by its mere existence.<br/><br/>'
         'Mathematics is encoded in \u03be-geometry. '
         'Physics realises this geometry in matter. '
         'Computing is propagation.'),
        bg='#1a1a2e', bc=DARK, fs=11))
    # white text for dark box
    story[-1] = ibox(
        ('<b>Das Grundprinzip in T0-Sprache:</b> \u03be = 4/30\u2009000 ist das geometrische '
         'Packungsdefizit des 3D-Gitters, aus dem alle Fundamentalkonstanten folgen. '
         'Kristallgitter, Bohr-Radius, Rydberg-Energie, Elastizit\u00e4tsmodul biologischen Gewebes, '
         'Cochleafrequenzen \u2014 alle liegen auf der \u03be\u2077-Stufe. '
         'Jedes physikalische System auf dieser Stufe <i>rechnet</i> automatisch auf der atomaren Skala '
         '\u2014 durch seine blo\u00dfe Existenz.<br/><br/>'
         'Mathematik ist in \u03be-Geometrie kodiert. '
         'Physik realisiert diese Geometrie in Materie. '
         'Rechnen ist Propagation.') if DE else
        ('<b>The fundamental principle in T0 language:</b> \u03be = 4/30\u2009000 is the geometric '
         'packing deficit of the 3D lattice from which all fundamental constants follow. '
         'Crystal lattices, Bohr radius, Rydberg energy, elastic modulus of biological tissue, '
         'cochlear frequencies \u2014 all lie on the \u03be\u2077 rung. '
         'Every physical system at this rung <i>computes</i> automatically at the atomic scale '
         '\u2014 by its mere existence.<br/><br/>'
         'Mathematics is encoded in \u03be-geometry. '
         'Physics realises this geometry in matter. '
         'Computing is propagation.'),
        bg='#eef2ff', bc=MID, fs=11)

    story.append(Spacer(1,0.5*cm))
    story.append(HRFlowable(width=PW, thickness=1, color=GRY, spaceAfter=8))
    story.append(Paragraph(
        ('<b>Zentrale These:</b> Die n\u00e4chste qualitative Verbesserung in der '
         'maschinellen H\u00f6rverarbeitung wird nicht durch gr\u00f6\u00dfere neuronale Netze kommen, '
         'sondern durch eine R\u00fcckkehr zum Prinzip, das die Natur seit Hunderten '
         'von Millionen Jahren nutzt \u2014 '
         '<b>Physik als Vorverarbeiter, Digitaltechnik als Interpreter</b>.') if DE else
        ('<b>Central thesis:</b> The next qualitative improvement in machine auditory '
         'processing will not come from larger neural networks, '
         'but from a return to the principle that nature has used for hundreds '
         'of millions of years \u2014 '
         '<b>physics as pre-processor, digital technology as interpreter</b>.'),
        S('th',fn='DV-I',fs=10,ld=15,sa=0,al=TA_JUSTIFY,tc=MID,li=12,ri=12)))

    # ══════════════════════════════════════════════════════════════════════
    # Kapitel 2: Gilt die Heisenbergsche Unschärfe fürs Hören?
    # ══════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(H1(
        '2\u2002Gilt die Heisenbergsche Unsch\u00e4rfe f\u00fcrs H\u00f6ren?' if DE else
        '2\u2002Does the Heisenberg Uncertainty Principle Apply to Hearing?'))

    story.append(ibox(
        ('<b>Kernaussage:</b> Die akustische Zeit-Frequenz-Unsch\u00e4rferelation '
         '\u0394t\u00b7\u0394f \u2265 1/4\u03c0 gilt f\u00fcr passive lineare Systeme. '
         'Die Cochlea ist keines davon. '
         'Als aktives, nichtlineares, koh\u00e4rentes Wellensystem unterschreitet sie '
         'die effektive Unsch\u00e4rfe \u2014 strukturell analog zu gequetschtem Licht '
         'in der Quantenoptik. '
         'Das Geh\u00f6r realisiert kein Quantencomputing im technischen Sinne, '
         'aber dasselbe Verarbeitungsprinzip: koh\u00e4rente aktive Wellenphysik '
         'ohne die Einschr\u00e4nkungen passiver klassischer Systeme.') if DE else
        ('<b>Core statement:</b> The acoustic time-frequency uncertainty relation '
         '\u0394t\u00b7\u0394f \u2265 1/4\u03c0 applies to passive linear systems. '
         'The cochlea is neither. '
         'As an active, non-linear, coherent wave system it effectively undercuts '
         'the uncertainty \u2014 structurally analogous to squeezed light '
         'in quantum optics. '
         'The auditory system does not realise quantum computing in the technical sense, '
         'but the same processing principle: coherent active wave physics '
         'without the limitations of passive classical systems.'),
        bg='#e8f4f8', bc=DARK, fs=10))

    # 2.1 Voraussetzungen
    story.append(H2(
        '2.1\u2002Die Unsch\u00e4rferelation und ihre Voraussetzungen' if DE else
        '2.1\u2002The Uncertainty Relation and its Preconditions'))
    story.append(Paragraph(
        ('Die Zeit-Frequenz-Unsch\u00e4rferelation '
         '\u0394t\u00b7\u0394f \u2265 1/4\u03c0 '
         'ist kein experimentelles Ergebnis \u2014 '
         'sie ist ein mathematisches Theorem, eine direkte Konsequenz der '
         'Fourier-Analyse f\u00fcr quadratisch integrierbare Funktionen. '
         'Sie gilt f\u00fcr jedes <b>passive lineare</b> System, das ein Wellenfeld misst.') if DE else
        ('The time-frequency uncertainty relation '
         '\u0394t\u00b7\u0394f \u2265 1/4\u03c0 '
         'is not an experimental result \u2014 '
         'it is a mathematical theorem, a direct consequence of Fourier analysis '
         'for square-integrable functions. '
         'It applies to every <b>passive linear</b> system that measures a wave field.'), sBody))
    story.append(Paragraph(
        ('Ein Mikrofon ist passiv und linear \u2014 es misst Druckschwankungen, '
         'ohne in das Schallfeld einzugreifen. '
         'Eine digitale FFT ist eine lineare Transformation \u00fcber einem endlichen Fenster. '
         'F\u00fcr das System Mikrofon\u202f+\u202fFFT gilt die Unsch\u00e4rfe hart. '
         'Die Cochlea ist weder passiv noch linear.') if DE else
        ('A microphone is passive and linear \u2014 it measures pressure fluctuations '
         'without intervening in the sound field. '
         'A digital FFT is a linear transformation over a finite window. '
         'For the system microphone\u202f+\u202fFFT the uncertainty applies strictly. '
         'The cochlea is neither passive nor linear.'), sBody))

    # 2.2 Aktives System
    story.append(H2(
        '2.2\u2002Die Cochlea als aktives nichtlineares System' if DE else
        '2.2\u2002The Cochlea as an Active Non-linear System'))
    story.append(H3('Energieinjektion durch \u00e4u\u00dfere Haarzellen' if DE else
                    'Energy Injection by Outer Hair Cells'))
    story.append(Paragraph(
        ('Die \u00e4u\u00dferen Haarzellen injizieren mechanische Energie in das '
         'Schwingungssystem der Basilarmembran. '
         'Das Membranprotein Prestin \u00e4ndert die Zell\u00e4nge in Abh\u00e4ngigkeit '
         'vom Membranpotential, mit Frequenzen bis zu 70\u2009kHz. '
         'Dies ist kein passiver Messprozess \u2014 '
         'es ist ein aktiver Eingriff in das Signal. '
         'Das System ist kein Beobachter des Schallfeldes. '
         'Es <i>ver\u00e4ndert</i> das Schallfeld, das es analysiert.') if DE else
        ('The outer hair cells inject mechanical energy into the vibration system '
         'of the basilar membrane. '
         'The membrane protein prestin changes cell length depending on '
         'membrane potential, at frequencies up to 70\u2009kHz. '
         'This is not a passive measurement process \u2014 '
         'it is an active intervention in the signal. '
         'The system is not an observer of the sound field. '
         'It <i>modifies</i> the sound field it analyses.'), sBody))

    story.append(H3('Gequetschtes Licht als strukturelle Analogie' if DE else
                    'Squeezed Light as a Structural Analogy'))
    story.append(Paragraph(
        ('In der Quantenoptik gilt f\u00fcr Amplitude und Phase eines Lichtfeldes: '
         '\u0394X\u2081\u00b7\u0394X\u2082 \u2265 1/4. '
         'Gequetschtes Licht reduziert \u0394X\u2081 unter das Vakuumlimit, '
         'indem es \u0394X\u2082 entsprechend vergr\u00f6\u00dfert. '
         'Dies verletzt die Unsch\u00e4rfe nicht \u2014 '
         'es zeigt, dass das Produkt ein <i>Minimum</i> ist, '
         'keine symmetrische Schranke. '
         'Das System kann asymmetrisch optimiert werden, wenn es aktiv kontrolliert wird.') if DE else
        ('In quantum optics, for amplitude and phase of a light field: '
         '\u0394X\u2081\u00b7\u0394X\u2082 \u2265 1/4. '
         'Squeezed light reduces \u0394X\u2081 below the vacuum limit '
         'by correspondingly increasing \u0394X\u2082. '
         'This does not violate the uncertainty relation \u2014 '
         'it shows the product is a <i>minimum</i>, not a symmetric bound. '
         'The system can be asymmetrically optimised when actively controlled.'), sBody))
    story.append(Paragraph(
        ('<b>Die \u00e4u\u00dferen Haarzellen tun dasselbe akustisch:</b> '
         'Sie dr\u00fccken die Frequenzunsch\u00e4rfe \u0394f unter das passive Limit, '
         'indem sie die Frequenzaufl\u00f6sung durch positive R\u00fcckkopplung sch\u00e4rfen. '
         'Der Preis ist Energieverbrauch \u2014 '
         'nicht der Verlust von Zeitaufl\u00f6sung.') if DE else
        ('<b>The outer hair cells do the same acoustically:</b> '
         'They push the frequency uncertainty \u0394f below the passive limit '
         'by sharpening frequency resolution through positive feedback. '
         'The price is energy expenditure \u2014 '
         'not loss of time resolution.'), sBody))

    # Comparison table FFT vs Cochlea
    story.append(mkt([
        [TH('Eigenschaft' if DE else 'Property'),
         TH('FFT (passiv, digital)'),
         TH('Cochlea (aktiv, analog)')],
        [TD('Mechanismus' if DE else 'Mechanism'),
         TD('Lineare Transformation \u00fcber Fenster' if DE else 'Linear transform over window'),
         TD('Physikalische Resonanz, kontinuierlich' if DE else 'Physical resonance, continuous')],
        [TD('Zeitfenster' if DE else 'Time window'),
         TD('Diskret, endlich, explizit' if DE else 'Discrete, finite, explicit'),
         TD('Keines \u2014 Resonanz l\u00e4uft st\u00e4ndig' if DE else 'None \u2014 resonance runs continuously')],
        [TD('Frequenzaufl\u00f6sung' if DE else 'Freq. resolution'),
         TF('\u0394f \u2265 1/T\u208a\u1d49\u207f\u02e2\u1d57\u1d49\u02b3'),
         TD('G\u00fcte Q des Resonators, aktiv erh\u00f6ht' if DE else 'Resonator quality Q, actively enhanced')],
        [TD('Zeitaufl\u00f6sung' if DE else 'Time resolution'),
         TF('\u0394t = 1/f\u209b (Abtastrate)' if DE else '\u0394t = 1/f\u209b (sample rate)'),
         TD('Onset-Detektion, unabh. von Frequenzanalyse' if DE else 'Onset detection, independent of freq. analysis')],
        [TD('Phaseninformation' if DE else 'Phase information'),
         TD('Nach FFT verloren' if DE else 'Lost after FFT'),
         TD('Im Spike-Timing erhalten (Phase-Locking)' if DE else 'Retained in spike timing (phase-locking)')],
        [TD('Unsch\u00e4rfe' if DE else 'Uncertainty'),
         TF('\u0394t\u00b7\u0394f \u2265 1/4\u03c0 (hart)' if DE else '\u0394t\u00b7\u0394f \u2265 1/4\u03c0 (hard)'),
         TD('Effektiv unterschritten durch aktive R\u00fcckkopplung' if DE else 'Effectively undercut by active feedback')],
    ],[4.0*cm,5.0*cm,5.2*cm]))
    story.append(Paragraph(
        ('Das Geh\u00f6r unterschreitet die Unsch\u00e4rfe nicht, indem es die Mathematik bricht \u2014 '
         'sondern indem es ein anderes physikalisches System ist.') if DE else
        ('The auditory system undercuts the uncertainty not by breaking the mathematics \u2014 '
         'but by being a different physical system.'), sCap))

    # 2.3 Phase-Locking
    story.append(H2('2.3\u2002Phase-Locking: Frequenzinformation aus der Zeit' if DE else
                    '2.3\u2002Phase-Locking: Frequency Information from Time'))
    story.append(Paragraph(
        ('Das Geh\u00f6r nutzt zwei grundlegend verschiedene Mechanismen <b>parallel</b>:<br/>'
         '<b>Ortscodierung</b> (<i>place coding</i>): Welche Nervenfaser feuert, '
         'codiert die Frequenz durch den Ort der Basilarmembran-Erregung \u2014 '
         'Breitband, begrenzte Aufl\u00f6sung.<br/>'
         '<b>Zeitcodierung</b> (<i>temporal coding</i>): H\u00f6rnervenfasern feuern '
         'bevorzugt zu einem bestimmten Zeitpunkt im Schwingungszyklus '
         '(Phase-Locking, bis ca.\u202f4\u2009kHz). '
         'Das Gehirn analysiert die Zeitintervalle zwischen Spikes \u2014 '
         'die Periodenstruktur des Signals ist im neuronalen Code erhalten. '
         'Die Frequenzaufl\u00f6sung durch Zeitcodierung \u00fcbersteigt die durch '
         'Ortscodierung bei tiefen Frequenzen um mehr als eine Gr\u00f6\u00dfenordnung.') if DE else
        ('The auditory system uses two fundamentally different mechanisms <b>in parallel</b>:<br/>'
         '<b>Place coding</b>: which nerve fibre fires encodes frequency by the '
         'location of basilar membrane excitation \u2014 broadband, limited resolution.<br/>'
         '<b>Temporal coding</b>: auditory nerve fibres fire preferentially at a '
         'specific point in the vibration cycle (phase-locking, up to ~4\u2009kHz). '
         'The brain analyses the time intervals between spikes \u2014 '
         'the periodic structure of the signal is retained in the neural code. '
         'Frequency resolution through temporal coding exceeds place coding '
         'at low frequencies by more than an order of magnitude.'), sBody))
    story.append(ibox(
        ('Die FFT kollabiert das Signal in ein Spektrum \u2014 '
         'danach ist die Phaseninformation weg. '
         'Die Cochlea kollabiert nicht. '
         'Sie erh\u00e4lt die zeitliche Feinstruktur parallel zur Frequenzinformation, '
         'weil beide auf verschiedenen physikalischen Mechanismen beruhen \u2014 '
         'nicht auf demselben mathematischen Kompromiss.') if DE else
        ('The FFT collapses the signal into a spectrum \u2014 '
         'after which phase information is gone. '
         'The cochlea does not collapse. '
         'It retains temporal fine structure in parallel with frequency information, '
         'because both rest on different physical mechanisms \u2014 '
         'not on the same mathematical trade-off.'),
        bg='#fff8e1', bc=ORG, fs=10, italic=True))

    # 2.4 Quantencomputer-Analogie
    story.append(H2(
        '2.4\u2002Das Geh\u00f6r als Quantencomputer \u2014 eine pr\u00e4zise Analogie' if DE else
        '2.4\u2002The Auditory System as Quantum Computer \u2014 a Precise Analogy'))
    story.append(Paragraph(
        ('<b>Provokative These:</b> Ein Quantencomputer befindet sich nicht im Gehirn \u2014 '
         'er befindet sich im Geh\u00f6r. '
         'Diese Aussage ist als Analogie zu verstehen, nicht als ontologische Behauptung '
         '\u00fcber Quantenzust\u00e4nde in biologischer Materie. '
         'Sie ist jedoch strukturell pr\u00e4ziser als sie zun\u00e4chst aussieht.') if DE else
        ('<b>Provocative thesis:</b> A quantum computer is not located in the brain \u2014 '
         'it is located in the auditory system. '
         'This is to be understood as an analogy, not as an ontological claim '
         'about quantum states in biological matter. '
         'It is, however, structurally more precise than it initially appears.'), sBody))

    story.append(mkt([
        [TH('Prinzip' if DE else 'Principle'),
         TH('Quantencomputer'),
         TH('Cochlea / Geh\u00f6r' if DE else 'Cochlea / Auditory system')],
        [TD('Superposition'),
         TD('Qubit in \u00dcberlagerung |0\u27e9 + |1\u27e9' if DE else 'Qubit in superposition |0\u27e9 + |1\u27e9'),
         TD('Alle Frequenzkan\u00e4le gleichzeitig aktiv' if DE else 'All frequency channels simultaneously active')],
        [TD('Koh\u00e4renz' if DE else 'Coherence'),
         TD('Phasenbeziehungen zwischen Qubits erhalten' if DE else 'Phase relations between qubits preserved'),
         TD('Phase-Locking: Phasenstruktur im Spike-Timing' if DE else 'Phase-locking: phase structure in spike timing')],
        [TD('Aktive Kontrolle' if DE else 'Active control'),
         TD('Fehlerkorrektur, Quantengatter' if DE else 'Error correction, quantum gates'),
         TD('\u00c4u\u00dfere Haarzellen: freq.selektive R\u00fcckkopplung' if DE else 'Outer hair cells: freq.-selective feedback')],
        [TD('Nichtlinearit\u00e4t' if DE else 'Non-linearity'),
         TD('Quantengatter nichtlinear, Messung kollabiert' if DE else 'Quantum gates non-linear, measurement collapses'),
         TD('Analog \u2192 Spike: Schwellenwertoperation' if DE else 'Analogue \u2192 spike: threshold operation')],
        [TD('Unsch\u00e4rfe' if DE else 'Uncertainty'),
         TD('Heisenberg, aktiv gemanagt (Squeezed states)' if DE else 'Heisenberg, actively managed (squeezed states)'),
         TD('Akust. Unsch\u00e4rfe effektiv unterschritten' if DE else 'Acoustic uncertainty effectively undercut')],
        [TD('Messung' if DE else 'Measurement'),
         TD('Kollaps auf Eigenzustand' if DE else 'Collapse to eigenstate'),
         TD('Mechanik \u2192 Rezeptorpotential \u2192 Spike' if DE else 'Mechanics \u2192 receptor potential \u2192 spike')],
    ],[3.2*cm,5.2*cm,5.8*cm]))

    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        ('<b>Was die Analogie bedeutet:</b> Das Geh\u00f6r realisiert dasselbe '
         '<i>Verarbeitungsprinzip</i> wie ein Quantencomputer: koh\u00e4rente Wellenphysik '
         'mit aktiver Kontrolle. Es ist nicht durch die Grenzen passiver klassischer '
         'Systeme beschr\u00e4nkt. '
         'Ein Quantencomputer ist leistungsf\u00e4higer als ein klassischer Computer '
         'nicht weil er schneller ist, sondern weil er ein anderes Berechnungsprinzip '
         'realisiert. Das Geh\u00f6r ist leistungsf\u00e4higer als Mikrofon\u202f+\u202fFFT '
         'aus demselben Grund.') if DE else
        ('<b>What the analogy means:</b> The auditory system realises the same '
         '<i>processing principle</i> as a quantum computer: coherent wave physics '
         'with active control. It is not constrained by the limits of passive classical systems. '
         'A quantum computer outperforms a classical computer not because it is faster, '
         'but because it realises a different computational principle. '
         'The auditory system outperforms microphone\u202f+\u202fFFT for the same reason.'), sBody))

    # 2.5 Konsequenzen
    story.append(H2('2.5\u2002Designprinzipien f\u00fcr technische H\u00f6rsysteme' if DE else
                    '2.5\u2002Design Principles for Technical Hearing Systems'))
    story.append(Paragraph(
        ('Aus dieser Analyse folgen f\u00fcnf konkrete Designprinzipien:') if DE else
        ('Five concrete design principles follow from this analysis:'), sBody))

    principles = ([
        ('Aktive Resonatoren statt passiver Filter',
         'Frequenzaufl\u00f6sung muss durch Resonanzg\u00fcte entstehen, nicht durch Fensterlänge. '
         'Aktive R\u00fcckkopplungsresonatoren, keine FIR/IIR-Filter.'),
        ('Zeitcodierung parallel zu Ortscodierung',
         'Die zeitliche Feinstruktur des Signals muss parallel zur Frequenzinformation erhalten bleiben. '
         'Spike-Timing-basierte Repr\u00e4sentationen sind fundamentaler als Spektrogramme.'),
        ('Nichtlinearit\u00e4t als Feature',
         'Kompression und Nichtlinearit\u00e4t der Cochlea sind keine Artefakte. '
         'Sie erm\u00f6glichen simultane Verarbeitung gro\u00dfer Dynamikbereiche.'),
        ('Kontinuierliche Verarbeitung ohne Frames',
         'Fensterbasierte Analyse ist eine Notl\u00f6sung des digitalen Paradigmas. '
         'Die Zielarchitektur ist asynchron und kausal \u2014 kein Frame, keine Latenz.'),
        ('Hybride Architektur',
         'Analoges Wellenverarbeitungssystem\u202f+\u202fdigitales Interpretationssystem. '
         'Die Grenze liegt dort, wo die Physik endet und die Symbolverarbeitung beginnt.'),
    ] if DE else [
        ('Active resonators instead of passive filters',
         'Frequency resolution must arise from resonator quality Q, not window length. '
         'Active feedback resonators, not FIR/IIR filters.'),
        ('Temporal coding parallel to place coding',
         'The temporal fine structure of the signal must be preserved alongside frequency information. '
         'Spike-timing-based representations are more fundamental than spectrograms.'),
        ('Non-linearity as a feature',
         'Compression and non-linearity are not artefacts to be compensated. '
         'They enable simultaneous processing of large dynamic ranges.'),
        ('Continuous processing without frames',
         'Window-based analysis is a workaround of the digital paradigm. '
         'The target architecture is asynchronous and causal \u2014 no frame, no latency.'),
        ('Hybrid architecture',
         'Analogue wave processing system\u202f+\u202fdigital interpretation system. '
         'The boundary lies where physics ends and symbol processing begins.'),
    ])
    for i,(title,body) in enumerate(principles):
        story.append(Paragraph(
            f'<b>Prinzip\u202f{i+1}: {title}.</b>\u2002{body}' if DE else
            f'<b>Principle\u202f{i+1}: {title}.</b>\u2002{body}',
            S(f'pr{i}','DV',10,15,5,4,li=10)))

    # Final box
    story.append(Spacer(1,0.5*cm))
    story.append(ibox(
        ('<b>Ein Quantencomputer befindet sich nicht im Gehirn.<br/>'
         'Er befindet sich im Geh\u00f6r.</b><br/><br/>'
         'Nicht weil dort Quantenmechanik herrscht,<br/>'
         'sondern weil dasselbe Verarbeitungsprinzip realisiert ist:<br/>'
         'Koh\u00e4rente aktive Wellenphysik \u00fcberwindet<br/>'
         'die Grenzen passiver klassischer Systeme.') if DE else
        ('<b>A quantum computer is not located in the brain.<br/>'
         'It is located in the auditory system.</b><br/><br/>'
         'Not because quantum mechanics governs it,<br/>'
         'but because the same processing principle is realised:<br/>'
         'Coherent active wave physics overcomes<br/>'
         'the limits of passive classical systems.'),
        bg='#1a1a2e', bc=MID, fs=11))
    # Replace with lighter version for readability
    story[-1] = ibox(
        ('<b>Ein Quantencomputer befindet sich nicht im Gehirn.<br/>'
         'Er befindet sich im Geh\u00f6r.</b><br/><br/>'
         'Nicht weil dort Quantenmechanik herrscht,<br/>'
         'sondern weil dasselbe Verarbeitungsprinzip realisiert ist:<br/>'
         'Koh\u00e4rente aktive Wellenphysik \u00fcberwindet<br/>'
         'die Grenzen passiver klassischer Systeme.') if DE else
        ('<b>A quantum computer is not located in the brain.<br/>'
         'It is located in the auditory system.</b><br/><br/>'
         'Not because quantum mechanics governs it,<br/>'
         'but because the same processing principle is realised:<br/>'
         'Coherent active wave physics overcomes<br/>'
         'the limits of passive classical systems.'),
        bg='#eef2ff', bc=MID, fs=11)

    # ══════════════════════════════════════════════════════════════════════
    # Schlusskapitel: Training statt Technik
    # ══════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(H1(
        '2\u2002Abschluss: Das trainierte Geh\u00f6r als \u00fcberlegene KI-Detektion' if DE else
        '2\u2002Conclusion: The Trained Ear as Superior AI Detection'))

    story.append(Paragraph(
        ('Die vorangegangenen Abschnitte haben gezeigt, dass das Geh\u00f6r ein physikalisches '
         'Verarbeitungssystem ist, das auf der \u03be\u2077-Stufe der T0-Geometrie operiert \u2014 '
         'jenseits der Grenzen passiver mathematischer Analyse, jenseits der '
         'Heisenbergschen Unsch\u00e4rfe f\u00fcr lineare Systeme. '
         'Daraus folgt eine praktische Schlussfolgerung, die in der aktuellen Debatte '
         '\u00fcber KI-generierte Medien kaum geh\u00f6rt wird:') if DE else
        ('The preceding sections have shown that the auditory system is a physical '
         'processing system operating at the \u03be\u2077 rung of T0 geometry \u2014 '
         'beyond the limits of passive mathematical analysis, beyond the '
         'Heisenberg uncertainty for linear systems. '
         'This leads to a practical conclusion that is rarely heard in the current '
         'debate about AI-generated media:'), sBody))

    story.append(ibox(
        ('<b>Wir w\u00e4ren gut bedient, unsere physikalischen F\u00e4higkeiten zu trainieren '
         'statt ausschlie\u00dflich auf technische L\u00f6sungen zu setzen.</b> '
         'Ein trainiertes menschliches Geh\u00f6r wird KI-generierte Fakes '
         'f\u00fcr Jahrzehnte erkennen k\u00f6nnen \u2014 '
         'solange wir es trainieren.') if DE else
        ('<b>We would be well served to train our physical capabilities '
         'rather than relying exclusively on technical solutions.</b> '
         'A trained human ear will be able to detect AI-generated fakes '
         'for decades to come \u2014 as long as we train it.'),
        bg='#fff8e1', bc=ORG, fs=11))

    story.append(H2(
        '2.1\u2002Warum technische Detektion strukturell im Nachteil ist' if DE else
        '2.1\u2002Why Technical Detection is Structurally Disadvantaged'))
    story.append(Paragraph(
        ('KI-generierte Audio- und Videofakes werden mit denselben mathematischen '
         'Werkzeugen erzeugt, mit denen digitale Detektionssysteme sie erkennen sollen: '
         'neuronale Netze, Fourier-Analyse, statistische Mustererkennung. '
         'Das ist ein strukturelles Problem: Der Angreifer und der Verteidiger '
         'operieren auf derselben Schicht \u2014 der digitalen, mathematischen, '
         'symbolverarbeitenden Schicht.') if DE else
        ('AI-generated audio and video fakes are produced with the same mathematical '
         'tools that digital detection systems are supposed to use to identify them: '
         'neural networks, Fourier analysis, statistical pattern recognition. '
         'This is a structural problem: the attacker and the defender '
         'operate on the same layer \u2014 the digital, mathematical, '
         'symbol-processing layer.'), sBody))
    story.append(Paragraph(
        ('Dies erzeugt ein R\u00fcstungsrennen, das der Angreifer strukturell gewinnt: '
         'Eine neue Generatorarchitektur macht den alten Detektor wertlos. '
         'Der Detektor wird nachger\u00fcstet. Der Generator wird verbessert. '
         'Die Zeitverz\u00f6gerung zwischen Angriff und Detektion '
         'w\u00e4chst mit der Komplexit\u00e4t des Systems.') if DE else
        ('This creates an arms race that the attacker structurally wins: '
         'a new generator architecture renders the old detector worthless. '
         'The detector is updated. The generator is improved. '
         'The time lag between attack and detection '
         'grows with the complexity of the system.'), sBody))
    story.append(ibox(
        ('Das menschliche Geh\u00f6r operiert auf einer anderen Schicht: '
         'der physikalischen, subatomaren, \u03be\u2077-kodierten Schicht. '
         'KI-Generatoren erzeugen Signale in der digitalen Dom\u00e4ne. '
         'Die physikalischen Signaturen echter Stimmen, echter R\u00e4ume, '
         'echter Instrumente entstehen durch mechanische Prozesse '
         'auf der atomaren Skala \u2014 und diese Signaturen '
         'sind in der digitalen Dom\u00e4ne nicht vollst\u00e4ndig reproduzierbar.') if DE else
        ('The human ear operates on a different layer: '
         'the physical, subatomic, \u03be\u2077-encoded layer. '
         'AI generators produce signals in the digital domain. '
         'The physical signatures of real voices, real rooms, '
         'real instruments arise from mechanical processes '
         'at the atomic scale \u2014 and these signatures '
         'are not fully reproducible in the digital domain.'),
        bg='#e8f0ff', bc=BLUE, fs=10))

    story.append(H2(
        '2.2\u2002Was ein trainiertes Geh\u00f6r erkennt' if DE else
        '2.2\u2002What a Trained Ear Detects'))
    story.append(Paragraph(
        ('Ein Stimmklang entsteht durch Vibration der Stimmlippen, '
         'Resonanz des Vokaltrakt-Rohrs, Abstrahlung durch Lippen und Nase. '
         'Jeder dieser Prozesse ist mechanisch, nichtlinear, '
         'von K\u00f6rperbau und Tagesform abh\u00e4ngig. '
         'Die akustische Signatur einer echten Stimme tr\u00e4gt '
         'die Fingerabdr\u00fccke dieser Mechanik:') if DE else
        ('A vocal sound arises from vibration of the vocal folds, '
         'resonance of the vocal tract tube, radiation through lips and nose. '
         'Each of these processes is mechanical, non-linear, '
         'dependent on physiology and condition of the day. '
         'The acoustic signature of a real voice carries '
         'the fingerprints of this mechanics:'), sBody))

    markers = ([
        'Mikrofluktuationen in Grundfrequenz und Amplitude (Jitter, Shimmer) '
        '\u2014 chaotisch, nicht reproduzierbar, aus Atemstrom und Muskelspannung',
        'Raumakustische Faltung: Reflexionen, Diffusion, Absorptionsmuster '
        'des physischen Raums, in dem gesprochen wurde',
        'Artikulatorische Koartikulation: \u00dcberg\u00e4nge zwischen Lauten '
        'entstehen durch Tr\u00e4gheit und Elastizit\u00e4t von Zunge, Lippen, Gaumen',
        'Atemger\u00e4usch-Textur: turbulente Str\u00f6mung in Kehle und Mund, '
        'jedes Mal einzigartig',
        'Subharmonische und Rauschwellenanteile aus echten Stimmlippen-Schlie\u00dfungsimpulsen',
    ] if DE else [
        'Micro-fluctuations in fundamental frequency and amplitude (jitter, shimmer) '
        '\u2014 chaotic, non-reproducible, arising from airflow and muscle tension',
        'Room acoustic convolution: reflections, diffusion, absorption patterns '
        'of the physical space in which speech was produced',
        'Articulatory coarticulation: transitions between phonemes '
        'arise from inertia and elasticity of tongue, lips, palate',
        'Breath noise texture: turbulent flow in throat and mouth, '
        'unique every time',
        'Subharmonics and noise components from real vocal fold closure impulses',
    ])
    for m in markers:
        story.append(bullet(m))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        ('KI-Generatoren lernen die <i>statistischen Mittelwerte</i> dieser Merkmale '
         'aus Trainingsdaten. Sie erzeugen wahrscheinliche Signale \u2014 '
         'aber keine physikalisch generierten. '
         'Die Abwesenheit echter Mechanik hinterl\u00e4sst systematische Spuren: '
         'zu regul\u00e4re Jitter-Verteilungen, '
         'fehlende Raumakustik-Konsistenz, '
         'untypische Koartikulationsmuster, '
         '\u00fcbergl\u00e4ttete Amplituenh\u00fcllkurven.') if DE else
        ('AI generators learn the <i>statistical averages</i> of these features '
         'from training data. They produce probable signals \u2014 '
         'but not physically generated ones. '
         'The absence of real mechanics leaves systematic traces: '
         'overly regular jitter distributions, '
         'missing room acoustic consistency, '
         'atypical coarticulation patterns, '
         'over-smoothed amplitude envelopes.'), sBody))
    story.append(Paragraph(
        ('Ein Laie h\u00f6rt: \u201eDas klingt irgendwie komisch.\u201c '
         'Ein trainiertes Geh\u00f6r h\u00f6rt: '
         '\u201eDer Atemdruck-Verlauf stimmt nicht mit dem Satzrhythmus \u00fcberein.\u201c '
         'Das ist kein mystisches Talent \u2014 es ist physikalisches Mustererkennen '
         'auf der richtigen Schicht.') if DE else
        ('A layperson hears: \u201cThat sounds somehow odd.\u201c '
         'A trained ear hears: '
         '\u201cThe breath-pressure profile does not match the sentence rhythm.\u201c '
         'This is not a mystical talent \u2014 it is physical pattern recognition '
         'on the correct layer.'), sBody))

    story.append(H2(
        '2.3\u2002Training statt Vertrauen in technische L\u00f6sungen' if DE else
        '2.3\u2002Training Instead of Trust in Technical Solutions'))
    story.append(Paragraph(
        ('Die Kontrolle von Videos und Audioaufnahmen auf KI-Fakes st\u00fctzt sich '
         'heute \u00fcberwiegend auf automatische Detektionssysteme. '
         'Das ist aus denselben Gr\u00fcnden problematisch wie digitale Audioanalyse '
         'gegen\u00fcber physikalischer Cochlea-Verarbeitung: '
         'Die technische L\u00f6sung operiert auf der falschen Schicht.') if DE else
        ('The verification of videos and audio recordings for AI fakes relies today '
         'predominantly on automated detection systems. '
         'This is problematic for the same reasons as digital audio analysis '
         'versus physical cochlear processing: '
         'the technical solution operates on the wrong layer.'), sBody))

    story.append(mkt([
        [TH('Ansatz' if DE else 'Approach'),
         TH('Schicht' if DE else 'Layer'),
         TH('R\u00fcstungsrennen?' if DE else 'Arms race?'),
         TH('Zeitlicher Vorteil' if DE else 'Temporal advantage')],
        [TD('Automatischer KI-Detektor' if DE else 'Automated AI detector'),
         TD('Digital / mathematisch' if DE else 'Digital / mathematical'),
         TD('Ja \u2014 Generator gewinnt strukturell' if DE else 'Yes \u2014 generator wins structurally'),
         TD('Monatelange Verz\u00f6gerung' if DE else 'Months of lag')],
        [TD('Trainiertes menschliches Geh\u00f6r' if DE else 'Trained human ear'),
         TD('Physikalisch / \u03be\u2077-kodiert' if DE else 'Physical / \u03be\u2077-encoded'),
         TD('Nein \u2014 andere Schicht, nicht angreifbar' if DE else 'No \u2014 different layer, not attackable'),
         TD('Sofort, jahrzehntelang stabil' if DE else 'Immediate, stable for decades')],
        [TD('Kombiniert: Geh\u00f6r + Detektor' if DE else 'Combined: ear + detector'),
         TD('Beide Schichten' if DE else 'Both layers'),
         TD('Teils \u2014 physikalische Schicht unver\u00e4nderlich' if DE else 'Partly \u2014 physical layer unchangeable'),
         TD('Optimal' if DE else 'Optimal')],
    ],[5.0*cm,3.5*cm,4.5*cm,3.2*cm]))
    story.append(Paragraph(
        'Vergleich der Ans\u00e4tze zur Detektion von KI-generierten Fakes.' if DE else
        'Comparison of approaches to detecting AI-generated fakes.', sCap))

    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        ('Was folgt daraus? Training. Nicht mehr Technik, sondern mehr Bewusstsein '
         'f\u00fcr das, was das Geh\u00f6r kann und wie man es sch\u00e4rft. '
         'Radiojournalisten und Tonmeister entwickeln dieses Geh\u00f6r im Berufsalltag. '
         'Es ist kein Geheimnis, wie: Aktives H\u00f6ren, bewusstes Vergleichen '
         'echter und synthetischer Stimmen, Analyse von Raumakustik, '
         'Arbeit mit unbearbeitetem Material.') if DE else
        ('What follows from this? Training. Not more technology, but more awareness '
         'of what the ear can do and how to sharpen it. '
         'Radio journalists and sound engineers develop this ear in their daily work. '
         'It is no secret how: active listening, conscious comparison '
         'of real and synthetic voices, analysis of room acoustics, '
         'work with unprocessed material.'), sBody))

    story.append(H2(
        '2.4\u2002Das trainierte Geh\u00f6r als \u00fcberlegener Detektor \u2014 auf Jahrzehnte' if DE else
        '2.4\u2002The Trained Ear as Superior Detector \u2014 for Decades'))
    story.append(Paragraph(
        ('KI-Generatoren werden besser. Aber sie werden besser in der digitalen Dom\u00e4ne: '
         'sie n\u00e4hern sich statistisch besser an echte Stimmen an. '
         'Sie werden nicht besser darin, echte Mechanik zu simulieren \u2014 '
         'weil echte Mechanik nicht digital ist. '
         'Die Stimmlippen-Turbulenz, die Raumimpulsantwort, der Atemdruck-Verlauf: '
         'diese entstehen in der physikalischen Welt, auf der \u03be\u2077-Skala, '
         'und kein Generator, der in der digitalen Dom\u00e4ne operiert, '
         'kann sie vollst\u00e4ndig reproduzieren.') if DE else
        ('AI generators will improve. But they will improve in the digital domain: '
         'they will statistically approximate real voices more closely. '
         'They will not improve at simulating real mechanics \u2014 '
         'because real mechanics is not digital. '
         'The vocal fold turbulence, the room impulse response, the breath-pressure profile: '
         'these arise in the physical world, at the \u03be\u2077 scale, '
         'and no generator operating in the digital domain '
         'can fully reproduce them.'), sBody))
    story.append(Paragraph(
        ('Das trainierte Geh\u00f6r erkennt diese fehlende Physik. '
         'Nicht weil es besser rechnet \u2014 sondern weil es selbst physikalisch ist. '
         'Es ist ein \u03be\u2077-System, das \u03be\u2077-Signaturen erkennt. '
         'Kein digitales System kann diese Ebene angreifen, '
         'weil es auf einer anderen Ebene operiert.') if DE else
        ('The trained ear detects this missing physics. '
         'Not because it computes better \u2014 but because it is itself physical. '
         'It is a \u03be\u2077 system detecting \u03be\u2077 signatures. '
         'No digital system can attack this level, '
         'because it operates on a different level.'), sBody))

    story.append(Spacer(1,0.3*cm))
    story.append(ibox(
        ('<b>Schlussfolgerung:</b> Wir verf\u00fcgen bereits \u00fcber den \u00fcberlegenen '
         'KI-Detektor \u2014 er sitzt zwischen unseren Ohren. '
         'Er operiert auf der physikalischen Schicht, '
         'ist nicht durch digitale Gegenmassnahmen angreifbar, '
         'arbeitet in Echtzeit ohne Latenz, '
         'und wird durch Training besser, nicht durch Rechenpower.<br/><br/>'
         'Die Frage ist nicht, ob wir der Technologie vertrauen sollen. '
         'Die Frage ist, warum wir aufgeh\u00f6rt haben, '
         'unserem eigenen Geh\u00f6r zu vertrauen.') if DE else
        ('<b>Conclusion:</b> We already possess the superior AI detector \u2014 '
         'it sits between our ears. '
         'It operates on the physical layer, '
         'is not attackable by digital countermeasures, '
         'works in real time without latency, '
         'and improves through training, not through computing power.<br/><br/>'
         'The question is not whether we should trust technology. '
         'The question is why we have stopped '
         'trusting our own ears.'),
        bg='#eef2ff', bc=MID, fs=11))

    story.append(Spacer(1,0.5*cm))
    story.append(HRFlowable(width=PW, thickness=1.5, color=DARK, spaceAfter=10))
    story.append(Paragraph(
        ('<i>Das menschliche Geh\u00f6r ist ein physikalischer Quantenprozessor '
         'auf der \u03be\u2077-Skala der T0-Geometrie. '
         'Es arbeitet jenseits der Heisenbergschen Unsch\u00e4rfe passiver Systeme, '
         'jenseits der Frame-Grenzen digitaler Abtastung, '
         'jenseits der Reichweite digitaler F\u00e4lschungen. '
         'Trainieren wir es.</i>') if DE else
        ('<i>The human ear is a physical quantum processor '
         'at the \u03be\u2077 scale of T0 geometry. '
         'It operates beyond the Heisenberg uncertainty of passive systems, '
         'beyond the frame limits of digital sampling, '
         'beyond the reach of digital forgeries. '
         'Let us train it.</i>'),
        S('fin','DV-I',11,17,8,0,TA_CENTER,MID)))

    story.append(Spacer(1,1.0*cm))

    doc = T0Doc(out,
        title='Dok.170: Analoge Vorverarbeitung als Rechenprinzip' if DE else
              'Doc.170: Analogue Pre-processing as a Computational Principle',
        author='Johann Pascher')
    doc.multiBuild(story)
    print(f'{"DE" if DE else "EN"} \u2192 {out}')

build('de')
build('en')
