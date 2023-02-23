import pytest
from PageObject.HomePage import Homepage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class TestAngularForm(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        log.info("firstname is " + getData["name"])
        homepage.Formname().send_keys(getData["name"])
        homepage.Formemail().send_keys(getData["email"])
        homepage.Formpwd().send_keys(getData["password"])
        homepage.Formcheckbox().click()
        self.Selectoption(homepage.Formdropdown(), getData["gender"])
        homepage.Formradiobtn().click()
        homepage.Formdate().send_keys(getData["DOB"])
        homepage.Formsubmit().click()
        successtext = homepage.Formalerttext().text
        assert "Success! The Form has been submitted successfully!." in successtext
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param

