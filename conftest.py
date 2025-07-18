import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", choices=["chromium", "firefox", "webkit"])
    parser.addoption("--headless", action="store", default="False", choices=["False", "True"], help="Headless mode")

@pytest.fixture(scope="session")
def playwright():
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope="session")
def browser(request, playwright):
    browser_name = request.config.getoption("--browser")
    headconf = request.config.getoption("--headless") == "True"
    browser = getattr(playwright, browser_name).launch(headless=headconf)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()
