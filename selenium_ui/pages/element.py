#lib
import inspect
import logging
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
    
    def send_keys(self, data: str, clear: bool = False) -> None:
        if(clear):
            self._find_element().clear()
        self._find_element().send_keys(data)

    def get_attribute(self, name: str) -> str:
        return self._find_element().get_attribute(name=name)

    def get_value(self)  -> str:
        return self._find_element().get_attribute(name='value')
    
    def get_text(self) -> None:
        return self._find_element().text
    
    def clean_text(self) -> None:
        self._find_element().clear()
    
    def element_exit(self) -> None:
        self._find_element(implicitly_wait=3)
        return True
     
    def _find_element(self, implicitly_wait: int = 3) -> object:
        self._logging_stack()
        try: 
            return self.driver.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def _logging_stack(self, limit=None, start=0) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        stack = inspect.stack()

        here = stack[3]

        
        logger.info('------------------------------------------------------------------------')
        #for i in here:
        frame, filename, lineno, function, code_context, index = here
        
        data = code_context[0].split('.')
        logger.info("Page = "+ data[0])
        logger.info("Element = "+ data[1])
        logger.info("Action = "  + data[2])
        
        #frame, filename, lineno, function, code_context, index = here
        logger.info('------------------------------------------------------------------------') 