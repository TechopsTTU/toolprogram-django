// playwright-tests/workcenters.spec.js
const { test, expect } = require('@playwright/test');

test('workcenters page loads successfully', async ({ page }) => {
  await page.goto('/workcenters/');
  await expect(page).toHaveTitle(/Tool Management System/);
});

test('workcenters page shows heading and add workcenter link', async ({ page }) => {
  await page.goto('/workcenters/');
  await expect(page.locator('h1:has-text("WorkCenter List")')).toBeVisible();
  await expect(page.getByRole('link', { name: 'Add WorkCenter' })).toBeVisible();
});

test('workcenter creation page loads', async ({ page }) => {
  await page.goto('/workcenters/workcenter/add/');
  await expect(page).toHaveTitle(/Tool Management System/);
  await expect(page.locator('form')).toBeVisible();
});
