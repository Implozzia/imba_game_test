from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.catalog_page import CatalogPage
from selenium import webdriver
import time


def test_order_from_catalog_page(browser):
    link = 'https://kz.imba.shop/'
    page = MainPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.add_to_basket_mosaic_product()
    base_page = BasePage(browser, browser.current_url)
    time.sleep(2)
    base_page.continue_shopping_popup()
    base_page.go_to_catalog_page()

    catalog_page = CatalogPage(browser, browser.current_url)
    catalog_page.add_first_item_to_cart()
    catalog_page.scroll_to_shaker_and_open_item()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    page.continue_shopping_popup()

    base_page.go_to_catalog_page()
    catalog_page.scroll_to_mango_and_open_item()

    product_page.increment_quantity()
    product_page.add_to_basket()
    time.sleep(2)
    base_page.continue_shopping_popup()

    base_page.go_to_basket_page()
    time.sleep(10)

