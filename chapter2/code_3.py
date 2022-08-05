from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("file:///C:/Users/husey/Documents/Projects/LinkedIn-Automation-Course/chapter2/html_code_02.html")

login_form_absolute = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form_relative = driver.find_element(By.XPATH, "//form[1]")
login_form_id = driver.find_element(By.XPATH, "//form[@id='loginForm']")

print(f"My login form element is: \n {login_form_absolute}")
print(f"My login form element is: \n {login_form_relative}")
print(f"My login form element is: \n {login_form_id}")

driver.close()