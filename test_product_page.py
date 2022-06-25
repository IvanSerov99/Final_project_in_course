import time

import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
'''
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
'''
@pytest.mark.test_that_the_guest_can_add_an_item_to_the_cart
def test_that_the_guest_can_add_an_item_to_the_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    item_price = page.get_item_price()
    item_name = page.get_item_name()
    page.add_cart_button_can_be_pushed(item_name, item_price)
    page.push_on_addcart_button(item_name, item_price)
    test_selenuim_usage = BasePage(browser, link)
    test_selenuim_usage.solve_quiz_and_get_code()
    page.add_item_right(item_name)

@pytest.mark.xfail(reason="Making negative checks that the element is not present")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    item_price = page.get_item_price()
    item_name = page.get_item_name()
    page.push_on_addcart_button(item_name, item_price)
    page.should_not_be_success_message()

@pytest.mark.test_guest_cant_see_success_message
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Making negative checks that the element should have disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    item_price = page.get_item_price()
    item_name = page.get_item_name()
    page.push_on_addcart_button(item_name, item_price)
    page.success_message_should_disappeared()

@pytest.mark.test_guest_should_see_login_link_on_product_page
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.test_guest_can_go_to_login_page_from_product_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = BasePage(browser, browser.current_url)
    page.should_be_able_to_follow_the_login_page()







