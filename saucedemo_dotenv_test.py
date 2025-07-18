from playwright.sync_api import sync_playwright, expect
import os
from dotenv import  load_dotenv

load_dotenv()

def test_saucedemo():
    playwright = sync_playwright().start()
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    try:
        # Открываем страницу, проверяем тайтл
        page.goto(os.getenv("SD_URL"), timeout=10000)
        expect(page).to_have_title("Swag Labs")

        # Авторизация
        page.fill("#user-name", os.getenv("SD_USERNAME"))
        page.fill("#password", os.getenv("SD_PASSWORD"))
        page.click("#login-button")
        # Проверка авторизации
        assert page.locator("#header_container > div.header_secondary_container > span").is_visible()
        assert page.title() == "Swag Labs"
        expect(page.locator("#header_container > div.header_secondary_container > span")).to_have_text("Products")

        # Добавление товара в корзину
        page.click("#item_4_title_link > div")
        page.click("#add-to-cart")

        # Проверка добавления товара в корзину
        expect(page.locator("#remove")).to_be_visible(timeout=10000)

    finally:
        # Закрытие
        browser.close()
        playwright.stop()