from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def increment_quantity(self):
        quantity_btn = self.browser.find_element(*ProductPageLocators.INCREMENT_QUANTITY)
        quantity_btn.click()
        quantity_btn.click()
