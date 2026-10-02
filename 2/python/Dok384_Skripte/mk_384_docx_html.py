#!/usr/bin/env python3
"""
mk_384_docx_html.py -- Dok. 384: Word- und HTML-Fassung aus der LaTeX-Quelle.

Erzeugt aus 2/Sources/ch/384_FFGFT_Kurzfassung_{De,En}_ch.tex
  2/docx/384_FFGFT_Kurzfassung_{De,En}.docx   (Formeln als Word-Formeln)
  2/html/384_FFGFT_Kurzfassung_{De,En}.html   (eigenständig, Formeln als MathML)
Benötigt pandoc (>= 3). Aufruf aus der Repo-Wurzel:
  python3 2/python/Dok384_Skripte/mk_384_docx_html.py
Der Inhalt wird nicht verändert; das Skript übersetzt nur die Layout-Makros
(Kästen, farbige Statusmarker, Zeilenfarben) in Word- bzw. HTML-Gestaltung.
"""
import os, re, subprocess, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC = os.path.join(ROOT, '2', 'Sources', 'ch')

META = {
    'De': dict(title='FFGFT in Kurzfassung',
               subtitle='Grundlagen, Ergebnisse und Status nach der Rechenprüfung',
               date='1. Oktober 2026 (erweitert und neu formatiert am 2. Oktober 2026)',
               lang='de-DE', abstract='Zusammenfassung', toc='Inhalt'),
    'En': dict(title='FFGFT in Brief',
               subtitle='Foundations, results and status after the calculation review',
               date='1 October 2026 (extended and reformatted 2 October 2026)',
               lang='en-GB', abstract='Abstract', toc='Contents'),
}
AUTHOR = 'Johann Pascher, ORCID 0009-0000-6518-4064'

LUA = r'''
local colors = {B="007F00", K="1565C0", S="E65100", X="BF0000", Q="616161"}
local css = {B="#007f00", K="#1565c0", S="#e65100", X="#bf0000", Q="#616161"}

function Strong(el)
  local t = pandoc.utils.stringify(el)
  local m = t:match("^%[([BKSXQ])%]$")
  if m then
    if FORMAT:match("docx") then
      return pandoc.RawInline("openxml",
        '<w:r><w:rPr><w:b/><w:color w:val="' .. colors[m] .. '"/></w:rPr><w:t xml:space="preserve">[' .. m .. ']</w:t></w:r>')
    elseif FORMAT:match("html") then
      return pandoc.RawInline("html", '<strong class="st st-' .. m .. '">[' .. m .. ']</strong>')
    end
  end
end

local function titel(strong)
  local inl = strong.content:clone()
  while #inl > 0 and (inl[1].t == "Space" or (inl[1].t == "Str" and inl[1].text:match("^KASTEN:"))) do
    table.remove(inl, 1)
  end
  return inl
end

function BlockQuote(el)
  if FORMAT:match("html") then
    local cls = "kern"
    local first = el.content[1]
    if first and first.t == "Para" and first.content[1] and first.content[1].t == "Strong"
       and pandoc.utils.stringify(first.content[1]):match("^KASTEN:") then
      cls = "kasten"
      table.remove(el.content, 1)
      table.insert(el.content, 1, pandoc.Div({pandoc.Plain(titel(first.content[1]))}, {class="kasten-titel"}))
    end
    return pandoc.Div(el.content, {class=cls})
  else
    local first = el.content[1]
    if first and first.t == "Para" and first.content[1] and first.content[1].t == "Strong"
       and pandoc.utils.stringify(first.content[1]):match("^KASTEN:") then
      el.content[1] = pandoc.Para({pandoc.Strong(titel(first.content[1]))})
    end
    return el
  end
end
'''

CSS = r'''
body { max-width: 52em; margin: 2em auto; padding: 0 1.2em; font-family: "Segoe UI", Arial, sans-serif;
       line-height: 1.5; color: #222; background: #fff; }
h1.title { font-size: 2em; margin-bottom: .1em; }
p.subtitle { font-size: 1.2em; color: #444; margin-top: 0; }
p.author, p.date { color: #555; margin: .1em 0; }
h1 { border-bottom: 2px solid #1565c0; padding-bottom: .15em; margin-top: 1.6em; }
h2 { color: #0d47a1; margin-top: 1.3em; }
div.abstract { background: #f5f7fa; border-left: 4px solid #1565c0; padding: .6em 1em; font-style: italic; }
div.kern { background: #eef5fd; border: 1px solid #1565c0; border-radius: 4px; padding: .3em .9em; margin: .9em 0; }
div.kasten { background: #f7f7f7; border: 1px solid #777; border-radius: 4px; padding: 0 .9em .4em .9em; margin: .9em 0; }
div.kasten-titel { background: #666; color: #fff; font-weight: bold; font-size: .92em;
                   margin: 0 -.9em .5em -.9em; padding: .2em .9em; border-radius: 3px 3px 0 0; }
.st { font-weight: bold; }
.st-B { color: #007f00; } .st-K { color: #1565c0; } .st-S { color: #e65100; }
.st-X { color: #bf0000; } .st-Q { color: #616161; }
table { border-collapse: collapse; margin: .8em auto; font-size: .93em; }
th { border-bottom: 2px solid #444; text-align: left; padding: .25em .6em; }
td { padding: .2em .6em; vertical-align: top; }
tbody tr:nth-child(odd) { background: #f3f3f3; }
nav#TOC { background: #fafafa; border: 1px solid #ddd; padding: .4em 1.2em; font-size: .92em; }
math { font-size: 1.05em; }
'''


