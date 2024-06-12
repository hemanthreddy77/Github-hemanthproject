from selenium import webdriver
from selenium.webdriver.common.by import (By)
class Loginpage:
    textbox_username = "#Email"
    textbox_password = "#Password"
    button_login = "//button[contains(text(),'Log in')]"
    logout_linktext = "//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver = driver
    def enter_username(self,username):
        # self.driver.find_element(By.CSS_SELECTOR, self.textbox_username).clear()
        usern = self.driver.find_element(By.CSS_SELECTOR, self.textbox_username)
        usern.clear()
        usern.send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).send_keys(password)
    def login_click(self):
        login_but = self.driver.find_element(By.XPATH, self.button_login)
        login_but.click()
    def logout_click(self):
        logout_but = self.driver.find_element(By.XPATH, self.logout_linktext)
        logout_but.click()

