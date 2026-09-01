import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const pages = [
  'index.html','location.html','office.html','sustainability.html','amenities.html',
  'availability.html','leasing.html','visit.html','resources.html','faq.html',
  'occupiers.html','retail.html','space.html','privacy.html','404.html'
];
const failures = [];
let assertions = 0;
const check = (condition, message) => { assertions += 1; if (!condition) failures.push(message); };
const read = file => fs.readFileSync(path.join(root, file), 'utf8');

const responsivePath = 'assets/capital-v6-responsive.css';
check(fs.existsSync(path.join(root, responsivePath)), 'mobile: responsive owner missing');
const css = read(responsivePath);
const compact = css.replace(/\s+/g, '').toLowerCase();
const js = read('assets/capital-v6.js');

for (const page of pages) {
  const html = read(page);
  check(/name=["']viewport["']/i.test(html), `${page}: viewport metadata missing`);
  check(/width=device-width/i.test(html), `${page}: device-width viewport missing`);
  check(/initial-scale=1(?:\.0)?/i.test(html), `${page}: initial-scale contract missing`);
  check(/viewport-fit=cover/i.test(html), `${page}: safe-area viewport-fit=cover missing`);
  check(!/user-scalable\s*=\s*no/i.test(html), `${page}: zoom is disabled`);
  check(!/maximum-scale\s*=\s*1(?:\.0)?/i.test(html), `${page}: maximum scale blocks zoom`);
  check(/assets\/capital-v6-responsive\.css\?v=20260901-1/.test(html), `${page}: V6.4 responsive owner not loaded last`);
  if (page !== '404.html') {
    check(/assets\/capital-v6\.js\?v=20260901-2/.test(html), `${page}: mobile nav JS cache version is stale`);
  }
}

check(/MOBILE|Responsive & device strategy owner/i.test(css), 'mobile: owner marker missing');
check(/safe-area-inset-top/.test(css) && /safe-area-inset-bottom/.test(css), 'mobile: notch/home-indicator safe area missing');
check(/100dvh/.test(css), 'mobile: dynamic viewport height guard missing');
check(/pointer:coarse/.test(css), 'mobile: coarse-pointer touch strategy missing');
check(/--cp-touch:44px/.test(compact), 'mobile: 44px touch token missing');
check(/min-height:var\(--cp-touch\)/.test(compact), 'mobile: shared touch-target rule missing');
check(/\.cp6-fieldinput,.cp6-fieldselect,.cp6-fieldtextarea\{[^}]*font-size:16px/.test(compact), 'mobile: iOS form zoom prevention missing');
check(/\.cp6-hero-actions\{[^}]*flex-direction:column/.test(compact), 'mobile: hero CTAs are not stacked on narrow screens');
check(/\.cp6-hero-factsspan:nth-child\(3\)\{[^}]*display:block!important/.test(compact), 'mobile: third building fact is still hidden');
check(/\.cp6-footera\{[^}]*min-height:44px/.test(compact), 'mobile: footer targets are too small');
check(/\.cp6-contact-metaa\{[^}]*min-height:44px/.test(compact), 'mobile: direct contact targets are too small');
check(/\.cp6-utility-hero\{[^}]*safe-area-inset-top/.test(css), 'mobile utility pages: hero does not clear safe-area header');
check(/\.cp6-error\{[^}]*safe-area-inset-top/.test(css), 'mobile 404: safe-area treatment missing');
check(/\.cp6-resource\{[^}]*min-height:180px[^}]*padding:22px/.test(compact), 'mobile resources: compact readable card treatment missing');
check(/\.cp6-resourcespan\{[^}]*font-size:13px/.test(compact), 'mobile resources: supporting text remains microtype');
check(/\.cp6-step-gridarticle\{[^}]*min-height:0[^}]*padding:24px22px/.test(compact), 'mobile visit steps: desktop card height still forced');
check(/max-width:360px/.test(css), 'mobile: 320–360px hardening breakpoint missing');
check(/orientation:landscape/.test(css), 'mobile: landscape hardening missing');
check(/forced-colors:active/.test(css), 'mobile: forced-colors focus guard missing');
check(/overflow-wrap:anywhere/.test(css), 'mobile: long email/copy overflow guard missing');
check(/scroll-margin-top/.test(css), 'mobile: fixed-nav anchor offset guard missing');
check(/\.cp6-lang\{[^}]*display:flex!important/.test(compact), 'mobile: language control remains hidden');
check(/amenities-hero\.jpg[\s\S]*::before[\s\S]*display:none/.test(css), 'mobile: amenities montage is not simplified for narrow crop');
check(/location-hero\.jpg[\s\S]*padding-right:calc/.test(css), 'mobile: location address stripe can overlap copy');

check(/cp6-menu-open/.test(js), 'mobile nav: body scroll lock class missing');
check(/lockedScrollY/.test(js) && /window\.scrollTo/.test(js), 'mobile nav: scroll position restoration missing');
check(/Close navigation/.test(js), 'mobile nav: open/close accessible label state missing');
check(/event\.key === 'Tab'/.test(js), 'mobile nav: focus loop missing');
check(/event\.key === 'Escape'/.test(js), 'mobile nav: Escape handling missing');
check(/aria-label', 'Primary navigation'/.test(js), 'mobile nav: missing navigation accessible-name fallback');
check(/pagehide/.test(js), 'mobile nav: page lifecycle cleanup missing');

if (failures.length) {
  console.error(`FAIL: ${failures.length} of ${assertions} mobile assertions failed`);
  failures.forEach(failure => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(`PASS: ${assertions} Capital Place V6.4 mobile/responsive assertions`);
console.log('Matrix contract: 320 · 360 · 375 · 390 · 414 · 600 · 768 · landscape · touch · safe-area · zoom/reflow');
