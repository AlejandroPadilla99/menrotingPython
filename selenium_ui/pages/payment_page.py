#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element

class ShoppingCartPage():
    def __init__(self, driver) -> None:
        self.driver = driver
    
    locators = {
        'continue': (By.XPATH, "(//table//input)[1]"), 
    }

    def continue_button(self) -> Element:
        return Element(driver=self.driver, method=self.locators.get('continue')[0], key=self.locators.get('continue')[1])  
