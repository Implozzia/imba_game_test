from .locators import CatalogPageLocators
from .locators import BasePageLocators
from .locators import CartPageLocators
from .locators import OrderPageLocators
from .locators import PaymentPageLocators
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CatalogPage(BasePage):
    def go_to_merch_tab(self):
        merch_tab = self.browser.find_element(*CatalogPageLocators.MERCH_TAB)
        merch_tab.click()

    def scroll_to_mousepad(self):
        mousepad = self.browser.find_element(*CatalogPageLocators.MOUSEPAD)
        ActionChains(self.browser).move_to_element(mousepad).perform()

    def add_mousepad_to_cart(self):
        mousepad_btn = self.browser.find_element(*CatalogPageLocators.MOUSEPAD_BTN)
        mousepad_btn.click()
        cart_icon = self.browser.find_element(*BasePageLocators.CART_ICON)
        cart_icon.click()


