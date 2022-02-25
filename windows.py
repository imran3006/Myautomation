import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
print(driver.current_window_handle) # provide the value of current window
handles= driver.window_handles # return to a variable of all the handles  values of browser windows
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(2)
    if driver.title=='Selenium':
        driver.close()       # close only selected browser


driver.quit()                # close all the browser