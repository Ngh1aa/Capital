import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />'

def head(title, desc, extra=''):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  {FONTS}
  <link rel="stylesheet" href="assets/style.css" />
  {extra}
</head>
<body>"""

NAV = """<nav id="main-nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo" aria-label="Capital Place Hanoi home">
      <img class="official-logo" src="assets/brand/capital-place-logo.svg" alt="Capital Place Hanoi" width="89" height="75" />
    </a>
    <div class="nav-links">
      <a href="index.html">Home</a>
      <a href="location.html">Location</a>
      <a href="office.html">Office</a>
      <a href="sustainability.html">Sustainability</a>
      <a href="amenities.html">Amenities</a>
      <div class="nav-sep"></div>
      <div class="lang-btns">
        <button type="button" class="active" onclick="setLang('EN')">EN</button>
        <span class="lang-sep2">|</span>
        <button type="button" onclick="setLang('VI')">VI</button>
      </div>
      <a href="amenities.html#leasing" class="btn-enquire">Enquire</a>
    </div>
    <button type="button" class="nav-ham" id="hamburger" aria-label="Toggle menu" aria-controls="mob-menu" aria-expanded="false">
      <svg id="icon-menu" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/></svg>
      <svg id="icon-close" style="display:none" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>
    </button>
  </div>
  <div id="mob-menu">
    <a href="index.html" onclick="closeMob()">Home</a>
    <a href="location.html" onclick="closeMob()">Location</a>
    <a href="office.html" onclick="closeMob()">Office</a>
    <a href="sustainability.html" onclick="closeMob()">Sustainability</a>
    <a href="amenities.html" onclick="closeMob()">Amenities</a>
    <a href="amenities.html#leasing" class="mob-enq" onclick="closeMob()">Leasing Enquiry</a>
  </div>
</nav>"""

FOOTER = """<footer>
  <div class="container">
    <div class="ft-grid">
      <div>
        <div class="ft-logo">
          <img class="official-logo official-logo-footer" src="assets/brand/capital-place-logo.svg" alt="Capital Place Hanoi" width="89" height="75" />
        </div>
        <p class="ft-intro">A landmark for business.<br>A new icon of Hanoi.</p>
        <p class="ft-addr">29 Lieu Giai<br>Ngoc Ha, Ba Dinh<br>Hanoi, Vietnam</p>
      </div>
      <div class="ft-col">
        <p class="ft-col-title">Explore Capital Place</p>
        <a href="index.html">Home</a>
        <a href="location.html">Location</a>
        <a href="office.html">Office</a>
        <a href="sustainability.html">Sustainability</a>
        <a href="amenities.html">Amenities</a>
      </div>
      <div class="ft-col">
        <p class="ft-col-title">Contact &amp; Leasing</p>
        <a href="amenities.html#leasing">Leasing Enquiry</a>
        <a href="tel:18009289">1800 9289</a>
        <a href="mailto:leasing@capitalplace.com.vn">leasing@capitalplace.com.vn</a>
      </div>
    </div>
    <div class="ft-bot">
      <p>&copy; 2026 Twin-Peaks Joint Stock Company. All rights reserved.</p>
      <p>Capital Place &middot; Hanoi</p>
    </div>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>"""

# ══════════════════════════════════
# index.html
# ══════════════════════════════════
idx_css = """<style>
#hero{position:relative;height:100svh;min-height:680px;overflow:hidden;background:var(--bg)}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}
.ov1{position:absolute;inset:0;background:rgba(17,17,17,.35)}
.ov2{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(17,17,17,.65) 0%,transparent 50%,var(--bg) 100%)}
.ov3{position:absolute;bottom:0;left:0;right:0;height:45%;background:linear-gradient(to top,var(--bg),transparent)}
.hero-badges{position:absolute;top:86px;right:var(--px);display:flex;flex-direction:column;align-items:flex-end;gap:8px;animation:fadeIn .9s .6s both}
.badge{font-family:var(--sans);font-size:9px;letter-spacing:.45em;text-transform:uppercase;border:1px solid;padding:7px 12px;backdrop-filter:blur(4px);background:rgba(17,17,17,.3)}
.badge-gold{color:var(--gold);border-color:rgba(184,155,94,.35)}
.badge-dim{color:rgba(184,155,94,.55);border-color:rgba(184,155,94,.15)}
.hero-content{position:absolute;bottom:clamp(4rem,8vw,5rem);left:0;right:0}
.hero-eyebrow{color:var(--gold);font-size:9px;letter-spacing:.55em;text-transform:uppercase;font-family:var(--sans);margin-bottom:1.5rem;animation:fadeUp 1.2s .1s both}
.hero-h1{font-family:var(--serif);font-weight:300;color:#fff;line-height:.88}
.hero-h1 span{display:block;font-size:clamp(2.8rem,7.5vw,6.5rem)}
.hero-h1 .italic{font-style:italic;color:var(--gold)}
.hero-h1 span:nth-child(1){animation:fadeUp 1s .2s both}
.hero-h1 span:nth-child(2){animation:fadeUp 1s .32s both}
.hero-h1 span:nth-child(3){animation:fadeUp 1s .44s both}
.hero-specs{margin-top:1.75rem;display:flex;flex-wrap:wrap;align-items:center;gap:1.25rem;animation:fadeUp 1s .5s both}
.hero-spec{display:flex;align-items:center;gap:1.25rem;font-family:var(--sans);font-size:9px;letter-spacing:.35em;text-transform:uppercase;color:rgba(255,255,255,.28)}
.spec-sep{width:1px;height:12px;background:rgba(184,155,94,.25)}
.hero-ctas{margin-top:2.25rem;display:flex;flex-wrap:wrap;gap:1rem;animation:fadeUp 1s .55s both}
.scroll-cue{position:absolute;bottom:28px;right:var(--px);display:flex;flex-direction:column;align-items:center;gap:6px;color:rgba(255,255,255,.18)}
.scroll-cue span{font-family:var(--sans);font-size:8px;letter-spacing:.4em;text-transform:uppercase}
.scroll-cue svg{width:12px;height:12px;margin-top:4px}
#specbar{border-top:1px solid var(--gold-b);border-bottom:1px solid var(--gold-b);background:var(--bg)}
.spec-grid{display:grid;grid-template-columns:repeat(2,1fr)}
@media(min-width:768px){.spec-grid{grid-template-columns:repeat(4,1fr)}}
.stat-cell{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2.5rem 1.5rem;gap:8px;border-right:1px solid var(--gold-b);border-bottom:1px solid var(--gold-b)}
@media(min-width:768px){.stat-cell{border-bottom:none}}
.stat-cell:last-child{border-right:none}
.stat-num{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(2rem,4vw,3.5rem)}
.stat-label{font-family:var(--sans);font-size:9px;letter-spacing:.42em;text-transform:uppercase;color:var(--gold)}
#explore{background:var(--bg);padding:clamp(6rem,12vw,9rem) 0}
.exp-header{margin-bottom:clamp(3.5rem,7vw,4.5rem);display:flex;flex-direction:column;gap:1.5rem}
@media(min-width:768px){.exp-header{flex-direction:row;align-items:flex-end}}
.exp-header .left{flex:1}
.exp-header>p{color:rgba(255,255,255,.42);font-size:14px;max-width:280px;line-height:1.7}@media(min-width:1100px){.exp-header>p{max-width:none;white-space:nowrap}}
.exp-grid{display:grid}
@media(min-width:1024px){.exp-grid{grid-template-columns:1fr 1.4fr}}
.zone-list{border-top:1px solid var(--gold-b)}
.zone-item{width:100%;text-align:left;border-bottom:1px solid var(--gold-b);padding:1.5rem 0;display:flex;align-items:flex-start;gap:1.5rem;transition:opacity .3s;background:none}
.zone-item.inactive{opacity:.3}.zone-item.inactive:hover{opacity:.6}
.zone-num{font-family:var(--sans);font-size:9px;letter-spacing:.4em;padding-top:2px;flex-shrink:0;min-width:24px;transition:color .3s;color:rgba(255,255,255,.3)}
.zone-item.active .zone-num{color:var(--gold)}
.zone-body{flex:1;min-width:0}
.zone-head{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-bottom:4px}
.zone-head h3{font-family:var(--serif);font-weight:300;font-size:clamp(1.1rem,2vw,1.3rem);line-height:1.2;transition:color .3s;color:rgba(255,255,255,.7)}
.zone-item.active .zone-head h3{color:#fff}
.zone-chevron{width:13px;height:13px;flex-shrink:0;transition:opacity .3s}
.zone-item.active .zone-chevron{color:var(--gold);opacity:1}
.zone-item.inactive .zone-chevron{opacity:0}
.zone-sub{font-family:var(--sans);font-size:9px;letter-spacing:.22em;text-transform:uppercase;transition:color .3s;color:rgba(255,255,255,.22)}
.zone-item.active .zone-sub{color:rgba(184,155,94,.65)}
.zone-detail{font-size:14px;line-height:1.7;color:var(--warm-ivory);overflow:hidden;max-height:0;opacity:0;transition:max-height .4s cubic-bezier(.22,1,.36,1),opacity .35s ease,margin-top .35s;margin-top:0}
.zone-detail.open{max-height:120px;opacity:1;margin-top:12px}
.img-panel{display:block;padding-left:0;margin-top:2rem}
@media(min-width:1024px){.img-panel{padding-left:3rem;margin-top:0}}
.img-sticky{position:relative}
@media(min-width:1024px){.img-sticky{position:sticky;top:88px}}
.img-wrap{position:relative;overflow:hidden;background:var(--card);height:min(72vh,640px)}
.zone-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .7s ease,transform .7s ease;opacity:0;transform:scale(1.04)}
.zone-img.active{opacity:1;transform:scale(1)}
.img-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(17,17,17,.85) 0%,transparent 60%,rgba(17,17,17,.15) 100%)}
.img-lbl{position:absolute;bottom:0;left:0;right:0;padding:3.75rem 2rem 2rem;z-index:2;overflow:hidden}.img-lbl::before{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(4,10,14,.96) 0%,rgba(4,10,14,.72) 48%,transparent 100%);z-index:-1;pointer-events:none}
.img-lbl-sub{font-family:var(--sans);font-size:9px;letter-spacing:.45em;text-transform:uppercase;color:var(--gold)}
.img-lbl-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(1.4rem,2.5vw,1.8rem);margin-top:4px}
.zone-dots{position:absolute;right:24px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:8px}
.zone-dot{width:1px;background:rgba(255,255,255,.2);transition:height .3s,background .3s;height:16px;border:none}
.zone-dot.active{height:32px;background:var(--gold)}.zone-dot:hover{background:rgba(255,255,255,.4)}
.quick-links{background:var(--bg2);border-top:1px solid var(--gold-b);padding:clamp(4rem,8vw,6rem) 0}
.ql-grid{display:grid;gap:1px;background:var(--gold-b)}
@media(min-width:768px){.ql-grid{grid-template-columns:repeat(4,1fr)}}
.ql-card{background:var(--bg2);padding:2.5rem 2rem;display:flex;flex-direction:column;gap:1rem;transition:background .25s,transform .25s,border-color .25s;position:relative;border:1px solid transparent}
.ql-card:hover{background:var(--card);border-color:rgba(184,155,94,.34);transform:translateY(-4px);z-index:1}.ql-card:focus-visible{background:var(--card);border-color:var(--gold);transform:translateY(-4px);z-index:1}
.ql-num{font-family:var(--sans);font-size:9px;letter-spacing:.4em;color:rgba(184,155,94,.4)}
.ql-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:1.25rem;line-height:1.2}
.ql-desc{font-family:var(--sans);font-size:13px;color:rgba(255,255,255,.3);line-height:1.6}
.ql-arrow{margin-top:auto;color:var(--gold);display:flex;align-items:center;gap:8px;font-family:var(--sans);font-size:10px;letter-spacing:.25em;text-transform:uppercase}
.ql-arrow svg{width:12px;height:12px;transition:transform .2s}
.ql-card:hover .ql-arrow svg{transform:translateX(3px)}
</style>"""

idx_body = """<section id="hero">
  <video class="hero-bg" autoplay muted loop playsinline preload="metadata" aria-label="Capital Place exterior architecture" poster="assets/images/official/capital-place-towers.jpg">
    <source src="https://capitalplace.com.vn/wp-content/uploads/2026/05/CAPITAL-PLACE-TVC_1080p.mp4" type="video/mp4">
  </video>
  <div class="ov1"></div><div class="ov2"></div><div class="ov3"></div>
  <div class="hero-content"><div class="container">
    <p class="hero-eyebrow">29 Lieu Giai &middot; Ba Dinh &middot; Hanoi</p>
    <h1 class="hero-h1"><span>Hanoi's</span><span class="italic">Premier</span><span>Address</span></h1>
    <div class="hero-specs">
      <span class="hero-spec">93,700 SQM</span>
      <span class="hero-spec"><span class="spec-sep"></span>2 Towers</span>
      <span class="hero-spec"><span class="spec-sep"></span>41 Storeys</span>
      <span class="hero-spec"><span class="spec-sep"></span>Grade A</span>
    </div>
    <div class="hero-ctas">
      <a href="#explore" class="btn-primary">Explore Building<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a>
      <a href="amenities.html#leasing" class="btn-ghost">Leasing Enquiry</a>
    </div>
  </div></div>
  <div class="scroll-cue"><span>Scroll</span><svg class="anim-bounce" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 13.5L12 21m0 0l-7.5-7.5M12 21V3"/></svg></div>
</section>
<section id="specbar">
  <div class="spec-grid container">
    <div class="stat-cell fade-up"><span class="stat-num" data-target="93700" data-fmt="comma">93,700</span><span class="stat-label">SQM Total GFA</span></div>
    <div class="stat-cell fade-up" style="transition-delay:.1s"><span class="stat-num" data-target="2">2</span><span class="stat-label">Towers</span></div>
    <div class="stat-cell fade-up" style="transition-delay:.2s"><span class="stat-num" data-target="41">41</span><span class="stat-label">Storeys</span></div>
    <div class="stat-cell fade-up" style="transition-delay:.3s"><span class="stat-num" data-target="2015">2015</span><span class="stat-label">Completed</span></div>
  </div>
</section>
<section id="explore">
  <div class="container">
    <div class="exp-header">
      <div class="left"><p class="eyebrow" style="margin-bottom:1rem">Discovery</p><h2 class="section-title">Explore<br><em>Capital Place</em></h2></div>
      <p>Navigate every level of the building &mdash; from the grand lobby to the sky lounge.</p>
    </div>
    <div class="exp-grid">
      <div class="zone-list" id="zone-list"></div>
      <div class="img-panel"><div class="img-sticky"><div class="img-wrap" id="img-wrap" role="region" aria-live="polite" aria-label="Capital Place area preview">
        <div class="img-ov"></div>
        <div class="img-lbl"><p class="img-lbl-sub" id="z-sub"></p><h3 class="img-lbl-title" id="z-title"></h3></div>
        <div class="zone-dots" id="zone-dots"></div>
      </div></div></div>
    </div>
  </div>
</section>
<section class="leasing-tease" aria-labelledby="leasing-tease-title">
  <div class="container">
    <div class="leasing-tease-grid">
      <div>
        <p class="eyebrow" style="margin-bottom:1rem">The Address In Full</p>
        <h2 id="leasing-tease-title" class="section-title">Make space<br><em>for more.</em></h2>
        <p class="leasing-tease-copy">Explore available floor plates, view the building layout, or speak with the Capital Place leasing team.</p>
      </div>
      <div class="leasing-tease-actions">
        <a href="office.html" class="btn-primary">View Floor Plans<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a>
        <a href="amenities.html#leasing" class="btn-ghost">Request Availability</a>
      </div>
    </div>
    <div class="proof-row" aria-label="Capital Place credentials">
      <span>Dual LEED Certified</span><span>Grade-A Office</span><span>93,700 SQM</span><span>29 Lieu Giai</span>
    </div>
  </div>
</section>
<section class="quick-links">
  <div class="container">
    <p class="eyebrow" style="margin-bottom:2.5rem">Explore More</p>
    <div class="ql-grid">
      <a href="location.html" class="ql-card"><span class="ql-num">01</span><h3 class="ql-title">Location</h3><p class="ql-desc">Prime Ba Dinh diplomatic quarter, steps from major embassies and government offices.</p><span class="ql-arrow">View<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></span></a>
      <a href="office.html" class="ql-card"><span class="ql-num">02</span><h3 class="ql-title">Office</h3><p class="ql-desc">Column-free open-plan layouts from 1,850 SQM per floor with full-height glazing.</p><span class="ql-arrow">View<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></span></a>
      <a href="sustainability.html" class="ql-card"><span class="ql-num">03</span><h3 class="ql-title">Sustainability</h3><p class="ql-desc">Dual LEED certified &mdash; Platinum for operations and Gold for design.</p><span class="ql-arrow">View<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></span></a>
      <a href="amenities.html" class="ql-card"><span class="ql-num">04</span><h3 class="ql-title">Amenities</h3><p class="ql-desc">Sky Lounge, fitness centre, conference halls and fine dining across the podium.</p><span class="ql-arrow">View<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></span></a>
    </div>
  </div>
