from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def add_to_basket_mosaic_product(self):
        add_to_basket_btn = self.browser.find_element(*MainPageLocators.MOSAIC_ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
