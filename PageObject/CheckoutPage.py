from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import ConfirmPage

class CheckOutPage:

    products = (By.XPATH,"//h4[@class='card-title']")
    product = (By.CSS_SELECTOR, ".btn.btn-info")
    checkoutbtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkoutbtn2 = (By.CSS_SELECTOR, ".btn.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getprouduct(self):
        return self.driver.find_elements(*CheckOutPage.product)

    def CheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutbtn)

    def CheckOutButton2(self):
        self.driver.find_element(*CheckOutPage.checkoutbtn2).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage