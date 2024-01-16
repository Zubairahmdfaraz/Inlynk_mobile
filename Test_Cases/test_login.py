import sys
import pytest
from appium import webdriver
from Pages.BasePage import BasePage
from Pages.LoginScreen import LoginScreen

project_root = r'f:\Inlynk_Appium'
sys.path.append(project_root)


class Test_Login(BasePage):
    username = "csk@yopmail.com"
    password = "Inlink@123"


    def test_login(self,appium_driver):
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin(self.username, self.password)
        self.lp.ClickLogin()





     