

from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import ConfirmPage

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
    #driver.find_elements(By.XPATH, "//*[@class='card h-100']")
    products = (By.XPATH,"//h4[@class='card-title']")

    #product.find_element(By.XPATH, "div/button").click()
    product = (By.CSS_SELECTOR, ".btn.btn-info")

    #driver.find_element(By.XPATH, "//*[@class='nav-link btn btn-primary']")
    checkoutbtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    #driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
    checkoutbtn2 = (By.CSS_SELECTOR, ".btn.btn-success")

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