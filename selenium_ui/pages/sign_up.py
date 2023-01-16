#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element
from selenium_ui.pages.base_page import BasePage

class SingUpPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

    class locators():
        username = (By.XPATH, "//input[@name='username']")
        password = (By.XPATH, "//input[@name='password']")
        login = (By.XPATH, "//input[@name='signon']")
        register = (By.XPATH, "//a[contains(.,'Register Now!')]")

    def username(self) -> Element:
        return self.create_element(locator=self.locators.username)

    def password(self) -> Element:
        return self.create_element(locator=self.locators.password)
    
    def login(self) -> Element:
        return self.create_element(locator=self.locators.login)
    
    def register(self) -> Element:
        return self.create_element(locator=self.locators.register)
    