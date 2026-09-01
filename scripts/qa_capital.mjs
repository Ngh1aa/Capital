import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const pages = [
  'index.html', 'location.html', 'office.html', 'sustainability.html', 'amenities.html',
  'availability.html', 'space.html', 'leasing.html', 'visit.html', 'resources.html',
  'retail.html', 'occupiers.html', 'faq.html', 'privacy.html', '404.html'
];
const failures = [];
let assertions = 0;

function assert(condition, message) {
  assertions += 1;
  if (!condition) failures.push(message);
}
function stripQuery(value) { return value.split('?')[0].split('#')[0]; }
function isRemote(value) { return /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(value); }
function read(file) { return fs.readFileSync(path.join(root, file), 'utf8'); }

const htmlByPage = new Map();
for (const page of pages) {
  const file = path.join(root, page);
  assert(fs.existsSync(file), `${page}: file is missing`);
  if (fs.existsSync(file)) htmlByPage.set(page, fs.readFileSync(file, 'utf8'));
}

for (const [page, html] of htmlByPage) {
  assert(/^<!doctype html>/i.test(html), `${page}: missing doctype`);
  assert(/<html\s+lang="en"/i.test(html), `${page}: document must start in implemented English locale`);
  assert(/<title>[^<]+<\/title>/i.test(html), `${page}: missing title`);
  assert(/<meta\s+name="description"\s+content="[^"]+"/i.test(html), `${page}: missing meta description`);
  assert((html.match(/<main\b/gi) || []).length === 1, `${page}: expected one main landmark`);
  assert((html.match(/<nav\b/gi) || []).length === 1, `${page}: expected one primary navigation landmark in source`);
  assert((html.match(/<footer\b/gi) || []).length === 1, `${page}: expected one footer landmark`);
  assert(html.includes('assets/capital-uiux-v2.css'), `${page}: missing shared UI/UX stylesheet`);
  assert(html.includes('assets/capital-uiux-v2.js'), `${page}: missing shared UI/UX interaction layer`);

  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  const duplicates = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];
  assert(duplicates.length === 0, `${page}: duplicate IDs ${duplicates.join(', ')}`);

  for (const match of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const reference = match[1];
    if (!reference || isRemote(reference)) continue;
    const localPath = stripQuery(reference);
    if (!localPath) continue;
    assert(fs.existsSync(path.resolve(root, localPath)), `${page}: unresolved local dependency ${reference}`);
    const hash = reference.includes('#') ? reference.split('#')[1] : '';
    const targetPage = localPath.endsWith('.html') ? localPath : '';
    if (hash && targetPage && htmlByPage.has(targetPage)) {
      assert(htmlByPage.get(targetPage).includes(`id="${hash}"`), `${page}: missing anchor target ${reference}`);
    }
  }
}

const allHtml = [...htmlByPage.values()].join('\n');
assert(!allHtml.includes('leasing@capitalplace.com.vn'), 'obsolete leasing email remains in HTML');
assert(!allHtml.includes('93,700'), 'obsolete 93,700 area figure remains in HTML');
assert(!/41\s+Storeys/i.test(allHtml), 'obsolete 41-storey figure remains in HTML');
assert(allHtml.includes('93,000'), 'verified 93,000 sqm figure is missing');
assert(allHtml.includes('leasing@capitalplace.vn'), 'verified leasing email is missing');
assert(!allHtml.toLowerCase().includes('unsplash'), 'third-party stock Unsplash asset remains in public HTML');

const leasingHtml = htmlByPage.get('leasing.html') || '';
assert(leasingHtml.includes('data-leasing-form'), 'leasing.html: form contract missing');
assert(leasingHtml.includes('This prototype has not transmitted your information'), 'leasing.html: truthful prepared-not-sent state missing');
assert(leasingHtml.includes('prototype privacy notice'), 'leasing.html: prototype privacy disclosure missing');
assert(leasingHtml.includes('Book Private Viewing') || leasingHtml.includes('Private Viewing'), 'leasing.html: viewing path missing');

