from playwright.sync_api import sync_playwright, expect


def test_saucedemo():
    playwright = sync_playwright().start()
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    try:
        # Открываем страницу, проверяем тайтл
        page.goto("https://www.saucedemo.com/", timeout=10000)
        expect(page).to_have_title("Swag Labs")

        # Авторизация
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Проверка авторизации
        expect(page.locator("#header_container > div.header_secondary_container > span")).to_be_visible(timeout=10000)

        # Добавление товара в корзину
        page.click("#item_4_title_link > div")
        page.click("#add-to-cart")

        # Проверка добавления товара в корзину
        expect(page.locator("#remove")).to_be_visible(timeout=10000)

    finally:
        # Закрытие
        browser.close()
        playwright.stop()