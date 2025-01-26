import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://thanhcaviet.net/login")

    # Example Click and fill textbox
    username_tb = page.get_by_placeholder("email@example.com")
    await username_tb.highlight()
    await username_tb.fill("email@example.com")

    email_login_btn = page.get_by_text("Đăng nhập bằng Email")
    await email_login_btn.click()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())