</section>"""

idx_js = """<script>
const ZONES=[
  {num:"01",id:"lobby",label:"Grand Lobby",sub:"Ground Floor \u00b7 Triple-height atrium",detail:"Marble floors, bamboo-inspired columns, and site-specific Vietnamese art define the arrival. The 18\u00a0m atrium opens both towers.",img:"https://www.hanoi-office.com/uploads/files/capital%20place/toa_nha_capital_place_8.jpg"},
  {num:"02",id:"office",label:"Office Floors",sub:"L6 \u2013 L38 \u00b7 Both towers \u00b7 93,700 SQM",detail:"Column-free, open-plan floorplates with full-height glazing. GFA 1,850\u20132,100 SQM per floor. NBF-compliant fresh air.",img:"https://thanhnien.mediacdn.vn/uploaded/quochung.qc/2020_10_12/capitalplace/2_AYLF.jpg?width=1200"},
  {num:"03",id:"fitness",label:"Fitness & Wellness",sub:"The Link · B1",detail:"Fitness facilities that support an active and balanced working day.",img:"assets/images/official/akademy-fitness.jpg"},
  {num:"04",id:"dining",label:"Dining & Retail",sub:"The Link · B1",detail:"Food, beverage and everyday services within the building.",img:"assets/images/official/dining.jpg"},
  {num:"05",id:"lounge",label:"Premium Lounge",sub:"The Nexus",detail:"A hospitality-led setting for executive meetings and guest reception.",img:"assets/images/official/premium-lounge.jpeg"},
  {num:"06",id:"conference",label:"Event Space",sub:"The Nexus",detail:"Flexible settings for presentations, seminars and tenant events.",img:"assets/images/official/lily-event-space.jpeg"},
];
let aZ=0;
(function(){
  const list=document.getElementById('zone-list'),wrap=document.getElementById('img-wrap'),dots=document.getElementById('zone-dots');
  ZONES.forEach((z,i)=>{
    const img=document.createElement('img');img.src=z.img;img.alt=z.label+' at Capital Place';img.loading=i===0?'eager':'lazy';img.decoding='async';img.className='zone-img'+(i===0?' active':'');
    wrap.insertBefore(img,wrap.querySelector('.img-ov'));
    const dot=document.createElement('button');dot.type='button';dot.className='zone-dot'+(i===0?' active':'');dot.setAttribute('aria-label','Show '+z.label);dot.setAttribute('aria-current',i===0?'true':'false');dot.onclick=()=>sz(i);dots.appendChild(dot);
    const btn=document.createElement('button');btn.type='button';btn.className='zone-item'+(i===0?' active':' inactive');
    btn.setAttribute('aria-controls','zone-detail-'+z.id);btn.setAttribute('aria-expanded',i===0?'true':'false');
    btn.innerHTML='<span class="zone-num">'+z.num+'</span><div class="zone-body"><div class="zone-head"><h3>'+z.label+'</h3><svg class="zone-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5"/></svg></div><p class="zone-sub">'+z.sub+'</p><p class="zone-detail'+(i===0?' open':'')+'" id="zone-detail-'+z.id+'">'+z.detail+'</p></div>';
    btn.onmouseenter=()=>sz(i);btn.onfocus=()=>sz(i);btn.onclick=()=>sz(i);list.appendChild(btn);
  });
  document.getElementById('z-sub').textContent=ZONES[0].sub;document.getElementById('z-title').textContent=ZONES[0].label;
})();
function sz(i){if(i===aZ)return;aZ=i;
  document.querySelectorAll('.zone-item').forEach((el,x)=>{el.classList.toggle('active',x===i);el.classList.toggle('inactive',x!==i);el.setAttribute('aria-expanded',x===i?'true':'false');el.querySelector('.zone-detail').classList.toggle('open',x===i)});
  document.querySelectorAll('.zone-img').forEach((el,x)=>el.classList.toggle('active',x===i));
  document.querySelectorAll('.zone-dot').forEach((el,x)=>{el.classList.toggle('active',x===i);el.setAttribute('aria-current',x===i?'true':'false')});
  document.getElementById('z-sub').textContent=ZONES[i].sub;document.getElementById('z-title').textContent=ZONES[i].label;
}
</script>"""

# Feedback image references are intentionally kept as remote URLs because the requested sources are external website assets.
# ══════════════════════════════════
# location.html
# ══════════════════════════════════
loc_css = """<style>
.loc-v2-hero{min-height:clamp(560px,72vh,760px);display:flex;align-items:end;position:relative;overflow:hidden;background:var(--bg)}
.loc-v2-hero .page-header-media{opacity:.68;object-position:center 42%}
.loc-v2-hero::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.14),rgba(17,17,17,.25) 42%,rgba(17,17,17,.94) 100%);pointer-events:none}
.loc-v2-hero>.container{position:relative;z-index:1;padding-bottom:clamp(4rem,9vw,7rem)}@media(min-width:900px){.loc-v2-hero>.container{transform:translateX(-200px)}.loc-v2-hero .page-header-actions .btn-gold{transform:translateY(16px)}}
.loc-v2-hero .page-header-eyebrow{color:var(--gold-champagne)}
.loc-v2-hero h1{max-width:780px}
.loc-v2-hero .hero-location{margin-top:1.5rem;color:var(--warm-ivory);font:11px var(--sans);letter-spacing:.25em;text-transform:uppercase}
.loc-v2-section{padding:clamp(5.5rem,10vw,9rem) 0;background:var(--bg)}
.loc-v2-section.alt{background:var(--bg2)}
.loc-v2-section.ivory{background:var(--warm-ivory);color:var(--capital-black)}
.loc-v2-section.ivory .section-title,.loc-v2-section.ivory h3{color:var(--capital-black)}
.loc-v2-section.ivory .eyebrow{color:var(--deep-gold)}
.loc-v2-section.ivory p{color:rgba(17,17,17,.62)}
.loc-address-grid{display:grid;gap:clamp(2rem,5vw,5rem);align-items:center}
@media(min-width:900px){.loc-address-grid{grid-template-columns:.88fr 1.12fr}}
.loc-address-copy{max-width:34rem}.loc-address-copy>p:not(.eyebrow){margin-top:1.5rem;color:rgba(242,238,229,.62);font:15px/1.8 var(--sans)}
.loc-address-block{border-top:1px solid var(--gold-b);margin-top:2.5rem;padding-top:1.5rem;display:grid;gap:.25rem;color:var(--warm-ivory);font:12px/1.65 var(--sans);letter-spacing:.2em;text-transform:uppercase}
.loc-address-visual{min-height:420px;background:var(--graphite);border:1px solid var(--gold-b);position:relative;overflow:hidden}.loc-address-visual iframe{display:block;width:100%;height:100%;min-height:420px;border:0;filter:contrast(1.02)}.loc-address-visual::after{display:none}.loc-map-caption{position:absolute;left:1.5rem;bottom:1.25rem;padding:.55rem .75rem;background:rgba(17,17,17,.86);color:var(--warm-ivory);font:9px var(--sans);letter-spacing:.3em}
.loc-reach-head{display:flex;gap:2rem;justify-content:space-between;align-items:end;flex-wrap:wrap}.loc-reach-head>p:last-child{max-width:28rem;color:rgba(242,238,229,.56);font:14px/1.7 var(--sans)}
.loc-metric-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--gold-b);margin-top:3.5rem}
.loc-metric{background:var(--bg);padding:clamp(1.5rem,4vw,3rem) 1rem;min-height:170px;display:flex;flex-direction:column;justify-content:space-between}.loc-metric-value{color:var(--gold);font:300 clamp(2.4rem,6vw,5rem) var(--serif)}.loc-metric-label{color:var(--warm-ivory);font:10px var(--sans);letter-spacing:.2em;text-transform:uppercase}.loc-metric-note{color:rgba(242,238,229,.4);font:11px/1.5 var(--sans);margin-top:.5rem}
.loc-metro{background:var(--graphite);overflow:hidden}.loc-metro-grid{display:grid;gap:2rem;align-items:center}@media(min-width:1000px){.loc-metro-grid{grid-template-columns:1fr}}
.loc-metro-copy>p:not(.eyebrow){color:rgba(242,238,229,.6);font:15px/1.8 var(--sans);max-width:34rem;margin-top:1.5rem}.loc-metro-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;margin-top:2.5rem}.loc-metro-stat{border-top:1px solid var(--gold-b);padding-top:.8rem}.loc-metro-stat strong{display:block;color:var(--gold-champagne);font:300 2.4rem var(--serif)}.loc-metro-stat span{display:block;color:rgba(242,238,229,.48);font:9px var(--sans);letter-spacing:.2em;text-transform:uppercase;margin-top:.3rem}
.loc-metro-grid{max-width:900px;margin:0 auto}.loc-metro-copy{max-width:760px}.loc-metro-stats{max-width:680px}
.loc-surroundings{background:var(--capital-black);color:var(--warm-ivory)}.loc-surroundings .section-title{color:var(--capital-black)}.loc-surroundings .eyebrow{color:var(--deep-gold)}.loc-surroundings .loc-section-intro{color:rgba(17,17,17,.58);font:15px/1.8 var(--sans);max-width:34rem;margin-top:1.25rem}.loc-surroundings .container{position:relative}.loc-surroundings .container::before{content:'';position:absolute;inset:0 0 auto;height:265px;background:linear-gradient(180deg,rgba(17,17,17,.96),rgba(17,17,17,.76) 58%,transparent);pointer-events:none}.loc-surroundings .container>*{position:relative;z-index:1}.loc-surroundings .container>.section-title{color:var(--warm-ivory)}.loc-surroundings .container>.loc-section-intro{color:rgba(242,238,229,.72)}.loc-surroundings .container>.eyebrow{color:var(--gold-champagne)}.loc-surroundings .loc-filter{border-color:rgba(242,238,229,.28);color:rgba(242,238,229,.8)}.loc-surroundings .loc-filter:hover,.loc-surroundings .loc-filter:focus-visible,.loc-surroundings .loc-filter.active{background:var(--gold);border-color:var(--gold);color:var(--capital-black)}.loc-filter-row{display:flex;gap:.5rem;flex-wrap:wrap;margin:2.5rem 0 1.5rem}.loc-filter{border:1px solid rgba(17,17,17,.18);background:transparent;padding:.7rem .9rem;color:rgba(17,17,17,.62);cursor:pointer;font:9px var(--sans);letter-spacing:.15em;text-transform:uppercase;transition:background .2s,color .2s,border-color .2s}.loc-filter:hover,.loc-filter:focus-visible,.loc-filter.active{background:var(--capital-black);border-color:var(--capital-black);color:var(--warm-ivory)}.loc-directory{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:transparent}@media(min-width:900px){.loc-directory{grid-template-columns:repeat(3,1fr)}}.loc-card{background:var(--warm-ivory);min-height:245px;padding:1.4rem;display:flex;flex-direction:column;justify-content:end;position:relative;overflow:hidden}.loc-card::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.06) 12%,rgba(17,17,17,.46) 42%,rgba(17,17,17,.96) 100%);opacity:.92}.loc-card-visual{position:absolute;inset:0;background-size:cover;background-position:center;filter:saturate(.72)}.loc-card-content{position:relative;z-index:1;color:var(--warm-ivory)}.loc-card-category{font:9px var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--gold-champagne)}.loc-card h3{font:300 1.35rem var(--serif);margin-top:.4rem;color:var(--warm-ivory)}.loc-card-meta{font:11px var(--sans);color:rgba(242,238,229,.62);margin-top:.35rem}.loc-card[hidden]{display:none}
.loc-business{display:grid;gap:2.5rem;align-items:center}@media(min-width:900px){.loc-business{grid-template-columns:1fr 1fr}}.loc-business-copy>p:not(.eyebrow),.loc-lifestyle-copy>p:not(.eyebrow){color:rgba(242,238,229,.62);font:15px/1.8 var(--sans);max-width:35rem;margin-top:1.25rem}.loc-business-visual,.loc-arrival-visual{min-height:360px;background-size:cover;background-position:center;border:1px solid var(--gold-b)}.loc-business-visual{background-image:linear-gradient(90deg,rgba(17,17,17,.66),rgba(17,17,17,.1)),url(assets/images/feedback/fb4-business.jpg)}.loc-arrival-visual{background-image:linear-gradient(90deg,rgba(17,17,17,.66),rgba(17,17,17,.1)),url(assets/images/feedback/fb4-arrival.jpg)}
.loc-category-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--gold-b);margin-top:2.5rem}.loc-category{background:var(--bg2);padding:1.5rem;min-height:150px;border:0;text-align:left;color:var(--warm-ivory);cursor:pointer;transition:background .2s,transform .2s}.loc-category:hover,.loc-category:focus-visible,.loc-category.active{background:var(--graphite);transform:translateY(-3px)}.loc-category strong{display:block;color:var(--gold);font:300 1.4rem var(--serif)}.loc-category span{display:block;color:rgba(242,238,229,.46);font:9px var(--sans);letter-spacing:.14em;text-transform:uppercase;margin-top:.75rem}
.loc-landmarks{background:var(--bg2)}.loc-landmark-scroller{display:flex;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;padding:2rem 0 .75rem;scrollbar-color:var(--gold) transparent}.loc-landmark{min-width:min(74vw,300px);min-height:230px;background:linear-gradient(180deg,rgba(17,17,17,.05),rgba(17,17,17,.92)),url(assets/images/feedback/location-page-header.jpg) center/cover;scroll-snap-align:start;padding:1.25rem;display:flex;align-items:end;border:1px solid var(--gold-b)}.loc-landmark span{color:var(--warm-ivory);font:10px var(--sans);letter-spacing:.22em;text-transform:uppercase}
.loc-map-section{background:var(--warm-ivory);color:var(--capital-black)}.loc-map-section .section-title{color:var(--capital-black)}.loc-map-section .eyebrow{color:var(--deep-gold)}.loc-map-stage{position:relative;min-height:460px;margin-top:2.5rem;background:linear-gradient(135deg,rgba(242,238,229,.96),rgba(216,208,193,.94)),repeating-linear-gradient(0deg,transparent 0 42px,rgba(17,17,17,.06) 42px 43px),repeating-linear-gradient(90deg,transparent 0 42px,rgba(17,17,17,.06) 42px 43px);border:1px solid rgba(17,17,17,.2);overflow:hidden}.loc-map-stage::before{content:'';position:absolute;inset:8% 14%;border:1px solid rgba(17,17,17,.12);transform:rotate(-8deg);pointer-events:none}.loc-map-stage::after{content:'29 LIEU GIAI · BA DINH · HANOI';position:absolute;left:1rem;top:1rem;color:rgba(17,17,17,.64);font:9px var(--sans);letter-spacing:.2em}.map-road{position:absolute;background:rgba(17,17,17,.24);height:4px;width:78%;left:11%;top:47%;transform:rotate(-13deg);box-shadow:0 0 0 1px rgba(242,238,229,.7)}.map-road-secondary{width:52%;left:24%;top:49%;transform:rotate(62deg)}.map-label{position:absolute;color:rgba(17,17,17,.58);font:9px var(--sans);letter-spacing:.16em;text-transform:uppercase}.map-label-north{left:44%;top:13%}.map-label-west{left:10%;top:38%}.map-label-east{right:10%;top:41%}.map-label-south{left:42%;bottom:12%}.map-pin{position:absolute;width:17px;height:17px;border:2px solid var(--capital-black);border-radius:50%;background:var(--warm-ivory);cursor:pointer;z-index:2;transition:transform .2s,background .2s}.map-pin:hover,.map-pin:focus-visible,.map-pin.active{background:var(--gold);transform:scale(1.3)}.map-pin::after{content:attr(data-label);position:absolute;white-space:nowrap;left:50%;top:23px;transform:translateX(-50%);color:var(--capital-black);font:9px var(--sans);letter-spacing:.12em;text-transform:uppercase}.map-pin.capital{left:48%;top:49%;background:var(--gold);width:25px;height:25px}.map-pin.west{left:63%;top:20%}.map-pin.hotel{left:27%;top:36%}.map-pin.retail{right:17%;top:40%}.map-pin.embassy{left:22%;bottom:22%}.map-pin.dining{right:25%;bottom:18%}.map-pin.hoankiem{left:51%;bottom:8%}.loc-map-legend{position:absolute;left:1rem;top:1rem;display:flex;gap:.6rem;flex-wrap:wrap;color:rgba(17,17,17,.58);font:9px var(--sans);letter-spacing:.14em;text-transform:uppercase}.map-detail{position:absolute;left:1rem;right:1rem;bottom:1rem;background:rgba(17,17,17,.92);color:var(--warm-ivory);padding:1rem 1.2rem;display:flex;align-items:end;justify-content:space-between;gap:1rem}.map-detail h3{color:var(--warm-ivory);font:300 1.3rem var(--serif)}.map-detail p{color:rgba(242,238,229,.56);font:11px var(--sans);margin-top:.25rem}.map-detail a{color:var(--gold);font:9px var(--sans);letter-spacing:.18em;text-transform:uppercase;white-space:nowrap}
.loc-arrival{display:grid;gap:2rem;align-items:center}@media(min-width:900px){.loc-arrival{grid-template-columns:1fr 1fr}}.loc-arrival-copy>p:not(.eyebrow),.transport-panel p{color:rgba(242,238,229,.62);font:15px/1.8 var(--sans);max-width:34rem;margin-top:1.25rem}.arrival-steps{display:grid;grid-template-columns:repeat(5,1fr);gap:.35rem;margin-top:2rem;align-items:start}.arrival-step{border-top:1px solid var(--gold-b);padding-top:.65rem;color:var(--warm-ivory);font:9px var(--sans);letter-spacing:.14em;text-transform:uppercase}.arrival-step::after{content:'↓';display:block;color:var(--gold);margin-top:.5rem}.arrival-step:last-child::after{content:'✓'}
.loc-transport{background:var(--graphite)}.transport-tabs{display:flex;gap:.5rem;flex-wrap:wrap;margin:2.5rem 0 1.5rem}.transport-tab{border:1px solid var(--gold-b);background:transparent;color:rgba(242,238,229,.58);padding:.75rem 1rem;cursor:pointer;font:9px var(--sans);letter-spacing:.16em;text-transform:uppercase}.transport-tab:hover,.transport-tab:focus-visible,.transport-tab.active{background:var(--gold);border-color:var(--gold);color:var(--capital-black)}.transport-panel{border-top:1px solid var(--gold-b);padding-top:1.5rem;min-height:115px}.transport-panel p{max-width:40rem}.transport-panel#transport-car p{max-width:31rem;white-space:normal;overflow-wrap:anywhere}.transport-panel p{max-width:40rem}.transport-panel#transport-car p{max-width:31rem;white-space:normal;overflow-wrap:anywhere}.transport-panel[hidden]{display:none}.loc-statement{background:var(--capital-black);text-align:center;padding:clamp(6rem,13vw,11rem) 0}.loc-statement h2{max-width:900px;margin:0 auto;color:var(--warm-ivory);font:300 clamp(2.5rem,7vw,6.5rem)/.94 var(--serif)}.loc-statement h2 em{color:var(--gold);font-style:italic}.loc-statement p{color:rgba(242,238,229,.56);font:15px/1.7 var(--sans);max-width:35rem;margin:1.5rem auto 0}.loc-cta{background:linear-gradient(135deg,rgba(38,53,46,.66),var(--bg2));text-align:center}.loc-cta .section-title{max-width:700px;margin:auto}.loc-cta p{color:rgba(242,238,229,.6);font:15px/1.7 var(--sans);max-width:34rem;margin:1rem auto 0}.loc-cta-actions{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:wrap;margin-top:2rem}
@media(max-width:767px){.loc-metric-grid,.loc-category-grid{grid-template-columns:1fr}.loc-directory{grid-template-columns:1fr}.loc-metro-stats{grid-template-columns:1fr 1fr}.loc-map-stage{min-height:380px}.map-detail{display:block}.map-detail a{display:inline-block;margin-top:.7rem}.arrival-steps{grid-template-columns:repeat(5,1fr);gap:.25rem}.arrival-step{font-size:7px;letter-spacing:.05em}.loc-v2-hero .page-header-actions{flex-direction:column;align-items:stretch}.loc-v2-hero .page-header-actions a{text-align:center}}
@media(prefers-reduced-motion:reduce){.map-pin,.loc-category,.loc-filter,.transport-tab{transition:none}}
</style>"""

loc_body = """<div class="page-header loc-v2-hero" style="--hero-position:center 42%;background-image:url(assets/images/feedback/location-generated.jpg);background-position:center 42%">
  <img class="page-header-media" src="assets/images/feedback/location-generated.jpg" alt="Capital Place and the Hanoi skyline" fetchpriority="high" />
  <div class="container">
    <p class="page-header-eyebrow">Location</p>
    <h1>At the heart<br><em>of Hanoi</em></h1>
    <p>A premier business address at the centre of Hanoi's diplomatic and commercial hub.</p>
    <p class="hero-location">29 Lieu Giai · Ngoc Ha · Hanoi</p>
    <div class="page-header-actions"><a class="btn-gold" href="#the-address">Explore the Area <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div>
  </div>
