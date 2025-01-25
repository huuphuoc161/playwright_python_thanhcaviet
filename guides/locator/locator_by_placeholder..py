import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    await page.goto("https://thanhcaviet.net/login")
    # Example get locator of element by placeholder
    username_tb = page.get_by_placeholder("email@example.com")
    await username_tb.highlight()
    await username_tb.fill("username")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())