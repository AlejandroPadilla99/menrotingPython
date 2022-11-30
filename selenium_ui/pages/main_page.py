#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui import driver
from selenium_ui.pages.base_page import BasePage
from selenium_ui.pages.element import Element



class MainPage(BasePage):
    def __init__(self):
        super().__init__()

    class locators():
        
        sing_in = (By.XPATH, "/html/body/div[1]/div[2]/div/a[2]")
        search_bar =  (By.XPATH, "//input[@name='keyword']")
        search_button = (By.XPATH, "//input[@name='searchProducts']")
        fish_section = (By.XPATH, "//img[contains(@src,'fish_icon')]")
        dogs_section = (By.XPATH, "//img[contains(@src,'dogs_icon')]")
        cats_section = (By.XPATH, "//img[contains(@src,'cats_icon')]")
        firts_element_search = (By.XPATH, "(//tbody//td//a)[2]")
        add_cart = (By.XPATH, "(//table//tr//td)[5]")

    def sing_in(self):
        return Element(driver, locator=self.locators.sing_in)

    def search_bar(self):
        return Element(driver, locator=self.locators.search_bar)

    def search_button(self):
        return Element(driver, locator=self.locators.search_button)
    
    def fish_section(self): 
        return Element(driver, locator=self.locators.fish_section)
    
    def firts_element_search(self):
        return Element(driver, locator=self.locators.firts_element_search)
    
    def add_cart(self):
        return Element(driver, locator=self.locators.add_cart)
    
    def dogs_sections(self):
        return Element(driver, locator=self.locators.dogs_section)
    
    def cats_section(self): 
        return Element(driver, locator=self.locators.cats_section)