const dataJs = read('assets/capital-data.js');
assert(dataJs.includes('leasableAreaSqm: 93000'), 'capital-data.js: verified area missing');
assert(dataJs.includes('storeysPerTower: 37'), 'capital-data.js: verified storeys missing');
assert(dataJs.includes("leasingEmail: 'leasing@capitalplace.vn'"), 'capital-data.js: verified leasing email missing');
assert(dataJs.includes("dataChecked: 'September 2026'"), 'capital-data.js: evidence review date is stale');
assert(dataJs.includes("dataSourceUrl: 'https://capitalplace.com.vn/office/'"), 'capital-data.js: first-party office source URL missing');
assert(dataJs.includes("evidence: 'OFFICIAL_PUBLIC_REFERENCE'"), 'capital-data.js: official floor reference evidence label missing');
assert(dataJs.includes("evidence: 'REPRESENTATIVE_PROTOTYPE'"), 'capital-data.js: representative scenario evidence label missing');
assert(dataJs.includes("availabilityMode: 'leasing-confirmation'"), 'capital-data.js: leasing-confirmation reality mode missing');

const wrapperCss = read('assets/capital-uiux-v2.css');
const v3Css = read('assets/capital-research-v3.css');
const v3Js = read('assets/capital-uiux-v2.js');
assert(wrapperCss.includes('capital-uiux-v2-legacy.css'), 'shared stylesheet must preserve the legacy owner layer');
assert(wrapperCss.includes('capital-research-v3.css'), 'shared stylesheet must load v3 research layer');
assert(v3Css.includes('--ui-accent:var(--cta-orange)'), 'v3 must reuse the existing CTA token rather than duplicate orange');
assert(!v3Css.toLowerCase().includes('#f15f22'), 'v3 duplicates the CTA orange hardcode instead of reusing the token');
assert(v3Css.includes('.cpv3-section-rule'), 'v3 architectural section-rule pattern missing');
assert(!/main#main-content>section\[id\].*::before/.test(v3Css.replace(/\s/g, '')), 'v3 must not overwrite section pseudo-elements used by cinematic overlays');
assert(v3Css.includes('env(safe-area-inset-bottom'), 'mobile fixed actions do not account for safe-area inset');
assert(v3Css.includes('@media(min-width:1760px)'), 'desktop directory lacks wide-screen overlap guard');
assert(v3Js.includes("document.documentElement.lang = 'en'"), 'language semantics are not pinned to implemented English content');
assert(v3Js.includes("setAttribute('aria-disabled', 'true')"), 'unimplemented VI control is not exposed truthfully');
assert(v3Js.includes('syncMenuUi'), 'mobile menu icon/expanded-state synchronization missing');
assert(v3Js.includes("mainNav.classList.add('cu2-nav-solid')"), 'utility-page navigation contrast handling missing');
assert(v3Js.includes("rule.className = 'cpv3-section-rule'"), 'safe DOM section-rule injection missing');
assert(v3Js.includes('Twin-Peaks Personal Data Protection Policy'), 'first-party privacy-policy bridge missing');

const buildGuard = read('scripts/build_pages.py');
assert(buildGuard.includes('LEGACY_GENERATOR_DISABLED'), 'legacy generator is not hard-disabled');
assert(!buildGuard.includes('leasing@capitalplace.com.vn'), 'legacy generator still carries obsolete contact data');

const profile = JSON.parse(read('.uiux-profile.json'));
assert(profile.project?.mode === 'interactive_prototype', '.uiux-profile.json: truthful project mode missing');
assert(profile.source_of_truth?.includes('docs/system-reality.md'), '.uiux-profile.json: system reality not registered as source of truth');

for (const cssFile of [
  'assets/style.css', 'assets/capital-upgrade.css', 'assets/capital-vision.css',
  'assets/capital-white.css', 'assets/capital-visual.css', 'assets/capital-uiux-v2-legacy.css',
  'assets/capital-research-v3.css'
]) {
  const css = read(cssFile);
  assert((css.match(/{/g) || []).length === (css.match(/}/g) || []).length, `${cssFile}: unbalanced braces`);
}

if (failures.length) {
  console.error(`FAIL: ${failures.length} of ${assertions} assertions failed`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log(`PASS: ${assertions} Capital Place structural, evidence, reality and UI/UX assertions`);
  console.log(`Pages: ${pages.length} · Mode: interactive prototype · Availability: leasing confirmation`);
}
