from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math

# Inter-Font registrieren (hat griechische Zeichen)
pdfmetrics.registerFont(TTFont('Inter-Bold', '/usr/local/share/fonts/ffgft/Inter-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Inter', '/usr/local/share/fonts/ffgft/Inter-Regular.ttf'))

W, H = landscape(A4)
OUT = "/home/claude/SM_Teilchen_GF27_En.pdf"
c = canvas.Canvas(OUT, pagesize=landscape(A4))

BLUE_DARK  = (0.10, 0.29, 0.48)
BLUE_MID   = (0.36, 0.64, 0.86)
GREEN_DARK = (0.00, 0.50, 0.55)
GREEN_MID  = (0.60, 0.25, 0.55)
PURPLE     = (0.33, 0.29, 0.72)
ORANGE     = (0.87, 0.48, 0.00)
GRAY       = (0.60, 0.60, 0.60)
RED_COL    = (0.85, 0.15, 0.15)
GREEN_COL  = (0.10, 0.60, 0.15)
BLUE_COL   = (0.10, 0.35, 0.80)
RED_BOX    = (0.75, 0.10, 0.10)

def rgb(t): c.setFillColorRGB(*t)
def srgb(t): c.setStrokeColorRGB(*t)

def arc_fill(cx, cy, r_out, r_in, a1_deg, a2_deg, col):
    """Ringsektor von r_in bis r_out, von a1 bis a2 Grad."""
    p = c.beginPath()
    steps = 30
    # Außenkante vorwärts
    for i in range(steps+1):
        a = math.radians(a1_deg + (a2_deg-a1_deg)*i/steps)
        x, y = cx + r_out*math.cos(a), cy + r_out*math.sin(a)
        if i == 0: p.moveTo(x, y)
        else: p.lineTo(x, y)
    # Innenkante rückwärts
    for i in range(steps+1):
        a = math.radians(a2_deg - (a2_deg-a1_deg)*i/steps)
        p.lineTo(cx + r_in*math.cos(a), cy + r_in*math.sin(a))
    p.close()
    rgb(col); c.drawPath(p, stroke=0, fill=1)

def fermion(cx, cy, sym, q, yv, yr, orbit_col, gen3=False,
            nu_right=False, color_ring=False):
    # Radien von innen nach außen (physikalisch korrekt):
    # Innenkreis: weiß
    # Farbring:   direkt nach weiß (Confinement — Quarks only)
    # Mittelring: Chiralität
    # Außenring:  Galois-Orbit
    # Gen.3:      gestrichelt ganz außen
    Ri = 18   # Innenkreis größer
    Rcf = 24  # Farbring außen
    Rm = 32   # Mittelring außen
    Ro = 42   # Außenring schmaler (war 44)

    # 1. Außenring als Basis (Orbit-Farbe)
    rgb(orbit_col); c.circle(cx, cy, Ro, stroke=0, fill=1)

    # 2. Mittelring (Chiralität) — übermalt inneren Teil
    rh = GRAY if nu_right else ORANGE
    arc_fill(cx, cy, Rm, Ri, 90,  270, PURPLE)
    arc_fill(cx, cy, Rm, Ri, 270, 450, rh)

    # 3. Farbring — direkt nach innen, nur Quarks
    if color_ring:
        arc_fill(cx, cy, Rcf, Ri, 90,  210, RED_COL)
        arc_fill(cx, cy, Rcf, Ri, 210, 330, GREEN_COL)
        arc_fill(cx, cy, Rcf, Ri, 330, 450, BLUE_COL)

    # 4. Weißer Innenkreis
    c.setFillColorRGB(1,1,1); c.circle(cx, cy, Ri, stroke=0, fill=1)

    # 5. Dunkler Rand des Außenrings
    dr = tuple(max(0, x-0.3) for x in orbit_col)
    srgb(dr); c.setLineWidth(1.5); c.circle(cx, cy, Ro, stroke=1, fill=0)

    # 6. Text im Innenkreis: Symbol + Q
    c.setFillColorRGB(0.05,0.05,0.05)
    c.setFont("Inter-Bold", 14); c.drawCentredString(cx, cy+5, sym)
    c.setFont("Helvetica", 8)
    c.drawCentredString(cx, cy-6,  f"Q={q}")
    # YL/YR links neben dem Kreis
    lx = cx - Ro - 52
    c.drawString(lx, cy+3,  f"YL={yv}")
    c.drawString(lx, cy-8,  f"YR={yr}")

    # 7. Gen3 — gestrichelt ganz außen
    if gen3:
        srgb((1,1,1)); c.setLineWidth(4.0)
        c.circle(cx, cy, Ro+1, stroke=1, fill=0)
        srgb((0,0,0)); c.setLineWidth(2.0); c.setDash(7,4)
        c.circle(cx, cy, Ro+1, stroke=1, fill=0)
        c.setDash()

