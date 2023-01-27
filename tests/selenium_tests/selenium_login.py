#lib
from assertpy import assert_that

#fixtures
from selenium_ui.selenium_fixtures.fixtures import base, main, sign_up
from selenium_ui.utilities_selenium.user_utilities_se import User

user = 'bts'
password = '12345'

def test_login(base, main, sign_up):

    base.return_to_base_page()
    sign_up.username().send_keys(data=user, clear=True)
    sign_up.password().clean_text()
    sign_up.password().send_keys(data=password, clear=True)
    sign_up.login().click()

    assert_that(main.welcome().get_text()).contains('Welcome')
    assert_that(main.welcome().element_exit()).is_true()
    assert_that(main.sign_out().element_exit()).is_true()
    assert_that(main.my_account().element_exit()).is_true()
    assert_that(main.main_picture().element_exit()).is_true()

    #logout
    base.return_to_base_page()
    main.sign_out().click()
