import unittest


def setUpModule():  # Will be executed before executing any class or any method present in the test class
    print("setUpModule")


def tearDownModule():  # Will be executed after completing everything present in the class or any method present in the test class
    print("setUpModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):  # It's execute at the beginning of each test method in the class
        print("This is login test")

    @classmethod
    def tearDown(self):  # It's execute at the end of each test method in the class
        print("This is logout test")

    @classmethod
    def setUpClass(cls):  # It's Only one time before starting all the method in the class.
        print("Open App\n")

    @classmethod
    def tearDownClass(cls):  # It's Only one time after  completing all the method in the class.
        print("Close App")

    def test_Search(self):
        print("This is search test")

    def test_advancesearch(self):
        print("This is advancesearch test")

    def test_prepaidrecharge(self):
        print("This is prepaidrecharge test")

    def test_postpaidrecharge(self):
        print("This is postpaidrecharge test")


# To execute all the test create inside the class
if __name__ == "__main__":
    unittest.main()
