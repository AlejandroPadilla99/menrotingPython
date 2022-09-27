#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.config_selenium import URL_SE

class BuyFish:
    def __init__(self, browser: object) -> None:
        self.base_url = URL_SE
        self.browser = browser
        self.finder = self.browser.find_element
        self.base_xpath = '/html/body/'

    def select_fish_store(self) -> None:

        #find the elements
        button_fish_store = self.finder(By.XPATH, self.base_xpath+'div[2]/div[2]/div[1]/div/a[1]/img')
        
        #do the actions
        button_fish_store.click()
    
    def select_fish(self):

        #find the element
        button_fish = self.finder(By.XPATH, self.base_xpath+'div[2]/div[2]/table/tbody/tr[2]/td[1]/a')

        #do the actions
        button_fish.click()

    def select_specie_fish(self) -> None:

        #find the element
        button_specie_fish = self.finder(By.XPATH, self.base_xpath+'div[2]/div[2]/table/tbody/tr[2]/td[5]/a')

        #do the actions
        button_specie_fish.click()

    def select_checkout_button(self) -> None:

        #find the element
        button_checkout = self.finder(By.XPATH, self.base_xpath+'div[2]/div[2]/div[1]/a')

        #do the actions
        button_checkout.click()
    
    def select_continue_button(self) -> None:

        #find the element
        button_continue = self.finder(By.XPATH, self.base_xpath+'div[2]/div/form/input')

        #do the actions
        button_continue.click()
    
    def select_confirm_button(self) -> None:

        #find the element
        buttton_confirm = self.finder(By.XPATH, self.base_xpath+'div[2]/div[2]/a')

        #do the actions
        buttton_confirm.click()

