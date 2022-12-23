#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element

class OderPage:

    class locators:
        confirm = (By.XPATH, "//a[text()='Confirm']")

    def confirm(self) -> Element:
        return Element(driver=driver, locator=self.locators.confirm)