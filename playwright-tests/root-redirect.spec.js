const { test, expect } = require('@playwright/test');

test('root URL redirects to tools', async ({ page }) => {
  const response = await page.goto('/');
  // Should redirect to /tools/
  await expect(page).toHaveURL(/\/tools\//);
  await expect(page).toHaveTitle(/Tool Management System/);
  await expect(page.locator('h1:has-text("Tool List")')).toBeVisible();
});
