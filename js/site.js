document.documentElement.classList.add('js');
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var top=document.getElementById('top');
  var marks=[].slice.call(document.querySelectorAll('[data-spin]'));
  var pars=[].slice.call(document.querySelectorAll('[data-par]'));
  var ticking=false;
  var tt=document.getElementById('totop'),ring=tt.querySelector('circle');
  tt.addEventListener('click',function(){scrollTo({top:0,behavior:reduce?'auto':'smooth'});});
  function frame(){
    var y=scrollY,h=document.documentElement.scrollHeight-innerHeight;
    top.classList.toggle('solid',y>40);
    top.style.setProperty('--prog',(h>0?y/h*100:0)+'%');
    tt.classList.toggle('show',y>innerHeight*.6);ring.style.strokeDashoffset=(176*(1-(h>0?y/h:0))).toFixed(1);
    if(!reduce){
      marks.forEach(function(m){var r=m.getBoundingClientRect();if(r.bottom<-200||r.top>innerHeight+200)return;m.style.transform='rotate('+(y*0.04)+'deg)';});
      pars.forEach(function(el){var r=el.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var k=parseFloat(el.dataset.par)||.08;var p=(r.top+r.height/2-innerHeight/2);el.style.transform='translate3d(0,'+(p*-k)+'px,0) scale(1.08)';});
    }
    ticking=false;
  }
  addEventListener('scroll',function(){if(!ticking){requestAnimationFrame(frame);ticking=true;}},{passive:true});frame();

  var heroCta=document.querySelector('[data-hero-cta]'),mast=document.getElementById('top');
  function ctaCheck(){if(!heroCta)return;mast.classList.toggle('cta-hide',(function(r){return r.bottom>70&&r.top<innerHeight;})(heroCta.getBoundingClientRect()));}
  addEventListener('scroll',ctaCheck,{passive:true});addEventListener('resize',ctaCheck);ctaCheck();
  var b=document.getElementById('burger'),nav=document.getElementById('nav');
  b.addEventListener('click',function(){var o=nav.classList.toggle('open');b.setAttribute('aria-expanded',o);top.classList.add('solid');});
  var links=[].slice.call(nav.querySelectorAll('a[href^="#"]')).filter(function(a){return a.getAttribute('href').length>1;});
  var spy=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id);});}});},{rootMargin:'-45% 0px -50% 0px'});
  links.forEach(function(a){var t=document.querySelector(a.getAttribute('href'));if(t)spy.observe(t);});

  document.querySelectorAll('.stg').forEach(function(g){[].forEach.call(g.children,function(c,i){c.style.transitionDelay=(i*0.1)+'s';});});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.18,rootMargin:'0px 0px -60px 0px'});
  document.querySelectorAll('.rv,.rv-l,.rv-r,.rv-s,.rv-img,.stg').forEach(function(el){io.observe(el);});
  var ioh=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target._h.classList.add('in');ioh.unobserve(e.target);}});},{threshold:0,rootMargin:'0px 0px -80px 0px'});
  document.querySelectorAll('.rv-h').forEach(function(h){var p=h.parentNode;p._h=h;ioh.observe(p);});


  // Formulário de agendamento: monta a mensagem e abre o WhatsApp da Spinfy.co
  var form=document.getElementById('agendaForm');
  if(form){form.addEventListener('submit',function(ev){ev.preventDefault();
    var f=form.elements,miss=[].filter.call(form.querySelectorAll('[required]'),function(i){return !i.value.trim();});
    if(miss.length){miss[0].focus();miss.forEach(function(i){i.style.borderColor='#C2541A';});return;}
    var per=(form.querySelector('input[name=periodo]:checked')||{}).value||'';
    var t='Olá! Quero agendar uma conversa com a Spinfy.co.\n\nNome: '+f.nome.value+'\nEmpresa: '+f.empresa.value+'\nTelefone: '+f.telefone.value+'\nFaturamento: '+f.faturamento.value+'\nMelhor período: '+per+(f.mensagem.value.trim()?'\nAssunto: '+f.mensagem.value.trim():'');
    form.classList.add('sent');
    window.open('https://wa.me/554191347696?text='+encodeURIComponent(t),'_blank','noopener');
  });}
  var steps=[
    ['Situação','A situação econômica, financeira e operacional da empresa.'],
    ['Posicionamento','O posicionamento da empresa no mercado e as atitudes de quem a conduz.'],
    ['Indicadores','Os indicadores do negócio, organizados em painéis de acompanhamento (BI).'],
    ['Negligências','Os riscos e os pontos que estão sendo deixados de lado.'],
    ['Forecast','Os cenários financeiros para os próximos anos (FP&A).'],
    ['Yield','Como o resultado é distribuído e quanto é reinvestido.'],
    ['Conselho aos objetivos','O conselho cruza as análises anteriores e sugere os objetivos da empresa.']
  ];
  var btns=document.querySelectorAll('.letter'),T=document.getElementById('sysT'),D=document.getElementById('sysD');
  btns.forEach(function(x){x.addEventListener('click',function(){btns.forEach(function(y){y.setAttribute('aria-pressed','false');});x.setAttribute('aria-pressed','true');var s=steps[+x.dataset.i];T.textContent=s[0];D.textContent=s[1];});});
})();
