import asyncio
from playwright.async_api import async_playwright, Playwright, expect
from utils.read_data import read_json_by_key
import os

# def on_route_modify_return_json(route: Route):
#     route.fulfill(
#         status=200,
#         json={
#             "username": "username",
#             "password": "password",
#             "Environment": os.environ['Environment']
#         }
#     )

# def test_example_read_json(page: Page):
#     page.route("**", on_route_modify_return_json)
#     environment = os.environ['Environment']
#     response = page.goto(read_json_by_key(f"../data/json/{environment}.json", "url"))
#     print(response.json())
#     assert response.json()['Environment'] == os.environ['Environment']

async def run(playwright: Playwright):
    environment = os.environ['Environment']
    url = read_json_by_key(f"../data/json/{environment}.json", "url")
    username = read_json_by_key(f"../data/json/{environment}.json", "username")
    password = read_json_by_key(f"../data/json/{environment}.json", "password")

    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto(url + "/login")

    username_tb = page.get_by_placeholder("email@example.com")
    await username_tb.highlight()
    await username_tb.fill(username)

    email_login_btn = page.get_by_text("Đăng nhập bằng Email")
    await email_login_btn.click()

    password_tb = page.get_by_label("Mật khẩu")
    await password_tb.highlight()
    await password_tb.fill(password)

    confirm_btn = page.get_by_text("Tiếp tục ")
    await expect(confirm_btn).to_be_visible()
    await confirm_btn.click()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())