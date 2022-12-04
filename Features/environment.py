from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave.fixture import use_fixture_by_tag
import sys
from helper.helper_web import get_browser

def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # # Reading the browser type from the configuration file for Selenium Python Tutorial
    # spec = importlib.util.spec_from_file_location("get_browser", "./helper/helper_web.py")
    # get_browser = importlib.util.module_from_spec(spec)
    # sys.modules["get_browser"] = get_browser
    # spec.loader.exec_module(get_browser)
    helper_func = get_browser(config.get('Environment', 'Browser'))
    print(context)
    context.HelperFunc = helper_func

    # Local Chrome WebDriver
    # if context.browser == "chrome":
    #   context.driver = webdriver.Chrome()


def after_all(context):
    context.HelperFunc.close()