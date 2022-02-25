from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title)

driver.get("https://www.daraz.com.bd/")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)