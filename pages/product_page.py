import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def get_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        return item_name.text

    def get_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        return item_price.text

    def get_item_header(self):
        item_header = self.browser.find_element(*ProductPageLocators.HEADER_ITEM)
        print(item_header)
        return item_header.text

    def push_on_addcart_button(self, item_name, item_price):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
        add_product.click()

    def add_cart_button_can_be_pushed(self, item_name, item_price):
        assert self.is_element_present(*ProductPageLocators.ADD_CART_BUTTON), "There is no button add product to cart"

    def add_item_right(self, item_name):
        item_header = ProductPage.get_item_header(self)
        assert str(item_name) == str(item_header)
