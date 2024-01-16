
from appium.webdriver.common.appiumby import AppiumBy


class LoginScreen:
    def __init__(self,driver):
        self.driver = driver
        self.textbox_username = "com.peoplelink.inlink:id/emailET"
        self.textbox_password = "com.peoplelink.inlink:id/passwordET"
        self.button_login_id = "com.peoplelink.inlink:id/loginBtn"


    def ValidLogin(self, username, password):
        self.driver.find_element(AppiumBy.ID, self.textbox_username).send_keys(username)
        self.driver.find_element(AppiumBy.ID, self.textbox_password).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(AppiumBy.ID, self.button_login_id).click()