#!/usr/bin/env python3
"""Monta as páginas do site Spinfy.co a partir dos parciais em src/.
Uso: python3 src/build.py   (gera os .html na raiz do projeto)"""
import json, re, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
ICONS = json.load(open(SRC / 'icons.json'))
rd = lambda n: (SRC / n).read_text()

WA = 'https://wa.me/554191347696'
AGENDA = 'contato.html#agendar'
AVATAR = 'https://images.unsplash.com/photo-1702669010463-3f2088abc0e9?w=120&amp;h=120&amp;fit=crop&amp;crop=faces&amp;q=80'

# Ícones de traço feitos para as páginas internas (mesma espessura visual do conjunto)
STROKE = {
    'clock': '<circle cx="128" cy="128" r="92"/><path d="M128 76v52l34 22"/>',
    'shield': '<path d="M128 30l82 30v58c0 52-35 90-82 108-47-18-82-56-82-108V60z"/><path d="M92 128l26 26 46-50"/>',
    'mail': '<rect x="30" y="58" width="196" height="140" rx="12"/><path d="M34 66l94 72 94-72"/>',
    'plus': '<path d="M128 56v144M56 128h144"/>',
    'book': '<path d="M40 52h64a24 24 0 0 1 24 24v128a18 18 0 0 0-18-18H40zM216 52h-64a24 24 0 0 0-24 24v128a18 18 0 0 1 18-18h70z"/>',
    'quiz': '<rect x="44" y="34" width="168" height="188" rx="14"/><path d="M84 86h88M84 128h88M84 170h50"/>',
    'video': '<rect x="26" y="66" width="148" height="124" rx="14"/><path d="M174 112l56-32v96l-56-32"/>',
    'map': '<path d="M30 62l64-24 68 24 64-24v156l-64 24-68-24-64 24zM94 38v156M162 62v156"/>',
    'layers': '<path d="M128 34l98 50-98 50-98-50z"/><path d="M30 134l98 50 98-50M30 172l98 50 98-50"/>',
    'cpu': '<rect x="66" y="66" width="124" height="124" rx="12"/><path d="M104 30v36M152 30v36M104 190v36M152 190v36M30 104h36M30 152h36M190 104h36M190 152h36"/>',
    'chartbar': '<path d="M36 214h184M64 214v-60M112 214V96M160 214v-86M208 214V58"/>',
    'archive': '<rect x="30" y="44" width="196" height="48" rx="8"/><path d="M46 92v120h164V92M104 132h48"/>',
    'gem': '<path d="M74 44h108l46 54-100 116L28 98z"/><path d="M28 98h200M104 44l-22 54 46 116 46-116-22-54"/>',
    'network': '<circle cx="128" cy="62" r="26"/><circle cx="56" cy="190" r="26"/><circle cx="200" cy="190" r="26"/><path d="M114 84l-44 82M142 84l44 82M82 190h92"/>',
}

def icon(name, cls='ico'):
    if name in STROKE:
        return (f'<svg class="{cls}" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" '
                f'fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">{STROKE[name]}</svg>')
    paths = ''.join(f'<path d="{d}"/>' for d in ICONS[name])
    return f'<svg class="{cls}" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor">{paths}</svg>'

def callbtn(label='Agende uma conversa', href=AGENDA, extra=''):
    return (f'<a class="btn call" {extra}href="{href}"><span class="av"><img src="{AVATAR}" alt="" width="42" height="42"><i></i></span>'
            f'<span class="lbl">{label}</span></a>')

NAV = [('para-empresarios', 'Para empresários'), ('casos', 'Casos de sucesso'), ('quem-somos', 'Quem somos'), ('perguntas-frequentes', 'Perguntas frequentes')]

def header(active):
    nav = ''.join(f'<a href="{k}.html"{" class=\"on\" aria-current=\"page\"" if k == active else ""}>{v}</a>' for k, v in NAV)
    nav += '<a href="seja-conselheiro.html" class="mob">Seja um conselheiro</a><a href="jornada-equity.html" class="mob">Jornada Equity</a><a href="contato.html" class="mob">Contato</a>'
    return f'''<div class="mast" id="top">
<div class="util">
  <div class="wrap">
    <div class="g">
      <a href="https://www.instagram.com/spinfy.co/" target="_blank" rel="noopener">{icon('instagram')}Instagram</a>
      <a href="https://www.linkedin.com/company/spinfy/" target="_blank" rel="noopener">{icon('linkedin')}LinkedIn</a>
    </div>
    <div class="g">
      <a href="seja-conselheiro.html">{icon('users')}Para conselheiros</a>
      <a href="jornada-equity.html">{icon('compass')}Jornada Equity</a>
      <a href="https://spinfy.app.br">{icon('lock')}Acesso restrito</a>
    </div>
  </div>
</div>
<header class="top">
  <div class="wrap">
    <nav class="nav" id="nav" aria-label="Menu principal">{nav}</nav>
    <a class="logo" href="index.html" aria-label="Spinfy.co, página inicial">{rd('_logo.html')}</a>
    <div class="right">
      <a class="help" href="contato.html">Não sabe por onde começar?<b>Fale com um especialista</b></a>
      {callbtn()}
      <button class="burger" id="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="nav">{icon('menu')}</button>
    </div>
  </div>
</header>
</div>
'''

