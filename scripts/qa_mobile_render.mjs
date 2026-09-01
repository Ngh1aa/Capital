import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

const baseURL = process.env.CAPITAL_QA_URL || 'http://127.0.0.1:4173';
const routes = [
  'index.html','location.html','office.html','sustainability.html','amenities.html',
  'availability.html','leasing.html','visit.html','resources.html','faq.html',
  'occupiers.html','retail.html','space.html','privacy.html','404.html'
];
const coreRoutes = new Set([
  'index.html','location.html','office.html','sustainability.html','amenities.html',
  'availability.html','leasing.html','faq.html','404.html'
]);
const matrices = [
  { name:'320', width:320, height:800, routes },
  { name:'390', width:390, height:844, routes },
  { name:'414', width:414, height:896, routes:[...coreRoutes] },
  { name:'768', width:768, height:1024, routes:[...coreRoutes] },
  { name:'landscape', width:667, height:375, routes:[...coreRoutes].filter(route => route !== '404.html') }
];

const failures = [];
let assertions = 0;
const check = (condition, message) => {
  assertions += 1;
  if (!condition) failures.push(message);
};

const screenshotDir = path.resolve('artifacts/mobile-render');
fs.mkdirSync(screenshotDir, { recursive:true });

const browser = await chromium.launch({ headless:true });

