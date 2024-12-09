from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.ui.pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_BUTTON = (By.ID, "login2")
    SIGNUP_BUTTON = (By.ID, "signin2")
    PRODUCT_LIST = (By.CLASS_NAME, "card-title")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_main_page(self):
        self.open("https://www.demoblaze.com")

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_product_titles(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_LIST)
        )
        elements = self.driver.find_elements(*self.PRODUCT_LIST)
        return [el.text for el in elements]
