#lib 
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
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
    #driver.quit()