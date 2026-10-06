(() => {
  'use strict';
  const ready = (fn) => document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn, {once:true}) : fn();

  ready(() => {
    const body = document.body;
    const toggle = document.getElementById('mobileToggle');
    const menu = document.getElementById('mobileMenu');
    const header = document.getElementById('siteHeader');
    const reduceMotion = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false;

    const setMenu = (open) => {
      if (!toggle || !menu) return;
      toggle.classList.toggle('active', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      menu.classList.toggle('active', open);
      menu.setAttribute('aria-hidden', String(!open));
      menu.inert = !open;
      body.classList.toggle('menu-open', open);
    };
    if (toggle && menu) {
      setMenu(false);
      toggle.addEventListener('click', () => setMenu(!menu.classList.contains('active')));
      menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
      document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
      window.addEventListener('resize', () => { if (window.innerWidth > 1100) setMenu(false); }, {passive:true});
    }

    const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 8);
    updateHeader(); window.addEventListener('scroll', updateHeader, {passive:true});
    const year = document.getElementById('year'); if (year) year.textContent = String(new Date().getFullYear());

    const revealItems = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && !reduceMotion) {
      const observer = new IntersectionObserver((entries, obs) => entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('is-visible'); obs.unobserve(entry.target); } }), {threshold:.12, rootMargin:'0px 0px -30px'});
      revealItems.forEach(item => observer.observe(item));
    } else revealItems.forEach(item => item.classList.add('is-visible'));

    initHeroSlider(reduceMotion);
    initPortfolio();
    initForms(reduceMotion);
    initAnchors(reduceMotion);
    initChat(reduceMotion);
    init3DHero(reduceMotion);
  });

  function initHeroSlider(reduceMotion) {
    const heroImage = document.getElementById('heroImage');
    const slideLabel = document.getElementById('heroSlideLabel');
    const slideCount = document.getElementById('heroSlideCount');
    if (!heroImage) return;
    const slides = [
      {src:'images/hero-home0.webp', label:'Web experiences'},
      {src:'images/hero-home1.webp', label:'Creative websites'},
      {src:'images/hero-home2.webp', label:'Digital presence'},
      {src:'images/hero-home3.webp', label:'Responsive systems'},
      {src:'images/hero-home4.webp', label:'Growth-ready design'}
    ];
    let current=0, timer=null;
    const preloadNext=()=>{const i=new Image(); i.decoding='async'; i.src=slides[(current+1)%slides.length].src;};
    const swap=()=>{if(reduceMotion || document.hidden) return; heroImage.classList.add('changing'); window.setTimeout(()=>{current=(current+1)%slides.length; heroImage.src=slides[current].src; heroImage.srcset=`${slides[current].src} 1x`; if(slideLabel) slideLabel.textContent=slides[current].label; if(slideCount) slideCount.textContent=`${String(current+1).padStart(2,'0')} / ${String(slides.length).padStart(2,'0')}`; heroImage.classList.remove('changing'); preloadNext();},180);};
    const start=()=>{if(reduceMotion || timer) return; timer=window.setInterval(swap,5000);};
    const stop=()=>{if(timer){window.clearInterval(timer);timer=null;}};
    document.addEventListener('visibilitychange',()=>document.hidden?stop():start());
    heroImage.closest('.hero-image-frame')?.addEventListener('touchstart',()=>stop(),{passive:true});
    start(); preloadNext();
  }

  function initPortfolio() {
    const grid=document.querySelector('.portfolio-project-grid'); if(!grid) return;
    const cards=[...grid.querySelectorAll('.project-card')];
    const buttons=[...document.querySelectorAll('.filter-btn')]; const count=document.getElementById('workCount'); const empty=document.getElementById('emptyWork'); const more=document.getElementById('loadMoreWork');
    const pageSize=12; let filter='all'; let shown=pageSize;
    const matches=(card,f)=>{if(f==='all') return true; const cats=(card.dataset.categories||'').toLowerCase().split('|'); if(f==='cafe') return cats.some(c=>['cafe','restaurant','hotel'].includes(c)); if(f==='3d / interactive') return cats.some(c=>['3d / interactive','interactive'].includes(c)); return cats.includes(f.toLowerCase());};
    const render=()=>{const matched=cards.filter(c=>matches(c,filter)); cards.forEach(c=>c.classList.add('is-hidden')); matched.slice(0,shown).forEach(c=>c.classList.remove('is-hidden')); if(count) count.textContent=`Showing ${Math.min(shown,matched.length)} of ${matched.length} project${matched.length===1?'':'s'}`; if(empty) empty.hidden=matched.length!==0; if(more){more.hidden=matched.length<=shown; more.disabled=matched.length<=shown; more.innerHTML=matched.length>shown?`Load ${Math.min(pageSize,matched.length-shown)} more <span aria-hidden="true">↓</span>`:'All work loaded';}};
    buttons.forEach(btn=>btn.addEventListener('click',()=>{buttons.forEach(b=>{b.classList.remove('active');b.setAttribute('aria-selected','false');});btn.classList.add('active');btn.setAttribute('aria-selected','true');filter=btn.dataset.filter||'all';shown=pageSize;render();}));
    grid.querySelectorAll('img[data-preview]').forEach(img=>{img.addEventListener('error',()=>{img.closest('.project-media')?.classList.add('preview-failed');},{once:true});});
    more?.addEventListener('click',()=>{shown+=pageSize;render();}); render();
  }

  async function initForms(reduceMotion) {
    document.querySelectorAll('form.site-form').forEach(form=>{
      const started=form.querySelector('input[name="startedAt"]'); if(started) started.value=String(Date.now());
      form.addEventListener('submit', async event=>{
        event.preventDefault();
        if(!form.reportValidity()) return;
        const status=form.querySelector('.form-status'); const button=form.querySelector('button[type="submit"]');
        const file=form.querySelector('input[type="file"]')?.files?.[0];
        if(file && file.size>3*1024*1024){if(status) status.textContent='Please keep the resume at 3 MB or less.'; return;}
        if(status) {status.className='form-status';status.textContent='Sending…';}
        if(button){button.disabled=true;button.setAttribute('aria-busy','true');}
        try{
          const fd=new FormData(form); const payload={};
          for(const [k,v] of fd.entries()){if(k==='resume') continue; payload[k]=v;}
          if(file){payload.resumeName=file.name;payload.resumeType=file.type||'application/octet-stream';payload.resumeBase64=await fileToDataUrl(file);}
          const response=await fetch(form.getAttribute('action')||'/api/submit',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(payload)});
          const data=await response.json().catch(()=>({}));
          if(!response.ok) throw new Error(data.message||'Unable to send right now.');
          if(status){status.className='form-status success';status.textContent=data.message||'Submitted successfully.';}
          form.reset(); if(started) started.value=String(Date.now());
        }catch(error){if(status){status.className='form-status error';status.textContent=error.message||'Something went wrong. Please use WhatsApp or email instead.';}}
        finally{if(button){button.disabled=false;button.removeAttribute('aria-busy');}}
      });
    });
  }
  function fileToDataUrl(file){return new Promise((resolve,reject)=>{const r=new FileReader();r.onload=()=>resolve(r.result);r.onerror=reject;r.readAsDataURL(file);});}

  function initAnchors(reduceMotion){document.querySelectorAll('a[href^="#"]').forEach(anchor=>anchor.addEventListener('click',event=>{const id=anchor.getAttribute('href');if(!id||id==='#')return;const target=document.querySelector(id);if(!target)return;event.preventDefault();target.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});}));}
  function initChat(reduceMotion){const bubble=document.getElementById('chatBubble');if(!bubble||reduceMotion)return;window.setTimeout(()=>bubble.classList.add('show'),1800);window.setTimeout(()=>bubble.classList.remove('show'),8500);}

  function init3DHero(reduceMotion){
    const canvas=document.getElementById('webora3D'); if(!canvas || reduceMotion) return;
    const ctx=canvas.getContext('2d',{alpha:true}); if(!ctx) return;
    const host=canvas.closest('.hero-3d-wrap'); if(!host) return;
    let width=0,height=0,dpr=1,raf=0,visible=true,points=[],mouse={x:0,y:0,active:false};
    const resize=()=>{const rect=host.getBoundingClientRect();dpr=Math.min(window.devicePixelRatio||1,2);width=Math.max(1,Math.floor(rect.width));height=Math.max(1,Math.floor(rect.height));canvas.width=Math.floor(width*dpr);canvas.height=Math.floor(height*dpr);canvas.style.width=width+'px';canvas.style.height=height+'px';ctx.setTransform(dpr,0,0,dpr,0,0);const count=width<700?34:64;points=Array.from({length:count},(_,i)=>({a:Math.random()*Math.PI*2,b:Math.acos(2*Math.random()-1),r:.38+Math.random()*.5,s:.12+Math.random()*.32,phase:Math.random()*Math.PI*2,seed:i}));};
    const project=(p,t)=>{const rot=t*p.s*.001+p.phase*.15;let x=Math.sin(p.b)*Math.cos(p.a+rot),y=Math.cos(p.b),z=Math.sin(p.b)*Math.sin(p.a+rot);const mx=mouse.active?(mouse.x/width-.5)*.35:0;const my=mouse.active?(mouse.y/height-.5)*.22:0;const cx=x*Math.cos(mx)-z*Math.sin(mx);const cz=x*Math.sin(mx)+z*Math.cos(mx);const cy=y*Math.cos(my)-cz*Math.sin(my);const zz=y*Math.sin(my)+cz*Math.cos(my);const scale=1.1/(1.8-zz);return {x:width*.72+cx*width*.23*scale,y:height*.5+cy*height*.42*scale,z:zz};};
    const draw=(t)=>{raf=0;if(!visible||document.hidden)return;ctx.clearRect(0,0,width,height);const ps=points.map(p=>project(p,t));for(let i=0;i<ps.length;i++){for(let j=i+1;j<ps.length;j++){const dx=ps[i].x-ps[j].x,dy=ps[i].y-ps[j].y,d=Math.hypot(dx,dy);if(d<width*.15){const alpha=(1-d/(width*.15))*.16*(.4+(ps[i].z+ps[j].z+2)/4);ctx.beginPath();ctx.moveTo(ps[i].x,ps[i].y);ctx.lineTo(ps[j].x,ps[j].y);ctx.strokeStyle=`rgba(22,164,224,${alpha})`;ctx.lineWidth=.7;ctx.stroke();}}}ps.forEach(p=>{const size=1.2+2.2*((p.z+1)/2);ctx.beginPath();ctx.arc(p.x,p.y,size,0,Math.PI*2);ctx.fillStyle=`rgba(22,164,224,${.25+.45*((p.z+1)/2)})`;ctx.fill();});if(visible)raf=requestAnimationFrame(draw);};
    const observer='IntersectionObserver' in window?new IntersectionObserver(entries=>{visible=entries[0]?.isIntersecting??true;if(visible&&!raf)raf=requestAnimationFrame(draw);},{rootMargin:'100px'}):null; observer?.observe(host);
    host.addEventListener('pointermove',e=>{const r=canvas.getBoundingClientRect();mouse.x=e.clientX-r.left;mouse.y=e.clientY-r.top;mouse.active=true;},{passive:true}); host.addEventListener('pointerleave',()=>{mouse.active=false;},{passive:true}); window.addEventListener('resize',resize,{passive:true}); resize(); raf=requestAnimationFrame(draw);
  }
})();
