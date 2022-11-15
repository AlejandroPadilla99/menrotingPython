from seleniumpagefactory import PageFactory

class AngelFishPage(PageFactory):
    def __init__(self, driver) -> None:
        self.driver = driver 
    
    locators = {
        'first_item': ("XPATH", "//a[contains(@class,'EST-1')]")
    }

    def click_first_item(self):
        self.first_item.click()
