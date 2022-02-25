
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#.........Launch different browser..................

driver = webdriver.Chrome(executable_path="D:\python\pythonProject\chromedriver.exe") # for chrome browser
#driver = webdriver.Firefox(executable_path="D:\python\pythonProject\geckodriver.exe")  # for mozila firefox
#driver = webdriver.Ie(executable_path="D:\python\pythonProject\IEDriverServer.exe")   # for Internet explorer

driver.get("https://bdtickets.com/")
print(driver.title)  # Title of the page
print(driver.current_url) # Url of the page
driver.find_element( "//*[@id='navbarSupportedContent']/ul[1]/div/a/span").click()
time.sleep(5)
driver.close()
