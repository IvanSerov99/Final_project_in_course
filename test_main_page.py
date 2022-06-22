import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_shop_functions():

    @pytest.mark.test_goods_has_add_to_basket_button
    def test_goods_has_add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.implicitly_wait(15)
        browser.get(link)
        #time.sleep(30) #sleep для проверки правильности инициализации браузера
        button = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "form.add-to-basket#add_to_basket_form button.btn.btn-lg.btn-primary.btn-add-to-basket")))
        assert (button!= None, 'Кнопка не найдена')
        button.click()

