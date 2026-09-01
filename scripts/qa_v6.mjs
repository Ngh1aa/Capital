import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const pages = ['index.html','location.html','office.html','sustainability.html','amenities.html','availability.html','leasing.html'];
const failures = [];
let assertions = 0;
const check = (condition, message) => { assertions++; if (!condition) failures.push(message); };
const exists = p => fs.existsSync(path.join(root,p));

check(exists('assets/capital-v6.css'),'missing capital-v6.css');
check(exists('assets/capital-v6.js'),'missing capital-v6.js');
check(exists('docs/DESIGN-CONTRACT-V6.md'),'missing V6 design contract');
check(exists('docs/design-reference-benchmark-v6.md'),'missing V6 reference benchmark');

for (const page of pages) {
  check(exists(page), `${page}: missing`);
  if (!exists(page)) continue;
  const html = fs.readFileSync(path.join(root,page),'utf8');
  check(/<body\s+class="cp6"/.test(html), `${page}: not on V6 body system`);
  check(/assets\/capital-v6\.css\?v=20260901-1/.test(html), `${page}: missing explicit V6 CSS version`);
  check(/assets\/capital-v6\.js\?v=20260901-1/.test(html), `${page}: missing explicit V6 JS version`);
  check(!/capital-uiux-v2\.css/.test(html), `${page}: still loads legacy UIUX wrapper`);
  check(!/capital-art-direction-v5\.css/.test(html), `${page}: still loads v5 patch layer`);
  check(/class="cp6-brand"/.test(html), `${page}: missing architectural brand podium`);
  check(/class="cp6-nav-cta"/.test(html), `${page}: missing primary leasing CTA`);
  check(/<main\s+id="main-content"/.test(html), `${page}: missing main landmark`);
  check(/class="cp6-footer"/.test(html), `${page}: missing V6 footer`);

  for (const match of html.matchAll(/(?:src|href)="([^"#?]+)(?:[?#][^"]*)?"/g)) {
    const ref = match[1];
    if (!ref || /^(https?:|mailto:|tel:|javascript:)/.test(ref)) continue;
    const local = ref.endsWith('/') ? `${ref}index.html` : ref;
    check(exists(local), `${page}: missing local reference ${ref}`);
  }
}

const css = fs.readFileSync(path.join(root,'assets/capital-v6.css'),'utf8');
check(/--cp-orange:#f15f22/i.test(css),'V6: Capital orange role missing');
check(/\.cp6-nav\{[^}]*background:rgba\(24,22,21/i.test(css.replace(/\s+/g,'')),'V6: nav is not locked dark');
check(/\.cp6-brand\{[^}]*background:#141312/i.test(css.replace(/\s+/g,'')),'V6: logo podium missing dark background');
check(/\.cp6-nav-cta\{[^}]*background:var\(--cp-orange\)/i.test(css.replace(/\s+/g,'')),'V6: primary nav CTA not solid orange');
check(/@media\(max-width:900px\)/.test(css.replace(/\s+/g,'')),'V6: missing tablet/mobile composition breakpoint');
check(/@media\(max-width:600px\)/.test(css.replace(/\s+/g,'')),'V6: missing mobile composition breakpoint');
check(/prefers-reduced-motion/.test(css),'V6: reduced motion guard missing');

const availability = fs.readFileSync(path.join(root,'availability.html'),'utf8');
check(/does not publish an unverified live vacancy list/i.test(availability),'availability: missing explicit reality statement');
check(/Current availability confirmed on request/i.test(availability),'availability: missing current-status truth');
check(!/Book this floor|Book a tour/i.test(availability),'availability: contains booking language without booking system');

const leasing = fs.readFileSync(path.join(root,'leasing.html'),'utf8');
check(/Prepare Leasing Email/.test(leasing),'leasing: action is not described as email preparation');
check(/does not transmit your data to a CRM or booking system/i.test(leasing),'leasing: missing prototype system-reality disclosure');
check(/mailto:leasing@capitalplace\.vn/.test(leasing),'leasing: mailto handoff missing');

if (failures.length) {
  console.error(`FAIL: ${failures.length} of ${assertions} V6 assertions failed`);
  failures.forEach(f => console.error(`- ${f}`));
  process.exit(1);
}
console.log(`PASS: ${assertions} Capital Place V6 design-contract assertions`);
console.log(`Core routes: ${pages.length} · System: Architectural Editorial × Leasing Blueprint`);
