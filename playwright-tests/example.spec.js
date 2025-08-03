// playwright-tests/tools.spec.js
const { test, expect } = require('@playwright/test');

test('tools page loads successfully', async ({ page }) => {
  await page.goto('/tools/');
  await expect(page).toHaveTitle(/Tool Management System/);
});

test('tools page shows heading and add tool link', async ({ page }) => {
  await page.goto('/tools/');
  await expect(page.locator('h1:has-text("Tool List")')).toBeVisible();
  await expect(page.getByRole('link', { name: 'Add Tool' })).toBeVisible();
});

test('tool creation page loads', async ({ page }) => {
  await page.goto('/tools/tool/add/');
  await expect(page).toHaveTitle(/Tool Management System/);
  // Check for form elements that should be present on a tool creation page
  await expect(page.locator('form')).toBeVisible();
});