</div>
<section id="the-address" class="loc-v2-section" aria-labelledby="address-title"><div class="container"><div class="loc-address-grid"><div class="loc-address-copy"><p class="eyebrow">The Address</p><h2 id="address-title" class="section-title">29 <em>Lieu Giai</em></h2><p>Capital Place stands at 29 Lieu Giai, Ngoc Ha — within one of Hanoi's established commercial and diplomatic districts.</p><div class="loc-address-block"><span>29 Lieu Giai</span><span>Ngoc Ha</span><span>Hanoi, Vietnam</span></div></div><div class="loc-address-visual"><iframe title="Capital Place location at 29 Lieu Giai" src="https://www.google.com/maps?q=Capital+Place+29+Lieu+Giai+Hanoi&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><span class="loc-map-caption">29 LIEU GIAI · NGOC HA · HANOI</span></div></div></div></section>
<section class="loc-v2-section alt" aria-labelledby="reach-title"><div class="container"><div class="loc-reach-head"><div><p class="eyebrow">The City, Within Reach</p><h2 id="reach-title" class="section-title">Connected to <em>what matters</em></h2></div><p>Strategically positioned to connect businesses with Hanoi's key commercial, diplomatic and cultural destinations.</p></div><div class="loc-metric-grid" role="list"><div class="loc-metric" role="listitem"><span class="loc-metric-value">05</span><span class="loc-metric-label">West Lake</span><span class="loc-metric-note">Approximate travel time</span></div><div class="loc-metric" role="listitem"><span class="loc-metric-value">10</span><span class="loc-metric-label">Hoan Kiem</span><span class="loc-metric-note">Approximate travel time</span></div><div class="loc-metric" role="listitem"><span class="loc-metric-value">30</span><span class="loc-metric-label">Noi Bai Airport</span><span class="loc-metric-note">Approximate travel time via Nhat Tan Bridge</span></div></div></div></section>
<section class="loc-v2-section loc-metro" aria-labelledby="metro-title"><div class="container"><div class="loc-metro-grid"><div class="loc-metro-copy"><p class="eyebrow">Direct MRT Access</p><h2 id="metro-title" class="section-title">Connected below.<br><em>Connected beyond.</em></h2><p>Capital Place connects directly to Hanoi's metro network through an underground pedestrian tunnel, creating seamless access to the city.</p><div class="loc-metro-stats"><div class="loc-metro-stat"><strong>10</strong><span>Trainsets in service</span></div><div class="loc-metro-stat"><strong>12</strong><span>Metro stations</span></div><div class="loc-metro-stat"><strong>05</strong><span>Districts connected</span></div><div class="loc-metro-stat"><strong>20,000</strong><span>Hourly commuters</span></div></div></div></div></div></section>
<section class="loc-v2-section loc-surroundings" aria-labelledby="surroundings-title"><div class="container"><p class="eyebrow">Your World, Within Reach</p><h2 id="surroundings-title" class="section-title">Business, hospitality,<br><em>life in full</em></h2><p class="loc-section-intro">Business, hospitality, diplomacy, culture and lifestyle — all within easy reach.</p><div class="loc-filter-row" role="group" aria-label="Filter surroundings directory"><button type="button" class="loc-filter active" data-loc-filter="all" onclick="filterLocationCards('all')">All</button><button type="button" class="loc-filter" data-loc-filter="business" onclick="filterLocationCards('business')">Business</button><button type="button" class="loc-filter" data-loc-filter="diplomatic" onclick="filterLocationCards('diplomatic')">Diplomatic</button><button type="button" class="loc-filter" data-loc-filter="hospitality" onclick="filterLocationCards('hospitality')">Hospitality</button><button type="button" class="loc-filter" data-loc-filter="dining" onclick="filterLocationCards('dining')">Dining</button><button type="button" class="loc-filter" data-loc-filter="retail" onclick="filterLocationCards('retail')">Retail</button><button type="button" class="loc-filter" data-loc-filter="culture" onclick="filterLocationCards('culture')">Culture</button></div><div class="loc-directory" id="surroundings-directory"><article class="loc-card" data-loc-category="business"><div class="loc-card-visual" style="background-image:url(assets/images/feedback/fb4-card-1.jpg)"></div><div class="loc-card-content"><span class="loc-card-category">Business</span><h3>Hanoi's commercial hub</h3><p class="loc-card-meta">Enterprise, finance and opportunity</p></div></article><article class="loc-card" data-loc-category="diplomatic"><div class="loc-card-visual" style="background-image:url(assets/images/feedback/fb4-card-2.jpg)"></div><div class="loc-card-content"><span class="loc-card-category">Diplomatic</span><h3>Embassy district</h3><p class="loc-card-meta">International missions and institutions</p></div></article><article class="loc-card" data-loc-category="hospitality"><div class="loc-card-visual" style="background-image:url(assets/images/feedback/fb4-card-3.jpg)"></div><div class="loc-card-content"><span class="loc-card-category">Hospitality</span><h3>Five-star stays</h3><p class="loc-card-meta">Hospitality and premium service</p></div></article><article class="loc-card" data-loc-category="dining"><div class="loc-card-visual" style="background-image:url(assets/images/feedback/fb4-card-4.jpg)"></div><div class="loc-card-content"><span class="loc-card-category">Dining</span><h3>Hanoi after hours</h3><p class="loc-card-meta">Restaurants, cafés and city life</p></div></article><article class="loc-card" data-loc-category="retail"><div class="loc-card-visual" style="background-image:url(assets/images/feedback/fb4-card-5.jpg)"></div><div class="loc-card-content"><span class="loc-card-category">Retail</span><h3>Everyday convenience</h3><p class="loc-card-meta">Shopping and essential services</p></div></article><article class="loc-card" data-loc-category="culture"><div class="loc-card-visual" style="background-image:url(assets/images/feedback/fb4-card-6.jpg)"></div><div class="loc-card-content"><span class="loc-card-category">Culture</span><h3>Landmarks of Hanoi</h3><p class="loc-card-meta">Lakes, heritage and cultural destinations</p></div></article></div></div></section>
<section class="loc-v2-section" aria-labelledby="business-title"><div class="container"><div class="loc-business"><div class="loc-business-copy"><p class="eyebrow">Business &amp; Diplomacy</p><h2 id="business-title" class="section-title">Where business<br><em>meets diplomacy</em></h2><p>Positioned among embassies, international enterprises, premium hospitality and Hanoi's established commercial destinations.</p></div><div class="loc-business-visual" role="img" aria-label="Capital Place within Hanoi's business and diplomatic district"></div></div></div></section>
<section class="loc-v2-section alt" aria-labelledby="lifestyle-title"><div class="container"><div class="loc-lifestyle-copy"><p class="eyebrow">Hospitality &amp; Lifestyle</p><h2 id="lifestyle-title" class="section-title">The city <em>after work</em></h2><p>From five-star hospitality and dining to retail, culture and entertainment, Hanoi unfolds around Capital Place.</p></div><div class="loc-category-grid" role="list"><button type="button" class="loc-category active" role="listitem" onclick="filterLocationCards('hospitality');document.getElementById('surroundings-directory').scrollIntoView({behavior:'smooth'})"><strong>Hospitality</strong><span>Five-star stays and service</span></button><button type="button" class="loc-category" role="listitem" onclick="filterLocationCards('dining');document.getElementById('surroundings-directory').scrollIntoView({behavior:'smooth'})"><strong>Dining</strong><span>Restaurants and cafés</span></button><button type="button" class="loc-category" role="listitem" onclick="filterLocationCards('retail');document.getElementById('surroundings-directory').scrollIntoView({behavior:'smooth'})"><strong>Retail</strong><span>Shopping and convenience</span></button><button type="button" class="loc-category" role="listitem" onclick="filterLocationCards('culture');document.getElementById('surroundings-directory').scrollIntoView({behavior:'smooth'})"><strong>Culture</strong><span>Landmarks and heritage</span></button></div></div></section>
<section class="loc-v2-section loc-landmarks" aria-labelledby="landmarks-title"><div class="container"><p class="eyebrow">The Landmarks</p><h2 id="landmarks-title" class="section-title">Hanoi, <em>within reach</em></h2><div class="loc-landmark-scroller" aria-label="Hanoi landmark gallery"><div class="loc-landmark" style="background-image:linear-gradient(180deg,rgba(17,17,17,.05),rgba(17,17,17,.92)),url(assets/images/feedback/fb4-west-lake.jpg);background-position:center;background-size:cover"><span>West Lake</span></div><div class="loc-landmark" style="background-image:linear-gradient(180deg,rgba(17,17,17,.05),rgba(17,17,17,.92)),url(assets/images/feedback/fb4-hoan-kiem.jpg);background-position:center;background-size:cover"><span>Hoan Kiem</span></div><div class="loc-landmark" style="background-image:linear-gradient(180deg,rgba(17,17,17,.05),rgba(17,17,17,.92)),url(assets/images/feedback/fb4-old-quarter.jpg);background-position:center;background-size:cover"><span>Old Quarter</span></div><div class="loc-landmark" style="background-image:linear-gradient(180deg,rgba(17,17,17,.05),rgba(17,17,17,.92)),url(assets/images/feedback/fb4-cultural.jpg);background-position:center;background-size:cover"><span>Cultural Landmarks</span></div><div class="loc-landmark"><span>Retail Destinations</span></div></div></div></section>
<section class="loc-v2-section loc-map-section" aria-labelledby="map-title"><div class="container"><p class="eyebrow">Explore the Neighbourhood</p><h2 id="map-title" class="section-title">See what <em>surrounds you</em></h2><div class="loc-filter-row" role="group" aria-label="Filter interactive map"><button type="button" class="loc-filter active" data-map-filter="all" onclick="filterMapPins('all')">All</button><button type="button" class="loc-filter" data-map-filter="business" onclick="filterMapPins('business')">Business</button><button type="button" class="loc-filter" data-map-filter="diplomatic" onclick="filterMapPins('diplomatic')">Embassies</button><button type="button" class="loc-filter" data-map-filter="hospitality" onclick="filterMapPins('hospitality')">Hotels</button><button type="button" class="loc-filter" data-map-filter="dining" onclick="filterMapPins('dining')">Dining</button><button type="button" class="loc-filter" data-map-filter="retail" onclick="filterMapPins('retail')">Retail</button><button type="button" class="loc-filter" data-map-filter="culture" onclick="filterMapPins('culture')">Culture</button><button type="button" class="loc-filter" data-map-filter="metro" onclick="filterMapPins('metro')">Metro</button></div><div class="loc-map-stage" role="region" aria-label="Interactive location map"><div class="map-road map-road-main"></div><div class="map-road map-road-secondary"></div><span class="map-label map-label-north">Ba Dinh</span><span class="map-label map-label-west">West Lake</span><span class="map-label map-label-east">Embassy district</span><span class="map-label map-label-south">Hoan Kiem</span><div class="loc-map-legend"><span>Neighbourhood guide</span><span>Capital Place · 29 Lieu Giai</span></div><button type="button" class="map-pin capital active" data-map-category="business" data-label="Capital Place" aria-label="Capital Place" onclick="selectMapPin(this,'Capital Place','Business address','29 Lieu Giai · Hanoi','At the heart of the district')"></button><button type="button" class="map-pin west" data-map-category="culture" data-label="West Lake" aria-label="West Lake" onclick="selectMapPin(this,'West Lake','Culture & lifestyle','Approx. 5 min','A landmark within easy reach')"></button><button type="button" class="map-pin hotel" data-map-category="hospitality" data-label="Hotel" aria-label="Hospitality district" onclick="selectMapPin(this,'Hospitality district','Hospitality','Within the district','Five-star stays and service')"></button><button type="button" class="map-pin retail" data-map-category="retail" data-label="Retail" aria-label="Retail destinations" onclick="selectMapPin(this,'Retail destinations','Retail','Within the district','Shopping and everyday convenience')"></button><button type="button" class="map-pin embassy" data-map-category="diplomatic" data-label="Embassy" aria-label="Embassy district" onclick="selectMapPin(this,'Embassy district','Diplomatic','Within the district','International missions and institutions')"></button><button type="button" class="map-pin dining" data-map-category="dining" data-label="Dining" aria-label="Dining destinations" onclick="selectMapPin(this,'Dining destinations','Dining','Within the district','Restaurants, cafés and city life')"></button><button type="button" class="map-pin hoankiem" data-map-category="culture" data-label="Hoan Kiem" aria-label="Hoan Kiem" onclick="selectMapPin(this,'Hoan Kiem','Culture & heritage','Approx. 10 min','Hanoi's historic centre')"></button><div class="map-detail" id="map-detail" aria-live="polite"><div><h3 id="map-detail-title">Capital Place</h3><p id="map-detail-meta">Business address · 29 Lieu Giai · Hanoi</p><p id="map-detail-copy">At the heart of the district</p></div><a href="https://www.google.com/maps/search/?api=1&amp;query=Capital+Place+29+Lieu+Giai+Hanoi" target="_blank" rel="noopener">Explore</a></div></div></div></section>
<section class="loc-v2-section" aria-labelledby="arrival-title"><div class="container"><div class="loc-arrival"><div class="loc-arrival-copy"><p class="eyebrow">A Great Arrival</p><h2 id="arrival-title" class="section-title">Arrive with <em>distinction</em></h2><p>From the city street to the building entrance, every arrival is designed to feel seamless.</p><div class="arrival-steps" aria-label="Arrival sequence"><span class="arrival-step">City</span><span class="arrival-step">Street</span><span class="arrival-step">Drop-off</span><span class="arrival-step">Lobby</span><span class="arrival-step">Office</span></div></div><div class="loc-arrival-visual" role="img" aria-label="Capital Place arrival experience from street to lobby"></div></div></div></section>
<section class="loc-v2-section loc-transport" aria-labelledby="transport-title"><div class="container"><p class="eyebrow">Location by Transport</p><h2 id="transport-title" class="section-title">Getting <em>here</em></h2><div class="transport-tabs" role="tablist" aria-label="Getting to Capital Place"><button type="button" role="tab" class="transport-tab active" aria-selected="true" aria-controls="transport-car" data-transport-tab="car" onclick="setTransport('car')">Car</button><button type="button" role="tab" class="transport-tab" aria-selected="false" aria-controls="transport-metro" data-transport-tab="metro" onclick="setTransport('metro')">Metro</button><button type="button" role="tab" class="transport-tab" aria-selected="false" aria-controls="transport-taxi" data-transport-tab="taxi" onclick="setTransport('taxi')">Taxi / Ride-hailing</button><button type="button" role="tab" class="transport-tab" aria-selected="false" aria-controls="transport-airport" data-transport-tab="airport" onclick="setTransport('airport')">Airport</button></div><div class="transport-panel" id="transport-car" role="tabpanel"><h3>Road access from the city's major arteries.</h3><p>Approach Capital Place via the established routes around Ba Dinh and Lieu Giai.</p></div><div class="transport-panel" id="transport-metro" role="tabpanel" hidden><h3>Direct MRT access via underground connection.</h3><p>A seamless pedestrian link connects the building with Hanoi's metro network.</p></div><div class="transport-panel" id="transport-taxi" role="tabpanel" hidden><h3>Dedicated arrival and drop-off experience.</h3><p>Arrive from the city street into a considered, welcoming building entrance.</p></div><div class="transport-panel" id="transport-airport" role="tabpanel" hidden><h3>Approximately 30 minutes to Noi Bai International Airport.</h3><p>Travel time is approximate and depends on traffic and route conditions.</p></div></div></section>
<section class="loc-statement" aria-labelledby="statement-title"><div class="container"><h2 id="statement-title">A location that <em>works for business</em></h2><p>Connected to the city. Close to opportunity. Positioned for the future.</p></div></section>
<section class="loc-v2-section loc-cta" aria-labelledby="location-cta-title"><div class="container"><p class="eyebrow">Capital Place Hanoi</p><h2 id="location-cta-title" class="section-title">Come to <em>Capital Place</em></h2><p>Discover a premier business address in the heart of Hanoi.</p><div class="loc-cta-actions"><a class="btn-gold" href="https://www.google.com/maps/search/?api=1&amp;query=Capital+Place+29+Lieu+Giai+Hanoi" target="_blank" rel="noopener">Get Directions <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a><a class="btn-outline-gold" href="amenities.html#leasing">Enquire</a></div></div></section>
<script>
function filterLocationCards(category){document.querySelectorAll('[data-loc-filter]').forEach(btn=>btn.classList.toggle('active',btn.dataset.locFilter===category));document.querySelectorAll('[data-loc-category]').forEach(card=>{card.hidden=category!=='all'&&card.dataset.locCategory!==category})}
function filterMapPins(category){document.querySelectorAll('[data-map-filter]').forEach(btn=>btn.classList.toggle('active',btn.dataset.mapFilter===category));document.querySelectorAll('.map-pin').forEach(pin=>{pin.hidden=category!=='all'&&pin.dataset.mapCategory!==category})}
function selectMapPin(pin,title,meta,distance,copy){document.querySelectorAll('.map-pin').forEach(item=>item.classList.remove('active'));pin.classList.add('active');const t=document.getElementById('map-detail-title'),m=document.getElementById('map-detail-meta'),d=document.getElementById('map-detail-copy');if(t)t.textContent=title;if(m)m.textContent=meta+' · '+distance;if(d)d.textContent=copy}
function setTransport(tab){document.querySelectorAll('[data-transport-tab]').forEach(btn=>{const active=btn.dataset.transportTab===tab;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',active?'true':'false')});document.querySelectorAll('.transport-panel').forEach(panel=>{panel.hidden=panel.id!=='transport-'+tab})}
</script>"""

# ══════════════════════════════════
# office.html
# ══════════════════════════════════
def make_svg(fid):
    G = fid == 'ground'
    S = fid == 'sky'
    ticks_n = ''.join(f'<line x1="{44+i*17}" y1="24" x2="{44+i*17}" y2="30" stroke="#B89B5E" stroke-width=".6" stroke-opacity=".6"/>' for i in range(24))
    ticks_s = ''.join(f'<line x1="{44+i*17}" y1="310" x2="{44+i*17}" y2="316" stroke="#B89B5E" stroke-width=".6" stroke-opacity=".6"/>' for i in range(24))
    ticks_w = ''.join(f'<line x1="24" y1="{44+i*17}" x2="30" y2="{44+i*17}" stroke="#B89B5E" stroke-width=".6" stroke-opacity=".6"/>' for i in range(16))
    ticks_e = ''.join(f'<line x1="450" y1="{44+i*17}" x2="456" y2="{44+i*17}" stroke="#B89B5E" stroke-width=".6" stroke-opacity=".6"/>' for i in range(16))
    cg = ''.join(f'<line x1="{x}" y1="24" x2="{x}" y2="316" stroke="#B89B5E" stroke-width=".5" stroke-opacity=".07" stroke-dasharray="4 5"/>' for x in [132,240,348])
    rg = ''.join(f'<line x1="24" y1="{y}" x2="456" y2="{y}" stroke="#B89B5E" stroke-width=".5" stroke-opacity=".07" stroke-dasharray="4 5"/>' for y in [120,196,268])
    core = '' if G else '<rect x="172" y="108" width="136" height="124" fill="#2F2D29" stroke="#B89B5E" stroke-width=".9"/>'
    lifts = '' if G or S else ''.join(f'<g><rect x="{185+i*18}" y="120" width="14" height="18" fill="#1c1c18" stroke="#B89B5E" stroke-width=".5"/><line x1="{186+i*18}" y1="121" x2="{198+i*18}" y2="137" stroke="#B89B5E" stroke-width=".4" stroke-opacity=".35"/><line x1="{198+i*18}" y1="121" x2="{186+i*18}" y2="137" stroke="#B89B5E" stroke-width=".4" stroke-opacity=".35"/></g>' for i in range(6))
    stairs = '' if G or S else '<rect x="178" y="153" width="22" height="26" fill="#1c1c18" stroke="#B89B5E" stroke-width=".5"/><rect x="280" y="153" width="22" height="26" fill="#1c1c18" stroke="#B89B5E" stroke-width=".5"/>'
    lbl = '' if G or S else '<text x="240" y="175" text-anchor="middle" fill="#242321" font-size="7" letter-spacing="2.5" font-family="sans-serif">CORE</text>'
    sp = ''
    if G: sp = '<rect x="176" y="130" width="128" height="8" rx="4" fill="none" stroke="#B89B5E" stroke-width=".8"/><rect x="196" y="148" width="88" height="44" fill="#2F2D29" stroke="#B89B5E" stroke-width=".8"/><text x="240" y="175" text-anchor="middle" fill="#242321" font-size="7" letter-spacing="2" font-family="sans-serif">RECEPTION</text>'
    if S: sp = '<ellipse cx="240" cy="170" rx="80" ry="60" fill="none" stroke="#B89B5E" stroke-width=".7" stroke-opacity=".25" stroke-dasharray="5 4"/><text x="240" y="174" text-anchor="middle" fill="#242321" font-size="7.5" letter-spacing="2" font-family="sans-serif">SKY LOUNGE</text>'
    return f'<svg viewBox="0 0 480 340" style="width:100%;height:auto;max-height:280px"><rect x="24" y="24" width="432" height="292" fill="none" stroke="#B89B5E" stroke-width="1.2"/>{ticks_n}{ticks_s}{ticks_w}{ticks_e}{cg}{rg}{core}{lifts}{stairs}{sp}{lbl}<text x="240" y="15" text-anchor="middle" fill="#242321" font-size="7.5" letter-spacing="2" font-family="sans-serif">N</text><text x="240" y="332" text-anchor="middle" fill="#242321" font-size="7.5" letter-spacing="2" font-family="sans-serif">S</text><text x="12" y="173" text-anchor="middle" fill="#242321" font-size="7.5" letter-spacing="2" font-family="sans-serif">W</text><text x="465" y="173" text-anchor="middle" fill="#242321" font-size="7.5" letter-spacing="2" font-family="sans-serif">E</text><g transform="translate(440,48)"><line x1="0" y1="12" x2="0" y2="-8" stroke="#B89B5E" stroke-width=".8"/><polygon points="0,-10 -5,-2 5,-2" fill="#B89B5E"/></g><g transform="translate(32,308)"><line x1="0" y1="0" x2="68" y2="0" stroke="#B89B5E" stroke-width=".8" stroke-opacity=".5"/><line x1="0" y1="-4" x2="0" y2="4" stroke="#B89B5E" stroke-width=".8" stroke-opacity=".5"/><line x1="68" y1="-4" x2="68" y2="4" stroke="#B89B5E" stroke-width=".8" stroke-opacity=".5"/><text x="34" y="-7" text-anchor="middle" fill="#242321" font-size="6.5" letter-spacing="1" font-family="sans-serif">20 m</text></g></svg>'

FLOORS = [
    {"id":"ground","label":"Arrival & Retail","range":"B3 · B1 · Level 1","tower":"Shared podium","use":"Three basement levels · Retail · Arrival","note":"The project includes three basement levels; the section diagram marks Level 1 as retail."},
    {"id":"podium","label":"Lower Office Band","range":"Levels 2 · 6","tower":"Tower 1 · Tower 2","use":"Office floors across the lower podium","note":"The lower office band sits above the retail level in both towers."},
    {"id":"lo","label":"Lower Office Floors","range":"7F · 19F","tower":"Tower 1 · Tower 2","use":"Grade-A office floors","note":"Both towers are shown with office floors from 7F through 19F."},
    {"id":"hi","label":"Upper Office Floors","range":"20F · 37F","tower":"Tower 1 · Tower 2","use":"Upper office floors","note":"The upper office band rises from 20F to 37F in both towers."},
]

def floor_panels():
    out = ''
    for i, f in enumerate(FLOORS):
        active = ' active' if i == 2 else ''
        rows = ''.join(f'<div class="spec-row"><span class="spec-key">{k}</span><span class="spec-val">{v}</span></div>' for k, v in [("Tower",f["tower"]),("Level band",f["range"]),("Function",f["use"]),("Reference",f["note"])])
        out += f'<div class="floor-panel{active}" id="floor-panel-{i}" data-fi="{i}" role="tabpanel" aria-labelledby="floor-tab-{i}"><div class="svg-box">{make_svg(f["id"])}</div><div class="floor-specs"><div class="floor-spec-hd"><span class="eyebrow">{f["range"]}</span><h3>{f["label"]}</h3></div><div class="spec-table">{rows}</div><a href="amenities.html#leasing" class="btn-outline-gold floor-plan-cta">Request Floor Plan<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div></div>'
    return out


def floor_btns():
    out = ''
    for i, f in enumerate(FLOORS):
        active = ' active' if i == 2 else ' inactive'
        selected = 'true' if i == 2 else 'false'
        out += f'<button type="button" class="floor-btn{active}" id="floor-tab-{i}" role="tab" aria-selected="{selected}" aria-controls="floor-panel-{i}" onclick="setFloor({i})"><span class="floor-range">{f["range"]}</span><span class="floor-lbl">{f["label"]}</span></button>'
    return out


STACK_LEVELS = [37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,"B1","B2","B3"]

def stacking_plan():
    rows = ''
    for level in STACK_LEVELS:
        label = f'{level}F' if isinstance(level, int) else level
        if level == 20:
            marker = '<span class="stack-zone stack-technical">Technical</span>'
        elif isinstance(level, int) and level >= 21:
            marker = '<span class="stack-zone stack-high">High zone</span>'
        elif isinstance(level, int) and level >= 7:
            marker = '<span class="stack-zone stack-low">Low zone</span>'
        elif level == 1:
            marker = '<span class="stack-zone stack-retail">Retail / arrival</span>'
        else:
            marker = '<span class="stack-zone stack-podium">Podium / basement</span>'
        key = str(level).lower().replace('f','')
        zone = 'High' if isinstance(level, int) and level >= 21 else 'Low' if isinstance(level, int) and level >= 7 else 'Podium'
        area_one = '1,329 m²' if level == 24 else 'Available on request'
        area_two = 'Available on request'
        rows += f'<div class="stack-row"><button type="button" class="stack-floor stack-floor-one" data-level="{label}" data-zone="{key}" aria-label="Tower 01 {label}" onclick="openFloorDetail(\'Tower 01\',\'{label}\',\'{zone}\',\'{area_one}\')">{label}</button>{marker}<button type="button" class="stack-floor stack-floor-two" data-level="{label}" data-zone="{key}" aria-label="Tower 02 {label}" onclick="openFloorDetail(\'Tower 02\',\'{label}\',\'{zone}\',\'{area_two}\')">{label}</button></div>'
    return f'<div class="stack-tower-head"><span>Tower 01</span><span>Stacking plan</span><span>Tower 02</span></div><div class="stack-rows">{rows}</div>'


def explorer_levels():
    out = ''
    for level in list(range(37, 20, -1)) + list(range(19, 6, -1)):
        zone = 'high' if level >= 21 else 'low'
        active = ' active' if level == 24 else ''
        area = '1,329 m²' if level == 24 else 'Available on request'
        out += f'<button type="button" class="floor-option{active}" data-tower="Tower 01" data-zone="{zone}" data-level="L{level}" data-area="{area}" aria-pressed="{str(level == 24).lower()}" onclick="selectExplorerFloor(this)"><span>L{level}</span><small>{zone.title()}</small></button>'
    return out

off_css = """<style>
.office-v2-hero .page-header-media{object-position:center 55%}@media(min-width:900px){.office-v2-hero>.container{transform:translateX(-200px)}.office-column-free .column-free-copy>.eyebrow{transform:translateY(-16px)}.office-features-v2 .feature-scroll .feature-card-v2:nth-child(4) h3{transform:translateY(-24px)}}
.office-v2-hero .page-header-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.7rem}
.office-v2-hero .page-header-actions .btn-gold,.office-v2-hero .page-header-actions .btn-outline-gold{font-size:10px;letter-spacing:.22em}
.office-v2-section{padding:clamp(5.5rem,11vw,9rem) 0;border-top:1px solid var(--gold-b)}
.office-v2-overview{background:var(--bg)}
.office-v2-split{display:grid;gap:3rem;align-items:end}
@media(min-width:900px){.office-v2-split{grid-template-columns:1fr 1fr;gap:6rem}}
.office-v2-copy{color:rgba(242,238,229,.64);font-size:15px;line-height:1.8;max-width:36rem;margin-top:1.5rem}
.office-v2-diagram{margin-top:4rem;border:1px solid var(--gold-b);background:var(--warm-ivory);padding:clamp(.5rem,2vw,1rem)}
.office-v2-diagram img{display:block;width:100%;height:auto;filter:saturate(.78) contrast(.98)}
.office-v2-diagram figcaption{font:9px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--deep-gold);padding:.85rem .35rem .15rem}
.office-numbers{background:var(--graphite);}
.office-number-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(214,192,138,.22);margin-top:3.5rem}
@media(min-width:900px){.office-number-grid{grid-template-columns:repeat(4,1fr)}}
.office-number{background:var(--graphite);padding:clamp(1.6rem,3vw,2.5rem) 1.25rem;min-height:150px;display:flex;flex-direction:column;justify-content:space-between}
.office-number-value{font:300 clamp(2.2rem,5vw,4.2rem)/.95 var(--serif);color:var(--gold);letter-spacing:-.03em}
.office-number-label{font:10px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--warm-ivory);line-height:1.5}
.office-number-note{font:12px var(--sans);color:rgba(242,238,229,.48);line-height:1.5;margin-top:.5rem}
.office-stacking{background:var(--bg2)}
.office-stacking-intro{max-width:42rem}
.office-stacking-intro p:not(.eyebrow){color:rgba(242,238,229,.58);font-size:14px;line-height:1.8;margin-top:1.4rem}
.stack-shell{margin-top:3.5rem;border:1px solid var(--gold-b);background:linear-gradient(180deg,rgba(38,53,46,.2),transparent 30%),var(--bg);padding:1rem}
.stack-tower-head{display:grid;grid-template-columns:1fr 1.8fr 1fr;align-items:center;border-bottom:1px solid var(--gold-b);padding:.8rem .4rem;color:var(--gold-champagne);font:10px var(--sans);letter-spacing:.25em;text-transform:uppercase;text-align:center}
.stack-tower-head span:nth-child(2){color:rgba(242,238,229,.38);font-size:9px}
.stack-rows{max-height:600px;overflow:auto;scrollbar-color:var(--gold-deep) transparent}
.stack-row{display:grid;grid-template-columns:1fr 1.8fr 1fr;min-height:30px;border-bottom:1px solid rgba(214,192,138,.1);align-items:center}
.stack-floor{border:0;background:transparent;color:rgba(242,238,229,.62);font:12px var(--sans);letter-spacing:.12em;padding:.45rem .25rem;cursor:pointer;transition:color .2s,background .2s}
.stack-floor:hover,.stack-floor:focus-visible{color:var(--warm-ivory);background:rgba(184,155,94,.16);outline:none}
.stack-zone{text-align:center;font:9px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:rgba(242,238,229,.32)}
.stack-high{color:var(--gold-champagne)}.stack-technical{color:var(--gold)}.stack-low{color:var(--green)}.stack-retail{color:var(--stone)}
.office-explorer{background:var(--bg)}
.office-explorer-head{display:grid;gap:2rem;align-items:end}
@media(min-width:900px){.office-explorer-head{grid-template-columns:1fr 1fr;gap:5rem}}
.office-explorer-head p:not(.eyebrow){color:rgba(242,238,229,.58);font-size:14px;line-height:1.8;margin-top:1.25rem}
.explorer-shell{display:grid;gap:1.5rem;margin-top:3.5rem}
@media(min-width:1024px){.explorer-shell{grid-template-columns:260px 1fr;gap:2.5rem}}
.explorer-controls{border-top:1px solid var(--gold-b)}
.explorer-control-group{display:flex;gap:.5rem;border-bottom:1px solid var(--gold-b);padding:.8rem 0}
.explorer-control{flex:1;border:1px solid transparent;background:transparent;color:rgba(242,238,229,.45);padding:.7rem .45rem;font:10px var(--sans);letter-spacing:.17em;text-transform:uppercase;cursor:pointer;transition:all .25s}
.explorer-control.active,.explorer-control:hover,.explorer-control:focus-visible{border-color:var(--gold);color:var(--warm-ivory);background:rgba(184,155,94,.12);outline:none}
.floor-options{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--gold-b);margin-top:1rem;max-height:420px;overflow:auto}
.floor-option{display:flex;align-items:baseline;justify-content:space-between;gap:.5rem;border:0;background:var(--bg2);color:rgba(242,238,229,.48);padding:.8rem .7rem;text-align:left;cursor:pointer;transition:all .2s}
.floor-option span{font:16px var(--serif)}.floor-option small{font:9px var(--sans);letter-spacing:.12em;text-transform:uppercase}
.floor-option.active,.floor-option:hover,.floor-option:focus-visible{background:var(--gold);color:var(--capital-black);outline:none}
.floor-option[data-zone="high"] small{color:var(--gold-champagne)}.floor-option.active small{color:var(--capital-black)}
.explorer-detail{display:grid;gap:1.5rem;align-items:stretch}
@media(min-width:768px){.explorer-detail{grid-template-columns:1.08fr .92fr}}
.floor-plan-preview{border:1px solid var(--gold-b);background:var(--warm-ivory);padding:1rem;min-height:280px;display:flex;align-items:center;justify-content:center}
.floor-plan-preview svg{width:100%;max-height:300px}
.floor-plan-caption{font:9px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--deep-gold);margin-top:-.75rem;background:var(--warm-ivory);padding:0 1.35rem .6rem}
.floor-detail-card{border:1px solid var(--gold-b);background:var(--graphite);padding:clamp(1.5rem,4vw,2.5rem);display:flex;flex-direction:column;justify-content:space-between}
.floor-detail-kicker{color:var(--gold-champagne);font:10px var(--sans);letter-spacing:.3em;text-transform:uppercase}
.floor-detail-title{color:var(--warm-ivory);font:300 clamp(2rem,4vw,3.4rem)/1 var(--serif);margin:.8rem 0}
.floor-detail-area{color:var(--gold);font:300 clamp(1.7rem,3vw,2.5rem) var(--serif)}
.floor-detail-meta{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--gold-b);margin:1.8rem 0}
.floor-meta-item{background:var(--graphite);padding:.85rem .7rem}.floor-meta-item span{display:block}.floor-meta-key{font:9px var(--sans);letter-spacing:.15em;text-transform:uppercase;color:rgba(242,238,229,.38)}.floor-meta-value{font:13px var(--sans);color:var(--warm-ivory);margin-top:.35rem}
.office-column-free{background:var(--graphite);overflow:hidden}
.column-free-grid{display:grid;gap:2.5rem;align-items:center}
@media(min-width:900px){.column-free-grid{grid-template-columns:.8fr 1.2fr;gap:5rem}}
.column-free-copy p:not(.eyebrow){color:rgba(242,238,229,.6);font-size:14px;line-height:1.8;max-width:32rem;margin-top:1.35rem}
.grid-visual{position:relative;min-height:320px;border:1px solid var(--gold-b);background:linear-gradient(90deg,transparent 49.8%,rgba(214,192,138,.42) 50%,transparent 50.2%),linear-gradient(0deg,transparent 49.8%,rgba(214,192,138,.42) 50%,transparent 50.2%),repeating-linear-gradient(90deg,rgba(242,238,229,.1) 0 1px,transparent 1px 52px),repeating-linear-gradient(0deg,rgba(242,238,229,.1) 0 1px,transparent 1px 52px);background-color:var(--bg);display:flex;align-items:center;justify-content:center;isolation:isolate}
.grid-visual::before{content:'';position:absolute;width:42%;height:30%;border:1px solid var(--gold);background:rgba(184,155,94,.08);box-shadow:0 0 0 18px rgba(184,155,94,.04),0 0 0 36px rgba(184,155,94,.025)}
.grid-visual::after{content:'COLUMN-FREE FLOOR PLATE';position:absolute;bottom:1rem;left:1rem;color:var(--gold-champagne);font:9px var(--sans);letter-spacing:.2em}
.office-features-v2{background:var(--bg2)}
.office-feature-intro{display:flex;justify-content:space-between;gap:2rem;align-items:end}.office-feature-intro p:not(.eyebrow){max-width:26rem;color:rgba(242,238,229,.54);font-size:13px;line-height:1.7}
.office-features-v2>.container{position:relative}.feature-scroll-guide{display:flex;justify-content:space-between;align-items:center;gap:1rem;margin-top:2rem;color:var(--gold-champagne);font:9px var(--sans);letter-spacing:.22em;text-transform:uppercase}.feature-scroll-guide span:last-child{color:rgba(242,238,229,.42);letter-spacing:.14em}.feature-scroll{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(230px,31vw);gap:1px;background:var(--gold-b);overflow-x:auto;margin-top:.75rem;scroll-snap-type:x mandatory;scrollbar-width:thin;scrollbar-color:var(--gold) rgba(214,192,138,.12);scroll-behavior:smooth;padding-bottom:8px}.feature-scroll::-webkit-scrollbar{height:6px}.feature-scroll::-webkit-scrollbar-track{background:rgba(214,192,138,.12)}.feature-scroll::-webkit-scrollbar-thumb{background:var(--gold)}.feature-scroll:focus-visible{outline:1px solid var(--gold);outline-offset:6px}
@media(max-width:767px){.feature-scroll{grid-auto-columns:78vw}}
.feature-card-v2{scroll-snap-align:start;min-height:220px;background:var(--bg2);padding:1.6rem;display:flex;flex-direction:column;justify-content:space-between}.feature-card-v2 .feat-num{color:var(--gold-champagne)}.feature-card-v2 h3{color:var(--warm-ivory);font:300 1.25rem var(--serif);margin-top:2rem}.feature-card-v2 p:last-child{color:rgba(242,238,229,.5);font:13px/1.65 var(--sans);margin-top:.8rem}
.office-specs{background:var(--bg)}
.spec-accordion{display:grid;gap:1px;background:var(--gold-b);margin-top:3.5rem}.spec-accordion details{background:var(--bg2)}.spec-accordion summary{cursor:pointer;list-style:none;display:grid;grid-template-columns:48px 1fr 22px;gap:1rem;align-items:center;padding:1.25rem 1rem;color:var(--warm-ivory)}.spec-accordion summary::-webkit-details-marker{display:none}.spec-index{color:var(--gold);font:10px var(--sans);letter-spacing:.2em}.spec-label{font:14px var(--serif)}.spec-plus{color:var(--gold-champagne);font-size:20px;transition:transform .2s}.spec-accordion details[open] .spec-plus{transform:rotate(45deg)}.spec-content{padding:0 1rem 1.25rem 64px;color:rgba(242,238,229,.55);font:13px/1.8 var(--sans)}.spec-content span{display:inline-block;border:1px solid var(--gold-b);padding:.35rem .55rem;margin:.25rem .35rem .25rem 0;color:var(--warm-ivory);font-size:11px}
.office-view{background:var(--graphite)}
.view-visual{position:relative;min-height:420px;margin-top:3.5rem;background-image:linear-gradient(90deg,rgba(17,17,17,.76),rgba(17,17,17,.08)),url(assets/images/feedback/location-generated.jpg);background-size:cover;background-position:center;display:flex;align-items:end;padding:clamp(1.5rem,4vw,3rem);border:1px solid var(--gold-b)}
.view-labels{display:flex;flex-wrap:wrap;gap:.6rem 1.2rem;color:var(--warm-ivory);font:10px var(--sans);letter-spacing:.2em;text-transform:uppercase}.view-labels span{display:inline-flex;align-items:center;gap:.45rem}.view-labels span::before{content:'↓';color:var(--gold)}
.office-fitout{background:var(--bg)}
.fitout-copy{max-width:37rem;color:rgba(242,238,229,.6);font:15px/1.8 var(--sans);margin-top:1.4rem}
.office-leasing{background:linear-gradient(135deg,rgba(38,53,46,.45),var(--bg2));border-top:1px solid var(--gold-b)}
.leasing-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:2rem}
@media(max-width:767px){.office-v2-hero .page-header-actions{flex-direction:column;align-items:stretch}.office-v2-hero .page-header-actions a{text-align:center}.stack-shell{padding:.45rem}.stack-row{min-height:28px}.stack-zone{font-size:7px;letter-spacing:.04em}.stack-floor{font-size:10px}.view-visual{min-height:300px}.office-feature-intro{display:block}.office-feature-intro p:not(.eyebrow){margin-top:1rem}.floor-detail-meta{grid-template-columns:1fr 1fr}}
@media(prefers-reduced-motion:reduce){.floor-option,.stack-floor,.spec-plus{transition:none}}
</style>"""

off_body = f"""<div class="page-header office-v2-hero" style="--hero-position:center 55%;background-image:url(assets/images/feedback/office-page-header.jpg);background-position:center 55%">
  <img class="page-header-media" src="assets/images/feedback/office-page-header.jpg" alt="Capital Place twin towers rising above Hanoi" fetchpriority="high" />
  <div class="container">
    <p class="page-header-eyebrow">Office</p>
    <h1>A workplace<br><em>without limits</em></h1>
    <p>Grade A office space designed for businesses that move forward.</p>
    <div class="page-header-actions"><a class="btn-gold" href="#building-overview">Explore Office <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a><a class="btn-outline-gold" href="#floor-explorer">View Floor Plans <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div>
  </div>
