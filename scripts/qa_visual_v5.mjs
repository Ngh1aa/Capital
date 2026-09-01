import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const read = (file) => fs.readFileSync(path.join(root, file), 'utf8');
const failures = [];
let assertions = 0;
const assert = (condition, message) => { assertions += 1; if (!condition) failures.push(message); };

const wrapper = read('assets/capital-uiux-v2.css');
const css = read('assets/capital-art-direction-v5.css');
const compact = css.replace(/\s/g, '');

assert(wrapper.trim().endsWith('@import url("./capital-art-direction-v5.css?v=art-20260901-5");'), 'v5 art direction must load last');
assert((css.match(/{/g) || []).length === (css.match(/}/g) || []).length, 'v5 CSS braces are unbalanced');
assert(css.includes('--cp5-accent:#f15f22'), 'brand CTA orange token missing');
assert(css.includes('.capital-uiux-v2 #main-nav .nav-logo'), 'new dark podium brand block missing');
assert(css.includes('background:var(--cp5-ink)!important'), 'dark podium/nav owner state missing');
assert(css.includes('border-right:4px solid var(--cp5-accent)!important'), 'architectural datum line missing');
assert(css.includes('filter:none!important'), 'white logo visibility contract missing');
assert(css.includes('.capital-uiux-v2 #main-nav.scrolled'), 'scrolled nav state missing');
assert(compact.includes('background:var(--cp5-accent)!important;border:1pxsolidvar(--cp5-accent)!important;color:var(--cp5-ink)!important') || css.includes('background:var(--cp5-accent)!important;'), 'solid CTA owner state missing');
assert(css.includes('.hc-home .hc-anatomy-grid'), 'home architectural composition missing');
assert(css.includes('.lc-location .lc-context-grid'), 'location map/editorial composition missing');
assert(css.includes('.oc-office .oc-floorplate-grid'), 'office floor-plan composition missing');
assert(css.includes('.ac-amenities .ac-nexus'), 'amenities hospitality composition missing');
assert(css.includes('.ss-page .ss-performance-grid'), 'sustainability evidence composition missing');
assert(css.includes('.av-page .av-explorer-grid'), 'availability decision-tool composition missing');
assert(css.includes('.capital-uiux-v2 footer'), 'dark architectural footer missing');
assert(css.includes('@media(max-width:1150px)'), 'tablet/mobile nav recomposition missing');
assert(css.includes('@media(max-width:900px)'), 'intermediate responsive recomposition missing');
assert(css.includes('@media(max-width:640px)'), 'mobile typography/layout recomposition missing');
assert(css.includes('@media(prefers-reduced-motion:reduce)'), 'reduced-motion contract missing');

if (failures.length) {
  console.error(`FAIL: ${failures.length} of ${assertions} visual v5 assertions failed`);
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log(`PASS: ${assertions} Capital Place visual art-direction v5 assertions`);
  console.log('Coverage: nav/logo/CTA · layout grammar · domain metaphor · responsive · reduced motion');
}
