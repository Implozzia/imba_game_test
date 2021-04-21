from .locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):
    def fill_order_page_data(self):
        number_input = self.browser.find_element(*OrderPageLocators.NUMBER)
        number_input.send_keys('+79110000000')

        name_input = self.browser.find_element(*OrderPageLocators.NAME)
        name_input.send_keys('test test')

        city_input = self.browser.find_element(*OrderPageLocators.CITY)
        city_input.clear()
        city_input.send_keys('г Нижний Новгород, Нижегородская обл.')
        name_input.click()

        address_input = self.browser.find_element(*OrderPageLocators.ADDRESS)
        address_input.send_keys('test test')

    def should_be_available_all_delivery(self):
        delivery_sber = self.browser.find_element(*OrderPageLocators.DELIVERY_SBER).text
        assert delivery_sber == 'Забрать в отделении Сбербанка или в Пятёрочке', 'Boxberry courier is not available'

        delivery_boxberry_courier = self.browser.find_element(*OrderPageLocators.DELIVERY_BOXBERRY_COURIER).text
        assert delivery_boxberry_courier == 'Курьером Boxberry (Только онлайн оплата)', 'Boxberry courier is not available'

        delivery_boxberry_pickup = self.browser.find_element(*OrderPageLocators.DELIVERY_BOXBERRY_PICKUP).text
        assert delivery_boxberry_pickup == 'Самовывоз Boxberry (Только онлайн оплата)', 'Boxberry pickup is not available'

        delivery_pickpoint = self.browser.find_element(*OrderPageLocators.DELIVERY_PICKPOINT).text
        assert delivery_pickpoint == 'PickPoint (Только онлайн оплата)', 'PickPoint is not available'

    def accept_order(self):
        news_checkbox = self.browser.find_element(*OrderPageLocators.NEWS_CHECKBOX)
        news_checkbox.click()
        order_btn = self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN)
        order_btn.click()