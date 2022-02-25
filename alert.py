import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,'//*[@id="OKTab"]/button').click()
time.sleep(3)

#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()



