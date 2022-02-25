import xlutils
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")

path= "D:\job prep\sqa\logininput.xlsx"

rows = xlutils.getRowCount(path, 'Sheet1')

for r in range(2,rows +1):
    username= xlutils.readData(path,'Sheet1', r,1)
    password = xlutils.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.NAME, "submit").click()

    if driver.h3 == "Login Successfully":
        print("test is passed")
        xlutils.writeData(path,"Sheet1", r, 3, "test is passed")
    else:
        print("test is failed")
        xlutils.writeData(path, "Sheet1", r, 3, "test is failed")


    driver.find_element(By.LINK_TEXT, "Home").click()





