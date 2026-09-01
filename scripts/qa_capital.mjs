import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const pages = [
  'index.html', 'location.html', 'office.html', 'sustainability.html', 'amenities.html',
  'availability.html', 'space.html', 'leasing.html', 'visit.html', 'resources.html',
  'retail.html', 'occupiers.html', 'faq.html', 'privacy.html', '404.html'
];
const highTrustDataPages = new Set(['availability.html', 'space.html', 'leasing.html', 'resources.html', 'faq.html']);
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
function read(file) { return fs.readFileSync(path.join(root, file), 'utf8'); }
function stripQuery(value) { return value.split('?')[0].split('#')[0]; }
function isRemote(value) { return /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(value); }
function hasMeta(html, name) {
  const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return new RegExp(`<meta\\b(?=[^>]*\\bname=["']${escaped}["'])[^>]*>`, 'i').test(html);
}
function attr(tag, name) {
  return tag.match(new RegExp(`\\b${name}=["']([^"']*)["']`, 'i'))?.[1] || '';
}

const dataJs = read('assets/capital-data.js');
const htmlByPage = new Map();
for (const page of pages) {
  const file = path.join(root, page);
  assert(fs.existsSync(file), `${page}: file is missing`);
  if (fs.existsSync(file)) htmlByPage.set(page, fs.readFileSync(file, 'utf8'));
}

