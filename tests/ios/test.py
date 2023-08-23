from appium.webdriver.common.appiumby import AppiumBy


def test_ios_click(appium_service, ios_driver_factory):
	# Usage of the context manager ensures the driver session is closed properly
	# after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
	with ios_driver_factory({
		'appium:app': 'testapps/proverbial_ios.ipa'  # /path/to/app/UICatalog.app.zip
	}) as driver:
		el = driver.find_element(by=AppiumBy.ID, value='com.lambdatest.proverbial:id/Textbox')
		assert el.text == "Hello! Welcome to lambdatest Sample App called Proverbial"
