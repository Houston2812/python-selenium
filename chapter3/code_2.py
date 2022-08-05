from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('file:///C:/Users/husey/Documents/Projects/LinkedIn-Automation-Course/chapter3/html_code_03.html')

select = Select(driver.find_element(By.NAME, "numReturnSelect"))

select.select_by_index(4)
time.sleep(2)

select.select_by_visible_text("200")
time.sleep(2)

select.select_by_value("250")
time.sleep(2)

options = select.options
print(f"All options: {options}")

submit_button = driver.find_element(By.NAME, "continue")
submit_button.submit()

time.sleep(2)

driver.close()