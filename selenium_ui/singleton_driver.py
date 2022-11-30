from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager





class SingletonDriver:
    def __init__(self) -> None:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(time_to_wait=10)


