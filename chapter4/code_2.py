from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("http://www.python.org")
myDynamicElement = driver.find_element(By.ID, "start-shell")

driver.close()