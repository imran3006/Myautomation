import unittest

def setUpModule():  # will be executed before any classes or method present
    print("setUpModule")

def tearDownModule():  # will be executed after any classes or method present
    print("tearDownModule")



class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):   # setup method will execute the statement within it before every test case method
        print("This is it ")
    @classmethod
    def tearDown(self):   # teardown method will execute after each test method
        print("This is done ")

    @classmethod
    def setUpClass(cls):
        print(" This is opening ")
    @classmethod
    def tearDownClass(cls):
        print("This is ending ")


    def test_search(self):
        print("This is search test ")

    def test_advancesearch(self):
        print("This is Advance search test ")

    def test_prepaidRecharge(self):
        print("This is prepaid Reacharge test ")

    def test_postpaidRecharge(self):
        print("This is postpaid Reacharge test ")


if __name__ == "__main__":
    unittest.main()
