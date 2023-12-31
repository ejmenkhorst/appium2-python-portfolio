"""Module for running PyTest framework."""
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

APPIUM_PORT = 4723
APPIUM_HOST = "127.0.0.1"


@pytest.fixture(scope="session")
def appium_service():
    """Starting Appium Service before running tests."""
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=["--address", APPIUM_HOST, "-p", str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_ios_driver(custom_opts=None):
    """Create IOS driver."""
    options = XCUITestOptions()
    options.platformVersion = "13.4"
    options.udid = "123456789ABC"
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)


def create_android_driver(custom_opts=None):
    """Create Android driver."""
    options = UiAutomator2Options()
    options.platformVersion = "10"
    options.udid = "emulator-5554"
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)


@pytest.fixture
def ios_driver_factory():
    """ios_driver_factory"""
    return create_ios_driver


@pytest.fixture
def ios_driver():
    """return ios_driver to the function using it, quit driver afterwards."""
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_ios_driver()
    yield driver
    driver.quit()


@pytest.fixture
def android_driver_factory():
    """android_driver_factory"""
    return create_android_driver


@pytest.fixture
def android_driver():
    """return android_driver to the function using it, quit driver afterwards."""
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_android_driver()
    yield driver
    driver.quit()
