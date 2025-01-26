from playwright.sync_api import sync_playwright, expect

def handle_accept_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.accept()
    print("Accept successfully")

def handle_cancel_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.dismiss()
    print("Cancel successfully")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.on("dialog", lambda dialog: dialog.accept("AutoTest"))

    page.goto("https://demoqa.com/alerts", wait_until='domcontentloaded')
    page.locator("//button[@id='promtButton']").click()
    expect(page.locator("//span[@id='promptResult']")).to_contain_text("AutoTest")

    page.close()
