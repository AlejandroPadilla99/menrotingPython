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
    return  BasePage()

@pytest.fixture
def main():
    return MainPage()

@pytest.fixture
def sign_up():
    return SingUpPage()

@pytest.fixture
def register():
    return RegisterPage()

@pytest.fixture
def shopping_cart():
    return ShoppingCartPage()

@pytest.fixture
def payment_details():
    return  PaymentDetailsPages()

@pytest.fixture
def order_page():
    return OderPage()

@pytest.fixture
def user_information():
    return UserInformation()