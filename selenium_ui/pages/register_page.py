#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui.pages.element import Element

class RegisterPage():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'user_id': (By.XPATH, "//input[@name='username']"),
        'new_password' :(By.XPATH, "//input[@name='password']"),
        'repeat_password': (By.XPATH, "//input[@name='repeatedPassword']"),
        'first_name': (By.XPATH, "//input[@name='account.firstName']"),
        'last_name': (By.XPATH, "//input[@name='account.lastName']"),
        'email': (By.XPATH, "//input[@name='account.email']"),
        'phone': (By.XPATH, "//input[@name='account.phone']"),
        'address1': (By.XPATH, "//input[@name='account.address1']"),
        'address2': (By.XPATH, "//input[@name='account.address2']"),
        'city': (By.XPATH, "//input[@name='account.city']"),
        'state': (By.XPATH, "//input[@name='account.state']"),
        'zip': (By.XPATH, "//input[@name='account.zip']"),
        'country': (By.XPATH, "//input[@name='account.country']"),
        'lenguage_preference': (By.XPATH, "//select[@name='account.languagePreference']"),
        'favourite_category': (By.XPATH, "//select[@name='account.favouriteCategoryId']"),
        'enable_mylist': (By.XPATH, "//input[@name='account.listOption']"),
        'enable_mybanner': (By.XPATH, "//input[@name='account.bannerOption']"),
        'save_account': (By.XPATH, "//input[@name='newAccount']")
    }

    def user_id(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('user_id')[0], key=self.locators.get('user_id')[1])

    def new_password(self)-> None:
        return Element(driver=self.driver, method=self.locators.get('new_password')[0], key=self.locators.get('new_password')[1])
    
    def repeat_password(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('repeat_password')[0], key=self.locators.get('repeat_password')[1]) 
    
    def first_name(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('first_name')[0], key=self.locators.get('first_name')[1]) 
         
    def last_name(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('last_name')[0], key=self.locators.get('last_name')[1]) 
         
    def email(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('email')[0], key=self.locators.get('email')[1])  
    
    def phone(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('phone')[0], key=self.locators.get('phone')[1])   

    def address1(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('address1')[0], key=self.locators.get('address1')[1])   
    
    def address2(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('address2')[0], key=self.locators.get('address2')[1])     
    
    def city(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('city')[0], key=self.locators.get('city')[1])     
    
    def state(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('state')[0], key=self.locators.get('state')[1])     
    
    def zip(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('zip')[0], key=self.locators.get('zip')[1])     

    def country(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('country')[0], key=self.locators.get('country')[1])     

    def language_preference(self) -> None: 
        return Element(driver=self.driver, method=self.locators.get('lenguage_preference')[0], key=self.locators.get('lenguage_preference')[1])     

    def favourite_category(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('favorite_category')[0], key=self.locators.get('favorite_category')[1])     

    def mylist(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('enable_mylist')[0], key=self.locators.get('enable_mylist')[1])

    def mybanner(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('enable_mybanner')[0], key=self.locators.get('enable_mybanner')[1])     
    
    def save_account(self) -> None:
        return Element(driver=self.driver, method=self.locators.get('save_account')[0], key=self.locators.get('save_account')[1])     