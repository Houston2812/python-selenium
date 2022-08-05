from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get("https://selenium.dev")

time.sleep(2)
driver.close()