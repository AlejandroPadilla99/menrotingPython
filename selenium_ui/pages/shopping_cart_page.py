#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element

class ShoppingCartPage():
    def __init__(self, driver) -> None:
        self.driver = driver
    
    locators = {
        'quantity': (By.XPATH, "(//table//input)[1]"),
        'remove': (By.XPATH, "(//table//a)[2]"),
        'update_cart': (By.XPATH, "//input[@value='Update Cart']"),
        'checkout': (By.XPATH, "//a[text()='Proceed to Checkout']")
    }

    def quantity(self) -> Element:
        return Element(driver=self.driver, method=self.locators.get('quantity')[0], key=self.locators.get('quantity')[1])
        
    def quantity(self) -> Element:
        return Element(driver=self.driver, method=self.locators.get('remove')[0], key=self.locators.get('remove')[1])

    def quantity(self) -> Element:
        return Element(driver=self.driver, method=self.locators.get('update_cart')[0], key=self.locators.get('update_cart')[1])

    def quantity(self) -> Element:
        return Element(driver=self.driver, method=self.locators.get('checkout')[0], key=self.locators.get('checkout')[1])
    
    
