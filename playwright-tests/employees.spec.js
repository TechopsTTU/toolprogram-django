// playwright-tests/employees.spec.js
const { test, expect } = require('@playwright/test');

test('employees page loads successfully', async ({ page }) => {
  await page.goto('/employees/');
  await expect(page).toHaveTitle(/Tool Management System/);
});

test('employees page shows heading and add employee link', async ({ page }) => {
  await page.goto('/employees/');
  await expect(page.locator('h1:has-text("Employee List")')).toBeVisible();
  await expect(page.getByRole('link', { name: /Add Employee|Create/ })).toBeVisible();
});

test('employee creation page loads', async ({ page }) => {
  await page.goto('/employees/employee/add/');
  await expect(page).toHaveTitle(/Tool Management System/);
  await expect(page.locator('form')).toBeVisible();
});