</div>
<section id="building-overview" class="office-v2-section office-v2-overview" aria-labelledby="building-overview-title">
  <div class="container">
    <div class="office-v2-split"><div><p class="eyebrow">The Building</p><h2 id="building-overview-title" class="section-title">Two towers.<br><em>One destination.</em></h2></div><p class="office-v2-copy">Capital Place comprises two Grade A office towers rising 37 storeys above a shared podium, creating a large-scale workplace destination in the heart of Hanoi.</p></div>
    <figure class="office-v2-diagram"><img src="assets/images/capital-place-tower-section.png" alt="Capital Place Tower 1 and Tower 2 section diagram above a shared podium" loading="lazy" decoding="async" /><figcaption>Capital Place · two towers above a shared podium</figcaption></figure>
  </div>
</section>
<section class="office-v2-section office-numbers" aria-labelledby="office-numbers-title"><div class="container"><p class="eyebrow">By the Numbers</p><h2 id="office-numbers-title" class="section-title">Built for <em>scale</em></h2><div class="office-number-grid" role="list"><div class="office-number" role="listitem"><span class="office-number-value">93,000</span><span class="office-number-label">Leasable office &amp; retail area</span><span class="office-number-note">m²</span></div><div class="office-number" role="listitem"><span class="office-number-value">02</span><span class="office-number-label">Office towers</span></div><div class="office-number" role="listitem"><span class="office-number-value">37</span><span class="office-number-label">Storeys per tower</span></div><div class="office-number" role="listitem"><span class="office-number-value">Grade A</span><span class="office-number-label">Office building</span></div></div></div></section>
<section class="office-v2-section office-stacking" aria-labelledby="stacking-title"><div class="container"><div class="office-stacking-intro"><p class="eyebrow">Building Stacking Plan</p><h2 id="stacking-title" class="section-title">Explore the <em>building</em></h2><p>Follow the vertical relationship between Tower 01 and Tower 02, from the shared podium and retail arrival to the low and high office zones. Select any level to open its floor detail.</p></div><div class="stack-shell">{stacking_plan()}</div></div></section>
<section id="floor-explorer" class="office-v2-section office-explorer" aria-labelledby="floor-explorer-title"><div class="container"><div class="office-explorer-head"><div><p class="eyebrow">Floor Plans</p><h2 id="floor-explorer-title" class="section-title">Find your <em>space</em></h2></div><p>Explore floor plates, layouts and workplace possibilities across both towers. Detailed availability and final layouts are confirmed through the leasing team.</p></div><div class="explorer-shell"><div class="explorer-controls"><div class="explorer-control-group" role="group" aria-label="Select tower"><button type="button" class="explorer-control active" data-explorer-tower="Tower 01" aria-pressed="true" onclick="setExplorerTower('Tower 01')">Tower 01</button><button type="button" class="explorer-control" data-explorer-tower="Tower 02" aria-pressed="false" onclick="setExplorerTower('Tower 02')">Tower 02</button></div><div class="explorer-control-group" role="group" aria-label="Select floor zone"><button type="button" class="explorer-control active" data-explorer-zone="high" aria-pressed="true" onclick="setExplorerZone('high')">High</button><button type="button" class="explorer-control" data-explorer-zone="low" aria-pressed="false" onclick="setExplorerZone('low')">Low</button></div><div class="floor-options" aria-label="Select a floor">{explorer_levels()}</div></div><div class="explorer-detail"><div><div class="floor-plan-preview" aria-label="Illustrative floor plan preview">{make_svg('hi')}</div><p class="floor-plan-caption">Illustrative floor plan preview · detailed plan available on request</p></div><div class="floor-detail-card" id="floor-detail-card" aria-live="polite"><div><span class="floor-detail-kicker" data-floor-detail-kicker>Tower 01 · Level 24</span><h3 class="floor-detail-title">A floor for <em>forward thinking</em></h3><div class="floor-detail-area" data-floor-detail-area>1,329 m²</div><div class="floor-detail-meta"><div class="floor-meta-item"><span class="floor-meta-key">Leasable area</span><span class="floor-meta-value" data-floor-detail-leasable>1,329 m²</span></div><div class="floor-meta-item"><span class="floor-meta-key">Occupancy</span><span class="floor-meta-value">—</span></div><div class="floor-meta-item"><span class="floor-meta-key">Workstations</span><span class="floor-meta-value">—</span></div><div class="floor-meta-item"><span class="floor-meta-key">Meeting rooms</span><span class="floor-meta-value">—</span></div></div></div><a class="btn-gold" href="amenities.html#leasing">Enquire About This Space <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div></div></div></div></section>
<section class="office-v2-section office-column-free" aria-labelledby="column-free-title"><div class="container"><div class="column-free-grid"><div class="column-free-copy"><p class="eyebrow">Column-Free Design</p><h2 id="column-free-title" class="section-title">Space without <em>compromise</em></h2><p>Large column-free floor plates create greater freedom for workplace planning, allowing teams to shape their environment around the way they work.</p></div><div class="grid-visual" role="img" aria-label="Abstract floor grid showing an open column-free floor plate"></div></div></div></section>
<section class="office-v2-section office-features-v2" aria-labelledby="features-title"><div class="container"><div class="office-feature-intro"><div><p class="eyebrow">Workplace Features</p><h2 id="features-title" class="section-title">Engineered for <em>better work</em></h2></div><p>Technical foundations designed to support comfort, flexibility and long-term workplace performance.</p></div><div class="feature-scroll-guide" aria-hidden="true"><span>Scroll to explore</span><span>01 &mdash; 06 &rarr;</span></div><div class="feature-scroll" role="list" tabindex="0" aria-label="Scroll horizontally to explore workplace features"><article class="feature-card-v2" role="listitem"><p class="feat-num">01</p><div><h3>2.7 m Clear Height</h3><p>Generous clear height for a more open workplace environment.</p></div></article><article class="feature-card-v2" role="listitem"><p class="feat-num">02</p><div><h3>150 mm Raised Floor</h3><p>Flexible infrastructure for workplace fit-out.</p></div></article><article class="feature-card-v2" role="listitem"><p class="feat-num">03</p><div><h3>High-Speed Elevators</h3><p>32 passenger elevators serving the two towers.</p></div></article><article class="feature-card-v2" role="listitem"><p class="feat-num">04</p><div><h3>Executive Toilets</h3><p>Executive toilet and shower facilities on every floor.</p></div></article><article class="feature-card-v2" role="listitem"><p class="feat-num">05</p><div><h3>Air Purification</h3><p>Air purification system using MERV 13 filters.</p></div></article><article class="feature-card-v2" role="listitem"><p class="feat-num">06</p><div><h3>Panoramic Views</h3><p>Views toward West Lake, Lieu Giai, Thu Le Lake and Kim Ma.</p></div></article></div></div></section>
<section class="office-v2-section office-specs" aria-labelledby="specs-title"><div class="container"><p class="eyebrow">Office Specifications</p><h2 id="specs-title" class="section-title">The details <em>behind the space</em></h2><div class="spec-accordion"><details open><summary><span class="spec-index">01</span><span class="spec-label">Floor</span><span class="spec-plus">+</span></summary><div class="spec-content"><span>37 storeys</span><span>2 towers</span></div></details><details><summary><span class="spec-index">02</span><span class="spec-label">Floor Plate</span><span class="spec-plus">+</span></summary><div class="spec-content"><span>Low Zone</span><span>High Zone</span><span>Column-free design</span></div></details><details><summary><span class="spec-index">03</span><span class="spec-label">Floor System</span><span class="spec-plus">+</span></summary><div class="spec-content"><span>150 mm raised floor</span><span>2.7 m clear height</span><span>4.5 kN/m² floor loading</span></div></details><details><summary><span class="spec-index">04</span><span class="spec-label">Vertical Transport</span><span class="spec-plus">+</span></summary><div class="spec-content"><span>Passenger elevators</span><span>Service elevators</span><span>32 passenger elevators</span></div></details><details><summary><span class="spec-index">05</span><span class="spec-label">HVAC</span><span class="spec-plus">+</span></summary><div class="spec-content"><span>Centralised AC</span><span>Air purification</span><span>MERV 13 filters</span></div></details><details><summary><span class="spec-index">06</span><span class="spec-label">Power</span><span class="spec-plus">+</span></summary><div class="spec-content"><span>100% backup power</span></div></details></div></div></section>
<section class="office-v2-section office-view" aria-labelledby="view-title"><div class="container"><p class="eyebrow">The View</p><h2 id="view-title" class="section-title">See Hanoi <em>differently</em></h2><div class="view-visual"><div class="view-labels"><span>West Lake</span><span>Lieu Giai</span><span>Capital Place</span><span>Kim Ma</span><span>Thu Le Lake</span></div></div><a class="text-link" href="location.html">Explore the Location <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div></section>
<section class="office-v2-section office-fitout" aria-labelledby="fitout-title"><div class="container"><p class="eyebrow">Fit-out</p><h2 id="fitout-title" class="section-title">Make the <em>space yours</em></h2><p class="fitout-copy">A flexible foundation for businesses to create a workplace that reflects their culture, identity and operational needs. Fit-out requirements and guidelines are available through the leasing team.</p><div class="leasing-actions"><a class="btn-outline-gold" href="amenities.html#leasing">Enquire About Fit-out Guidelines <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div></div></section>
<section class="office-v2-section office-leasing" id="office-leasing" aria-labelledby="leasing-title"><div class="container"><p class="eyebrow">Leasing</p><h2 id="leasing-title" class="section-title">Find the space that <em>fits your business</em></h2><p class="fitout-copy">Explore available spaces and discover the right workplace for your business.</p><div class="leasing-actions"><a class="btn-gold" href="#floor-explorer">View Available Space <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a><a class="btn-outline-gold" href="amenities.html#leasing">Enquire <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div></div></section>"""

off_js = """<script>
let explorerTower='Tower 01';
let explorerZone='high';
function setExplorerTower(tower){explorerTower=tower;document.querySelectorAll('[data-explorer-tower]').forEach(b=>{const active=b.dataset.explorerTower===tower;b.classList.toggle('active',active);b.setAttribute('aria-pressed',active?'true':'false')});updateFloorDetail();}
function setExplorerZone(zone){explorerZone=zone;document.querySelectorAll('[data-explorer-zone]').forEach(b=>{const active=b.dataset.explorerZone===zone;b.classList.toggle('active',active);b.setAttribute('aria-pressed',active?'true':'false')});document.querySelectorAll('.floor-option').forEach(b=>{const visible=b.dataset.zone===zone;b.hidden=!visible;b.setAttribute('aria-hidden',visible?'false':'true')});const first=document.querySelector('.floor-option:not([hidden])');if(first){document.querySelectorAll('.floor-option').forEach(b=>{b.classList.remove('active');b.setAttribute('aria-pressed','false')});first.classList.add('active');first.setAttribute('aria-pressed','true')}updateFloorDetail();}
function selectExplorerFloor(button){document.querySelectorAll('.floor-option').forEach(b=>{const active=b===button;b.classList.toggle('active',active);b.setAttribute('aria-pressed',active?'true':'false')});updateFloorDetail(button.dataset.level,button.dataset.area);}
function updateFloorDetail(level,area){const selected=document.querySelector('.floor-option.active');level=level||selected?.dataset.level||'L24';area=area||selected?.dataset.area||'1,329 m²';const kicker=document.querySelector('[data-floor-detail-kicker]');const areaEl=document.querySelector('[data-floor-detail-area]');const leasable=document.querySelector('[data-floor-detail-leasable]');if(kicker)kicker.textContent=explorerTower+' · '+level;if(areaEl)areaEl.textContent=area;if(leasable)leasable.textContent=area;}
function openFloorDetail(tower,level,zone,area){setExplorerTower(tower);setExplorerZone(zone.toLowerCase()==='high'?'high':'low');const matching=[...document.querySelectorAll('.floor-option')].find(b=>b.dataset.level===level.replace('F','').replace('Level ','L').replace(/^L?/, 'L')&&b.dataset.zone===explorerZone);if(matching){selectExplorerFloor(matching)}else{updateFloorDetail(level,area)}document.getElementById('floor-explorer')?.scrollIntoView({behavior:'smooth',block:'start'});}
</script>"""

# ══════════════════════════════════
# sustainability.html
# ══════════════════════════════════
sus_css = """<style>
.sus-hero .page-header-media{object-position:center 34%}@media(min-width:900px){.sus-hero>.container{transform:translateX(-200px)}}
.sus-certifications,.sus-performance,.sus-technical,.sus-water,.sus-indoor,.sus-future,.sus-human{padding:clamp(5.5rem,11vw,9rem) 0;border-top:1px solid var(--gold-b)}
.sus-certifications{background:var(--bg)}
.sus-intro{max-width:660px;color:rgba(242,238,229,.64);font-size:15px;line-height:1.8;margin-top:1.5rem}
.sus-cert-grid{display:grid;gap:1px;background:rgba(214,192,138,.24);margin-top:3.5rem}
@media(min-width:768px){.sus-cert-grid{grid-template-columns:1fr 1fr}}
.sus-cert-card{position:relative;min-height:360px;padding:clamp(2.5rem,6vw,5rem);background:linear-gradient(145deg,rgba(38,53,46,.42),var(--graphite));overflow:hidden;transition:background .35s,transform .35s}
.sus-cert-card::after{content:'';position:absolute;inset:auto -14% -38% 30%;height:72%;background:radial-gradient(ellipse,rgba(214,192,138,.13),transparent 64%);transform:rotate(-12deg);transition:transform .45s,opacity .45s;pointer-events:none}
.sus-cert-card:hover,.sus-cert-card:focus-visible{background:linear-gradient(145deg,rgba(38,53,46,.72),var(--graphite-soft));transform:translateY(-3px)}
.sus-cert-card:hover::after,.sus-cert-card:focus-visible::after{transform:rotate(-12deg) translate(-8px,-10px);opacity:1.35}
.sus-cert-card:focus-visible{outline:1px solid var(--gold);outline-offset:-6px}
.sus-cert-kicker{position:relative;z-index:1;color:var(--champagne-gold);font:10px var(--sans);letter-spacing:.38em;text-transform:uppercase}
.sus-cert-mark{position:relative;z-index:1;font-family:var(--serif);font-size:clamp(3.8rem,8vw,7rem);line-height:.82;font-weight:300;color:var(--warm-ivory);margin:2.4rem 0 1.4rem}
.sus-cert-mark em{display:block;color:var(--gold);font-style:italic}
.sus-cert-title{position:relative;z-index:1;color:var(--warm-ivory);font:11px var(--sans);letter-spacing:.2em;text-transform:uppercase;line-height:1.55;max-width:260px}
.sus-cert-detail{position:relative;z-index:1;color:rgba(242,238,229,.58);font-size:13px;line-height:1.7;max-width:330px;margin-top:1.3rem}
.sus-performance{background:linear-gradient(135deg,rgba(38,53,46,.26),transparent 55%) var(--bg2)}
.sus-section-head{max-width:700px}
.sus-section-head p{max-width:600px;color:rgba(242,238,229,.58);font-size:14px;line-height:1.8;margin-top:1.25rem}
.sus-metric-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(214,192,138,.2);margin-top:3rem}
@media(min-width:900px){.sus-metric-grid{grid-template-columns:repeat(4,1fr)}}
.sus-metric{background:var(--bg2);padding:2rem 1.5rem;min-height:210px;display:flex;flex-direction:column;justify-content:space-between}
.sus-metric-type{color:var(--champagne-gold);font:9px var(--sans);letter-spacing:.32em;text-transform:uppercase}
.sus-metric-value{color:var(--gold);font-family:var(--serif);font-size:clamp(2.1rem,4vw,3.8rem);font-weight:300;line-height:.9;margin:2rem 0 .9rem}
.sus-metric-note{color:rgba(242,238,229,.54);font-size:12px;line-height:1.55}
.sus-technical{background:var(--bg)}
.sus-tech-grid{display:grid;gap:1px;background:rgba(214,192,138,.2);margin-top:3rem}
@media(min-width:768px){.sus-tech-grid{grid-template-columns:1fr 1fr}}
@media(min-width:1100px){.sus-tech-grid{grid-template-columns:repeat(3,1fr)}}
.sus-tech-card{background:var(--card);min-height:230px;transition:background .25s}
.sus-tech-card:hover,.sus-tech-card:focus-within{background:var(--graphite-soft)}
.sus-tech-card summary{list-style:none;cursor:pointer;padding:1.5rem;display:flex;align-items:flex-start;gap:.9rem;color:var(--warm-ivory)}
.sus-tech-card summary::-webkit-details-marker{display:none}
.sus-tech-number{color:var(--gold);font:10px var(--sans);letter-spacing:.2em}
.sus-tech-name{font:11px var(--sans);letter-spacing:.18em;text-transform:uppercase;line-height:1.45;flex:1}
.sus-tech-toggle{color:var(--gold-champagne);font-size:1.25rem;line-height:1;transition:transform .25s}
.sus-tech-card[open] .sus-tech-toggle{transform:rotate(45deg)}
.sus-tech-body{padding:0 1.5rem 1.6rem 3.15rem}
.sus-tech-body p{color:rgba(242,238,229,.54);font-size:13px;line-height:1.7}
.sus-tech-stat{display:block;color:var(--gold);font-family:var(--serif);font-size:2rem;font-weight:300;line-height:1;margin-top:1.1rem}
.sus-tech-stat small{display:block;color:var(--champagne-gold);font:9px var(--sans);letter-spacing:.2em;text-transform:uppercase;margin-top:.55rem}
.sus-water{background:var(--bg2)}
.sus-water-grid,.sus-indoor-grid,.sus-future-grid{display:grid;gap:1rem;margin-top:3rem}
@media(min-width:768px){.sus-water-grid,.sus-indoor-grid,.sus-future-grid{grid-template-columns:repeat(3,1fr)}}
.sus-info-card{background:var(--card);border:1px solid rgba(214,192,138,.16);padding:2rem;min-height:245px}
.sus-info-card h3{font-family:var(--serif);font-size:1.65rem;font-weight:300;color:var(--warm-ivory);line-height:.98;margin:1.6rem 0 .9rem}
.sus-info-card p{color:rgba(242,238,229,.52);font-size:13px;line-height:1.7}
.sus-info-stat{color:var(--gold);font:2.2rem var(--serif);font-weight:300;display:block}
.sus-indoor{background:var(--bg)}
.sus-indoor-card{background:linear-gradient(145deg,rgba(38,53,46,.52),var(--card));border-top:1px solid var(--gold);padding:2rem;min-height:190px}
.sus-indoor-card h3{font:11px var(--sans);letter-spacing:.28em;text-transform:uppercase;color:var(--champagne-gold);margin:1rem 0}
.sus-indoor-card p{color:rgba(242,238,229,.56);font-size:14px;line-height:1.7}
.sus-visual-section{display:grid;min-height:clamp(500px,58vw,720px);background:var(--graphite);border-top:1px solid var(--gold-b)}
@media(min-width:900px){.sus-visual-section{grid-template-columns:1fr 1fr}}
.sus-visual-media{min-height:360px;overflow:hidden}.sus-visual-media img{width:100%;height:100%;min-height:360px;object-fit:cover;display:block;transition:transform .8s ease}.sus-visual-section:hover .sus-visual-media img{transform:scale(1.025)}
.sus-visual-copy{padding:clamp(3rem,8vw,8rem) clamp(1.5rem,7vw,8rem);align-self:center}.sus-visual-copy h2{font-family:var(--serif);font-size:clamp(3rem,6vw,6.2rem);font-weight:300;color:var(--warm-ivory);line-height:.88;margin:1rem 0 1.5rem}.sus-visual-copy h2 em{color:var(--gold);font-style:italic}.sus-visual-copy p{color:rgba(242,238,229,.62);font-size:15px;line-height:1.8;max-width:440px}
.sus-waste-copy{max-width:470px}.sus-waste-words{display:flex;flex-wrap:wrap;gap:.55rem 1.2rem;margin:2.4rem 0 0;padding:0;list-style:none;color:var(--gold);font:clamp(1.6rem,3vw,2.7rem) var(--serif);font-weight:300}.sus-waste-words li:nth-child(2){color:var(--champagne-gold)}.sus-waste-words li:nth-child(3){color:var(--stone)}
.sus-future{background:linear-gradient(145deg,rgba(38,53,46,.92),var(--capital-black));border-top-color:rgba(214,192,138,.28)}
.sus-future .sus-section-head p{color:rgba(242,238,229,.68)}
.sus-future .sus-info-card{background:rgba(17,17,17,.34);border-color:rgba(214,192,138,.26)}
.sus-future .sus-info-card h3{font-size:1.45rem;margin-top:1rem}
.sus-human{background:var(--bg2)}
.sus-cta{padding:clamp(5rem,10vw,8rem) 0;background:var(--capital-black);border-top:1px solid var(--gold-b);text-align:center}
.sus-cta h2{font-family:var(--serif);font-size:clamp(2.8rem,6vw,5.8rem);font-weight:300;line-height:.9;color:var(--warm-ivory)}
.sus-cta h2 em{color:var(--gold);font-style:italic}.sus-cta p{color:rgba(242,238,229,.58);font-size:15px;line-height:1.7;margin:1.5rem auto 2rem;max-width:480px}.sus-cta-actions{display:flex;justify-content:center;flex-wrap:wrap;gap:1rem}
@media(max-width:640px){.sus-metric{min-height:180px;padding:1.25rem}.sus-metric-value{font-size:2rem}.sus-cert-card{min-height:320px}.sus-tech-card summary{padding:1.25rem}.sus-tech-body{padding-left:2.8rem}.sus-visual-copy{padding:3.5rem 1.5rem}.sus-waste-words{font-size:1.8rem}}
@media(prefers-reduced-motion:reduce){.sus-cert-card,.sus-tech-toggle,.sus-visual-media img{transition:none}}
</style>"""

sus_body = """<div class="page-header sus-hero" style="--hero-position:center 34%">
  <img class="page-header-media" src="assets/images/feedback/sustainability-generated.jpg" alt="Capital Place glass facade with natural light and greenery" fetchpriority="high" />
  <div class="container">
    <p class="page-header-eyebrow">Sustainability</p>
    <h1>Sustainability<br><em>as a Standard</em></h1>
    <p>A healthier, more responsible workplace designed for long-term performance.</p>
  </div>