for (const matrix of matrices) {
  const context = await browser.newContext({
    viewport:{ width:matrix.width, height:matrix.height },
    isMobile:matrix.width <= 768,
    hasTouch:matrix.width <= 768,
    reducedMotion:'reduce',
    deviceScaleFactor:1
  });

  for (const route of matrix.routes) {
    const page = await context.newPage();
    const url = `${baseURL}/${route}`;
    try {
      const response = await page.goto(url, { waitUntil:'domcontentloaded', timeout:15000 });
      check(Boolean(response?.ok()), `${route}@${matrix.name}: HTTP response failed`);
      await page.evaluate(async () => {
        if (document.fonts?.ready) {
          await Promise.race([document.fonts.ready, new Promise(resolve => setTimeout(resolve, 1200))]);
        }
      });
      await page.waitForTimeout(80);

      const layout = await page.evaluate(() => {
        const viewport = document.documentElement.clientWidth;
        const visible = el => {
          const style = getComputedStyle(el);
          const rect = el.getBoundingClientRect();
          return style.display !== 'none' && style.visibility !== 'hidden' && Number(style.opacity) !== 0 && rect.width > 0 && rect.height > 0;
        };
        const overflowers = [...document.body.querySelectorAll('*')]
          .filter(visible)
          .map(el => ({ el, rect:el.getBoundingClientRect() }))
          .filter(({ el, rect }) => {
            if (el.closest('.cp6-nav-links') && !el.closest('.cp6-nav-links.is-open')) return false;
            return rect.left < -1 || rect.right > viewport + 1;
          })
          .slice(0,8)
          .map(({ el, rect }) => ({
            tag:el.tagName.toLowerCase(),
            cls:el.className?.toString?.().slice(0,90) || '',
            left:Math.round(rect.left),
            right:Math.round(rect.right),
            viewport
          }));

        const headings = [...document.querySelectorAll('.cp6-display,.cp6-h1,.cp6-h2')]
          .filter(visible)
          .map(el => {
            const style = getComputedStyle(el);
            const rect = el.getBoundingClientRect();
            return {
              text:(el.textContent || '').trim().slice(0,80),
              width:rect.width,
              left:rect.left,
              right:rect.right,
              fontSize:parseFloat(style.fontSize),
              lineHeight:parseFloat(style.lineHeight)
            };
          });

        const targetSelector = '.cp6-primary,.cp6-secondary,.cp6-menu,.cp6-nav-cta,.cp6-footer a,.cp6-contact-meta a,.cp6-faq-list summary';
        const targets = [...document.querySelectorAll(targetSelector)]
          .filter(visible)
          .map(el => {
            const rect = el.getBoundingClientRect();
            return { label:(el.textContent || el.getAttribute('aria-label') || el.tagName).trim().slice(0,50), width:rect.width, height:rect.height };
          });

        const fields = [...document.querySelectorAll('input,select,textarea')]
          .filter(visible)
          .map(el => ({ name:el.name || el.id || el.tagName, fontSize:parseFloat(getComputedStyle(el).fontSize), height:el.getBoundingClientRect().height }));

        const thirdFact = document.querySelector('.cp6-hero-facts span:nth-child(3)');
        const lang = document.querySelector('.cp6-lang');
        return {
          scrollWidth:document.documentElement.scrollWidth,
          clientWidth:viewport,
          overflowers,
          headings,
          targets,
          fields,
          thirdFactVisible:thirdFact ? visible(thirdFact) : null,
          langExists:Boolean(lang)
        };
      });

      check(layout.scrollWidth <= layout.clientWidth + 1, `${route}@${matrix.name}: document horizontal overflow ${layout.scrollWidth}/${layout.clientWidth}`);
      check(layout.overflowers.length === 0, `${route}@${matrix.name}: visible element overflow ${JSON.stringify(layout.overflowers)}`);

      for (const heading of layout.headings) {
        check(heading.left >= -1 && heading.right <= layout.clientWidth + 1, `${route}@${matrix.name}: heading escapes viewport “${heading.text}”`);
        if (matrix.width <= 414 && Number.isFinite(heading.lineHeight) && heading.fontSize >= 30) {
          check(heading.lineHeight >= heading.fontSize * .96, `${route}@${matrix.name}: heading line-height too tight “${heading.text}”`);
        }
      }

      if (matrix.width <= 414) {
        for (const target of layout.targets) {
          check(target.height >= 43.5, `${route}@${matrix.name}: touch target below 44px “${target.label}” = ${target.height.toFixed(1)}px`);
        }
        for (const field of layout.fields) {
          check(field.fontSize >= 16, `${route}@${matrix.name}: form field can trigger iOS zoom “${field.name}” = ${field.fontSize}px`);
          check(field.height >= 44, `${route}@${matrix.name}: form field target below 44px “${field.name}” = ${field.height.toFixed(1)}px`);
        }
      }

      if (route === 'index.html' && matrix.width <= 414) {
        check(layout.thirdFactVisible === true, `${route}@${matrix.name}: 37-storey fact is hidden`);
      }

      if (route !== '404.html' && matrix.width <= 768) {
        const menu = page.locator('.cp6-menu');
        await menu.click();
        await page.waitForTimeout(40);
        check(await menu.getAttribute('aria-expanded') === 'true', `${route}@${matrix.name}: mobile menu did not open semantically`);
        check(await page.locator('.cp6-nav-links').evaluate(el => getComputedStyle(el).display !== 'none'), `${route}@${matrix.name}: mobile menu panel is not visible`);
        check(await page.evaluate(() => getComputedStyle(document.body).position) === 'fixed', `${route}@${matrix.name}: mobile menu does not lock page scroll`);
        const activeTag = await page.evaluate(() => document.activeElement?.tagName?.toLowerCase());
        check(activeTag === 'a', `${route}@${matrix.name}: focus did not enter opened navigation`);

        if (layout.langExists) {
          const langVisible = await page.locator('.cp6-lang').evaluate(el => {
            const r=el.getBoundingClientRect(), s=getComputedStyle(el); return s.display !== 'none' && r.height > 0;
          });
          check(langVisible, `${route}@${matrix.name}: language control disappears in mobile menu`);
        }

        await menu.focus();
        await page.keyboard.press('Shift+Tab');
        const wrappedToNav = await page.evaluate(() => Boolean(document.activeElement?.closest?.('.cp6-nav-links')));
        check(wrappedToNav, `${route}@${matrix.name}: Shift+Tab does not wrap focus to end of menu`);
        await page.keyboard.press('Tab');
        check(await page.evaluate(() => document.activeElement?.classList?.contains('cp6-menu')) === true, `${route}@${matrix.name}: Tab does not wrap focus back to menu button`);

        await page.keyboard.press('Escape');
        check(await menu.getAttribute('aria-expanded') === 'false', `${route}@${matrix.name}: Escape did not close mobile menu`);
        check(await page.evaluate(() => document.activeElement?.classList?.contains('cp6-menu')) === true, `${route}@${matrix.name}: Escape did not restore focus to menu button`);
        check(await page.evaluate(() => getComputedStyle(document.body).position) !== 'fixed', `${route}@${matrix.name}: body remains scroll-locked after menu close`);
      }

      const shouldCapture = coreRoutes.has(route) && (matrix.name === '390' || matrix.name === '768')
        || ['index.html','availability.html','leasing.html'].includes(route) && matrix.name === '320';
      if (shouldCapture) {
        await page.screenshot({
          path:path.join(screenshotDir, `${route.replace('.html','')}-${matrix.name}.png`),
          fullPage:false
        });
      }
    } catch (error) {
      failures.push(`${route}@${matrix.name}: ${error.message}`);
    } finally {
      await page.close();
    }
  }

  await context.close();
}

await browser.close();

if (failures.length) {
  console.error(`FAIL: ${failures.length} rendered-mobile issues across ${assertions} assertions`);
  failures.forEach(failure => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(`PASS: ${assertions} Chromium rendered-mobile assertions`);
console.log('Rendered matrix: all routes @320/@390 · core @414/@768 · core landscape 667×375');
console.log(`Screenshots: ${screenshotDir}`);