def prepare(tex, lang):
    # Layout-Block entfernen (Makros werden unten aufgelöst)
    tex = re.sub(r'% Layout.*?before skip=8pt,after skip=8pt}\n', '', tex, flags=re.S)
    tex = re.sub(r'\\providecommand\{\\[A-Z]M\}\{[^\n]*\}\n', '', tex)
    for k in 'BKSXQ':
        tex = tex.replace('\\' + k + 'M\\ ', '\\textbf{[' + k + ']} ')
        tex = tex.replace('\\' + k + 'M', '\\textbf{[' + k + ']}')
    tex = re.sub(r'\\chapter\*\{[^}]*\}\n\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}\n', '', tex)
    # Kästen -> Zitatblöcke (der Lua-Filter macht daraus Kästen)
    tex = tex.replace('\\begin{ffkern}', '\\begin{quote}').replace('\\end{ffkern}%', '\\end{quote}')
    tex = tex.replace('\\end{ffkern}', '\\end{quote}')
    tex = re.sub(r'\\begin\{ffkasten\}\{(.*?)\}\n', lambda m: '\\begin{quote}\n\\textbf{KASTEN: ' + m.group(1) + '}\n\n', tex)
    tex = tex.replace('\\end{ffkasten}', '\\end{quote}')
    # Tabellen-/Listenoptionen, die pandoc nicht kennt
    tex = re.sub(r'\\rowcolors\{[^}]*\}\{[^}]*\}\{[^}]*\}\n', '', tex)
    tex = re.sub(r'\\rowcolor\{[^}]*\}', '', tex)
    tex = re.sub(r'\\begin\{(itemize|enumerate|description)\}\[[^\]]*\]', r'\\begin{\1}', tex)
    tex = re.sub(r'\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{[^{}]*\}', r'\1', tex)
    tex = tex.replace('\\glqq ', '„').replace('\\glqq{}', '„').replace('\\glqq', '„')
    tex = tex.replace('\\grqq{}', '“').replace('\\grqq\\ ', '“ ').replace('\\grqq', '“')
    tex = tex.replace('\\begin{center}\n\\small\n', '\\begin{center}\n')
    tex = tex.replace('{,}', '\\text{,}')
    tex = tex.replace('\\multicolumn{4}{@{}l}', '\\multicolumn{4}{l}')
    for a, b in (('\\Bigl', '\\left'), ('\\Bigr', '\\right'), ('\\bigl', '\\left'), ('\\bigr', '\\right')):
        tex = tex.replace(a, b)
    return '\\documentclass{article}\n\\usepackage{amsmath,amssymb}\n\\begin{document}\n' + tex + '\n\\end{document}\n'


def run(lang):
    m = META[lang]
    tex = open(os.path.join(SRC, f'384_FFGFT_Kurzfassung_{lang}_ch.tex'), encoding='utf-8').read()
    src = prepare(tex, lang)
    os.makedirs(os.path.join(ROOT, '2', 'docx'), exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        p_tex = os.path.join(td, 'in.tex'); open(p_tex, 'w', encoding='utf-8').write(src)
        p_lua = os.path.join(td, 'f.lua'); open(p_lua, 'w').write(LUA)
        p_css = os.path.join(td, 's.css'); open(p_css, 'w').write(CSS)
        common = ['pandoc', p_tex, '-f', 'latex', '--lua-filter', p_lua, '--toc', '--toc-depth=2',
                  '-M', 'title=' + m['title'], '-M', 'subtitle=' + m['subtitle'],
                  '-M', 'author=' + AUTHOR, '-M', 'date=' + m['date'], '-M', 'lang=' + m['lang'],
                  '-M', 'toc-title=' + m['toc'], '-M', 'abstract-title=' + m['abstract'],
                  '--number-sections']
        out_docx = os.path.join(ROOT, '2', 'docx', f'384_FFGFT_Kurzfassung_{lang}.docx')
        subprocess.run(common + ['-t', 'docx', '-o', out_docx], check=True)
        out_html = os.path.join(ROOT, '2', 'html', f'384_FFGFT_Kurzfassung_{lang}.html')
        subprocess.run(common + ['-t', 'html5', '-s', '--mathml', '--embed-resources',
                                 '--css', p_css, '-o', out_html], check=True)
    print('erstellt:', os.path.relpath(out_docx, ROOT), os.path.relpath(out_html, ROOT))


if __name__ == '__main__':
    for lang in ('De', 'En'):
        run(lang)
