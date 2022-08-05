from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("file:///C:/Users/husey/Documents/Projects/LinkedIn-Automation-Course/chapter2/html_code_02.html")
login_form = driver.find_element(By.ID, "loginForm")
print(f"My login form element is: \n {login_form}")

driver.close()