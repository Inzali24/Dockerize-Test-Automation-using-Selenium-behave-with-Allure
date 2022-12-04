from selenium.webdriver.support.wait import WebDriverWait
from helper.helper_base import HelperFunc


def __init__(self, driver):
    super(HelperFunc, self).__init__()
    self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
    self._driver = driver


def open(self, url):
    self._driver.get(url)