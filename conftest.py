import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        choices=["chromium", "firefox", "webkit"],
        help="Выбор браузера"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Запуск браузера в скрытом режиме"
    )

@pytest.fixture(scope="session")
def playwright():
    pw = sync_playwright().start()  # Запускаем Playwright
    yield pw
    pw.stop()  # Останавливаем в конце

@pytest.fixture(scope="session")
def browser(request, playwright):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless", default=False)
    browser = getattr(playwright, browser_name).launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()
