# Conteúdo das páginas internas do site Spinfy.co.
# Cada função recebe os utilitários do build (g) e devolve o HTML do <main>.

U = 'https://images.unsplash.com/'
def img(i, w=1100):
    return f'{U}{i}?auto=format&fit=crop&w={w}&q=72'
def vid(i, fps=25):
    return f'https://videos.pexels.com/video-files/{i}/{i}-hd_1920_1080_{fps}fps.mp4'
def poster(i, name='pexels-photo'):
    return f'https://images.pexels.com/videos/{i}/{name}-{i}.jpeg?auto=compress&w=1920'


def para_empresarios(g):
    I, H = g['icon'], g['phero']
    side = f'''<aside class="route hl" style="--d:.9s" aria-label="Prazos da jornada">
        <div class="route-top"><span class="ri">{g['CTX']['markcolor']}</span><p class="rt">A jornada em prazos claros</p></div>
        <ol class="rsteps">
          <li><span class="rn">1</span><div><b>10 dias</b><small>pré-diagnóstico na plataforma</small></div></li>
          <li><span class="rn">2</span><div><b>90 dias</b><small>estruturação estratégica</small></div></li>
          <li><span class="rn">3</span><div><b>9 meses</b><small>aconselhamento, com Board Pack</small></div></li>
          <li class="on"><span class="rn">4</span><div><b>À mesa</b><small>valores e oportunidades para você decidir</small></div></li>
        </ol>
      </aside>'''
    hero = H('Para empresários', 'Do dia a dia <em class="o">à cadeira do conselho.</em>',
             'Uma jornada com prazos claros para o fundador que quer pensar o futuro da empresa com quem conhece seus desafios.',
             vid(7552490), poster(7552490), 'Para empresários',
             ctas=g['CTX']['call_hero'] + f'<a class="tlink" href="#jornada" style="color:#fff">Veja a jornada <span class="c">{I("arrow")}</span></a>',
             side=side,
             note='Uma conversa de 30 minutos com um conselheiro sênior. É o primeiro passo do diagnóstico, e o investimento é informado antes da confirmação.')
    return hero + f'''
<!-- PARA QUEM É -->
<section class="sec">
  <div class="wrap duo">
    <div class="collage rv-l">
      <div class="mark nv" data-spin>{g['CTX']['mark']}</div>
      <div class="a rv-img"><img src="{img('photo-1714974528232-f62051870736')}" alt="Empresário experiente conversando com outro executivo à mesa" loading="lazy"></div>
      <div class="b rv-s" style="--d:.35s"><img src="{img('photo-1790596685394-4a6c0ca886f2',700)}" alt="Retrato de empresário de cabelos grisalhos no escritório" loading="lazy"></div>
      <div class="badge rv" style="--d:.6s"><b>240</b><span>empresários aconselhados pela Spinfy.co</span></div>
    </div>
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">Para quem é</span>
      <h2 class="h2 rv-h">Para quem construiu a empresa e <em class="o">quer decidir melhor</em> o próximo passo.</h2>
      <div class="prose">
        <p>A Spinfy.co atende empresas médias conduzidas pelo fundador ou em passagem entre gerações. Em geral, são negócios sólidos, com décadas de história, que chegaram a um ponto em que o dia a dia não deixa tempo para pensar o futuro.</p>
        <p>As decisões importantes raramente são tomadas sozinho. Sócios, filhos, advogado e contador participam, e o processo foi pensado para incluir essas pessoas.</p>
      </div>
      <div class="who">
        <div><b>R$ 30 a 100 mi</b><span>de faturamento anual, na maioria dos casos</span></div>
        <div><b>Fundador</b><span>ou família na passagem entre gerações</span></div>
        <div><b>Indústria e serviços</b><span>alimentos, construção, madeira e outros setores</span></div>
      </div>
    </div>
  </div>
</section>

<!-- SITUAÇÕES -->
<section class="sec dark prob">
  <div class="bg"><img src="{img('photo-1517048676732-d65bc937f952',1800)}" alt="" loading="lazy" data-par=".12"></div>
  <div class="wrap">
    <div class="shead">
      <div class="rv">
        <span class="eyebrow">O ponto de partida</span>
        <h2 class="h2 rv-h">O que costuma trazer o empresário <em class="o">até a mesa.</em></h2>
      </div>
      <p class="lead rv" style="--d:.1s">São as situações que mais aparecem na primeira conversa. Muitas vezes, mais de uma ao mesmo tempo.</p>
    </div>
    <div class="pains stg">
      <article class="pain"><span class="n">01</span><div class="ic">{I('bank')}</div><h3>Dependência de dívida</h3><p>Os juros pesam no caixa e em cada decisão.</p></article>
      <article class="pain"><span class="n">02</span><div class="ic">{I('coins')}</div><h3>Falta de capital</h3><p>Faltam recursos para dar o próximo passo.</p></article>
      <article class="pain"><span class="n">03</span><div class="ic">{I('users')}</div><h3>Sucessão em aberto</h3><p>Ainda não há um herdeiro preparado para assumir.</p></article>
      <article class="pain"><span class="n">04</span><div class="ic">{I('compass')}</div><h3>Decisões solitárias</h3><p>As escolhas importantes são feitas sem dados e sem com quem conversar.</p></article>
    </div>
    <div class="prob-foot rv">
      <p>Você não precisa decidir sozinho.</p>
      {g['callbtn']('Converse sobre o seu caso')}
    </div>
  </div>
</section>

<!-- JORNADA -->
<section class="sec ivory" id="jornada">
  <div class="wrap">
    <div class="shead">
      <div class="rv">
        <span class="eyebrow">A jornada</span>
        <h2 class="h2 rv-h">Quatro etapas, <em class="o">uma de cada vez.</em></h2>
      </div>
      <p class="lead rv" style="--d:.1s">Do primeiro diagnóstico até a cadeira de conselho da sua própria empresa. Cada etapa tem prazo e entrega definidos.</p>
    </div>
    <div class="journey stg">
      <article class="jstep">
        <span class="num">01</span>
        <div><span class="t">10 + 90 dias</span><h3>Prepare</h3><p>A empresa é organizada para que as decisões partam de dados, e não da urgência.</p></div>
        <div><span class="k">O que acontece</span><ul>
          <li>{I('check')}Cadastro da empresa e pré-diagnóstico na plataforma, em cerca de 10 dias.</li>
          <li>{I('check')}Estruturação estratégica em 90 dias, com o Sistema 7SS.</li>
          <li>{I('check')}Uma estratégia escrita, com prioridades e indicadores.</li></ul></div>
      </article>
      <article class="jstep">
        <span class="num">02</span>
        <div><span class="t">9 meses</span><h3>Valorize</h3><p>Os conselheiros passam a sentar com você a cada três meses para acompanhar e ajustar o rumo.</p></div>
        <div><span class="k">O que acontece</span><ul>
          <li>{I('check')}Planejamento, plano de negócio e governança.</li>
          <li>{I('check')}Relatório do conselho (Board Pack) desde o primeiro encontro.</li>
          <li>{I('check')}Menos dependência de dívida e uma empresa que vale mais.</li></ul></div>
      </article>
      <article class="jstep">
        <span class="num">03</span>
        <div><span class="t">Mais opções</span><h3>Escolha</h3><p>Com a casa organizada, surgem caminhos que antes não estavam na mesa.</p></div>
        <div><span class="k">Caminhos possíveis</span><ul>
          <li>{I('check')}Adquirir, captar, vender ou se associar.</li>
          <li>{I('check')}Aconselhar outras empresas com a experiência que você construiu.</li>
          <li>{I('check')}Nenhum caminho é obrigatório. Quem escolhe é você.</li></ul></div>
      </article>
      <article class="jstep">
        <span class="num">04</span>
        <div><span class="t">À mesa</span><h3>Realize</h3><p>Valores e oportunidades à mesa para você decidir, com dados e com conselheiros de confiança.</p></div>
        <div><span class="k">O que muda</span><ul>
          <li>{I('check')}Você passa a decidir do conselho, e não da operação.</li>
          <li>{I('check')}Mais tempo para a estratégia e para a família.</li>
          <li>{I('check')}Se quiser, também aconselha outras empresas.</li></ul></div>
      </article>
    </div>
  </div>
</section>

<!-- PASSAR A ACONSELHAR -->
<section class="sec">
  <div class="wrap duo rev">
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">Conselheiro em 9 meses</span>
      <h2 class="h2 rv-h">Sentar do <em class="o">outro lado da mesa.</em></h2>
      <div class="prose">
        <p>Ao fim dos 9 meses de aconselhamento, você pode delegar o papel executivo e ocupar a cadeira do conselho da sua própria empresa.</p>
        <p>Se quiser, também pode aconselhar outras empresas. É uma forma de diluir o risco, ampliar a experiência e colocar em uso o que você levou décadas para aprender.</p>
      </div>
      <ul class="ticks">
        <li>{I('checkcircle')}No conselho da sua empresa, com mais tempo para a estratégia.</li>
        <li>{I('checkcircle')}Em outras empresas, como conselheiro da rede Spinfy.co.</li>
      </ul>
    </div>
    <div class="img rv-img"><img src="{img('photo-1714974528796-e4e7a077d0cc',1100)}" alt="Empresário experiente falando à mesa de reunião" loading="lazy"><div class="cap2">{I('chair')}Quem aconselha você já sentou na sua cadeira.</div></div>
  </div>
</section>

<!-- SISTEMA 7SS -->
<section class="sec navyb" id="sistema-7ss" style="position:relative;overflow:hidden;isolation:isolate">
  <div class="mark" data-spin style="right:-160px;top:-120px;width:560px">{g['CTX']['mark']}</div>
  <div class="wrap">
    <div class="shead">
      <div class="rv">
        <span class="eyebrow">Método próprio</span>
        <div class="sys-logo" role="img" aria-label="Sistema 7SS"><span class="tx"><span class="s1">Sistema</span><span class="s2">7<i>SS</i></span></span></div>
        <h2 class="h2 rv-h" style="font-size:clamp(30px,3.2vw,44px)">O método que dá nome <em class="o">à Spinfy.co.</em></h2>
      </div>
      <p class="lead rv" style="--d:.1s">Sete etapas, uma para cada letra do nome. Juntas, formam o diagnóstico completo da empresa e a base de cada conselho. O e-book Bússola do Equity explica cada uma em detalhe.</p>
    </div>
    <div class="ss stg">
      <div class="ssi"><b class="l">S</b><div><h3>Situação</h3><p>A situação econômica, financeira e operacional da empresa.</p></div></div>
      <div class="ssi"><b class="l">P</b><div><h3>Posicionamento</h3><p>O posicionamento da empresa no mercado e as atitudes de quem a conduz.</p></div></div>
      <div class="ssi"><b class="l">I</b><div><h3>Indicadores</h3><p>Os indicadores do negócio, organizados em painéis de acompanhamento (BI).</p></div></div>
      <div class="ssi"><b class="l">N</b><div><h3>Negligências</h3><p>Os riscos e os pontos que estão sendo deixados de lado.</p></div></div>
      <div class="ssi"><b class="l">F</b><div><h3>Forecast</h3><p>Os cenários financeiros para os próximos anos (FP&amp;A).</p></div></div>
      <div class="ssi"><b class="l">Y</b><div><h3>Yield</h3><p>Como o resultado é distribuído e quanto é reinvestido.</p></div></div>
      <div class="ssi co"><b class="l">Co</b><div><h3>Conselho aos objetivos</h3><p>O conselho cruza as análises anteriores e sugere os objetivos da empresa. A decisão é sempre sua.</p></div></div>
    </div>
    <div class="aibox rv">
      <span class="ic">{I('ai')}</span>
      <p><b>Inteligência artificial a serviço do conselho.</b> Cada etapa é analisada por um colegiado de IA inspirado nas maiores referências do mercado. Na etapa final, o Marcellus, nosso conselheiro de IA, cruza essas análises e sugere caminhos. Quem decide é você, à mesa com os conselheiros.</p>
      {g['callbtn']('Agende uma conversa')}
    </div>
  </div>
</section>

<!-- CONSELHEIRO X CONSULTOR -->
<section class="sec vs-sec">
  <div class="wrap vs">
    <figure class="vs-img rv-img" style="margin:0">
      <img src="{img('photo-1714974528683-8940bd8311aa')}" alt="Dois executivos analisando números juntos em um notebook" loading="lazy">
      <figcaption>{I('chair')}Conselheiro não executa por você. Ajuda você a decidir melhor.</figcaption>
    </figure>
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">Conselho e consultoria</span>
      <h2 class="h2 rv-h">Conselheiro <em class="o">não é</em> consultor.</h2>
      <div class="cmp" role="table" aria-label="Diferença entre consultor e conselheiro">
        <div class="cmp-row" role="row"><div role="columnheader"></div><div role="columnheader">Consultor</div><div role="columnheader">Conselheiro</div></div>
        <div class="cmp-row" role="row"><div role="rowheader">O que faz</div><div role="cell">Faz um diagnóstico e entrega um relatório.</div><div role="cell">Senta com você à mesa e ajuda a decidir.</div></div>
        <div class="cmp-row" role="row"><div role="rowheader">Por quanto tempo</div><div role="cell">Encerra o trabalho com a entrega.</div><div role="cell">Acompanha ao longo do tempo, com encontros a cada três meses.</div></div>
        <div class="cmp-row" role="row"><div role="rowheader">Quem decide</div><div role="cell">Recomenda o caminho.</div><div role="cell">Você. O conselheiro amplia o que você enxerga antes de cada decisão.</div></div>
      </div>
      <p class="pull">Não chegamos com um destino pronto. O futuro da sua empresa é desenhado à mesa, com você.</p>
    </div>
  </div>
</section>

<!-- COBRANÇA -->
<section class="sec ivory">
  <div class="wrap duo">
    <div class="rv">
      <span class="eyebrow">Como cobramos</span>
      <h2 class="h2 rv-h">Um modelo <em class="o">simples e transparente.</em></h2>
      <div class="prose"><p>O trabalho é remunerado por uma mensalidade fixa e, nas operações de captação e venda, por uma comissão abaixo da média do mercado. Os valores são apresentados na conversa inicial, antes de qualquer compromisso.</p></div>
      <div class="price">
        <div><small>Aconselhamento</small><b>Mensalidade fixa</b><p>O retainer cobre a estruturação e os encontros do conselho.</p></div>
        <div><small>Operações</small><b>Comissão abaixo do mercado</b><p>Só quando há captação, venda ou associação.</p></div>
      </div>
    </div>
    <div class="rv" style="--d:.1s">
      <div class="expect">
        <div class="tile"><div class="ic">{I('calendar')}</div><h3>Primeiro passo: uma conversa</h3><p>30 minutos com um conselheiro sênior. É o primeiro passo do diagnóstico, e o investimento é informado antes da confirmação.</p></div>
        <div class="tile"><div class="ic">{g['icon']('shield')}</div><h3>Sem destino pronto</h3><p>Vender ou captar são opções. Ninguém é levado a uma operação que não quer fazer.</p></div>
      </div>
    </div>
  </div>
</section>
''' + g['close_block']('Respeitamos a sua trajetória, honramos o seu presente e <em class="o">construímos com você o seu amanhã.</em>')