</div>
<section class="sus-certifications">
  <div class="container">
    <div class="sus-section-head">
      <p class="eyebrow">Dual LEED Certified</p>
      <h2 class="section-title">Certified<br><em>for Performance</em></h2>
      <p class="sus-intro">Capital Place is the first building in Hanoi to achieve both LEED Platinum for Operations &amp; Maintenance and LEED Gold for Building Design &amp; Construction.</p>
    </div>
    <div class="sus-cert-grid">
      <article class="sus-cert-card fade-up" tabindex="0">
        <span class="sus-cert-kicker">LEED</span>
        <p class="sus-cert-mark">Platinum</p>
        <h3 class="sus-cert-title">Operations &amp; Maintenance</h3>
        <p class="sus-cert-detail">Operational performance and ongoing building management.</p>
      </article>
      <article class="sus-cert-card fade-up" style="transition-delay:.12s" tabindex="0">
        <span class="sus-cert-kicker">LEED</span>
        <p class="sus-cert-mark"><em>Gold</em></p>
        <h3 class="sus-cert-title">Building Design &amp; Construction</h3>
        <p class="sus-cert-detail">Sustainable design and construction.</p>
      </article>
    </div>
  </div>
</section>
<section class="sus-performance">
  <div class="container">
    <div class="sus-section-head">
      <p class="eyebrow">Performance by Numbers</p>
      <h2 class="section-title">Measuring<br><em>What Matters</em></h2>
      <p>Selected performance indicators published by Capital Place, presented with their original qualifiers.</p>
    </div>
    <div class="sus-metric-grid">
      <article class="sus-metric fade-up"><span class="sus-metric-type">Energy</span><strong class="sus-metric-value">69%</strong><span class="sus-metric-note">Up to cooling energy saved.</span></article>
      <article class="sus-metric fade-up" style="transition-delay:.08s"><span class="sus-metric-type">Water</span><strong class="sus-metric-value">10,000 m³</strong><span class="sus-metric-note">Clean water saved annually.</span></article>
      <article class="sus-metric fade-up" style="transition-delay:.16s"><span class="sus-metric-type">Energy</span><strong class="sus-metric-value">27,636 kWh</strong><span class="sus-metric-note">Saved annually through smart sensor lighting.</span></article>
      <article class="sus-metric fade-up" style="transition-delay:.24s"><span class="sus-metric-type">Water</span><strong class="sus-metric-value">2,000+ m³</strong><span class="sus-metric-note">Water saved annually through reuse and green-space maintenance.</span></article>
    </div>
  </div>