def footer():
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-g">
      <div>
        <a class="logo" href="index.html" aria-label="Spinfy.co">{rd('_flogo.html')}</a>
        <p class="motto2">A empresa gira e todos ganham.</p>
      </div>
      <div><h4>Empresários</h4><ul><li><a href="para-empresarios.html">Para empresários</a></li><li><a href="casos.html">Casos de sucesso</a></li><li><a href="perguntas-frequentes.html">Perguntas frequentes</a></li><li><a href="{AGENDA}">Agende uma conversa</a></li></ul></div>
      <div><h4>Spinfy.co</h4><ul><li><a href="quem-somos.html">Quem somos</a></li><li><a href="seja-conselheiro.html">Seja um conselheiro</a></li><li><a href="jornada-equity.html">Jornada Equity</a></li><li><a href="https://spinfy.app.br">Acesso restrito</a></li></ul></div>
      <div><h4>Contato</h4><ul><li><a href="tel:+554130218343">(41) 3021-8343</a></li><li><a href="mailto:service@spinfy.co">service@spinfy.co</a></li><li>Rua Ébano Pereira, 60, 21º andar</li><li>Centro, Curitiba/PR, 80410-250</li></ul></div>
    </div>
    <div class="foot-b"><span>© 2026 Spinfy.co. Todos os direitos reservados.</span><span class="kroma">Feito com {rd('_heart.html')} por <a href="https://agenciakroma.com.br/" target="_blank" rel="noopener">Agência KROMA</a></span></div>
  </div>
</footer>

{rd('_totop.html')}
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Fale pelo WhatsApp">{icon('whatsapp')}<span>WhatsApp</span></a>
'''

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400;1,6..72,500&family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@400;500;600&family=Unbounded:wght@500;700;800&display=swap">
<link rel="stylesheet" href="css/site.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Spinfy.co","url":"https://spinfy.co","email":"service@spinfy.co","telephone":"+55-41-3021-8343","foundingDate":"2015","address":{{"@type":"PostalAddress","streetAddress":"Rua Ébano Pereira, 60, Andar 21, Centro","addressLocality":"Curitiba","addressRegion":"PR","postalCode":"80410-250","addressCountry":"BR"}},"description":"Conselho entre pares para empresários de médias empresas. Sistema 7SS, aconselhamento, captação e M&A."}}
</script>
</head>
<body>
'''

def phero(eyebrow, title, sub, video, poster, crumb, ctas='', side='', note=''):
    return f'''<section class="hero phero" aria-label="Apresentação">
  <video autoplay muted loop playsinline preload="auto" poster="{poster}">
    <source src="{video}" type="video/mp4">
  </video>
  <div class="shade"></div>
  <div class="mark" data-spin>{rd('_mark.html')}</div>
  <svg class="trail" viewBox="0 0 1440 220" preserveAspectRatio="none" aria-hidden="true"><path d="M-20 200 C 260 210, 420 120, 700 130 S 1120 40, 1460 10"/></svg>
  <div class="hero-in">
    <div class="wrap hero-grid{' solo' if not side else ''}">
      <div>
        <nav class="crumb hl" style="--d:.05s" aria-label="Você está em"><a href="index.html">Início</a><span>/</span><b>{crumb}</b></nav>
        <span class="eyebrow lt hl" style="--d:.1s">{eyebrow}</span>
        <h1 class="hl" style="--d:.25s">{title}</h1>
        <p class="sub hl" style="--d:.45s">{sub}</p>
        {f'<div class="ctas hl" style="--d:.6s">{ctas}</div>' if ctas else ''}
        {f'<p class="note hl" style="--d:.75s">{note}</p>' if note else ''}
      </div>
      {side}
    </div>
  </div>
</section>
'''

