#lib
from selenium.webdriver.common.by import By

#localA
from selenium_ui import driver
from selenium_ui.pages.element import Element

class PaymentDetailsPages():

    class locators():
        continue_button = (By.XPATH, "//input[@name='newOrder']")
        thank_you = (By.XPATH, "//li[contains(text(), 'Thank you, your order has been submitted.')]")
        first_name = (By.XPATH, "//input[@name='order.billToFirstName']")
        last_name = (By.XPATH, "//input[@name='order.billToLastName']")
        address1 = (By.XPATH, "//input[@name='order.billAddress1']")
        address2 = (By.XPATH, "//input[@name='order.billAddress2']")
        city = (By.XPATH, "//input[@name='order.billCity']")
        state = (By.XPATH, "//input[@name='order.billState']")
        zip = (By.XPATH, "//input[@name='order.billZip']")
        country = (By.XPATH,"//input[@name='order.billCountry']" )
        

    def continue_button(self) -> Element:
        return Element(driver=driver, locator=self.locators.continue_button)
    
    def thank_you(self) -> Element:
        return Element(driver=driver, locator=self.locators.thank_you)
    
    def first_name(self) -> Element:
        return Element(driver=driver, locator=self.locators.first_name)
    
    def last_name(self) -> Element:
        return Element(driver=driver, locator=self.locators.last_name)
    
    def address1(self) -> Element:
        return Element(driver=driver, locator=self.locators.address1)
    
    def address2(self) -> Element:
        return Element(driver=driver, locator=self.locators.address2)
    
    def city(self) -> Element:
        return Element(driver=driver, locator=self.locators.city)
    
    def state(self) -> Element:
        return Element(driver=driver, locator=self.locators.state)
    
    def zip(self) -> Element:
        return Element(driver=driver, locator=self.locators.zip)
    
    def country(self) -> Element:
        return Element(driver=driver, locator=self.locators.country)