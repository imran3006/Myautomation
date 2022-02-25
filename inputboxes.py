import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

#---- no of input boxes -----------
inputboxes = driver.find_elements(By.CLASS_NAME,'mr-sm-2 form-control')
print(len(inputboxes))

#status checking----------

#status= driver.find_element(By.ID, "firstName").is_displayed()
#print(status)
#status= driver.find_element(By.ID, "firstName").is_enabled()
#print(status)



driver.find_element(By.ID, "firstName").send_keys('Imran')
time.sleep(2)
driver.find_element(By.ID, "lastName").send_keys('Sarker')
time.sleep(2)

driver.find_element(By.ID, "userEmail").send_keys('abc@gmail.com')
time.sleep(2)

#------- radio button
status= driver.find_element(By.ID, "gender-radio-1").is_selected()
print(status)
driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label").click()
time.sleep(2)
status= driver.find_element(By.ID, "gender-radio-1").is_selected()
print(status)

#---- checkbox-----
#driver.find_element(By.ID, "hobbies-checkbox-1").click() #SPORTS
#driver.find_element(By.ID, "hobbies-checkbox-2").click() #READING


#--- dropdown---

element= driver.find_element(By.ID, "state")
drop = Select(element)

drop.select_by_visible_text('NCR')

#drop.select_by_index(1)

#drop.select_by_value()
driver.quit()
