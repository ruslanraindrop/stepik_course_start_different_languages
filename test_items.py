import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestAddToCart:
    def test_add_button_is_present(self, browser):
        browser.get(link)
        time.sleep(30)
        add_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert add_button, "Button not available"
