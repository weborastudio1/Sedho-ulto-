from pathlib import Path
import re

projects = [
# best client work
('Elite Eleven Sporting','https://eliteelevensporting.com/','Best Work, International, eCommerce, Sports','Web development + digital marketing','International eCommerce for clothing and sports brands.'),
('Love, Bonito','https://www.lovebonito.com/','Best Work, International, eCommerce, Fashion','Web development + digital marketing','Women’s clothing and sports brand eCommerce experience.'),
('Bargainia','https://bargainia.com/','Best Work, International, eCommerce, Furniture','SEO + product listing + digital marketing','Premium furniture and home products digital growth work.'),
('Down Home Dental','https://www.downhomedentalkansas.com/','Best Work, Health, Dental, International','Web development + digital marketing','Dental practice website and digital marketing.'),
('Gidental Center','https://www.gidentalcenter.com/','Best Work, Health, Dental, International','Web development + digital marketing','Dental healthcare web presence.'),
('The Dentists in Lawrence','https://www.thedentistsinlawrence.com/','Best Work, Health, Dental, International','Digital marketing','Dental practice digital marketing work.'),
('Aesthetic Dentistry PC','https://aestheticdentistrypc.com/','Best Work, Health, Dental, International','Google Search Ads','Paid search campaign work for a dental practice.'),
('Minden Dentist','https://www.mindennedentist.com/','Best Work, Health, Dental, International','Web development + digital marketing','Dental practice digital presence.'),
('Dr. Baker Neurosurgery','https://www.drbakerneurosurgery.com/','Best Work, Health, Medical, International','Web development','Neurosurgery specialist website.'),
('Michigan Orthopaedic Institute','https://michiganortho.com/','Best Work, Health, Orthopedic, International','Web development','Orthopedic healthcare website.'),
('Lynda’s Events','https://lyndasevents.com/','Best Work, International, Events','Web development','Event planner website experience.'),
('Pavestone','https://www.pavestone.com/','Best Work, International, Construction, Ads','Google Ads + TikTok Ads + Meta Ads','Digital marketing for paver, block and tile products.'),
('US Brick & Block','https://usbrickandblock.com/','Best Work, International, Construction','Web development','Website for bricks, blocks and building products.'),
('GCC','https://www.gcc.com/','Best Work, International, Construction','Digital marketing + web development','Construction materials digital presence.'),
('CEMEX USA','https://www.cemexusa.com/','Best Work, International, Construction','Digital marketing + web development','Construction materials digital work.'),
('Construction Kenya','https://www.constructionkenya.com/','Best Work, International, Media','Website development + AdSense approval','News and publishing website development.'),
('Plano Eye Care','https://www.planoeyecare.com/','Best Work, Health, Eye Care, International','Web development','Eye care and doctors website.'),
('Plano Eye','https://planoeye.com/','Best Work, Health, Eye Care, International','Google Ads + Facebook Ads','Paid social and search campaigns.'),
('EyeCare Consultants of Texas','https://eyecarecs.com/','Best Work, Health, Eye Care, International','Google Search Ads','Search advertising for eye care.'),
('Bennett Eye Care Midwest','https://www.bennetteyecaremidwest.com/','Best Work, Health, Eye Care, International','Web development','Eye doctor website development.'),
('Ecoadoctors','https://www.ecoadoctors.com/','Best Work, Health, Eye Care, International','Google Ads','Google advertising work.'),
('Graham County Hospital','https://grahamcountyhospital.org/','Best Work, Health, Hospital, International','Web development','Hospital website development.'),
('UnitedMD','https://unitedmd.com/','Best Work, Health, Hospital, International','Web development','Healthcare organization website.'),
('Piper Electric','https://piperelectric.com/','Best Work, International, Electrical','Web development + digital marketing','Electrician business website and growth work.'),
('Mr. Electric Dallas','https://www.mrelectricdallas.com/','Best Work, International, Electrical','Web development + digital marketing','Electrical services digital presence.'),
('The American Electrician','https://www.theamericanelectrician.com/','Best Work, International, Electrical','Web development + digital marketing','Electrician website and marketing.'),
('Heineken Electric','https://heinekenelectric.com/','Best Work, International, Electrical','Web development + digital marketing','Electrical services web presence.'),
('7 Leaves Cafe','https://7leavescafe.com/','Best Work, International, Cafe','Web development + digital marketing','Cafe digital presence.'),
('7 Brew','https://7brew.com/','Best Work, International, Cafe','Web development + digital marketing','Drive-through beverage brand digital experience.'),
('Americana Las Vegas','https://americanalasvegas.com/','Best Work, International, Restaurant','Web development + digital marketing','Restaurant website and marketing work.'),
('Total Wine','https://www.totalwine.com/','Best Work, International, Retail','Web design + digital marketing','Retail and beverage digital experience.'),
('Roots to Fruits Nursery','https://rootstofruitsnursery.com/','Best Work, International, Nursery','Web development + digital marketing','Nursery business digital presence.'),
('Another Broken Egg Cafe','https://www.anotherbrokenegg.com/','Best Work, International, Restaurant','Web development + digital marketing','Restaurant digital experience.'),
('Jim’s Restaurants','https://www.jimsrestaurants.com/','Best Work, International, Restaurant','Web development + digital marketing','Restaurant website and marketing work.'),
('Cafe Ole','https://cafeole.org/','Best Work, International, Restaurant','Web development + digital marketing','Restaurant digital presence.'),
('JLF Firm','https://jlffirm.com/','Best Work, International, Legal','Web development','Law firm website.'),
('Dodds Law','https://doddslaw.com/','Best Work, International, Legal','Web development','Law firm digital presence.'),
('Castillo Law','https://www.castillolaw.us/','Best Work, International, Legal','Web development','Legal services website.'),
('Selis Law','https://www.selislaw.com/','Best Work, International, Legal','Web development','Law firm website.'),
('Eduprize','https://www.eduprize.com/','Best Work, International, Education','Web development','School website experience.'),
('Comfort Plus Shoes','https://comfortplusshoes.com/','Best Work, International, eCommerce, Fashion','Web development','Footwear eCommerce presence.'),
('Alankaram','https://www.alankaram.in/','Best Work, India, eCommerce, Furniture','Web development + digital marketing','Premium furniture brand eCommerce work in India.'),
# demos / additional work
('SpaceEdu','https://spaceedu-site-2-1.vercel.app','Web Development, Education, Demo','Web development','Education-focused website concept.'),
('Terra Hero','https://terra-hero-manik.vercel.app/','Web Development, Creative, Demo','Web development','Creative hero-led web experience.'),
('Tubes — Interactive Background','https://tubes-interactive-background-vercel.vercel.app','Creative, 3D / Interactive, Demo','Interactive web development','Experimental interactive visual experience.'),
('LTX — The World Model','https://ltx-ecom.vercel.app/','Creative, Web Design, Interactive, Demo','Interactive web design','Cinematic interactive product storytelling.'),
('Cyber Ronin — Neural Edges','https://cyber-ronin-neural-edges.vercel.app/','Creative, UI/UX, Product, Demo','Landing page + UI/UX','Futuristic product landing experience.'),
('Loopa — Team Productivity','https://loopa-memphis-vercel.vercel.app/','SaaS, Product UI, Conversion, Demo','Web design + conversion','SaaS-style productivity product experience.'),
('Orbit — Secure System','https://orbit-secure-system.vercel.app/','Technology, Web UI, Systems, Demo','Web UI + systems design','Technology-focused interface.'),
('ManikHub','https://manikhub.vercel.app/','Web Development, Business, Demo','Web development','Business web experience.'),
('Cast Steel','https://cast-steel.vercel.app/','Web Development, Industrial, Demo','Web development','Industrial product website concept.'),
('GreenGrow Nursery','https://greengrow-nursery.vercel.app/','Business, Nursery, Demo','Web development','Nursery and plant business website.'),
('Do Better Help','https://www.dobetterhelp.com/','Health, Services, International','Web development','Health and service-focused website.'),
('Colours Photobooks','https://coloursphotobooks.in/','Creative, Photography, India','Web development','Photography and photobook business website.'),
('Prime Estate Global','https://prime-estate-global-delta.vercel.app/','Real Estate, UI/UX, Demo','Web development','Real-estate presentation experience.'),
('SmileCove Dental','https://smilecove-dental.vercel.app/','Health, Dental, Demo','Web development','Dental clinic website concept.'),
('STRONVEX Fitness','https://stronvex-fitness.vercel.app/','Fitness, Branding, Demo','Web development','Fitness brand website.'),
('My Interior App','https://my-interior-app.vercel.app/','Interior, Portfolio, Demo','Web development','Interior design visual presentation.'),
('Kitchen Interior Design','https://kitchen-interior-design.vercel.app/','Interior, Design, Demo','Web development','Kitchen interior design experience.'),
('Home Interior Demo','https://home-interior-demo.vercel.app/','Interior, Design, Demo','Web development','Home interior presentation.'),
('Benevolent Project','https://benevolent-smakager-c642c0.netlify.app/','Web Development, Demo','Web development','Additional website project.'),
('Fascinating Parfait','https://fascinating-parfait-84da0b.netlify.app/','Web Development, Demo','Web development','Additional website project.'),
('Illustrious Capybara','https://illustrious-capybara-bf7111.netlify.app/','Web Development, Demo','Web development','Additional website project.'),
('Aarshdeep Dental Hospital','https://aarshdeepdentalhospital.netlify.app/','Health, Dental, Demo','Web development','Dental hospital website demo.'),
('Sprightly Kashata','https://sprightly-kashata-3029ae.netlify.app/','Web Development, Demo','Web development','Additional website project.'),
('Shades of Smile','https://shades-of-smile1.netlify.app/','Health, Dental, Demo','Web development','Dental website demo.'),
]
# dedupe by url, preserving first occurrence
seen=set(); rows=[]
for p in projects:
    if p[1] not in seen:
        seen.add(p[1]); rows.append(p)
