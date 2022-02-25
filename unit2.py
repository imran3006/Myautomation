import unittest
from selenium import webdriver

class SesrchEngineTest(unittest.TestCase):
    def test_google(self):
        # here the below code is to find the driver path using this method object
        self.driver = webdriver.Chrome(executable_path='D:\python\pythonProject\chromedriver.exe')
        self.driver.get("https://www.google.com/")
        print("Title of the page is :" + self.driver.title)
        self.driver.close()
    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path='D:\python\pythonProject\chromedriver.exe')
        self.driver.get("https://www.bing.com/")
        print("Title of the page is :" + self.driver.title)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
