import unittest

class Apptesting(unittest.TestCase):
    @unittest.SkipTest  #decorator
    def test_search(self):
        print("This is search test ")
    @unittest.skip("I am skipping this as it is not ready yet")  #skip with reason
    def test_advancesearch(self):
        print("This is Advance search test ")
    @unittest.skipIf(1==1, "Numbers are not equal")  #skip with condition
    def test_prepaidRecharge(self):
        print("This is prepaid Reacharge test ")

    def test_postpaidRecharge(self):
        print("This is postpaid Reacharge test ")

if __name__ == "__main__":
    unittest.main
