from selenium.webdriver.common.by import By


class BasePageLocators:
    CART_ICON = (By.CSS_SELECTOR, '.basket-link')
    HEADER_CATALOG_LINK = (By.LINK_TEXT, 'Магазин')
    POPUP_CONTINUE_SHOPPING = (By.CSS_SELECTOR, '.thankyou-popup__continue-link')


class CartPageLocators:
    PROMO_INPUT = (By.CSS_SELECTOR, '.cart-block__input-block')
    PROMO_BTN = (By.CSS_SELECTOR, '.cart-block__send-button')
    PROMO_SUCCESS_TXT = (By.CSS_SELECTOR, '.cart-block__promo-text')
    ORDER_BTN = (By.CSS_SELECTOR, '.cart-block__order-button')
    DELETE_MANGO_BTN = (By.XPATH, '/html/body/div[2]/div/form/div[1]/div[4]/div[2]/button')


class CatalogPageLocators:
    MERCH_TAB = (By.CSS_SELECTOR, '.productslist-categories__item--6')
    MOUSEPAD = (By.CSS_SELECTOR, '.product-item:nth-child(6)')
    MOUSEPAD_BTN = (By.CSS_SELECTOR, '.product-item:nth-child(6) button')
    FIRST_ITEM_ON_PAGE = (By.CSS_SELECTOR, '.product-item:nth-child(1) button')
    SHAKER = (By.CSS_SELECTOR, '.product-item:nth-child(12)')
    SHAKER_BTN = (By.CSS_SELECTOR, '.product-item:nth-child(12) button')
    MANGO = (By.CSS_SELECTOR, '.product-item:nth-child(7)')
    MANGO_BTN = (By.CSS_SELECTOR, '.product-item:nth-child(7) button')


class OrderPageLocators:
    NUMBER = (By.CSS_SELECTOR, '#client_phone')
    NAME = (By.CSS_SELECTOR, '#client_name')
    CITY = (By.CSS_SELECTOR, '#shipping_address_full_locality_name')
    ADDRESS = (By.CSS_SELECTOR, '#shipping_address_address')
    ORDER_BTN = (By.CSS_SELECTOR, '#create_order')
    IMBA_CLUB = (By.CSS_SELECTOR, '#delivery_title_2896395')
    DELIVERY_SBER = (By.CSS_SELECTOR, '#delivery_title_2860009')
    DELIVERY_BOXBERRY_COURIER = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/div[2]/label[1]/span[2]/span[1]')
    DELIVERY_BOXBERRY_PICKUP = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/div[2]/label[2]/span[2]/span[1]')
    DELIVERY_PICKPOINT = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/div[2]/label[3]/span[2]/span[1]')
    NEWS_CHECKBOX = (By.CSS_SELECTOR, '.co-input-information')
    CREATE_ORDER_BTN = (By.CSS_SELECTOR, '#create_order')
    DELIVERY_INFO = (By.CSS_SELECTOR, '.checkout-block__free-delivery')
    FREE_DELIVERY = (By.CSS_SELECTOR, '#price_2298042')


class PaymentPageLocators:
    IFRAME = (By.CSS_SELECTOR, '.with-appled')
    IFRAME_BANK_CARD = (By.XPATH, '//*[@id="paymentMethodsContainer"]/div[1]/button')


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.vers1')
    INCREMENT_QUANTITY = (By.CSS_SELECTOR, '.product-card__plus')


class MainPageLocators:
    MOSAIC_ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.products-mosaic__item:nth-child(1) .indexproduct__buy-button')
