import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const pages = [
  'index.html', 'location.html', 'office.html', 'sustainability.html', 'amenities.html',
  'availability.html', 'space.html', 'leasing.html', 'visit.html', 'resources.html',
  'retail.html', 'occupiers.html', 'faq.html', 'privacy.html', '404.html'
];
const runtimeAliases = Object.freeze({
  'office.html': new Set(['floor-explorer', 'office-specifications']),
  'resources.html': new Set(['specifications']),
  'location.html': new Set(['transport'])
});
const failures = [];
let assertions = 0;

function assert(condition, message) {
  assertions += 1;
  if (!condition) failures.push(message);
}
function stripQuery(value) { return value.split('?')[0].split('#')[0]; }
function isRemote(value) { return /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(value); }
function read(file) { return fs.readFileSync(path.join(root, file), 'utf8'); }

const dataJs = read('assets/capital-data.js');
const htmlByPage = new Map();
for (const page of pages) {
  const file = path.join(root, page);
  assert(fs.existsSync(file), `${page}: file is missing`);
  if (fs.existsSync(file)) htmlByPage.set(page, fs.readFileSync(file, 'utf8'));
}

for (const [page, html] of htmlByPage) {
  assert(/^<!doctype html>/i.test(html), `${page}: missing doctype`);
  assert(/<html\s+lang="en"/i.test(html), `${page}: document must start in implemented English locale`);
  assert(/<meta\s+name="viewport"/i.test(html), `${page}: missing viewport metadata`);
  assert(/<title>[^<]+<\/title>/i.test(html), `${page}: missing title`);
  const hasStaticDescription = /<meta\s+name="description"\s+content="[^"]+"/i.test(html);
  const hasCentralDescription = page === 'faq.html' && dataJs.includes("'faq.html': Object.freeze") && dataJs.includes('Frequently asked questions about Capital Place Hanoi');
  assert(hasStaticDescription || hasCentralDescription, `${page}: missing meta description contract`);
  assert((html.match(/<main\b/gi) || []).length === 1, `${page}: expected one main landmark`);
  assert((html.match(/<nav\b/gi) || []).length === 1, `${page}: expected one primary navigation landmark in source`);
  assert((html.match(/<footer\b/gi) || []).length === 1, `${page}: expected one footer landmark`);
  assert((html.match(/<h1\b/gi) || []).length === 1, `${page}: expected one H1 in source`);
  assert(html.includes('assets/capital-uiux-v2.css'), `${page}: missing shared UI/UX stylesheet`);
  assert(html.includes('assets/capital-uiux-v2.js'), `${page}: missing shared UI/UX interaction layer`);
  assert(html.includes('assets/capital-data.js'), `${page}: missing shared evidence/content-integrity layer`);

  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  const duplicates = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];
  assert(duplicates.length === 0, `${page}: duplicate IDs ${duplicates.join(', ')}`);

  for (const image of html.matchAll(/<img\b[^>]*>/gi)) {
    assert(/\salt="[^"]*"/i.test(image[0]), `${page}: image without alt attribute`);
  }

  for (const blankLink of html.matchAll(/<a\b[^>]*target="_blank"[^>]*>/gi)) {
    assert(/\srel="[^"]*noopener[^"]*"/i.test(blankLink[0]), `${page}: target=_blank link missing noopener`);
  }

  for (const match of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const reference = match[1];
    if (!reference || isRemote(reference)) continue;
    const localPath = stripQuery(reference);
    if (!localPath) continue;
    assert(fs.existsSync(path.resolve(root, localPath)), `${page}: unresolved local dependency ${reference}`);
    const hash = reference.includes('#') ? reference.split('#')[1] : '';
    const targetPage = localPath.endsWith('.html') ? localPath : '';
    if (hash && targetPage && htmlByPage.has(targetPage)) {
      const staticTarget = htmlByPage.get(targetPage).includes(`id="${hash}"`);
      const runtimeTarget = runtimeAliases[targetPage]?.has(hash) === true;
      assert(staticTarget || runtimeTarget, `${page}: missing anchor target ${reference}`);
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
assert(!/\bClick here\b/i.test(allHtml), 'generic CTA copy "Click here" remains in public HTML');
assert(!/\bLearn more\b/i.test(allHtml), 'generic CTA copy "Learn more" remains in public HTML');

const leasingHtml = htmlByPage.get('leasing.html') || '';
assert(leasingHtml.includes('data-leasing-form'), 'leasing.html: form contract missing');
assert(leasingHtml.includes('This prototype has not transmitted your information'), 'leasing.html: truthful prepared-not-sent state missing');
assert(leasingHtml.includes('prototype privacy notice'), 'leasing.html: prototype privacy disclosure missing');
assert(leasingHtml.includes('Private Viewing'), 'leasing.html: viewing path missing');

assert(dataJs.includes('leasableAreaSqm: 93000'), 'capital-data.js: verified area missing');
assert(dataJs.includes('storeysPerTower: 37'), 'capital-data.js: verified storeys missing');
assert(dataJs.includes("leasingEmail: 'leasing@capitalplace.vn'"), 'capital-data.js: verified leasing email missing');
assert(dataJs.includes("dataChecked: 'September 2026'"), 'capital-data.js: evidence review date is stale');
assert(dataJs.includes("dataSourceUrl: 'https://capitalplace.com.vn/office/'"), 'capital-data.js: first-party office source URL missing');
assert(dataJs.includes("evidence: 'OFFICIAL_PUBLIC_REFERENCE'"), 'capital-data.js: official floor reference evidence label missing');
assert(dataJs.includes("evidence: 'REPRESENTATIVE_PROTOTYPE'"), 'capital-data.js: representative scenario evidence label missing');
assert(dataJs.includes("floor: 'Representative Planning Scenario B'"), 'capital-data.js: 1,240 sqm prototype is still presented as an official reference floor plate');
assert(!dataJs.includes("floor: 'Reference Floor Plate B'"), 'capital-data.js: misleading Reference Floor Plate B label remains');
assert(dataJs.includes("availabilityMode: 'leasing-confirmation'"), 'capital-data.js: leasing-confirmation reality mode missing');
assert(dataJs.includes("href: 'availability.html#building-availability'"), 'capital-data.js: availability resource points to a dead anchor');
assert(dataJs.includes('truthfulActionCopy'), 'capital-data.js: truthful CTA compatibility guard missing');
assert(dataJs.includes("'Check live status': 'Confirm with Leasing'"), 'capital-data.js: misleading live-status CTA remediation missing');
assert(dataJs.includes("'Book this floor': 'Request a viewing'"), 'capital-data.js: booking/request truth remediation missing');
assert(dataJs.includes('legacyAnchorAliases'), 'capital-data.js: URL/deep-link compatibility contract missing');
for (const alias of ['floor-explorer', 'office-specifications', 'specifications', 'transport']) {
  assert(dataJs.includes(`'${alias}'`), `capital-data.js: compatibility alias ${alias} missing`);
}
assert(dataJs.includes("href: 'office.html#floor-planning'"), 'capital-data.js: floor-plan resource still uses obsolete anchor');
assert(dataJs.includes("href: 'office.html#technical-specifications'"), 'capital-data.js: specification resource still uses obsolete anchor');

const availabilityJs = read('assets/availability-cinematic.js');
assert(availabilityJs.includes('global.CapitalData'), 'availability experience duplicates planning facts instead of consuming CapitalData');
assert(!availabilityJs.includes("label: 'Reference Floor Plate B'"), 'availability experience still labels the representative scenario as an official reference');
assert(availabilityJs.includes('REPRESENTATIVE_PROTOTYPE'), 'availability experience does not distinguish representative prototype evidence');
assert(availabilityJs.includes('Request a viewing →'), 'availability viewing CTA still implies an automatic booking');
assert(availabilityJs.includes('Request a tour of both →'), 'availability compare CTA still implies an automatic booking');
assert(!availabilityJs.includes('♡ Save Space'), 'availability UI still mixes a text glyph icon into the action system');
assert(availabilityJs.includes('hideUnsupportedFilters'), 'availability UI still exposes unsupported timing/fit-out filters as functional controls');
assert(availabilityJs.includes("prefers-reduced-motion: reduce"), 'availability scroll behavior ignores reduced-motion preference');
assert(!availabilityJs.includes("$$('#av-headcount,#av-headcount"), 'availability field listener contains a duplicate selector');

const wrapperCss = read('assets/capital-uiux-v2.css');
const v3Css = read('assets/capital-research-v3.css');
const qaCss = read('assets/capital-qa-v4.css');
const v3Js = read('assets/capital-uiux-v2.js');
assert(wrapperCss.includes('capital-uiux-v2-legacy.css'), 'shared stylesheet must preserve the legacy owner layer');
assert(wrapperCss.includes('capital-research-v3.css'), 'shared stylesheet must load v3 research layer');
assert(wrapperCss.includes('capital-qa-v4.css'), 'shared stylesheet must load final QA remediation layer');
assert(v3Css.includes('--ui-accent:var(--cta-orange)'), 'v3 must reuse the existing CTA token rather than duplicate orange');
assert(!v3Css.toLowerCase().includes('#f15f22'), 'v3 duplicates the CTA orange hardcode instead of reusing the token');
assert(v3Css.includes('.cpv3-section-rule'), 'v3 architectural section-rule pattern missing');
const compactV3Css = v3Css.replace(/\s/g, '');
assert(!compactV3Css.includes('main#main-content>section[id]:not(:first-child)::before'), 'v3 must not overwrite top-level section pseudo-elements used by cinematic overlays');
assert(v3Css.includes('env(safe-area-inset-bottom'), 'mobile fixed actions do not account for safe-area inset');
assert(v3Css.includes('@media(min-width:1760px)'), 'desktop directory lacks wide-screen overlap guard');
assert(qaCss.includes('--qa-font-action:.75rem'), 'QA typography token must keep actions at 12px or above');
assert(qaCss.includes('--qa-font-nav:.78125rem'), 'QA typography token must keep desktop navigation readable');
assert(qaCss.includes('.ft-col a{font-size:var(--qa-font-footer)!important;color:rgba(35,31,32,.72)!important'), 'footer normal-text contrast/readability remediation missing');
assert(qaCss.includes('.cu2-mobile-actions a{'), 'mobile conversion-dock remediation missing');
assert(qaCss.includes('font-size:var(--qa-font-action)!important'), 'mobile/action microtype remediation missing');
assert(qaCss.includes('outline:2px solid var(--ui-focus)!important'), 'focus indicator normalization missing');
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
assert(fs.existsSync(path.join(root, 'docs/visual-regression-plan.md')), 'visual-regression plan is missing');

for (const cssFile of [
  'assets/style.css', 'assets/capital-upgrade.css', 'assets/capital-vision.css',
  'assets/capital-white.css', 'assets/capital-visual.css', 'assets/capital-uiux-v2-legacy.css',
  'assets/capital-research-v3.css', 'assets/capital-qa-v4.css'
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
  console.log('Final QA: typography/contrast/action truth/representative-data contracts enabled');
}
