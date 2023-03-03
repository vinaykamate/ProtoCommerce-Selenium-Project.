from selenium.webdriver.common.by import By

class ConfirmPage:

    textbox = (By.ID, "country")
    SelectIndia = (By.LINK_TEXT, "India")
    selectCheckbox = (By.CSS_SELECTOR, ".checkbox-primary")
    Submitbtn = (By.XPATH, "//input[@type='submit']")
    alertetxt = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def __init__(self, driver):
        self.driver = driver

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


