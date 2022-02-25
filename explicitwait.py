import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.daraz.com.bd/")
time.sleep(3)

#driver.find_element(By.CSS_SELECTOR, "class = btn btn-primary").click()
A=driver.find_element(By.XPATH, "//*[@id='anonLogin']/a")
A.click()
b= driver.find_element(By.CSS_SELECTOR, "input[type=text]")
b.send_keys('emran.emu.sk@gmail.com')
c = driver.find_element(By.CSS_SELECTOR, "input[type=password]")
c.send_keys('IMRAN3006')
time.sleep(3)
B=driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/button")
B.click()

#explicit waits
wait = WebDriverWait(driver, 10)  #creating object
element = wait.until(EC.element_to_be_clickable([By.XPATH, "//*[@id='Level_1_Category_No1']/a/span"]))

element.click()
time.sleep(3)
driver.quit()