import unittest


class PaymentTest(unittest.TestCase):

    def test_PaymentDollar(self):
        print("This is payment in Dollar")
        self.assertTrue(True)

    def test_PaymentEuro(self):
        print("This is euro in Dollar")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
