#lib
from assertpy import assert_that
#local
from selenium_ui.pages.login import Login
from selenium_ui.pages.register_user import RegisterUser
from selenium_ui.pages.buy_fish import BuyFish
from selenium_ui.utilities_selenium.user_utilities_se import User

def test_login_in_website(browser):

    #preconditions
    login_page = Login(browser=browser)

    #test
    login_page.load_page()
    login_page.enter_data(username='Alejandro',password='12345')

    assert_that(login_page.get_result_login()).is_equal_to('Welcome alejandro!')

    #delete data
    del login_page

'''
def test_create_user(browser):

    #preconditions
    user = User()
    login_page = Login(browser=browser)
    register_user = RegisterUser(browser=browser)

    #test
    register_user.load_page()
    register_user.click_register_now()
    register_user.enter_user_data(user_data=user.user_credentials)
    register_user.enter_account_data(account_data=user.account_data)
    register_user.enter_profile_data(profile_data=user.profile_data)
    
    login_page.load_page()
    login_page.enter_data(username=user.user_credentials['id'], password=user.user_credentials['password'])

    assert_that(login_page.get_result_login(), description='hola').is_equal_to(f'Welcome {user.account_data["first_name"]}!')

    del login_page, register_user

def test_buy_pet(browser):
    
    #preconditions
    login = Login(browser=browser)
    buy_fish = BuyFish(browser=browser)

    login.load_page()
    login.enter_data(username='Alejandro', password='12345')

    #test
    buy_fish.select_fish_store()
    buy_fish.select_fish()
    buy_fish.select_specie_fish()
    buy_fish.select_checkout_button()
    buy_fish.select_continue_button()
    buy_fish.select_confirm_button()

    del login, buy_fish

'''