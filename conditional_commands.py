import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
#----------- checking the username and pass field-----------
a=driver.find_element(By.NAME,"userName")
print(a.is_displayed())
print(a.is_enabled())
a.send_keys("abc")
b=driver.find_element(By.NAME,"password")
print(b.is_displayed())
print(b.is_enabled())
b.send_keys("abc")
time.sleep(4)


driver.find_element(By.NAME,"submit").click()



