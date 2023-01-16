#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element
from selenium_ui.pages.base_page import BasePage

class OderPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

    class locators:
        confirm = (By.XPATH, "//a[text()='Confirm']")

    def confirm(self) -> Element:
        return self.create_element(locator=self.locators.confirm)