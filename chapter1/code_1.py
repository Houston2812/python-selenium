from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
# opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
# browser = webdriver.Chrome("../drivers/chromedriver.exe");
# browser = webdriver.Firefox()
browser.get("http://www.seleniumhq.org")    