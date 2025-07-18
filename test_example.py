def test_example(page):
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(2000)
    assert "Swag Labs" in page.title()
    print("vse ok")
