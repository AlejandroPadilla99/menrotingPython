#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element
from selenium_ui.pages.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
    
    class locators():
        add_to_cart = (By.XPATH, "//a[text()='Add to Cart']")

    def add_to_cart(self) -> Element:
        return self.create_element(locator=self.locators.add_to_cart)