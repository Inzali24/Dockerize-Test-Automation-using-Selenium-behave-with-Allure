from selenium import webdriver
from  helper.helper_base import HelperFunc

def get_browser(browser):
    if browser == "chrome":
        op = webdriver.ChromeOptions()
        # add option
        op.add_argument('--headless')
        op.add_argument('--no-sandbox')
        op.add_argument("--disable-setuid-sandbox") 
        op.add_argument('--use-fake-ui-for-media-stream')
        op.add_argument('window-size=780,480')        
        chrome_path = r"/usr/local/bin/chromedriver"
        return HelperFunc(webdriver.Chrome(chrome_path, chrome_options=op))
