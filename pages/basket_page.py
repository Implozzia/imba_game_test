from .locators import CartPageLocators
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class BasketPage(BasePage):
    def delete_mango_item(self):
        delete_btn = self.browser.find_element(*CartPageLocators.DELETE_MANGO_BTN)
        delete_btn.click()

    def use_promocode(self):
        promo_input = self.browser.find_element(*CartPageLocators.PROMO_INPUT)
        promo_input.send_keys('bebey')
        promo_btn = self.browser.find_element(*CartPageLocators.PROMO_BTN)
        promo_btn.click()

    def scroll_to_promocode_area(self):
        promo_input = self.browser.find_element(*CartPageLocators.PROMO_INPUT)
        ActionChains(self.browser).move_to_element(promo_input).perform()

    def should_be_promocode_text(self):
        promo_text = self.browser.find_element(*CartPageLocators.PROMO_SUCCESS_TXT).text
        assert promo_text == 'Скидка по купону BEBEY', "Promocode text doesn't equal"

    def go_to_order_page(self):
        order_btn = self.browser.find_element(*CartPageLocators.ORDER_BTN)
        order_btn.click()
