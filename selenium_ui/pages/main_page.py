#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element

class MainPage():
    def __init__(self, driver):
        self.driver = driver
    
    locators = {
        'sing_in': (By.XPATH, "/html/body/div[1]/div[2]/div/a[2]"),
        'search_bar': (By.XPATH, "//input[@name='keyword']"),
        'search_button': (By.XPATH, "//input[@name='searchProducts']"),
        'fish_section': (By.XPATH, "//img[contains(@src,'fish_icon')]"),
        'dogs_section': (By.XPATH, "//img[contains(@src,'dogs_icon')]"),
        'cats_section': (By.XPATH, "//img[contains(@src,'cats_icon')]"),
        'firts_element_search': (By.XPATH, "(//tbody//td//a)[2]"),
        'add_cart': (By.XPATH, "(//table//tr//td)[5]")
    }

    #return Element(self.driver, method=self.locators.get('angelfish')[0], key=self.locators.get('angelfish')[1])

    def sing_in(self):
        return Element(self.driver, method=self.locators.get('sing_in')[0], key=self.locators.get('sing_in')[1])

    def search_bar(self):
        return Element(self.driver, method=self.locators.get('search_bar')[0], key=self.locators.get('search_bar')[1])

    def search_button(self):
        return Element(self.driver, method=self.locators.get('search_button')[0], key=self.locators.get('search_button')[1])
    
    def fish_section(self): 
        return Element(self.driver, method=self.locators.get('fish_section')[0], key=self.locators.get('fish_section')[1])
    
    def firts_element_search(self):
        return Element(self.driver, method=self.locators.get('firts_element_search')[0], key=self.locators.get('firts_element_search')[1])
    
    def add_cart(self):
        return Element(self.driver, method=self.locators.get('add_cart')[0], key=self.locators.get('add_cart')[1])
    
    def dogs_sections(self):
        return Element(self.driver, method=self.locators.get('dogs_section')[0], key=self.locators.get('dogs_section')[1])
    
    def cats_section(self): 
        return Element(self.driver, method=self.locators.get('cats_section')[0], key=self.locators.get('cats_section')[1])