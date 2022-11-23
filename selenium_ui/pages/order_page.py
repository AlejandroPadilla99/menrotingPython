#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element


class OderPage():
    def __init__(self, driver: object) -> None:
        self.driver = driver

    class locators():
        confirm = (By.XPATH, "//a[text()='Confirm']")

    def confirm(self) -> Element:
        return Element(driver=self.driver, locator=self.locators.confirm)