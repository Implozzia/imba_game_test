from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def go_to_basket_page(self):
        basket_icon = self.browser.find_element(*BasePageLocators.CART_ICON)
        basket_icon.click()

    def go_to_catalog_page(self):
        catalog_page_link = self.browser.find_element(*BasePageLocators.HEADER_CATALOG_LINK)
        catalog_page_link.click()

    def continue_shopping_popup(self):
        continue_shopping_btn = self.browser.find_element(*BasePageLocators.POPUP_CONTINUE_SHOPPING)
        continue_shopping_btn.click()