def jornada_equity(g):
    I, H = g['icon'], g['phero']
    side = f'''<aside class="hside hl" style="--d:.9s"><span class="k">O que está incluído</span><ul>
      <li>{g['icon']('book')}E-book Bússola do Equity</li>
      <li>{g['icon']('quiz')}Diagnóstico estratégico do seu momento</li>
      <li>{g['icon']('video')}Sessão de 30 minutos com a liderança da Spinfy.co</li></ul></aside>'''
    hero = H('Jornada Equity', 'Sua experiência pode <em class="o">valer muito mais.</em>',
             'A porta de entrada para executivos, advisors e conselheiros que querem colocar a própria trajetória a serviço de empresas médias.',
             vid(7593574), poster(7593574, 'accounting-administration-adult-airplane'), 'Jornada Equity',
             ctas=f'<a class="btn" data-hero-cta href="#comecar">Quero descobrir meu potencial {I("arrow")}</a>', side=side)
    pil = [('layers', 'Governança', 'Conselhos, papéis e rituais que fazem a empresa decidir melhor.'),
           ('brief', 'Estrutura', 'Organização da empresa para crescer sem depender do dono.'),
           ('cpu', 'Inteligência artificial', 'A plataforma com IA que apoia cada análise do conselho.'),
           ('chartbar', 'Indicadores', 'Os números que mostram para onde a empresa está indo.'),
           ('shield', 'Compliance', 'Regras, controles e riscos sob acompanhamento.'),
           ('archive', 'Memória organizacional', 'O conhecimento da empresa registrado e preservado.'),
           ('gem', 'Valor patrimonial', 'O que faz a empresa valer mais numa captação ou venda.')]
    tiles = ''.join(f'<div class="tile"><span class="n">0{i+1}</span><div class="ic">{I(a)}</div><h3>{b}</h3><p>{c}</p></div>' for i, (a, b, c) in enumerate(pil))
    return hero + f'''
<!-- PARA QUEM -->
<section class="sec">
  <div class="wrap duo">
    <div class="img rv-img"><img src="{img('photo-1714974528348-de4b304b5011',1100)}" alt="Dois profissionais experientes conversando à mesa" loading="lazy"><div class="cap2">{I('users')}Para quem já viveu os desafios de uma empresa.</div></div>
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">Para quem é</span>
      <h2 class="h2 rv-h">Para quem tem <em class="o">bagagem</em> e quer usá-la melhor.</h2>
      <div class="prose"><p>A Jornada Equity foi pensada para profissionais que já ajudam empresas a crescer, ou querem começar a ajudar, e buscam método, rede e apoio para atuar como conselheiros.</p></div>
      <ul class="ticks">
        <li>{I('checkcircle')}Executivos e empresários com experiência sólida.</li>
        <li>{I('checkcircle')}Advisors e conselheiros que já atendem empresas.</li>
        <li>{I('checkcircle')}Profissionais de finanças, contabilidade e jurídico.</li>
      </ul>
    </div>
  </div>
</section>

<!-- 7 PILARES -->
<section class="sec ivory">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Os 7 pilares</span><h2 class="h2 rv-h">O que sustenta o <em class="o">valor de uma empresa.</em></h2></div>
      <p class="lead rv" style="--d:.1s">A jornada percorre os pilares que o conselho acompanha em cada empresa da rede Spinfy.co.</p>
    </div>
    <div class="cards4 stg">{tiles}
      <div class="tile" style="background:var(--navy)"><div class="ic" style="background:var(--orange);color:var(--ink)">{I('compass')}</div><h3 style="color:#fff">Bússola do Equity</h3><p style="color:rgba(255,255,255,.75)">O e-book que explica cada pilar e cada etapa do Sistema 7SS.</p></div>
    </div>
  </div>
</section>

<!-- O QUE INCLUI -->
<section class="sec" id="comecar">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Como funciona</span><h2 class="h2 rv-h">Três passos para <em class="o">descobrir o seu potencial.</em></h2></div>
      <p class="lead rv" style="--d:.1s">Em poucos dias você entende onde a sua experiência gera mais valor e qual é o próximo passo na rede.</p>
    </div>
    <div class="cards3 stg">
      <div class="tile"><span class="n">01</span><div class="ic">{I('book')}</div><h3>Leia a Bússola do Equity</h3><p>O e-book apresenta o Sistema 7SS e os pilares de valor de uma empresa média.</p></div>
      <div class="tile"><span class="n">02</span><div class="ic">{I('quiz')}</div><h3>Faça o diagnóstico</h3><p>Um diagnóstico estratégico mostra o seu momento e onde a sua experiência pesa mais.</p></div>
      <div class="tile"><span class="n">03</span><div class="ic">{I('video')}</div><h3>Converse com a liderança</h3><p>Uma sessão de 30 minutos com a liderança da Spinfy.co para definir o próximo passo.</p></div>
    </div>
    <div class="strip rv" style="margin-top:40px">
      <div class="mark" data-spin>{g['CTX']['mark']}</div>
      <p>Sua trajetória pode <em>ajudar outras empresas</em> a decidir melhor.</p>
      <a class="btn" href="#">Quero descobrir meu potencial {I('arrow')}</a>
    </div>
    <span class="todo-in">[Destino do botão a definir com o Marcelo: LP atual da Jornada Equity ou cadastro na plataforma.]</span>
  </div>
</section>

<!-- DEPOIMENTOS -->
<section class="sec ivory">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Quem já fez</span><h2 class="h2 rv-h">O que dizem <em class="o">os participantes.</em></h2></div>
      <p class="lead rv" style="--d:.1s">Depoimentos de quem passou pela Jornada Equity.</p>
    </div>
    <div class="quotes stg">
      <div class="qcard">{I('quote')}<p>[Depoimento a confirmar e autorizar.]</p><div class="who2"><i></i><div><b>Alessandro Augusto</b><span>Participante da Jornada Equity</span></div></div></div>
      <div class="qcard">{I('quote')}<p>[Depoimento a confirmar e autorizar.]</p><div class="who2"><i></i><div><b>Ricardo G. Anders</b><span>Participante da Jornada Equity</span></div></div></div>
      <div class="qcard">{I('quote')}<p>[Depoimento a confirmar e autorizar.]</p><div class="who2"><i></i><div><b>Angélica de Fátima</b><span>Participante da Jornada Equity</span></div></div></div>
    </div>
  </div>
</section>
''' + g['close_block']('Quer atuar como conselheiro? <em class="o">Conheça a rede Spinfy.co.</em>', eyebrow='Próximo passo',
                       btn=f'<a class="btn" href="seja-conselheiro.html">Seja um conselheiro {I("arrow")}</a>',
                       note='Se você é empresário e quer conselho para a sua empresa, o caminho é a página Para empresários.')