projects=rows

# local fallback image pool from existing site assets
fallbacks=['images/hero-home0.jpg','images/hero-home1.jpg','images/hero-home2.jpg','images/hero-home3.jpg','images/hero-home4.jpg','images/Ecommerce.png','images/agency.png']

cards=[]
for i,(name,url,cats,service,desc) in enumerate(projects,1):
    cat_list=[c.strip() for c in cats.split(',')]
    best='best' if 'Best Work' in cat_list else ''
    primary=cat_list[1] if len(cat_list)>1 else cat_list[0]
    domain=re.sub(r'^https?://(www\.)?','',url).rstrip('/')
    # use remote screenshot service; local fallback remains if service is unavailable
    preview='https://image.thum.io/get/width/1200/crop/760/noanimate/'+url
    fb=fallbacks[(i-1)%len(fallbacks)]
    tags=''.join(f'<span>{x}</span>' for x in cat_list[:3])
    cards.append(f'''<article class="project-card reveal" data-categories="{'|'.join(x.lower() for x in cat_list)}" data-rank="{0 if best else 1}">
  <a class="project-media" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="Open {name} website">
    <img src="{preview}" data-fallback="{fb}" alt="{name} website preview" loading="lazy" decoding="async">
    <span class="project-number">{i:02d}</span>
    <span class="project-badge">{('BEST WORK' if best else primary.upper())}</span>
    <span class="project-view"><i class="fa-solid fa-arrow-up-right-from-square"></i> Live</span>
  </a>
  <div class="project-content">
    <div class="project-top"><span class="project-service">{service}</span><span class="project-domain">{domain}</span></div>
    <h3>{name}</h3>
    <p>{desc}</p>
    <div class="project-tags">{tags}</div>
    <a class="project-link" href="{url}" target="_blank" rel="noopener noreferrer">View project <span>↗</span></a>
  </div>
</article>''')

