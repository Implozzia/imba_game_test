from .locators import PaymentPageLocators
from .base_page import BasePage


class PaymentPage(BasePage):
    def iframe_order(self):
        self.browser.switch_to.frame(self.browser.find_element(*PaymentPageLocators.IFRAME))
        card_btn = self.browser.find_element(*PaymentPageLocators.IFRAME_BANK_CARD)
        card_btn.click()