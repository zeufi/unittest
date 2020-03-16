import unittest


class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_Search(self):
        print("This is search test")

    @unittest.skip("I skipping this method for test")
    def test_advancesearch(self):
        print("This is advancesearch test")

    @unittest.skipIf(1 == 1, "numbers are not equal")
    def test_prepaidrecharge(self):
        print("This is prepaidrecharge test")

    def test_postpaidrecharge(self):
        print("This is postpaidrecharge test")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")


if __name__ == "__main__":
    unittest.main()
