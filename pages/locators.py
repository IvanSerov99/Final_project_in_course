from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, ".well#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".well#register_form")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    HEADER_ITEM = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner strong")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_PAGE = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "div.content div#content_inner p")
    EMPTY_BASKET = (By.CSS_SELECTOR, "form.basket_summary#basket_formset")


