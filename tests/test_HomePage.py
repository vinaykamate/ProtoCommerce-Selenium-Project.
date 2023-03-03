import time

import pytest
from PageObject.HomePage import Homepage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class TestAngularForm(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        log.info("firstname is " + getData["Name"])
        homepage.Formname().send_keys(getData["Name"])
        homepage.Formemail().send_keys(getData["Email"])
        homepage.Formpwd().send_keys(getData["Password"])
        homepage.Formcheckbox().click()
        self.Selectoption(homepage.Formdropdown(), getData["Gender"])
        homepage.Formradiobtn().click()
        homepage.Formdate().send_keys(getData["DOB"])
        homepage.Formsubmit().click()
        time.sleep(5)
        successtext = homepage.Formalerttext().text
        assert "Success! The Form has been submitted successfully!." in successtext
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("T3"))
    def getData(self, request):
        return request.param