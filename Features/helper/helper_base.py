from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class HelperFunc(object):
    __TIMEOUT = 30

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)


    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    # Helper functions that are used to identify the web locators in Selenium Python tutorial
    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def wait_until(self):
        return self._driver_wait.until(EC.alert_is_present())

    def switch_to(self):
        return self._driver.switch_to.alert

    def execute_script(self, statement, id2):
        return self._driver.execute_script(statement, self.find_by_id(id2))

    def set_window_size(self, width, height):
        return self._driver.set_window_size(width, height)

    def current_url(self):
        return self._driver.current_url

    
    def set_window_size(self):
        return self._driver.set_window_size(1536,714)



