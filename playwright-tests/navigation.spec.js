// playwright-tests/navigation.spec.js
const { test, expect } = require('@playwright/test');

test('navigation between main sections works', async ({ page }) => {
  // Start at tools page
  await page.goto('/tools/');
  
  // Find and click navigation links
  // Note: This will need adjustment based on your actual navigation structure
  const workcentersLink = page.getByRole('link', { name: /workcenters/i });
  if (await workcentersLink.count() > 0) {
    await workcentersLink.click();
    await expect(page).toHaveURL(/.*workcenters.*/);
  }
  
  const employeesLink = page.getByRole('link', { name: /employees/i });
  if (await employeesLink.count() > 0) {
    await employeesLink.click();
    await expect(page).toHaveURL(/.*employees.*/);
  }
  
  // Navigate back to tools
  const toolsLink = page.getByRole('link', { name: /tools/i });
  if (await toolsLink.count() > 0) {
    await toolsLink.click();
    await expect(page).toHaveURL(/.*tools.*/);
  }
});

test('admin page is accessible', async ({ page }) => {
  await page.goto('/admin/');
  await expect(page).toHaveTitle(/Log in | Django/);
  await expect(page.locator('form#login-form')).toBeVisible();
});
