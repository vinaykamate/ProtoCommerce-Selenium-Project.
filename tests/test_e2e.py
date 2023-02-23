from PageObject.HomePage import Homepage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        checkoutpage = homepage.ShopItems()
        log.info("getting all the product title")
        products = checkoutpage.getProducts()
        i = -1
        for product in products:
            i = i + 1
            productname = product.text
            log.info(productname)
            if productname == 'Blackberry':
                checkoutpage.getprouduct()[i].click()
        checkoutpage.CheckOutButton().click()
        confirmpage = checkoutpage.CheckOutButton2()
        log.info("Entering country name as ind")
        confirmpage.TextBox().send_keys("ind")
        self.VerifyLinkPresence("India")
        confirmpage.Select().click()
        confirmpage.CheckBox().click()
        confirmpage.SubmitButton().click()
        successtext = confirmpage.getsuccesstext().text
        log.info("text received from application is" + successtext)
        assert "Success! Thank you!" in successtext