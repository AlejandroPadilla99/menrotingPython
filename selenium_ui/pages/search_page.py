#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element
from selenium_ui.pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
   
    class locators:
       return_to_main =  (By.XPATH, "//a[contains(.,'Return to Main Menu')]")
       item = (By.XPATH, "(//a[contains(@href, 'K9-BD-01')])[2]")
    
    def return_to_main(self) -> Element:
        return self.create_element(locator=self.locators.return_to_main)

    def item(self) -> Element:
        return self.create_element(locator=self.locators.item)
