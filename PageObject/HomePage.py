from selenium.webdriver.common.by import By
from PageObject.CheckoutPage import CheckOutPage

class Homepage:

    name = (By.XPATH, "(//input[@name='name'])[1]")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    radiobutton = (By.ID, "inlineRadio1")
    date = (By.XPATH, "//input[@name='bday']")
    submitbutton = (By.CSS_SELECTOR, ".btn.btn-success")
    alerttext = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    shop = (By.XPATH, "//*[contains(@href,'shop')]")

    def __init__(self, driver):
        self.driver = driver

    def Formname(self):
        return self.driver.find_element(*Homepage.name)

    def Formemail(self):
        return self.driver.find_element(*Homepage.email)

    def Formpwd(self):
        return self.driver.find_element(*Homepage.password)

    def Formcheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def Formdropdown(self):
        return self.driver.find_element(*Homepage.dropdown)

    def Formradiobtn(self):
        return self.driver.find_element(*Homepage.radiobutton)

    def Formdate(self):
        return self.driver.find_element(*Homepage.date)

    def Formsubmit(self):
        return self.driver.find_element(*Homepage.submitbutton)

    def Formalerttext(self):
        return self.driver.find_element(*Homepage.alerttext)

    def ShopItems(self):
       self.driver.find_element(*Homepage.shop).click()
       checkoutpage = CheckOutPage(self.driver)
       return checkoutpage
