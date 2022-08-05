from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("file:///C:/Users/husey/Documents/Projects/LinkedIn-Automation-Course/chapter2/html_code_02.html")
username_element = driver.find_element(By.NAME, "username")
print(f"My username element is: \n {username_element}")

driver.close()