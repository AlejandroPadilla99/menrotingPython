#lib
from selenium.webdriver.common.by import By

#localA
from selenium_ui import driver
from selenium_ui.pages.element import Element

class PaymentDetailsPages():

    class locators():
        continue_button = (By.XPATH, "//input[@name='newOrder']")
        thank_you = (By.XPATH, "//li[contains(text(), 'Thank you, your order has been submitted.')]")

    def continue_button(self) -> Element:
        return Element(driver=driver, locator=self.locators.continue_button)
    
    def thank_you(self) -> Element:
        return Element(driver=driver, locator=self.locators.thank_you)