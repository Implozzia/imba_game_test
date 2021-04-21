from .pages.catalog_page import CatalogPage
from selenium import webdriver
import time


def test_order_from_catalog_page(browser):
    link = 'https://kz.imba.shop/'
    page = CatalogPage(browser, link)
    browser.implicitly_wait(10)
    page.open()
    page.go_to_merch_tab()
    page.scroll_to_mousepad()
    page.add_mousepad_to_cart()
    page.use_promocode()
    page.should_be_promocode_text()
    page.go_to_order_page()
    page.fill_order_page_data()
    time.sleep(10)  # TODO заменить на нормальное ожидание
    page.should_be_available_all_delivery()
    page.accept_order()
    time.sleep(10)  # TODO заменить на нормальное ожидание
    page.iframe_order()
    time.sleep(5)
