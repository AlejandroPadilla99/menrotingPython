#lib
from selenium.webdriver.common.by import By
#local
from selenium_ui.pages.element import Element

class PaymentDetailsPages():

    class locators():
        order_submitted = (By.XPATH, "//li[text()='Thank you, your order has been submitted.']")
        total_cost = (By.XPATH, "")