
from selenium.common.exceptions import NoSuchElementException

class Element:
    #change for tuple
    def __init__(self, driver: object, locator: tuple) -> None:
        self.driver = driver
        self.element = self._find_element(locator)
    
    def click(self):
        self.element.click()

    def select_by_value(self, data: str) -> None:
        self.element.select_by_value(data)
    
    def send_keys(self, data: str) -> None:
        self.element.send_keys(data)
    
    def get_text(self) -> None:
        self.element.text
    
    def clean_text(self) -> None:
        self.element.clear()
    
    def element_exit(self) -> bool:
        if(self.element):
            return True
        else:
            return False
    
    def _find_element(self, locator: tuple) -> object:
        try: 
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None