html=Path('/mnt/data/work/portfolio.html').read_text()
start=html.index('<main id="main">')
end=html.index('</main>', start)+len('</main>')
new_main=f'''<main id="main">
<section class="portfolio-hero">
  <div class="container portfolio-hero-grid">
    <div>
      <span class="eyebrow">Our work</span>
      <h1>Work that deserves a closer look. <span>Built for the real web.</span></h1>
      <p>From international eCommerce and healthcare websites to paid-growth work and experimental interfaces, this is the broader WEBORA work library. Best work is prioritised first, then grouped by industry and project type.</p>
      <div class="hero-actions"><a href="#work" class="btn btn-primary">Explore all work <i class="fa-solid fa-arrow-down"></i></a><a href="contact.html" class="btn btn-outline">Start a project</a></div>
      <div class="portfolio-stats"><div><strong>{len(projects)}</strong><span>listed projects</span></div><div><strong>01</strong><span>prioritised best-work layer</span></div><div><strong>∞</strong><span>ways to build</span></div></div>
    </div>
    <div class="portfolio-hero-art" aria-hidden="true"><div class="hero-art-grid"></div><div class="hero-orb orb-a"></div><div class="hero-orb orb-b"></div><div class="hero-art-card"><span>WEBORA / WORK INDEX</span><strong>Web · Growth · Design</strong><small>Live domains. Real project destinations.</small></div></div>
  </div>
</section>
<section class="portfolio-filter-wrap" id="work">
  <div class="container">
    <div class="portfolio-toolbar"><div><span class="eyebrow">Work library</span><h2>Browse the work.</h2></div><div class="work-count" id="workCount">Showing {len(projects)} projects</div></div>
    <div class="portfolio-filters" role="tablist" aria-label="Portfolio filters">
      <button class="filter-btn active" data-filter="all" role="tab" aria-selected="true">All work</button>
      <button class="filter-btn" data-filter="best work" role="tab" aria-selected="false">Best work</button>
      <button class="filter-btn" data-filter="health" role="tab" aria-selected="false">Health</button>
      <button class="filter-btn" data-filter="international" role="tab" aria-selected="false">International</button>
      <button class="filter-btn" data-filter="ecommerce" role="tab" aria-selected="false">eCommerce</button>
      <button class="filter-btn" data-filter="cafe" role="tab" aria-selected="false">Cafe / Restaurant</button>
      <button class="filter-btn" data-filter="construction" role="tab" aria-selected="false">Construction</button>
      <button class="filter-btn" data-filter="creative" role="tab" aria-selected="false">Creative</button>
      <button class="filter-btn" data-filter="demo" role="tab" aria-selected="false">Demos</button>
      <button class="filter-btn" data-filter="india" role="tab" aria-selected="false">India</button>
    </div>
    <div class="project-grid portfolio-project-grid">{''.join(cards)}</div>
    <div class="empty-work" id="emptyWork" hidden><i class="fa-regular fa-folder-open"></i><h3>No projects in this filter yet.</h3><p>Try another category to explore the full work library.</p></div>
  </div>
</section>
<section class="section section-soft portfolio-proof"><div class="container split-grid"><div class="split-copy"><span class="eyebrow">How to read this portfolio</span><h2>See the work. Open the domain. Then talk to us.</h2><p>Every card keeps the project destination visible so a prospect can move from portfolio proof to the live website in one tap. Service labels describe the work supplied in your project list; they are not performance guarantees.</p><a href="contact.html" class="text-link">Discuss a similar project <span>→</span></a></div><div class="proof-card proof-stack"><div class="proof-row"><span>01</span><div><strong>Best work first</strong><small>Highest-priority projects sit at the top.</small></div></div><div class="proof-row"><span>02</span><div><strong>Domain visible</strong><small>Clients can inspect the destination directly.</small></div></div><div class="proof-row"><span>03</span><div><strong>Category filters</strong><small>Find healthcare, eCommerce, hospitality, demos and more.</small></div></div></div></div></section>
<section class="section cta-band"><div class="container cta-band-inner"><div><span class="eyebrow">Build the next one</span><h2>Have a project that should live in this library?</h2></div><a href="contact.html" class="btn btn-light">Start a project <span>→</span></a></div></section>
</main>'''
Path('/mnt/data/work/portfolio.html').write_text(html[:start]+new_main+html[end:])

