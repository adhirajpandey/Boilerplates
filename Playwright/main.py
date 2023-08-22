from playwright.sync_api import Playwright, sync_playwright
from undetected_playwright import stealth_sync
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    stealth_sync(context)
    page = context.new_page()

    #goto bot detection page
    page.goto("https://bot.sannysoft.com/")
    
    # cookie_file = open('./cookies.json')
    # cookies = json.load(cookie_file)
    # context.add_cookies(cookies)
    
    time.sleep(2)

    #capture screenshot
    page.screenshot(path='./screenshots/bot_test.png')

    #to capture test/codegen using custom setup 
    #page.pause()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
