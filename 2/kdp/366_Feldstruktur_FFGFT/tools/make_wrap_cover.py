# Erzeugt die Paperback-Umschlaege (Rueckseite+Ruecken+Vorderseite), 6x9 in, Beschnitt 0.125 in, weisses Papier.
# Benoetigt front_de.jpg/front_en.jpg (= cover/366_Cover_Kindle_*.jpg) sowie back_*.jpg (gespiegelt, Gauss 28, Helligkeit 0.45) im Arbeitsordner.
import asyncio, math
from playwright.async_api import async_playwright
BLEED=0.125; TW=6.0; TH=9.0
def spine(pages): return (pages + pages%2)*0.002252
TXT={
'en':dict(pages=38, kicker='FFGFT Corpus · Document 366',
 head='Where does electrical energy actually flow?',
 paras=['Not in the wire, but in the field around it. Starting from the Goubau line — energy transport along a single wire without a return conductor — this book takes the Poynting vector <b>S = E × H</b> seriously as the primary description and follows one principle across all scales: <i>the geometry of the carrier determines which couplings are allowed.</i>',
 'Antenna engineering, atomic selection rules, Bragg conditions in crystals and the orbital resonances of the planets turn out to be the same structure on different carriers: coupling happens only where mode structures are compatible — regardless of field strength.',
 'Within the Fundamental Fractal Geometric Field Theory (FFGFT) this is not an analogy but a consequence of the time–mass duality <b>T̃·m = 1</b> on the compact carrier <b>T⁴/ℤ₃</b>. In natural units, current is mass, voltage is energy and power is E·m — exactly, not approximately.',
 'Every statement carries an epistemic marker — proven, numerically confirmed, structurally plausible, posited — and the book states clearly what it does not explain.'],
 author='Johann Pascher', meta='ORCID 0009-0000-6518-4064<br>github.com/jpascher/T0-Time-Mass-Duality'),
'de':dict(pages=37, kicker='FFGFT-Korpus · Dokument 366',
 head='Wo fließt elektrische Energie wirklich?',
 paras=['Nicht im Draht, sondern im Feld um ihn herum. Ausgehend von der Goubau-Leitung — Energietransport entlang eines einzelnen Drahtes ohne Rückleiter — nimmt dieses Buch den Poynting-Vektor <b>S = E × H</b> als primäre Beschreibung ernst und verfolgt ein Prinzip über alle Skalen: <i>Die Geometrie des Trägers bestimmt, welche Kopplungen erlaubt sind.</i>',
 'Antennentechnik, atomare Auswahlregeln, Bragg-Bedingungen im Kristall und die Bahnresonanzen der Planeten erweisen sich als dieselbe Struktur auf verschiedenen Trägern: Kopplung gibt es nur dort, wo Modenstrukturen kompatibel sind — unabhängig von der Feldstärke.',
 'In der Fundamentalen Fraktalen Geometrischen Feldtheorie (FFGFT) ist das keine Analogie, sondern eine Folge der Zeit-Masse-Dualität <b>T̃·m = 1</b> auf dem kompakten Träger <b>T⁴/ℤ₃</b>. In natürlichen Einheiten ist Strom Masse, Spannung Energie und Leistung E·m — exakt, nicht näherungsweise.',
 'Jede Aussage trägt einen epistemischen Marker — bewiesen, numerisch bestätigt, strukturell plausibel, gesetzt — und das Buch sagt klar, was es nicht erklärt.'],
 author='Johann Pascher', meta='ORCID 0009-0000-6518-4064<br>github.com/jpascher/T0-Time-Mass-Duality'),
}
def html(tag):
    t=TXT[tag]; s=spine(t['pages'])
    W=2*BLEED+2*TW+s; H=TH+2*BLEED
    backW=BLEED+TW; frontX=backW+s; frontW=TW+BLEED
    paras=''.join(f'<p>{p}</p>' for p in t['paras'])
    return W,H,s,f'''<html><head><style>
@page{{size:{W}in {H}in;margin:0}} html,body{{margin:0;padding:0}}
body{{width:{W}in;height:{H}in;position:relative;overflow:hidden;background:#141b2b;font-family:Carlito,'DejaVu Sans',sans-serif}}
.back{{position:absolute;left:0;top:0;width:{backW}in;height:{H}in;background:url(back_{tag}.jpg) center/cover}}
.back::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,19,32,.55),rgba(14,19,32,.78))}}
.spine{{position:absolute;left:{backW}in;top:0;width:{s}in;height:{H}in;background:#131a28}}
.front{{position:absolute;left:{frontX}in;top:0;width:{frontW}in;height:{H}in;background:url(front_{tag}.jpg) center/cover}}
.txt{{position:absolute;z-index:2;left:{BLEED+0.55}in;top:{BLEED+0.6}in;width:{TW-1.1}in;color:#e6e9f0}}
.kick{{font-size:10pt;letter-spacing:.14em;text-transform:uppercase;color:#6fa8dc;margin-bottom:.18in}}
h1{{font-family:Carlito,sans-serif;font-weight:700;font-size:21pt;line-height:1.15;color:#d8b46a;margin:0 0 .22in}}
p{{font-size:11pt;line-height:1.42;margin:0 0 .13in;text-align:left;hyphens:auto}}
p b{{color:#f0d596}} p i{{color:#cfe0f5}}
.rule{{width:1.2in;height:1.5px;background:#d8b46a;margin:.22in 0 .16in}}
.auth{{font-size:14pt;font-weight:700;color:#fff}} .meta{{font-size:9pt;color:#9fb0c8;line-height:1.4;margin-top:.05in}}
</style></head><body>
<div class="back"></div><div class="spine"></div><div class="front"></div>
<div class="txt"><div class="kick">{t['kicker']}</div><h1>{t['head']}</h1>{paras}
<div class="rule"></div><div class="auth">{t['author']}</div><div class="meta">{t['meta']}</div></div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for tag in ['en','de']:
            W,H,s,h=html(tag)
            open(f'wrap_{tag}.html','w').write(h)
            pg=await b.new_page(viewport={'width':int(W*96),'height':int(H*96)})
            import os
            await pg.goto('file://'+os.path.abspath(f'wrap_{tag}.html')); await pg.wait_for_timeout(500)
            await pg.pdf(path=f'366_Paperback_Cover_{tag.capitalize()}.pdf',width=f'{W}in',height=f'{H}in',print_background=True,prefer_css_page_size=True)
            await pg.screenshot(path=f'prev_{tag}.png')
            # guard: text height
            bottom=await pg.evaluate("document.querySelector('.txt').getBoundingClientRect().bottom/96")
            print(tag,'W',round(W,4),'H',H,'spine',round(s,4),'text bottom in',round(bottom,2))
        await b.close()
asyncio.run(main())
