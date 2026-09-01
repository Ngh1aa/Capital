import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const pages = ['index.html','location.html','office.html','sustainability.html','amenities.html','availability.html','leasing.html','visit.html','resources.html','faq.html','occupiers.html','retail.html','space.html','privacy.html','404.html'];
const utilityPages = new Set(['visit.html','resources.html','faq.html','occupiers.html','retail.html','space.html','privacy.html','404.html']);
const remediatedPages = new Set(['index.html','office.html','sustainability.html','amenities.html','availability.html']);
const failures = [];
let assertions = 0;
const check = (condition, message) => { assertions++; if (!condition) failures.push(message); };
const exists = p => fs.existsSync(path.join(root,p));

check(exists('assets/capital-v6.css'),'missing capital-v6.css');
check(exists('assets/capital-v6-utility.css'),'missing capital-v6-utility.css');
check(exists('assets/capital-v6.js'),'missing capital-v6.js');
check(exists('docs/DESIGN-CONTRACT-V6.md'),'missing V6 design contract');
check(exists('docs/design-reference-benchmark-v6.md'),'missing V6 reference benchmark');
check(exists('docs/HERO-SYSTEM-V6.2.md'),'missing hero-system contract');

for (const page of pages) {
  check(exists(page), `${page}: missing`);
  if (!exists(page)) continue;
  const html = fs.readFileSync(path.join(root,page),'utf8');
  check(/<body\s+class="cp6"/.test(html), `${page}: not on V6 body system`);
  check(/assets\/capital-v6\.css\?v=20260901-(?:1|3)/.test(html), `${page}: missing explicit V6 CSS version`);
  if (remediatedPages.has(page)) check(/assets\/capital-v6\.css\?v=20260901-3/.test(html), `${page}: rendered-QA remediation is not cache-busted`);
  check(!/capital-uiux-v2\.css/.test(html), `${page}: still loads legacy UIUX wrapper`);
  check(!/capital-art-direction-v5\.css/.test(html), `${page}: still loads v5 patch layer`);
  check(!/assets\/(style|capital-upgrade|capital-white|capital-visual|home-cinematic|office-cinematic|location-cinematic|amenities-cinematic|sustainability-cinematic|availability-cinematic)\.css/.test(html), `${page}: still loads legacy/page-patch CSS`);
  if (utilityPages.has(page)) check(/assets\/capital-v6-utility\.css\?v=20260901-1/.test(html), `${page}: missing V6 utility layer`);

  if (page !== '404.html') {
    check(/class="cp6-brand"/.test(html), `${page}: missing architectural brand podium`);
    check(/class="cp6-nav-cta"/.test(html), `${page}: missing primary leasing CTA`);
    check(/<main\s+id="main-content"/.test(html), `${page}: missing main landmark`);
    check(/class="cp6-footer"/.test(html), `${page}: missing V6 footer`);
    check(/assets\/capital-v6\.js\?v=20260901-1/.test(html), `${page}: missing explicit V6 JS version`);
  }

  for (const match of html.matchAll(/(?:src|href|action)="([^"#?]+)(?:[?#][^"]*)?"/g)) {
    const ref = match[1];
    if (!ref || /^(https?:|mailto:|tel:|javascript:)/.test(ref)) continue;
    const local = ref.endsWith('/') ? `${ref}index.html` : ref;
    check(exists(local), `${page}: missing local reference ${ref}`);
  }
}

const css = fs.readFileSync(path.join(root,'assets/capital-v6.css'),'utf8');
const compact = css.replace(/\s+/g,'').toLowerCase();
check(compact.includes('--cp-orange:#f15f22'),'V6: Capital orange role missing');
check(compact.includes('.cp6-nav{') && compact.includes('background:rgba(24,22,21,.96)'), 'V6: nav is not locked dark');
check(compact.includes('.cp6-brand{') && compact.includes('background:#141312'), 'V6: logo podium missing dark background');
check(compact.includes('.cp6-nav-cta{display:inline-flex') && compact.includes('background:var(--cp-orange)'), 'V6: primary nav CTA not solid orange');
check(compact.includes('@media(max-width:900px)'), 'V6: missing tablet/mobile composition breakpoint');
check(compact.includes('@media(max-width:600px)'), 'V6: missing mobile composition breakpoint');
check(/prefers-reduced-motion/.test(css),'V6: reduced motion guard missing');

// Hero matrix: core decision pages must not collapse into one copy-left/image-right template.
check(/HERO MATRIX V6\.3/.test(css),'V6.3: hero matrix marker missing');
const heroAssets = {
  'location.html':'location-hero.jpg',
  'office.html':'office-hero.jpg',
  'sustainability.html':'sustainability-hero.jpg',
  'amenities.html':'amenities-hero.jpg',
  'availability.html':'capital-place-towers.jpg',
  'leasing.html':'architecture-lobby-official.jpg'
};
const seenHeroSources = new Set();
for (const [page,asset] of Object.entries(heroAssets)) {
  const html = fs.readFileSync(path.join(root,page),'utf8');
  check(html.includes(asset), `${page}: expected hero source ${asset} missing`);
  check(css.includes(`img[src*="${asset}"]`), `${page}: missing page-role hero selector for ${asset}`);
  const match = html.match(/cp6-page-hero-media[^>]*>\s*<img[^>]+src="([^"]+)"/);
  if (match) seenHeroSources.add(match[1]);
}
check(seenHeroSources.size === Object.keys(heroAssets).length,'V6.3: core pages reuse the same hero media source');
check(/PUBLISHED PLANNING REFERENCE\s*\/\s*1,847 SQM/.test(css),'office hero: planning-reference signature missing');
check(/PLATINUM\s+·\s+LEED O\+M/.test(css) && /GOLD\s+·\s+LEED BD\+C/.test(css),'sustainability hero: compact certification labels missing');
check(/08:00\s+ARRIVE/.test(css) && /18:00\s+RECHARGE/.test(css),'amenities hero: workday signature missing');
check(/AVAILABILITY\s*\/\s*CONFIRMED BY LEASING/.test(css),'availability hero: leasing-truth signature missing');
check(/1800 9289/.test(css) && /LEASING@CAPITALPLACE\.VN/.test(css),'leasing hero: direct-contact signature missing');

