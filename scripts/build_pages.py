import os

ROOT = r'c:\Users\LENOVO\Documents\GitHub\Capital'

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
    <a href="index.html" class="nav-logo">
      <span class="logo-top">Capital</span>
      <span class="logo-bot">Place</span>
    </a>
    <div class="nav-links">
      <a href="index.html">Home</a>
      <a href="location.html">Location</a>
      <a href="office.html">Office</a>
      <a href="sustainability.html">Sustainability</a>
      <a href="amenities.html">Amenities</a>
      <div class="nav-sep"></div>
      <div class="lang-btns">
        <button class="active" onclick="setLang('EN')">EN</button>
        <span class="lang-sep2">|</span>
        <button onclick="setLang('VI')">VI</button>
      </div>
      <a href="amenities.html#leasing" class="btn-enquire">Enquire</a>
    </div>
    <button class="nav-ham" id="hamburger" aria-label="Toggle menu">
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
        <div class="ft-logo"><span class="logo-top">Capital</span><span class="logo-bot">Place</span></div>
        <p class="ft-addr">Twin-Peaks Joint Stock Company<br>29 Lieu Giai, Ngoc Ha<br>Ba Dinh, Hanoi, Vietnam</p>
      </div>
      <div class="ft-col">
        <p class="ft-col-title">Navigate</p>
        <a href="index.html">Home</a>
        <a href="location.html">Location</a>
        <a href="office.html">Office</a>
        <a href="sustainability.html">Sustainability</a>
        <a href="amenities.html">Amenities</a>
      </div>
      <div class="ft-col">
        <p class="ft-col-title">Contact</p>
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
.ov1{position:absolute;inset:0;background:rgba(11,11,9,.35)}
.ov2{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(11,11,9,.65) 0%,transparent 50%,var(--bg) 100%)}
.ov3{position:absolute;bottom:0;left:0;right:0;height:45%;background:linear-gradient(to top,var(--bg),transparent)}
.hero-badges{position:absolute;top:86px;right:var(--px);display:flex;flex-direction:column;align-items:flex-end;gap:8px;animation:fadeIn .9s .6s both}
.badge{font-family:var(--sans);font-size:9px;letter-spacing:.45em;text-transform:uppercase;border:1px solid;padding:7px 12px;backdrop-filter:blur(4px);background:rgba(11,11,9,.3)}
.badge-gold{color:var(--gold);border-color:rgba(201,168,102,.35)}
.badge-dim{color:rgba(201,168,102,.55);border-color:rgba(201,168,102,.15)}
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
.spec-sep{width:1px;height:12px;background:rgba(201,168,102,.25)}
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
.exp-header>p{color:rgba(255,255,255,.28);font-size:14px;max-width:280px;line-height:1.7}
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
.zone-item.active .zone-sub{color:rgba(201,168,102,.65)}
.zone-detail{font-size:14px;line-height:1.7;color:rgba(255,255,255,.38);overflow:hidden;max-height:0;opacity:0;transition:max-height .4s cubic-bezier(.22,1,.36,1),opacity .35s ease,margin-top .35s;margin-top:0}
.zone-detail.open{max-height:120px;opacity:1;margin-top:12px}
.img-panel{display:none;padding-left:3rem}
@media(min-width:1024px){.img-panel{display:block}}
.img-sticky{position:sticky;top:88px}
.img-wrap{position:relative;overflow:hidden;background:var(--card);height:min(72vh,640px)}
.zone-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .7s ease,transform .7s ease;opacity:0;transform:scale(1.04)}
.zone-img.active{opacity:1;transform:scale(1)}
.img-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(10,10,8,.85) 0%,transparent 60%,rgba(10,10,8,.15) 100%)}
.img-lbl{position:absolute;bottom:0;left:0;right:0;padding:2rem}
.img-lbl-sub{font-family:var(--sans);font-size:9px;letter-spacing:.45em;text-transform:uppercase;color:var(--gold)}
.img-lbl-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(1.4rem,2.5vw,1.8rem);margin-top:4px}
.zone-dots{position:absolute;right:24px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:8px}
.zone-dot{width:1px;background:rgba(255,255,255,.2);transition:height .3s,background .3s;height:16px;border:none}
.zone-dot.active{height:32px;background:var(--gold)}.zone-dot:hover{background:rgba(255,255,255,.4)}
.quick-links{background:var(--bg2);border-top:1px solid var(--gold-b);padding:clamp(4rem,8vw,6rem) 0}
.ql-grid{display:grid;gap:1px;background:var(--gold-b)}
@media(min-width:768px){.ql-grid{grid-template-columns:repeat(4,1fr)}}
.ql-card{background:var(--bg2);padding:2.5rem 2rem;display:flex;flex-direction:column;gap:1rem;transition:background .3s}
.ql-card:hover{background:var(--card)}
.ql-num{font-family:var(--sans);font-size:9px;letter-spacing:.4em;color:rgba(201,168,102,.4)}
.ql-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:1.25rem;line-height:1.2}
.ql-desc{font-family:var(--sans);font-size:13px;color:rgba(255,255,255,.3);line-height:1.6}
.ql-arrow{margin-top:auto;color:var(--gold);display:flex;align-items:center;gap:8px;font-family:var(--sans);font-size:10px;letter-spacing:.25em;text-transform:uppercase}
.ql-arrow svg{width:12px;height:12px;transition:transform .2s}
.ql-card:hover .ql-arrow svg{transform:translateX(3px)}
</style>"""

idx_body = """<section id="hero">
  <video class="hero-bg" autoplay muted loop playsinline poster="https://images.unsplash.com/photo-1690944851207-3f288c8fcd0b?w=1600&h=2000&fit=crop&auto=format&q=90">
    <source src="https://capitalplace.com.vn/wp-content/uploads/2026/05/CAPITAL-PLACE-TVC_1080p.mp4" type="video/mp4">
  </video>
  <div class="ov1"></div><div class="ov2"></div><div class="ov3"></div>
  <div class="hero-badges">
    <span class="badge badge-gold">LEED Platinum</span>
    <span class="badge badge-dim">LEED Gold</span>
  </div>
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
    <div class="stat-cell fade-up"><span class="stat-num" data-target="93700" data-fmt="comma">0</span><span class="stat-label">SQM Total GFA</span></div>
    <div class="stat-cell fade-up" style="transition-delay:.1s"><span class="stat-num" data-target="2">0</span><span class="stat-label">Towers</span></div>
    <div class="stat-cell fade-up" style="transition-delay:.2s"><span class="stat-num" data-target="41">0</span><span class="stat-label">Storeys</span></div>
    <div class="stat-cell fade-up" style="transition-delay:.3s"><span class="stat-num" data-target="2015">0</span><span class="stat-label">Completed</span></div>
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
      <div class="img-panel"><div class="img-sticky"><div class="img-wrap" id="img-wrap">
        <div class="img-ov"></div>
        <div class="img-lbl"><p class="img-lbl-sub" id="z-sub"></p><h3 class="img-lbl-title" id="z-title"></h3></div>
        <div class="zone-dots" id="zone-dots"></div>
      </div></div></div>
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
  {num:"01",id:"lobby",label:"Grand Lobby",sub:"Ground Floor \u00b7 Triple-height atrium",detail:"Marble floors, bamboo-inspired columns, and site-specific Vietnamese art define the arrival. The 18\u00a0m atrium opens both towers.",img:"https://images.unsplash.com/photo-1780369088190-914cc3eee938?w=1200&h=900&fit=crop&auto=format"},
  {num:"02",id:"office",label:"Office Floors",sub:"L6 \u2013 L38 \u00b7 Both towers \u00b7 93,700 SQM",detail:"Column-free, open-plan floorplates with full-height glazing. GFA 1,850\u20132,100 SQM per floor. NBF-compliant fresh air.",img:"https://images.unsplash.com/photo-1531972111231-7482a960e109?w=1200&h=900&fit=crop&auto=format"},
  {num:"03",id:"fitness",label:"Fitness & Wellness",sub:"Podium Level 3",detail:"Full gym, yoga studio, meditation zone, spa showers, and end-of-trip cyclist facilities. Open to all tower tenants.",img:"https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=1200&h=900&fit=crop&auto=format"},
  {num:"04",id:"dining",label:"Dining & Retail",sub:"Ground \u00b7 L1 \u00b7 L2",detail:"A curated selection of caf\u00e9s, restaurants, and specialty retail across the podium.",img:"https://images.unsplash.com/photo-1587702068694-a909ef4aa346?w=1200&h=900&fit=crop&auto=format"},
  {num:"05",id:"sky",label:"Sky Lounge",sub:"Level 39 \u00b7 Tower A",detail:"An exclusive tenant amenity floor with 360\u00b0 panoramic views of Hanoi.",img:"https://images.unsplash.com/photo-1758193431353-87812fbff5cd?w=1200&h=900&fit=crop&auto=format"},
  {num:"06",id:"conference",label:"Conference Centre",sub:"Podium L4 \u2013 L5",detail:"Divisible event halls, tiered auditorium (200 pax), breakout suites, and a dedicated event team.",img:"https://images.unsplash.com/photo-1617761141732-d481912af1a9?w=1400&h=950&fit=crop&auto=format"},
];
let aZ=0;
(function(){
  const list=document.getElementById('zone-list'),wrap=document.getElementById('img-wrap'),dots=document.getElementById('zone-dots');
  ZONES.forEach((z,i)=>{
    const img=document.createElement('img');img.src=z.img;img.alt=z.label;img.loading='lazy';img.className='zone-img'+(i===0?' active':'');
    wrap.insertBefore(img,wrap.querySelector('.img-ov'));
    const dot=document.createElement('button');dot.className='zone-dot'+(i===0?' active':'');dot.setAttribute('aria-label',z.label);dot.onclick=()=>sz(i);dots.appendChild(dot);
    const btn=document.createElement('button');btn.className='zone-item'+(i===0?' active':' inactive');
    btn.innerHTML='<span class="zone-num">'+z.num+'</span><div class="zone-body"><div class="zone-head"><h3>'+z.label+'</h3><svg class="zone-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5"/></svg></div><p class="zone-sub">'+z.sub+'</p><p class="zone-detail'+(i===0?' open':'')+'">'+z.detail+'</p></div>';
    btn.onmouseenter=btn.onclick=()=>sz(i);list.appendChild(btn);
  });
  document.getElementById('z-sub').textContent=ZONES[0].sub;document.getElementById('z-title').textContent=ZONES[0].label;
})();
function sz(i){if(i===aZ)return;aZ=i;
  document.querySelectorAll('.zone-item').forEach((el,x)=>{el.classList.toggle('active',x===i);el.classList.toggle('inactive',x!==i);el.querySelector('.zone-detail').classList.toggle('open',x===i)});
  document.querySelectorAll('.zone-img').forEach((el,x)=>el.classList.toggle('active',x===i));
  document.querySelectorAll('.zone-dot').forEach((el,x)=>el.classList.toggle('active',x===i));
  document.getElementById('z-sub').textContent=ZONES[i].sub;document.getElementById('z-title').textContent=ZONES[i].label;
}
</script>"""

# ══════════════════════════════════
# location.html
# ══════════════════════════════════
loc_css = """<style>
.loc-map{width:100%;height:clamp(320px,45vw,560px);border:0;filter:grayscale(1) contrast(1.1) brightness(.6)}
.loc-grid{display:grid;gap:0;border-top:1px solid var(--gold-b)}
@media(min-width:1024px){.loc-grid{grid-template-columns:1fr 1fr}}
.loc-cell{padding:clamp(3rem,6vw,5rem);border-bottom:1px solid var(--gold-b)}
@media(min-width:1024px){.loc-cell{border-right:1px solid var(--gold-b);border-bottom:none}}
.loc-cell:last-child{border-right:none;border-bottom:none}
.loc-cell-label{font-family:var(--sans);font-size:9px;letter-spacing:.45em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem}
.loc-cell h3{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(1.3rem,2.5vw,1.8rem);line-height:1.1;margin-bottom:1rem}
.loc-cell p{color:rgba(255,255,255,.3);font-size:14px;line-height:1.75}
.nearbylist{list-style:none;margin-top:1.5rem;display:flex;flex-direction:column;gap:.75rem}
.nearbylist li{display:flex;align-items:center;gap:1rem;color:rgba(255,255,255,.3);font-size:13px;font-family:var(--sans)}
.nearbylist li::before{content:'';display:block;width:20px;height:1px;background:var(--gold);flex-shrink:0}
.transport-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--gold-b);margin-top:clamp(3rem,6vw,5rem)}
.transport-cell{background:var(--bg);padding:2rem;display:flex;flex-direction:column;gap:.5rem}
.transport-icon{font-family:var(--sans);font-size:9px;letter-spacing:.4em;text-transform:uppercase;color:rgba(201,168,102,.5)}
.transport-name{font-family:var(--serif);font-weight:300;color:#fff;font-size:1.1rem}
.transport-dist{font-family:var(--sans);font-size:12px;color:rgba(255,255,255,.25)}
</style>"""

loc_body = """<div class="page-header">
  <div class="container">
    <p class="page-header-eyebrow">Location</p>
    <h1>Prime<br><em>Ba Dinh</em></h1>
    <p>29 Lieu Giai Street, Ngoc Ha Ward &mdash; at the heart of Hanoi's most prestigious diplomatic and government district.</p>
  </div>
</div>
<iframe class="loc-map"
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3723.7530985168567!2d105.82763!3d21.03543!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3135ab4f84b16e69%3A0x53c9a6d0c4c4bd2b!2sCapital%20Place!5e0!3m2!1sen!2s!4v1692000000000"
  allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Capital Place map">
</iframe>
<section style="background:var(--bg);padding:clamp(6rem,12vw,9rem) 0">
  <div class="container">
    <div class="loc-grid">
      <div class="loc-cell fade-up">
        <p class="loc-cell-label">Address</p>
        <h3>29 Lieu Giai<br>Ba Dinh, Hanoi</h3>
        <p>Situated in the Ba Dinh diplomatic quarter &mdash; home to Vietnam's National Assembly, Presidential Palace, Ho Chi Minh Mausoleum, and dozens of foreign embassies.</p>
        <ul class="nearbylist">
          <li>National Assembly &mdash; 800 m</li>
          <li>Presidential Palace &mdash; 1.2 km</li>
          <li>Noi Bai Airport &mdash; 28 km</li>
          <li>Hoan Kiem Lake &mdash; 3.5 km</li>
          <li>West Lake (Ho Tay) &mdash; 1.8 km</li>
        </ul>
      </div>
      <div class="loc-cell fade-up" style="transition-delay:.1s">
        <p class="loc-cell-label">Why Ba Dinh</p>
        <h3>Hanoi's Most<br>Prestigious Address</h3>
        <p>Ba Dinh is Hanoi's political and diplomatic centre. Major multinational tenants in the area include embassies of the US, EU, UK, Japan, and Korea, as well as Vietnam's largest state-owned enterprises.</p>
        <p style="margin-top:1rem">Capital Place provides unmatched visibility and prestige for organisations that require proximity to government and diplomatic missions.</p>
      </div>
    </div>
    <div class="transport-grid">
      <div class="transport-cell fade-up"><span class="transport-icon">Car</span><span class="transport-name">Noi Bai Airport</span><span class="transport-dist">28 km &mdash; approx. 35 min</span></div>
      <div class="transport-cell fade-up" style="transition-delay:.08s"><span class="transport-icon">Walk</span><span class="transport-name">Kim Ma Bus Rapid Transit</span><span class="transport-dist">200 m &mdash; 2 min walk</span></div>
      <div class="transport-cell fade-up" style="transition-delay:.16s"><span class="transport-icon">Metro</span><span class="transport-name">Metro Line 3 (Planned)</span><span class="transport-dist">Lieu Giai Station &mdash; adjacent</span></div>
      <div class="transport-cell fade-up" style="transition-delay:.24s"><span class="transport-icon">Walk</span><span class="transport-name">Hanoi Railway Station</span><span class="transport-dist">4.5 km &mdash; approx. 12 min</span></div>
    </div>
  </div>
</section>"""

# ══════════════════════════════════
# office.html
# ══════════════════════════════════
def make_svg(fid):
    G = fid == 'ground'
    S = fid == 'sky'
    ticks_n = ''.join(f'<line x1="{44+i*17}" y1="24" x2="{44+i*17}" y2="30" stroke="#c9a866" stroke-width=".6" stroke-opacity=".6"/>' for i in range(24))
    ticks_s = ''.join(f'<line x1="{44+i*17}" y1="310" x2="{44+i*17}" y2="316" stroke="#c9a866" stroke-width=".6" stroke-opacity=".6"/>' for i in range(24))
    ticks_w = ''.join(f'<line x1="24" y1="{44+i*17}" x2="30" y2="{44+i*17}" stroke="#c9a866" stroke-width=".6" stroke-opacity=".6"/>' for i in range(16))
    ticks_e = ''.join(f'<line x1="450" y1="{44+i*17}" x2="456" y2="{44+i*17}" stroke="#c9a866" stroke-width=".6" stroke-opacity=".6"/>' for i in range(16))
    cg = ''.join(f'<line x1="{x}" y1="24" x2="{x}" y2="316" stroke="#c9a866" stroke-width=".5" stroke-opacity=".07" stroke-dasharray="4 5"/>' for x in [132,240,348])
    rg = ''.join(f'<line x1="24" y1="{y}" x2="456" y2="{y}" stroke="#c9a866" stroke-width=".5" stroke-opacity=".07" stroke-dasharray="4 5"/>' for y in [120,196,268])
    core = '' if G else '<rect x="172" y="108" width="136" height="124" fill="#131310" stroke="#c9a866" stroke-width=".9"/>'
    lifts = '' if G or S else ''.join(f'<g><rect x="{185+i*18}" y="120" width="14" height="18" fill="#1c1c18" stroke="#c9a866" stroke-width=".5"/><line x1="{186+i*18}" y1="121" x2="{198+i*18}" y2="137" stroke="#c9a866" stroke-width=".4" stroke-opacity=".35"/><line x1="{198+i*18}" y1="121" x2="{186+i*18}" y2="137" stroke="#c9a866" stroke-width=".4" stroke-opacity=".35"/></g>' for i in range(6))
    stairs = '' if G or S else '<rect x="178" y="153" width="22" height="26" fill="#1c1c18" stroke="#c9a866" stroke-width=".5"/><rect x="280" y="153" width="22" height="26" fill="#1c1c18" stroke="#c9a866" stroke-width=".5"/>'
    lbl = '' if G or S else '<text x="240" y="175" text-anchor="middle" fill="#3a3428" font-size="7" letter-spacing="2.5" font-family="sans-serif">CORE</text>'
    sp = ''
    if G: sp = '<rect x="176" y="130" width="128" height="8" rx="4" fill="none" stroke="#c9a866" stroke-width=".8"/><rect x="196" y="148" width="88" height="44" fill="#131310" stroke="#c9a866" stroke-width=".8"/><text x="240" y="175" text-anchor="middle" fill="#3a3428" font-size="7" letter-spacing="2" font-family="sans-serif">RECEPTION</text>'
    if S: sp = '<ellipse cx="240" cy="170" rx="80" ry="60" fill="none" stroke="#c9a866" stroke-width=".7" stroke-opacity=".25" stroke-dasharray="5 4"/><text x="240" y="174" text-anchor="middle" fill="#3a3428" font-size="7.5" letter-spacing="2" font-family="sans-serif">SKY LOUNGE</text>'
    return f'<svg viewBox="0 0 480 340" style="width:100%;height:auto;max-height:280px"><rect x="24" y="24" width="432" height="292" fill="none" stroke="#c9a866" stroke-width="1.2"/>{ticks_n}{ticks_s}{ticks_w}{ticks_e}{cg}{rg}{core}{lifts}{stairs}{sp}{lbl}<text x="240" y="15" text-anchor="middle" fill="#3a3428" font-size="7.5" letter-spacing="2" font-family="sans-serif">N</text><text x="240" y="332" text-anchor="middle" fill="#3a3428" font-size="7.5" letter-spacing="2" font-family="sans-serif">S</text><text x="12" y="173" text-anchor="middle" fill="#3a3428" font-size="7.5" letter-spacing="2" font-family="sans-serif">W</text><text x="465" y="173" text-anchor="middle" fill="#3a3428" font-size="7.5" letter-spacing="2" font-family="sans-serif">E</text><g transform="translate(440,48)"><line x1="0" y1="12" x2="0" y2="-8" stroke="#c9a866" stroke-width=".8"/><polygon points="0,-10 -5,-2 5,-2" fill="#c9a866"/></g><g transform="translate(32,308)"><line x1="0" y1="0" x2="68" y2="0" stroke="#c9a866" stroke-width=".8" stroke-opacity=".5"/><line x1="0" y1="-4" x2="0" y2="4" stroke="#c9a866" stroke-width=".8" stroke-opacity=".5"/><line x1="68" y1="-4" x2="68" y2="4" stroke="#c9a866" stroke-width=".8" stroke-opacity=".5"/><text x="34" y="-7" text-anchor="middle" fill="#3a3428" font-size="6.5" letter-spacing="1" font-family="sans-serif">20 m</text></g></svg>'

FLOORS = [
    {"id":"ground","label":"Ground Floor","range":"Level G","gfa":"4,200 SQM","height":"12.0 m (triple)","grid":"\u2014","use":"Lobby \u00b7 Retail \u00b7 Drop-off \u00b7 Security"},
    {"id":"podium","label":"Podium","range":"L1 \u2013 L5","gfa":"8,400 SQM","height":"4.5 m (slab-slab)","grid":"9 \u00d7 9 m","use":"Amenities \u00b7 Parking \u00b7 Conference \u00b7 Retail"},
    {"id":"lo","label":"Office (Lower)","range":"L6 \u2013 L20","gfa":"2,100 SQM","height":"2.85 m (finished)","grid":"9 \u00d7 9 m","use":"Grade-A Open Plan \u00b7 Column-free"},
    {"id":"hi","label":"Office (Upper)","range":"L21 \u2013 L38","gfa":"1,850 SQM","height":"2.85 m (finished)","grid":"9 \u00d7 9 m","use":"Premium Open Plan \u00b7 270\u00b0 Views"},
    {"id":"sky","label":"Sky Levels","range":"L39 \u2013 L41","gfa":"1,600 SQM","height":"3.5 m","grid":"\u2014","use":"Sky Lounge \u00b7 Mechanical \u00b7 Roof Garden"},
]

def floor_panels():
    out = ''
    for i, f in enumerate(FLOORS):
        active = ' active' if i == 2 else ''
        rows = ''.join(f'<div class="spec-row"><span class="spec-key">{k}</span><span class="spec-val">{v}</span></div>' for k, v in [("GFA",f["gfa"]),("Ceiling Height",f["height"]),("Column Grid",f["grid"]),("Primary Use",f["use"])])
        out += f'<div class="floor-panel{active}" data-fi="{i}"><div class="svg-box">{make_svg(f["id"])}</div><div class="floor-specs"><div class="floor-spec-hd"><span class="eyebrow">{f["range"]}</span><h3>{f["label"]}</h3></div><div class="spec-table">{rows}</div><a href="amenities.html#leasing" class="btn-outline-gold">Request Floor Plan<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg></a></div></div>'
    return out

def floor_btns():
    out = ''
    for i, f in enumerate(FLOORS):
        active = ' active' if i == 2 else ' inactive'
        out += f'<button class="floor-btn{active}" onclick="setFloor({i})"><span class="floor-range">{f["range"]}</span><span class="floor-lbl">{f["label"]}</span></button>'
    return out

off_css = """<style>
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.fp-header{margin-bottom:3.5rem}
.fp-grid{display:grid}
@media(min-width:1024px){.fp-grid{grid-template-columns:240px 1fr}}
.floor-sel{border-top:1px solid var(--gold-b);border-right:1px solid var(--gold-b);padding-right:2rem;margin-bottom:2.5rem}
@media(min-width:1024px){.floor-sel{margin-bottom:0}}
.floor-btn{width:100%;text-align:left;border-bottom:1px solid var(--gold-b);padding:1.25rem 0;display:flex;flex-direction:column;gap:4px;transition:opacity .3s;background:none}
.floor-btn.inactive{opacity:.3}.floor-btn.inactive:hover{opacity:.55}
.floor-range{font-family:var(--sans);font-size:9px;letter-spacing:.35em;text-transform:uppercase;transition:color .3s;color:rgba(255,255,255,.3)}
.floor-btn.active .floor-range{color:var(--gold)}
.floor-lbl{font-family:var(--serif);font-weight:300;font-size:16px;transition:color .3s;color:rgba(255,255,255,.6)}
.floor-btn.active .floor-lbl{color:#fff}
.floor-viewer{padding-left:0}
@media(min-width:1024px){.floor-viewer{padding-left:2.5rem}}
.floor-panel{display:none}
.floor-panel.active{display:grid;animation:fadeIn .4s ease}
@media(min-width:768px){.floor-panel.active{grid-template-columns:1.2fr 1fr;gap:2.5rem}}
.svg-box{border:1px solid var(--gold-b);background:var(--bg);padding:1.5rem;display:flex;align-items:center;justify-content:center;min-height:240px}
.floor-spec-hd{margin-bottom:1.5rem}
.floor-spec-hd .eyebrow{margin-bottom:4px;display:block}
.floor-spec-hd h3{font-family:var(--serif);font-weight:300;color:#fff;font-size:1.5rem}
.spec-table{border-top:1px solid var(--gold-b)}
.spec-row{border-bottom:1px solid var(--gold-b);padding:1rem 0;display:grid;grid-template-columns:120px 1fr;gap:1rem}
.spec-key{font-family:var(--sans);font-size:9px;letter-spacing:.28em;text-transform:uppercase;color:rgba(255,255,255,.25)}
.spec-val{font-family:var(--sans);font-size:14px;color:rgba(255,255,255,.65)}
.office-features{background:var(--bg2);border-top:1px solid var(--gold-b);padding:clamp(4rem,8vw,6rem) 0}
.feat-grid{display:grid;gap:1px;background:var(--gold-b);margin-top:3rem}
@media(min-width:768px){.feat-grid{grid-template-columns:repeat(3,1fr)}}
.feat-card{background:var(--bg2);padding:2.5rem 2rem}
.feat-num{font-family:var(--sans);font-size:9px;letter-spacing:.4em;color:rgba(201,168,102,.35);margin-bottom:.75rem}
.feat-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:1.1rem;margin-bottom:.75rem}
.feat-desc{font-family:var(--sans);font-size:13px;color:rgba(255,255,255,.3);line-height:1.6}
</style>"""

off_body = f"""<div class="page-header">
  <div class="container">
    <p class="page-header-eyebrow">Office</p>
    <h1>Grade-A<br><em>Office Floors</em></h1>
    <p>93,700 SQM of premium column-free workspace across two towers, L6 to L38, with full-height glazing and panoramic city views.</p>
  </div>
</div>
<section style="background:var(--bg2);padding:clamp(6rem,12vw,9rem) 0;border-top:1px solid var(--gold-b)">
  <div class="container">
    <div class="fp-header">
      <p class="eyebrow" style="margin-bottom:1rem">Layouts</p>
      <h2 class="section-title">Floor<br><em>Plans</em></h2>
    </div>
    <div class="fp-grid">
      <div class="floor-sel">{floor_btns()}</div>
      <div class="floor-viewer">{floor_panels()}</div>
    </div>
  </div>
</section>
<section class="office-features">
  <div class="container">
    <p class="eyebrow" style="margin-bottom:1rem">Specifications</p>
    <h2 class="section-title">Built For<br><em>Excellence</em></h2>
    <div class="feat-grid">
      <div class="feat-card fade-up"><p class="feat-num">01</p><h3 class="feat-title">Column-Free Floorplates</h3><p class="feat-desc">Open-plan layouts with zero internal columns allow complete flexibility in workspace configuration.</p></div>
      <div class="feat-card fade-up" style="transition-delay:.08s"><p class="feat-num">02</p><h3 class="feat-title">Full-Height Glazing</h3><p class="feat-desc">Floor-to-ceiling glass on all four elevations maximises natural light and panoramic views.</p></div>
      <div class="feat-card fade-up" style="transition-delay:.16s"><p class="feat-num">03</p><h3 class="feat-title">NBF Fresh Air System</h3><p class="feat-desc">Compliant with the National Building Framework, delivering superior indoor air quality for occupant wellbeing.</p></div>
      <div class="feat-card fade-up" style="transition-delay:.24s"><p class="feat-num">04</p><h3 class="feat-title">Raised Access Floors</h3><p class="feat-desc">600 mm module raised-access flooring throughout for flexible MEP distribution and future-proofing.</p></div>
      <div class="feat-card fade-up" style="transition-delay:.32s"><p class="feat-num">05</p><h3 class="feat-title">BMS Integration</h3><p class="feat-desc">Building management system controls HVAC, lighting, and security from a centralised dashboard.</p></div>
      <div class="feat-card fade-up" style="transition-delay:.4s"><p class="feat-num">06</p><h3 class="feat-title">24/7 Security</h3><p class="feat-desc">Turnstile access control, CCTV, on-site security team, and visitor management system.</p></div>
    </div>
  </div>
</section>"""

off_js = """<script>
let aF=2;
function setFloor(i){if(i===aF)return;aF=i;
  document.querySelectorAll('.floor-btn').forEach((b,x)=>{b.classList.toggle('active',x===i);b.classList.toggle('inactive',x!==i)});
  document.querySelectorAll('.floor-panel').forEach((p,x)=>p.classList.toggle('active',x===i));
}
</script>"""

# ══════════════════════════════════
# sustainability.html
# ══════════════════════════════════
sus_css = """<style>
.sus-banner{position:relative;height:clamp(280px,40vw,520px);overflow:hidden}
.sus-banner img{width:100%;height:100%;object-fit:cover;object-position:center}
.sus-banner-ov{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(11,11,9,.5),transparent 50%,rgba(11,11,9,.7))}
.sus-banner-txt{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center}
.sus-banner-txt p{font-family:var(--serif);font-weight:300;color:rgba(255,255,255,.75);font-size:clamp(.9rem,2.5vw,1.4rem);letter-spacing:.25em}
.leed-strip{border-top:1px solid var(--gold-b);border-bottom:1px solid var(--gold-b);background:var(--bg)}
.leed-grid{display:grid}
@media(min-width:768px){.leed-grid{grid-template-columns:1fr 1fr}}
.leed-card{padding:clamp(3rem,6vw,5rem) 0;border-bottom:1px solid var(--gold-b)}
@media(min-width:768px){
  .leed-card{border-bottom:none;border-right:1px solid var(--gold-b);padding:clamp(3rem,6vw,5rem) 3rem}
  .leed-card:last-child{border-right:none;padding-right:0}
  .leed-card:first-child{padding-left:0}
}
.leed-card:last-child{border-bottom:none}
.leed-badge-label{font-family:var(--sans);font-size:9px;letter-spacing:.45em;text-transform:uppercase;color:var(--gold)}
.leed-card h3{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(1.3rem,2.5vw,1.8rem);margin-top:12px;line-height:1.1}
.leed-card p{color:rgba(255,255,255,.3);font-size:14px;margin-top:1rem;line-height:1.75}
.metrics-section{background:var(--bg2);padding:clamp(6rem,12vw,9rem) 0;border-top:1px solid var(--gold-b)}
.metrics-grid{display:grid;gap:1px;background:var(--gold-b);margin-top:3rem}
@media(min-width:768px){.metrics-grid{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1024px){.metrics-grid{grid-template-columns:repeat(4,1fr)}}
.metric-cell{background:var(--bg2);padding:2.5rem 2rem;display:flex;flex-direction:column;gap:.5rem}
.metric-val{font-family:var(--serif);font-weight:300;color:var(--gold);font-size:clamp(2rem,3.5vw,2.8rem)}
.metric-key{font-family:var(--sans);font-size:9px;letter-spacing:.38em;text-transform:uppercase;color:rgba(255,255,255,.25)}
.metric-desc{font-family:var(--sans);font-size:12px;color:rgba(255,255,255,.2);line-height:1.5;margin-top:.25rem}
</style>"""

sus_body = """<div class="page-header">
  <div class="container">
    <p class="page-header-eyebrow">Sustainability</p>
    <h1>Dual<br><em>LEED Certified</em></h1>
    <p>Capital Place is one of the very few buildings in Vietnam to hold two LEED certifications simultaneously &mdash; Platinum and Gold &mdash; reflecting the highest global standards in sustainable design and operations.</p>
  </div>
</div>
<div class="sus-banner">
  <img src="https://images.unsplash.com/photo-1435575653489-b0873ec954e2?w=1800&h=1200&fit=crop&auto=format" alt="Capital Place facade" loading="lazy"/>
  <div class="sus-banner-ov"></div>
  <div class="sus-banner-txt"><p>DUAL LEED CERTIFIED &nbsp;&middot;&nbsp; GRADE A OFFICES &nbsp;&middot;&nbsp; HANOI</p></div>
</div>
<section class="leed-strip">
  <div class="container">
    <div class="leed-grid">
      <div class="leed-card fade-up">
        <span class="leed-badge-label">LEED Platinum</span>
        <h3>Operations &amp; Maintenance</h3>
        <p>The highest possible rating for building operations &mdash; recognising outstanding performance in energy efficiency, water conservation, occupant wellbeing, and indoor environment quality.</p>
        <p style="margin-top:1rem">Capital Place achieves Platinum through continuous monitoring of all building systems, occupant surveys, and annual performance reviews against USGBC benchmarks.</p>
      </div>
      <div class="leed-card fade-up" style="transition-delay:.12s">
        <span class="leed-badge-label">LEED Gold</span>
        <h3>Building Design &amp; Construction</h3>
        <p>Sustainability was embedded from day one &mdash; not retrofitted. Every material, system, and structural decision was evaluated against LEED BD+C criteria during design and construction phases.</p>
        <p style="margin-top:1rem">From low-VOC materials and high-performance glazing to stormwater management and construction waste reduction, Capital Place was built with the future in mind.</p>
      </div>
    </div>
  </div>
</section>
<section class="metrics-section">
  <div class="container">
    <p class="eyebrow" style="margin-bottom:1rem">Performance</p>
    <h2 class="section-title">Measured<br><em>Impact</em></h2>
    <div class="metrics-grid">
      <div class="metric-cell fade-up"><span class="metric-val">35%</span><span class="metric-key">Energy Reduction</span><span class="metric-desc">vs ASHRAE 90.1 baseline through high-performance HVAC and building envelope</span></div>
      <div class="metric-cell fade-up" style="transition-delay:.08s"><span class="metric-val">40%</span><span class="metric-key">Water Savings</span><span class="metric-desc">Through low-flow fixtures, cooling tower optimisation, and rainwater reuse</span></div>
      <div class="metric-cell fade-up" style="transition-delay:.16s"><span class="metric-val">90%</span><span class="metric-key">Construction Waste Diverted</span><span class="metric-desc">Recycled or reused &mdash; keeping materials out of landfill during build phase</span></div>
      <div class="metric-cell fade-up" style="transition-delay:.24s"><span class="metric-val">100%</span><span class="metric-key">Daylight &amp; Views</span><span class="metric-desc">Regularly occupied spaces achieve LEED credits for daylight and quality views</span></div>
    </div>
  </div>
</section>"""

# ══════════════════════════════════
# amenities.html
# ══════════════════════════════════
am_css = """<style>
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.am-mosaic{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(201,168,102,.08)}
@media(min-width:768px){.am-mosaic{grid-template-columns:repeat(3,1fr)}}
.am-card{position:relative;overflow:hidden;background:var(--card);cursor:pointer;min-height:200px}
.am-card.tall{grid-row:span 2;min-height:280px}
@media(min-width:768px){.am-card.tall{min-height:0}}
.am-card img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .7s ease}
.am-card:hover img{transform:scale(1.06)}
.am-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(10,10,8,.9) 0%,rgba(10,10,8,.2) 50%,transparent 100%);transition:background .5s}
.am-card:hover .am-ov{background:linear-gradient(to top,rgba(10,10,8,.9) 0%,rgba(10,10,8,.25) 50%,rgba(201,168,102,.05) 100%)}
.am-info{position:absolute;bottom:0;left:0;right:0;padding:clamp(1.5rem,3vw,2rem)}
.am-sub{font-family:var(--sans);font-size:9px;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);margin-bottom:6px}
.am-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(1.1rem,2vw,1.4rem);line-height:1.2}
#leasing{background:var(--bg2);padding:clamp(6rem,12vw,9rem) 0;border-top:1px solid var(--gold-b)}
.ls-grid{display:grid;gap:4rem}
@media(min-width:1024px){.ls-grid{grid-template-columns:1fr 1.3fr;gap:5rem}}
.ls-title{font-family:var(--serif);font-weight:300;color:#fff;font-size:clamp(2rem,4vw,3.2rem);line-height:.9;margin-bottom:2.5rem}
.ls-title em{color:var(--gold);font-style:italic}
.ls-desc{color:rgba(255,255,255,.28);font-size:14px;max-width:280px;line-height:1.7;margin-bottom:3rem}
.ct-links{display:flex;flex-direction:column;gap:1.25rem}
.ct-link{display:flex;align-items:center;gap:1rem}
.ct-icon{width:36px;height:36px;border:1px solid rgba(201,168,102,.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:border-color .3s}
.ct-link:hover .ct-icon{border-color:var(--gold)}
.ct-icon svg{width:12px;height:12px;color:var(--gold)}
.ct-text{color:rgba(255,255,255,.4);font-size:14px;transition:color .3s}
.ct-link:hover .ct-text{color:rgba(255,255,255,.7)}
.ls-addr{margin-top:3rem;padding-top:2.5rem;border-top:1px solid var(--gold-b)}
.ls-addr p{color:rgba(255,255,255,.18);font-size:12px;line-height:2}
.enq-form{display:flex;flex-direction:column;gap:1.75rem}
.field label{display:block;font-family:var(--sans);font-size:9px;letter-spacing:.42em;text-transform:uppercase;color:rgba(255,255,255,.22);margin-bottom:10px}
.field input,.field textarea{width:100%;background:transparent;border:none;border-bottom:1px solid rgba(201,168,102,.15);color:#fff;font-size:14px;font-family:var(--sans);padding:10px 0;outline:none;caret-color:var(--gold);transition:border-color .3s;resize:none}
.field input:focus,.field textarea:focus{border-color:var(--gold)}
.btn-submit{width:100%;border:1px solid var(--gold);color:var(--gold);padding:16px;font-size:10px;letter-spacing:.42em;text-transform:uppercase;font-family:var(--sans);transition:background .3s,color .3s;margin-top:8px}
.btn-submit:hover{background:var(--gold);color:var(--bg)}
#success-msg{display:none;border:1px solid rgba(201,168,102,.12);min-height:360px;padding:3.5rem;align-items:center;justify-content:center;text-align:center}
#success-msg.show{display:flex}
.succ-line{width:40px;height:1px;background:var(--gold);margin:0 auto 1.5rem}
#success-msg .eyebrow{margin-bottom:12px;display:block}
#success-msg p{color:rgba(255,255,255,.3);font-size:14px}
</style>"""

am_body = """<div class="page-header">
  <div class="container">
    <p class="page-header-eyebrow">Amenities</p>
    <h1>World-Class<br><em>Facilities</em></h1>
    <p>Every amenity is designed to elevate the working experience &mdash; from the triple-height grand lobby to the 360&deg; sky lounge on Level 39.</p>
  </div>
</div>
<section style="background:var(--bg);padding:clamp(6rem,12vw,9rem) 0">
  <div class="container">
    <p class="eyebrow" style="margin-bottom:3rem">All Amenities</p>
    <div class="am-mosaic">
      <div class="am-card tall"><img src="https://images.unsplash.com/photo-1780369088190-914cc3eee938?w=1200&h=900&fit=crop&auto=format" alt="Grand Lobby" loading="lazy"/><div class="am-ov"></div><div class="am-info"><p class="am-sub">Triple-height atrium</p><h3 class="am-title">Grand Lobby</h3></div></div>
      <div class="am-card"><img src="https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=1200&h=900&fit=crop&auto=format" alt="Fitness" loading="lazy"/><div class="am-ov"></div><div class="am-info"><p class="am-sub">Gym &middot; Yoga &middot; Spa showers</p><h3 class="am-title">Fitness &amp; Wellness</h3></div></div>
      <div class="am-card"><img src="https://images.unsplash.com/photo-1587702068694-a909ef4aa346?w=1200&h=900&fit=crop&auto=format" alt="Dining" loading="lazy"/><div class="am-ov"></div><div class="am-info"><p class="am-sub">Ground &amp; Podium levels</p><h3 class="am-title">Dining &amp; Retail</h3></div></div>
      <div class="am-card"><img src="https://images.unsplash.com/photo-1758193431353-87812fbff5cd?w=1200&h=900&fit=crop&auto=format" alt="Sky Lounge" loading="lazy"/><div class="am-ov"></div><div class="am-info"><p class="am-sub">Level 39 &middot; 360&deg; panorama</p><h3 class="am-title">Sky Lounge</h3></div></div>
      <div class="am-card"><img src="https://images.unsplash.com/photo-1768312783857-072ef0b3eea2?w=1200&h=900&fit=crop&auto=format" alt="Conference" loading="lazy"/><div class="am-ov"></div><div class="am-info"><p class="am-sub">Event halls &amp; breakout</p><h3 class="am-title">Conference Centre</h3></div></div>
    </div>
  </div>
</section>
<section id="leasing">
  <div class="container">
    <div class="ls-grid">
      <div>
        <p class="eyebrow" style="margin-bottom:1rem">Contact</p>
        <h2 class="ls-title">Leasing<br><em>Enquiries</em></h2>
        <p class="ls-desc">Our team is available to discuss floor plates, fit-out contributions, and tailored tenancy arrangements.</p>
        <div class="ct-links">
          <a href="tel:18009289" class="ct-link"><span class="ct-icon"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg></span><span class="ct-text">1800 9289</span></a>
          <a href="mailto:leasing@capitalplace.com.vn" class="ct-link"><span class="ct-icon"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg></span><span class="ct-text">leasing@capitalplace.com.vn</span></a>
        </div>
        <div class="ls-addr"><p>29 Lieu Giai Street<br>Ngoc Ha, Ba Dinh<br>Hanoi, Vietnam</p></div>
      </div>
      <div>
        <div id="success-msg"><div><div class="succ-line"></div><span class="eyebrow">Enquiry Received</span><p>Our leasing team will contact you within 24 hours.</p></div></div>
        <form class="enq-form" id="enq-form" onsubmit="submitForm(event)">
          <div class="field"><label for="fn">Full Name</label><input type="text" id="fn" required/></div>
          <div class="field"><label for="fc">Company</label><input type="text" id="fc" required/></div>
          <div class="field"><label for="fe">Email</label><input type="email" id="fe" required/></div>
          <div class="field"><label for="fp">Phone</label><input type="tel" id="fp" required/></div>
          <div class="field"><label for="fm">Message</label><textarea id="fm" rows="3"></textarea></div>
          <button type="submit" class="btn-submit">Submit Enquiry</button>
        </form>
      </div>
    </div>
  </div>
</section>"""

am_js = """<script>
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

for fname, content in pages.items():
    path = os.path.join(ROOT, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{fname}: {len(content):,} bytes")

print("Done!")
