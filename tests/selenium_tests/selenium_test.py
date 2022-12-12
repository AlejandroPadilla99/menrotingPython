#lib
from time import sleep
from assertpy import assert_that
import time


#fixtures
from selenium_ui.selenium_fixtures.fixtures import base, main, sing_up, register, shopping_cart, payment_details, order_page


def test_login_in_website(base, main, sing_up):

    #test
    print(base)
    base.return_to_base_page()
    main.sing_in().click()
    sing_up.username().send_keys(data='test19')
    sing_up.password().clean_text()
    sing_up.password().send_keys(data='12345')
    #sing_up.login().click()
    #assert_that(main.welcome().get_text()).contains('Welcome')

def test_register_in_website(base, main, sing_up, register):
    user = 'test00000000020'
    
    #test
    print(base)
    base.return_to_base_page()
    main.sing_in().click()
    sing_up.register().click()
    register.user_id().send_keys(data=user)
    register.new_password().send_keys(data='12345')
    register.repeat_password().send_keys(data='12345')
    register.first_name().send_keys(data='Juan')
    register.last_name().send_keys(data='Perez')
    register.email().send_keys(data='example@gmail.com')
    register.phone().send_keys(data='395678123')
    register.address1().send_keys(data='123')
    register.address2().send_keys(data='123')
    register.city().send_keys(data='Guadalajara')
    register.state().send_keys(data='Jalisco')
    register.zip().send_keys(data='124123')
    register.country().send_keys(data='Mexico')
    #register.language_preference().select_by_value(data='english')
    #register.favourite_category().select_by_value(data='CATS')
    register.mylist().click()
    register.mybanner().click()
    register.save_account().click()
    main.sing_in().click()
    sing_up.username().send_keys(data=user)
    sing_up.password().clean_text()
    sing_up.password().send_keys(data='12345')
    sing_up.login().click()

    #print(main.welcome().get_text(), " = this is the text")
    #assert_that(main.welcome().get_text()).contains('Welcome')
    assert_that(main.welcome().element_exit()).is_true()
    assert_that(main.sing_out().element_exit()).is_true()
    assert_that(main.my_account().element_exit()).is_true()

def test_buy_by_search_bar(base, main, shopping_cart, payment_details, order_page):
    print(base)
    pass
    #test
    '''
    base.return_to_base_page()
    main.search_bar().send_keys(data='dog')
    main.search_button().click()
    main.firts_element_search().click()
    main.add_cart().click()
    shopping_cart.checkout().click()
    order_page.confirm().click()
`
    '''
    