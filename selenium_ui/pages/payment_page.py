#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver 
from selenium_ui.pages.element import Element

class ShoppingCartPage():

    class locators():
        continue_button = (By.XPATH, "(//table//input)[1]")
    
    def continue_button(self) -> Element:
        return Element(driver=driver, method=self.locators.continue_button)  
