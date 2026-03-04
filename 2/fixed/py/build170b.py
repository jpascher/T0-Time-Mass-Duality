"""
Dokument 170b – Vereinfachte Version ohne xi-Bezüge
Das Gehör als physikalischer Vorverarbeiter
und der trainierte Mensch als überlegener KI-Detektor
Johann Pascher, März 2026
"""
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
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

BASE = '/usr/share/fonts/truetype/dejavu/'
for nm, fp in [('DV','DejaVuSans.ttf'),('DV-B','DejaVuSans-Bold.ttf'),
               ('DV-I','DejaVuSans-Oblique.ttf'),('DV-M','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(nm, BASE+fp))

PW   = A4[0]-5*cm
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
sH1    = S('H1','DV-B',13,18,18,6,TA_LEFT,MID)
sH2    = S('H2','DV-B',11,15,12,5,TA_LEFT,BLUE)
sH3    = S('H3','DV-B',10,14,8,4,TA_LEFT,TEAL)
sBody  = S('BO','DV',10,16,0,7)
sQuote = S('QU','DV-I',10,16,6,6,TA_JUSTIFY,DARK,li=20,ri=20)
sCap   = S('CA','DV-I',9,13,2,8,TA_CENTER,GRY)
sTOCH  = S('TCH','DV-B',13,18,0,10,TA_LEFT,MID)
sTOC1  = S('TC1','DV-B',10,14,2,2,TA_LEFT,DARK)
sTOC2  = S('TC2','DV',9,13,1,1,TA_LEFT,DARK,li=12)
sBullet= S('BU','DV',10,16,0,4,TA_JUSTIFY,DARK,li=14)

def TH(t): return Paragraph(t,S('th','DV-B',9,13,0,0,TA_LEFT,WHITE))
def TD(t): return Paragraph(t,S('td','DV',9,13,0,0,TA_LEFT,DARK))
def TB(t): return Paragraph(t,S('tb','DV-B',9,13,0,0,TA_LEFT,TEAL))

BASE_TS=[('BACKGROUND',(0,0),(-1,0),MID),
         ('ROWBACKGROUNDS',(0,1),(-1,-1),[LGRY,WHITE]),
         ('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#bbb')),
         ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
         ('LEFTPADDING',(0,0),(-1,-1),9),('VALIGN',(0,0),(-1,-1),'TOP')]

def mkt(rows,cols,extra=None):
    t=Table(rows,colWidths=cols,repeatRows=1)
    ts=list(BASE_TS)
    if extra: ts.extend(extra)
    t.setStyle(TableStyle(ts)); return t

def ibox(text,bg='#e8f4f8',bc=BLUE,fs=10,italic=False):
    fn='DV-I' if italic else 'DV'
    p=Paragraph(text,S('ib',fn,fs,17,0,0,TA_JUSTIFY,bc))
    t=Table([[p]],colWidths=[PW])
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1.5,bc),
        ('BACKGROUND',(0,0),(-1,-1),colors.HexColor(bg)),
        ('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12),
        ('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),16)]))
    return t

def bullet(text):
    return Paragraph(f'\u2022\u2002{text}',sBullet)

def H1(text):
    p=Paragraph(text,sH1); p._tocLevel=0; return p
def H2(text):
    p=Paragraph(text,sH2); p._tocLevel=1; return p
def H3(text):
    return Paragraph(text,sH3)

class T0Doc(BaseDocTemplate):
    def __init__(self,path,**kw):
        BaseDocTemplate.__init__(self,path,pagesize=A4,
            leftMargin=2.5*cm,rightMargin=2.5*cm,
            topMargin=2.5*cm,bottomMargin=2.5*cm,**kw)
        f=Frame(2.5*cm,2.5*cm,PW,A4[1]-5*cm,id='main')
        self.addPageTemplates([PageTemplate('main',[f])])
    def afterFlowable(self,flowable):
        lvl=getattr(flowable,'_tocLevel',None)
        if lvl is not None:
            self.notify('TOCEntry',(lvl,flowable.getPlainText(),self.page))


def build(lang):
    DE=(lang=='de')
    out=f'/mnt/user-data/outputs/T0_170b_Gehoer_{"De" if DE else "En"}.pdf'
    story=[]

    # TOC
    toc=TableOfContents(); toc.levelStyles=[sTOC1,sTOC2]; toc.dotsMinLevel=0
    story.append(Paragraph('Inhaltsverzeichnis' if DE else 'Table of Contents',sTOCH))
    story.append(Spacer(1,0.3*cm)); story.append(toc); story.append(PageBreak())

    # Titel
    story.append(Paragraph('Dokument 170b' if DE else 'Document 170b',sMeta))
    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        'Das Geh\u00f6r als physikalischer Vorverarbeiter' if DE else
        'The Ear as a Physical Pre-processor',sTitle))
    story.append(Paragraph(
        'Und warum ein trainiertes Geh\u00f6r KI-Fakes erkennt \u2014 auf Jahrzehnte' if DE else
        'And why a trained ear detects AI fakes \u2014 for decades',sSubT))
    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        'Johann Pascher \u00b7 M\u00e4rz 2026' if DE else
        'Johann Pascher \u00b7 March 2026',sMeta))
    story.append(HRFlowable(width=PW,thickness=2,color=DARK,spaceAfter=16))

    story.append(ibox(
        ('Spracherkennung und KI-Audiogenerierung haben enorme Fortschritte gemacht. '
         'Dennoch \u00fcbertrifft das menschliche Geh\u00f6r digitale Systeme in bestimmten '
         'Aufgaben nach wie vor. Das hat eine strukturelle Ursache: '
         'Das Geh\u00f6r ist kein biologisches Mikrofon \u2014 es ist ein physikalischer '
         'Rechner, der Schall verarbeitet, bevor das Gehirn auch nur eine einzige '
         'bewusste Operation durchf\u00fchrt. '
         'Und ein trainiertes Geh\u00f6r erkennt KI-generierte Fakes '
         'auf einer Ebene, die kein digitaler Generator je vollst\u00e4ndig erreichen kann.') if DE else
        ('Speech recognition and AI audio generation have made enormous advances. '
         'Yet the human ear still surpasses digital systems in certain tasks. '
         'This has a structural cause: '
         'the ear is not a biological microphone \u2014 it is a physical computer '
         'that processes sound before the brain performs a single '
         'conscious operation. '
         'And a trained ear detects AI-generated fakes '
         'at a level no digital generator can ever fully reach.'),
        bg='#e8f4f8',bc=DARK,fs=10))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════
    # Kapitel 1: Die Verarbeitungskette des Gehörs
    # ══════════════════════════════════════════════════════════════════════
    story.append(H1(
        '1\u2002Das Geh\u00f6r rechnet, bevor das Gehirn denkt' if DE else
        '1\u2002The Ear Computes Before the Brain Thinks'))

    story.append(H2('1.1\u2002Eine lang bekannte, wenig beachtete Diskrepanz' if DE else
                    '1.1\u2002A Long-known, Little-noticed Discrepancy'))
    story.append(Paragraph(
        ('Wer sich \u00fcber Jahrzehnte mit Tonsignalen besch\u00e4ftigt, begegnet einer '
         'hartn\u00e4ckigen Beobachtung: Menschen unterscheiden Kl\u00e4nge, Stimmen '
         'und Musikinstrumente in Bruchteilen einer Sekunde \u2014 aus \u00fcberlagerten '
         'Signalen, bei schlechtem Signal-Rausch-Verh\u00e4ltnis, in l\u00e4rmiger Umgebung. '
         'Digitale Systeme tun sich damit nach wie vor schwer, '
         'obwohl sie mit gewaltiger Rechenleistung arbeiten.') if DE else
        ('Anyone who has worked with sound signals over decades encounters a '
         'persistent observation: humans distinguish sounds, voices, and musical '
         'instruments in fractions of a second \u2014 from overlapping signals, '
         'in poor signal-to-noise conditions, in noisy environments. '
         'Digital systems still struggle with this, '
         'despite working with enormous computing power.'),sBody))

    story.append(Paragraph(
        'Konkret bleibt das menschliche Geh\u00f6r \u00fcberlegen bei:' if DE else
        'Specifically, the human ear remains superior at:',sBody))
    for t in ([
        'Trennung gleichzeitiger Sprecher in einem lauten Raum (Cocktailpartyproblem)',
        'Identifikation eines einzelnen Instruments im vollen Orchesterklang',
        'Erkennung kurzer, transienter Klangereignisse unter 20 Millisekunden',
        'H\u00f6ren weit unterhalb von Rauschpegeln, bei denen digitale Verfahren versagen',
        'Sofortige Stimmidentifikation selbst bei stark verrauschtem Signal',
    ] if DE else [
        'Separating simultaneous speakers in a noisy room (cocktail-party problem)',
        'Identifying a single instrument within a full orchestral texture',
        'Detecting short transient sound events below 20 milliseconds',
        'Hearing far below noise levels at which digital methods fail',
        'Immediate voice identification even in heavily noisy signals',
    ]):
        story.append(bullet(t))

    story.append(Spacer(1,0.3*cm))
    story.append(ibox(
        ('Die Ursache ist nicht, dass digitale Systeme noch nicht leistungsf\u00e4hig genug sind. '
         'Die Ursache ist strukturell: Das Geh\u00f6r und digitale Systeme '
         'verarbeiten Schall auf grundlegend verschiedenen Ebenen.') if DE else
        ('The cause is not that digital systems are not yet powerful enough. '
         'The cause is structural: the ear and digital systems '
         'process sound on fundamentally different levels.'),
        bg='#fff8e1',bc=ORG,fs=10))

    story.append(H2('1.2\u2002Was das Geh\u00f6r macht, bevor das Gehirn eingreift' if DE else
                    '1.2\u2002What the Ear Does Before the Brain Intervenes'))
    story.append(Paragraph(
        ('Das Geh\u00f6r ist keine passive Aufnahmevorrichtung. '
         'Es ist eine mehrstufige analoge Verarbeitungsanlage, '
         'die das Schallsignal in weniger als zehn Millisekunden '
         'vollst\u00e4ndig vorverarbeitet \u2014 ohne Takt, ohne Speicher, ohne Digitalisierung.') if DE else
        ('The ear is not a passive recording device. '
         'It is a multi-stage analogue processing unit '
         'that fully pre-processes the sound signal in less than ten milliseconds '
         '\u2014 without a clock, without memory, without digitisation.'),sBody))

    # Ear image
    story.append(Spacer(1,0.2*cm))
    story.append(Image('/home/claude/ear_anatomy.png',
                       width=PW, height=PW*(1090/2000)))
    story.append(Paragraph(
        ('Anatomie des menschlichen Geh\u00f6rs. '
         'Jede Stufe \u2014 Ohrmuschel, Geh\u00f6rgang, Trommelfell, '
         'Geh\u00f6rkn\u00f6chelchen, Cochlea \u2014 ist ein analoger Vorverarbeiter.') if DE else
        ('Anatomy of the human ear. '
         'Every stage \u2014 pinna, ear canal, eardrum, '
         'ossicles, cochlea \u2014 is an analogue pre-processor.'),sCap))
    story.append(Spacer(1,0.4*cm))

    # Die vier Stufen
    stufen = ([
        ('Ohrmuschel: Rechnen durch Form',
         'Die Geometrie der Ohrmuschel filtert Schall frequenz- und richtungsabh\u00e4ngig \u2014 '
         'passiv, ohne Energie. Sie kodiert r\u00e4umliche Information in das Frequenzspektrum. '
         'Ein Mikrofon kann das nicht. Eine Software kann es nachrechnen, '
         'braucht daf\u00fcr aber mehrere Mikrofone und erhebliche Verarbeitungszeit.'),
        ('Mittelohr: Anpassung und Schutz',
         'Die drei Geh\u00f6rkn\u00f6chelchen (Hammer, Amboss, Steigb\u00fcgel) passen den '
         'Schallwiderstand zwischen Luft und Innenohrfl\u00fcssigkeit an \u2014 '
         'und d\u00e4mpfen bei zu lauten Signalen automatisch, '
         'noch bevor das Trommelfell Schaden nehmen kann.'),
        ('Cochlea: Der mechanische Frequenzanalysator',
         'Die Hörschnecke enthält die Basilarmembran: ein spiralf\u00f6rmiges Band, '
         'das an verschiedenen Stellen auf verschiedene Frequenzen anspricht. '
         'Hohe T\u00f6ne (bis 20\u2009kHz) erregen den Eingang, tiefe T\u00f6ne (ab 20\u2009Hz) '
         'das Ende. Die Schallwelle zerlegt sich ohne jeden Rechenvorgang '
         'in ihr Frequenzspektrum \u2014 weil die Mechanik des Systems so gebaut ist.'),
        ('\u00c4u\u00dfere Haarzellen: Aktive Verst\u00e4rkung und Sch\u00e4rfung',
         'Das Entscheidende: Die Cochlea ist kein passives System. '
         'Die \u00e4u\u00dferen Haarzellen verst\u00e4rken aktiv bestimmte Frequenzen '
         'durch mechanische R\u00fcckkopplung. Sie fungieren als biologischer '
         'analoger Verst\u00e4rker mit automatischer Frequenzabstimmung \u2014 '
         'auf jedem der \u00fcber 3\u2009000 Frequenzkan\u00e4le gleichzeitig.'),
    ] if DE else [
        ('Pinna: Computing through shape',
         'The geometry of the pinna filters sound as a function of frequency and direction \u2014 '
         'passively, without energy. It encodes spatial information into the frequency spectrum. '
         'A microphone cannot do this. Software can compute it afterwards, '
         'but needs several microphones and considerable processing time.'),
        ('Middle ear: Matching and protection',
         'The three ossicles (malleus, incus, stapes) match the acoustic impedance '
         'between air and inner-ear fluid \u2014 '
         'and automatically dampen excessively loud signals '
         'before the eardrum can be damaged.'),
        ('Cochlea: The mechanical frequency analyser',
         'The cochlea contains the basilar membrane: a spiral ribbon '
         'that responds to different frequencies at different positions. '
         'High tones (up to 20\u2009kHz) excite the entrance, low tones (from 20\u2009Hz) '
         'the far end. The sound wave decomposes into its frequency spectrum '
         'without any computation \u2014 because the mechanics of the system are built that way.'),
        ('Outer hair cells: Active amplification and sharpening',
         'The decisive element: the cochlea is not a passive system. '
         'The outer hair cells actively amplify specific frequencies '
         'through mechanical feedback. They act as a biological '
         'analogue amplifier with automatic frequency tuning \u2014 '
         'on each of the more than 3\u2009000 frequency channels simultaneously.'),
    ])

    for title,body in stufen:
        story.append(H3(title))
        story.append(Paragraph(body,sBody))

    story.append(Paragraph(
        ('Das Ergebnis: Was beim Gehirn ankommt, ist keine Rohdaten\u00fcbertragung. '
         'Es ist eine bereits aufbereitete akustische Szene: '
         'spektral zerlegt, r\u00e4umlich verortet, '
         'dynamisch komprimiert, selektiv verst\u00e4rkt. '
         'In weniger als zehn Millisekunden, ohne Takt, ohne Rechenpause.') if DE else
        ('The result: what reaches the brain is not a raw data transmission. '
         'It is an already prepared acoustic scene: '
         'spectrally decomposed, spatially located, '
         'dynamically compressed, selectively amplified. '
         'In less than ten milliseconds, without a clock, without a processing pause.'),sBody))

    story.append(ibox(
        'Die Physik rechnet. Das Gehirn interpretiert.' if DE else
        'Physics computes. The brain interprets.',
        bg='#f0fff0',bc=GRN,fs=12,italic=True))

    # ── 1.3 Unschärfe ──────────────────────────────────────────────────────
    story.append(H2(
        '1.3\u2002Das Geh\u00f6r und die Grenzen der Signaltheorie' if DE else
        '1.3\u2002The Ear and the Limits of Signal Theory'))
    story.append(Paragraph(
        ('In der Signalverarbeitung gibt es ein fundamentales Limit: '
         'Je k\u00fcrzer man ein Signal analysiert, desto ungenauer ist die '
         'Frequenzinformation \u2014 und umgekehrt. '
         'Dieses Prinzip gilt f\u00fcr jeden passiven mathematischen Analysator, '
         'der ein Signal speichert und dann auswertet.') if DE else
        ('In signal processing there is a fundamental limit: '
         'the shorter the time window used to analyse a signal, '
         'the less precise the frequency information \u2014 and vice versa. '
         'This principle applies to every passive mathematical analyser '
         'that stores and then evaluates a signal.'),sBody))
    story.append(Paragraph(
        ('Das Geh\u00f6r ist kein solcher Analysator. '
         'Es speichert kein Signal und wertet es anschlie\u00dfend aus. '
         'Es reagiert physikalisch in Echtzeit: '
         'Die Basilarmembran schwingt \u2014 kontinuierlich, ohne Frame, ohne Takt. '
         'Zeit- und Frequenzinformation entstehen durch <i>verschiedene physikalische Prozesse</i>, '
         'nicht durch denselben mathematischen Kompromiss. '
         'Das Geh\u00f6r umgeht das theoretische Limit, weil es ein anderes System ist.') if DE else
        ('The ear is not such an analyser. '
         'It does not store a signal and evaluate it afterwards. '
         'It responds physically in real time: '
         'the basilar membrane vibrates \u2014 continuously, without frames, without a clock. '
         'Time and frequency information arise from <i>different physical processes</i>, '
         'not from the same mathematical trade-off. '
         'The ear circumvents the theoretical limit because it is a different kind of system.'),sBody))

    story.append(Paragraph(
        ('Dazu kommt das Phase-Locking: Die Hörnervfasern feuern ihre Impulse '
         'phasengekoppelt mit der Schallwelle \u2014 bis etwa 4\u2009kHz '
         'bleibt die vollst\u00e4ndige Zeitstruktur des Signals im neuronalen Code erhalten. '
         'Frequenz und Zeit sind nicht gegeneinander abgetauscht '
         '\u2014 sie existieren <i>gleichzeitig</i> in der Nervenaktivit\u00e4t.') if DE else
        ('Additionally, phase-locking occurs: auditory nerve fibres fire their impulses '
         'phase-coupled to the sound wave \u2014 up to approximately 4\u2009kHz '
         'the complete temporal structure of the signal is preserved in the neural code. '
         'Frequency and time are not traded against each other '
         '\u2014 they exist <i>simultaneously</i> in the nerve activity.'),sBody))

    story.append(ibox(
        ('<b>Provokante These:</b> Das Geh\u00f6r ist ein physikalischer Quantenprozessor '
         '\u2014 nicht im technischen Sinn von Qubits, '
         'aber im strukturellen Sinn: ein koh\u00e4rentes Wellensystem '
         'mit aktiver R\u00fcckkopplung, das Informationsverarbeitung leistet, '
         'die passive klassische Systeme prinzipiell nicht erreichen k\u00f6nnen. '
         'Die Grenze liegt nicht an Rechenleistung \u2014 '
         'sie liegt an der falschen Architektur.') if DE else
        ('<b>Provocative thesis:</b> The ear is a physical quantum processor '
         '\u2014 not in the technical sense of qubits, '
         'but in the structural sense: a coherent wave system '
         'with active feedback that achieves information processing '
         'that passive classical systems cannot in principle reach. '
         'The limit is not computing power \u2014 '
         'it is the wrong architecture.'),
        bg='#e8f0ff',bc=BLUE,fs=10))

    # ── 1.4 Tiere ──────────────────────────────────────────────────────────
    story.append(H2('1.4\u2002Tiere als lebender Beweis' if DE else
                    '1.4\u2002Animals as Living Proof'))
    story.append(Paragraph(
        ('Flederm\u00e4use orten Insekten auf wenige Zentimeter durch Ultraschall-Echolokation '
         '\u2014 in absoluter Dunkelheit, w\u00e4hrend sie fliegen, '
         'in einer Umgebung mit vielen anderen Flederm\u00e4usen. '
         'Die r\u00e4umliche Aufl\u00f6sung und Verarbeitungsgeschwindigkeit dieser Leistung '
         'w\u00e4re f\u00fcr ein digitales System, das dieselbe Aufgabe rechnerisch l\u00f6sen soll, '
         'bei der Gehirngr\u00f6\u00dfe einer Fledermaus schlicht unm\u00f6glich.') if DE else
        ('Bats locate insects to within a few centimetres through ultrasonic echolocation '
         '\u2014 in total darkness, while flying, '
         'in an environment with many other bats. '
         'The spatial resolution and processing speed of this performance '
         'would be simply impossible for a digital system solving the same task computationally '
         'at the brain size of a bat.'),sBody))
    story.append(Paragraph(
        ('Delfine analysieren Ultraschallreflexe so pr\u00e4zise, '
         'dass sie Materialien hinter Hindernissen identifizieren k\u00f6nnen. '
         'Der Schimpanse erkennt eine Stimme aus seiner sozialen Gruppe '
         'auch nach Jahren sofort \u2014 aus wenigen Silben. '
         'Das Nervensystem dieser Tiere ist f\u00fcr digitale Verarbeitung '
         'dieser Komplexit\u00e4t bei weitem nicht gro\u00df genug.') if DE else
        ('Dolphins analyse ultrasonic reflections so precisely '
         'that they can identify materials behind obstacles. '
         'The chimpanzee immediately recognises a voice from its social group '
         'even after years \u2014 from just a few syllables. '
         'The nervous systems of these animals are far too small '
         'for digital processing of this complexity.'),sBody))
    story.append(ibox(
        'Die Physik rechnet. Das Nervensystem interpretiert.' if DE else
        'Physics computes. The nervous system interprets.',
        bg='#f0fff0',bc=GRN,fs=11,italic=True))

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════
    # Kapitel 2: Physik ist in Materie kodiert
    # ══════════════════════════════════════════════════════════════════════
    story.append(H1(
        '2\u2002Physik ist in Materie kodiert: '
        'Kristalle, Cochlea und nat\u00fcrliche Signale' if DE else
        '2\u2002Physics is Encoded in Matter: '
        'Crystals, Cochlea, and Natural Signals'))

    story.append(Paragraph(
        ('Hinter der Leistungsf\u00e4higkeit des Geh\u00f6rs steckt ein tieferes Prinzip, '
         'das \u00fcber Biologie hinausgeht. Dieselbe Grundidee findet sich in '
         'Kristallen, in photonischen Rechensystemen, '
         'und \u2014 auf fundamentaler physikalischer Ebene \u2014 '
         'in der Struktur der Materie selbst.') if DE else
        ('Behind the performance of the ear lies a deeper principle '
         'that goes beyond biology. The same fundamental idea is found in '
         'crystals, in photonic computing systems, '
         'and \u2014 at a fundamental physical level \u2014 '
         'in the structure of matter itself.'),sBody))

    story.append(H2('2.1\u2002Kristalle rechnen durch ihre Geometrie' if DE else
                    '2.1\u2002Crystals Compute Through Their Geometry'))
    story.append(Paragraph(
        ('Ein Kristall l\u00f6st kein Eigenwertproblem \u2014 er <i>ist</i> die L\u00f6sung. '
         'Wenn Licht durch einen Kristall f\u00e4llt, wird es gebeugt, '
         'gefiltert, reflektiert \u2014 nach Maßgabe der Gittergeometrie. '
         'Kein Algorithmus rechnet. Die Physik des Gitters '
         'f\u00fchrt die Berechnung durch, indem sie existiert.') if DE else
        ('A crystal does not solve an eigenvalue problem \u2014 it <i>is</i> the solution. '
         'When light passes through a crystal, it is diffracted, '
         'filtered, reflected \u2014 according to the lattice geometry. '
         'No algorithm computes. The physics of the lattice '
         'performs the computation by existing.'),sBody))
    story.append(Paragraph(
        ('Die Gitterkonstante eines Kristalls \u2014 der Abstand zwischen den Atomen \u2014 '
         'ist durch die atomare Skala vorgegeben: Bindungsl\u00e4ngen, '
         'Atomradien, chemische Bindungsenergie. '
         'Diese Skala ist dieselbe wie die Frequenzskala der Cochlea. '
         'Kein Zufall: Beide Systeme sind aus Materie gebaut, '
         'und Materie hat ihre fundamentalen Skalen '
         'durch die Konstanten der Physik vorgegeben \u2014 '
         'Elektronenmasse, Feinstrukturkonstante, Rydberg-Energie.') if DE else
        ('The lattice constant of a crystal \u2014 the distance between atoms \u2014 '
         'is set by the atomic scale: bond lengths, '
         'atomic radii, chemical bond energy. '
         'This scale is the same as the frequency scale of the cochlea. '
         'Not a coincidence: both systems are built from matter, '
         'and matter has its fundamental scales '
         'set by the constants of physics \u2014 '
         'electron mass, fine-structure constant, Rydberg energy.'),sBody))

    story.append(H2('2.2\u2002Die Cochlea und die logarithmische Skala der Natur' if DE else
                    '2.2\u2002The Cochlea and the Logarithmic Scale of Nature'))
    story.append(Paragraph(
        ('Die Cochlea analysiert Frequenzen auf einer logarithmischen Skala: '
         'jede Oktave (Verdopplung der Frequenz) beansprucht '
         'ungef\u00e4hr gleich viel Platz auf der Basilarmembran. '
         'Das ist kein biologischer Zufall \u2014 es ist das optimale Design '
         'f\u00fcr die Statistik nat\u00fcrlicher Schallquellen.') if DE else
        ('The cochlea analyses frequencies on a logarithmic scale: '
         'each octave (doubling of frequency) occupies '
         'approximately equal space on the basilar membrane. '
         'This is not a biological accident \u2014 it is the optimal design '
         'for the statistics of natural sound sources.'),sBody))
    story.append(Paragraph(
        ('Nat\u00fcrliche Kl\u00e4nge \u2014 Sprache, Musik, Umgebungsger\u00e4usche '
         'aus Wind, Wasser, tierischen Lauten \u2014 '
         'haben statistisch gleich viel Energie pro Oktave (sogenanntes Rosa Rauschen). '
         'Die logarithmische Cochlea-Skala ist exakt f\u00fcr diese Statistik optimiert: '
         'jeder Frequenzkanal erh\u00e4lt gleich viel Signalenergie. '
         'Die Cochlea ist auf die Statistik der nat\u00fcrlichen Welt kalibriert, '
         'weil sie selbst aus dieser nat\u00fcrlichen Welt \u2014 '
         'aus atomarer Materie mit ihren physikalischen Konstanten \u2014 '
         'aufgebaut ist.') if DE else
        ('Natural sounds \u2014 speech, music, ambient sounds '
         'from wind, water, animal calls \u2014 '
         'statistically have equal energy per octave (so-called pink noise). '
         'The logarithmic cochlea scale is precisely optimised for this statistics: '
         'each frequency channel receives equal signal energy. '
         'The cochlea is calibrated to the statistics of the natural world '
         'because it is itself built from that natural world \u2014 '
         'from atomic matter with its physical constants.'),sBody))

    story.append(H2('2.3\u2002Hybride photonische Systeme: dasselbe Prinzip in der Technik' if DE else
                    '2.3\u2002Hybrid Photonic Systems: the Same Principle in Technology'))
    story.append(Paragraph(
        ('Die Erkenntnis, dass Physik rechnen kann, beginnt in der Technik '
         'Gestalt anzunehmen. Sogenannte Coherent Ising Machines (CIM) '
         'l\u00f6sen kombinatorische Optimierungsprobleme, '
         'indem optische Oszillatoren physikalisch in einen '
         'Energieminimumszustand relaxieren \u2014 '
         'das ist die L\u00f6sung des Problems. '
         'Ein digitaler Computer liest das Ergebnis danach nur noch aus.') if DE else
        ('The insight that physics can compute is beginning to take shape in technology. '
         'So-called Coherent Ising Machines (CIM) '
         'solve combinatorial optimisation problems '
         'by having optical oscillators physically relax '
         'into a minimum-energy state \u2014 '
         'that is the solution to the problem. '
         'A digital computer then merely reads out the result.'),sBody))

    story.append(mkt([
        [TH('Cochlea'),
         TH('Coherent Ising Machine'),
         TH('Gemeinsames Prinzip' if DE else 'Common principle')],
        [TD('Mechanische Resonanz der Basilarmembran' if DE else
            'Mechanical resonance of basilar membrane'),
         TD('Optische Resonatoren' if DE else 'Optical resonators'),
         TD('Physik relaxiert in L\u00f6sung' if DE else 'Physics relaxes into solution')],
        [TD('Aktive R\u00fcckkopplung durch Haarzellen' if DE else
            'Active feedback by hair cells'),
         TD('Phasensensitiver Verst\u00e4rker' if DE else 'Phase-sensitive amplifier'),
         TD('Aktive Energieeinleitung' if DE else 'Active energy injection')],
        [TD('Nervenimpuls: analog \u2192 Spike' if DE else
            'Neural spike: analogue \u2192 spike'),
         TD('Messung: analog \u2192 bin\u00e4r' if DE else
            'Measurement: analogue \u2192 binary'),
         TD('Digitale Nachverarbeitung' if DE else 'Digital post-processing')],
        [TD('Gehirn interpretiert Vorstrukturiertes' if DE else
            'Brain interprets pre-structured data'),
         TD('Computer liest relaxierten Zustand' if DE else
            'Computer reads relaxed state'),
         TD('Hybrid: Physik + Digital' if DE else 'Hybrid: physics + digital')],
    ],[5.0*cm,5.0*cm,4.2*cm]))
    story.append(Paragraph(
        'Strukturelle Parallelen zwischen Cochlea und Coherent Ising Machine.' if DE else
        'Structural parallels between cochlea and Coherent Ising Machine.',sCap))

    story.append(Spacer(1,0.3*cm))
    story.append(ibox(
        ('<b>Das gemeinsame Prinzip:</b> Ein physikalisches System mit geeigneter Struktur '
         'relaxiert in einen Zustand, der ein schwieriges Problem l\u00f6st. '
         'Die Verarbeitung <i>ist</i> die Physik \u2014 '
         'nicht eine Berechnung, die danach auf Messdaten l\u00e4uft.<br/><br/>'
         'Mathematik ist in die Geometrie der Materie kodiert. '
         'Physik realisiert diese Geometrie. '
         'Rechnen ist Propagation.') if DE else
        ('<b>The common principle:</b> A physical system with suitable structure '
         'relaxes into a state that solves a difficult problem. '
         'The processing <i>is</i> the physics \u2014 '
         'not a computation running afterwards on measurement data.<br/><br/>'
         'Mathematics is encoded in the geometry of matter. '
         'Physics realises this geometry. '
         'Computing is propagation.'),
        bg='#eef2ff',bc=MID,fs=10))

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════
    # Kapitel 3: Trainiertes Gehör als KI-Detektor
    # ══════════════════════════════════════════════════════════════════════
    story.append(H1(
        '3\u2002Das trainierte Geh\u00f6r als \u00fcberlegener KI-Detektor' if DE else
        '3\u2002The Trained Ear as Superior AI Detector'))

    story.append(ibox(
        ('<b>Kernaussage:</b> Wir w\u00e4ren gut bedient, '
         'unsere physikalischen F\u00e4higkeiten zu trainieren '
         'statt ausschlie\u00dflich auf technische L\u00f6sungen zu setzen. '
         'Ein trainiertes menschliches Geh\u00f6r wird KI-generierte Fakes '
         'f\u00fcr Jahrzehnte erkennen k\u00f6nnen \u2014 '
         'solange wir es trainieren.') if DE else
        ('<b>Core statement:</b> We would be well served to train our physical capabilities '
         'rather than relying exclusively on technical solutions. '
         'A trained human ear will be able to detect AI-generated fakes '
         'for decades to come \u2014 as long as we train it.'),
        bg='#fff8e1',bc=ORG,fs=11))

    story.append(H2('3.1\u2002Das strukturelle Problem automatischer Detektion' if DE else
                    '3.1\u2002The Structural Problem of Automated Detection'))
    story.append(Paragraph(
        ('KI-generierte Stimmen und Videos werden mit neuronalen Netzen erzeugt. '
         'Automatische Detektionssysteme nutzen dieselben Werkzeuge, '
         'um sie zu erkennen. Das erzeugt ein R\u00fcstungsrennen '
         'auf derselben technischen Ebene: '
         'Eine neue Generatorarchitektur macht den alten Detektor wertlos. '
         'Der Detektor wird nachger\u00fcstet. Der Generator wird verbessert.') if DE else
        ('AI-generated voices and videos are produced with neural networks. '
         'Automated detection systems use the same tools to identify them. '
         'This creates an arms race on the same technical level: '
         'a new generator architecture renders the old detector worthless. '
         'The detector is updated. The generator is improved.'),sBody))
    story.append(Paragraph(
        ('Dieses R\u00fcstungsrennen gewinnt strukturell der Angreifer: '
         'Er bestimmt die Richtung, der Verteidiger reagiert. '
         'Die Zeitverz\u00f6gerung zwischen neuem Fake und funktionierendem Detektor '
         'kann Monate betragen. In dieser Zeit ist der Schaden bereits angerichtet.') if DE else
        ('This arms race is structurally won by the attacker: '
         'they set the direction, the defender reacts. '
         'The time lag between new fake and working detector '
         'can be months. In this time the damage is already done.'),sBody))

    story.append(H2('3.2\u2002Was echte Stimmen von KI-Stimmen unterscheidet' if DE else
                    '3.2\u2022What Distinguishes Real Voices from AI Voices'))
    story.append(Paragraph(
        ('Eine echte Stimme entsteht durch Mechanik: '
         'Luftdruck aus der Lunge, Schwingung der Stimmlippen, '
         'Resonanz von Rachen und Mund, Abstrahlung durch Lippen und Nase. '
         'Jeder dieser Vorg\u00e4nge ist physikalisch, nichtlinear, '
         'von K\u00f6rper und Moment abh\u00e4ngig.') if DE else
        ('A real voice arises from mechanics: '
         'air pressure from the lungs, vibration of the vocal folds, '
         'resonance of throat and mouth, radiation through lips and nose. '
         'Each of these processes is physical, non-linear, '
         'dependent on body and moment.'),sBody))
    story.append(Paragraph(
        'Diese Mechanik hinterl\u00e4sst Spuren, die in der digitalen Dom\u00e4ne nicht vollst\u00e4ndig reproduzierbar sind:' if DE else
        'This mechanics leaves traces that are not fully reproducible in the digital domain:',sBody))

    for t in ([
        'Mikrovariationen in Tonh\u00f6he und Lautst\u00e4rke (Jitter und Shimmer): '
        'chaotisch, durch Atemstrom und Muskelspannung erzeugt, '
        'jedes Mal einzigartig',
        'Raumakustik: Reflexionen, Nachhall und Absorptionsmuster des physischen Raums, '
        'in dem gesprochen wurde',
        '\u00dcbergangslaute zwischen W\u00f6rtern und Silben (Koartikulation): '
        'entstehen durch Tr\u00e4gheit und Elastizit\u00e4t von Zunge, Lippen und Gaumen',
        'Atemger\u00e4usch und Luftstr\u00f6mungstextur: turbulente Str\u00f6mung, '
        'jedes Mal anders',
        'Feine Klangfarbenver\u00e4nderungen durch Tagesform, '
        'Emotionen, K\u00f6rperhaltung',
    ] if DE else [
        'Micro-variations in pitch and loudness (jitter and shimmer): '
        'chaotic, produced by airflow and muscle tension, unique every time',
        'Room acoustics: reflections, reverberation, and absorption patterns '
        'of the physical space where speech was produced',
        'Transition sounds between words and syllables (coarticulation): '
        'arise from inertia and elasticity of tongue, lips, and palate',
        'Breath noise and airflow texture: turbulent flow, different every time',
        'Fine timbral changes due to daily condition, emotions, body posture',
    ]):
        story.append(bullet(t))

    story.append(Spacer(1,0.3*cm))
    story.append(Paragraph(
        ('KI-Generatoren lernen die statistischen Durchschnittswerte dieser Merkmale. '
         'Sie erzeugen wahrscheinliche Signale \u2014 aber keine physikalisch generierten. '
         'Die fehlende Mechanik hinterl\u00e4sst systematische Spuren: '
         'zu gleichm\u00e4\u00dfige Mikrovariation, '
         'fehlende Raumakustik-Konsistenz, '
         '\u00fcbergl\u00e4ttete Klangverl\u00e4ufe.') if DE else
        ('AI generators learn the statistical averages of these features. '
         'They produce probable signals \u2014 but not physically generated ones. '
         'The missing mechanics leaves systematic traces: '
         'overly regular micro-variation, '
         'missing room-acoustic consistency, '
         'over-smoothed tonal contours.'),sBody))

    story.append(H2('3.3\u2002Warum der Vorteil auf Jahrzehnte stabil bleibt' if DE else
                    '3.3\u2002Why the Advantage Remains Stable for Decades'))
    story.append(Paragraph(
        ('KI-Generatoren werden besser \u2014 in der digitalen Dom\u00e4ne. '
         'Sie lernen aus mehr Daten, mit gr\u00f6\u00dferen Modellen. '
         'Aber sie werden nicht besser darin, '
         'echte Mechanik zu simulieren \u2014 '
         'weil echte Mechanik nicht digital ist. '
         'Stimmlippen-Turbulenz, Raumimpulsantwort, Atemdruck-Verlauf: '
         'diese entstehen in der physikalischen Welt '
         'und sind im digitalen Signalraum nur n\u00e4herungsweise darstellbar.') if DE else
        ('AI generators will improve \u2014 in the digital domain. '
         'They learn from more data, with larger models. '
         'But they will not improve at simulating real mechanics \u2014 '
         'because real mechanics is not digital. '
         'Vocal fold turbulence, room impulse response, breath-pressure profile: '
         'these arise in the physical world '
         'and can only be approximately represented in the digital signal space.'),sBody))
    story.append(Paragraph(
        ('Das trainierte Geh\u00f6r erkennt die fehlende Physik. '
         'Nicht weil es besser rechnet als ein digitales System \u2014 '
         'sondern weil es selbst physikalisch ist. '
         'Es ist ein physikalisches System, das physikalische Signaturen erkennt. '
         'Kein digitaler Generator kann diese Ebene angreifen, '
         'weil er auf einer anderen Ebene operiert.') if DE else
        ('The trained ear detects the missing physics. '
         'Not because it computes better than a digital system \u2014 '
         'but because it is itself physical. '
         'It is a physical system detecting physical signatures. '
         'No digital generator can attack this level '
         'because it operates on a different level.'),sBody))

    story.append(mkt([
        [TH('Ansatz' if DE else 'Approach'),
         TH('Schicht' if DE else 'Layer'),
         TH('R\u00fcstungsrennen?' if DE else 'Arms race?'),
         TH('Stabilit\u00e4t' if DE else 'Stability')],
        [TD('Automatischer KI-Detektor' if DE else 'Automated AI detector'),
         TD('Digital'),
         TD('Ja \u2014 Angreifer gewinnt' if DE else 'Yes \u2014 attacker wins'),
         TD('Monate bis Jahre' if DE else 'Months to years')],
        [TD('Trainiertes Geh\u00f6r' if DE else 'Trained ear'),
         TD('Physikalisch' if DE else 'Physical'),
         TD('Nein \u2014 andere Ebene' if DE else 'No \u2014 different level'),
         TD('Jahrzehnte' if DE else 'Decades')],
        [TD('Kombination beider' if DE else 'Combination of both'),
         TD('Beide' if DE else 'Both'),
         TD('Teils' if DE else 'Partly'),
         TD('Optimal' if DE else 'Optimal')],
    ],[4.5*cm,3.0*cm,4.0*cm,3.2*cm]))

    story.append(H2('3.4\u2002Training: konkret und m\u00f6glich' if DE else
                    '3.4\u2002Training: Concrete and Achievable'))
    story.append(Paragraph(
        ('Das trainierte Geh\u00f6r ist kein mystisches Talent. '
         'Radiojournalisten, Tonmeister und Musiker entwickeln es im Berufsalltag. '
         'Es folgt aus gezielter \u00dcbung:') if DE else
        ('The trained ear is not a mystical talent. '
         'Radio journalists, sound engineers, and musicians develop it in daily work. '
         'It follows from deliberate practice:'),sBody))
    for t in ([
        'Aktives, bewusstes H\u00f6ren: Analyse statt blo\u00dfes Konsumieren',
        'Direkter Vergleich: echte und synthetische Stimmen nebeneinander',
        'Raumakustik-Sensibilisierung: nat\u00fcrliche vs. k\u00fcnstliche Hallr\u00e4ume',
        'Arbeit mit unbearbeitetem Rohmaterial',
        'Analyse von Atemmustern, Sprechrhythmus, mikrovokaler Textur',
        'Geh\u00f6rbildung wie in der Musikausbildung \u2014 nur auf Echtheit statt Tonh\u00f6he fokussiert',
    ] if DE else [
        'Active, deliberate listening: analysis instead of mere consumption',
        'Direct comparison: real and synthetic voices side by side',
        'Room-acoustic sensitisation: natural vs. artificial reverberation',
        'Working with unprocessed raw material',
        'Analysis of breathing patterns, speech rhythm, micro-vocal texture',
        'Ear training as in music education \u2014 but focused on authenticity rather than pitch',
    ]):
        story.append(bullet(t))

    # Schluss
    story.append(Spacer(1,0.5*cm))
    story.append(HRFlowable(width=PW,thickness=1.5,color=DARK,spaceAfter=12))
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
         'The question is why we have stopped trusting our own ears.'),
        bg='#eef2ff',bc=MID,fs=11))

    story.append(Spacer(1,0.5*cm))
    story.append(Paragraph(
        ('<i>Das menschliche Geh\u00f6r ist ein physikalischer Prozessor, '
         'der auf der atomaren Skala der Materie operiert. '
         'Es arbeitet jenseits der Grenzen passiver digitaler Systeme, '
         'jenseits der Frame-Grenzen der Abtastung, '
         'jenseits der Reichweite digitaler F\u00e4lschungen. '
         'Trainieren wir es.</i>') if DE else
        ('<i>The human ear is a physical processor '
         'operating at the atomic scale of matter. '
         'It works beyond the limits of passive digital systems, '
         'beyond the frame limits of sampling, '
         'beyond the reach of digital forgeries. '
         'Let us train it.</i>'),
        S('fin','DV-I',11,17,8,0,TA_CENTER,MID)))

    story.append(Spacer(1,1.0*cm))

    doc=T0Doc(out,
        title='Dok.170b: Das Geh\u00f6r als physikalischer Vorverarbeiter' if DE else
              'Doc.170b: The Ear as a Physical Pre-processor',
        author='Johann Pascher')
    doc.multiBuild(story)
    print(f'{"DE" if DE else "EN"} \u2192 {out}')

build('de')
build('en')
