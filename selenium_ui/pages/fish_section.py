from seleniumpagefactory import PageFactory

from selenium_ui.pages.element import Element
from selenium.webdriver.common.by import By

class FishPage(PageFactory):
    def __init__(self, driver) -> None:
        self.driver = driver


    locators = {
        'angelfish': (By.XPATH, "//a[contains(.,'FI-SW-01')]"),
        'tiger_shark': (By.XPATH, "//a[contains(.'FI-SW-02')]")
    }

    def angelfish(self):
        return Element(self.driver, method=self.locators.get('angelfish')[0], key=self.locators.get('angelfish')[1])
    
    def click_tiger_shark(self):
        self.tiger_shark.click()


print(By.XPATH) 