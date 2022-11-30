#lib
from time import sleep
from assertpy import assert_that
import time

#local
from selenium_ui.pages.base_page import BasePage
from selenium_ui.pages.main_page import MainPage
from selenium_ui.pages.sing_up import SingUpPage
from selenium_ui.pages.register_page import RegisterPage
from selenium_ui.pages.shopping_cart_page import ShoppingCartPage
from selenium_ui.utilities_selenium.user_utilities_se import User


def test_login_in_website():

    #Pages
    base_page = BasePage() 
    main_page = MainPage()
    sing_up_page = SingUpPage()

    #test
    base_page.return_to_base__page()
    main_page.sing_in().click()
    sing_up_page.username().send_keys(data='test')
    sing_up_page.password().send_keys(data='12345')
    sing_up_page.login().click()

def test_register_in_website():
    

    #precondition
    user = User()
    user.create_account_data()
    #Pages
    base_page = BasePage()
    main_page = MainPage()
    sing_up_page = SingUpPage()
    register_page = RegisterPage()

    #test
    base_page.return_to_base__page()
    main_page.sing_in().click()
    sing_up_page.register().click()
    register_page.user_id().send_keys(data='test')
    register_page.new_password().send_keys(data='12345')
    register_page.repeat_password().send_keys(data='12345')
    register_page.first_name().send_keys(data='Juan')
    register_page.last_name().send_keys(data='Perez')
    register_page.email().send_keys(data='example@gmail.com')
    register_page.phone().send_keys(data='395678123')
    register_page.address1().send_keys(data='123')
    register_page.address2().send_keys(data='123')
    register_page.city().send_keys(data='Guadalajara')
    register_page.state().send_keys(data='Jalisco')
    register_page.zip().send_keys(data='124123')
    register_page.country().send_keys(data='Mexico')
    #register_page.language_preference().select_by_value(data='english')
    #register_page.favourite_category().select_by_value(data='CATS')
    register_page.mylist().click()
    register_page.mybanner().click()

def test_buy_by_search_bar():
 
    #Pages
    base_page = BasePage()
    main_page = MainPage()
    shopping_cart = ShoppingCartPage()
    
    #test
    base_page.return_to_base__page()
    main_page.search_bar().send_keys(data='dog')
    main_page.search_button().click()
    main_page.firts_element_search().click()
    main_page.add_cart().click()
    shopping_cart.checkout().click() 