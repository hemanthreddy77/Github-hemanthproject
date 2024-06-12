import pytest

from selenium import webdriver
from page_objects.loginpage import Loginpage
from Utilities.read_properties import read_config as input_data
from Utilities.custom_logger import LogGen

class Test_login_001():
    admin_pageurl = input_data.get_baseurl()
    username = input_data.get_user_email()
    password = input_data.get_user_password()
    # invalid_username = 'admininvalid@yourstore.com'
# This is a girlkjdwlskjclkjdljljdsllkklkjlkjlkjl
    logger = LogGen.loggen()

    def test_title_verification(self,setup):
        self.driver = setup
        self.logger.info("******************************")
        self.driver.get(self.admin_pageurl)
        self.logger.info("********* page loaded ******")
        act_title = self.driver.title
        expec_title = "Your store. Login"
        if act_title==expec_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_title_verification.png")
            self.driver.close()
            assert False
        self.logger.info("** Test cse successfull")
    def test_successfull_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_pageurl)
        self.lp = Loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.login_click()
        expec_title = "Dashboard / nopCommerce administration"
        act_title = self.driver.title
        if act_title == expec_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False





