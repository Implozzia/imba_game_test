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

