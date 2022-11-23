
class Element:
    #change for tuple
    def __init__(self, driver: object, locator: tuple) -> None:
        self.driver = driver
        self.element = self._find_element(*locator)
    
    def click(self):
        self.element.click()

    def select_by_value(self, data: str) -> None:
        self.element.select_by_value(data)
    
    def send_keys(self, data: str) -> None:
        self.element.send_keys(data)
    
    def _find_element(self, locator: tuple) -> object:
        return self.driver.find_element(locator[0], locator[1])