def close_block(title, eyebrow='Agende uma conversa', note='Ainda está avaliando? Comece pelo WhatsApp. Atendimento presencial em Curitiba, online e na sua empresa.', btn=None, img='https://images.unsplash.com/photo-1779700210487-a01758a3c55a?auto=format&fit=crop&w=1800&q=72'):
    btn = btn or callbtn()
    return f'''<section class="sec close" id="fechamento">
  <div class="bg"><img src="{img}" alt="" loading="lazy" data-par=".12"></div>
  <div class="wrap close-in">
    <div class="rv">
      <span class="eyebrow lt">{eyebrow}</span>
      <h2>{title}</h2>
      <div class="ctas">
        {btn}
        <a class="btn ghost-lt" href="{WA}" target="_blank" rel="noopener">{icon('whatsapp')}Prefiro o WhatsApp</a>
      </div>
      <p class="note">{note}</p>
    </div>
    <div class="contact stg">
      <a class="ccard" href="tel:+554130218343"><span class="ic">{icon('phone')}</span><span><small>Telefone</small><b>(41) 3021-8343</b></span></a>
      <a class="ccard" href="{WA}" target="_blank" rel="noopener"><span class="ic">{icon('whatsapp')}</span><span><small>WhatsApp</small><b>Fale com a nossa equipe</b></span></a>
      <div class="ccard"><span class="ic">{icon('pin')}</span><span><small>Endereço</small><b>Rua Ébano Pereira, 60, 21º andar, Centro, Curitiba/PR</b></span></div>
    </div>
  </div>
</section>
'''

CTX = {}

def render(text):
    text = re.sub(r'\{\{icon:([a-z]+)\}\}', lambda m: icon(m.group(1)), text)
    text = re.sub(r'\{\{([a-z_]+)\}\}', lambda m: str(CTX[m.group(1)]), text)
    return text

PAGES = [
    ('index', 'Spinfy.co · Conselho entre pares para empresas médias', 'Na Spinfy.co, o empresário senta à mesa com conselheiros que conhecem seus desafios, ganha uma agenda estratégica, depende menos de dívida e passa a ter mais opções: captar, se associar, vender, investir ou se tornar conselheiro também.', None),
    ('para-empresarios', 'Para empresários · Spinfy.co', 'A jornada da Spinfy.co para o empresário fundador: pré-diagnóstico, estruturação estratégica em 90 dias, 9 meses de aconselhamento e o Sistema 7SS.', 'para-empresarios'),
    ('jornada-equity', 'Jornada Equity · Spinfy.co', 'A Jornada Equity é a porta de entrada para executivos, advisors e conselheiros que querem valorizar a própria experiência e atuar na rede Spinfy.co.', None),
    ('casos', 'Casos de sucesso · Spinfy.co', 'Empresas que passaram pela mesa da Spinfy.co: 240 empresários aconselhados, 57 intermediações de captação e M&A e R$ 310 milhões transacionados.', 'casos'),
    ('quem-somos', 'Quem somos · Spinfy.co', 'A Spinfy.co constrói as mesas onde empresários de médias empresas decidem ao lado de conselheiros que já viveram seus desafios. Conheça o manifesto, Marcelo Fonzaghi e os nossos valores.', 'quem-somos'),
    ('seja-conselheiro', 'Seja um conselheiro · Spinfy.co', 'Executivos, empresários e profissionais de finanças, contabilidade e jurídico podem atuar como conselheiros na rede Spinfy.co, com formação no Sistema 7SS.', None),
    ('perguntas-frequentes', 'Perguntas frequentes · Spinfy.co', 'Respostas sobre conselho e consultoria, prazos, cobrança, sigilo, participação de sócios e filhos e como começa o trabalho com a Spinfy.co.', 'perguntas-frequentes'),
    ('contato', 'Contato e agendamento · Spinfy.co', 'Agende uma conversa de 30 minutos com um conselheiro sênior da Spinfy.co. Telefone, WhatsApp e endereço em Curitiba.', None),
]

def build():
    CTX.update(call=callbtn(), call_hero=callbtn(extra='data-hero-cta '), wa=WA, agenda=AGENDA,
               mark=rd('_mark.html'), markcolor=rd('_markcolor.html'))
    import importlib.util
    spec = importlib.util.spec_from_file_location('content', SRC / 'content.py')
    content = importlib.util.module_from_spec(spec); spec.loader.exec_module(content)
    for slug, title, desc, active in PAGES:
        body = rd(f'pages/{slug}.html') if slug == 'index' else content.PAGE[slug](globals())
        html = head(title, desc) + '\n' + header(active) + '\n<main>\n' + render(body) + '\n</main>\n\n' + footer() + '\n<script src="js/site.js"></script>\n</body>\n</html>\n'
        (ROOT / f'{slug}.html').write_text(html)
        print('ok', slug, len(html))

if __name__ == '__main__':
    build()
