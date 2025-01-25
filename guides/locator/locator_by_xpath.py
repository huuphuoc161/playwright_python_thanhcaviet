import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://thanhcaviet.net/")

    ## Example get locator of element by Xpath
    search_textbox_example_1 = page.locator("xpath=//a/img[@alt='Logo']")
    await search_textbox_example_1.highlight()
    await page.close()



async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())