#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element

class SingUpPage():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'username': (By.XPATH, "//input[@name='username']"),
        'password': (By.XPATH, "//input[@name='password']"),
        'login': (By.XPATH, "//input[@name='signon']"),
        'register': (By.XPATH, "//a[contains(.,'Register Now!')]")
    }


    def username(self) -> Element:
        return Element(self.driver, method=self.locators.get('username')[0], key=self.locators.get('username')[1])

    def password(self) -> Element:
        return Element(self.driver, method=self.locators.get('password')[0], key=self.locators.get('password')[1])
    
    def login(self) -> Element:
        return Element(self.driver, method=self.locators.get('login')[0], key=self.locators.get('login')[1])
    
    def register(self) -> Element:
        return Element(self.driver, method=self.locators.get('register')[0], key=self.locators.get('register')[1])
    