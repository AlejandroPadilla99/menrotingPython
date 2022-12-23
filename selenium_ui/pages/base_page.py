#local
from selenium_ui import driver

class BasePage():

    def return_to_base_page(self) -> None:
        driver.get('https://petstore.octoperf.com/actions/Account.action?signonForm=')