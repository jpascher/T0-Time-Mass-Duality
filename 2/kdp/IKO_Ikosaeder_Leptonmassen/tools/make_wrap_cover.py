import asyncio, os
from playwright.async_api import async_playwright
BLEED=0.125; TW=6.0; TH=9.0
def spine(p): return (p+p%2)*0.002252
TXT={
'en':dict(pages=73, kicker='Fundamental Fractal Geometric Field Theory',
 head='One number. Every lepton mass.',
 paras=['In 1981 Yoshio Koide noticed a relation between the masses of the electron, the muon and the tau that is accurate to six digits — and nobody could say why. This book gives the reason: the relation is the shadow of a geometric object, the icosahedron.',
 'The path there is told from the ground up. A four-dimensional torus instead of an equation as the starting point. A single dimensionless parameter, ξ = 4/30 000, from which the masses follow as powers, not as fitted values. Then the step from the closed torus to the space and time we observe — and finally the icosahedron, whose angle 2/9 closes a forty-year-old open question.',
 'Written for readers who want the argument rather than the formalism: the derivations and verification scripts stay in the FFGFT corpus, the reasoning stays in the text. Every claim is marked for what it is — proven, numerically confirmed, or posited.'],
 author='Johann Pascher', meta='ORCID 0009-0000-6518-4064<br>github.com/jpascher/T0-Time-Mass-Duality'),
'de':dict(pages=75, kicker='Fundamentale Fraktale Geometrische Feldtheorie',
 head='Eine Zahl. Alle Leptonmassen.',
 paras=['1981 bemerkte Yoshio Koide eine Beziehung zwischen den Massen von Elektron, Myon und Tau, die auf sechs Stellen genau stimmt — und niemand konnte sagen, warum. Dieses Buch nennt den Grund: Die Beziehung ist der Schatten eines geometrischen Körpers, des Ikosaeders.',
 'Der Weg dorthin wird von Grund auf erzählt. Ein vierdimensionaler Torus statt einer Gleichung als Ausgangspunkt. Ein einziger dimensionsloser Parameter, ξ = 4/30 000, aus dem die Massen als Potenzen folgen, nicht als angepasste Werte. Dann der Schritt vom geschlossenen Torus zu Raum und Zeit, die wir beobachten — und schließlich das Ikosaeder, dessen Winkel 2/9 eine vierzig Jahre offene Frage schließt.',
 'Geschrieben für Leser, die das Argument wollen und nicht den Formalismus: Die Ableitungen und Prüfskripte bleiben im FFGFT-Korpus, die Begründung bleibt im Text. Jede Aussage ist als das gekennzeichnet, was sie ist — bewiesen, numerisch bestätigt oder gesetzt.'],
 author='Johann Pascher', meta='ORCID 0009-0000-6518-4064<br>github.com/jpascher/T0-Time-Mass-Duality'),
}
def html(tag):
    t=TXT[tag]; s=spine(t['pages']); W=2*BLEED+2*TW+s; H=TH+2*BLEED
    backW=BLEED+TW; frontX=backW+s; frontW=TW+BLEED
    paras=''.join(f'<p>{p}</p>' for p in t['paras'])
    return W,H,s,f'''<html><head><meta charset="utf-8"><style>
@page{{size:{W}in {H}in;margin:0}} html,body{{margin:0;padding:0}}
body{{width:{W}in;height:{H}in;position:relative;overflow:hidden;background:#0e1017;font-family:Caladea,'DejaVu Serif',serif}}
.back{{position:absolute;left:0;top:0;width:{backW}in;height:{H}in;background:url(back_{tag}.jpg) center/cover}}
.back::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,20,.62),rgba(10,12,20,.82))}}
.spine{{position:absolute;left:{backW}in;top:0;width:{s}in;height:{H}in;background:#10131c}}
.front{{position:absolute;left:{frontX}in;top:0;width:{frontW}in;height:{H}in;background:url(front_{tag}.jpg) center/cover}}
.txt{{position:absolute;z-index:2;left:{BLEED+0.6}in;top:{BLEED+0.75}in;width:{TW-1.2}in;color:#e8e7e2}}
.kick{{font-family:Carlito,sans-serif;font-size:9.5pt;letter-spacing:.13em;text-transform:uppercase;color:#9aa8c4;margin-bottom:.2in}}
h1{{font-size:22pt;line-height:1.16;color:#d9bd84;margin:0 0 .26in;font-weight:700}}
p{{font-size:11pt;line-height:1.46;margin:0 0 .15in;hyphens:auto}}
.rule{{width:1.3in;height:1.5px;background:#d9bd84;margin:.26in 0 .18in}}
.auth{{font-size:14.5pt;color:#fff}} .meta{{font-family:Carlito,sans-serif;font-size:9pt;color:#93a0b6;line-height:1.45;margin-top:.06in}}
</style></head><body><div class="back"></div><div class="spine"></div><div class="front"></div>
<div class="txt"><div class="kick">{t['kicker']}</div><h1>{t['head']}</h1>{paras}
<div class="rule"></div><div class="auth">{t['author']}</div><div class="meta">{t['meta']}</div></div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for tag in ['de','en']:
            W,H,s,h=html(tag); open(f'wrap_{tag}.html','w').write(h)
            pg=await b.new_page(viewport={'width':int(W*96),'height':int(H*96)})
            await pg.goto('file://'+os.path.abspath(f'wrap_{tag}.html')); await pg.wait_for_timeout(600)
            name=f'IKO_Paperback_Cover_{tag.capitalize()}.pdf'
            await pg.pdf(path=name,width=f'{W}in',height=f'{H}in',print_background=True,prefer_css_page_size=True)
            await pg.screenshot(path=f'prev_{tag}.png')
            bot=await pg.evaluate("document.querySelector('.txt').getBoundingClientRect().bottom/96")
            print(tag,'W',round(W,4),'spine',round(s,4),'textbottom',round(bot,2))
        await b.close()
asyncio.run(main())