// Rendered-QA regression guards from stakeholder screenshots, 2026-09-01.
check(css.includes('body.cp6 a.cp6-experience-card{color:#fff!important}'),'image cards: anchor inherit can override white overlay copy');
check(/\.cp6-experience-card div\{[^}]*background:rgba\(17,16,15,\.76\)/.test(css),'image cards: local contrast backplate missing behind copy');
check(/\.cp6-experience-card h3\{[^}]*color:#fff!important/.test(css),'image cards: heading color is not locked readable over photography');
check(/\.cp6-floor-sheet img\{[^}]*max-width:min\(100%,430px\)/.test(css),'floor preview: tiny raster is allowed to upscale excessively');
check(/\.cp6-plate-compare figure img\{[^}]*max-width:min\(100%,430px\)/.test(css),'availability floor preview: tiny raster is allowed to upscale excessively');
check(!/floor-standard\.png\) center\/contain no-repeat/.test(css),'hero: low-resolution floor-standard.png is still enlarged as a hero/background');
check(!/PLATINUM\\A O\+M/.test(css) && !/GOLD\\A BD\+C/.test(css),'sustainability: old multiline pseudo-label pattern that overlapped remains');
check(/bottom:74px/.test(css) && /bottom:16px/.test(css),'sustainability mobile: credential labels lack separated vertical positions');
check(/brightness\(\.8\)/.test(css),'sustainability: hero imagery remains excessively dimmed');

const index = fs.readFileSync(path.join(root,'index.html'),'utf8');
check(/A beacon for modern Hanoi/i.test(index),'home: landmark positioning missing');
check(/1,847/.test(index) && /floor-standard\.png/.test(index),'home: published floor-plan decision object missing');
check(/The Nexus/.test(index) && /The Link/.test(index),'home: workday proposition missing');

const availability = fs.readFileSync(path.join(root,'availability.html'),'utf8');
check(/does not publish an unverified live vacancy list/i.test(availability),'availability: missing explicit reality statement');
check(/Current availability confirmed on request/i.test(availability),'availability: missing current-status truth');
check(!/Book this floor|Book a tour/i.test(availability),'availability: contains booking language without booking system');

const leasing = fs.readFileSync(path.join(root,'leasing.html'),'utf8');
check(/Prepare Leasing Email/.test(leasing),'leasing: action is not described as email preparation');
check(/does not transmit your data to a CRM or booking system/i.test(leasing),'leasing: missing prototype system-reality disclosure');
check(/mailto:leasing@capitalplace\.vn/.test(leasing),'leasing: mailto handoff missing');

const privacy = fs.readFileSync(path.join(root,'privacy.html'),'utf8');
check(/static prototype/i.test(privacy) && /official policy/i.test(privacy),'privacy: missing prototype/first-party distinction');

const js = fs.readFileSync(path.join(root,'assets/capital-v6.js'),'utf8');
check(/aria-controls/.test(js) && /Escape/.test(js),'V6: mobile navigation semantics/escape handling missing');

if (failures.length) {
  console.error(`FAIL: ${failures.length} of ${assertions} V6 assertions failed`);
  failures.forEach(f => console.error(`- ${f}`));
  process.exit(1);
}
console.log(`PASS: ${assertions} Capital Place V6.3 design-contract and rendered-QA regression assertions`);
console.log(`Routes: ${pages.length} · System: Architectural Editorial × Leasing Blueprint · Hero matrix: 6 core archetypes`);