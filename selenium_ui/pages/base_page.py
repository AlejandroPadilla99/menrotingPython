#local
from selenium_ui import driver
from selenium_ui.pages.element import Element

class BasePage():

    def return_to_base_page(self) -> None:
        driver.get('https://petstore.octoperf.com/actions/Account.action?signonForm=')
    
    def logout_session(self) -> None:
        driver.get('https://petstore.octoperf.com/actions/Account.action?signoff=')
    
    def create_element(self, locator: tuple) -> Element:
        return Element(driver=driver, locator=locator) 
