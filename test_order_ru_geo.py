from .pages.catalog_page import CatalogPage
from .pages.basket_page import BasketPage
from .pages.order_page import OrderPage
from .pages.payment_page import PaymentPage
from selenium import webdriver
import time


def test_order_from_catalog_page(browser):
    link = 'https://imba.shop/collection/tovary'
    page = CatalogPage(browser, link)
    browser.implicitly_wait(10)
    page.open()
    page.go_to_merch_tab()
    page.scroll_to_mousepad()
    page.add_mousepad_to_cart()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.use_promocode()
    basket_page.should_be_promocode_text()
    basket_page.go_to_order_page()

    order_page = OrderPage(browser, browser.current_url)
    order_page.fill_order_page_data()
    time.sleep(10)  # TODO заменить на нормальное ожидание
    order_page.should_be_available_all_delivery()
    order_page.accept_order()
    time.sleep(5)

    payment_page = PaymentPage(browser, browser.current_url)
    payment_page.iframe_order()
    time.sleep(5)
