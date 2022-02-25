import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")

fff= driver.find_elements(By.TAG_NAME,'a')
print("num of links present: ", len(fff))

for link in fff:
    print(link.text)

# clicking on the link
driver.find_element(By.LINK_TEXT,'Agile Project').click()
