import unittest


class Logintest(unittest.TestCase):

    def test_loginbyemail(self):
        print("login by email pass")
        self.assertTrue(True)

    def test_loginbyfacebook(self):
        print("login by facebook pass")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("login by twitter pass")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
