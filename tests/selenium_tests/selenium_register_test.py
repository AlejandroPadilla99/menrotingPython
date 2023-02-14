#lib
from assertpy import assert_that

#fixtures
from selenium_ui.selenium_fixtures.fixtures import base, main, sign_up, register
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
    register.user_id().send_keys(data=user.user_credentials.get('id'), clear=True)
    register.new_password().send_keys(data=user.user_credentials.get('password'), clear=True)
    register.repeat_password().send_keys(data=user.user_credentials.get('password'), clear=True)
    register.first_name().send_keys(data=user.account_data.get('first_name'), clear=True)
    register.last_name().send_keys(data=user.account_data.get('second_name'), clear=True)
    register.email().send_keys(data=user.account_data.get('email'), clear=True)
    register.phone().send_keys(data=user.account_data.get('phone'), clear=True)
    register.address1().send_keys(data=user.account_data.get('address1'), clear=True)
    register.address2().send_keys(data=user.account_data.get('address2'), clear=True)
    register.city().send_keys(data=user.account_data.get('city'), clear=True)
    register.state().send_keys(data=user.account_data.get('state'), clear=True)
    register.zip().send_keys(data=user.account_data.get('zip'), clear=True)
    register.country().send_keys(data=user.account_data.get('country'), clear=True)
    register.language_preference().select_by_value(data=user.profile_data.get('language_preference'))
    register.favourite_category().select_by_value(data=user.profile_data.get('favorite_category'))
    register.mylist().click()
    register.mybanner().click()
    register.save_account().click()
    main.sign_in().click()
    sign_up.username().send_keys(data=user.user_credentials.get('id'), clear=True)
    sign_up.password().clean_text()
    sign_up.password().send_keys(data=user.user_credentials.get('password'), clear=True)
    sign_up.login().click()

    assert_that(main.welcome().get_text()).contains(user.account_data.get('first_name'))
    assert_that(main.welcome().element_exit()).is_true()
    assert_that(main.sign_out().element_exit()).is_true()
    assert_that(main.my_account().element_exit()).is_true()
    assert_that(main.main_picture().element_exit()).is_true()

    #logout
    base.return_to_base_page()
    main.sign_out().click()
