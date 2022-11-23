#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element

class SingUpPage():
    def __init__(self, driver):
        self.driver = driver

    class locators():
        username = (By.XPATH, "//input[@name='username']"),
        password = (By.XPATH, "//input[@name='password']"),
        login = (By.XPATH, "//input[@name='signon']"),
        register = (By.XPATH, "//a[contains(.,'Register Now!')]")


    def username(self) -> Element:
        return Element(self.driver, locator=self.locators.username)

    def password(self) -> Element:
        return Element(self.driver, locator=self.locators.password)
    
    def login(self) -> Element:
        return Element(self.driver, locator=self.locators.login)
    
    def register(self) -> Element:
        return Element(self.driver, locator=self.locators.register)
    