#lib
from selenium.webdriver.common.by import By

#local
from selenium_ui import driver
from selenium_ui.pages.element import Element

class MainPage:
   
    class locators:
        
        sign_in = (By.XPATH, "/html/body/div[1]/div[2]/div/a[2]")
        sign_out = (By.XPATH, "//a[text()='Sign Out']")
        my_account = (By.XPATH, "//a[text()='My Account']")
        main_picture = (By.XPATH, "//map[@name='estoremap']")
        search_bar =  (By.XPATH, "//input[@name='keyword']")
        welcome = (By.ID, "WelcomeContent")
        search_button = (By.XPATH, "//input[@name='searchProducts']")
        fish_section = (By.XPATH, "//img[contains(@src,'fish_icon')]")
        dogs_section = (By.XPATH, "//img[contains(@src,'dogs_icon')]")
        cats_section = (By.XPATH, "//img[contains(@src,'cats_icon')]")
        firts_element_search = (By.XPATH, "(//tbody//td//a)[2]")
        add_cart = (By.XPATH, "(//table//tr//td)[5]")


    def sign_in(self) -> Element:
        return Element(driver=driver, locator=self.locators.sign_in)

    def sign_out(self) -> Element:
        return Element(driver=driver, locator=self.locators.sign_out)

    def my_account(self) -> Element:
        return Element(driver=driver, locator=self.locators.my_account)

    def main_picture(self) -> Element:
        return Element(driver=driver, locator=self.locators.main_picture)

    def search_bar(self) -> Element:
        return Element(driver=driver, locator=self.locators.search_bar)

    def welcome(self) -> Element:
        return Element(driver=driver, locator=self.locators.welcome)
    
    def search_button(self) -> Element:
        return Element(driver=driver, locator=self.locators.search_button)
    
    def fish_section(self) -> Element: 
        return Element(driver=driver, locator=self.locators.fish_section)
    
    def firts_element_search(self) -> Element:
        return Element(driver=driver, locator=self.locators.firts_element_search)
    
    def add_cart(self) -> Element:
        return Element(driver=driver, locator=self.locators.add_cart)
    
    def dogs_sections(self) -> Element:
        return Element(driver=driver, locator=self.locators.dogs_section)
    
    def cats_section(self) -> Element: 
        return Element(driver=driver, locator=self.locators.cats_section)