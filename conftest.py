import os
import pytest
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser

load_dotenv()
user_name = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')


@pytest.fixture(scope='function', autouse=False)
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": user_name,
            "accessKey": password
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = 10

    yield

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": user_name,
            "accessKey": password
        }
    })

    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = 10

    yield

    browser.quit()