</section>
<section class="sus-technical">
  <div class="container">
    <div class="sus-section-head">
      <p class="eyebrow">Energy Performance</p>
      <h2 class="section-title">Engineered<br><em>for Efficiency</em></h2>
      <p>Intelligent systems work quietly behind the scenes to optimise energy performance throughout the building.</p>
    </div>
    <div class="sus-tech-grid">
      <details class="sus-tech-card" open><summary><span class="sus-tech-number">01</span><span class="sus-tech-name">Building Management System</span><span class="sus-tech-toggle" aria-hidden="true">+</span></summary><div class="sus-tech-body"><p>Intelligent building management helps monitor and optimise energy use.</p><strong class="sus-tech-stat">10,000+ kWh<small>saved annually</small></strong></div></details>
      <details class="sus-tech-card"><summary><span class="sus-tech-number">02</span><span class="sus-tech-name">Low-E Glass Façade</span><span class="sus-tech-toggle" aria-hidden="true">+</span></summary><div class="sus-tech-body"><p>High-performance glazing across a 151,000 m² façade helps reduce solar heat gain.</p><strong class="sus-tech-stat">69%<small>up to cooling energy saved</small></strong></div></details>
      <details class="sus-tech-card"><summary><span class="sus-tech-number">03</span><span class="sus-tech-name">High-Efficiency IE3 Motors</span><span class="sus-tech-toggle" aria-hidden="true">+</span></summary><div class="sus-tech-body"><p>High-efficiency motors support lower energy demand in building systems.</p><strong class="sus-tech-stat">30%<small>energy saving compared to IE1</small></strong></div></details>
      <details class="sus-tech-card"><summary><span class="sus-tech-number">04</span><span class="sus-tech-name">Active Harmonic Filter</span><span class="sus-tech-toggle" aria-hidden="true">+</span></summary><div class="sus-tech-body"><p>Active harmonic filtering supports cleaner and more efficient electrical performance.</p><strong class="sus-tech-stat">1%<small>of total building energy consumption saved</small></strong></div></details>
      <details class="sus-tech-card"><summary><span class="sus-tech-number">05</span><span class="sus-tech-name">Smart Sensor Lighting</span><span class="sus-tech-toggle" aria-hidden="true">+</span></summary><div class="sus-tech-body"><p>Smart sensors respond to occupancy and daylight to reduce unnecessary lighting demand.</p><strong class="sus-tech-stat">27,636 kWh<small>saved per year</small></strong></div></details><details class="sus-tech-card"><summary><span class="sus-tech-number">06</span><span class="sus-tech-name">Water Reuse &amp; Green Space</span><span class="sus-tech-toggle" aria-hidden="true">+</span></summary><div class="sus-tech-body"><p>Water reuse supports responsible green-space maintenance across the Capital Place community.</p><strong class="sus-tech-stat">2,000+ m&sup3;<small>water saved annually</small></strong></div></details>
    </div>
  </div>