# patch stylesheet by appending portfolio + 3D background system
css=Path('/mnt/data/work/css/style.css').read_text()
css += r'''

/* WEBORA 3D ambient layer + premium portfolio */
body::before{content:"";position:fixed;inset:-25%;z-index:-2;pointer-events:none;background:radial-gradient(circle at 15% 20%,rgba(22,164,224,.09),transparent 24%),radial-gradient(circle at 85% 65%,rgba(0,105,160,.07),transparent 22%),linear-gradient(135deg,rgba(255,255,255,.95),rgba(246,251,254,.96));}
body::after{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.42;background-image:linear-gradient(rgba(22,164,224,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(22,164,224,.035) 1px,transparent 1px);background-size:58px 58px;mask-image:linear-gradient(to bottom,black,transparent 78%);}
.ambient-3d{position:fixed;inset:0;z-index:-1;overflow:hidden;pointer-events:none;perspective:1000px;opacity:.7}.ambient-3d span{position:absolute;border:1px solid rgba(22,164,224,.12);border-radius:24%;transform-style:preserve-3d;animation:float3d 18s ease-in-out infinite}.ambient-3d .a1{width:190px;height:190px;left:4%;top:22%;transform:rotateX(58deg) rotateZ(32deg)}.ambient-3d .a2{width:120px;height:120px;right:7%;top:42%;transform:rotateX(62deg) rotateZ(-24deg);animation-delay:-6s}.ambient-3d .a3{width:260px;height:260px;right:18%;bottom:-80px;transform:rotateX(66deg) rotateZ(18deg);animation-delay:-11s}.ambient-3d .a4{width:85px;height:85px;left:34%;top:14%;border-radius:50%;animation-delay:-3s}
@keyframes float3d{0%,100%{translate:0 0;rotate:0deg}50%{translate:18px -24px;rotate:8deg}}
.portfolio-hero{padding:92px 0 70px;position:relative;overflow:hidden;background:linear-gradient(180deg,rgba(248,252,254,.96),rgba(255,255,255,.9))}.portfolio-hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:70px;align-items:center}.portfolio-hero h1{font-size:clamp(44px,6.3vw,78px);line-height:.98;letter-spacing:-.06em;margin-top:16px;max-width:850px}.portfolio-hero h1 span{color:var(--primary)}.portfolio-hero p{max-width:720px;color:var(--muted);font-size:18px;margin-top:22px}.portfolio-stats{display:flex;gap:28px;margin-top:38px;flex-wrap:wrap}.portfolio-stats div{display:grid;gap:2px}.portfolio-stats strong{font-size:24px;letter-spacing:-.04em}.portfolio-stats span{font-size:10px;color:#788695;text-transform:uppercase;letter-spacing:.12em;font-weight:800}.portfolio-hero-art{min-height:430px;position:relative;border:1px solid rgba(210,226,235,.8);border-radius:34px;background:linear-gradient(145deg,#fafdff,#e9f5fa);overflow:hidden;box-shadow:0 30px 80px rgba(16,24,32,.09);isolation:isolate}.hero-art-grid{position:absolute;inset:-30%;background-image:linear-gradient(rgba(22,164,224,.1) 1px,transparent 1px),linear-gradient(90deg,rgba(22,164,224,.1) 1px,transparent 1px);background-size:38px 38px;transform:perspective(600px) rotateX(58deg) rotateZ(-18deg) translateY(80px);transform-origin:center;opacity:.65}.hero-orb{position:absolute;border-radius:50%;filter:blur(1px);mix-blend-mode:multiply}.orb-a{width:260px;height:260px;left:-80px;top:40px;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.9),rgba(22,164,224,.18) 45%,rgba(22,164,224,0) 70%);animation:orbFloat 10s ease-in-out infinite}.orb-b{width:340px;height:340px;right:-120px;bottom:-130px;background:radial-gradient(circle at 40% 35%,rgba(255,255,255,.8),rgba(0,105,160,.13) 48%,transparent 70%);animation:orbFloat 13s ease-in-out infinite reverse}.hero-art-card{position:absolute;left:50%;top:50%;width:min(78%,360px);padding:24px;border-radius:22px;background:rgba(255,255,255,.72);border:1px solid rgba(255,255,255,.9);box-shadow:0 25px 55px rgba(16,24,32,.12);backdrop-filter:blur(16px);transform:translate(-50%,-50%) rotate(-4deg);animation:cardFloat 7s ease-in-out infinite}.hero-art-card span{font-size:9px;font-weight:900;letter-spacing:.18em;color:var(--primary-dark)}.hero-art-card strong{display:block;font-size:28px;line-height:1.05;letter-spacing:-.04em;margin-top:14px}.hero-art-card small{display:block;color:#6e7e8d;margin-top:10px;font-size:12px}@keyframes orbFloat{50%{translate:18px -18px;scale:1.05}}@keyframes cardFloat{50%{translate:0 -12px;rotate:1deg}}
.portfolio-filter-wrap{padding:76px 0 110px;background:rgba(247,250,252,.88);border-top:1px solid var(--line)}.portfolio-toolbar{display:flex;align-items:end;justify-content:space-between;gap:25px;margin-bottom:28px}.portfolio-toolbar h2{font-size:clamp(32px,4vw,52px);letter-spacing:-.05em;margin-top:8px}.work-count{font-size:12px;font-weight:800;color:#788695}.portfolio-filters{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:34px}.filter-btn{border:1px solid var(--line);background:#fff;color:#596876;padding:11px 16px;border-radius:999px;font-size:11px;font-weight:850;cursor:pointer;transition:all var(--transition);box-shadow:0 2px 8px rgba(16,24,32,.025)}.filter-btn:hover{border-color:#9bd7ee;color:var(--primary-dark);transform:translateY(-1px)}.filter-btn.active{background:var(--primary);border-color:var(--primary);color:#fff;box-shadow:0 8px 20px rgba(22,164,224,.2)}.portfolio-project-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}.portfolio-project-grid .project-card{padding:0;overflow:hidden;border-radius:22px;background:#fff;border:1px solid #dfe8ef;box-shadow:0 12px 32px rgba(16,24,32,.055);transition:transform .3s ease,box-shadow .3s ease,border-color .3s ease}.portfolio-project-grid .project-card:hover{transform:translateY(-7px);box-shadow:0 24px 60px rgba(16,24,32,.12);border-color:#b7e1f0}.project-media{display:block;position:relative;aspect-ratio:16/9;background:linear-gradient(135deg,#eaf6fb,#cfeaf5);overflow:hidden}.project-media::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.04),transparent 42%,rgba(0,0,0,.22));pointer-events:none}.project-media img{width:100%;height:100%;object-fit:cover;transition:transform .65s cubic-bezier(.2,.7,.2,1),filter .4s ease}.project-card:hover .project-media img{transform:scale(1.035);filter:saturate(1.04)}.project-number,.project-badge,.project-view{position:absolute;z-index:2}.project-number{left:14px;top:14px;width:34px;height:34px;border-radius:11px;background:rgba(255,255,255,.9);display:grid;place-items:center;font-size:10px;font-weight:950}.project-badge{right:14px;top:14px;padding:7px 10px;border-radius:999px;background:rgba(9,20,27,.82);color:#fff;font-size:8px;font-weight:900;letter-spacing:.08em;backdrop-filter:blur(8px)}.project-view{right:14px;bottom:14px;padding:8px 11px;border-radius:10px;background:#159fe0;color:#fff;font-size:10px;font-weight:850;box-shadow:0 8px 20px rgba(22,164,224,.28)}.project-content{padding:20px 20px 19px}.project-top{display:flex;align-items:center;justify-content:space-between;gap:12px}.project-service{font-size:9px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--primary-dark)}.project-domain{font-size:9px;color:#8997a4;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:50%}.project-content h3{font-size:21px;letter-spacing:-.03em;line-height:1.15;margin-top:9px}.project-content p{font-size:13px;color:var(--muted);margin-top:7px;min-height:40px}.project-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:13px}.project-tags span{padding:5px 8px;background:#f2f7fa;border-radius:7px;color:#71808d;font-size:9px;font-weight:800}.project-link{display:flex;justify-content:space-between;align-items:center;margin-top:16px;padding-top:13px;border-top:1px solid #edf1f4;color:#168fca;font-size:12px;font-weight:900}.project-link span{transition:transform .2s ease}.project-link:hover span{transform:translate(3px,-3px)}.project-card.is-hidden{display:none}.empty-work{text-align:center;padding:70px 20px;color:var(--muted)}.empty-work i{font-size:34px;color:var(--primary)}.empty-work h3{font-size:22px;margin-top:14px;color:var(--ink)}.empty-work p{margin-top:5px}.proof-stack{display:grid;gap:0;padding:0;overflow:hidden}.proof-row{display:grid;grid-template-columns:42px 1fr;gap:15px;padding:22px;border-bottom:1px solid var(--line)}.proof-row:last-child{border-bottom:0}.proof-row>span{font-size:10px;font-weight:950;color:var(--primary-dark);padding-top:2px}.proof-row strong{display:block;font-size:15px}.proof-row small{display:block;color:var(--muted);font-size:12px;margin-top:3px}
@media(max-width:900px){.portfolio-hero-grid{grid-template-columns:1fr}.portfolio-hero-art{min-height:340px}.portfolio-project-grid{grid-template-columns:1fr}}
@media(max-width:560px){.portfolio-hero{padding:64px 0 55px}.portfolio-hero h1{font-size:clamp(40px,13vw,58px)}.portfolio-hero p{font-size:15px}.portfolio-stats{gap:18px}.portfolio-hero-art{min-height:285px}.hero-art-card strong{font-size:22px}.portfolio-toolbar{align-items:flex-start;flex-direction:column;gap:8px}.filter-btn{padding:9px 12px}.project-content{padding:17px}.project-domain{max-width:43%}.ambient-3d{display:none}}
@media(prefers-reduced-motion:reduce){.ambient-3d,.hero-orb,.hero-art-card{animation:none!important}.project-media img{transition:none}}
'''
Path('/mnt/data/work/css/style.css').write_text(css)

