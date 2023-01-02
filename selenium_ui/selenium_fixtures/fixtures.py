#lib
import pytest

#local
from selenium_ui.pages.base_page import BasePage
from selenium_ui.pages.main_page import MainPage
from selenium_ui.pages.sign_up import SingUpPage
from selenium_ui.pages.register_page import RegisterPage
from selenium_ui.pages.shopping_cart_page import ShoppingCartPage
from selenium_ui.pages.payment_details_page import PaymentDetailsPages
from selenium_ui.pages.order_page import OderPage
from selenium_ui.pages.user_information_page import UserInformation

@pytest.fixture
def base():
    base_page = BasePage()
    return base_page

@pytest.fixture
def main():
    main_page = MainPage()
    return main_page

@pytest.fixture
def sign_up():
    sign_up = SingUpPage()
    return sign_up

@pytest.fixture
def register():
    register = RegisterPage()
    return register

@pytest.fixture
def shopping_cart():
    shopping_cart = ShoppingCartPage()
    return shopping_cart

@pytest.fixture
def payment_details():
    payment_details = PaymentDetailsPages()
    return payment_details

@pytest.fixture
def order_page():
    order_page = OderPage()
    return order_page

@pytest.fixture
def user_information():
    user_information = UserInformation()
    return user_information