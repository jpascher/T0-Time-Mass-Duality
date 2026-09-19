import pikepdf
from pikepdf import Name, Dictionary, Array
import sys
# Aufruf: python3 fix_pdf_seite7.py <Kindle_De.pdf> <Kindle_En.pdf> [scale]
# scale 0.95 = Paperback (Raender), 1.0 = Kindle
U=''
JOBS=[('De',sys.argv[1],616.5),('En',sys.argv[2],603.5)]
S=float(sys.argv[3]) if len(sys.argv)>3 else 0.95; W,H=432,648; TX=W*(1-S)/2; TY=H*(1-S)/2
for tag,src,cut in JOBS:
    pdf=pikepdf.open(src)
    # remove footer rule on page 7
    pg7=pdf.pages[6]; ops=pikepdf.parse_content_stream(pg7)
    new=[]
    for i,(o,op) in enumerate(ops):
        if str(op)=='cm' and abs(float(o[5])-30.199)<0.5:
            # zero-length the following line
            for j in range(i+1,i+6):
                if str(ops[j][1])=='l': ops[j]=pikepdf.ContentStreamInstruction([0,0],pikepdf.Operator('l'))
    pg7.Contents=pdf.make_stream(pikepdf.unparse_content_stream(ops))
    out=pikepdf.new()
    def add(page,clip=None,dy=0):
        xo=out.copy_foreign(page.as_form_xobject()); xo.BBox=Array([0,-700,W,H])
        np=out.add_blank_page(page_size=(W,H))
        np.Resources=Dictionary(XObject=Dictionary(P=xo))
        c=f'q {S} 0 0 {S} {TX} {TY} cm '
        if clip: c+=f'0 {clip[0]} {W} {clip[1]-clip[0]} re W n '
        c+=f'1 0 0 1 0 {dy} cm /P Do Q'
        # note: clip is applied before dy shift, in shifted coords -> handle below
        np.Contents=out.make_stream(c.encode())
    for i,pg in enumerate(pdf.pages):
        if i==6:
            add(pg,clip=(H-cut,H))                        # 7a: top part
            dy=cut-50                                     # 7b: shift lower part up
            add(pg,clip=(-1000+dy+0, H-cut+dy),dy=dy)    # clip in page coords after shift
        else:
            add(pg)
    fn=f'366_Feldstruktur_FFGFT_{"Paperback" if S<1 else "Kindle"}_{tag}_fix.pdf'
    out.save(fn); print(fn,len(out.pages))

# Hinweis: fuer die Paperback-Fassung wurden danach die Seiten 7-8 mit 600 dpi (Graustufen) gerastert,
# damit KDP den weggeclippten Text nicht als Randueberschreitung meldet; die En-Fassung bekam eine Leerseite (38 S.).