def dublett_box(x1, y1, x2, y2):
    srgb(RED_BOX); c.setLineWidth(1.5); c.setDash(6,3)
    c.rect(x1, y1, x2-x1, y2-y1, stroke=1, fill=0)
    c.setDash()

# Layout
LBL_W = 72; RHS_W = 206
FW = W - LBL_W - RHS_W; COL_W = FW/3
R = 44; PAD = 8
ROW1 = H-118; ROW2 = H-248; ROW3 = H-398; ROW4 = H-508

# Titel
c.setFont("Helvetica-Bold", 11); c.setFillColorRGB(0,0,0)
c.drawCentredString(LBL_W+FW/2, H-12,
    "Standard Model Particles from GF(27)* — all quantum numbers algebraically forced [B]")
c.setFont("Helvetica", 9)
c.drawCentredString(LBL_W+FW/2, H-24,
    "FFGFT · J. Pascher 2026 · Doc. 346/347/348/349")

for i,lbl in enumerate(["Generation 1","Generation 2","Generation 3"]):
    c.setFont("Helvetica-Bold", 10); c.setFillColorRGB(0.15,0.15,0.15)
    c.drawCentredString(LBL_W+(i+0.5)*COL_W, H-40, lbl)

def rlabel(y, lines):
    c.setFont("Helvetica", 9); c.setFillColorRGB(0.25,0.25,0.25)
    for i,l in enumerate(lines): c.drawString(4, y-i*11, l)

rlabel(ROW1+8,  ["Neutrinos","(QR)"])
rlabel(ROW2+8,  ["Charged","leptons","(QR)"])
rlabel(ROW3+8,  ["Up quarks","(NQR)"])
rlabel(ROW4+8,  ["Down","quarks","(NQR)"])

# Dublett-Kästen (rot gestrichelt) — vor den Teilchen
for col in range(3):
    cx = LBL_W+(col+0.5)*COL_W
    dublett_box(cx-R-PAD, ROW2-R-PAD, cx+R+PAD, ROW1+R+PAD)
    dublett_box(cx-R-PAD, ROW4-R-PAD, cx+R+PAD, ROW3+R+PAD)

c.setFont("Helvetica", 8); c.setFillColorRGB(0.65,0.10,0.10)
c.drawCentredString(LBL_W+FW/2, ROW1+R+PAD+6, "SU(2)L-doublet = Sd-sector [B] Doc.349")
c.drawCentredString(LBL_W+FW/2, ROW3+R+PAD+6, "SU(2)L-doublet = Sd-sector [B] Doc.349")

# Teilchen
# (col, row, sym, Q, YL, YR, orbit_col, gen3, nu_right, color_ring)
parts = [
    (0,ROW1,"ν",  "0",   "-1",  "—",    BLUE_DARK, False,True, False),
    (1,ROW1,"νμ", "0",   "-1",  "—",    BLUE_MID,  False,True, False),
    (2,ROW1,"ντ", "0",   "-1",  "—",    BLUE_DARK, True, True, False),
    (0,ROW2,"e",  "-1",  "-1",  "-2",   BLUE_DARK, False,False,False),
    (1,ROW2,"μ",  "-1",  "-1",  "-2",   BLUE_MID,  False,False,False),
    (2,ROW2,"τ",  "-1",  "-1",  "-2",   BLUE_DARK, True, False,False),
    (0,ROW3,"u",  "+2/3","+1/3","+4/3", GREEN_DARK,False,False,True),
    (1,ROW3,"c",  "+2/3","+1/3","+4/3", GREEN_MID, False,False,True),
    (2,ROW3,"t",  "+2/3","+1/3","+4/3", GREEN_DARK,True, False,True),
    (0,ROW4,"d",  "-1/3","+1/3","-2/3", GREEN_DARK,False,False,True),
    (1,ROW4,"s",  "-1/3","+1/3","-2/3", GREEN_MID, False,False,True),
    (2,ROW4,"b",  "-1/3","+1/3","-2/3", GREEN_DARK,True, False,True),
]
for (col,ry,sym,q,yl,yr,col_,g3,nur,cr) in parts:
    fermion(LBL_W+(col+0.5)*COL_W, ry, sym, q, yl, yr, col_, g3, nur, cr)

