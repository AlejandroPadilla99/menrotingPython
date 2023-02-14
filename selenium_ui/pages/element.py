#lib
import inspect
import logging
import traceback
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from conftest import logger

class Element:
    def __init__(self, driver: object, locator: tuple) -> None:
        stack_status = inspect.stack()
        trace = traceback.extract_stack()
        self._logging_stack(stack=stack_status, locator=locator, trace=trace)
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
        try: 
            return self.driver.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def _logging_stack(self, stack, locator, trace) -> None:

        
        for i in stack:
            frame, filename, lineno, function, code_context, index = i
            if "selenium_tests" in filename:
                data = code_context[0]
                data = data.split('.')
                if not "assert_that" in data[0]:
                    logger.info("\n\tPage: " + data[0]+ "\n\tElement: "+ data [1] +  "\n\tAction: " + data[2])