import time
import pytest
from dataclasses import dataclass, field

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

'''@pytest.fixture
def browser():

    # Initialize the ChromeDriver instance
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Make its calls wait up to 10 second for element to appear
    driver.implicitly_wait(time_to_wait=10)

    #return the WebDriver instance for the setup
    yield driver

    #Quit the WebDriver instance for the cleanup
    driver.quit()

'''
# Initialize the ChromeDriver instance
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Make its calls wait up to 10 second for element to appear
driver.implicitly_wait(time_to_wait=10)



#############################################
find_by_map = {
    "xpath": By.XPATH,
    "id": By.ID
}

def finder_element(key: str, by: str = "id") -> object:
    return driver.find_element(find_by_map[by], key)

@dataclass
class Action:
    label: str 
    func: str 
    params: dict

    def exec(self):
        self.element = self.func(key=self.params['key'], by=self.params['by'])
        if self.params['action']:
            if self.params['type'] == 'click':
                self._click()
            if self.params['type'] == 'send_keys':
                self._send_keys()
        return True
    
    def _click(self):
        self.element.click()
    
    def _send_keys(self):
        self.element.send_keys(self.params['value'])

    @staticmethod 
    def _kill_driver():
        driver.quit()

#Holds the factory
@dataclass
class Actions:
    factory: list = field(default_factory=list)

    def enroll(self, label, func, params):
        action = Action(label, func, params)
        self.factory.append(action)


#Define factory behavior
class Page:
    def __init__(self) -> None:
        driver.get('https://petstore.octoperf.com/')
        self.flows = Actions() # the set of the actions 


login = Page()

login.flows.enroll(
    'Find the enter the store button', finder_element, 
    {
        'by':'xpath',
        'key':'/html/body/div[1]/p[1]/a',
        'action':True,
        'type':'click'
    }
)
login.flows.enroll(
    'Click on sing in button', finder_element, 
    {
        'by':'xpath',
        'key':'/html/body/div[1]/div[2]/div/a[2]',
        'action':True,
        'type':'click'
    }
)
login.flows.enroll(
    'Fill the username textbox', finder_element,
    {
        'by':'id',
        'key':'stripes--94156071',
        'action':True,
        'type':'send_keys',
        'value': 'Alejandro'
    }
)


@pytest.mark.parametrize("flow", login.flows.factory)
def test_factory(flow):
    assert flow.exec() == True