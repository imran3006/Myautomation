import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.daraz.com.bd/")

admin= driver.find_element(By.XPATH, "//*[@id='Level_1_Category_No1']/a/span")
usermngmt= driver.find_element(By.XPATH, "//*[@id='J_3442298940']/div/ul/ul[1]/li[1]/a/span")
users= driver.find_element(By.XPATH, "//*[@id='J_3442298940']/div/ul/ul[1]/li[1]/ul/li[1]/a/span")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermngmt).move_to_element(users).click().perform()
