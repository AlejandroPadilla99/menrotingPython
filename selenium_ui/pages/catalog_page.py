#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element

class CatalogPage():
   
    class locators():
        add_to_cart = (By.XPATH, "//a[text()='Add to Cart']")

    def add_to_cart(self) -> Element:
        return Element(driver=driver, locator=self.locators.add_to_cart)