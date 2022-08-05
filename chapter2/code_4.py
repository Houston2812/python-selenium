from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("file:///C:/Users/husey/Documents/Projects/LinkedIn-Automation-Course/chapter2/html_code_02.html")
heading_content = driver.find_element(By.CLASS_NAME, "content")
print(f"My heading content (class) is: \n {heading_content}")

driver.close()