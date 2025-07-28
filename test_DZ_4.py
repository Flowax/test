import pytest
from playwright.sync_api import expect


# Фикстура авторизации
@pytest.fixture
def auth_page(page):
    page.goto("https://www.saucedemo.com/", timeout=10000)
    assert page.title() == "Swag Labs"
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    # Проверка авторизации
    assert page.locator("#header_container > div.header_secondary_container > span").is_visible()
    expect(page.locator("#header_container > div.header_secondary_container > span")).to_have_text("Products")

def test_add_to_cart(page, auth_page):
    # Добавление товара в корзину
    page.click("#item_4_title_link > div")
    page.click("#add-to-cart")
    # Проверка добавления товара в корзину
    expect(page.locator("#remove")).to_be_visible(timeout=10000)

def test_about_page(page, auth_page):
    # Переход на страницу About
    page.click("#react-burger-menu-btn")
    page.click("#about_sidebar_link")
    # Проверка открытия страницы About
    assert page.title() == "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"
