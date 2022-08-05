from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://wiki.python.org/moin/FrontPage')

search = driver.find_element(By.ID, 'searchinput')
search.clear()
search.send_keys("Beginner")
search.send_keys(Keys.RETURN)
time.sleep(2)

select = Select(driver.find_element(By.XPATH, "//*/form/div/select"))
select.select_by_visible_text("Raw Text")

time.sleep(4)

driver.close()