# Rechtes Panel
RX = LBL_W+FW+6; LW2 = RHS_W-10

# Eichbosonen
c.setFont("Helvetica-Bold",10); c.setFillColorRGB(0,0,0)
c.drawString(RX, H-36, "Gauge bosons")
# g — groß, allein (starke Wechselwirkung)
GSQ=44; BY1=H-88
def bsq(bx,by,bw,bh,fc,lbl,sub="",fs=13):
    rgb(fc); c.rect(bx,by,bw,bh,stroke=0,fill=1)
    srgb((0.55,0.55,0.55)); c.setLineWidth(0.6); c.rect(bx,by,bw,bh,stroke=1,fill=0)
    c.setFillColorRGB(0,0,0); c.setFont("Helvetica-Bold",fs)
    c.drawCentredString(bx+bw/2,by+bh/2+1,lbl)
    if sub: c.setFont("Helvetica",7); c.drawCentredString(bx+bw/2,by+5,sub)

bsq(RX, BY1, GSQ, GSQ, (0.78,0.78,0.78), "g", "Q=0", fs=16)
c.setFont("Helvetica",7); c.setFillColorRGB(0.2,0.2,0.2)
c.drawString(RX, BY1-10, "GF(3) fixed field [B] Doc.339")
# W+ W- Z0 — kleiner, als Gruppe darunter (EW)
SQ=28; GAP=3; BY2=H-133
bsq(RX,           BY2, SQ, SQ, (0.95,0.62,0.65), "W+", fs=11)
bsq(RX+SQ+GAP,   BY2, SQ, SQ, (0.95,0.62,0.65), "W-", fs=11)
bsq(RX+2*(SQ+GAP),BY2, SQ, SQ, (0.95,0.75,0.80), "Z0", fs=11)
c.setFont("Helvetica",7); c.setFillColorRGB(0.2,0.2,0.2)
c.drawString(RX, BY2-10, "Gal(GF(9)/GF(3))=Z2 [K] Doc.336")