def casos(g):
    I, H = g['icon'], g['phero']
    side = f'''<aside class="hside hl" style="--d:.9s"><span class="k">Em números</span>
      <div class="big"><b>240</b><span>empresários aconselhados</span></div>
      <div class="big"><b>57</b><span>intermediações de captação e M&amp;A</span></div>
      <div class="big"><b>R$ 310 mi</b><span>transacionados</span></div></aside>'''
    hero = H('Casos de sucesso', 'Empresas que <em class="o">passaram pela mesa.</em>',
             'Os nomes ficam em sigilo. Os resultados são reais.', vid(7552425), poster(7552425), 'Casos de sucesso',
             ctas=g['CTX']['call_hero'], side=side)
    return hero + f'''
<!-- NÚMEROS -->
<section class="sec" style="padding-bottom:0">
  <div class="wrap">
    <div class="stats stg">
      <div class="stat"><b>240</b><span>empresários aconselhados</span></div>
      <div class="stat"><b>57</b><span>intermediações de captação e M&amp;A</span></div>
      <div class="stat"><b>310<small>mi</small></b><span>em reais transacionados</span></div>
      <div class="stat"><b>18<small>anos</small></b><span>estruturando estratégias de sucesso</span></div>
    </div>
  </div>
</section>

<!-- CASOS -->
<section class="sec">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Histórias reais</span><h2 class="h2 rv-h">Cada empresa chega com <em class="o">uma pergunta diferente.</em></h2></div>
      <p class="lead rv" style="--d:.1s">Dois exemplos de como o conselho muda a conversa dentro de empresas familiares.</p>
    </div>
    <article class="cased rv">
      <div class="im"><img src="{img('photo-1714974528737-3e6c7e4d11af')}" alt="Sócios de uma empresa familiar reunidos" loading="lazy"><span class="sector">{I('factory')}Indústria de produtos para construção</span></div>
      <div class="bd">
        <span class="eyebrow">Caso 01</span>
        <h3>Da segunda para a terceira geração, com o conselho no meio.</h3>
        <div class="facts"><span>R$ 200 milhões por ano</span><span>2ª para 3ª geração</span><span>Empresa familiar</span></div>
        <dl>
          <div><dt>A situação</dt><dd>A empresa estava na passagem da segunda para a terceira geração, com decisões concentradas e pouco espaço para a estratégia.</dd></div>
          <div><dt>O que foi feito</dt><dd>Dois sócios foram levados ao conselho, e as decisões passaram a ser tomadas com dados e em encontros regulares.</dd></div>
        </dl>
        <div class="res"><b>+14%</b><p>de lucro operacional (EBITDA) no primeiro ano.</p></div>
      </div>
    </article>
    <article class="cased rev rv">
      <div class="im"><img src="{img('photo-1714974528757-f63c72154a1b')}" alt="Família empresária conversando à mesa" loading="lazy"><span class="sector">{I('tree')}Madeireira de compensados</span></div>
      <div class="bd">
        <span class="eyebrow">Caso 02</span>
        <h3>Quando a família decide seguir caminhos diferentes.</h3>
        <div class="facts"><span>17 familiares na sociedade</span><span>3ª geração</span></div>
        <dl>
          <div><dt>A situação</dt><dd>A terceira geração não tinha interesse em seguir no negócio, e 17 familiares precisavam chegar a um acordo.</dd></div>
          <div><dt>O que foi feito</dt><dd>O conselho organizou a conversa entre os sócios e conduziu a saída de forma estruturada.</dd></div>
        </dl>
        <div class="res"><p class="q">O conselho virou a ponte para a saída dos sócios.</p></div>
      </div>
    </article>
  </div>
</section>

<!-- DEPOIMENTOS -->
<section class="sec ivory">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Depoimentos</span><h2 class="h2 rv-h">Na palavra de <em class="o">quem sentou à mesa.</em></h2></div>
      <p class="lead rv" style="--d:.1s">Este espaço recebe depoimentos de empresários com nome e foto, assim que forem autorizados.</p>
    </div>
    <div class="quotes stg">
      <div class="qcard">{I('quote')}<p>[Depoimento de empresário a receber.]</p><div class="who2"><i></i><div><b>Nome do empresário</b><span>Cargo e setor</span></div></div></div>
      <div class="qcard">{I('quote')}<p>[Depoimento de empresário a receber.]</p><div class="who2"><i></i><div><b>Nome do empresário</b><span>Cargo e setor</span></div></div></div>
      <div class="qcard">{I('quote')}<p>[Depoimento de empresário a receber.]</p><div class="who2"><i></i><div><b>Nome do empresário</b><span>Cargo e setor</span></div></div></div>
    </div>
  </div>
</section>
''' + g['close_block']('A próxima história pode ser <em class="o">a da sua empresa.</em>', eyebrow='Quero um resultado assim',
                       btn=g['callbtn']('Quero um resultado assim'))


