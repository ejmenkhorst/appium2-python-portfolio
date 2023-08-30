"""driver to use locators"""
from appium.webdriver.common.appiumby import AppiumBy


def test_android_click(android_driver_factory):
    """Test if the mobile app can find the text on the Android app"""
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with android_driver_factory(
        {
            # "appium:app": "/Users/erikmenkhorst/Documents/GitHub/appium2-python-portfolio/testapps/proverbial_android.apk",
            "appium:app": "C:\\Users\\emenkhorst\\Desktop\\Local repo\\appium2-python-portfolio\\testapps\\proverbial_android.apk",
            "appium:udid": "emulator-5554",
        }
    ) as driver:
        element = driver.find_element(
            by=AppiumBy.ID, value="com.lambdatest.proverbial:id/Textbox"
        )
        assert (
            element.text == "Hello! Welcome to lambdatest Sample App called Proverbial"
        )
