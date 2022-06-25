from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_REGISTRATION_FORM)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_FORM)
        input_password.send_keys(password)
        confirm_input_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTRATION_FORM)
        confirm_input_password.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()
        confirm_registration_right_text = "Thanks for registering!"
        confirm_registration_right = self.browser.find_element(*LoginPageLocators.SUCCESSFULL_REGISTRATION)
        assert str(confirm_registration_right.text) == confirm_registration_right_text, \
            "Registration was not successful"