# add ambient layer to all pages after body opening, and include filter logic in JS
for f in Path('/mnt/data/work').glob('*.html'):
    s=f.read_text()
    if '<body' in s and 'class="ambient-3d"' not in s:
        s=s.replace('>', '>\n  <div class="ambient-3d" aria-hidden="true"><span class="a1"></span><span class="a2"></span><span class="a3"></span><span class="a4"></span></div>', 1)
        f.write_text(s)

js=Path('/mnt/data/work/js/main.js').read_text()
js += r'''

// Portfolio filtering and resilient preview fallbacks
const portfolioGrid = document.querySelector('.portfolio-project-grid');
if (portfolioGrid) {
  const cards = [...portfolioGrid.querySelectorAll('.project-card')];
  const buttons = [...document.querySelectorAll('.filter-btn')];
  const count = document.getElementById('workCount');
  const empty = document.getElementById('emptyWork');
  const applyFilter = (filter) => {
    let visible = 0;
    cards.forEach(card => {
      const categories = (card.dataset.categories || '').split('|');
      const match = filter === 'all' || categories.includes(filter);
      card.classList.toggle('is-hidden', !match);
      if (match) visible++;
    });
    if (count) count.textContent = `Showing ${visible} project${visible === 1 ? '' : 's'}`;
    if (empty) empty.hidden = visible !== 0;
  };
  buttons.forEach(button => button.addEventListener('click', () => {
    buttons.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
    button.classList.add('active'); button.setAttribute('aria-selected','true');
    applyFilter(button.dataset.filter || 'all');
  }));
  portfolioGrid.querySelectorAll('img[data-fallback]').forEach(img => {
    img.addEventListener('error', () => {
      if (img.dataset.failed) return;
      img.dataset.failed = '1';
      img.src = img.dataset.fallback;
    }, { once: true });
  });
  // Best work is already first in the source; keep that ordering stable.
  applyFilter('all');
}
'''
Path('/mnt/data/work/js/main.js').write_text(js)

# Make featured-work redirect to portfolio to eliminate duplicate content
fw=Path('/mnt/data/work/featured-work.html')
fw.write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0; url=portfolio.html"><link rel="canonical" href="https://www.weborastudio.xyz/portfolio.html"><title>Portfolio | WEBORA Studio</title></head><body><p>Portfolio moved to <a href="portfolio.html">Portfolio</a>.</p><script>window.location.replace('portfolio.html');</script></body></html>''')

print(f'Projects: {len(projects)}')
