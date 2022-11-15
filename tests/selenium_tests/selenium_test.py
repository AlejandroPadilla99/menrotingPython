#lib
from time import sleep
from assertpy import assert_that
import time

#local
from selenium_ui.pages.main_page import MainPage
from selenium_ui.pages.sing_up import SingUpPage
from selenium_ui.pages.register_page import RegisterPage
from selenium_ui.pages.fish_section import FishPage
from selenium_ui.pages.angelfish_page import AngelFishPage
from selenium_ui.utilities_selenium.user_utilities_se import User

#fixture
#from utilities.conftest import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Initialize the ChromeDriver instance
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

# Make its calls wait up to 10 second for element to appear
browser.implicitly_wait(time_to_wait=10)

#return the WebDriver instance for the setup
#yield driver

#Quit the WebDriver instance for the cleanup
#driver.quit()

def test_login_in_website():

    browser.get('https://petstore.octoperf.com/actions/Account.action?signonForm=')

    #Pages
    main_page = MainPage(driver=browser)
    sing_up_page = SingUpPage(driver=browser)

    #test
    main_page.sing_in().click()
    sing_up_page.username().send_keys(data='test')
    sing_up_page.password().send_keys(data='12345')
    sing_up_page.login().click()

def test_register_in_website():
    
    browser.get('https://petstore.octoperf.com/actions/Account.action?signonForm=')

    #precondition
    user = User()
    user.create_account_data()
    #Pages
    main_page = MainPage(driver=browser)
    sing_up_page = SingUpPage(driver=browser)
    register_page = RegisterPage(driver=browser)

    #test
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
    time.sleep(10)
    

