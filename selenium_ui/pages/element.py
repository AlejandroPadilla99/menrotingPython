
class Element:
    def __init__(self, driver: object, method: str, key: str) -> None:
        self.driver = driver
        self.element = self._find_element(method=method, key=key)
    
    def click(self):
        self.element.click()

    def select_by_value(self, data: str) -> None:
        self.element.select_by_value(data)
    
    def send_keys(self, data: str) -> None:
        self.element.send_keys(data)
    
    def _find_element(self, method: str, key: str) -> object:
        return self.driver.find_element(method, key)