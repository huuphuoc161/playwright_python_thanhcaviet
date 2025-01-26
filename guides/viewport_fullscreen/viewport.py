import asyncio

from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    #View port:
    await page.set_viewport_size({"width": 393, "height": 852})

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