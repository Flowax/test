from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False)
page = browser.new_page()

try:
    page.goto("https://duckduckgo.com/",timeout=10000)
    page.fill("#searchbox_input", "Playwright")
    page.wait_for_timeout(1000)
    page.press("#searchbox_input", "Enter")
    page.wait_for_timeout(10000)
    if "Playwright at DuckDuckGo" in page.title():
        print("ok")
    else:
        print("ne ok")

except Exception as e:
    print("Ошибка")
finally:
    browser.close()
    playwright.stop()