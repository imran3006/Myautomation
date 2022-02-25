import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

time.sleep(2)
#scroll down page by pixel
driver.execute_script("window.scrollBy(0,1000)", "")

#scroll down by elements
flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[16]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll down til end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")