for (const [page, html] of htmlByPage) {
  assert(/^<!doctype html>/i.test(html), `${page}: missing doctype`);
  assert(/<html\b[^>]*\blang=["']en["']/i.test(html), `${page}: implemented locale must be English`);
  assert(hasMeta(html, 'viewport'), `${page}: missing viewport metadata`);
  assert(/<title>[^<]+<\/title>/i.test(html), `${page}: missing title`);
  const staticDescription = hasMeta(html, 'description');
  const centralDescription = page === 'faq.html' && dataJs.includes('Frequently asked questions about Capital Place Hanoi');
  assert(staticDescription || centralDescription, `${page}: missing description contract`);
  assert((html.match(/<main\b/gi) || []).length === 1, `${page}: expected one main landmark`);
  assert((html.match(/<nav\b/gi) || []).length === 1, `${page}: expected one primary nav landmark`);
  assert((html.match(/<footer\b/gi) || []).length === 1, `${page}: expected one footer landmark`);
  assert((html.match(/<h1\b/gi) || []).length === 1, `${page}: expected exactly one H1`);
  assert(html.includes('assets/capital-uiux-v2.css'), `${page}: shared UI/UX stylesheet missing`);
  assert(html.includes('assets/capital-uiux-v2.js'), `${page}: shared interaction layer missing`);
  if (highTrustDataPages.has(page)) assert(html.includes('assets/capital-data.js'), `${page}: evidence/content-integrity layer missing`);

  const ids = [...html.matchAll(/\sid=["']([^"']+)["']/g)].map((match) => match[1]);
  const duplicates = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];
  assert(duplicates.length === 0, `${page}: duplicate IDs ${duplicates.join(', ')}`);

  for (const image of html.matchAll(/<img\b[^>]*>/gi)) {
    assert(/\salt=["'][^"']*["']/i.test(image[0]), `${page}: image missing alt attribute`);
  }

  for (const link of html.matchAll(/<a\b[^>]*>/gi)) {
    const tag = link[0];
    const href = attr(tag, 'href');
    const target = attr(tag, 'target');
    if (target === '_blank' && /^https?:/i.test(href)) {
      assert(/\brel=["'][^"']*noopener[^"']*["']/i.test(tag), `${page}: external target=_blank link missing noopener`);
    }
  }

  for (const match of html.matchAll(/\s(?:href|src)=["']([^"']+)["']/g)) {
    const reference = match[1];
    if (!reference || isRemote(reference)) continue;
    const localPath = stripQuery(reference);
    if (!localPath) continue;
    assert(fs.existsSync(path.resolve(root, localPath)), `${page}: unresolved local dependency ${reference}`);
    const hash = reference.includes('#') ? reference.split('#')[1] : '';
    const targetPage = localPath.endsWith('.html') ? localPath : '';
    if (hash && targetPage && htmlByPage.has(targetPage)) {
      const staticTarget = htmlByPage.get(targetPage).includes(`id="${hash}"`) || htmlByPage.get(targetPage).includes(`id='${hash}'`);
      const runtimeTarget = runtimeAliases[targetPage]?.has(hash) === true;
      assert(staticTarget || runtimeTarget, `${page}: missing anchor target ${reference}`);
    }
  }
}

const allHtml = [...htmlByPage.values()].join('\n');
assert(!allHtml.includes('leasing@capitalplace.com.vn'), 'obsolete leasing email remains in HTML');
assert(!allHtml.includes('93,700'), 'obsolete 93,700 area figure remains in HTML');
assert(!/41\s+Storeys/i.test(allHtml), 'obsolete 41-storey figure remains in HTML');
assert(allHtml.includes('93,000'), 'verified 93,000 sqm figure missing');
assert(allHtml.includes('leasing@capitalplace.vn'), 'verified leasing email missing');
assert(!allHtml.toLowerCase().includes('unsplash'), 'third-party Unsplash asset remains in public HTML');
assert(!/\bClick here\b/i.test(allHtml), 'generic CTA "Click here" remains');
assert(!/\bLearn more\b/i.test(allHtml), 'generic CTA "Learn more" remains');

const leasingHtml = htmlByPage.get('leasing.html') || '';
assert(leasingHtml.includes('data-leasing-form'), 'leasing.html: form contract missing');
assert(leasingHtml.includes('This prototype has not transmitted your information'), 'leasing.html: prepared-not-sent truth missing');
assert(leasingHtml.includes('prototype privacy notice'), 'leasing.html: prototype privacy disclosure missing');
assert(leasingHtml.includes('Private Viewing'), 'leasing.html: viewing route missing');

assert(dataJs.includes('leasableAreaSqm: 93000'), 'capital-data.js: verified area missing');
assert(dataJs.includes('storeysPerTower: 37'), 'capital-data.js: verified storeys missing');
assert(dataJs.includes("leasingEmail: 'leasing@capitalplace.vn'"), 'capital-data.js: verified leasing email missing');
assert(dataJs.includes("dataChecked: 'September 2026'"), 'capital-data.js: evidence date stale');
assert(dataJs.includes("dataSourceUrl: 'https://capitalplace.com.vn/office/'"), 'capital-data.js: first-party source URL missing');
assert(dataJs.includes("evidence: 'OFFICIAL_PUBLIC_REFERENCE'"), 'capital-data.js: official evidence label missing');
assert(dataJs.includes("evidence: 'REPRESENTATIVE_PROTOTYPE'"), 'capital-data.js: representative evidence label missing');
assert(dataJs.includes("floor: 'Representative Planning Scenario B'"), 'capital-data.js: 1,240 sqm scenario is mislabeled');
assert(!dataJs.includes("floor: 'Reference Floor Plate B'"), 'capital-data.js: misleading Reference Floor Plate B remains');
assert(dataJs.includes("availabilityMode: 'leasing-confirmation'"), 'capital-data.js: availability reality mode missing');
assert(dataJs.includes("href: 'availability.html#building-availability'"), 'capital-data.js: availability resource anchor invalid');
assert(dataJs.includes('truthfulActionCopy'), 'capital-data.js: truthful CTA guard missing');
assert(dataJs.includes("'Check live status': 'Confirm with Leasing'"), 'capital-data.js: live-status copy guard missing');
assert(dataJs.includes("'Book this floor': 'Request a viewing'"), 'capital-data.js: booking/request copy guard missing');
assert(dataJs.includes('legacyAnchorAliases'), 'capital-data.js: legacy anchor compatibility missing');
for (const alias of ['floor-explorer', 'office-specifications', 'specifications', 'transport']) {
  assert(dataJs.includes(`'${alias}'`), `capital-data.js: compatibility alias ${alias} missing`);
}

const availabilityJs = read('assets/availability-cinematic.js');
assert(availabilityJs.includes('global.CapitalData'), 'availability: duplicates planning data instead of consuming CapitalData');
assert(availabilityJs.includes('isOfficialReference'), 'availability: evidence-aware reference predicate missing');
assert(availabilityJs.includes('Representative prototype scenario'), 'availability: representative scenario disclosure missing');
assert(!availabilityJs.includes("label: 'Reference Floor Plate B'"), 'availability: stale Reference Floor Plate B hardcode remains');
assert(availabilityJs.includes('Request a viewing →'), 'availability: viewing action still implies automatic booking');
assert(availabilityJs.includes('Request a tour of both →'), 'availability: compare action still implies automatic booking');
assert(!availabilityJs.includes('♡ Save Space'), 'availability: text-glyph heart icon remains in dynamic UI');
assert(availabilityJs.includes('hideUnsupportedFilters'), 'availability: unsupported filters are still exposed');
assert(availabilityJs.includes("prefers-reduced-motion: reduce"), 'availability: smooth scroll ignores reduced motion');
assert(!availabilityJs.includes("$$('#av-headcount,#av-headcount"), 'availability: duplicate field selector remains');

const wrapperCss = read('assets/capital-uiux-v2.css');
const v3Css = read('assets/capital-research-v3.css');
const qaCss = read('assets/capital-qa-v4.css');
const v3Js = read('assets/capital-uiux-v2.js');
assert(wrapperCss.includes('capital-uiux-v2-legacy.css'), 'shared stylesheet: legacy owner layer missing');
assert(wrapperCss.includes('capital-research-v3.css'), 'shared stylesheet: research v3 layer missing');
assert(wrapperCss.includes('capital-qa-v4.css'), 'shared stylesheet: final QA layer missing');
assert(v3Css.includes('--ui-accent:var(--cta-orange)'), 'v3: CTA token not reused');
assert(!v3Css.toLowerCase().includes('#f15f22'), 'v3: duplicate CTA orange hardcode remains');
assert(v3Css.includes('.cpv3-section-rule'), 'v3: architectural section rule missing');
assert(!v3Css.replace(/\s/g, '').includes('main#main-content>section[id]:not(:first-child)::before'), 'v3: top-level cinematic pseudo-element collision risk remains');
assert(v3Css.includes('env(safe-area-inset-bottom'), 'v3: mobile fixed actions ignore safe area');
assert(v3Css.includes('@media(min-width:1760px)'), 'v3: building directory overlap guard missing');
assert(qaCss.includes('--qa-font-action:.75rem'), 'QA typography: action minimum 12px token missing');
assert(qaCss.includes('--qa-font-nav:.78125rem'), 'QA typography: readable nav token missing');
assert(qaCss.includes('color:rgba(35,31,32,.72)!important'), 'QA contrast: readable footer text treatment missing');
assert(qaCss.includes('font-size:var(--qa-font-action)!important'), 'QA typography: action microtype remediation missing');
assert(qaCss.includes('outline:2px solid var(--ui-focus)!important'), 'QA accessibility: focus normalization missing');
assert(v3Js.includes("document.documentElement.lang = 'en'"), 'language integrity: English semantics not pinned');
assert(v3Js.includes("setAttribute('aria-disabled', 'true')"), 'language integrity: unavailable VI control not exposed');
assert(v3Js.includes('syncMenuUi'), 'mobile menu: state synchronization missing');
assert(v3Js.includes("mainNav.classList.add('cu2-nav-solid')"), 'utility navigation: contrast mode missing');
assert(v3Js.includes("rule.className = 'cpv3-section-rule'"), 'architectural rule: DOM injection missing');
assert(v3Js.includes('Twin-Peaks Personal Data Protection Policy'), 'privacy: first-party policy bridge missing');

const buildGuard = read('scripts/build_pages.py');
assert(buildGuard.includes('LEGACY_GENERATOR_DISABLED'), 'legacy generator is not hard-disabled');
assert(!buildGuard.includes('leasing@capitalplace.com.vn'), 'legacy generator contains obsolete contact data');

const profile = JSON.parse(read('.uiux-profile.json'));
assert(profile.project?.mode === 'interactive_prototype', '.uiux-profile.json: truthful project mode missing');
assert(profile.source_of_truth?.includes('docs/system-reality.md'), '.uiux-profile.json: system reality not registered');
assert(fs.existsSync(path.join(root, 'docs/visual-regression-plan.md')), 'visual-regression plan missing');

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
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log(`PASS: ${assertions} Capital Place structural, evidence, reality and final UI/UX assertions`);
  console.log(`Pages: ${pages.length} · Mode: interactive prototype · Availability: leasing confirmation`);
  console.log('Final QA contracts: typography · contrast · CTA truth · evidence integrity · responsive/a11y source guards');
}