def quem_somos(g):
    I, H = g['icon'], g['phero']
    hero = H('Quem somos', 'Construímos as mesas onde <em class="o">empresários decidem.</em>',
             'Ao lado de conselheiros que já viveram seus desafios, para valorizar o negócio e conquistar novas opções.',
             vid(8426041), poster(8426041), 'Quem somos', ctas=g['CTX']['call_hero'])
    vals = [('Ambição Estratégica', 'Pensar a empresa no horizonte de anos, e não da próxima urgência.'),
            ('Mentalidade de Equity', 'Cada decisão olha para o valor que a empresa constrói.'),
            ('Eficácia nos Contratos', 'Acordos claros, cumpridos e acompanhados.'),
            ('Excelência Técnica', 'O Sistema 7SS como base de cada análise.'),
            ('Resultados Práticos', 'Conselho que vira decisão e decisão que vira resultado.'),
            ('Rede de Confiança', 'Conselheiros com reputação e resultados próprios.'),
            ('Companhia Estratégica', 'Ninguém precisa decidir sozinho.')]
    vt = ''.join(f'<div class="value"><span class="n">0{i+1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(vals))
    vt += f'<div class="value dk"><span class="n">7SS</span><b>A empresa gira e todos ganham.</b><span>Company Spins, Everyone Wins.</span></div>'
    return hero + f'''
<!-- MANIFESTO -->
<section class="band" aria-label="Manifesto">
  <video autoplay muted loop playsinline preload="metadata" poster="{poster(7552616)}"><source src="{vid(7552616)}" type="video/mp4"></video>
  <div class="wrap rv">
    <div class="manifesto">
      {I('quote', 'q')}
      <p>Todo empresário vive o dia a dia do seu negócio. Poucos têm com quem pensar o futuro.</p>
      <p>Décadas de trabalho merecem mais do que a próxima urgência.</p>
      <p>Nossas mesas reúnem conselheiros, método próprio e inteligência artificial imparcial. <em>Não chegamos com um destino pronto.</em></p>
      <p>Respeitamos a sua trajetória, honramos o seu presente e construímos com você o seu amanhã.</p>
      <cite>A Mesa do Empresário · Manifesto Spinfy.co</cite>
      <span class="todo-in" style="margin-top:26px">[Versão resumida com as frases oficiais. Conferir com o texto completo do manifesto.]</span>
    </div>
  </div>
</section>

<!-- MARCELO -->
<section class="sec guide">
  <div class="wrap guide-in">
    <div class="portrait rv-l">
      <div class="ph"><img src="img/marcelo-fonzaghi.jpg" alt="Marcelo Fonzaghi, CEO da Spinfy.co, em seu escritório" width="628" height="640"><div class="cap"><b>Marcelo Fonzaghi</b><span>CEO da Spinfy.co</span></div></div>
    </div>
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">Quem conduz</span>
      <h2 class="h2 rv-h">Há 18 anos <em class="o">estruturando estratégias de sucesso.</em></h2>
      <div class="sign"><span class="bar"></span><div><b>Marcelo Fonzaghi</b><span>CEO da Spinfy.co</span></div></div>
      <p class="todo">[Bio do Marcelo, com trajetória, aparições e associações. Texto a receber.]</p>
      <div class="pillars stg">
        <div>{I('books')}<b>Conhecimento</b></div>
        <div>{I('target')}<b>Assertividade</b></div>
        <div>{I('bulb')}<b>Sabedoria</b></div>
      </div>
    </div>
  </div>
</section>

<!-- MISSÃO E VISÃO -->
<section class="sec">
  <div class="wrap">
    <div class="mvv stg">
      <div><small>Missão</small><p>Construímos as mesas onde empresários de médias empresas decidem ao lado de conselheiros que já viveram seus desafios, valorizam o seu negócio e conquistam novas opções, inclusive a de se tornar conselheiro também.</p></div>
      <div><small>Visão</small><p>Até 2032, ser a maior plataforma de conselho e transações para empresas médias do Brasil, onde empresários pensam o futuro, valorizam suas empresas e passam a ter mais opções.</p>
        <div class="goal"><b>17</b><span>empresas valendo R$ 1 bilhão ou mais até 2032</span></div></div>
    </div>
  </div>
</section>

<!-- VALORES -->
<section class="sec ivory">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Nossos valores</span><h2 class="h2 rv-h">Sete valores, <em class="o">uma forma de sentar à mesa.</em></h2></div>
      <p class="lead rv" style="--d:.1s">É o que esperamos de cada conselheiro e o que cada empresário pode cobrar de nós.</p>
    </div>
    <div class="values stg">{vt}</div>
  </div>
</section>

<!-- HISTÓRIA -->
<section class="sec">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Nossa trajetória</span><h2 class="h2 rv-h">Uma rede construída <em class="o">mesa a mesa.</em></h2></div>
      <p class="lead rv" style="--d:.1s">Atendimento presencial em Curitiba, online em todo o Brasil e na empresa do cliente, quando necessário.</p>
    </div>
    <div class="timeline stg">
      <div class="tl"><b>18 anos</b><p>de experiência de Marcelo Fonzaghi estruturando estratégias de empresas.</p></div>
      <div class="tl"><b>2015</b><p>Nasce a Spinfy.co, em Curitiba, com foco em empresas médias.</p></div>
      <div class="tl"><b>240</b><p>empresários aconselhados e 57 intermediações de captação e M&amp;A.</p></div>
      <div class="tl"><b>2032</b><p>A meta: 17 empresas da rede valendo R$ 1 bilhão ou mais.</p></div>
    </div>
  </div>
</section>

<!-- REDE -->
<section class="sec" id="conselheiros" style="padding-top:0">
  <div class="wrap">
    <div class="adv rv-s">
      <div class="tx">
        <span class="eyebrow lt">A rede de conselheiros</span>
        <h2 class="h2 rv-h">Conselheiros que <em class="o">já sentaram na sua cadeira.</em></h2>
        <ul>
          <li>{I('brief')}Empresários e executivos com resultados pessoais sólidos</li>
          <li>{I('scales')}Profissionais de finanças, contabilidade e jurídico</li>
          <li>{I('grad')}Formados no Sistema 7SS, em duas partes: Start e Método</li>
        </ul>
        <div class="ctas"><a class="btn" href="seja-conselheiro.html">Seja um conselheiro {I('arrow')}</a></div>
        <p class="motto">A empresa gira e todos ganham.</p>
      </div>
      <div class="im"><img src="{img('photo-1685375421073-4dae366f8e84',1000)}" alt="Empresário experiente, sorridente, sentado em uma poltrona no escritório" loading="lazy" style="object-position:50% 22%"></div>
    </div>
  </div>
</section>
''' + g['close_block']('Respeitamos a sua trajetória, honramos o seu presente e <em class="o">construímos com você o seu amanhã.</em>')


def seja_conselheiro(g):
    I, H = g['icon'], g['phero']
    hero = H('Seja um conselheiro', 'Sua experiência pode <em class="o">ajudar outras empresas.</em>',
             'Entre para a rede de conselheiros da Spinfy.co, os Spinners, e aconselhe empresários de médias empresas com método e plataforma próprios.',
             vid(8123986, 30), poster(8123986, 'adult-age-aging-aging-active'), 'Seja um conselheiro',
             ctas=f'<a class="btn" data-hero-cta href="#entrar">Quero ser um Spinner {I("arrow")}</a><a class="tlink" href="jornada-equity.html" style="color:#fff">Conheça a Jornada Equity <span class="c">{I("arrow")}</span></a>')
    return hero + f'''
<!-- PARA QUEM -->
<section class="sec">
  <div class="wrap duo">
    <div class="rv">
      <span class="eyebrow">Para quem é</span>
      <h2 class="h2 rv-h">Para quem já <em class="o">construiu resultados</em> e quer multiplicá-los.</h2>
      <div class="prose"><p>Os Spinners são empresários, executivos e profissionais técnicos que levam a própria experiência para a mesa de outras empresas. A entrada na rede não tem taxa nem comissão.</p></div>
      <ul class="ticks">
        <li>{I('checkcircle')}Executivos e empresários com experiência sólida.</li>
        <li>{I('checkcircle')}Empresários de sucesso no seu segmento, aconselhando outras empresas.</li>
        <li>{I('checkcircle')}Profissionais de finanças, contabilidade e jurídico.</li>
        <li>{I('checkcircle')}Conselheiros que já atendem empresas.</li>
      </ul>
    </div>
    <div class="img rv-img"><img src="{img('photo-1685375421073-4dae366f8e84',1000)}" alt="Empresário experiente, sorridente, sentado em uma poltrona no escritório" loading="lazy" style="object-position:50% 25%"><div class="cap2">{I('users')}A empresa gira e todos ganham.</div></div>
  </div>
</section>

<!-- O QUE FAZ -->
<section class="sec ivory">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">O que o Spinner faz</span><h2 class="h2 rv-h">À mesa, <em class="o">ao lado do empresário.</em></h2></div>
      <p class="lead rv" style="--d:.1s">O conselheiro não executa pelo empresário. Ele amplia o que o empresário enxerga antes de cada decisão.</p>
    </div>
    <div class="cards3 stg">
      <div class="tile"><span class="n">01</span><div class="ic">{I('chair')}</div><h3>Aconselha</h3><p>Participa dos encontros do conselho, a cada três meses, com o apoio do Board Pack.</p></div>
      <div class="tile"><span class="n">02</span><div class="ic">{I('coins')}</div><h3>Estrutura captações</h3><p>Ajuda a preparar a empresa para buscar capital com investidores.</p></div>
      <div class="tile"><span class="n">03</span><div class="ic">{I('handshake')}</div><h3>Intermedeia operações</h3><p>Apoia fusões, aquisições e a entrada de novos sócios.</p></div>
    </div>
  </div>
</section>

<!-- FORMAÇÃO E REDE -->
<section class="sec navyb" style="position:relative;overflow:hidden;isolation:isolate">
  <div class="mark" data-spin style="right:-160px;bottom:-200px;width:560px">{g['CTX']['mark']}</div>
  <div class="wrap duo">
    <div class="rv">
      <span class="eyebrow">Formação</span>
      <div class="sys-logo" role="img" aria-label="Sistema 7SS"><span class="tx"><span class="s1">Sistema</span><span class="s2">7<i>SS</i></span></span></div>
      <h2 class="h2 rv-h" style="font-size:clamp(30px,3.2vw,44px)">Formação em duas partes, <em class="o">com prática.</em></h2>
      <div class="prose"><p>Todo Spinner é formado no Sistema 7SS, o método que dá nome à Spinfy.co, com acompanhamento prático nas primeiras mesas.</p></div>
      <div class="price" style="margin-top:30px">
        <div style="background:rgba(255,255,255,.06)"><small style="color:var(--orange)">Parte 1</small><b style="color:#fff">Start</b><p style="color:rgba(255,255,255,.72)">Os fundamentos do conselho e das sete etapas do método.</p></div>
        <div style="background:var(--orange);color:var(--ink)"><small style="color:var(--ink)">Parte 2</small><b>Método</b><p style="color:rgba(23,19,58,.8)">A aplicação do Sistema 7SS em empresas reais.</p></div>
      </div>
    </div>
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">O que a rede oferece</span>
      <ul class="ticks" style="margin-top:22px">
        <li>{I('check')}Estrutura física em Curitiba e estrutura digital.</li>
        <li>{I('check')}Plataforma com inteligência artificial para cada etapa do 7SS.</li>
        <li>{I('check')}Acesso a empresários e investidores da rede.</li>
        <li>{I('check')}Acompanhamento da liderança da Spinfy.co.</li>
      </ul>
    </div>
  </div>
</section>

<!-- COMO ENTRAR -->
<section class="sec" id="entrar">
  <div class="wrap">
    <div class="shead">
      <div class="rv"><span class="eyebrow">Como entrar</span><h2 class="h2 rv-h">Quatro passos até <em class="o">a sua primeira mesa.</em></h2></div>
      <p class="lead rv" style="--d:.1s">Sem taxa de entrada e sem comissão para fazer parte da rede.</p>
    </div>
    <div class="timeline stg">
      <div class="tl"><b>Cadastro</b><p>Você conta a sua trajetória e a sua área de experiência.</p></div>
      <div class="tl"><b>Formação</b><p>Start e Método, no Sistema 7SS.</p></div>
      <div class="tl"><b>Associação</b><p>A entrada formal na rede de Spinners.</p></div>
      <div class="tl"><b>Atuação</b><p>As primeiras mesas, com acompanhamento.</p></div>
    </div>
    <div class="strip rv" style="margin-top:56px">
      <div class="mark" data-spin>{g['CTX']['mark']}</div>
      <p>A empresa gira e <em>todos ganham.</em></p>
      <a class="btn" href="{g['WA']}" target="_blank" rel="noopener">Quero ser um Spinner {I('arrow')}</a>
    </div>
  </div>
</section>

<!-- DEPOIMENTO E VISÃO -->
<section class="sec ivory">
  <div class="wrap duo">
    <div class="qcard rv" style="background:var(--white)">{I('quote')}<p>[Depoimento de um Spinner associado a receber.]</p><div class="who2"><i></i><div><b>Nome do conselheiro</b><span>Spinner da rede Spinfy.co</span></div></div></div>
    <div class="rv" style="--d:.1s">
      <span class="eyebrow">Para onde vamos</span>
      <h2 class="h2 rv-h">17 empresas valendo <em class="o">R$ 1 bilhão</em> até 2032.</h2>
      <div class="prose"><p>A visão da Spinfy.co é ser a maior plataforma de conselho e transações para empresas médias do Brasil. Os Spinners são parte central desse caminho.</p></div>
    </div>
  </div>
</section>
''' + g['close_block']('Pronto para levar a sua experiência <em class="o">a outras mesas?</em>', eyebrow='Quero ser um Spinner',
                       btn=f'<a class="btn" href="{g["WA"]}" target="_blank" rel="noopener">Quero ser um Spinner {I("arrow")}</a>',
                       note='Prefere conhecer antes? Comece pela Jornada Equity.')


def faq(g):
    I, H = g['icon'], g['phero']
    hero = H('Perguntas frequentes', 'O que você precisa saber <em class="o">antes da conversa.</em>',
             'Respostas diretas sobre o conselho, os prazos, a cobrança e o sigilo. Fáceis de encaminhar para sócios, filhos, advogado e contador.',
             vid(8847933), poster(8847933), 'Perguntas frequentes', ctas=g['CTX']['call_hero'])
    def q(t, a, open_=False):
        return f'<details{" open" if open_ else ""}><summary>{t}<span class="pm">{g["icon"]("plus")}</span></summary><div class="ans">{a}</div></details>'
    groups = [
        ('conselho', 'chair', 'Sobre o conselho', [
            q('Qual é a diferença entre um conselheiro e um consultor?', '<p>O consultor faz um diagnóstico, entrega um relatório e encerra o trabalho. O conselheiro acompanha você ao longo do tempo, senta à mesa a cada três meses e ajuda a decidir.</p><p>Ele não executa e não decide por você. Amplia o que você enxerga antes de cada decisão.</p>', True),
            q('Para que tipo de empresa a Spinfy.co é indicada?', '<p>Para empresas médias conduzidas pelo fundador ou em passagem entre gerações. A maioria dos nossos clientes fatura entre R$ 30 e 100 milhões por ano.</p>'),
            q('Quem são os conselheiros?', '<p>Empresários e executivos com resultados pessoais sólidos e reputação ilibada, formados no Sistema 7SS. À frente está Marcelo Fonzaghi, há 18 anos estruturando estratégias de sucesso.</p>'),
            q('Meus sócios e meus filhos participam?', '<p>Sim. Muitas das empresas que atendemos são familiares e estão na passagem entre gerações. Envolver sócios e sucessores faz parte do processo. <span class="tbc">a confirmar</span></p>'),
        ]),
        ('jornada', 'clock', 'Sobre a jornada', [
            q('Como começa o trabalho?', '<p>Com uma conversa de 30 minutos com um conselheiro sênior. Ela é o primeiro passo do diagnóstico, e o investimento é informado antes da confirmação.</p><p>Depois vem o pré-diagnóstico, feito a partir do cadastro da empresa na plataforma, em cerca de 10 dias.</p>'),
            q('Quanto tempo leva?', '<p>A estruturação estratégica leva 90 dias. Em seguida vêm 9 meses de aconselhamento, com encontros a cada três meses e um relatório do conselho (Board Pack) desde o início.</p>'),
            q('O que significa "Conselheiro em 9 meses"?', '<p>Ao fim dos 9 meses, você pode delegar o papel executivo e ocupar a cadeira do conselho da sua própria empresa, com mais tempo para a estratégia. Se quiser, também pode aconselhar outras empresas.</p>'),
            q('Preciso vender a minha empresa?', '<p>Não. Vender, captar, trazer um sócio ou investir são opções, não obrigações. Não chegamos com um destino pronto: o futuro da sua empresa é desenhado à mesa, com você.</p>'),
        ]),
        ('metodo', 'ai', 'Sobre o método e a IA', [
            q('O que é o Sistema 7SS?', '<p>É o nosso método, com 7 etapas que formam o nome da marca: Situação, Posicionamento, Indicadores, Negligências, Forecast, Yield e Conselho aos objetivos. O e-book Bússola do Equity explica cada uma.</p><p><a class="tlink" href="para-empresarios.html#sistema-7ss">Veja as 7 etapas <span class="c">' + g['icon']('arrow') + '</span></a></p>'),
            q('Como a inteligência artificial participa?', '<p>Cada etapa do Sistema 7SS é analisada por um colegiado de IA inspirado nas maiores referências do mercado. Na etapa final, o Marcellus, nosso conselheiro de IA, cruza essas análises e sugere caminhos. A decisão é sempre sua, com os conselheiros.</p>'),
        ]),
        ('cobranca', 'shield', 'Cobrança, sigilo e atendimento', [
            q('Como vocês cobram?', '<p>Trabalhamos com uma mensalidade fixa (retainer) e comissão nas operações de captação e venda, abaixo da média do mercado. Os valores são apresentados na conversa inicial.</p>'),
            q('As informações da minha empresa ficam em sigilo?', '<p>Sim. Os nomes das empresas atendidas não são divulgados, e os casos do site são apresentados de forma anônima. <span class="tbc">a confirmar como é formalizado</span></p>'),
            q('Vocês atendem fora de Curitiba?', '<p>Sim. Atendemos presencialmente em Curitiba, online em todo o Brasil e com visitas à empresa quando necessário.</p>'),
        ]),
    ]
    tabs = ''.join(f'<li><a href="#{k}">{t}<span>{len(qs):02d}</span></a></li>' for k, ic, t, qs in groups)
    body = ''.join(f'<div class="fgroup" id="{k}"><h2>{g["icon"](ic)}{t}</h2><div class="faq">{"".join(qs)}</div></div>' for k, ic, t, qs in groups)
    return hero + f'''
<section class="sec">
  <div class="wrap faq-wrap">
    <aside class="faq-side rv">
      <span class="eyebrow">Temas</span>
      <h2 class="h2" style="font-size:clamp(30px,3vw,40px)">Escolha <em class="o">um tema.</em></h2>
      <ul class="tabs">{tabs}</ul>
      <div class="mapcard" style="margin-top:26px">
        <div class="mark" data-spin>{g['CTX']['mark']}</div>
        <small>Não achou a resposta?</small>
        <b>Fale com a nossa equipe pelo WhatsApp.</b>
        <a class="tlink" href="{g['WA']}" target="_blank" rel="noopener">Abrir WhatsApp <span class="c">{I('arrow')}</span></a>
      </div>
    </aside>
    <div class="rv" style="--d:.1s">{body}</div>
  </div>
</section>
''' + g['close_block']('A melhor resposta vem <em class="o">numa conversa.</em>')


def contato(g):
    I = g['icon']
    WA = g['WA']
    chans = [
        ('phone', 'Telefone', '(41) 3021-8343', 'Ligue em horário comercial.', 'tel:+554130218343', ''),
        ('whatsapp', 'WhatsApp', '(41) 9134-7696', 'Fale com a nossa equipe a qualquer momento.', WA, ' target="_blank" rel="noopener"'),
        ('mail', 'E-mail', 'service@spinfy.co', 'Para propostas, documentos e parcerias.', 'mailto:service@spinfy.co', ''),
        ('instagram', 'Instagram', '@spinfy.co', 'Acompanhe as novidades da Spinfy.co.', 'https://www.instagram.com/spinfy.co/', ' target="_blank" rel="noopener"'),
        ('linkedin', 'LinkedIn', 'Spinfy.co', 'Artigos e conteúdos para empresários.', 'https://www.linkedin.com/company/spinfy/', ' target="_blank" rel="noopener"'),
        ('lock', 'Plataforma', 'Acesso restrito', 'Área de clientes e conselheiros.', 'https://spinfy.app.br', ''),
    ]
    ch = ''.join(f'<a class="chan" href="{h}"{t}><span class="ic">{I(ic)}</span><span><small>{k}</small><b>{v}</b><em>{d}</em></span></a>' for ic, k, v, d, h, t in chans)
    return f'''
<section class="sec ctop">
  <div class="wrap">
    <nav class="crumb dk rv" aria-label="Você está em"><a href="index.html">Início</a><span>/</span><b>Contato</b></nav>
    <div class="shead">
      <div class="rv"><span class="eyebrow">Contato</span><h1 class="h2 rv-h" style="font-size:clamp(44px,5.4vw,76px)">Fale com <em class="o">a Spinfy.co.</em></h1></div>
      <p class="lead rv" style="--d:.1s">Escolha o canal que preferir. Atendimento presencial em Curitiba, online em todo o Brasil e na sua empresa.</p>
    </div>
    <div class="chans stg">{ch}</div>
  </div>
</section>

<section class="sec ivory" id="agendar">
  <div class="wrap book">
    <form class="form rv" id="mailForm" novalidate>
      <span class="eyebrow">Envie uma mensagem</span>
      <h2>Conte um pouco sobre a sua empresa.</h2>
      <p class="lead">A mensagem chega ao e-mail da nossa equipe, que responde em até um dia útil.</p>
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <div class="fg">
        <div class="field"><label for="f-nome">Seu nome</label><input id="f-nome" name="nome" autocomplete="name" required></div>
        <div class="field"><label for="f-empresa">Empresa</label><input id="f-empresa" name="empresa" autocomplete="organization"></div>
        <div class="field"><label for="f-email">E-mail</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-tel">Telefone ou WhatsApp</label><input id="f-tel" name="telefone" type="tel" autocomplete="tel" inputmode="tel"></div>
        <div class="field"><label for="f-ass">Assunto</label><select id="f-ass" name="assunto"><option>Agendar uma conversa</option><option>Quero ser um conselheiro</option><option>Jornada Equity</option><option>Imprensa e parcerias</option><option>Outro assunto</option></select></div>
        <div class="field"><label for="f-fat">Faturamento anual da empresa</label><select id="f-fat" name="faturamento"><option>Até R$ 30 milhões</option><option selected>De R$ 30 a 100 milhões</option><option>Acima de R$ 100 milhões</option><option>Prefiro não informar</option></select></div>
        <div class="field full"><label for="f-msg">Mensagem</label><textarea id="f-msg" name="mensagem" required placeholder="Conte o que você gostaria de conversar."></textarea></div>
      </div>
      <div class="send">
        <button class="btn" type="submit">Enviar mensagem {I('arrow')}</button>
        <p class="fine">Seus dados são usados apenas para responder ao seu contato.</p>
      </div>
      <p class="ok" role="status">Mensagem enviada. Em breve nossa equipe entra em contato.</p>
      <p class="err" role="alert">Não foi possível enviar agora. Escreva para service@spinfy.co ou ligue para (41) 3021-8343.</p>
    </form>
    <div class="expect rv" style="--d:.1s">
      <span class="eyebrow">Agende uma conversa</span>
      <div class="tile"><span class="n">01</span><div class="ic">{I('clock')}</div><h3>30 minutos</h3><p>Uma conversa com um conselheiro sênior sobre o momento da sua empresa.</p></div>
      <div class="tile"><span class="n">02</span><div class="ic">{I('shield')}</div><h3>Sem surpresas</h3><p>É o primeiro passo do diagnóstico, e o investimento é informado antes da confirmação.</p></div>
      <a class="btn" href="{WA}" target="_blank" rel="noopener" style="justify-content:center">{I('whatsapp')}Agendar pelo WhatsApp</a>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:clamp(64px,7vw,96px)">
  <div class="wrap visit">
    <div class="rv">
      <span class="eyebrow">Onde estamos</span>
      <h2 class="h2 rv-h">Rua Ébano Pereira, 60, <em class="o">21º andar.</em></h2>
      <div class="prose"><p>Centro, Curitiba/PR, CEP 80410-250. Recebemos empresários com hora marcada e também vamos até a sua empresa.</p></div>
      <a class="tlink" style="margin-top:28px" href="https://www.google.com/maps/search/?api=1&amp;query=Rua+%C3%89bano+Pereira+60+Curitiba" target="_blank" rel="noopener">Abrir no Google Maps <span class="c">{I('arrow')}</span></a>
    </div>
    <div class="map rv" style="--d:.1s"><iframe title="Mapa: Rua Ébano Pereira, 60, Curitiba" src="https://www.google.com/maps?q=Rua+%C3%89bano+Pereira,+60,+Centro,+Curitiba+PR&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
'''


PAGE = {'para-empresarios': para_empresarios, 'jornada-equity': jornada_equity, 'casos': casos, 'quem-somos': quem_somos,
        'seja-conselheiro': seja_conselheiro, 'perguntas-frequentes': faq, 'contato': contato}
