from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_ios_search_wiki_Appium(mobile_management_ios):
    with step('I do not know'):
        # Test case for the BrowserStack sample iOS app.
        # If you have uploaded your app, update the test case here.
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("hello@browserstack.com" + "\n")
        text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(be.clickable)
        text_output.should(have.text("hello@browserstack.com"))
