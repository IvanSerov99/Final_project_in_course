from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)


    def basket_must_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"

    def basket_should_have_text_that_it_is_empty(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        right_empty_basket_text = "Your basket is empty. Continue shopping"
        assert str(empty_basket_text.text) == right_empty_basket_text, \
            "The empty cart text is different from the correct one"