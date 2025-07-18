from playwright.sync_api import Page, sync_playwright, Browser, BrowserContext, Playwright

def init_pw() -> Playwright:
    return sync_playwright().start()

def init_bw(playwright: Playwright, browser_name: str = "firefox", headconf: bool = False) -> Browser:
    return getattr(playwright, browser_name).launch(headless=headconf)

def bw_context(browser: Browser) -> BrowserContext:
    return browser.new_context(viewport={"width": 1280, "height": 720})

def init_page(context: BrowserContext) -> Page:
    return context.new_page()

def test_run(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(2000)
    assert "Swag Labs" in page.title()
    print("OK")

pw = init_pw()
bw = init_bw(pw, "firefox", headconf = False)
ctx = bw_context(bw)
page = init_page(ctx)

test_run(page)

page.close()
ctx.close()
bw.close()
pw.stop()