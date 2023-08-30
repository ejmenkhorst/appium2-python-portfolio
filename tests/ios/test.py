"""driver to use locators."""
from appium.webdriver.common.appiumby import AppiumBy


def test_ios_click(ios_driver_factory):
    """Test if the mobile app can find the text on IOS app"""
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with ios_driver_factory(
        {"appium:app": "testapps/proverbial_ios.ipa"}  # /path/to/app/UICatalog.app.zip
    ) as driver:
        element = driver.find_element(
            by=AppiumBy.ID, value="com.lambdatest.proverbial:id/Textbox"
        )
        assert element.text == "Hello! Welcome to lambdatest Sample App called"
