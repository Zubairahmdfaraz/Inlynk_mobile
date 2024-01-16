from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

class BasePage:
    @pytest.fixture
    def appium_driver(self):
        desired_caps = dict(
            deviceName="emulator-5554",
            platformName="Android",
            PlatformVersion="13",
            app="F:\\Inlink_29_12_23_test.apk",
            automationName="UiAutomator2",
            appWaitForLaunch="false",
            #noReset="false",
            fullReset="",
            autoGrantPermissions="true"
        )
        Capabilities_Options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', options=Capabilities_Options)
        # request.cls.driver = driver
        driver.implicitly_wait(20)
        driver.find_element(AppiumBy.ID,'com.peoplelink.inlink:id/skipBtn').click()
        driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/checkBox').click()
        ele = driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/continueBtn')
        ele.click()
        yield driver

        # driver.quit()
        