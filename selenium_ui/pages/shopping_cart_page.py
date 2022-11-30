#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui import driver
from selenium_ui.pages.element import Element

class ShoppingCartPage():
   
    class locators():
        quantity = (By.XPATH, "(//table//input)[1]")
        remove = (By.XPATH, "(//table//a)[2]")
        update_cart = (By.XPATH, "//input[@value='Update Cart']")
        checkout = (By.XPATH, "//a[text()='Proceed to Checkout']")

    def quantity(self) -> Element:
        return Element(driver=driver, locator=self.locators.quantity)
        
    def remove(self) -> Element:
        return Element(driver=driver, locator=self.locators.remove)

    def update_cart(self):
        return Element(driver=driver, locator=self.locators.update_cart)

    def checkout(self) -> Element:
        return Element(driver=driver, locator=self.locators.checkout)
    
    