</section>
<section class="sus-water">
  <div class="container">
    <div class="sus-section-head"><p class="eyebrow">Water Management</p><h2 class="section-title">Every Drop<br><em>Counts</em></h2><p>Intelligent water systems reduce consumption and support responsible resource management.</p></div>
    <div class="sus-water-grid">
      <article class="sus-info-card fade-up"><span class="sus-info-stat">10,000 m³</span><h3>Sensor Faucets &amp; Eco-Flush</h3><p>Clean water saved per year.</p></article>
      <article class="sus-info-card fade-up" style="transition-delay:.1s"><span class="sus-info-stat">69,120 kWh</span><h3>Wastewater System</h3><p>Estimated annual savings.</p></article>
      <article class="sus-info-card fade-up" style="transition-delay:.2s"><span class="sus-info-stat">2,000+ m³</span><h3>Water Reuse</h3><p>Water saved annually through reuse and green-space maintenance.</p></article>
    </div>
  </div>
</section>
<section class="sus-indoor">
  <div class="container">
    <div class="sus-section-head"><p class="eyebrow">Indoor Environment</p><h2 class="section-title">A Healthier<br><em>Workplace</em></h2><p>Sustainability is also about the people inside the building — from indoor air quality to a more comfortable working environment.</p></div>
    <div class="sus-indoor-grid">
      <article class="sus-indoor-card fade-up"><span class="sus-cert-kicker">01</span><h3>Air Quality</h3><p>Improved indoor air environment for the people who work in the building.</p></article>
      <article class="sus-indoor-card fade-up" style="transition-delay:.1s"><span class="sus-cert-kicker">02</span><h3>Energy</h3><p>Efficient building systems that work quietly behind the scenes.</p></article>
      <article class="sus-indoor-card fade-up" style="transition-delay:.2s"><span class="sus-cert-kicker">03</span><h3>Wellbeing</h3><p>A healthier workplace designed around comfort, focus and connection.</p></article>
    </div>
  </div>
</section>
<section class="sus-visual-section">
  <div class="sus-visual-media"><img src="assets/images/feedback/sustainability-generated-2.jpg" alt="Capital Place architecture and planted landscape" loading="lazy" /></div>
  <div class="sus-visual-copy sus-waste-copy"><p class="eyebrow">Responsible Every Day</p><h2>Designed to<br><em>Reduce Waste</em></h2><p>Sustainability extends beyond building systems. Capital Place encourages responsible waste sorting, recycling and everyday environmental habits across its community.</p><p style="margin-top:1rem">Green Station, located at the Kim Ma entrance, supports the sorting and collection of recyclable materials.</p><ul class="sus-waste-words" aria-label="Responsible waste principles"><li>Reduce</li><li>Reuse</li><li>Recycle</li></ul></div>
</section>
<section class="sus-future">
  <div class="container">
    <div class="sus-section-head"><p class="eyebrow">Green Future</p><h2 class="section-title">Building a More<br><em>Conscious Community</em></h2><p>From greener everyday habits to community initiatives, sustainability at Capital Place extends beyond the building itself.</p></div>
    <div class="sus-future-grid">
      <article class="sus-info-card fade-up"><span class="sus-cert-kicker">01</span><h3>Green Station</h3><p>Encouraging responsible recycling and greener everyday habits.</p></article>
      <article class="sus-info-card fade-up" style="transition-delay:.1s"><span class="sus-cert-kicker">02</span><h3>Community</h3><p>Initiatives that bring tenants and the wider community together.</p></article>
      <article class="sus-info-card fade-up" style="transition-delay:.2s"><span class="sus-cert-kicker">03</span><h3>Wellbeing</h3><p>Activities supporting a healthier and more connected workplace.</p></article>
    </div>
  </div>
</section>
<section class="sus-visual-section sus-human">
  <div class="sus-visual-copy"><p class="eyebrow">The Human Side</p><h2>Better for the Building.<br><em>Better for People.</em></h2><p>A sustainable building should do more than reduce its environmental impact. It should create a workplace where people can work, connect and thrive.</p></div>
  <div class="sus-visual-media"><img src="assets/images/feedback/sustainability-generated.jpg" alt="People, greenery and natural light inside a premium workplace" loading="lazy" /></div>
</section>
<section class="sus-cta"><div class="container"><h2>Work Towards a<br><em>Better Future</em></h2><p>Discover a workplace built around performance, responsibility and people.</p><div class="sus-cta-actions"><a class="btn-primary" href="office.html">Explore Office <span aria-hidden="true">&rarr;</span></a><a class="btn-outline-gold" href="amenities.html#leasing">Enquire <span aria-hidden="true">&rarr;</span></a></div></div></section>"""

# ══════════════════════════════════
# amenities.html
# ══════════════════════════════════
am_css = """<style>
.am-hero-actions{display:flex;flex-wrap:wrap;gap:1rem;margin-top:2rem}@media(min-width:900px){.am-hero>.container{transform:translateX(-200px)}.am-flagship#the-nexus .am-flagship-content{transform:translateX(-200px)}.am-directory-grid .am-dir-card:first-child .am-dir-category,.am-directory-grid .am-dir-card:first-child h3{transform:translateX(16px)}.am-directory-grid .am-dir-card:first-child .am-dir-explore{transform:translateX(33px)}#success-msg>div>span.eyebrow{display:inline-block;transform:translateY(31px)}#success-msg>div>p{transform:translateY(-16px)}}
.am-section{padding:clamp(5.5rem,11vw,9rem) 0}
.am-section.alt{background:var(--bg2);border-top:1px solid var(--gold-b);border-bottom:1px solid var(--gold-b)}
.am-kicker{font-family:var(--sans);font-size:9px;letter-spacing:.42em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem}
.am-lead{max-width:560px;color:rgba(242,238,229,.62);font-size:15px;line-height:1.85}
.am-feature{display:grid;gap:3rem;align-items:center}
@media(min-width:900px){.am-feature{grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(4rem,8vw,9rem)}.am-feature.reverse{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr)}.am-feature.reverse .am-feature-copy{order:2}}
.am-feature-copy h2,.am-section-head h2{font-family:var(--serif);font-weight:300;color:var(--warm-ivory);font-size:clamp(2.4rem,5vw,4.8rem);line-height:.94;margin-bottom:1.25rem}
.am-feature-copy h2 em,.am-section-head h2 em{color:var(--gold);font-style:italic}
.am-feature-copy p{max-width:500px;color:rgba(242,238,229,.54);font-size:14px;line-height:1.85;margin-bottom:1rem}
.am-media{position:relative;min-height:360px;overflow:hidden;background:var(--card);border:1px solid rgba(214,192,138,.14)}
.am-media img{width:100%;height:100%;min-height:360px;object-fit:cover;display:block;transition:transform .7s ease}.am-media:hover img{transform:scale(1.025)}
.am-media::after{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(17,17,17,.1),transparent 50%,rgba(17,17,17,.45));pointer-events:none}
.am-category-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:rgba(214,192,138,.16);margin-top:2.5rem}
@media(min-width:768px){.am-category-grid{grid-template-columns:repeat(3,1fr)}}
.am-category{background:var(--card);padding:1.5rem;min-height:140px}.am-category h3{font-family:var(--serif);font-weight:300;color:var(--warm-ivory);font-size:1.2rem;margin-bottom:.6rem}.am-category p{color:rgba(242,238,229,.42);font-size:12px;line-height:1.6}
.am-flagship{position:relative;min-height:clamp(520px,64vw,760px);display:flex;align-items:flex-end;overflow:hidden;background:var(--bg3)}
.am-flagship img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}.am-flagship::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(17,17,17,.78),rgba(17,17,17,.18) 58%,rgba(17,17,17,.55)),linear-gradient(0deg,rgba(17,17,17,.88),transparent 55%)}
.am-flagship-content{position:relative;z-index:1;padding:clamp(3rem,8vw,7rem) 0;max-width:760px}.am-flagship-content h2{font-family:var(--serif);font-size:clamp(3rem,7vw,7rem);font-weight:300;line-height:.88;color:var(--warm-ivory);margin-bottom:1.25rem}.am-flagship-content h2 em{color:var(--gold);font-style:italic}.am-flagship-content p{max-width:560px;color:rgba(242,238,229,.68);font-size:15px;line-height:1.8}
.am-highlights{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;margin:2rem 0 2.5rem}.am-highlight{border-top:1px solid rgba(214,192,138,.35);padding-top:.8rem;color:var(--warm-ivory);font-family:var(--sans);font-size:10px;letter-spacing:.28em;text-transform:uppercase}@media(min-width:768px){.am-highlights{grid-template-columns:repeat(4,1fr)}}
.am-section-head{max-width:700px}.am-section-head p{max-width:560px;color:rgba(242,238,229,.56);font-size:14px;line-height:1.8}
.am-space-grid{display:grid;gap:1px;background:rgba(214,192,138,.16);margin-top:3rem}.am-space-card{background:var(--card);padding:2rem;min-height:215px}.am-space-num{font-family:var(--serif);font-size:2rem;color:var(--gold);font-weight:300}.am-space-card h3{color:var(--warm-ivory);font-family:var(--serif);font-weight:300;font-size:1.35rem;line-height:1.05;margin:1.25rem 0 .75rem}.am-space-card p{color:rgba(242,238,229,.46);font-size:13px;line-height:1.7}.am-space-card small{display:block;margin-top:1rem;color:var(--gold-champagne);font-size:10px;letter-spacing:.15em;text-transform:uppercase;line-height:1.6}@media(min-width:768px){.am-space-grid{grid-template-columns:repeat(2,1fr)}}@media(min-width:1100px){.am-space-grid{grid-template-columns:repeat(4,1fr)}}
.am-lounge{display:grid;gap:0;background:var(--bg3)}@media(min-width:900px){.am-lounge{grid-template-columns:1.1fr .9fr}}.am-lounge-media{min-height:420px}.am-lounge-media img{width:100%;height:100%;min-height:420px;object-fit:cover;display:block}.am-lounge-copy{padding:clamp(3rem,7vw,7rem) clamp(1.5rem,6vw,6rem);align-self:center}.am-lounge-copy h2{font-family:var(--serif);font-weight:300;color:var(--warm-ivory);font-size:clamp(2.6rem,5vw,5rem);line-height:.92}.am-lounge-copy p{color:rgba(242,238,229,.55);font-size:14px;line-height:1.8;margin:1.25rem 0 2rem}.am-points{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;border-top:1px solid var(--gold-b);padding-top:1.25rem}.am-point{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-champagne);line-height:1.5}
.am-wellness-grid{display:grid;gap:1rem;margin-top:3rem}@media(min-width:768px){.am-wellness-grid{grid-template-columns:repeat(3,1fr)}}.am-wellness-card{border:1px solid rgba(214,192,138,.18);padding:2rem;background:linear-gradient(145deg,rgba(38,53,46,.38),rgba(36,35,33,.88))}.am-wellness-card h3{font-family:var(--serif);font-weight:300;color:var(--warm-ivory);font-size:1.5rem}.am-wellness-card p{color:rgba(242,238,229,.48);font-size:13px;line-height:1.7;margin-top:.8rem}
.am-directory{background:var(--bg);padding:clamp(5.5rem,11vw,9rem) 0;border-top:1px solid var(--gold-b)}.am-filters{display:flex;flex-wrap:wrap;gap:.5rem;margin:2rem 0}.am-filter{border:1px solid rgba(214,192,138,.25);color:rgba(242,238,229,.56);background:transparent;padding:.75rem 1rem;font:10px var(--sans);letter-spacing:.22em;text-transform:uppercase;cursor:pointer;transition:background .2s,color .2s,border-color .2s}.am-filter:hover,.am-filter:focus-visible,.am-filter[aria-pressed=true]{background:var(--gold);border-color:var(--gold);color:var(--capital-black)}.am-directory-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(.75rem,2vw,1.25rem);background:transparent;align-items:stretch}@media(min-width:768px){.am-directory-grid{grid-template-columns:repeat(3,1fr)}}.am-dir-card{border:0;border-radius:0;background:var(--card);padding:0;text-align:left;color:inherit;cursor:pointer;min-width:0;height:100%;transition:background .2s,transform .2s}.am-dir-card:hover,.am-dir-card:focus-visible{background:var(--graphite);transform:translateY(-2px)}.am-dir-card[hidden]{display:none}.am-dir-card img{display:block;width:100%;height:170px;object-fit:cover}.am-dir-copy{padding:1.25rem 1.25rem 1.25rem 2.25rem}.am-dir-category{font-size:9px;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);display:block;margin-bottom:.65rem}.am-dir-card h3{font-family:var(--serif);font-size:1.35rem;font-weight:300;color:var(--warm-ivory);line-height:1.05}.am-dir-meta{font-size:10px;letter-spacing:.18em;color:rgba(242,238,229,.42);text-transform:uppercase;margin-top:.75rem}.am-dir-explore{display:inline-block;color:var(--gold-champagne);font-size:10px;letter-spacing:.2em;text-transform:uppercase;margin-top:1.2rem}
.am-community{background:var(--bg2);border-top:1px solid var(--gold-b);padding:clamp(5rem,10vw,8rem) 0}.am-community-grid{display:grid;gap:2rem}@media(min-width:768px){.am-community-grid{grid-template-columns:1fr 1fr;align-items:end}}.am-activity-list{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:2rem}.am-activity{border-top:1px solid var(--gold-b);padding-top:.75rem;color:var(--warm-ivory);font-size:11px;letter-spacing:.18em;text-transform:uppercase;line-height:1.5}
#leasing{background:var(--bg2);padding:clamp(6rem,12vw,9rem) 0;border-top:1px solid var(--gold-b)}.ls-grid{display:grid;gap:4rem}@media(min-width:1024px){.ls-grid{grid-template-columns:1fr 1.3fr;gap:5rem}}.ls-title{font-family:var(--serif);font-weight:300;color:var(--warm-ivory);font-size:clamp(2rem,4vw,3.2rem);line-height:.9;margin-bottom:1.4rem}.ls-title em{color:var(--gold);font-style:italic}.ls-desc{color:rgba(242,238,229,.5);font-size:14px;max-width:380px;line-height:1.7;margin-bottom:2rem}.ct-links{display:flex;flex-direction:column;gap:1.25rem}.ct-link{display:flex;align-items:center;gap:1rem}.ct-icon{width:36px;height:36px;border:1px solid rgba(214,192,138,.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:border-color .3s}.ct-link:hover .ct-icon{border-color:var(--gold)}.ct-icon svg{width:12px;height:12px;color:var(--gold)}.ct-text{color:rgba(242,238,229,.56);font-size:14px;transition:color .3s}.ct-link:hover .ct-text{color:var(--warm-ivory)}.ls-addr{margin-top:3rem;padding-top:2.5rem;border-top:1px solid var(--gold-b)}.ls-addr p{color:rgba(242,238,229,.38);font-size:12px;line-height:2}.enq-form{display:flex;flex-direction:column;gap:1.75rem}.field label{display:block;font-family:var(--sans);font-size:9px;letter-spacing:.42em;text-transform:uppercase;color:#fff;opacity:1;margin-bottom:10px}.field input,.field textarea{width:100%;background:transparent;border:none;border-bottom:1px solid rgba(214,192,138,.2);color:var(--warm-ivory);font-size:14px;font-family:var(--sans);padding:10px 0;outline:none;caret-color:var(--gold);transition:border-color .3s;resize:none}.field input:focus,.field textarea:focus{border-color:var(--gold)}.btn-submit{width:100%;border:1px solid var(--gold);color:var(--gold);padding:16px;font-size:10px;letter-spacing:.42em;text-transform:uppercase;font-family:var(--sans);transition:background .3s,color .3s;margin-top:8px}.btn-submit:hover{background:var(--gold);color:var(--capital-black)}
.am-dialog{position:fixed;inset:0;z-index:80;background:rgba(17,17,17,.86);display:grid;place-items:center;padding:1rem}.am-dialog[hidden]{display:none}.am-dialog-panel{width:min(680px,100%);max-height:90vh;overflow:auto;background:var(--graphite);border:1px solid rgba(214,192,138,.35);box-shadow:0 20px 80px rgba(0,0,0,.45);position:relative}.am-dialog-panel img{width:100%;height:220px;object-fit:cover;display:block}.am-dialog-body{padding:1.5rem 1.5rem 2rem}.am-dialog-close{position:absolute;right:1rem;top:1rem;width:36px;height:36px;border:1px solid rgba(242,238,229,.5);background:rgba(17,17,17,.55);color:var(--warm-ivory);cursor:pointer}.am-dialog-close:hover,.am-dialog-close:focus-visible{background:var(--gold);color:var(--capital-black);border-color:var(--gold)}.am-dialog-category{color:var(--gold);font-size:9px;letter-spacing:.3em;text-transform:uppercase}.am-dialog h3{font-family:var(--serif);font-size:2rem;font-weight:300;color:var(--warm-ivory);margin:.5rem 0}.am-dialog p{font-size:13px;line-height:1.7;color:rgba(242,238,229,.58)}.am-dialog-meta{font-size:10px;letter-spacing:.16em;color:var(--gold-champagne);text-transform:uppercase;margin:.75rem 0}
@media(prefers-reduced-motion:reduce){.am-media img,.am-dir-card{transition:none}}
</style>"""

am_body = """<div class="page-header am-hero" style="--hero-position:center 48%">
  <img class="page-header-media" src="assets/images/official/amenities-hero.jpg" alt="Capital Place grand lobby and connected amenities" fetchpriority="high" />
  <div class="container">
    <p class="page-header-eyebrow">Amenities</p>
    <h1>Everything<br><em>Within Reach</em></h1>
    <p>A connected workplace designed to support the way you work, meet, recharge and connect.</p>
    <div class="am-hero-actions"><a class="btn-gold" href="#amenity-directory">Explore Amenities <span aria-hidden="true">&rarr;</span></a></div>
  </div>
