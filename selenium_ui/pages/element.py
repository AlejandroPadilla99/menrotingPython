#lib
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

class Element:
    def __init__(self, driver: object, locator: tuple) -> None:
        self.driver = driver
        self.locator = locator
    
    def click(self) -> None:
        self._find_element().click()

    def select_by_value(self, data: str) -> None:
        Select(self._find_element()).select_by_value(data)
    
    def send_keys(self, data: str) -> None:
        self._find_element().clear()
        self._find_element().send_keys(data)

    def get_attribute(self, name: str) -> str:
        return self._find_element().get_attribute(name=name)
    
    def get_text(self) -> None:
        return self._find_element().text
    
    def clean_text(self) -> None:
        self._find_element().clear()
    
    def element_exit(self, time: int) -> None:
        self._find_element(implicitly_wait=time)
        return True
     
    def _find_element(self, implicitly_wait: int = 3) -> object:
        try: 
            return self.driver.find_element(*self.locator)
        except NoSuchElementException:
            return None