#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.config_selenium import URL_SE

class Login:
    '''
        A class used to do login with the webdriver

        Attributes
        ----------
        browser: object
            the driver from selenium
    '''

    def __init__(self, browser: object) -> None:
        '''
        Parameters
        ----------
        browser: object
            The web browser in witch the test will be executed
        '''

        self.base_url = URL_SE
        self.browser = browser
        self.finder = self.browser.find_element

    def load_page(self) -> None:
        self.browser.get(url=self.base_url)
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/a[2]').click()
    
    def enter_data(self, username: str, password: str) -> None: 

        input_username = self.finder(By.NAME, 'username') 
        input_password = self.finder(By.NAME, 'password')
        login_button = self.finder(By.NAME, 'signon')

        input_username.send_keys(username)
        input_password.clear()
        input_password.send_keys(password)
        login_button.click()

    def get_result_login(self) -> str:
        '''return the welcome menssage from the web site

            Return
            ------
            str 
                a string with the welcome menssage 
        '''


        welcome_message = self.finder(By.ID, 'WelcomeContent')
        return welcome_message.text