# Gluonen 2×4
c.setFont("Helvetica-Bold",9); c.setFillColorRGB(0,0,0)
c.drawString(RX,H-168,"Gluons gx8")
gsq=24; ggap=3
for gi in range(8):
    gx=RX+(gi%4)*(gsq+ggap); gy=H-200-(gi//4)*(gsq+ggap)
    # 2 Gruppen à 4 in unterschiedlichem Grau (Z₂-Paritäten)
    if gi < 4:
        c.setFillColorRGB(0.60,0.60,0.60)  # dunkleres Grau
    else:
        c.setFillColorRGB(0.82,0.82,0.82)  # helleres Grau
    c.rect(gx,gy,gsq,gsq,stroke=0,fill=1)
    srgb((0.45,0.45,0.45)); c.setLineWidth(0.4); c.rect(gx,gy,gsq,gsq,stroke=1,fill=0)
c.setFont("Helvetica",7); c.setFillColorRGB(0.2,0.2,0.2)
c.drawString(RX,H-238,"4 Z13-Orbits x 2 Z2-par. = 8 [B]")

# Higgs
c.setFont("Helvetica-Bold",9); c.setFillColorRGB(0,0,0)
c.drawString(RX,H-248,"Higgs")
HX=RX; HY=H-282; HW=52; HH=32
c.setFillColorRGB(0.95,0.93,0.80); c.rect(HX,HY,HW,HH,stroke=0,fill=1)
# Schraffur: diagonale Linien von links-unten nach rechts-oben
srgb((0.70,0.65,0.30)); c.setLineWidth(0.5)
for xi in range(-HH, HW+HH, 7):
    x1 = HX + xi;       y1 = HY
    x2 = HX + xi + HH;  y2 = HY + HH
    # Clip auf Rechteck
    if x1 < HX:
        y1 += (HX - x1); x1 = HX
    if x2 > HX+HW:
        y2 -= (x2 - (HX+HW)); x2 = HX+HW
    if x1 < x2:
        c.line(x1, y1, x2, y2)
srgb((0.55,0.50,0.15)); c.setLineWidth(1.0)
c.rect(HX,HY,HW,HH,stroke=1,fill=0)
c.setFillColorRGB(0,0,0); c.setFont("Helvetica-Bold",12)
c.drawCentredString(HX+HW/2,HY+HH/2+1,"H0")
c.setFont("Helvetica",7); c.setFillColorRGB(0.2,0.2,0.2)
c.drawString(RX,HY-9,"Q=0")
c.drawString(RX,HY-19,"T~.m=1 replaces Higgs (Doc.019)  Exp. established [X]")

# Legende
entries = [
    ("hdr",None,      "Outer ring = Galois orbit:"),
    ("dot",BLUE_DARK, "O1/O3: Gen.1/3 leptons (blue)"),
    ("dot",BLUE_MID,  "O3: Gen.2 leptons (light blue)"),
    ("dot",GREEN_DARK,"O2: Gen.1/3 quarks (teal)"),
    ("dot",GREEN_MID, "O4: Gen.2 quarks (berry)"),
    ("hdr",None,      "Middle ring = chirality:"),
    ("dot",PURPLE,    "Left violet = Sd = left-h. [B]"),
    ("dot",ORANGE,    "Right orange = Su = right-h. [B]"),
    ("dot",GRAY,      "Gray = vR absent; Dirac [B/S]"),
    ("hdr",None,      "Colour ring (quarks only):"),
    ("rgb",None,      "r/g/b = colour charge [B] Doc.346"),
    ("rdash",None,    "Red dashed = SU(2)L doublet"),
    ("gdash",None,    "Black dashed = Gen.3"),
    ("txt",None,      "[B] algebraically proved"),
    ("txt",None,      "[K] numerically  [X] experimentally"),
]
lh=18; leg_h=20+len(entries)*lh+6; LEG_TOP=H-310
c.setFillColorRGB(0.96,0.96,0.94); srgb((0.72,0.72,0.72)); c.setLineWidth(0.5)
c.rect(RX,LEG_TOP-leg_h,LW2,leg_h,stroke=1,fill=1)
c.setFont("Helvetica-Bold",12); c.setFillColorRGB(0,0,0)
c.drawString(RX+4,LEG_TOP-13,"Legend")
c.setFont("Helvetica",8.5)
for i,(typ,col,txt) in enumerate(entries):
    ey=LEG_TOP-26-i*lh
    if typ=="hdr":
        c.setFont("Helvetica-Bold",7.5); c.setFillColorRGB(0.35,0.35,0.35)
        c.drawString(RX+4,ey-3,txt); c.setFont("Helvetica",8.5)
    elif typ=="dot":
        rgb(col); c.circle(RX+7,ey,5,stroke=0,fill=1)
        c.setFillColorRGB(0.05,0.05,0.05); c.drawString(RX+16,ey-4,txt)
    elif typ=="rgb":
        from math import radians, cos, sin
        def sp(a1,a2,col2):
            p=c.beginPath(); p.moveTo(RX+7,ey)
            for j in range(13):
                a=radians(a1+(a2-a1)*j/12)
                p.lineTo(RX+7+7*cos(a),ey+7*sin(a))
            p.close(); rgb(col2); c.drawPath(p,stroke=0,fill=1)
        sp(90,210,RED_COL); sp(210,330,GREEN_COL); sp(330,450,BLUE_COL)
        c.setFillColorRGB(0.96,0.96,0.94); c.circle(RX+7,ey,3.5,stroke=0,fill=1)
        c.setFillColorRGB(0.05,0.05,0.05); c.drawString(RX+16,ey-4,txt)
    elif typ=="rdash":
        srgb(RED_BOX); c.setLineWidth(1.0); c.setDash(4,2)
        c.rect(RX+2,ey-5,11,11,stroke=1,fill=0); c.setDash()
        c.setFillColorRGB(0.05,0.05,0.05); c.drawString(RX+16,ey-4,txt)
    elif typ=="gdash":
        srgb((0,0,0)); c.setLineWidth(1.2); c.setDash(5,3)
        c.circle(RX+7,ey,5,stroke=1,fill=0); c.setDash()
        c.setFillColorRGB(0.05,0.05,0.05); c.drawString(RX+16,ey-4,txt)
    elif typ=="txt":
        c.setFillColorRGB(0.22,0.22,0.22); c.drawString(RX+4,ey-4,txt)

c.setFont("Helvetica",6.5); c.setFillColorRGB(0.4,0.4,0.4)
c.drawCentredString(W/2,10,
    "All SM fermion quantum numbers follow from GF(27)* without free parameters · FFGFT J. Pascher 2026")
c.save(); print(f"OK: {OUT}")
