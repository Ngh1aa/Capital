import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const pages = [
  'index.html', 'location.html', 'office.html', 'sustainability.html', 'amenities.html',
  'availability.html', 'space.html', 'leasing.html', 'visit.html', 'resources.html',
  'retail.html', 'occupiers.html', 'privacy.html', '404.html'
];
const failures = [];
let assertions = 0;

function assert(condition, message) {
  assertions += 1;
  if (!condition) failures.push(message);
}

function stripQuery(value) {
  return value.split('?')[0].split('#')[0];
}

function isRemote(value) {
  return /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(value);
}

const htmlByPage = new Map();
for (const page of pages) {
  const file = path.join(root, page);
  assert(fs.existsSync(file), `${page}: file is missing`);
  if (!fs.existsSync(file)) continue;
  const html = fs.readFileSync(file, 'utf8');
  htmlByPage.set(page, html);
  assert(html.startsWith('<!DOCTYPE html>'), `${page}: missing doctype`);
  assert(/<html\s+lang="en">/.test(html), `${page}: missing document language`);
  assert(/<title>[^<]+<\/title>/.test(html), `${page}: missing title`);
  assert(/<meta\s+name="description"\s+content="[^"]+"/.test(html), `${page}: missing meta description`);
  assert((html.match(/<main\b/g) || []).length === 1, `${page}: expected one main landmark`);
  assert((html.match(/<nav\b/g) || []).length === 1, `${page}: expected one navigation landmark`);
  assert((html.match(/<footer\b/g) || []).length === 1, `${page}: expected one footer landmark`);
  assert(html.includes('assets/capital-upgrade.css?v=ux-20260824-1'), `${page}: missing upgrade stylesheet`);
  assert(html.includes('assets/capital-data.js?v=ux-20260824-1'), `${page}: missing central data module`);
  assert(html.includes('assets/capital-upgrade.js?v=ux-20260824-1'), `${page}: missing interaction module`);

  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]);
  const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
  assert(duplicates.length === 0, `${page}: duplicate IDs ${[...new Set(duplicates)].join(', ')}`);

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
assert(!allHtml.includes('leasing@capitalplace.com.vn'), 'obsolete leasing email remains in generated HTML');
assert(!allHtml.includes('93,700'), 'obsolete 93,700 area figure remains in generated HTML');
assert(!allHtml.includes('41 Storeys'), 'obsolete 41-storey figure remains in generated HTML');
assert(allHtml.includes('93,000'), 'verified 93,000 sqm figure is missing');
assert(allHtml.includes('37 Storeys Per Tower'), 'verified 37-storey label is missing');

const requiredHooks = {
  'index.html': ['data-home-availability', 'availability.html#space-finder'],
  'office.html': ['data-space-finder', 'office-specifications', 'stack-shell'],
  'availability.html': ['data-space-finder', 'data-availability-list', 'data-filter-status'],
  'space.html': ['data-space-page', 'data-space-plan', 'data-space-action="viewing"'],
  'leasing.html': ['data-leasing-form', 'name="requiredArea"', 'name="targetMoveIn"', 'name="preferredDate"', 'name="brand"', 'privacy.html'],
  'visit.html': ['visitor-guide', 'visit-map', 'Reception'],
  'resources.html': ['data-resource-list', 'technical-package'],
  'retail.html': ['leasing.html?intent=retail', 'Available<br><em>on request</em>'],
  'occupiers.html': ['Occupier Gateway', 'Building Support'],
  '404.html': ['View Office', 'Contact Leasing']
};
for (const [page, hooks] of Object.entries(requiredHooks)) {
  const html = htmlByPage.get(page) || '';
  for (const hook of hooks) assert(html.includes(hook), `${page}: required UX hook missing: ${hook}`);
}

const dataJs = fs.readFileSync(path.join(root, 'assets/capital-data.js'), 'utf8');
for (const status of ['available', 'available-soon', 'under-offer', 'leased', 'future-availability', 'on-request']) {
  assert(dataJs.includes(`${status}:`) || dataJs.includes(`'${status}':`), `capital-data.js: missing status ${status}`);
}
assert(dataJs.includes("leasingEmail: 'leasing@capitalplace.vn'"), 'capital-data.js: verified leasing email missing');
assert(dataJs.includes('leasableAreaSqm: 93000'), 'capital-data.js: verified area missing');
assert(dataJs.includes('storeysPerTower: 37'), 'capital-data.js: verified storeys missing');
assert((dataJs.match(/id: 't\d-l\d+'/g) || []).length >= 6, 'capital-data.js: insufficient demonstration availability states');

for (const cssFile of ['assets/style.css', 'assets/capital-upgrade.css']) {
  const css = fs.readFileSync(path.join(root, cssFile), 'utf8');
  assert((css.match(/{/g) || []).length === (css.match(/}/g) || []).length, `${cssFile}: unbalanced braces`);
}

if (failures.length) {
  console.error(`FAIL: ${failures.length} of ${assertions} assertions failed`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log(`PASS: ${assertions} Capital Place structural, data and leasing-flow assertions`);
  console.log(`Pages: ${pages.length} · Availability states: 6 · Central facts: verified`);
}
