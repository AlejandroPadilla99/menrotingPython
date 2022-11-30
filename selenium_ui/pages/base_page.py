from selenium_ui import driver

class BasePage():

    def __init__(self) -> None:
        pass
    
    def return_to_base__page(self) -> None:
        driver.get('https://petstore.octoperf.com/actions/Account.action?signonForm=')