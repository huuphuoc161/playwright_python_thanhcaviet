import asyncio
import os

from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    user_dir = 'tmp/playwright'
    user_dir = os.path.join(os.getcwd(), user_dir)

    chromium = playwright.chromium
    browser = await chromium.launch_persistent_context(user_dir, headless=False, slow_mo=500, args=['--start-maximized'], no_viewport=True)
    page = await browser.new_page()

    await page.goto("https://thanhcaviet.net/")
    # Click Me button
    logo = page.locator("//a/img[@alt='Logo']")

    await logo.highlight()
    await expect(logo).to_be_visible()

    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())