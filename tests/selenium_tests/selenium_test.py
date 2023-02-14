#lib
from assertpy import assert_that

#local
from config import USER, PASSWORD

#fixtures
from selenium_ui.selenium_fixtures.fixtures import base, main, sign_up, register, shopping_cart, payment_details, order_page, user_information, session
from selenium_ui.utilities_selenium.user_utilities_se import User

user_old = USER 
password_old = PASSWORD

#User
user = User()
user.create_account_data()
user.create_profile_data(language_preference='japanese', favorite_category='CATS', my_list=True, my_banner=True)

def test_buy_by_search_bar(base, main, shopping_cart, payment_details, order_page, session):
 
    #test
    base.return_to_base_page()
    main.search_bar().send_keys(data='dog', clear=True)
    main.search_button().click()
    main.firts_element_search().click()
    main.add_cart().click()
    shopping_cart.checkout().click()

    assert_that(payment_details.first_name().get_value()).is_equal_to(session.account_data.get('first_name'))
    assert_that(payment_details.last_name().get_value()).is_equal_to(session.account_data.get('second_name'))
    assert_that(payment_details.address1().get_value()).is_equal_to(session.account_data.get('address1'))
    assert_that(payment_details.address2().get_value()).is_equal_to(session.account_data.get('address2'))
    assert_that(payment_details.city().get_value()).is_equal_to(session.account_data.get('city'))
    assert_that(payment_details.state().get_value()).is_equal_to(session.account_data.get('state'))
    assert_that(payment_details.zip().get_value()).is_equal_to(session.account_data.get('zip'))
    assert_that(payment_details.country().get_value()).is_equal_to(session.account_data.get('country'))

    payment_details.continue_button().click()
    order_page.confirm().click()

    assert_that(payment_details.thank_you().element_exit()).is_true()

    base.logout_session()

def test_search_empty_bar(base, main):

    #test
    base.return_to_base_page()
    main.search_bar().send_keys(data='', clear=True)
    main.search_button().click()
    
    assert_that(main.error_empty().get_text()).is_equal_to('Please enter a keyword to search for, then press the search button.')

def test_update_account_data(base, main, user_information, session):

    #precondition 
    user.create_account_data()

    #test
    base.return_to_base_page()
    main.my_account().click()
    user_information.first_name().send_keys(user.account_data.get('first_name'), clear=True)
    user_information.last_name().send_keys(user.account_data.get('second_name'), clear=True)
    user_information.email().send_keys(user.account_data.get('email'), clear=True)
    user_information.phone().send_keys(user.account_data.get('phone'), clear=True)
    user_information.address1().send_keys(user.account_data.get('address1'), clear=True)
    user_information.address2().send_keys(user.account_data.get('address2'), clear=True)
    user_information.city().send_keys(user.account_data.get('city'), clear=True)
    user_information.state().send_keys(user.account_data.get('state'), clear=True)
    user_information.zip().send_keys(user.account_data.get('zip'), clear=True)
    user_information.country().send_keys(user.account_data.get('country'), clear=True)
    user_information.save().click()
    base.return_to_base_page()
    main.my_account().click()

    assert_that(user_information.first_name().get_value()).is_equal_to(user.account_data.get('first_name'))
    assert_that(user_information.last_name().get_value()).is_equal_to(user.account_data.get('second_name'))
    assert_that(user_information.email().get_value()).is_equal_to(user.account_data.get('email'))
    assert_that(user_information.phone().get_value()).is_equal_to(user.account_data.get('phone'))
    assert_that(user_information.address1().get_value()).is_equal_to(user.account_data.get('address1'))
    assert_that(user_information.address2().get_value()).is_equal_to(user.account_data.get('address2'))
    assert_that(user_information.city().get_value()).is_equal_to(user.account_data.get('city'))
    assert_that(user_information.state().get_value()).is_equal_to(user.account_data.get('state'))
    assert_that(user_information.zip().get_value()).is_equal_to(user.account_data.get('zip'))
    assert_that(user_information.country().get_value()).is_equal_to(user.account_data.get('country'))