import { chromium } from 'playwright';
import fs from 'node:fs/promises';

const base = 'http://127.0.0.1:4173/__beta/FAMILY_TREE/';
await fs.mkdir('family-tree-beta-artifacts', { recursive: true });
const browser = await chromium.launch({
  headless: true,
  ...(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {}),
});

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function assertDesktopTreeFits(page, label) {
  const result = await page.locator('.ft-stage-scroll').evaluate((container) => {
    const box = container.getBoundingClientRect();
    const nodes = [...container.querySelectorAll('.ft-node')];
    const offenders = nodes
      .map((node) => ({ label: node.textContent.trim().replace(/\s+/g, ' '), box: node.getBoundingClientRect() }))
      .filter(({ box: nodeBox }) => nodeBox.left < box.left - 1 || nodeBox.right > box.right + 1)
      .map(({ label }) => label);
    return {
      horizontalOverflow: container.scrollWidth - container.clientWidth,
      offenders,
    };
  });
  assert(result.horizontalOverflow <= 1, `${label} desktop tree requires horizontal scrolling: ${result.horizontalOverflow}px`);
  assert(result.offenders.length === 0, `${label} has nodes outside the visible tree area: ${result.offenders.join(', ')}`);
}

const desktop = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
await desktop.goto(base, { waitUntil: 'networkidle' });
await desktop.waitForSelector('.ft-node');
assert(await desktop.locator('[data-ft-family] option').count() === 3, 'Expected three representative beta families');
assert(await desktop.locator('.ft-node').count() === 7, 'Lucyd beta should render seven visible nodes');
await assertDesktopTreeFits(desktop, 'Lucyd');
await desktop.screenshot({ path: 'family-tree-beta-artifacts/lucyd-desktop.png', fullPage: true });

await desktop.selectOption('[data-ft-family]', 'memomind');
await desktop.waitForTimeout(100);
assert(await desktop.locator('.ft-node').count() === 4, 'MemoMind beta should render four nodes');
await assertDesktopTreeFits(desktop, 'MemoMind');
await desktop.screenshot({ path: 'family-tree-beta-artifacts/memomind-desktop.png', fullPage: true });

await desktop.selectOption('[data-ft-family]', 'hecyan');
await desktop.waitForTimeout(100);
assert(await desktop.locator('.ft-node').count() === 12, 'HeyCyan beta should render twelve nodes with aliases');
await assertDesktopTreeFits(desktop, 'HeyCyan');
await desktop.uncheck('[data-ft-aliases]');
await desktop.waitForTimeout(100);
assert(await desktop.locator('.ft-node').count() === 5, 'HeyCyan alias toggle should collapse to five structural nodes');
await assertDesktopTreeFits(desktop, 'HeyCyan without aliases');
await desktop.check('[data-ft-aliases]');
await desktop.uncheck('[data-ft-inferred]');
await desktop.waitForTimeout(100);
assert(await desktop.locator('.ft-node').count() === 11, 'Inferred toggle should remove only the inferred STARK Horizon identity');
await assertDesktopTreeFits(desktop, 'HeyCyan without inferred relationships');
await desktop.screenshot({ path: 'family-tree-beta-artifacts/hecyan-desktop.png', fullPage: true });

await desktop.selectOption('[data-ft-family]', 'lucyd');
await desktop.check('[data-ft-inferred]');
await desktop.locator('.ft-node', { hasText: 'Lucyd Armor' }).click();
assert((await desktop.locator('[data-ft-detail]').innerText()).includes('No evidence inheritance'), 'Detail panel must state the inheritance boundary');
assert((await desktop.locator('[data-ft-detail]').innerText()).includes('GLS-0159'), 'Detail panel must retain canonical GLS identity');

const mobile = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
await mobile.goto(base, { waitUntil: 'networkidle' });
await mobile.waitForSelector('.ft-node');
const overflow = await mobile.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
assert(overflow <= 1, `Mobile preview has horizontal page overflow: ${overflow}px`);
await mobile.selectOption('[data-ft-family]', 'hecyan');
await mobile.waitForTimeout(100);
await mobile.screenshot({ path: 'family-tree-beta-artifacts/hecyan-mobile.png', fullPage: true });

await browser.close();
console.log('Family-tree beta browser tests passed: branching, aliases, inferred filtering, detail provenance, desktop fit, and mobile layout.');
