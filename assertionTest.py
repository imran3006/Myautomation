import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_google(self):
        driver = webdriver.Chrome(executable_path='D:\python\pythonProject\chromedriver.exe')
        driver.get("https://www.google.com/")
        titleOfWebpage= driver.title

        #assertequal
        #self.assertEqual("Google",titleOfWebpage, "Title is not same" )
        #self.assertNotEqual("Googl1123", titleOfWebpage )
        #self.assertTrue(titleOfWebpage == 'Google')  #using expression. More than 2 parameter we use assertionTrue
        self.assertFalse(titleOfWebpage == 'Google123')


if __name__ == "__main__":
    unittest.main()