</div>
<section class="am-section" id="the-link">
  <div class="container">
    <div class="am-feature">
      <div class="am-feature-copy"><p class="am-kicker">The Link &middot; B1</p><h2>The <em>Link</em></h2><p class="am-lead">A connection between work and leisure.</p><p>The Link @ Capital Place is a multifunctional retail and lifestyle area located on B1, connecting workplace amenities with the Capital Place community.</p><p>Designed as a contemporary space inspired by water, The Link provides a place to start the working day, recharge between meetings and connect with colleagues and visitors.</p><a class="btn-outline-gold" href="#amenity-directory">Explore The Link <span aria-hidden="true">&rarr;</span></a></div>
      <figure class="am-media"><img src="assets/images/feedback/fb4-the-link.jpg" alt="Contemporary dining and lifestyle interior at The Link" loading="lazy"/><figcaption class="sr-only">The Link at B1</figcaption></figure>
    </div>
    <div class="am-category-grid" aria-label="The Link amenity categories">
      <div class="am-category"><h3>Dining</h3><p>Food and beverage options for everyday meals.</p></div><div class="am-category"><h3>Caf&eacute; &amp; Beverages</h3><p>Coffee and refreshments throughout the working day.</p></div><div class="am-category"><h3>Convenience</h3><p>Everyday essentials within the building.</p></div><div class="am-category"><h3>Fitness</h3><p>Fitness facilities for staying active during the workday.</p></div><div class="am-category"><h3>Wellness</h3><p>Services designed for relaxation and personal wellbeing.</p></div><div class="am-category"><h3>Family</h3><p>A dedicated space for children and families.</p></div>
    </div>
  </div>
</section>
<section class="am-flagship" id="the-nexus" aria-labelledby="nexus-title">
  <img src="assets/images/official/the-nexus.jpg" alt="The Nexus shared workspace at Capital Place" loading="lazy"/>
  <div class="container"><div class="am-flagship-content"><p class="am-kicker">The Nexus</p><h2 id="nexus-title">A Garden<br>of <em>Ideas</em></h2><p>The Nexus introduces a new kind of workspace &mdash; one shaped not only for work, but for people, ideas and shared experiences.</p><p>Designed as a “garden of ideas”, The Nexus brings together individuals, teams and perspectives within an environment created to inspire connection and growth.</p><div class="am-highlights"><span class="am-highlight">Work</span><span class="am-highlight">Connect</span><span class="am-highlight">Meet</span><span class="am-highlight">Grow</span></div><a class="btn-gold" href="#amenity-directory">Discover The Nexus <span aria-hidden="true">&rarr;</span></a></div></div>
</section>
<section class="am-section alt" id="meeting-collaboration">
  <div class="container"><div class="am-section-head"><p class="am-kicker">Workspace &amp; Meeting</p><h2>Space to Meet<br><em>&amp; Collaborate</em></h2><p>Flexible spaces designed for meetings, presentations, discussions and collaborative work.</p></div><div class="am-space-grid">
    <article class="am-space-card"><span class="am-space-num">01</span><h3>Professional Meeting Rooms</h3><p>Dedicated meeting spaces equipped for professional discussions and team meetings.</p><small>Approx. 8&ndash;16 people &middot; 30&ndash;50 m&sup2;</small></article>
    <article class="am-space-card"><span class="am-space-num">02</span><h3>Private Workspace</h3><p>Private studios designed for focused work and small teams.</p><small>Business address &middot; high-speed internet &middot; 24/7 access</small></article>
    <article class="am-space-card"><span class="am-space-num">03</span><h3>Event &amp; Seminar Spaces</h3><p>Flexible spaces for corporate meetings, presentations, talks and seminars.</p><small>Approx. 24&ndash;60 people &middot; 50&ndash;70 m&sup2;</small></article>
    <article class="am-space-card"><span class="am-space-num">04</span><h3>Collaboration Spaces</h3><p>Flexible shared spaces for casual collaboration and individual work.</p><small>Shared-space access &middot; tenant events &amp; member benefits</small></article>
  </div></div>
</section>
<section class="am-lounge" id="lounge"><div class="am-lounge-media"><img src="assets/images/official/premium-lounge.jpeg" alt="Premium lounge interior with city-facing atmosphere" loading="lazy"/></div><div class="am-lounge-copy"><p class="am-kicker">Premium &amp; VIP Lounge</p><h2>A Space<br>to <em>Host</em></h2><p>A private, elegant setting designed for executive meetings and high-level business engagements.</p><div class="am-points"><span class="am-point">Private setting</span><span class="am-point">Panoramic city views</span><span class="am-point">Professional beverage service</span><span class="am-point">Executive meetings</span></div></div></section>
<section class="am-section" id="common-area"><div class="container"><div class="am-feature reverse"><div class="am-feature-copy"><p class="am-kicker">Common Area</p><h2>Space to<br><em>Pause</em></h2><p>Welcoming and versatile shared spaces designed for individual work, casual collaboration and moments of relaxation.</p><div class="am-category-grid"><div class="am-category"><h3>Shared Lounge</h3></div><div class="am-category"><h3>Phone Booths</h3></div><div class="am-category"><h3>Focus Pods</h3></div><div class="am-category"><h3>Individual Workspace</h3></div><div class="am-category"><h3>Casual Collaboration</h3></div></div></div><figure class="am-media"><img src="assets/images/official/common-area.jpg" alt="Shared lounge and collaboration space" loading="lazy"/></figure></div></div></section>
<section class="am-section alt" id="wellness"><div class="container"><div class="am-section-head"><p class="am-kicker">Wellness</p><h2>Work Well.<br><em>Live Well.</em></h2><p>Wellness facilities designed to help people stay active, refreshed and balanced throughout the working day.</p></div><div class="am-wellness-grid"><article class="am-wellness-card"><h3>Fitness</h3><p>A modern fitness facility offering personalised training and diverse workout programmes to support strength, conditioning and overall wellbeing.</p></article><article class="am-wellness-card"><h3>Health &amp; Beauty</h3><p>Personal care and beauty services designed for relaxation and renewal.</p></article><article class="am-wellness-card"><h3>Family</h3><p>A safe and engaging play space designed for children and families.</p></article></div></div></section>
<section class="am-directory" id="amenity-directory" aria-labelledby="directory-title"><div class="container"><div class="am-section-head"><p class="am-kicker">Amenity Directory</p><h2 id="directory-title">Explore the<br><em>Amenities</em></h2><p>Filter by the way you work, meet and recharge. Select a card for location and service details.</p></div><div class="am-filters" role="tablist" aria-label="Filter amenities"><button class="am-filter" type="button" role="tab" aria-selected="true" aria-pressed="true" data-filter="all">All</button><button class="am-filter" type="button" role="tab" aria-selected="false" aria-pressed="false" data-filter="dining">Dining</button><button class="am-filter" type="button" role="tab" aria-selected="false" aria-pressed="false" data-filter="workspace">Workspace</button><button class="am-filter" type="button" role="tab" aria-selected="false" aria-pressed="false" data-filter="meeting">Meeting</button><button class="am-filter" type="button" role="tab" aria-selected="false" aria-pressed="false" data-filter="lounge">Lounge</button><button class="am-filter" type="button" role="tab" aria-selected="false" aria-pressed="false" data-filter="wellness">Wellness</button><button class="am-filter" type="button" role="tab" aria-selected="false" aria-pressed="false" data-filter="family">Family</button></div><div class="am-directory-grid" role="list">
  <button class="am-dir-card" type="button" role="listitem" data-category="dining" data-title="Dining" data-location="The Link · B1" data-hours="Current opening hours available on request" data-description="Food and beverage options for everyday meals within The Link." data-image="https://images.unsplash.com/photo-1587702068694-a909ef4aa346?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1587702068694-a909ef4aa346?w=800&h=500&fit=crop&auto=format" alt="Dining space at The Link" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Dining</span><h3>Dining</h3><span class="am-dir-meta">B1</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
  <button class="am-dir-card" type="button" role="listitem" data-category="workspace" data-title="Private Workspace" data-location="Capital Place community spaces" data-hours="Access details available on request" data-description="Private studios designed for focused work and small teams, with business address, high-speed internet and shared-space access." data-image="https://images.unsplash.com/photo-1768312783857-072ef0b3eea2?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1768312783857-072ef0b3eea2?w=800&h=500&fit=crop&auto=format" alt="Private workspace and shared lounge" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Workspace</span><h3>Private Workspace</h3><span class="am-dir-meta">Flexible access</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
  <button class="am-dir-card" type="button" role="listitem" data-category="meeting" data-title="Professional Meeting Rooms" data-location="Meeting & collaboration area" data-hours="Booking details available on request" data-description="Dedicated meeting spaces for professional discussions and team meetings, supporting approximately 8–16 people." data-image="https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=800&h=500&fit=crop&auto=format" alt="Professional meeting room" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Meeting</span><h3>Meeting Rooms</h3><span class="am-dir-meta">8&ndash;16 people</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
  <button class="am-dir-card" type="button" role="listitem" data-category="meeting" data-title="Event & Seminar Spaces" data-location="Meeting & collaboration area" data-hours="Booking details available on request" data-description="Flexible spaces for corporate meetings, presentations, talks and seminars, supporting approximately 24–60 people." data-image="https://images.unsplash.com/photo-1758193431353-87812fbff5cd?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1758193431353-87812fbff5cd?w=800&h=500&fit=crop&auto=format" alt="Event and seminar space" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Meeting</span><h3>Event Spaces</h3><span class="am-dir-meta">24&ndash;60 people</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
  <button class="am-dir-card" type="button" role="listitem" data-category="lounge" data-title="Premium & VIP Lounge" data-location="Capital Place lounge" data-hours="Availability details available on request" data-description="A private, elegant setting designed for executive meetings and high-level business engagements." data-image="https://images.unsplash.com/photo-1758193431353-87812fbff5cd?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1758193431353-87812fbff5cd?w=800&h=500&fit=crop&auto=format" alt="Premium and VIP lounge" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Lounge</span><h3>Premium &amp; VIP Lounge</h3><span class="am-dir-meta">Executive setting</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
  <button class="am-dir-card" type="button" role="listitem" data-category="wellness" data-title="Fitness & Wellness" data-location="The Link · B1" data-hours="Current opening hours available on request" data-description="Facilities designed to help people stay active, refreshed and balanced throughout the working day." data-image="https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=800&h=500&fit=crop&auto=format" alt="Fitness and wellness facility" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Wellness</span><h3>Fitness &amp; Wellness</h3><span class="am-dir-meta">B1</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
  <button class="am-dir-card" type="button" role="listitem" data-category="family" data-title="Family Space" data-location="The Link · B1" data-hours="Current opening hours available on request" data-description="A safe and engaging play space designed for children and families." data-image="https://images.unsplash.com/photo-1780369088190-914cc3eee938?w=1200&h=900&fit=crop&auto=format"><img src="https://images.unsplash.com/photo-1780369088190-914cc3eee938?w=800&h=500&fit=crop&auto=format" alt="Family-friendly amenity space" loading="lazy"/><span class="am-dir-copy"><span class="am-dir-category">Family</span><h3>Family Space</h3><span class="am-dir-meta">B1</span><span class="am-dir-explore">Explore &rarr;</span></span></button>
</div></div></section>
<section class="am-community"><div class="container"><div class="am-community-grid"><div><p class="am-kicker">Capital Place Community</p><h2 class="section-title">More Than<br><em>A Workplace</em></h2></div><div><p class="am-lead">A connected community where people, businesses and ideas come together.</p><div class="am-activity-list"><span class="am-activity">Community events</span><span class="am-activity">Wellbeing activities</span><span class="am-activity">Green initiatives</span><span class="am-activity">First aid training</span><span class="am-activity">Community programmes</span></div></div></div></div></section>
<section id="leasing"><div class="container"><div class="ls-grid"><div><p class="am-kicker">Enquire</p><h2 class="ls-title">Make Capital Place<br><em>Your Place</em></h2><p class="ls-desc">Discover a workplace designed around your business, your people and the way you work.</p><div class="ct-links"><a href="tel:18009289" class="ct-link"><span class="ct-icon"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg></span><span class="ct-text">1800 9289</span></a><a href="mailto:leasing@capitalplace.com.vn" class="ct-link"><span class="ct-icon"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg></span><span class="ct-text">leasing@capitalplace.com.vn</span></a></div><div class="ls-addr"><p>29 Lieu Giai Street<br>Ngoc Ha, Ba Dinh<br>Hanoi, Vietnam</p></div></div><div><div id="success-msg"><div><div class="succ-line"></div><span class="eyebrow">Enquiry Received</span><p class="success-copy">Our leasing team will contact you within 24 hours.</p></div></div><form class="enq-form" id="enq-form" onsubmit="submitForm(event)"><div class="field"><label for="fn">Full Name</label><input type="text" id="fn" name="name" autocomplete="name" required/></div><div class="field"><label for="fc">Company</label><input type="text" id="fc" name="company" autocomplete="organization" required/></div><div class="field"><label for="fe">Email</label><input type="email" id="fe" name="email" autocomplete="email" required/></div><div class="field"><label for="fp">Phone</label><input type="tel" id="fp" name="phone" autocomplete="tel" required/></div><div class="field"><label for="fm">Message</label><textarea id="fm" name="message" rows="3"></textarea></div><button type="submit" class="btn-submit">Submit Enquiry</button></form></div></div></div></section>
<div class="am-dialog" id="am-dialog" role="dialog" aria-modal="true" aria-labelledby="am-dialog-title" hidden><div class="am-dialog-panel"><button class="am-dialog-close" type="button" aria-label="Close amenity details">&times;</button><img id="am-dialog-image" src="" alt=""/><div class="am-dialog-body"><span class="am-dialog-category" id="am-dialog-category"></span><h3 id="am-dialog-title"></h3><p class="am-dialog-meta" id="am-dialog-meta"></p><p id="am-dialog-description"></p></div></div></div>"""

am_js = """<script>
(function(){
  const dialog=document.getElementById('am-dialog');
  const dialogImage=document.getElementById('am-dialog-image');
  const dialogCategory=document.getElementById('am-dialog-category');
  const dialogTitle=document.getElementById('am-dialog-title');
  const dialogMeta=document.getElementById('am-dialog-meta');
  const dialogDescription=document.getElementById('am-dialog-description');
  let lastTrigger=null;
  function closeDialog(){if(!dialog)return;dialog.hidden=true;document.body.classList.remove('dialog-open');if(lastTrigger)lastTrigger.focus()}
  document.querySelectorAll('.am-filter').forEach(btn=>btn.addEventListener('click',()=>{
    const filter=btn.dataset.filter;
    document.querySelectorAll('.am-filter').forEach(item=>{const active=item===btn;item.setAttribute('aria-selected',active?'true':'false');item.setAttribute('aria-pressed',active?'true':'false')});
    document.querySelectorAll('.am-dir-card').forEach(card=>{card.hidden=filter!=='all' && card.dataset.category!==filter});
  }));
  document.querySelectorAll('.am-dir-card').forEach(card=>card.addEventListener('click',()=>{
    lastTrigger=card;dialogImage.src=card.dataset.image;dialogImage.alt=card.dataset.title;dialogCategory.textContent=card.dataset.category;dialogTitle.textContent=card.dataset.title;dialogMeta.textContent=card.dataset.location+' · '+card.dataset.hours;dialogDescription.textContent=card.dataset.description;dialog.hidden=false;document.body.classList.add('dialog-open');dialog.querySelector('.am-dialog-close').focus()
  }));
  dialog?.querySelector('.am-dialog-close')?.addEventListener('click',closeDialog);
  dialog?.addEventListener('click',e=>{if(e.target===dialog)closeDialog()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape' && dialog && !dialog.hidden)closeDialog()});
})();
function submitForm(e){e.preventDefault();document.getElementById('enq-form').style.display='none';document.getElementById('success-msg').classList.add('show')}
</script>"""

# ══════════════════════════════════
# Write all files
# ══════════════════════════════════
pages = {
    'index.html': head("Capital Place \u2013 Hanoi's Premier Address",
        "Capital Place is Hanoi's premier Grade-A office address. 93,700 SQM, LEED Platinum, 29 Lieu Giai, Ba Dinh.",
        idx_css) + "\n" + NAV + "\n" + idx_body + "\n" + idx_js + "\n" + FOOTER,

    'location.html': head("Location \u2013 Capital Place Hanoi",
        "Capital Place is located at 29 Lieu Giai, Ba Dinh, Hanoi \u2013 the heart of Vietnam's diplomatic quarter.",
        loc_css) + "\n" + NAV + "\n" + loc_body + "\n" + FOOTER,

    'office.html': head("Office Floors \u2013 Capital Place Hanoi",
        "Grade-A office floors at Capital Place \u2013 column-free, 1,850\u20132,100 SQM per floor, full-height glazing.",
        off_css) + "\n" + NAV + "\n" + off_body + "\n" + off_js + "\n" + FOOTER,

    'sustainability.html': head("Sustainability \u2013 Capital Place Hanoi",
        "Capital Place holds dual LEED certifications: Platinum for Operations and Gold for Building Design & Construction.",
        sus_css) + "\n" + NAV + "\n" + sus_body + "\n" + FOOTER,

    'amenities.html': head("Amenities \u2013 Capital Place Hanoi",
        "World-class amenities at Capital Place: Sky Lounge, Fitness Centre, Conference Centre, Dining and Retail.",
        am_css) + "\n" + NAV + "\n" + am_body + "\n" + am_js + "\n" + FOOTER,
}

from ux_upgrade import apply_upgrade

pages = apply_upgrade(pages, head, NAV, FOOTER)

for fname, content in pages.items():
    path = os.path.join(ROOT, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{fname}: {len(content):,} bytes")

print("Done!")
