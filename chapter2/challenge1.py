from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://www.seleniumhq.org")

element_q_id = driver.find_element(By.ID, "selenium_logo")
print(f"My element_q (id) is: \n {element_q_id}")

# element_q_name = driver.find_element(By.NAME, "Selenium IDE")
# print(f"My element_q (name) is: \n {element_q_name}")

element_class = driver.find_element(By.CLASS_NAME, "selenium-button")
print(f"My search by class element (class name) is: \n {element_class}")

driver.close()