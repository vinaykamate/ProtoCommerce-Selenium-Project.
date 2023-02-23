from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_element(By.ID, "country").send_keys("ind")
    textbox = (By.ID, "country")

    #driver.find_element(By.LINK_TEXT, "India").click()
    SelectIndia = (By.LINK_TEXT, "India")

    #driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()
    selectCheckbox = (By.CSS_SELECTOR, ".checkbox-primary")

    #driver.find_element(By.XPATH, "//input[@type='submit']").click()
    Submitbtn = (By.XPATH, "//input[@type='submit']")

    #driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    alertetxt = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def TextBox(self):
        return self.driver.find_element(*ConfirmPage.textbox)

    def Select(self):
        return self.driver.find_element(*ConfirmPage.SelectIndia)

    def CheckBox(self):
        return self.driver.find_element(*ConfirmPage.selectCheckbox)

    def SubmitButton(self):
        return self.driver.find_element(*ConfirmPage.Submitbtn)

    def getsuccesstext(self):
        return self.driver.find_element(*ConfirmPage.alertetxt)


