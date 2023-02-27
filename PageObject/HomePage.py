from selenium.webdriver.common.by import By
from PageObject.CheckoutPage import CheckOutPage


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CSS_SELECTOR, ".form-control.ng-untouched.ng-pristine.ng-invalid").send_keys("vinayak")
    name = (By.XPATH, "(//input[@name='name'])[1]")

    #driver.find_element(By.XPATH, "//input[@name='email']")
    email = (By.XPATH, "//input[@name='email']")

    #driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("vinay9000")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")

    #driver.find_element(By.XPATH, "//input[@type='checkbox']").
    checkbox = (By.XPATH, "//input[@type='checkbox']")

    # driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1")
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    #driver.find_element(By.ID, "inlineRadio1")
    radiobutton = (By.ID, "inlineRadio1")

    #driver.find_element(By.XPATH, "//input[@name='bday']")
    date = (By.XPATH, "//input[@name='bday']")

    #driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
    submitbutton = (By.CSS_SELECTOR, ".btn.btn-success")

    #driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    alerttext = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    shop = (By.XPATH, "//*[contains(@href,'shop')]")

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
