from appium.webdriver.common.appiumby import AppiumBy


def test_android_click(appium_service, android_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with android_driver_factory({
        # 'appium:app': '/Users/erikmenkhorst/Documents/GitHub/appium2-python-portfolio/testapps/proverbial_android.apk',
        'appium:app': 'C:\\Users\\emenkhorst\\Desktop\\Local repo\\appium2-python-portfolio\\testapps\\proverbial_android.apk',
        'appium:udid': 'emulator-5554',
    }) as driver:
        el = driver.find_element(by=AppiumBy.ID, value='com.lambdatest.proverbial:id/Textbox')
        assert el.text == "Hello! Welcome to lambdatest Sample App called Proverbial"
