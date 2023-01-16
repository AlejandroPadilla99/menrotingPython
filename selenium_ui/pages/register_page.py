#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element
from selenium_ui.pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
    
    class locators(): 
        user_id =  (By.XPATH, "//input[@name='username']")
        new_password = (By.XPATH, "//input[@name='password']")
        repeat_password = (By.XPATH, "//input[@name='repeatedPassword']")
        first_name = (By.XPATH, "//input[@name='account.firstName']")
        last_name = (By.XPATH, "//input[@name='account.lastName']")
        email = (By.XPATH, "//input[@name='account.email']")
        phone = (By.XPATH, "//input[@name='account.phone']")
        address1 = (By.XPATH, "//input[@name='account.address1']")
        address2 = (By.XPATH, "//input[@name='account.address2']")
        city = (By.XPATH, "//input[@name='account.city']")
        state = (By.XPATH, "//input[@name='account.state']")
        zip = (By.XPATH, "//input[@name='account.zip']")
        country = (By.XPATH, "//input[@name='account.country']")
        lenguage_preference = (By.XPATH, "//select[@name='account.languagePreference']")
        favourite_category = (By.XPATH, "//select[@name='account.favouriteCategoryId']")
        enable_mylist = (By.XPATH, "//input[@name='account.listOption']")
        enable_mybanner = (By.XPATH, "//input[@name='account.bannerOption']")
        save_account = (By.XPATH, "//input[@name='newAccount']")

    def user_id(self) -> Element:
        return self.create_element(locator=self.locators.user_id)

    def new_password(self)-> Element:
        return self.create_element(locator=self.locators.new_password)
    
    def repeat_password(self) -> Element:
        return self.create_element(locator=self.locators.repeat_password) 
    
    def first_name(self) -> Element:
        return self.create_element(locator=self.locators.first_name) 
         
    def last_name(self) -> Element:
        return self.create_element(locator=self.locators.last_name) 
         
    def email(self) -> Element:
        return self.create_element(locator=self.locators.email)  
    
    def phone(self) -> Element:
        return self.create_element(locator=self.locators.phone)   

    def address1(self) -> Element:
        return self.create_element(locator=self.locators.address1)   
    
    def address2(self) -> Element:
        return self.create_element(locator=self.locators.address2)     
    
    def city(self) -> Element:
        return self.create_element(locator=self.locators.city)     
    
    def state(self) -> Element:
        return self.create_element(locator=self.locators.state)     
    
    def zip(self) -> Element:
        return self.create_element(locator=self.locators.zip)     

    def country(self) -> Element:
        return self.create_element(locator=self.locators.country)     

    def language_preference(self) -> Element: 
        return self.create_element(locator=self.locators.lenguage_preference)     

    def favourite_category(self) -> Element:
        return self.create_element(locator=self.locators.favourite_category)     

    def mylist(self) -> Element:
        return self.create_element(locator=self.locators.enable_mylist)

    def mybanner(self) -> Element:
        return self.create_element(locator=self.locators.enable_mybanner)     
    
    def save_account(self) -> Element:
        return self.create_element(locator=self.locators.save_account)     