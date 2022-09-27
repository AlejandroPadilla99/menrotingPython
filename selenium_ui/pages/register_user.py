#lib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker

#local
from selenium_ui.config_selenium import URL_SE

import time

class RegisterUser:

    def __init__(self, browser: object) -> None:
        self.base_url = URL_SE
        self.base_xpath = '/html/body/'
        self.browser = browser
        self.finder = self.browser.find_element
    
    def load_page(self) -> None:
        self.browser.get(url=self.base_url)
        self.browser.find_element(By.XPATH, self.base_xpath+'div[1]/div[2]/div/a[2]').click()

    def click_register_now(self)-> None:

        #find the elements
        register_button = self.finder(By.XPATH, self.base_xpath+'div[2]/div/a')

        #Do the actions
        register_button.click()

    def enter_user_data(self, user_data: dict) -> None:

        #find the elements
        input_id = self.finder(By.NAME, 'username')
        input_new_password = self.finder(By.NAME, 'password')
        input_repeat_password = self.finder(By.NAME, 'repeatedPassword')

        #Do the actions
        input_id.send_keys(user_data['id'])
        input_new_password.send_keys(user_data['password'])
        input_repeat_password.send_keys(user_data['password'])

    def enter_account_data(self, account_data: dict) -> None:

        #find the elements
        input_firstname = self.finder(By.NAME, 'account.firstName')
        input_lastname = self.finder(By.NAME, 'account.lastName')
        input_email = self.finder(By.NAME, 'account.email')
        input_phone = self.finder(By.NAME, 'account.phone')
        input_address_1 = self.finder(By.NAME, 'account.address1')
        input_address_2 = self.finder(By.NAME, 'account.address2')
        input_city = self.finder(By.NAME, 'account.city')
        input_state = self.finder(By.NAME, 'account.state')
        input_zip = self.finder(By.NAME, 'account.zip')
        input_country = self.finder(By.NAME, 'account.country')
        
        #do the actions 
        input_firstname.send_keys(account_data['first_name'])
        input_lastname.send_keys(account_data['second_name'])
        input_email.send_keys(account_data['email'])
        input_phone.send_keys(account_data['phone'])
        input_address_1.send_keys(account_data['address1'])
        input_address_2.send_keys(account_data['address2'])
        input_city.send_keys(account_data['city'])
        input_state.send_keys(account_data['state'])
        input_zip.send_keys(account_data['zip'])
        input_country.send_keys(account_data['country'])
       
        
    def enter_profile_data(self,  profile_data: dict) -> None:

        #find the elements
        select_language_preference = Select(self.finder(By.NAME, 'account.languagePreference'))
        select_favourite_category = Select(self.finder(By.NAME,  'account.favouriteCategoryId'))
        input_enable_my_list = self.finder(By.NAME, 'account.listOption')
        input_enable_my_banner = self.finder(By.NAME, 'account.bannerOption')
        input_save = self.finder(By.NAME, 'newAccount')

        #do the actions
        select_language_preference.select_by_value(profile_data['language_preference'])
        select_favourite_category.select_by_value(profile_data['favorite_category'])
        if profile_data['my_list']:
            input_enable_my_list.click()
        if profile_data['my_banner']:
            input_enable_my_banner.click()
        
        input_save.click()





