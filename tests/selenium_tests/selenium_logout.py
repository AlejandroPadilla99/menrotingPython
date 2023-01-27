#lib
from assertpy import assert_that

#fixtures
from selenium_ui.selenium_fixtures.fixtures import base, main, sign_up
from selenium_ui.utilities_selenium.user_utilities_se import User

user = 'bts'
password = '12345'

def test_logout(base, main,sign_up):

    #precondition
    base.return_to_base_page()
    sign_up.username().send_keys(data=user, clear=True)
    sign_up.password().clean_text()
    sign_up.password().send_keys(data=password, clear=True)
    sign_up.login().click()

    #test
    base.return_to_base_page()
    main.sign_out().click()

    assert_that(main.sign_in().element_exit()).is_true()
