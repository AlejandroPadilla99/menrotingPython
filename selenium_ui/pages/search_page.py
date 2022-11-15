from seleniumpagefactory import PageFactory

class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators = {
       'return_to_main': ("XPATH", "//a[contains(.,'Return to Main Menu')]")
    }

    def click_return_to_main(self):
        self.return_to_main.click()
