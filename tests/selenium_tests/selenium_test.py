#lib
from time import sleep
from assertpy import assert_that
import time


#fixtures
from selenium_ui.selenium_fixtures.fixtures import base, main, sign_up, register, shopping_cart, payment_details, order_page, user_information
from selenium_ui.utilities_selenium.user_utilities_se import User

#User
user = User()
user.create_account_data()
user.create_profile_data(language_preference='japanese', favorite_category='CATS', my_list=True, my_banner=True)

def test_register_in_website(base, main, sign_up, register):
    
    #test
    base.return_to_base_page()
    main.sign_in().click()
    sign_up.register().click()
    register.user_id().send_keys(data=user.user_credentials.get('id'))
    register.new_password().send_keys(data=user.user_credentials.get('password'))
    register.repeat_password().send_keys(data=user.user_credentials.get('password'))
    register.first_name().send_keys(data=user.account_data.get('first_name'))
    register.last_name().send_keys(data=user.account_data.get('second_name'))
    register.email().send_keys(data=user.account_data.get('email'))
    register.phone().send_keys(data=user.account_data.get('phone'))
    register.address1().send_keys(data=user.account_data.get('address1'))
    register.address2().send_keys(data=user.account_data.get('address2'))
    register.city().send_keys(data=user.account_data.get('city'))
    register.state().send_keys(data=user.account_data.get('state'))
    register.zip().send_keys(data=user.account_data.get('zip'))
    register.country().send_keys(data=user.account_data.get('country'))
    register.language_preference().select_by_value(data=user.profile_data.get('language_preference'))
    register.favourite_category().select_by_value(data=user.profile_data.get('favorite_category'))
    register.mylist().click()
    register.mybanner().click()
    register.save_account().click()
    main.sign_in().click()
    sign_up.username().send_keys(data=user.user_credentials.get('id'))
    sign_up.password().clean_text()
    sign_up.password().send_keys(data=user.user_credentials.get('password'))
    sign_up.login().click()

    assert_that(main.welcome().get_text()).contains('Welcome')
    assert_that(main.welcome().element_exit(time=5)).is_true()
    assert_that(main.sign_out().element_exit(time=5)).is_true()
    assert_that(main.my_account().element_exit(time=5)).is_true()
    assert_that(main.main_picture().element_exit(time=5)).is_true()

def test_buy_by_search_bar(base, main, shopping_cart, payment_details, order_page):
    
    #test
    base.return_to_base_page()
    main.search_bar().send_keys(data='dog')
    main.search_button().click()
    main.firts_element_search().click()
    main.add_cart().click()
    shopping_cart.checkout().click()

    assert_that(payment_details.first_name().get_attribute(name='value')).is_equal_to(user.account_data.get('first_name'))
    assert_that(payment_details.last_name().get_attribute(name='value')).is_equal_to(user.account_data.get('second_name'))
    assert_that(payment_details.address1().get_attribute(name='value')).is_equal_to(user.account_data.get('address1'))
    assert_that(payment_details.address2().get_attribute(name='value')).is_equal_to(user.account_data.get('address2'))
    assert_that(payment_details.city().get_attribute(name='value')).is_equal_to(user.account_data.get('city'))
    assert_that(payment_details.state().get_attribute(name='value')).is_equal_to(user.account_data.get('state'))
    assert_that(payment_details.zip().get_attribute(name='value')).is_equal_to(user.account_data.get('zip'))
    assert_that(payment_details.country().get_attribute(name='value')).is_equal_to(user.account_data.get('country'))

    payment_details.continue_button().click()
    order_page.confirm().click()

    assert_that(payment_details.thank_you().element_exit(time=5)).is_true()

def test_update_account_data(base, main, user_information):

    #precondition 
    user.create_account_data()

    #test
    base.return_to_base_page()
    main.my_account().click()
    user_information.first_name().send_keys(user.account_data.get('first_name'))
    user_information.last_name().send_keys(user.account_data.get('second_name'))
    user_information.email().send_keys(user.account_data.get('email'))
    user_information.phone().send_keys(user.account_data.get('phone'))
    user_information.address1().send_keys(user.account_data.get('address1'))
    user_information.address2().send_keys(user.account_data.get('address2'))
    user_information.city().send_keys(user.account_data.get('city'))
    user_information.state().send_keys(user.account_data.get('state'))
    user_information.zip().send_keys(user.account_data.get('zip'))
    user_information.country().send_keys(user.account_data.get('country'))
    user_information.save().click()
    base.return_to_base_page()
    main.my_account().click()

    assert_that(user_information.first_name().get_attribute(name='value')).is_equal_to(user.account_data.get('first_name'))
    assert_that(user_information.last_name().get_attribute(name='value')).is_equal_to(user.account_data.get('second_name'))
    assert_that(user_information.email().get_attribute(name='value')).is_equal_to(user.account_data.get('email'))
    assert_that(user_information.phone().get_attribute(name='value')).is_equal_to(user.account_data.get('phone'))
    assert_that(user_information.address1().get_attribute(name='value')).is_equal_to(user.account_data.get('address1'))
    assert_that(user_information.address2().get_attribute(name='value')).is_equal_to(user.account_data.get('address2'))
    assert_that(user_information.city().get_attribute(name='value')).is_equal_to(user.account_data.get('city'))
    assert_that(user_information.state().get_attribute(name='value')).is_equal_to(user.account_data.get('state'))
    assert_that(user_information.zip().get_attribute(name='value')).is_equal_to(user.account_data.get('zip'))
    assert_that(user_information.country().get_attribute(name='value')).is_equal_to(user.account_data.get('country'))

def test_sign_out(base, main):

    #test
    base.return_to_base_page()
    main.sign_out().click()

    assert_that(main.sign_in().element_exit(time=5)).is_true()